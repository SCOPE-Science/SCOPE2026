"""Standalone finite-dimensional cross-checks for the one-sink XX-cycle cooling theorem.

Requires Python 3, NumPy and SymPy. All checks use newly constructed
matrices, not precomputed spectra. Finite checks supplement the analytic proof.
"""
import itertools
from math import comb, cos, pi
import numpy as np
import sympy as sp


def ring_matrix(n, d, q=1):
    h = np.zeros((n, n), dtype=float)
    for i in range(n-1):
        h[i, i+1] = h[i+1, i] = 1.
    h[0, n-1] = h[n-1, 0] = q
    h[1, 1] += d
    return h


def sector_matrices(n, p, d):
    states = [sum(1 << j for j in s) for s in itertools.combinations(range(n), p)]
    lookup = {v:i for i,v in enumerate(states)}
    spin = np.zeros((len(states), len(states)))
    wedge = np.zeros_like(spin)
    q = (-1)**(p-1)
    h = ring_matrix(n,d,q)
    for col,state in enumerate(states):
        spin[col,col] += d * bool(state & 2)
        wedge[col,col] += d * bool(state & 2)
        for src in range(n):
            if not (state >> src)&1:
                continue
            for dst in [(src+1)%n,(src-1)%n]:
                if (state >> dst)&1:
                    continue
                other = state ^ (1 << src)
                row = lookup[other | (1 << dst)]
                spin[row,col] += 1.
                between = range(min(src,dst)+1,max(src,dst))
                parity = sum((other>>j)&1 for j in between)%2
                wedge[row,col] += h[dst,src]*(-1)**parity
    return states, spin, wedge


def dark_dim(H, states):
    # A dark eigenstate vanishes on the basis states where the cooled site is occupied.
    ev,V = np.linalg.eigh(H)
    occupied = np.array([bool(s&1) for s in states])
    ans=0
    a=0
    while a<len(ev):
        b=a+1
        while b<len(ev) and abs(ev[b]-ev[a])<3e-8:
            b+=1
        A=V[occupied,a:b]
        sv=np.linalg.svd(A,compute_uv=False)
        r=int(sum(x>2e-7 for x in sv))
        ans+=(b-a)-r
        a=b
    return ans


def one_dark(h):
    # Observability/cyclicity using the spectral projector on each eigenvalue.
    ev,V=np.linalg.eigh(h)
    ans=0
    i=0
    while i<len(ev):
        j=i+1
        while j<len(ev) and abs(ev[j]-ev[i])<2e-8:
            j+=1
        ans+=j-i-int(np.linalg.norm(V[0,i:j])>2e-7)
        i=j
    return ans


def exceptions(n):
    return [2*cos(k*pi/(n-2)) for k in range(1,n-2,2)]


def run():
    count=0
    x=sp.symbols('x')
    # Chebyshev continuant identity, exact polynomial arithmetic.
    for m in range(3,31):
        A=sp.chebyshevu(m,x/2)
        B=sp.chebyshevu(m-1,x/2)
        C=sp.chebyshevu(m-2,x/2)
        assert sp.expand(A*C-B*B+1)==0
        count+=1
    # All spin matrix elements match exterior-power fermionic matrix elements.
    for n in range(4,9):
        for p in range(1,n):
            states,H,W=sector_matrices(n,p,0.7)
            assert np.array_equal(H,W), (n,p,np.max(abs(H-W)))
            count+=1
    # Verify full spin-sector dark space in finite cases, including anti-periodic
    # one-body resonances where the physical many-body system still cools.
    for n,d,expected in [(4,0,True),(4,1,False),(5,-1,False),
                         (5,0,True),(5,1,True),(5,2,False),
                         (6,0,True),(6,1,False),(6,2,False),
                         (7,0,True),(7,1,False),(7,2,False),
                         (8,0,True),(8,1,False),(8,-1,False)]:
        total_dark=0
        for p in range(1,n+1):
            states,H,W=sector_matrices(n,p,d)
            total_dark+=dark_dim(H,states)
            count+=1
        assert (total_dark>0)==expected,(n,d,total_dark,expected)
    # Identify every exceptional one-particle mode and parity selectivity.
    for n in range(4,17):
        for k in range(1,n-2):
            d=2*cos(k*pi/(n-2))
            plus=one_dark(ring_matrix(n,d,+1))
            minus=one_dark(ring_matrix(n,d,-1))
            if abs(d)<2e-10:
                assert plus>=1 and minus>=1,(n,k,d,plus,minus)
            else:
                assert (plus,minus)==((1,0) if k%2 else (0,1)),(n,k,d,plus,minus)
            count+=1
        for d in (-3.,-2.7,-0.47,0.341,1.123,3.):
            plus=one_dark(ring_matrix(n,d,+1))
            if all(abs(d-r)>2e-7 for r in exceptions(n)):
                assert plus==0,(n,d,plus)
            count+=1
    # A dark vector at a positive-parity resonance, constructed by recurrence.
    for n in range(4,18):
        m=n-1
        for k in range(1,n-2,2):
            d=2*cos(k*pi/(n-2))
            v=np.zeros(n)
            for j in range(1,n):
                v[j]=float(sp.chebyshevu(m-j,x/2).subs(x,d))
            err=np.linalg.norm(ring_matrix(n,d,1)@v-d*v)
            assert err<3e-7,(n,k,err)
            assert abs(v[0])<1e-10
            count+=1
    print('VERIFY_OK',count)

if __name__=='__main__':
    run()
