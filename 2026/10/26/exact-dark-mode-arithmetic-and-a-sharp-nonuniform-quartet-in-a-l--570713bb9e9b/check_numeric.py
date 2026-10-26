"""Independent numerical check of the loss-free spectrum and endpoint survival."""
import numpy as np

def test(m):
    N=12*m+2; M=2*N; a=1.0; b=2**.5; Gamma=0.7
    H=np.diag([a if j%2==0 else b for j in range(M-1)],1)
    H=H+H.T
    vals,V=np.linalg.eigh(H)
    abs_at_loss=np.abs(V[4,:])
    dark=np.flatnonzero(abs_at_loss<1e-10)
    expected=np.array([-np.sqrt(2+np.sqrt(3)),-np.sqrt(2-np.sqrt(3)),np.sqrt(2-np.sqrt(3)),np.sqrt(2+np.sqrt(3))])
    assert len(dark)==4,(m,len(dark))
    assert np.allclose(np.sort(vals[dark]),expected,atol=1e-10)
    survival=(np.abs(V[0,dark])**2).sum()
    exact=2*(8*m+1)/(3*(8*m+1)**2-1)
    assert np.isclose(survival,exact,atol=1e-11),(m,survival,exact)
    nonherm=H.astype(complex)
    nonherm[4,4]=-1j*Gamma
    eig=np.linalg.eigvals(nonherm)
    assert sum(abs(eig.imag)<1e-12)==4,(m,np.sort(abs(eig.imag))[:7])
    assert all(eig.imag<=1e-8)
    print(f'N={N:3d}, loss-site=5, dark=4, survival={survival:.15f}, formula={exact:.15f}')

if __name__=='__main__':
    for m in (1,2,3):test(m)
    print('numerical independent check: PASS')
