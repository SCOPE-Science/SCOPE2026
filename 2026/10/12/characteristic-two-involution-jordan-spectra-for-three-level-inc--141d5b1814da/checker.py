"""Reproduce rank-refined counts of square-zero matrices in a three-layer incidence algebra.
Only the standard library is needed. Run: python3 checker.py
"""
from itertools import product
from math import prod


def mul(a,b,q):
    if q != 4:
        return (a*b)%q
    a0,a1=a&1,a>>1; b0,b1=b&1,b>>1
    x=(a0*b0)^(a1*b1)
    y=(a0*b1)^(a1*b0)^(a1*b1)
    return x|(y<<1)

def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def inv(a,q):
    assert a
    for b in range(1,q):
        if mul(a,b,q)==1:return b
    raise ValueError

def rank(rows,q):
    if not rows:return 0
    v=[row[:] for row in rows];m=len(v);n=len(v[0]);k=0
    for j in range(n):
        t=next((i for i in range(k,m) if v[i][j]),None)
        if t is None:continue
        v[k],v[t]=v[t],v[k]
        z=inv(v[k][j],q);v[k]=[mul(z,h,q) for h in v[k]]
        for i in range(k+1,m):
            if v[i][j]:
                z=v[i][j];v[i]=[add(v[i][h], (-mul(z,v[k][h],q))%q if q!=4 else mul(z,v[k][h],q), q) for h in range(n)]
        k+=1
        if k==m:break
    return k

def gaussian(n,k,q):
    if not 0<=k<=n:return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def matcount(m,n,r,q):
    return gaussian(m,r,q)*prod(q**n-q**i for i in range(r))

def formula(a,b,c,q):
    counts={}
    for r in range(min(a,b)+1):
        for s in range(min(b-r,c)+1):
            pref=matcount(a,b,r,q)*matcount(b-r,c,s,q)*q**(r*c+(a-r)*s)
            for t in range(min(a-r,c-s)+1):
                z=r+s+t
                counts[z]=counts.get(z,0)+pref*matcount(a-r,c-s,t,q)
    return {k:v for k,v in sorted(counts.items()) if v}

def exhaustive(a,b,c,q):
    n=a+b+c; coords=[(i,j) for i in range(n) for j in range(n) if (i<a and a<=j<n) or (a<=i<a+b and a+b<=j<n)]
    out={};total=0
    for values in product(range(q),repeat=len(coords)):
        mat=[[0]*n for _ in range(n)]
        for (i,j),v in zip(coords,values):mat[i][j]=v
        # General-field computation, no characteristic assumptions.
        valid=True
        for i in range(n):
            for j in range(n):
                z=0
                for k in range(n):z=add(z,mul(mat[i][k],mat[k][j],q),q)
                if z:valid=False;break
            if not valid:break
        if valid:
            r=rank(mat,q);out[r]=out.get(r,0)+1;total+=1
    return dict(sorted(out.items()))

def main():
    cases=[(1,1,1,2),(1,2,1,2),(2,1,2,2),(2,2,1,2),(2,2,2,2),
           (1,1,1,3),(1,2,1,3),(1,1,1,4),(1,2,1,4),(2,2,1,4)]
    for a,b,c,q in cases:
        got=exhaustive(a,b,c,q);expected=formula(a,b,c,q)
        assert got==expected,(a,b,c,q,got,expected)
        print('PASS',a,b,c,q,got)
    print('VERIFY_OK')
if __name__=='__main__':main()
