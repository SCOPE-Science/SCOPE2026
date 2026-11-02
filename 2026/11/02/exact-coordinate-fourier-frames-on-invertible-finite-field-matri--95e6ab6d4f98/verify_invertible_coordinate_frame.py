"""Independent finite-field enumeration of coordinate-character Gram matrices.
Run with Python 3 and NumPy: python verify_invertible_coordinate_frame.py
The exact formulas in RESULT.md establish the all-prime-power theorem; these
finite tests independently exercise the entrywise character conventions.
"""
import itertools
import math
import numpy as np


def full_rank(a, p, d):
    a = [list(a[i*d:(i+1)*d]) for i in range(d)]
    row = 0
    for col in range(d):
        pivot = next((r for r in range(row, d) if a[r][col] % p), None)
        if pivot is None:
            return False
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col] % p, -1, p)
        a[row] = [(u*inv) % p for u in a[row]]
        for r in range(row+1, d):
            scale = a[r][col]
            a[r] = [(x-scale*y) % p for x,y in zip(a[r],a[row])]
        row += 1
    return True


def theoretical(p, d):
    b = -1/(p**d-1)
    c = 1/((p**d-1)*(p**(d-1)-1))
    return (1+2*(d-1)*b+(d-1)**2*c,
            1+(d-2)*b-(d-1)*c,
            1-2*b+c), b,c


def check(p, d):
    count = 0
    size = d*d
    omega = np.exp(2j*np.pi/p)
    M = np.zeros((size+1,size+1),dtype=np.complex128)
    for entries in itertools.product(range(p),repeat=size):
        if not full_rank(entries,p,d):
            continue
        count += 1
        x = np.asarray([1]+[omega**k for k in entries])
        M += np.outer(np.conjugate(x),x)
    expected_count = math.prod(p**d-p**j for j in range(d))
    assert count == expected_count, (p,d,count,expected_count)
    M /= count
    (lam0,lam1,lam2), b,c=theoretical(p,d)
    T=np.zeros_like(M)
    T[0,0]=1
    T[0,1:]=b
    T[1:,0]=b
    for a in range(size):
        for z in range(size):
            T[a+1,z+1]=1 if a==z else b if (a//d==z//d or a%d==z%d) else c
    gram_err = np.max(np.abs(M-T))
    assert gram_err < 1e-10, (p,d,gram_err)
    got=np.linalg.eigvalsh(M)
    mu_minus=(1+lam0-np.sqrt((1-lam0)**2+4*d*d*b*b))/2
    mu_plus=(1+lam0+np.sqrt((1-lam0)**2+4*d*d*b*b))/2
    target=np.array(sorted([mu_minus,mu_plus]+[lam1]*(2*(d-1))+[lam2]*((d-1)**2)))
    assert len(got)==len(target)
    eig_err=np.max(np.abs(got-target))
    assert eig_err < 1e-10, (p,d,eig_err)
    assert min(got)>0
    if (p,d)!=(2,2):
        assert lam0<lam1<lam2
    else:
        assert abs(lam0-lam1)<1e-12
    assert (mu_plus < lam2 if d<=3 else mu_plus>lam2)
    print('PASS',p,d,'invertible',count,'entries',size,'max_gram_error',round(float(gram_err),13),'max_spectrum_error',round(float(eig_err),13),'eigenvalues',tuple(round(float(t),9) for t in (mu_minus,mu_plus,lam1,lam2)))


if __name__=='__main__':
    for p,d in [(2,2),(3,2),(5,2),(2,3),(3,3),(2,4)]:
        check(p,d)
    print('ALL_CHECKS_PASS')
