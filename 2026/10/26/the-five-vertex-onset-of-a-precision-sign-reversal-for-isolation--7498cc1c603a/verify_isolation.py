"""Exact arithmetic verification of a vertex-isolation partial-correlation theorem.

Requires only the Python 3 standard library. This verifies finite symbolic
certificates and finite enumeration, not a separate proof of the general theorem.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb


def add(a,b):
    n=max(len(a),len(b));return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n))
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tuple(c)
def coeff_binomial(d):
    # Polynomial [d]_(1+u) = sum_{k=0}^{d-1} (1+u)^k.
    return tuple(sum(comb(k,j) for k in range(j,d)) for j in range(d))
def det_poly(A):
    n=len(A); out=(0,)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=(1,)
        for i in range(n):term=mul(term,A[i][perm[i]])
        if inversions%2:term=tuple(-v for v in term)
        out=add(out,term)
    return tuple(out)
def cofactor_poly(B,i,j):
    # Matrix adjugate_{ij} is cofactor_{ji}.
    sub=[[B[r][c] for c in range(len(B)) if c!=i] for r in range(len(B)) if r!=j]
    v=det_poly(sub)
    if (i+j)%2:v=tuple(-c for c in v)
    return v

def connected(n,edges):
    seen={0}; changed=True
    while changed:
        changed=False
        for a,b in edges:
            if a in seen and b not in seen:seen.add(b);changed=True
            if b in seen and a not in seen:seen.add(a);changed=True
    return len(seen)==n

def B_poly(n,edges):
    deg=[0]*n
    for i,j in edges:deg[i]+=1;deg[j]+=1
    E=set(edges)
    return [[coeff_binomial(deg[i]) if i==j else ((1,) if (min(i,j),max(i,j)) in E else (0,)) for j in range(n)] for i in range(n)]

def invert_fraction(A):
    n=len(A); T=[[Fraction(x) for x in A[i]]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if T[k][j])
        T[k],T[j]=T[j],T[k]
        fac=T[j][j];T[j]=[x/fac for x in T[j]]
        for i in range(n):
            if i==j:continue
            fac=T[i][j]
            T[i]=[T[i][k]-fac*T[j][k] for k in range(2*n)]
    return [row[n:] for row in T]

def graph_covariance(n,edges,p):
    q=1-p;degree=[0]*n;edges=set(edges)
    for i,j in edges:degree[i]+=1;degree[j]+=1
    a=[q**d for d in degree]
    return [[a[i]*(1-a[i]) if i==j else (a[i]*a[j]*p/q if (min(i,j),max(i,j)) in edges else Fraction(0)) for j in range(n)] for i in range(n)]

def verify():
    assertions=0;count={}
    for n in (3,4):
        possible=list(combinations(range(n),2)); total=0
        for mask in range(1<<len(possible)):
            edges=[possible[k] for k in range(len(possible)) if mask>>k&1]
            if not connected(n,edges):continue
            total+=1;B=B_poly(n,edges)
            # Every off-diagonal adjugate polynomial has one sign on u>0,
            # witnessed by all coefficients having a common weak sign.
            for i,j in possible:
                cof=cofactor_poly(B,i,j)
                assert all(v>=0 for v in cof) or all(v<=0 for v in cof),(n,edges,i,j,cof)
                assert any(v for v in cof),(n,edges,i,j,'zero polynomial')
                assertions+=2
            d=det_poly(B)
            assert all(v>=0 for v in d) and any(v>0 for v in d)
            assertions+=1
        assert total=={3:4,4:38}[n];count[n]=total;assertions+=1

    for r in range(1,11):
        n=r+2;edges=[(0,1)]+[(0,k) for k in range(2,n)]+[(1,k) for k in range(2,n)]
        for p in (Fraction(1,7),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(9,10)):
            cov=graph_covariance(n,edges,p)
            inv=invert_fraction(cov)
            q=1-p;t=1/q
            h=sum(t**j for j in range(r+1))
            rho=(t+1-r)/((t+1)*h-r)
            assert -inv[0][1]/inv[0][0]==rho,(r,p,inv[0][1],rho)
            assert inv[0][0]==inv[1][1]
            assert cov[0][1]>0
            assertions+=3

    # Verify the pivotal book graph directly, summing 2^7 edge states.
    r=3;n=r+2;edges=[(0,1)]+[(0,k) for k in range(2,n)]+[(1,k) for k in range(2,n)]
    for p,rho_expected in [(Fraction(1,4),Fraction(-27,491)),(Fraction(1,2),Fraction(0)),(Fraction(3,4),Fraction(1,211))]:
        q=1-p;prob=[Fraction(0)]*n;mom=[[Fraction(0)]*n for _ in range(n)]
        for state in product((0,1),repeat=len(edges)):
            m=sum(state);w=p**m*q**(len(edges)-m)
            deg=[0]*n
            for s,(i,j) in zip(state,edges):
                if s:deg[i]+=1;deg[j]+=1
            z=[int(d==0) for d in deg]
            for i in range(n):
                prob[i]+=w*z[i]
                for j in range(n):mom[i][j]+=w*z[i]*z[j]
        cov=[[mom[i][j]-prob[i]*prob[j] for j in range(n)] for i in range(n)]
        expected=graph_covariance(n,edges,p)
        assert cov==expected
        inv=invert_fraction(cov)
        assert -inv[0][1]/inv[0][0]==rho_expected
        assertions+=2
    return assertions,count

if __name__=='__main__':
    n,g=verify();print('PASS:',n,'exact assertions; connected labeled graphs:',g,'; full enumeration: 128 configurations per probability')
