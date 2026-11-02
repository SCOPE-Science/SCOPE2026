"""Finite-dimensional consistency checks for antilinear trace-frame ranges.

The general statement is proved analytically; these computations test only
finite matrix identities, extremizers and zero-valued frames.
"""
import numpy as np


def unitary(n, rng):
    a = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    q, r = np.linalg.qr(a)
    phase = np.diag(r)
    return q @ np.diag(phase / np.abs(phase))


def zero_frame(diag, k):
    n = len(diag)
    cols = []
    if k % 2 == 0:
        pair_count = k // 2
    elif k < n:
        pair_count = (k-1) // 2
    else:
        pair_count = (k-3) // 2
    for j in range(pair_count):
        a, b = 2*j, 2*j+1
        v = np.zeros(n, dtype=complex)
        w = np.zeros(n, dtype=complex)
        v[a],v[b]=1/np.sqrt(2),1j/np.sqrt(2)
        w[a],w[b]=1j/np.sqrt(2),1/np.sqrt(2)
        cols.extend([v,w])
    if k % 2:
        h = 2*pair_count
        if k < n:
            a,b=float(diag[h]), float(diag[h+1])
            v=np.zeros(n,dtype=complex)
            if a+b==0:
                v[h]=1
            else:
                v[h]=np.sqrt(b/(a+b))
                v[h+1]=1j*np.sqrt(a/(a+b))
            cols.append(v)
        else:
            a,b,c=map(float,diag[h:h+3])
            t=0.0 if a+b==0 else c/(a+b)
            theta=np.arccos(t)/2
            p=np.cos(theta)
            q=1j*np.sin(theta)
            v=np.zeros(n,dtype=complex); w=np.zeros(n,dtype=complex)
            z=np.zeros(n,dtype=complex)
            v[h],v[h+1]=p,q
            w[h],w[h+1]=q,p
            z[h+2]=1j
            cols.extend([v,w,z])
    return np.stack(cols,axis=1)


def check():
    rng=np.random.default_rng(20261027)
    count=0
    for n in range(2,11):
        for sample in range(20):
            singular=np.sort(rng.uniform(0.0,4.0,size=n))[::-1]
            if sample%5==0:
                singular[-1]=0.
            if sample%7==0:
                singular[:]=singular[0]
            U=unitary(n,rng)
            symmetric=U @ np.diag(singular) @ U.T
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
            skew=raw-raw.T
            B=symmetric+skew
            for k in range(1,n+1):
                if k==1:
                    pass
                # A frame that realizes the entire Ky Fan boundary.
                positive=np.conjugate(U[:,:k])
                val=sum(positive[:,j].T @ B @ positive[:,j] for j in range(k))/k
                target=sum(singular[:k])/k
                assert abs(val-target)<5e-10, (n,k,val,target)
                count+=1
                # Explicit frame that realizes zero in every dimension >=2.
                Z0=zero_frame(singular,k)
                assert np.max(abs(Z0.conj().T @ Z0-np.eye(k)))<5e-10
                Z=np.conjugate(U)@Z0
                assert np.max(abs(Z.conj().T @ Z-np.eye(k)))<5e-10
                z=sum(Z[:,j].T @ B @ Z[:,j] for j in range(k))/k
                assert abs(z)<5e-10, (n,k,z)
                count+=3
                # Random frame: cannot exceed the predicted radius.
                R=unitary(n,rng)[:,:k]
                random_value=sum(R[:,j].T @ B @ R[:,j] for j in range(k))/k
                assert abs(random_value)<=target+5e-10
                count+=1
            # Ky Fan sums invert to exactly the starting spectrum.
            radii=np.cumsum(singular)/np.arange(1,n+1)
            reconstructed=np.diff(np.r_[0.,np.arange(1,n+1)*radii])
            assert np.allclose(reconstructed,singular,atol=1e-12)
            count+=1
    print(f"PASS: {count} finite matrix assertions, n=2..10, 20 samples each")


if __name__=='__main__':
    check()
