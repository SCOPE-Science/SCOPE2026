"""Independent finite-dimensional checks of the single-defect diamond flat-band transfer identities.

Dependencies: Python 3, NumPy. Run `python verify.py`.
"""
import numpy as np
from numpy.linalg import eigvalsh, eigh, norm, solve


def matrices(n, delta):
    assert n >= 2 and abs(delta) < 1
    b = np.zeros((n, 2*n))
    for j in range(n):
        b[j, 2*j:2*j+2] += 1.
        if j:
            if j == 1:
                b[j, :2] += [1+delta, 1-delta]
            else:
                b[j, 2*j-2:2*j] += 1.
    m = b @ b.T
    p = np.eye(2*n) - b.T @ solve(m,b)
    return b,m,p


def formulas(n,delta):
    q=1+(n-1)*delta**2
    eta_s=1/(2*q)
    eta_r=(1+n*delta**2)/(2*q)
    lam=(-1)**(n+1)*delta/(2*q)
    c=0. if delta == 0 else 1/np.sqrt(1+n*n*delta*delta/4)
    return eta_s,eta_r,lam,c


def run():
    num=0
    worst=0.
    for n in range(2,23):
        for delta in [-.9,-.55,-.13,-.011,0,.011,.13,.55,.9]:
            b,m,p=matrices(n,delta)
            q=1+(n-1)*delta**2
            expected=2**n*q
            det=np.linalg.slogdet(m)
            assert det[0]>0
            err=abs(det[1]-np.log(expected)); worst=max(worst,err); assert err<2e-11
            err=norm(p@p-p,ord=2); worst=max(worst,err); assert err<2e-10
            assert eigvalsh(m)[0]>1e-9
            assert norm(b@p,ord=2)<2e-10
            s,r,lam,c=formulas(n,delta)
            g=np.array([[p[0,0],p[0,2*(n-1)]],[p[2*(n-1),0],p[2*(n-1),2*(n-1)]]])
            err=norm(g-np.array([[s,lam],[lam,r]]),ord=2)
            worst=max(worst,err);assert err<1e-10,(n,delta,err)
            num += 6
            if delta == 0: continue
            # The full effective model uses P to couple the two endpoints to the flat-band subspace.
            h=np.zeros((2+2*n,2+2*n))
            h[0,2:]=p[0,:]
            h[1,2:]=p[2*(n-1),:]
            h[2:,0]=p[:,0]
            h[2:,1]=p[:,2*(n-1)]
            spec,u=eigh(h)
            sep=np.sqrt((s-r)**2+4*lam**2)
            vals=eigvalsh(g)
            for t in [.1,1.7,3.1,7.9,12.2]:
                exact=np.dot(u[1,:]*u[0,:],np.exp(-1j*spec*t))
                analytic=(lam/sep)*(np.cos(np.sqrt(vals[1])*t)-np.cos(np.sqrt(vals[0])*t))
                err=abs(exact-analytic);worst=max(worst,err)
                assert err<1e-10,(n,delta,t,err)
                assert abs(exact)<=c+1e-12
                num+=2
    # Scaling check: for delta=c/n, the slow frequency splitting behaves as g*c*sqrt(c^2+4)/(2*sqrt(2)*n).
    for c in [0.25,0.6,1.3,2.1]:
        gap_ratios=[]
        for n in [40,80,160,400]:
            d=c/n; s,r,lam,_=formulas(n,d)
            ev=eigvalsh(np.array([[s,lam],[lam,r]]))
            gap=np.sqrt(ev[1])-np.sqrt(ev[0])
            gap_ratios.append(n*gap)
        limit=c*np.sqrt(c*c+4)/(2*np.sqrt(2))
        assert abs(gap_ratios[-1]-limit)<0.02,(c,gap_ratios,limit)
        num+=1
    print(f'PASS {num} independent numerical comparisons; max observed error {worst:.3e}.')

if __name__ == '__main__':
    run()
