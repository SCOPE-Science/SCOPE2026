"""Exact-rational checks for the equilateral farthest-projection theorem.

All coordinates are exact: (a,b) denotes (a, sqrt(3)*b).
No floating-point decisions occur in the geometric tests.
"""
from fractions import Fraction as F
from math import floor, log

V = ((F(0), F(0)), (F(2), F(0)), (F(1), F(1)))
D = tuple(tuple(V[(i+1)%3][j] - V[i][j] for j in (0,1)) for i in range(3))


def add(a, b): return (a[0]+b[0], a[1]+b[1])
def sub(a, b): return (a[0]-b[0], a[1]-b[1])
def scale(t, a): return (t*a[0], t*a[1])
def dot(a, b): return a[0]*b[0] + 3*a[1]*b[1]

def geometric_step(i, t):
    x = add(V[i], scale(t,D[i]))
    options=[]
    for j in range(3):
        if j==i:continue
        s=dot(sub(x,V[j]),D[j])/dot(D[j],D[j])
        y=add(V[j],scale(s,D[j]))
        options.append((dot(sub(x,y),sub(x,y)),j,s))
    a,b=options
    if a[0]==b[0]:return i,t
    return (a[1],a[2]) if a[0]>b[0] else (b[1],b[2])

def symbolic_step(i,t):
    if t==F(1,2): return i,t
    if t<F(1,2): return ((i+1)%3, (1-t)/2)
    return ((i-1)%3, 1-t/2)

def exceptional(t,lim=10):
    if t==F(1,2): return True
    for k in range(lim):
        z=4**k
        if t in (F(z),F(2*z),F(1-z),F(1-2*z)):
            return True
    return False

def exact_basin(t):
    if exceptional(t,15):return 'E'
    if 0<t<F(1,2):return 'L'
    if F(1,2)<t<1:return 'H'
    if t>1:
        z=F(t)
        while z>1:z/=4
        return 'L' if z<F(1,2) else 'H'
    if t<0:
        u=1-t
        while u>1:u/=4
        z=1-u
        return 'L' if z<F(1,2) else 'H'
    raise AssertionError(t)

def limb(t):
    for _ in range(60):
        if t==F(1,2):return 'E'
        if 0<t<F(1,2):return 'L'
        if F(1,2)<t<1:return 'H'
        if t<F(1,2):t=(1-t)/2
        else:t=1-t/2
    raise AssertionError('unclassified')

n=0
for d in range(1,14):
    for q in range(-600,601):
        t=F(q,d)
        for i in range(3):
            assert geometric_step(i,t)==symbolic_step(i,t),(i,t)
            n+=1
        assert exact_basin(t)==limb(t),(t,exact_basin(t),limb(t))

for i in range(3):
    for t in (F(1,3),F(2,3)):
        z=(i,t)
        for _ in range(3):z=symbolic_step(*z)
        assert z==(i,t)
    assert symbolic_step(i,F(1,2))==(i,F(1,2))

for k in range(10):
    for t in (F(4**k),F(2*4**k),F(1-4**k),F(1-2*4**k)):
        assert limb(t)=='E'

# Partition lengths of L and H over [0,R] from an independent
# interval union, including every branch shell touching [0,R].
def union_L_length(R):
    intervals=[(F(0),F(1,2))]
    for j in range(20):
        lo=F(4**j);hi=2*lo
        if lo>R:break
        intervals.append((lo,hi))
    return sum(max(F(0),min(R,b)-max(F(0),a)) for a,b in intervals)

def closed_length(R):
    if R<=1: return min(R,F(1,2))
    z=F(1);m=0
    while z*4<=R:z*=4;m+=1
    return z/3+F(1,6)+min(R-z,z)

for den in range(1,13):
    for num in range(1,400):
        R=F(num,den)
        assert union_L_length(R)==closed_length(R),(R,union_L_length(R),closed_length(R))

print('PASS exact geometric comparisons:',n)
print('PASS complete rational state basin checks:',13*1201)
print('PASS exact one-sided measure comparisons:',12*399)
print('PASS periodic and exceptional state checks')
