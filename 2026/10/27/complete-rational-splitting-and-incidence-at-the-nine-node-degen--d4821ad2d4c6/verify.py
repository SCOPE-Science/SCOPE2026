"""Exact finite-field certificate for a nodal quartic's marked line incidence.

Run: python3 verify.py
Dependencies: Python standard library.
The published geometric line and singularity counts are cited in RESULT.md.
"""
import json
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path

# F_9 = F_3[t]/(t^2+1), integer code a+3*b represents a+b*t.
Q = range(9)
I = 3

def add(x, y):
    return ((x % 3 + y % 3) % 3) + 3 * (((x // 3) + (y // 3)) % 3)

def mul(x, y):
    a, b = x % 3, x // 3
    c, d = y % 3, y // 3
    return (a*c + 2*b*d) % 3 + 3 * ((a*d + b*c) % 3)

def neg(x):
    return ((-(x % 3)) % 3) + 3 * ((-(x // 3)) % 3)

def power(x, n):
    r = 1
    while n:
        if n & 1:
            r = mul(r, x)
        x = mul(x, x)
        n //= 2
    return r

def sm(*xs):
    z = 0
    for x in xs: z = add(z, x)
    return z

def pr(*xs):
    z = 1
    for x in xs: z = mul(z, x)
    return z

assert power(I, 2) == 2
assert len({power(x, 8) for x in range(1,9)}) == 1
assert all(power(x, 8) == 1 for x in range(1,9))

# F = (1-i)(X^2 UV-X^2Y^2+UVY^2)
#     -(1+i)(U^2V^2-XY(U^2+V^2))
#     -(UV+XY)(X+Y)(U+V), with (X,U,V,Y) = (x0,x1,x2,x3).
K = add(1, neg(I))
L = neg(add(1, I))

def quartic_at(x):
    X, U, V, Y = x
    X2, U2, V2, Y2 = (mul(t, t) for t in x)
    uv, xy = mul(U, V), mul(X, Y)
    b = sm(pr(X2, uv), neg(pr(X2, Y2)), pr(uv, Y2))
    c = sm(pr(U2, V2), neg(pr(xy, sm(U2, V2))))
    d = pr(sm(uv, xy), sm(X, Y), sm(U, V))
    return sm(mul(K,b),mul(L,c),neg(d))

# Independent substitution in F_9[s] with exact coefficient arrays.
def pa(A,B):
    return [add(x,y) for x,y in zip(A,B)]
def pn(A):
    return [neg(x) for x in A]
def pm(A,B):
    C = [0]*5
    for i,x in enumerate(A):
        for j,y in enumerate(B):
            if i+j < 5: C[i+j] = add(C[i+j],mul(x,y))
    return C

def pp(*X):
    c = [1,0,0,0,0]
    for a in X:c = pm(c,a)
    return c

def scalar(a,X):
    return [mul(a,b) for b in X]

def quartic_on_line(u,v):
    X,U,V,Y = ([u[i],v[i],0,0,0] for i in range(4))
    X2,U2,V2,Y2 = (pp(z,z) for z in (X,U,V,Y))
    uv,xy=pp(U,V),pp(X,Y)
    b=pa(pa(pp(X2,uv), pn(pp(X2,Y2))),pp(uv,Y2))
    c=pa(pp(U2,V2),pn(pp(xy,pa(U2,V2))))
    d=pp(pa(uv,xy),pa(X,Y),pa(U,V))
    return pa(pa(scalar(K,b),scalar(L,c)),pn(d))

def projective_normalize(vec):
    for x in vec:
        if x:
            inv=power(x,7)
            return tuple(mul(y,inv) for y in vec)
    raise ValueError('zero vector')

def projective_points():
    for i in range(4):
        for tail in product(Q, repeat=3-i):
            yield tuple([0]*i+[1]+list(tail))

def rref_lines():
    for i in range(4):
        for j in range(i+1,4):
            free = [(0,k) for k in range(i+1,4) if k != j]
            free += [(1,k) for k in range(j+1,4)]
            for vals in product(Q,repeat=len(free)):
                u=[0]*4;v=[0]*4
                u[i]=v[j]=1
                for (row,k),z in zip(free,vals):
                    (u if row == 0 else v)[k]=z
                yield (tuple(u),tuple(v))

def line_points(u,v):
    for t in Q:
        yield projective_normalize([add(u[k],mul(t,v[k])) for k in range(4)])
    yield projective_normalize(v)

# Formal multivariate polynomial arithmetic and derivatives, independent of
# the restriction routine above. Monomials indexed by 4-tuples of exponents.
ZERO=(0,0,0,0)
def dictadd(A,B):
    out=dict(A)
    for k,v in B.items():out[k]=add(out.get(k,0),v)
    return {k:v for k,v in out.items() if v}
def dictneg(A):return {k:neg(v) for k,v in A.items()}
def dictmul(A,B):
    out={}
    for e,a in A.items():
        for f,b in B.items():
            g=tuple(e[i]+f[i] for i in range(4))
            out[g]=add(out.get(g,0),mul(a,b))
    return {k:v for k,v in out.items() if v}
def polprod(*args):
    out={ZERO:1}
    for A in args:out=dictmul(out,A)
    return out
def polscalar(a,B):return {k:mul(a,v) for k,v in B.items() if mul(a,v)}
def derivative(A,i):
    out={}
    for e,v in A.items():
        if e[i]:
            f=list(e);f[i]-=1
            out[tuple(f)]=mul(e[i]%3,v)
    return {k:v for k,v in out.items() if v}
def poleval(A,x):
    z=0
    for e,v in A.items():
        for k in range(4):v=mul(v,power(x[k],e[k]))
        z=add(z,v)
    return z

def quartic_polynomial():
    X,U,V,Y=({tuple(1 if i == j else 0 for i in range(4)):1} for j in range(4))
    X2,U2,V2,Y2=(polprod(t,t) for t in (X,U,V,Y))
    uv,xy=polprod(U,V),polprod(X,Y)
    b=dictadd(dictadd(polprod(X2,uv),dictneg(polprod(X2,Y2))),polprod(uv,Y2))
    c=dictadd(polprod(U2,V2),dictneg(polprod(xy,dictadd(U2,V2))))
    d=polprod(dictadd(uv,xy),dictadd(X,Y),dictadd(U,V))
    return dictadd(dictadd(polscalar(K,b),polscalar(L,c)),dictneg(d))

def determinant3(a):
    t=lambda i,j,k:pr(a[0][i],a[1][j],a[2][k])
    return sm(t(0,1,2),t(1,2,0),t(2,0,1),neg(t(0,2,1)),neg(t(1,0,2)),neg(t(2,1,0)))

# Reproduce line search in all six row-echelon charts.
line_list=[]; seen=0
for u,v in rref_lines():
    seen+=1
    if quartic_on_line(u,v)==[0]*5:
        assert all(quartic_at(x)==0 for x in line_points(u,v))
        line_list.append([list(u),list(v)])
assert seen == 9**4+9**3+2*9**2+9+1 == 7462
assert len(line_list)==40
cert_path=Path(__file__).with_name('lines_f9.json')
certificate=json.loads(cert_path.read_text('utf8'))
assert certificate['field']=='F3[t]/(t^2+1)'
assert certificate['lines']==line_list

QPOL=quartic_polynomial()
assert len(QPOL)>0
assert all(quartic_at(P)==poleval(QPOL,P) for P in projective_points())
grad=[derivative(QPOL,i) for i in range(4)]
singular=[]
for P in projective_points():
    if poleval(QPOL,P)==0 and all(poleval(g,P)==0 for g in grad):
        singular.append(P)
assert len(singular)==9
for P in singular:
    pivot=next(i for i in range(4) if P[i])
    inds=[i for i in range(4) if i!=pivot]
    h=[[poleval(derivative(grad[i],j),P) for j in inds] for i in inds]
    assert determinant3(h)!=0,(P,h)

inc=defaultdict(set)
for k,(u,v) in enumerate(line_list):
    for P in line_points(u,v):inc[P].add(k)
assert len(inc)==199
assert Counter(len(s) for s in inc.values())==Counter({1:36,2:153,4:1,6:9})
assert all(len(inc[P])==6 for P in singular)
assert all(P in singular for P in inc if len(inc[P])==6)
assert sum(len(inc[P]) for P in singular)==54
assert sum(len(inc[P]) for P in inc)==400
assert len([P for P in inc if len(inc[P])==4 and P not in singular])==1

edges=set()
for s in inc.values():edges.update(combinations(sorted(s),2))
assert len(edges)==294
assert sum(1 for u,v in edges if any(u in inc[P] and v in inc[P] for P in singular))==135
deg=Counter()
for u,v in edges:
    deg[u]+=1;deg[v]+=1
assert Counter(deg.values())==Counter({12:4,14:18,16:18})
adj={i:set() for i in range(40)}
for u,v in edges:
    adj[u].add(v)
    adj[v].add(u)
visited={0}
front=[0]
while front:
    for v in adj[front.pop()]:
        if v not in visited:
            visited.add(v)
            front.append(v)
assert len(visited)==40
assert Counter(sum(k in inc[P] for P in singular) for k in range(40))==Counter({0:4,1:18,2:18})

print('VERIFY_OK')
print('lines=40, nodes=9, covered F9 projective lines=7462')
print('incidence=36 isolated-on-line points, 153 double, 1 quadruple, 9 sixfold')
print('line graph: 40 vertices, 294 edges, degree sequence 12^4 14^18 16^18')
