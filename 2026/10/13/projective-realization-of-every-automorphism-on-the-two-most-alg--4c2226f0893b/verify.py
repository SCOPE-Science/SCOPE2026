from __future__ import annotations
from collections import Counter
import sympy as sp

x0,x1,x2,x3 = sp.symbols("x0 x1 x2 x3")
xs = (x0,x1,x2,x3)
I = sp.I

FI = (
    -x0**2*x1**2*x2**2 + 8*x0**2*x1**2*x3**2
    + 8*x0**2*x2**2*x3**2 - x1**2*x2**2*x3**2
    - 8*x0**3*x1*x2*x3 + 9*x0*x1**3*x2*x3
    - 7*x0*x1*x2**3*x3 - 8*x0*x1*x2*x3**3
)
FII = (
    -x0**2*x1**2*x2**2 + x0**2*x1**2*x3**2
    + x0**2*x2**2*x3**2 + 63*x1**2*x2**2*x3**2
    - x0**3*x1*x2*x3 + x0*x1**3*x2*x3
    + x0*x1*x2**3*x3 - x0*x1*x2*x3**3
)

a = sp.diag(1,-1,-1,1)
b = sp.diag(1,-1,1,-1)
sI = sp.Matrix([[0,0,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,0]])
u = sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
v = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,I],[0,0,-I,0]])

def action(F,M):
    ys = list(M*sp.Matrix(xs))
    return sp.expand(F.subs(dict(zip(xs,ys)), simultaneous=True))

def norm(M):
    M = sp.Matrix(M)
    for z in list(M):
        if sp.simplify(z) != 0:
            return M.applyfunc(lambda q: sp.simplify(q/z))
    raise AssertionError("zero matrix")

def key(M):
    return tuple(str(z) for z in list(norm(M)))

def closure(gens):
    e = sp.eye(4)
    seen = {key(e): e}
    todo = [e]
    while todo:
        A = todo.pop()
        for g in gens:
            B = norm(A*g)
            k = key(B)
            if k not in seen:
                seen[k] = B
                todo.append(B)
    return list(seen.values())

def order(M):
    ekey = key(sp.eye(4))
    P = sp.eye(4)
    for n in range(1,49):
        P = norm(P*M)
        if key(P) == ekey:
            return n
    raise AssertionError("order exceeded bound")

for M in (a,b,sI):
    assert sp.expand(action(FI,M)-FI) == 0
for M in (a,b,u,v):
    assert sp.expand(action(FII,M)-FII) == 0

GI = closure((a,b,sI))
GII = closure((a,b,u,v))
profile_I = Counter(order(g) for g in GI)
profile_II = Counter(order(g) for g in GII)

assert len(GI) == 8
assert profile_I == Counter({2:5,4:2,1:1})
assert len(GII) == 24
assert profile_II == Counter({2:9,3:8,4:6,1:1})

print(
    "VERIFY_OK "
    "typeI=8:D8 profile=1^1,2^5,4^2 "
    "typeII=24:S4 profile=1^1,2^9,3^8,4^6"
)
