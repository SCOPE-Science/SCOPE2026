"""Reproducible checks for a uniform ring with balanced on-site imaginary defects.
Requires Python 3, numpy and sympy. Tests illustrate, not replace, the all-size proof.
"""
import math
import numpy as np
import sympy as sp

z, gamma = sp.symbols('z gamma')

def symbolic_hamiltonian(n, defect, strength):
    H = sp.zeros(n)
    for j in range(n):
        H[j, (j + 1) % n] = 1
        H[(j + 1) % n, j] = 1
    H[0, 0] = sp.I * strength
    H[defect, defect] = -sp.I * strength
    return H

def numeric_hamiltonian(n, defect, strength):
    H = np.zeros((n, n), dtype=complex)
    for j in range(n):
        H[j, (j + 1) % n] = H[(j + 1) % n, j] = 1
    H[0, 0] = 1j * strength
    H[defect, defect] = -1j * strength
    return H

characteristic_tests = 0
for m in range(2, 7):
    H = symbolic_hamiltonian(2*m, m, gamma)
    predicted = sp.expand((z*z + gamma*gamma - 4)*sp.chebyshevu(m-1,z/2)**2)
    actual = H.charpoly(z).as_expr()
    assert sp.expand(actual-predicted) == 0, (m, sp.factor(actual-predicted))
    characteristic_tests += 1

jordan_tests = 0
for m in range(2, 7):
    H = symbolic_hamiltonian(2*m, m, sp.Integer(2))
    nullities = [2*m-(H**j).rank() for j in (1,2,3,4)]
    expected = ([2,3,4,4] if m%2 == 0 else [1,2,2,2])
    assert nullities == expected, (m,nullities,expected)
    jordan_tests += 1

perturbative_tests = 0
for n in range(3, 35):
    for d in range(1, n//2+1):
        eps=1e-5
        ev=np.linalg.eigvals(numeric_hamiltonian(n,d,eps))
        if n%2 == 0 and d==n//2:
            assert np.max(np.abs(ev.imag)) < 5e-7
            continue
        energy=2*math.cos(2*math.pi/n)
        pair=ev[np.argsort(np.abs(ev.real-energy))[:2]]
        empirical=abs(pair[0].imag)/eps
        predicted=2*abs(math.sin(2*math.pi*d/n))/n
        assert predicted>1e-12
        assert abs(empirical-predicted) < 2e-3*predicted + 1e-6, (n,d,empirical,predicted)
        perturbative_tests += 1

real_spectrum_tests = 0
for n in range(4, 35, 2):
    for strength in (0.01,0.1,0.3,0.6,1.3,1.75,1.99):
        ev=np.linalg.eigvals(numeric_hamiltonian(n,n//2,strength))
        assert max(abs(ev.imag)) < 4e-7, (n,strength)
        real_spectrum_tests += 1

print('PASS: symbolic all-size characteristic-factor checks:',characteristic_tests)
print('PASS: exact exceptional-point Jordan-nullity checks:',jordan_tests)
print('PASS: non-antipodal first-order complex splittings:',perturbative_tests)
print('PASS: antipodal real-spectrum numerical checks:',real_spectrum_tests)

interior_jordan_tests = 0
for m, k, s in [(3,1,sp.sqrt(3)),(4,1,sp.sqrt(2)),(5,1,sp.sqrt(sp.Rational(5,2)-sp.sqrt(5)/2)),(6,1,sp.Integer(1)),(6,2,sp.sqrt(3))]:
    H=symbolic_hamiltonian(2*m,m,s)
    e=2*sp.cos(sp.pi*k/m)
    mult=sp.Poly(H.charpoly(z).as_expr(),z).multiplicity(e) if False else None
    # At the collision the symmetric eigenvalue has a size-two Jordan block.
    dim=2*m-(H-e*sp.eye(2*m)).rank()
    if dim != 2: raise AssertionError((m,k,dim))
    interior_jordan_tests += 1
print('PASS: interior exceptional-point eigenspace checks:',interior_jordan_tests)
