"""Reproduce finite-rate two-end alternating-gate formulas by an independent lattice CTMC."""
import math
import numpy as np


def formulas(L, D, k, x):
    a = math.sqrt(2*k/D)
    t = a*L/2
    gate_delay = L*math.tanh(t)/(2*D*a)
    residence = x*(L-x)/(2*D) + gate_delay
    left_hit = 0.5 + (L/2-x)/(L+2/(a*math.tanh(t)))
    return residence, left_hit


def discrete(L,D,k,N):
    h=L/N
    transient=[(s,j) for s in (0,1) for j in range(N+1)
              if not ((s==0 and j==0) or (s==1 and j==N))]
    indices={z:i for i,z in enumerate(transient)}
    K=len(transient)
    Q=np.zeros((K,K))
    b=np.zeros(K)
    for (s,j),i in indices.items():
        if 0<j<N:
            transitions=[(s,j-1,D/h**2),(s,j+1,D/h**2)]
        elif j==0:
            transitions=[(s,j+1,2*D/h**2)]
        else:
            transitions=[(s,j-1,2*D/h**2)]
        transitions.append((1-s,j,k))
        for ns,nj,r in transitions:
            Q[i,i]-=r
            if (ns,nj) in indices:
                Q[i,indices[(ns,nj)]]+=r
            elif ns==0 and nj==0:
                b[i]+=r
            else:
                assert ns==1 and nj==N
    times=np.linalg.solve(-Q,np.ones(K))
    splits=np.linalg.solve(-Q,b)
    return indices,times,splits


def main():
    cases=0
    max_t_error=max_p_error=0.0
    for L,D,k in [(1.,1.,0.3),(1.,2.,5.),(2.,0.7,1.1),(3.,4.,20.)]:
        for N in (40,80):
            inds,T,P=discrete(L,D,k,N)
            for j in (N//4,N//2,3*N//4):
                expected_t,expected_p=formulas(L,D,k,L*j/N)
                t_avg=(T[inds[(0,j)]]+T[inds[(1,j)]])/2
                p_avg=(P[inds[(0,j)]]+P[inds[(1,j)]])/2
                max_t_error=max(max_t_error,abs(t_avg-expected_t))
                max_p_error=max(max_p_error,abs(p_avg-expected_p))
                assert abs(t_avg-expected_t)<2.0e-3*(1+expected_t)
                assert abs(p_avg-expected_p)<2.0e-3
                cases+=1
    # Evaluate exact distinctions and universal monotonicity.
    for k in [0.001,0.05,0.3,1,10,100]:
        L,D=2.,3.
        a=math.sqrt(2*k/D)
        z=a*L/2
        h_T=D*a/math.tanh(z)
        h_P=D*a*math.tanh(z)
        assert h_T>h_P>0
        assert math.isclose(h_T/h_P,1/math.tanh(z)**2,rel_tol=2e-14)
        assert 0<math.tanh(z)/z<1
    print('PASS: stationary mean and splitting independently checked at',cases,'grid instances')
    print('maximum absolute numerical errors:',max_t_error,max_p_error)
    print('PASS: positive distinct Robin calibrations and strict penalty')

if __name__=='__main__':
    main()
