"""Independent rational-parametrization and pair-generated-line verification.

No external packages. Every field element is a base-three polynomial residue.
Run: python3 check_parameter.py
"""
from collections import Counter, defaultdict
from itertools import combinations


def compute(r, modulus, expected):
    q = 3 ** r
    powers = [3 ** j for j in range(r)]
    digits = [[(n // powers[j]) % 3 for j in range(r)] for n in range(q)]

    def code(coeff):
        return sum((coeff[j] % 3) * powers[j] for j in range(r))

    def add(a, b):
        return code([digits[a][j] + digits[b][j] for j in range(r)])

    def neg(a):
        return code([-t for t in digits[a]])

    def mul(a, b):
        poly = [0] * (2 * r - 1)
        for i in range(r):
            for j in range(r):
                poly[i+j] += digits[a][i] * digits[b][j]
        for k in range(2*r-2, r-1, -1):
            c = poly[k] % 3
            for j in range(r):
                poly[k-r+j] -= c * modulus[j]
        return code(poly[:r])

    def power(a, e):
        p = 1
        while e:
            if e & 1: p = mul(p, a)
            a = mul(a, a)
            e //= 2
        return p

    inverses = {}
    for a in range(1,q):
        inverses[a] = next(b for b in range(1,q) if mul(a,b)==1)

    def direct(x,y):
        # Equation Y^4-(X^3+X)+(Y^2-2X)^2=0 in characteristic three.
        k=add(power(y,2),neg(mul(2,x)))
        return add(add(add(power(y,4),neg(power(x,3))),neg(x)),power(k,2))

    direct_points={(x,y,1) for x in range(q) for y in range(q) if direct(x,y)==0}
    direct_points.add((1,0,0))
    parameter_points=set()
    for t in range(q):
        x=mul(2,power(add(t,1),4))
        y=add(2,add(t,power(t,3)))
        assert direct(x,y)==0
        parameter_points.add((x,y,1))
    parameter_points.add((1,0,0))
    # The three rational nodes can be absent from the F_{3^odd}-rational normalization.
    for p in [(1,1,1),(1,2,1),(2,0,1)]:
        assert direct(p[0],p[1])==0
        parameter_points.add(p)
    assert parameter_points==direct_points
    P=sorted(parameter_points)

    def cross(p,t):
        ax=add(mul(p[1],t[2]),neg(mul(p[2],t[1])))
        ay=add(mul(p[2],t[0]),neg(mul(p[0],t[2])))
        az=add(mul(p[0],t[1]),neg(mul(p[1],t[0])))
        vv=(ax,ay,az)
        z=next(w for w in vv if w)
        return tuple(mul(inverses[z],w) for w in vv)

    L=defaultdict(set)
    for i,j in combinations(range(len(P)),2):
        L[cross(P[i],P[j])].update([i,j])
    four={l for l,points in L.items() if len(points)==4}
    ambient=[(x,y,1) for x in range(q) for y in range(q)] + [(1,y,0) for y in range(q)] + [(0,1,0)]
    def inc(l,p):
        return add(add(mul(l[0],p[0]),mul(l[1],p[1])),mul(l[2],p[2]))==0
    count=Counter()
    offcount=Counter()
    for p in ambient:
        n=sum(inc(l,p) for l in four)
        count[n]+=1
        if p not in parameter_points: offcount[n]+=1
    answer=(len(P),len(four),offcount[0],dict(count),dict(offcount))
    assert answer==expected, (r,answer,expected)
    assert sum(count.values())==q*q+q+1
    print(f"F_{q}: points={len(P)} four_secants={len(four)} off_uncovered={offcount[0]}")
    print("PARAM_OK", r)


compute(3,[1,0,2],(31,24,282,{0:289,1:312,2:132,4:24},{0:282,1:312,2:132}))
compute(4,[1,0,1,1],(79,204,108,{0:111,1:1332,2:2496,3:1248,4:1134,5:240,10:72,18:6,24:4},{0:108,1:1332,2:2496,3:1248,4:1134,5:240,18:6}))
