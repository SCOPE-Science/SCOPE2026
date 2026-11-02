"""Independent coefficient-recursion and finite-chain tests for a tilted Lindblad walk.

Requires Python 3.10+, NumPy, SciPy. Run: python verify.py
"""
import math
import numpy as np
from scipy.sparse import diags, identity, kron, coo_matrix
from scipy.sparse.linalg import expm_multiply


def closed_rates(gamma, w, c, e):
    a = gamma + 2 * w
    d = a*a + e*e
    k2 = 2*w + c*c*a/d
    k4 = (2*w + c*c*(a*d + 12*w*(e*e-a*a))/d**2
           - 3*a*c**4*(a**4+10*a*a*e*e-3*e**4)/(d**3*(a*a+4*e*e)))
    return k2, k4


def independent_taylor_rates(gamma, w, c, e, radius=5):
    """Recursively solve a finite tilt-jet eigenproblem, not the closed formula."""
    a = gamma + 2*w
    n = 2*radius+1
    center = radius
    z0 = np.zeros((n,n), dtype=complex)
    for j in range(n):
        r = j-radius
        if r: z0[j,j] = -a-1j*e*r
    z1 = np.zeros_like(z0)
    for j in range(n-1):
        z1[j,j+1] = -1j*c/2
        z1[j+1,j] = +1j*c/2
    z2 = np.zeros_like(z0)
    z2[center,center] = w
    blocks = [None,z1,z2,z1/24,z2/12]
    v0 = np.zeros(n,complex)
    v0[center]=1
    vectors=[v0]
    coeffs=[0]
    for order in range(1,5):
        source=sum(blocks[j] @ vectors[order-j] for j in range(1,order+1))
        co = source[center]
        coeffs.append(co)
        rhs=source-sum(coeffs[j]*vectors[order-j] for j in range(1,order))
        vv=np.zeros(n,complex)
        for j in range(n):
            if j!=center: vv[j]=rhs[j]/(-z0[j,j])
        vectors.append(vv)
    return float((2*coeffs[2]).real), float((24*coeffs[4]).real)


def threshold(gamma,w):
    a=gamma+2*w
    zstar=(5+2*math.sqrt(7))/3
    return a*math.sqrt(zstar)


def direct_cumulants(gamma,w,c,e,t,size=61):
    """Independent finite-volume density-matrix Lindblad propagation."""
    coords=np.arange(size)-size//2
    ham=diags([np.full(size-1,-c/2),e*coords,np.full(size-1,-c/2)],
              [-1,0,1],format='csr',dtype=complex)
    eye=identity(size,format='csr')
    op=-1j*(kron(ham,eye,format='csr')-kron(eye,ham.T,format='csr'))
    row=np.repeat(np.arange(size),size)
    col=np.tile(np.arange(size),size)
    op=op+diags(np.where(row==col,-2*w,-gamma-2*w),0,format='csr')
    target=[];source=[];values=[]
    for n in range(1,size-1):
        for m in (n-1,n+1):
            target.append(m*size+m)
            source.append(n*size+n)
            values.append(w)
    op=op+coo_matrix((values,(target,source)),shape=(size*size,size*size)).tocsr()
    seed=np.zeros(size*size,dtype=complex)
    seed[(size//2)*size+size//2]=1.
    solution=expm_multiply(t*op,seed).reshape(size,size)
    prob=solution.diagonal().real
    moment2=float(np.dot(coords**2,prob))
    moment4=float(np.dot(coords**4,prob))
    return moment2,moment4-3*moment2**2,float(np.sum(prob)),float(sum(prob[:5])+sum(prob[-5:]))


def main():
    count=0
    samples=[(.6,.2,1.2,0),(.6,.2,1.2,.8),(.6,.2,1.2,2.5),
             (1.,0,1.5,1.4),(1.,0,1.5,2.3),(1.,0,.1,.6),
             (.2,.1,4.,3.),(.04,.5,2.3,2.9),(1.7,0,.6,0),
             (.8,.3,3.5,0.1)]
    for par in samples:
        expect=closed_rates(*par)
        actual=independent_taylor_rates(*par)
        for a,b in zip(actual,expect):
            assert abs(a-b)<=2e-9*(1+abs(b)),(par,actual,expect)
            count+=1
    # Structural positivity on either side of the universal field barrier.
    zstar=(5+2*math.sqrt(7))/3
    for a in (.8,1.2,2.4):
        for s in (0,.15,.4):
            w=a*s
            gamma=a-2*w
            for z in (zstar,zstar+0.01,4.,10.):
                for y in (.01,.3,1.,5.,30.):
                    k4=closed_rates(gamma,w,a*math.sqrt(y),a*math.sqrt(z))[1]
                    assert k4>0,(a,s,z,y,k4)
                    count+=1
    # Below the barrier there is precisely one positive quartic zero.
    for s in (0.,.1,.4):
        a=1.0
        w=s*a
        gamma=a-2*w
        for z in (0,.1,.9,2.5,zstar-.001):
            b=(1+z+12*s*(z-1))/(1+z)**2
            coeff=3*(1+10*z-3*z*z)/((1+z)**3*(1+4*z))
            yy=(b+math.sqrt(b*b+8*s*coeff))/(2*coeff)
            # The critical polynomial has one positive solution by sign/shape.
            assert yy>0
            left=closed_rates(gamma,w,math.sqrt(yy*.5),math.sqrt(z))[1]
            mid=closed_rates(gamma,w,math.sqrt(yy),math.sqrt(z))[1]
            right=closed_rates(gamma,w,math.sqrt(yy*1.5),math.sqrt(z))[1]
            assert left>0 and right<0 and abs(mid)<1e-7,(s,z,left,mid,right)
            count+=3
    # Completely separate finite-chain Lindblad propagation: check trend and mass.
    low=direct_cumulants(.6,.2,1.2,0.,t=10)
    high=direct_cumulants(.6,.2,1.2,2.5,t=10)
    assert low[1]<0<high[1],(low,high)
    assert abs(low[2]-1)<1e-6 and abs(high[2]-1)<1e-6
    assert low[3]<.0001 and high[3]<.0001
    count+=6
    print('PASS',count,'deterministic independent numerical checks')
    print('Representative zero-field and strong-field finite-time cumulants:',low[1],high[1])


if __name__=='__main__': main()
