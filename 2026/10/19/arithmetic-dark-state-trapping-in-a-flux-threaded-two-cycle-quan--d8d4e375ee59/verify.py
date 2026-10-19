"""Finite-matrix checks of exact dark-state and survival formulas."""
import math
import numpy as np


def matrix(m, n, flux_a, flux_b, hopping=1.0):
    assert m >= 3 and n >= 3 and hopping > 0
    h = np.zeros((m+n-1, m+n-1), dtype=np.complex128)
    for length, first, phi in ((m, 1, flux_a), (n, m, flux_b)):
        edges = [(0, first, hopping)]
        edges += [(first+j, first+j+1, hopping) for j in range(length-2)]
        edges += [(0, first+length-2, hopping*np.exp(1j*phi))]
        for x, y, z in edges:
            h[x,y] = z
            h[y,x] = np.conj(z)
    return h


def dark_basis(m, n, flux_a, flux_b):
    size = m+n-1
    g = math.gcd(m,n)
    columns=[]
    energies=[]
    for r in range(1,g):
        k=m*r//g
        ell=n*r//g
        ua=np.zeros(size,complex)
        ub=np.zeros(size,complex)
        ua[1:m]=np.sqrt(2/m)*np.sin(np.pi*k*np.arange(1,m)/m)
        ub[m:]=np.sqrt(2/n)*np.sin(np.pi*ell*np.arange(1,n)/n)
        a=np.sqrt(2/m)*np.sin(np.pi*r/g)*(1-(-1)**k*np.exp(1j*flux_a))
        b=np.sqrt(2/n)*np.sin(np.pi*r/g)*(1-(-1)**ell*np.exp(1j*flux_b))
        columns.append((b*ua-a*ub)/np.hypot(abs(a),abs(b)))
        energies.append(2*np.cos(np.pi*r/g))
    if not columns:
        return np.empty((size,0),complex),np.array([])
    return np.column_stack(columns),np.array(energies)


def survival(m, n, phi, psi, side, j):
    length = m if side == 0 else n
    g=math.gcd(m,n)
    val=0.0
    for r in range(1,g):
        a=abs(1-(-1)**(m*r//g)*np.exp(1j*phi))**2/m
        b=abs(1-(-1)**(n*r//g)*np.exp(1j*psi))**2/n
        factor=b/(a+b) if side==0 else a/(a+b)
        val+=2/length*factor*np.sin(np.pi*r*j/g)**2
    return val


def test():
    comparisons=0
    maximum=0.0
    phase_pairs=((np.pi/2,np.pi/2), (np.pi/2,3*np.pi/2), (0.37,2.03), (2.66,0.71))
    for m in range(3,16):
        for n in range(3,16):
            for phi,psi in phase_pairs:
                h=matrix(m,n,phi,psi)
                d,e=dark_basis(m,n,phi,psi)
                assert d.shape[1]==math.gcd(m,n)-1
                p=d@d.conj().T
                if e.size:
                    maximum=max(maximum,float(np.max(abs(h@d-d*e))))
                    maximum=max(maximum,float(np.max(abs(d.conj().T@d-np.eye(len(e))))))
                for side,(length,offset) in enumerate(((m,1),(n,m))):
                    for j in range(1,length):
                        observed=p[offset+j-1,offset+j-1].real
                        formula=survival(m,n,phi,psi,side,j)
                        maximum=max(maximum,abs(observed-formula))
                        if np.isclose(abs(np.cos(phi)),0.0,atol=1.e-12) and np.isclose(abs(np.cos(psi)),0.0,atol=1.e-12):
                            target=math.gcd(m,n)/(m+n) if j%math.gcd(m,n) else 0.
                            maximum=max(maximum,abs(observed-target))
                        comparisons+=1
    # Directly verify dissipative spectral count and negativity off the dark space.
    for m,n in ((3,3),(4,6),(6,9),(7,8),(6,12),(8,10)):
        h=matrix(m,n,0.37,2.03)
        loss=h.copy();loss[0,0]-=0.6j
        ev=np.linalg.eigvals(loss)
        count=np.sum(abs(ev.imag)<1.e-8)
        assert count==math.gcd(m,n)-1, (m,n,count)
        assert all(z.imag<1.e-8 for z in ev)
    print(f'PASS: {comparisons} site comparisons; worst residual {maximum:.3e}; six lossy spectrum checks')
    assert maximum < 2.e-12


if __name__=='__main__':
    test()
