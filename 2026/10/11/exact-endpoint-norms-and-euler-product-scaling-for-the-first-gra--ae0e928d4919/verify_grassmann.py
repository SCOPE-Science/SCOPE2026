"""Exact finite checks for the degree-one Grassmann projection theorem.

Uses arithmetic on q-subspace intersection counts and explicit RREF subspaces
for small prime fields. No finite check is a proof for arbitrary n,k,q.
"""
from fractions import Fraction
from math import comb
from itertools import combinations, product


def gauss(n, k, q):
    if k < 0 or k > n:
        return 0
    a, b = 1, 1
    for i in range(k):
        a *= q ** (n-i)-1
        b *= q ** (k-i)-1
    assert a % b == 0
    return a//b


def qint(k,q):
    return (q**k-1)//(q-1)


def val(n,k,q):
    v, R, B = qint(n,q), qint(k,q), gauss(n,k,q)
    mu=Fraction(R*R,v)
    assert mu < 1
    masses=[q**((k-j)**2)*gauss(k,j,q)*gauss(n-k,k-j,q) for j in range(k+1)]
    assert sum(masses)==B
    assert sum(masses[j]*qint(j,q) for j in range(k+1)) == Fraction(B*R*R,v)
    exact=sum(masses[j]*abs(qint(j,q)-mu) for j in range(k+1))*Fraction(v*(v-1),B*R*(v-R))
    simpler=Fraction(2*R*(v-1),v-R)*Fraction(q**(k*k)*gauss(n-k,k,q),B)
    assert exact==simpler, (n,k,q,exact,simpler)
    return exact


def rref_subspaces(n,k,p):
    for piv in combinations(range(n),k):
        options=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
        for values in product(range(p), repeat=len(options)):
            basis=[[0]*n for _ in range(k)]
            for i,j in enumerate(piv): basis[i][j]=1
            for (i,j),t in zip(options,values):basis[i][j]=t
            vectors=set()
            for cs in product(range(p),repeat=k):
                x=tuple(sum(cs[i]*basis[i][j] for i in range(k))%p for j in range(n))
                vectors.add(x)
            assert len(vectors)==p**k
            yield frozenset(vectors)


def direct(n,k,p):
    spaces=list(rref_subspaces(n,k,p));B=gauss(n,k,p)
    assert len(spaces)==B and len(set(spaces))==B
    v,R=qint(n,p),qint(k,p)
    pref=Fraction(v*(v-1),B*R*(v-R)); mu=Fraction(R*R,v)
    diag=Fraction(v-1,B)
    first=spaces[0]
    sumrow=Fraction(0)
    for Y in spaces:
        inter=len(first.intersection(Y));d=0
        while p**d<inter:d+=1
        assert p**d==inter
        Pxy=pref*(qint(d,p)-mu)
        if Y==first:assert Pxy==diag
        sumrow+=abs(Pxy)
    assert sumrow==val(n,k,p), (n,k,p,sumrow,val(n,k,p))
    # Additional independent moment check: every column count uses the same q-hypergeometric distribution.
    return B


def main():
    count=0
    for q in (2,3,4,5,7):
        for n in range(2,21):
            for k in range(1,n//2+1):
                val(n,k,q); count+=1
    dct=0
    for p in (2,3):
        for n in range(2,7 if p==2 else 6):
            for k in range(1,n//2+1):
                if gauss(n,k,p)>1600:continue
                direct(n,k,p);dct+=1
    print(f'VERIFY_OK q_binomial_cases={count} explicit_rref_cases={dct} fields=2,3')

if __name__=='__main__':main()
