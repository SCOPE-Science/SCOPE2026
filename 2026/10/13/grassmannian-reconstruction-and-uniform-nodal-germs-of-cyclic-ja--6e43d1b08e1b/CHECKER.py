"""Exact arithmetic checks for the cyclic Jacobi corank-two Grassmannian chart.
The computations test examples; the general statements require the proof.
"""
from random import Random
import sympy as sp
R=Random(20261009)
tests=0
for n in range(4,10):
    for _ in range(14):
        while True:
            Q=sp.Matrix([[R.randint(-4,4) for j in range(n)] for k in range(2)])
            p=lambda i,j: sp.det(Q[:,[i%n,j%n]])
            if Q.rank()==2 and all(p(i,(i+1)%n) != 0 for i in range(n)):
                break
        E=[p(i,(i+1)%n) for i in range(n)]
        P=sp.prod(E)
        a=[sp.cancel(-P*p((i-1)%n,(i+1)%n)/(E[(i-1)%n]*E[i])) for i in range(n)]
        b=[P/E[i] for i in range(n)]
        A=sp.diag(*a)
        for i in range(n):
            j=(i+1)%n
            A[i,j]=b[i]
            A[j,i]=b[i]
        assert A*Q.T == sp.zeros(n,2), ('kernel',n)
        assert A.rank()==n-2, ('rank',n)
        # Test the corank-two hypersurface normal slice spanned by
        # two neighboring diagonal perturbations and their edge.
        qi=Q[:,0];qj=Q[:,1]
        forms=[qi*qi.T,qj*qj.T,qi*qj.T+qj*qi.T]
        vec=lambda B: sp.Matrix([B[0,0],B[0,1],B[1,1]])
        assert sp.Matrix.hstack(*map(vec,forms)).det()!=0
        # kernel recovery on the projective matrix: rebuilt A should agree.
        K=sp.Matrix.hstack(*A.nullspace()).T
        pp=lambda i,j: sp.det(K[:,[i%n,j%n]])
        ppE=[pp(i,(i+1)%n) for i in range(n)]
        c=sp.prod(ppE)
        AA=sp.zeros(n)
        for i in range(n):
            AA[i,i]=-c*pp((i-1)%n,(i+1)%n)/(ppE[(i-1)%n]*ppE[i])
            j=(i+1)%n
            AA[i,j]=AA[j,i]=c/ppE[i]
        ratios=[sp.cancel(AA[i,j]/A[i,j]) for i,j in [(i,(i+1)%n) for i in range(n)]]
        assert all(t==ratios[0] for t in ratios)
        tests+=1
print('checks:',tests,'exact cyclic Plucker reconstructions, kernel rank, and normal Hessian spans; n=4..9')
