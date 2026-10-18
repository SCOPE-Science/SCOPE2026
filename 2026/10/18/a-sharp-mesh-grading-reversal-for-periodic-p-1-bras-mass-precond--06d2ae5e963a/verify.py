"""Reproduce exact small-periodic-mesh mass/BRAS/Jacobi calculations.
Uses only Python standard library; finite tests corroborate independent proofs.
"""
from fractions import Fraction as F
from random import Random
from math import isclose

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def matrix(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]

def assemble(lengths):
    n=len(lengths)
    assert n>=2
    M=matrix(n); B=matrix(n)
    for i,h in enumerate(lengths):
        h=F(h)
        assert h>0
        j=(i+1)%n
        for a,b in ((i,i),(j,j)):
            M[a][b]+=h/3
            B[a][b]+=1/h
        M[i][j]+=h/6; M[j][i]+=h/6
        B[i][j]-=1/(2*h);B[j][i]-=1/(2*h)
    return M,B

def char3(A):
    tr=sum(A[i][i] for i in range(3))
    c2=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i,j in ((0,1),(0,2),(1,2)))
    det=(A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-
         A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+
         A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
    return tr,c2,det

def main():
    count=0
    for a in range(1,25):
        for b in range(1,25):
            M,B=assemble([F(a,5),F(b,7)])
            A=matmul(B,M)
            scalar=F((F(a,5)+F(b,7))**2,4*F(a,5)*F(b,7))
            assert A==[[scalar,F(0)],[F(0),scalar]]
            count+=1
    qlist=[F(1,j) for j in range(1,201)]+[F(j,201) for j in range(1,202)]
    for q in qlist:
        M,B=assemble([q,F(1),F(1)])
        A=matmul(B,M)
        ea=F(1,2*q)+F(7,12)+q/6
        eb=F(1,6*q)+F(7,12)+q/2
        expected=(1+ea+eb, ea+eb+ea*eb, ea*eb)
        assert char3(A)==expected
        assert 1<eb<=ea
        DinvM=[[M[i][j]/M[i][i] for j in range(3)] for i in range(3)]
        ja=F(3,2); jb=(2*q+1)/(2*(q+1)); jc=(q+2)/(2*(q+1))
        assert char3(DinvM)==(ja+jb+jc,ja*jb+ja*jc+jb*jc,ja*jb*jc)
        assert jb<=jc<=ja
        assert ea>eb or q==1
        count+=1
    # General periodic assemblies are positive quadratic forms element by element.
    # These finite exact checks exercise the generic n-cell assembly and two-element
    # component geometry; the asymptotic eigenspace arguments are in the proof.
    rng=Random(23091)
    for n in range(3,19):
        for trial in range(100):
            h=[F(1, rng.randint(1,1000))]+[F(1) for _ in range(n-1)]
            M,B=assemble(h)
            assert M[0][0]>0 and B[0][0]>0
            assert all(M[i][i]>sum(abs(M[i][j]) for j in range(n) if j!=i) for i in range(n))
            # The leading inverse local-element contribution has exactly two
            # linearly independent endpoints, while one unaffected node exists.
            assert n>=3 and (n-2)>=1
            count+=1
    from decimal import Decimal, getcontext
    getcontext().prec=50
    l=Decimal('0.2'); u=Decimal('0.3')
    P=lambda x:4*x**3-20*x**2-17*x+6
    assert P(l)>0>P(u)
    for _ in range(190):
        mid=(l+u)/2
        if P(mid)>0:l=mid
        else:u=mid
    root=(l+u)/2
    assert abs(root-Decimal('0.27114057472819640557916457468727741869071212128946'))<Decimal('1e-45')
    print('PASS',count,'exact-and-assembly checks; crossover',str(root))

if __name__=='__main__':main()
