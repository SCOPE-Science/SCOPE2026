"""Independent exact enumeration of fixed-composition permutation-null covariances."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def theorem(N, a):
    b=N-a; Q=a*b
    B=F(N*(N+1)-6*Q,(N-3)*(N-2))
    return [F(2*Q,N*(N-1))*(F(1-Q,6)+B*(F(2*j-N,2)**2-F(N*(N-2),12))) for j in range(1,N)]

def run():
    checks=0
    for N in range(4,12):
        for a in range(1,N):
            b=N-a; Q=a*b
            outcomes=[]
            for indices in combinations(range(N),a):
                bits=[int(i in indices) for i in range(N)]
                w=sum((2*i+1-N)*bits[i] for i in range(N))
                R=1+sum(bits[i]!=bits[i+1] for i in range(N-1))
                t=[int(bits[i]!=bits[i+1]) for i in range(N-1)]
                outcomes.append((w*w,R,t))
            num=comb(N,a)
            ey=F(sum(v[0] for v in outcomes),num)
            assert ey==F(Q*(N+1),3)
            er=F(sum(v[1] for v in outcomes),num)
            assert er==1+F(2*Q,N)
            cov4=F(sum(v[0]*v[1] for v in outcomes),num)-ey*er
            assert cov4==F(4*Q*(1-Q),3*N)
            checks+=3
            pred=theorem(N,a)
            for j in range(N-1):
                observed=F(sum(v[0]*v[2][j] for v in outcomes),num)-ey*F(sum(v[2][j] for v in outcomes),num)
                assert observed==4*pred[j], (N,a,j,observed,4*pred[j])
                checks+=1
            assert sum(pred)==F(Q*(1-Q),3*N)
            checks+=1
    for a,expected in [(1,('positive','negative','negative','negative','negative','negative','positive')),
                       (2,('negative',)*7),(4,('negative','negative','negative','positive','negative','negative','negative'))]:
        signs=tuple('positive' if x>0 else ('negative' if x<0 else 'zero') for x in theorem(8,a))
        assert signs==expected,(a,signs)
        checks+=1
    print('PASS:',checks,'exact-rational checks, including all compositions N=4..11 and three N=8 regimes')
if __name__=='__main__':run()
