"""Numerical cross-checks for the normalized-adjacency barbell theorem.
Run: python barbell_verification.py
Requires NumPy. These are finite checks, not a proof of the limits.
"""
import numpy as np
from numpy.linalg import eigh


def full_graph(a,b):
    N=a+b
    A=np.zeros((N,N), dtype=float)
    A[:a,:a]=np.ones((a,a))-np.eye(a)
    A[a:,a:]=np.ones((b,b))-np.eye(b)
    A[a-1,a]=A[a,a-1]=1
    d=A.sum(axis=1)
    H=A / np.sqrt(np.outer(d,d))
    L=np.r_[np.ones(a)/np.sqrt(a),np.zeros(b)]
    R=np.r_[np.zeros(a),np.ones(b)/np.sqrt(b)]
    v=np.zeros(N);v[0]=1  # an unbridged vertex
    return H,L,R,v


def quotient(a,b):
    H=np.array([[(a-2)/(a-1),1/np.sqrt(a),0,0],
                [1/np.sqrt(a),0,1/np.sqrt(a*b),0],
                [0,1/np.sqrt(a*b),0,1/np.sqrt(b)],
                [0,0,1/np.sqrt(b),(b-2)/(b-1)]],float)
    L=np.array([np.sqrt((a-1)/a),1/np.sqrt(a),0,0])
    R=np.array([0,0,1/np.sqrt(b),np.sqrt((b-1)/b)])
    I=np.array([1.,0,0,0])
    return H,L,R,I


def evolve(H,initial,t):
    vals,v=eigh(H)
    return v@(np.exp(-1j*vals*t)*(v.T@initial))


def predicted(r,s):
    q=r+1/r
    return 4*np.sin(s*q/2)**2/q**2


def main():
    checked=0
    for a,b in [(3,3),(3,5),(4,7),(5,5),(7,11),(8,13)]:
        H,l,r,v=full_graph(a,b)
        Q,lq,rq,iq=quotient(a,b)
        assert np.max(abs(H-H.T))<1e-14
        for s in (0, .1,.3,.7,1.0,2.3):
            t=s*a*b
            out=evolve(H,l,t); red=evolve(Q,lq,t)
            f_full=abs(np.vdot(r,out))**2
            f_red=abs(np.vdot(rq,red))**2
            # Match both collective amplitude and experimentally measured right-clique mass.
            assert abs(f_full-f_red)<5e-13
            assert abs(np.sum(abs(out[a:])**2)-np.sum(abs(red[2:])**2))<5e-13
            # Exact dark-state identity for any nonbridge initial vertex.
            local=evolve(H,v,t)
            assert abs(np.sum(abs(local[a:])**2)-np.sum(abs(evolve(Q,iq,t)[2:])**2)/(a-1))<5e-13
            checked+=3
    print('Finite full-space versus quotient and dark-state identities:',checked)
    print('a,b, peak-fidelity, limiting ceiling, scaled upper eigenvalue splitting')
    for a,b in [(40,40),(100,100),(200,200),(50,100),(100,200),(200,400),(100,300),(300,200)]:
        Q,L,R,I=quotient(a,b)
        r=a/b;q=r+1/r
        t=a*b*np.pi/q
        evolved=evolve(Q,L,t)
        f=abs(np.vdot(R,evolved))**2
        total=np.sum(abs(evolved[2:])**2)
        ceiling=predicted(r,np.pi/q)
        ev=eigh(Q)[0]
        print(a,b,round(f,9),round(ceiling,9),round((ev[-1]-ev[-2])*a*b,9))
        assert abs(f-ceiling)<.01
        assert abs(total-ceiling)<.012
        assert abs((ev[-1]-ev[-2])*a*b-q)<.1
        checked+=3
    for a,b in [(50,50),(80,120),(100,200),(240,120)]:
        Q,L,R,I=quotient(a,b);r=a/b
        for s in (0,.2,.5,1,1.7):
            evolved=evolve(Q,L,a*b*s)
            f=abs(np.vdot(R,evolved))**2
            total=np.sum(abs(evolved[2:])**2)
            limit=predicted(r,s)
            assert abs(f-limit)<.06
            assert abs(total-limit)<.06
            checked+=2
    print('Total finite diagnostics:',checked)
if __name__=='__main__':main()
