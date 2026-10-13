"""Exact arithmetic certificate for the characteristic-five conic-line bridge.
Standard-library Python 3, no external packages or network calls.
"""
from itertools import combinations, product
from math import gcd, isqrt
from functools import reduce
from collections import Counter

L10 = [(1,0,0),(2,2,1),(-2,2,1),(-3,4,0),(3,4,0),(-4,2,5),(4,2,5)]
L4 = [(0,1,0),(-1,1,-1),(1,1,-1),(-1,-1,-1),(1,-1,-1)]
UV = [((0,1,0),(0,0,1)),((1,-1,0),(0,1,-2)),((1,1,0),(0,1,-2)),((4,3,0),(0,0,1)),((4,-3,0),(0,0,1)),((1,2,0),(0,-5,2)),((1,-2,0),(0,-5,2))]
M = ((0,1,0),(3,0,2),(1,0,3))
EXPECTED = {(0,0,1),(0,1,-2),(0,5,-2),(0,5,6),(4,-7,6),(4,-3,-2),(4,-3,14),(4,3,-14),(4,3,2),(4,7,-6),(20,-15,22),(20,15,-22)}

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(c,a): return tuple(c*x for x in a)
def primitive(a):
    g=reduce(gcd,a)
    assert g
    b=tuple(x//g for x in a)
    return tuple(-x for x in b) if next(x for x in b if x)<0 else b

def q10(a):
    x,y,z=a
    return -4*x*x+12*y*y-4*y*z-5*z*z

def q4(a):
    x,y,z=a
    return x*x+y*y-z*z

def norm(a,p):
    a=tuple(x%p for x in a)
    v=next(x for x in a if x)
    return tuple(x*pow(v,-1,p)%p for x in a)

def strip_small(n):
    n=abs(n)
    for p in (2,3,5):
        while n and n%p==0: n//=p
    return n

assert det(*M)==-7
assert len(set(L10))==7 and len(set(L4))==5
# Enumerate all 21 line intersections and 14 conic-line intersections over Q.
pts=set()
for a,b in combinations(L10,2):
    cp=cross(a,b)
    assert cp!=(0,0,0)
    pts.add(primitive(cp))
discs=[]
for (line,(u,v)) in zip(L10,UV):
    assert dot(line,u)==dot(line,v)==0
    assert abs(det(u,v,line))==dot(line,line) or cross(u,v) in (line,scale(-1,line)), (line,u,v)
    a=q10(u); b=q10(add(u,v))-a-q10(v); c=q10(v)
    disc=b*b-4*a*c; root=isqrt(disc)
    assert root*root==disc and a!=0 and disc!=0
    discs.append(disc)
    for sg in (-1,1):
        pt=primitive(add(scale(-b+sg*root,u),scale(2*a,v)))
        assert dot(line,pt)==0 and q10(pt)==0
        pts.add(pt)
assert set(discs)=={256,1024,9216},discs
assert len(pts)==12 and pts==EXPECTED
assert all(strip_small(d)==1 for d in discs)
for a,b,c in combinations(L10,3):
    d=det(a,b,c)
    if d: assert strip_small(d)==1
assert sum(det(*tri)==0 for tri in combinations(L10,3))==5
assert all(strip_small(reduce(gcd,cross(a,b)))==1 for a,b in combinations(pts,2))
# Conic matrix determinant = 256. Therefore all conics smooth for p >= 5.
B10 = ((-4,0,0),(0,12,-2),(0,-2,-5))
assert det(*B10)==256
assert Counter(sum(dot(line,P)==0 for line in L10)+(q10(P)==0) for P in pts)==Counter({2:5,3:4,4:3})
assert all(sum(dot(line,P)==0 for line in L10)+(q10(P)==0)>=2 for P in pts)
assert sum((m*(m-1)//2 for m in [sum(dot(l,P)==0 for l in L10)+(q10(P)==0) for P in pts]))==35
# Every distinct component pair meets among pts; 21 line pairs and 14 line-conic contacts.
assert all(any(dot(a,P)==dot(b,P)==0 for P in pts) for a,b in combinations(L10,2))
assert all(sum(dot(l,P)==0 and q10(P)==0 for P in pts)==2 for l in L10)
# p=5: reductions have exactly five distinct lines; conic still smooth.
R10=list(dict.fromkeys(norm(l,5) for l in L10))
assert len(R10)==5
assert [norm(L10[3],5),norm(L10[4],5)]==[norm(L10[5],5),norm(L10[6],5)]
all_proj = {norm(P,5) for P in product(range(5),repeat=3) if any(P)}
assert len(all_proj)==31
sing=[]
for P in all_proj:
    hit=sum(dot(l,P)%5==0 for l in R10)
    inc=(q10(P)%5==0)
    if hit+inc>=2:
        grad=(-8*P[0],24*P[1]-4*P[2],-4*P[1]-10*P[2])
        assert inc==False or all(norm(grad,5)!=line for line in R10 if dot(line,P)%5==0)
        sing.append((P,hit+int(inc)))
assert len(sing)==6
assert Counter(m for P,m in sing)==Counter({2:2,3:2,4:2})
assert sum(m*(m-1)//2 for P,m in sing)==20
assert all(sum(dot(l,P)%5==0 for P in all_proj if q10(P)%5==0)==2 for l in R10)
# Exact PGL3(F5) projective equivalence with the separate CL4 arrangement.
assert det(*M)%5!=0
# Conic pullback q10(M[U,V,W]) is q4(U,V,W) modulo 5.
for U,V,W in product(range(5),repeat=3):
    input=(U,V,W)
    output=tuple(dot(row,input) for row in M)
    assert (q10(output)-q4(input))%5==0
pullback_lines={norm(tuple(dot(col,l) for col in zip(*M)),5) for l in R10}
assert pullback_lines=={norm(l,5) for l in L4}
# Counterpart CL4 also has six ordinary singularities.
assert Counter(sum(dot(l,P)%5==0 for l in L4)+(q4(P)%5==0) for P in all_proj if sum(dot(l,P)%5==0 for l in L4)+(q4(P)%5==0)>=2)==Counter({2:2,3:2,4:2})
print('VERIFY_OK: integral incidence certificate, all primes >=7, p=5 degeneration, projective CL4 bridge')
