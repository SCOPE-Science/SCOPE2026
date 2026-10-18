"""Direct finite Fourier and projector-Gram checks for prime-power cubic chirps.
Computational consistency tests only; the theorem uses exact Gauss-sum algebra.
"""
import numpy as np

def valuation(a,p,k):
    if a==0:return k
    j=0
    while a%p==0:
        a//=p;j+=1
    return j

def theoretical(p,k):
    n=p**k
    expected=np.zeros((n,n),float)
    for a in range(n):
        for b in range(n):
            if a==0:
                expected[a,b]=float(b==0)
                continue
            s=valuation(a,p,k);r=k-s
            B=3*a*a+b
            if p==2:
                if r==1:
                    if B%(2**(s+1))==2**s:expected[a,b]=1.
                elif B%(2**(s+1))==0:
                    expected[a,b]=2.**(1-r)
            elif p==3:
                if r==1:
                    if B%n==0:expected[a,b]=1.
                elif B%(3**(s+1))==0:
                    expected[a,b]=3.**(1-r)
            elif B%(p**s)==0:
                expected[a,b]=float(p**(-r))
    return expected

def predicted_levels(p,k):
    n=p**k
    if p==2:
        vals=[(n,2)]+[(n*2.**(1-r),4**(r-1)) for r in range(2,k+1)]
        rank=(n*n+2)//3
    elif p==3:
        vals=[(n,3)]+[(n*3.**(1-r),2*3**(2*r-2)) for r in range(2,k+1)]
        rank=(n*n+3)//4
    else:
        vals=[(n,1)]+[(n*p**(-r),(p-1)*p**(2*r-1)) for r in range(1,k+1)]
        rank=(p*n*n+1)//(p+1)
    assert sum(m for _,m in vals)==rank
    return vals,rank

def test(p,k):
    n=p**k
    if n>350:raise ValueError('Only moderate numerical sizes tested')
    g=np.exp(2j*np.pi*(np.arange(n,dtype=np.int64)**3%n)/n)/np.sqrt(n)
    obs=np.zeros((n,n))
    for a in range(n):
        obs[a,:]=np.abs(np.fft.ifft(n*np.conj(g)*np.roll(g,a)))**2
    expected=theoretical(p,k)
    err=np.max(np.abs(obs-expected))
    assert err<5e-11,(p,k,err)
    vals,rank=predicted_levels(p,k)
    assert np.count_nonzero(expected)==rank,(p,k,'rank',np.count_nonzero(expected),rank)
    assert abs(np.sum(expected)-n)<5e-8,(p,k,'sum',np.sum(expected))
    eigerr=None
    if n<=16:
        roots=np.exp(2j*np.pi*np.arange(n)/n)
        orbit=np.array([roots[(np.arange(n)*b)%n]*np.roll(g,a) for a in range(n) for b in range(n)])
        K=np.abs(orbit@orbit.conj().T)**2
        eig=np.sort(np.linalg.eigvalsh(K))
        target=np.sort(np.r_[np.zeros(n*n-rank),*[np.repeat(value,mult) for value,mult in vals]])
        eigerr=np.max(np.abs(eig-target))
        assert eigerr<2e-10,(p,k,'Gram',eigerr)
    return n,rank,err,eigerr

if __name__=='__main__':
    cases=[(2,k) for k in range(1,9)]+[(3,k) for k in range(1,6)]+[(5,k) for k in range(1,4)]+[(7,k) for k in range(1,3)]+[(11,k) for k in range(1,3)]+[(13,1)]
    for p,k in cases:
        n,rank,err,eigerr=test(p,k)
        print('p=%d, k=%d, N=%d, rank=%d, ambiguity_error=%.4g, Gram_error=%s'%(p,k,n,rank,err,eigerr))
    print('%d prime-power cases passed.'%len(cases))
