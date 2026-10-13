"""Exact arithmetic certificate for the singular points of a six-conic, six-line divisor.

Run with Python 3: python verify.py. No third-party packages are required.
"""
from collections import Counter
from functools import reduce
from itertools import combinations
from math import gcd

# Elements of Z[i,sqrt(3)] have coefficient vectors (a,b,c,d), representing
# a+b*i+c*r+d*i*r, where i*i=-1 and r*r=3.
ZERO=(0,0,0,0); ONE=(1,0,0,0); I=(0,1,0,0); R=(0,0,1,0); H=(0,0,0,1)
def number(n): return (int(n),0,0,0)
def add(u,v): return tuple(a+b for a,b in zip(u,v))
def neg(u): return tuple(-a for a in u)
def sub(u,v): return add(u,neg(v))
def scale(k,u): return tuple(k*a for a in u)
def mul(u,v):
    a,b,c,d=u; e,f,g,h=v
    return (a*e-b*f+3*c*g-3*d*h,
            a*f+b*e+3*(c*h+d*g),
            a*g+c*e-b*h-d*f,
            a*h+b*g+c*f+d*e)
def norm(u):
    a,b,c,d=u
    x=a*a+b*b+3*(c*c+d*d)
    y=2*(a*c+b*d)
    return x*x-3*y*y

def support(n):
    n=abs(n); out=set(); d=2
    while d*d<=n:
        if n%d==0:
            out.add(d)
            while n%d==0:n//=d
        d+=1 if d==2 else 2
    if n>1:out.add(n)
    return out

def cross(u,v):
    return (sub(mul(u[1],v[2]),mul(u[2],v[1])),
            sub(mul(u[2],v[0]),mul(u[0],v[2])),
            sub(mul(u[0],v[1]),mul(u[1],v[0])))

def pt(x,y,z):return (x,y,z)
points=[]
for a,b,c in [(0,0,1),(0,1,0),(1,-2,-1),(1,-2,1),
              (1,-1,0),(1,0,-1),(1,0,1)]:
    points.append((f'P({a},{b},{c})',pt(*map(number,(a,b,c)))))
for e in (1,-1):
    i=scale(e,I); r=scale(e,R); h=scale(e,H)
    points += [
      (f'H{e}',pt(number(2),add(number(-1),h),add(number(-1),h))),
      (f'I0{e}',pt(ONE,ZERO,i)),
      (f'I1{e}',pt(sub(number(-1),i),number(2),add(ONE,i))),
      (f'I2{e}',pt(add(number(-1),i),number(2),add(ONE,i))),
      (f'R0{e}',pt(sub(number(-1),r),number(2),add(number(-1),r))),
      (f'R1{e}',pt(add(number(-1),r),number(2),add(number(-1),r))),
      (f'R2{e}',pt(number(-1),number(2),add(number(2),r))),
    ]
assert len(points)==21

# Exponents of (x,y,z) and exact integral coefficients for six conics
# followed by six lines. The source's last line is multiplied by two.
polys=[
 {(2,0,0):1,(1,1,0):2,(0,2,0):1,(1,0,1):-1},
 {(2,0,0):1,(1,1,0):1,(0,1,1):2,(0,0,2):-1},
 {(2,0,0):1,(1,0,1):1,(0,1,1):1},
 {(2,0,0):1,(1,1,0):1,(0,0,2):1},
 {(2,0,0):1,(1,1,0):2,(1,0,1):-1,(0,1,1):1},
 {(2,0,0):1,(0,2,0):-1,(1,0,1):1,(0,1,1):2},
 {(0,1,0):1},
 {(1,0,0):1,(0,0,1):1},
 {(1,0,0):1,(0,1,0):1,(0,0,1):-1},
 {(1,0,0):1,(0,1,0):1,(0,0,1):1},
 {(1,0,0):1,(0,0,1):-1},
 {(1,0,0):2,(0,1,0):1},
]
def evaluate(poly,p):
    out=ZERO
    for ex,coeff in poly.items():
        term=number(coeff)
        for j,k in enumerate(ex):
            for _ in range(k):term=mul(term,p[j])
        out=add(out,term)
    return out

