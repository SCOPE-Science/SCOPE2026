"""Finite exact witnesses for cyclic sparse-symmetric rank-two geometry.

Requires Python 3 and sympy.  Infinite claims are established by the accompanying proof.
"""
from itertools import combinations
from math import lcm
import sympy as s

def build(n, a, b):
    A=s.zeros(n)
    for i in range(n):
        A[i,i]=a[i]
        A[i,(i+1)%n]=b[i]
        A[(i+1)%n,i]=b[i]
    return A

def cycle_witness(n):
    t=[i*i+3*i for i in range(n)]
    w=[t[(i+1)%n]-t[i] for i in range(n)]
    assert all(w)
    q=lcm(*[abs(v) for v in w])
    b=[s.Integer(q)//w[i] for i in range(n)]
    a=[-(b[i-1]+b[i]) for i in range(n)]
    A=build(n,a,b)
    assert A.rank()==n-2
    assert A*s.ones(n,1)==s.zeros(n,1)
    assert A*s.Matrix(t)==s.zeros(n,1)

def cut_witness(n,i,j):
    b=[s.Integer(1)]*n
    b[i]=b[j]=0
    a=[-b[k-1]-b[k] for k in range(n)]
    A=build(n,a,b)
    assert A.rank()==n-2
    # Find the two arcs by traversing remaining edges.
    parts=[]
    unseen=set(range(n))
    while unseen:
        root=min(unseen)
        seen={root}; stack=[root]
        while stack:
            v=stack.pop()
            for edge,adj in ((v,(v+1)%n),((v-1)%n,(v-1)%n)):
                if b[edge] and adj not in seen:
                    seen.add(adj);stack.append(adj)
        parts.append(seen);unseen-=seen
    assert len(parts)==2
    u=s.Matrix([int(k in parts[0]) for k in range(n)])
    v=s.Matrix([int(k in parts[1]) for k in range(n)])
    assert A*u==s.zeros(n,1) and A*v==s.zeros(n,1)
    # Matrix of induced symmetric bilinear forms on the kernel
    def restrict(E):return [int((u.T*E*u)[0]),int((v.T*E*v)[0]),int((u.T*E*v)[0])]
    Es=[]
    for vertex in range(n):
        E=s.zeros(n);E[vertex,vertex]=1;Es.append(E)
    for cut in (i,j):
        E=s.zeros(n);E[cut,(cut+1)%n]=1;E[(cut+1)%n,cut]=1;Es.append(E)
    rank=s.Matrix.hstack(*[s.Matrix(restrict(E)) for E in Es]).rank()
    assert rank==3
    assert all(restrict(E)[2]!=0 for E in Es[-2:])

for n in range(4,9):
    cycle_witness(n)
    for i,j in combinations(range(n),2):
        cut_witness(n,i,j)
    print('n',n,'cut-pairs',n*(n-1)//2,'OK')
print('VERIFY_OK')
