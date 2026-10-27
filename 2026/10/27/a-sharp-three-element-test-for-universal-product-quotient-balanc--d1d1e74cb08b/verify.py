"""Finite checks for the sharp three-element product/quotient witness theorem.
Run with Python 3 standard library: python3 verify.py
"""
from itertools import combinations, product


def abelian(*mods):
    elems = list(product(*(range(m) for m in mods)))
    def mul(x,y): return tuple((a+b)%m for a,b,m in zip(x,y,mods))
    def inv(x): return tuple(-a%m for a,m in zip(x,mods))
    return elems,mul,inv


def dihedral(n):
    elems=list(product(range(n),range(2)))
    def mul(x,y):
        r,e=x; s,f=y
        return ((r+(-s if e else s))%n,(e+f)%2)
    def inv(x):
        r,e=x
        return ((-r if not e else r)%n,e)
    return elems,mul,inv


def quaternion():
    # coordinates (sign, basis) with basis in {1,i,j,k}
    elems=list(product(range(2),range(4)))
    tab=((0,1,2,3), (1,0,3,2), (2,3,0,1), (3,2,1,0))
    sg=((0,0,0,0), (0,1,0,1), (0,1,1,0), (0,0,1,1))
    def mul(x,y):
        (s,i),(t,j)=x,y
        return ((s+t+sg[i][j])%2,tab[i][j])
    def inv(x):
        s,i=x
        return ((s+(i!=0))%2,i)
    return elems,mul,inv


def signature(A,mul,inv):
    return len({mul(x,y) for x in A for y in A}),len({mul(x,inv(y)) for x in A for y in A})


def inspect(G,label,expected_smallest,exhaustive=False):
    elems,mul,inv=G
    n=len(elems)
    for r in (1,2,3):
        witness=None
        for A in combinations(elems,r):
            a,b=signature(A,mul,inv)
            if a!=b:
                witness=(A,(a,b));break
        if witness is not None:
            assert r==expected_smallest,(label,r,expected_smallest,witness)
            found_r = r
            break
    else:
        found_r = None
        assert expected_smallest is None,(label,'unexpectedly universally balanced at size <=3')
    if exhaustive:
        for r in range(n+1):
            for A in combinations(elems,r):
                a,b=signature(A,mul,inv)
                if expected_smallest is None:
                    assert a==b,(label,A,a,b)
    print(label,n,'witness_size',found_r if witness is not None else 'none', 'witness',witness)


def main():
    for n in range(1,17):
        inspect(abelian(n),f'C{n}',None if n<=5 else 3,exhaustive=n<=9)
    for n in (2,3,4,5,6):
        inspect(abelian(*([2]*n)),f'C2^{n}',None,exhaustive=n<=3)
    for mods in ((3,3),(4,2),(5,5),(2,3),(2,4),(2,2,3),(3,3,3),(4,4),(2,2,4)):
        inspect(abelian(*mods),'x'.join(map(str,mods)),3,exhaustive=False)
    for n in range(3,13):
        inspect(dihedral(n),f'D{2*n}',2,exhaustive=n<=5)
    inspect(quaternion(),'Q8',3,exhaustive=True)
    # Explicit abelian witnesses required in the proof.
    for m in range(6,101):
        G=abelian(m)
        e,mu,iv=G
        assert signature(((0,),(1,),(3,)),mu,iv)==((5,6) if m==6 else (6,7)),m
    for mods,want in (((3,3),(6,7)),((5,5),(6,7)),((4,2),(5,6))):
        e,mu,iv=abelian(*mods)
        A=(tuple(0 for _ in mods),(1,0),(0,1))
        assert signature(A,mu,iv)==want,(mods,signature(A,mu,iv))
    print('VERIFY_OK')
if __name__=='__main__': main()
