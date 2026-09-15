import numpy as np, itertools
# Exact check: signed K8 adjacency with integer spectrum {-3x3,-1,+1,+3x3}
M = np.array([[ 0, 1,-1, 1,-1, 1,-1,-1],
 [ 1, 0,-1, 1, 1,-1,-1,-1],
 [-1,-1, 0, 1,-1, 1, 1,-1],
 [ 1, 1, 1, 0,-1,-1, 1,-1],
 [-1, 1,-1,-1, 0,-1, 1,-1],
 [ 1,-1, 1,-1,-1, 0,-1,-1],
 [-1,-1, 1, 1, 1,-1, 0,-1],
 [-1,-1,-1,-1,-1,-1,-1, 0]])
# exact charpoly via integers (Faddeeva / numpy roundoff-safe: use sympy if avail else integer elimination)
try:
    import sympy as sp
    x=sp.Symbol('x')
    cp = sp.Matrix(M.tolist()).charpoly(x).as_expr()
    print("charpoly:", sp.expand(cp))
    print("roots:", sp.factor(cp))
except ImportError:
    print("no sympy; eig:", np.linalg.eigvalsh(M))
B = 2*np.sqrt(6)
ev = np.linalg.eigvalsh(M)
print("specrad:", np.max(np.abs(ev)), "<= 2sqrt6 =", B, ":", bool(np.max(np.abs(ev))<=B))
# K8 spectrum: 7, -1 x7 ; lift G1 spectrum = union
print("G1 nontrivial max abs:", max(1.0, float(np.max(np.abs(ev)))))
print("G1 two-sided Ramanujan:", bool(max(1.0,float(np.max(np.abs(ev))))<=B))
