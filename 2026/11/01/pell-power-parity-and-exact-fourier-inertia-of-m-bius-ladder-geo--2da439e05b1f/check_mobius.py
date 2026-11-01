"""Independent finite checks for geodesic distance spectra of Möbius ladders.

Run: python check_mobius.py
Dependencies: Python 3, numpy, sympy. Exact determinants use integer arithmetic.
"""
from collections import deque
from math import cos, sin, pi, floor
import numpy as np
import sympy as sp


def shortest_path_matrix(n):
    size=2*n
    neighbors=[[(i-1)%size,(i+1)%size,(i+n)%size] for i in range(size)]
    M=np.empty((size,size),dtype=int)
    for source in range(size):
        row=[-1]*size
        row[source]=0
        que=deque([source])
        while que:
            i=que.popleft()
            for j in neighbors[i]:
                if row[j]<0:
                    row[j]=row[i]+1
                    que.append(j)
        assert min(row)==0
        M[source]=row
    return M


def claimed_eigenvalues(n):
    ev=[]
    for k in range(2*n):
        if k==0:
            ev.append((n*n+2*n-1)//2)
            continue
        x=pi*k/(2*n)
        if k%2:
            sign=(-1)**((k+1)//2)
            value=sign*(1/sin(x) if n%2 else cos(x)/sin(x))
        elif n%2==0:
            value=-1 if (k//2)%2==0 else -1-2*(cos(x)/sin(x))**2
        else:
            value=-1/(1+(-1)**(k//2)*cos(x))
        ev.append(value)
    return np.array(ev,dtype=float)


def det_formula(n):
    tr=(n*n+2*n-1)//2
    if n%2:
        return (-1)**((n+1)//2)*tr*2**(2*n-2)
    m=n//2
    a,b=1,1
    for k in range(2,m+1):
        a,b=b,2*b+a
    return -tr*b*b


def positive_count(n):
    if n%2: return (n+1)//2
    return 1+2*(n//4)


def run():
    checks=0
    for n in range(3,72):
        M=shortest_path_matrix(n)
        first=M[0]
        direct=np.array([min(k,2*n-k,1+abs(n-k)) for k in range(2*n)])
        assert np.array_equal(first,direct), ('metric',n)
        checks+=1
        spectrum_direct=np.fft.fft(first).real
        spectrum_claimed=claimed_eigenvalues(n)
        assert np.max(np.abs(spectrum_direct-spectrum_claimed))<2e-8, ('spectrum',n)
        checks+=1
        assert np.count_nonzero(spectrum_claimed>1e-8)==positive_count(n),('inertia',n)
        assert np.count_nonzero(np.abs(spectrum_claimed)<1e-8)==0,('nullity',n)
        checks+=2
        assert abs(sum(first)-claimed_eigenvalues(n)[0])<1e-9,('row sum',n)
        checks+=1
        if n<=16:
            Q=sp.Matrix(M.tolist())
            exact=int(Q.det(method='domain-ge'))
            assert exact==det_formula(n),('determinant',n,exact,det_formula(n))
            checks+=1
    for m in range(2,80):
        pell_earlier,pell=1,1
        for i in range(2,m+1):
            pell_earlier,pell=pell,2*pell+pell_earlier
        lhs=1.
        for j in range(1,m,2):
            angle=pi*j/(2*m)
            lhs*=1+2*(cos(angle)/sin(angle))**2
        assert abs(lhs/pell-1)<2e-9,('Pell product',m,lhs,pell)
        checks+=1
    print('PASS:',checks,'independent assertion groups, spanning n=3..71; integer determinants n=3..16; Pell products m=2..79.')


if __name__=='__main__': run()
