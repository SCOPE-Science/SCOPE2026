"""Finite abelian-torsion orbit arithmetic for one-nodal maximal genus-two curves."""
from collections import Counter

def matmul(A,B,n):
    return ((A[0]*B[0]+A[1]*B[2])%n,(A[0]*B[1]+A[1]*B[3])%n,
            (A[2]*B[0]+A[3]*B[2])%n,(A[2]*B[1]+A[3]*B[3])%n)
def generated(n,gens):
    eye=(1,0,0,1)
    seen={tuple(x%n for x in eye)}
    active=list(seen)
    for X in active:
        for g in gens:
            Y=matmul(X,g,n)
            if Y not in seen:
                seen.add(Y);active.append(Y)
    return seen

def action(A,D,n):
    a,b,c,d=A;x,y=D
    return ((a*x+b*y)%n,(c*x+d*y)%n)

def orbit_stats(n,G):
    pts={(x,y) for x in range(n) for y in range(n)}-{(0,0)}
    classes=[]
    while pts:
        D=next(iter(pts))
        orbit={action(g,D,n) for g in G}
        assert orbit<=pts
        pts-=orbit
        cls=(len(orbit), (D[0]*2%n==0 and D[1]*2%n==0))
        classes.append(cls)
    return Counter(classes)

def run(p,s,kind):
    n=s-1
    minus=(-1,0,0,-1)
    I=(-0,-1,1,0)
    U6=(0,-1,1,1)
    if kind=='general':G=generated(n,[minus]); order=2
    elif kind=='j1728':G=generated(n,[I]);order=4
    elif kind=='j0':G=generated(n,[U6]);order=6
    else:
        A=(0,-1,1,-1)
        B=None
        for a in range(n):
            for b in range(n):
                if (a*a+a*b+b*b+1)%n==0:
                    B=(a,b,a+b,-a);break
            if B is not None:break
        assert B is not None
        G=generated(n,[A,B]);order=12
    counts=orbit_stats(n,G)
    # For non-2-torsion, stabilizers in U up to sign have size 2*|U|/orbit_size
    # because +D,-D are distinct. For order-2 D, two affine lifts are possible.
    by_aut=Counter()
    for (orb_len,is2),multiplicity in counts.items():
        if is2:
            aut=2*order//orb_len
        else:
            aut=2*order//orb_len
        by_aut[aut]+=multiplicity
    return len(G),len(counts),sum(counts.values()),dict(sorted(by_aut.items()))

cases=[(13,13,'general'),(17,17,'j0'),(11,11,'j1728'),(5,5,'j0'),(7,7,'j1728'),(3,3,'wild3'),(3,9,'wild3'),(3,27,'wild3'),(5,25,'j0')]
for p,s,kind in cases:
    observed=run(p,s,kind)
    n=s-1
    if kind=='general':expected=n*n//2+1
    elif kind=='j1728':expected=n*n//4+1
    elif kind=='j0':expected=(n*n+2+4*(n%3==0))//6
    else:expected=(n*n+8)//12
    assert observed[0]== {'general':2,'j1728':4,'j0':6,'wild3':12}[kind] or (p==3 and n==2 and observed[0]==6)
    assert observed[2]==expected,(p,s,kind,observed,expected)
    print(p,s,kind,'n',n,'group effective',observed[0],'orbits',observed[2], 'by Aut order',observed[3])
print('ALL_ORBIT_CHECKS_PASSED')