def partial(poly,j):
    out={}
    for ex,n in poly.items():
        if ex[j]:
            new=tuple(ex[k]-(1 if j==k else 0) for k in range(3))
            out[new]=out.get(new,0)+n*ex[j]
    return out

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def verify_exact():
    # A nonzero Hessian determinant certifies every conic's smoothness
    # away from residue characteristics two and three.
    hess=[]
    for poly in polys[:6]:
        M=[]
        for j in range(3):
            first=partial(poly,j)
            M.append([partial(first,k).get((0,0,0),0) for k in range(3)])
        hess.append(det3(M))
    assert hess==[-2,-6,-2,-2,-6,-6],hess

    incidence=[]
    for name,p in points:
        inc=[i for i,poly in enumerate(polys) if evaluate(poly,p)==ZERO]
        incidence.append(inc)
    assert Counter(len(m) for m in incidence)=={6:9,2:12}
    assert len(set(tuple(m) for m in incidence))==14
    assert incidence[:7]==[
      [0,2,4,5,6,11],[1,2,3,4,7,10],[3,4,5,7,8,11],
      [0,2,3,9,10,11],[0,1,3,5,8,9],
      [1,2,5,6,7,9],[0,1,4,6,8,10]]
    assert incidence[7]==[0,1,2,3,4,5]

    degrees=[2]*6+[1]*6
    for i,j in combinations(range(12),2):
        n=sum(i in mem and j in mem for mem in incidence)
        assert n==degrees[i]*degrees[j],(i,j,n)

    # All pairwise point-collision obstructions, extra incidences, and
    # failures of transversality have norm-content supported on {2,3}.
    counts=[0,0,0]
    for a,b in combinations(range(len(points)),2):
        w=cross(points[a][1],points[b][1]);q=reduce(gcd,(abs(norm(z)) for z in w))
        assert q>0 and support(q)<={2,3},('collision',a,b,q)
        counts[0]+=1
    for (name,p),mem in zip(points,incidence):
        for j,poly in enumerate(polys):
            if j not in mem:
                q=abs(norm(evaluate(poly,p)))
                assert q>0 and support(q)<={2,3},('extra',name,j,q)
                counts[1]+=1
        for j,k in combinations(mem,2):
            gj=[evaluate(partial(polys[j],t),p) for t in range(3)]
            gk=[evaluate(partial(polys[k],t),p) for t in range(3)]
            w=cross(gj,gk);q=reduce(gcd,(abs(norm(z)) for z in w))
            assert q>0 and support(q)<={2,3},('tangency',name,j,k,q)
            counts[2]+=1
    assert counts==[210,174,147],counts

    # The 7 rational points, one conjugate pair over Q(sqrt(-3)),
    # three pairs over Q(i), and three pairs over Q(sqrt(3)).
    assert [name for name,_ in points if name.startswith('H')]==['H1','H-1']
    assert sum(name.startswith('I') for name,_ in points)==6
    assert sum(name.startswith('R') for name,_ in points)==6
    return tuple(counts)

def evaluate_mod(poly,pv,p):
    return sum(n*pow(pv[0],e[0],p)*pow(pv[1],e[1],p)*pow(pv[2],e[2],p)
               for e,n in poly.items())%p

def rational_singular_count(p):
    # Exact enumeration of all p^2+p+1 projective F_p-points.
    count=0
    candidates=((1,a,b) for a in range(p) for b in range(p))
    for v in candidates:
        if sum(evaluate_mod(f,v,p)==0 for f in polys)>=2:count+=1
    for v in ((0,1,a) for a in range(p)):
        if sum(evaluate_mod(f,v,p)==0 for f in polys)>=2:count+=1
    if sum(evaluate_mod(f,(0,0,1),p)==0 for f in polys)>=2:count+=1
    return count

def verify_modular():
    for p in (5,7,11,13,17,19,23,29,31,37,41,43):
        expected={1:21,5:13,7:9,11:13}[p%12]
        got=rational_singular_count(p)
        assert got==expected,(p,got,expected)

if __name__=='__main__':
    assert verify_exact()==(210,174,147)
    verify_modular()
    print('VERIFY_OK: all 21 points, 210 collisions, 174 non-incidences, 147 tangent checks, 12 finite fields')
