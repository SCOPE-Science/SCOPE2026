"""Reproducible numerical tests for rare-tumbling entropy production.

The analytic proof, not finite discretization, establishes the universal limit.
"""
import math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve


def exact_monostable(b, T, v, r):
    """Independent evaluation of the two-decay-mode stationary solution."""
    coeffs = [1, 2*b/T, -((v*v-b*b)/(T*T)+2*r/T), -2*r*b/(T*T)]
    roots = np.roots(coeffs)
    neg = sorted([-float(np.real(z)) for z in roots if abs(np.imag(z)) < 1e-8 and np.real(z)<0])
    assert len(neg) == 2
    l1,l2=neg
    w1=l1*(b-T*l1)
    w2=l2*(b-T*l2)
    f1=-w2/(w1-w2)
    f2=1-f1
    assert min(f1,f2)>-1e-9
    pzero=(f1*l1+f2*l2)/2
    # This expression follows from stationary force-current balance.
    entropy=(v*v-b*b)/T+2*b*pzero
    return entropy, pzero, neg


def stationary_fv(b,T,v,r,L,dx,shape='bistable'):
    """Finite-volume reflected-state generator for the two-orientation diffusion."""
    n=int(round(2*L/dx))+1
    xx=np.linspace(-L,L,n)
    dx=xx[1]-xx[0]
    if shape=='bistable':
        a=1.3
        force=np.where(abs(xx)>a,-b*np.sign(xx),b*np.sign(xx))
    elif shape=='monostable':
        force=-b*np.sign(xx)
    elif shape=='irregular':
        force=np.where(abs(xx)>2.5,-b*np.sign(xx), 0.7*np.sin(2*xx)+0.45)
    else:
        raise ValueError(shape)
    rows=[];cols=[];vv=[]
    for orientation in range(2):
        state= 1 if orientation==0 else -1
        drift=force+state*v
        for i in range(n):
            u=orientation*n+i
            right=(T/dx**2+max(float(drift[i]),0)/dx) if i<n-1 else 0
            left=(T/dx**2+max(float(-drift[i]),0)/dx) if i>0 else 0
            flip=r
            for j,k in ((u+1,right),(u-1,left),((1-orientation)*n+i,flip)):
                if k:
                    rows.append(j); cols.append(u); vv.append(k)
            rows.append(u);cols.append(u);vv.append(-right-left-flip)
    M=coo_matrix((vv,(rows,cols)),shape=(2*n,2*n)).tolil()
    M[-1,:]=np.ones((1,2*n))
    rhs=np.zeros(2*n);rhs[-1]=1
    pi=spsolve(M.tocsc(),rhs)
    assert abs(pi.sum()-1)<5e-9
    assert min(pi)>-1e-9
    ep=(v/T)*(v+np.dot(force,pi[:n]-pi[n:]))
    pinner=sum(pi[:n][abs(xx)<2.5])+sum(pi[n:][abs(xx)<2.5])
    return float(ep),float(pinner),n


def main():
    b,T=1.0,0.7
    nchecks=0
    for v in (0.45,0.8,1.0,1.3,1.5,2.2):
        target=max(0.0,(v*v-b*b)/T)
        ee=[]
        for r in (0.2,0.04,0.008,0.0016,0.00032):
            ep,center,rs=exact_monostable(b,T,v,r)
            assert ep>=-1e-9
            ee.append(ep)
            nchecks+=2
        assert abs(ee[-1]-target)<0.10
        assert ee[-1]<ee[0]
        nchecks+=2
        print(f'monostable v={v:.2f} target={target:.8f} r=0.00032: {ee[-1]:.8f}')
    print('Finite-volume checks for differing interior forces (errors include grid truncation):')
    for shape in ('monostable','bistable','irregular'):
        for v,r,L in ((1.5,0.10,125),(1.5,0.03,250),(0.6,0.03,100)):
            ep,inner,nn=stationary_fv(b,T,v,r,L,0.45,shape)
            ex=exact_monostable(b,T,v,r)[0] if shape=='monostable' else float('nan')
            assert ep>=0
            assert ep < v*v/T+1e-8
            if shape=='monostable':
                assert abs(ep-ex)<0.16
            nchecks+=3
            print(f'{shape} v={v} r={r} ep={ep:.7f} monostable={ex:.7f} innerProb={inner:.6f} grid={nn}')
    print(f'PASS: {nchecks} deterministic checks.')


if __name__ == '__main__':
    main()
