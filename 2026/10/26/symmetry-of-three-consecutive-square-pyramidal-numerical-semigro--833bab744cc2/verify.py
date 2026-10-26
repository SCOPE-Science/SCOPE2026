"""Independent finite checks for three consecutive square-pyramidal numerical semigroups."""
from heapq import heappush, heappop
from math import gcd


def pyramid(n):
    return n*(n+1)*(2*n+1)//6


def apery_invariants(values):
    a=min(values)
    dist=[None]*a
    dist[0]=0
    pq=[(0,0)]
    while pq:
        w,r=heappop(pq)
        if w!=dist[r]:
            continue
        for x in values:
            nr=(r+x)%a
            nw=w+x
            if dist[nr] is None or nw<dist[nr]:
                dist[nr]=nw
                heappush(pq,(nw,nr))
    assert all(w is not None for w in dist)
    F=max(dist)-a
    g=(sum(dist)//a)-(a-1)//2
    # Correct for even a: sum(dist)/a -(a-1)/2; integer via doubled expression.
    g=(2*sum(dist)-a*(a-1))//(2*a)
    symmetric=(2*g==F+1)
    return F,g,symmetric


def gluing_membership(values,i):
    u,v=[values[j] for j in range(3) if j!=i]
    w=values[i]
    d=gcd(u,v)
    if d==1:
        return False
    U,V=u//d,v//d
    # A linear Diophantine membership test, using modular inversion.
    if U==1 or V==1:
        return True
    # Solve xU+yV=w with 0<=x<V, nonnegative y.
    x=(w*pow(U,-1,V))%V
    return w>=x*U and (w-x*U)%V==0


def frobenius_formula(n):
    return (4*n**5+32*n**4+101*n**3+175*n**2+102*n-36)//36


def main():
    apery_cases=0
    for n in range(1,41):
        abc=[pyramid(n+i) for i in range(3)]
        assert gcd(gcd(*abc[:2]),abc[2])==1
        predicted=(n in (1,2) or n%6 in (0,4))
        F,g,symmetric=apery_invariants(abc)
        assert symmetric==predicted,(n,'symmetry',F,g)
        if n%6 in (0,4):
            assert F==frobenius_formula(n),(n,'frobenius',F)
            assert g==(F+1)//2
        if n==1:
            assert (F,g)==(-1,0)
        if n==2:
            assert (F,g)==(51,26)
        if n>=3:
            # All three generators are minimal for n>=3.
            a,b,c=abc
            assert not any(c==x*a+y*b for x in range(c//a+1) for y in range((c-x*a)//b+1))
            assert (gluing_membership(abc,2)==(n%6 in (0,4)))
            assert not gluing_membership(abc,0)
            assert not gluing_membership(abc,1)
        apery_cases+=1
    algebraic_cases=0
    for n in range(3,10001):
        abc=[pyramid(n+i) for i in range(3)]
        a,b,c=abc
        assert gcd(a,b)==(n+1)//gcd(n+1,6)
        assert gcd(b,c)==(n+2)//gcd(n+2,6)
        assert gcd(a,c) in (1,5)
        assert (n+1)*c==(n+2)*a+5*b
        assert gluing_membership(abc,2)==(n%6 in (0,4))
        assert not gluing_membership(abc,0)
        assert not gluing_membership(abc,1)
        algebraic_cases+=1
    print(f'VERIFY_OK: {apery_cases} independent Apery/Frobenius/genus cases, '
          f'{algebraic_cases} exact gcd/recurrence/gluing cases, all three gluing orientations.')

if __name__=='__main__':
    main()
