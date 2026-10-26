#!/usr/bin/env python3
"""Exact finite checks for derivations of prime-order Latin Alexander quandle algebras.

Uses only Python standard library. These computations corroborate, but do not prove,
the stated theorem for arbitrary finite abelian groups.
"""

def prime_factors(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1: out.append(n)
    return out

def primitive_root(p):
    factors=prime_factors(p-1)
    return next(g for g in range(1,p) if all(pow(g,(p-1)//r,p)!=1 for r in factors))

def rank_mod(rows, ncols, ell=1009):
    piv={}
    for row in rows:
        v={j:x%ell for j,x in row.items() if x%ell}
        while v:
            j=min(v)
            if j in piv:
                a=v[j]
                for k,b in piv[j].items():
                    z=(v.get(k,0)-a*b)%ell
                    if z: v[k]=z
                    elif k in v: del v[k]
            else:
                inv=pow(v[j],-1,ell)
                piv[j]={k:(a*inv)%ell for k,a in v.items()}
                break
    return len(piv)

def mult_rule(p,t):
    inv=pow(t,-1,p)
    return [(i*inv)%p for i in range(p)],[(i*(1-t)*inv)%p for i in range(p)]

def full_derivation_equations(p,t):
    tau,sigma=mult_rule(p,t)
    for i in range(p):
        for j in range(p):
            for k in range(p):
                v={}
                def add(key,coef):
                    v[key]=v.get(key,0)+coef
                    if not v[key]:del v[key]
                # Variables are indexed as D[input, output].
                if j==sigma[i]:add(tau[i]*p+k,1)
                for a in range(p):
                    if j==sigma[a] and tau[a]==k:add(i*p+a,-1)
                if tau[i]==k:add(j*p+sigma[i],-1)
                if v:yield v

def diagonal_equations(p,t):
    for j in range(p):
        v={}
        for i,c in [(j,1),((t*j)%p,-1),(((1-t)*j)%p,-1)]:
            v[i]=v.get(i,0)+c
            if not v[i]:del v[i]
        if v:yield v

def multiplicative_char_dim(p,t):
    if (p-1)%6:return 0
    g=int(primitive_root(p)); logs={pow(g,k,p):k for k in range(p-1)}
    a,b=logs[t],logs[(1-t)%p];n=p-1
    return sum(((k*a)%n,(k*b)%n) in ((n//6,5*n//6),(5*n//6,n//6)) for k in range(n))

if __name__=='__main__':
    tested=0
    for p,ts in [(3,[2]),(5,[2,3,4]),(7,[2,3,4,5,6]),(11,[2,3,5]),(13,[2,4,10])]:
        for t in ts:
            predicted=multiplicative_char_dim(p,t)
            diag=p-rank_mod(diagonal_equations(p,t),p)
            assert predicted==diag,(p,t,predicted,diag)
            if p<=7:
                full=p*p-rank_mod(full_derivation_equations(p,t),p*p)
                assert full==diag,(p,t,full,diag)
            print(f'prime={p} parameter={t} derivation_dimension={diag}')
            tested+=1
    print('VERIFY_OK cases=',tested)
