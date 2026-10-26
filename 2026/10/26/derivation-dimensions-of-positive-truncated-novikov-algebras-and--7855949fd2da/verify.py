#!/usr/bin/env python3
"""Independent linear-equation checks for truncated polynomial Novikov derivations.
Standard library only. No computational check substitutes for the written all-n proof.
"""
from fractions import Fraction

def prod(n,i,j):
    k=i+j-1
    return (j,k) if k<=n else (0,0)

def dimension(n,p):
    # Coefficient constraints of D(a circle b)=(Da) circle b+a circle(Db).
    # Variables are column entries D(e_col)_{row}, indices start at one.
    piv={}
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                row={}
                v,t=prod(n,i,j)
                if v:
                    idx=(t-1)*n+(k-1)
                    row[idx]=row.get(idx,0)+v
                for a in range(1,n+1):
                    v,t=prod(n,a,j)
                    if v and t==k:
                        idx=(i-1)*n+(a-1)
                        row[idx]=row.get(idx,0)-v
                    v,t=prod(n,i,a)
                    if v and t==k:
                        idx=(j-1)*n+(a-1)
                        row[idx]=row.get(idx,0)-v
                if p:
                    row={c:v%p for c,v in row.items() if v%p}
                else:
                    row={c:Fraction(v) for c,v in row.items() if v}
                while row:
                    c=min(row)
                    if c not in piv:
                        if p: 
                            inv=pow(row[c],-1,p)
                            piv[c]={key:val*inv%p for key,val in row.items()}
                        else:
                            inv=1/row[c]
                            piv[c]={key:val*inv for key,val in row.items()}
                        break
                    factor=row[c]
                    for key,val in piv[c].items():
                        new=row.get(key,0)-factor*val
                        if p:new%=p
                        if new:row[key]=new
                        elif key in row:del row[key]
    return n*n-len(piv)

def predicted(n,p):
    if p==0:return 1
    if p==2:
        return (3*(n//2) - (n//2)%2) if n%2==0 else 3*(n//2)
    return 1+n//p+(n-2)//p

def valid_map(n,p,Map):
    # Map[(output,input)] is a field coefficient, check all basis pairs.
    for i in range(1,n+1):
        for j in range(1,n+1):
            lhs=[0]*n;rhs=[0]*n
            coef,out=prod(n,i,j)
            if coef:
                for k in range(1,n+1): lhs[k-1]=(coef*Map.get((k,out),0))%p
            for a in range(1,n+1):
                coef,out=prod(n,a,j)
                if coef:rhs[out-1]=(rhs[out-1]+Map.get((a,i),0)*coef)%p
                coef,out=prod(n,i,a)
                if coef:rhs[out-1]=(rhs[out-1]+Map.get((a,j),0)*coef)%p
            if lhs!=rhs: return False,(i,j,lhs,rhs)
    return True,None

def odd_generators(n,p):
    for s in range(0,n):
        if s%p==0 and s<=n-2:
            yield f'A{s}', {(i+s,i):(i-1)%p for i in range(1,n-s+1) if (i-1)%p}
        if (s+1)%p==0:
            yield f'B{s}', {(i+s,i):i%p for i in range(1,n-s+1) if i%p}

def char2_generators(n):
    a=(n+1)//2; b=n//2
    # Odd indices: t u^r, r=0..a-1; even indices: t^2 u^r, r=0..b-1.
    # Delta(u)=u^j, constrained as in proof.
    constant_allowed=(a==b and a%2==0)
    for j in range(0 if constant_allowed else 1,a):
        M={}
        for r in range(1,a):
            out=r-1+j
            if out<a and r%2:M[(2*out+1,2*r+1)]=1
        for r in range(1,b):
            out=r-1+j
            if out<b and r%2:M[(2*out+2,2*r+2)]=1
        yield f'delta_u{j}', M
    # F(a)=v*a from odd to even; F(1)=u^j
    for j in range(b):
        yield f'F{j}', {(2*(r+j)+2,2*r+1):1 for r in range(a) if r+j<b}
    # T(b)=w*b, w=u^j
    for j in range(b):
        yield f'T{j}', {(2*(r+j)+2,2*r+2):1 for r in range(b) if r+j<b}

def main():
    checked=0
    for p in (2,3,5,7,11):
        for n in range(2,15):
            d=dimension(n,p)
            assert d==predicted(n,p),(n,p,d,predicted(n,p))
            generators=list(char2_generators(n) if p==2 else odd_generators(n,p))
            assert len(generators)==d,(n,p,d,len(generators))
            for name,m in generators:
                ok,details=valid_map(n,p,m)
                assert ok,(n,p,name,details)
            checked+=1
    for n in range(2,9):
        assert dimension(n,0)==1,(n,dimension(n,0))
    assert dimension(16,2)==24
    assert dimension(17,2)==24
    print('NOVIKOV_DERIVATION_CENSUS_OK', 'positive_characteristic_cases=',checked,
          'characteristic_zero_cases=',7,'extra_mod_four_cases=2')
if __name__=='__main__':main()
