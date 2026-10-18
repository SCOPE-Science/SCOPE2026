"""Independent discretized generator checks for a spatially varying velocity-jump model.
Scientific parameters are dimensionless: interval and speed one.
"""
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

def formula(lam,s):
    # midpoint quadrature exact for piecewise constant rate on mesh cells
    h=1/len(lam); centers=(np.arange(len(lam))+.5)*h
    eta=sum(lam)*h; moment=sum(lam*centers)*h
    # for s=mesh midpoint: split current-cell contribution in two halves
    i=int(np.floor(s/h)); i=min(i,len(lam)-1)
    a=sum(lam[:i])*h + lam[i]*(s-i*h)
    b=sum(lam[:i]*centers[:i])*h + lam[i]*(s*s-(i*h)**2)/2
    C=(.5+moment)/(1+eta)
    return C*(1+2*a)-2*b

def lattice(lam):
    m=len(lam); dx=1/m; row=[]; col=[]; data=[]
    for i in range(m):
      for direction in [0,1]:
        j=2*i+direction
        row.append(j);col.append(j);data.append(m+lam[i])
        row.append(j);col.append(2*i+(1-direction));data.append(-lam[i])
        ni=i+(1 if direction else -1)
        if 0 <= ni < m:
           row.append(j);col.append(2*ni+direction);data.append(-m)
    Q=coo_matrix((data,(row,col)),shape=(2*m,2*m)).tocsr()
    ans=spsolve(Q,np.ones(2*m))
    return .5*(ans[::2]+ans[1::2])

def run():
    for mode in ('uniform','source_left','split_endpoints'):
      errs=[]
      for m in (40,80,160,320,640,1280):
        x=(np.arange(m)+.5)/m
        if mode=='uniform': rate=np.ones(m)*1.7
        elif mode=='source_left': rate=np.where((x>=.65)&(x<.75),30.,0.)
        else: rate=np.where((x<.1)|(x>.9),15.,0.)
        calculated=lattice(rate)
        reference=np.array([formula(rate,xi) for xi in x])
        max_err=max(abs(calculated-reference));errs.append(max_err)
        eta=rate.mean()
        low=.5-eta*np.abs(x-.5)/(1+eta)
        high=(1+eta)/2
        assert all(reference >= low-1e-12) and all(reference <= high+1e-12)
      print(mode, 'm sizes',(40,80,160,320,640,1280),'errors',np.array(errs).round(9))
      assert errs[-1]<.02
      assert errs[-1] < errs[0]*.3
    print('PASS finite-state Markov-chain validation against PDE formula and sharp bounds')

if __name__=='__main__':run()

def sharpness_checks():
    """Check concentration sequences using exact integrals for piecewise-constant rates."""
    s=.3; eta=2.; bounds=(.5-eta*abs(s-.5)/(1+eta),(.5*(1+eta)))
    for m in (200,400,800,1600,3200):
        centers=(np.arange(m)+.5)/m
        h=1/m
        # source-adjacent rightward layer of total dimensionless mass eta
        interior=(centers>=s)&(centers<s+10*h)
        left=np.zeros(m);left[interior]=eta/(sum(interior)*h)
        # equal intensity in two narrow endpoint strips
        edges=(centers<10*h)|(centers>1-10*h)
        right=np.zeros(m);right[edges]=eta/(sum(edges)*h)
        lo=formula(left,s);hi=formula(right,s)
        assert lo>bounds[0]-1e-9 and hi<bounds[1]+1e-9
        assert abs(lo-bounds[0])<12*h
        assert abs(hi-bounds[1])<12*h
    for m in (64,128,256):
        x=(np.arange(m)+.5)/m
        rate=1+4*(x-.5)**2
        assert all(formula(rate,s)>=.5-1e-12 for s in x)
    print('PASS extremizing layer convergence and symmetric-profile obstruction')

if __name__=='__main__':sharpness_checks()
