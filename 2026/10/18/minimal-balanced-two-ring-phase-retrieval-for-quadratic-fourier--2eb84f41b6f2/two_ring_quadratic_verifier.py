"""Reproducible algebraic and numerical checks for quadratic phaseless sampling.

Requires SymPy and NumPy. The theorem itself is proved analytically in RESULT.md.
"""
import math
import numpy as np
import sympy as sp


def hermitian_measurement_row(z):
    """Coefficients in [H00,H11,H22,Re H10,Im H10,Re H21,Im H21,Re H20,Im H20]."""
    x, y = sp.re(z), sp.im(z)
    radius2 = sp.expand(x*x + y*y)
    return [sp.Integer(1),radius2,radius2**2,2*x,-2*y,2*radius2*x,-2*radius2*y,
            2*(x*x-y*y),-4*x*y]


def exact_check():
    r = sp.Rational(1,2)
    s = sp.Integer(1)
    root2 = sp.sqrt(2)
    inner = [r,sp.I*r,-r,-sp.I*r]
    outer = [s*(1+sp.I)/root2,s*(-1+sp.I)/root2,
             s*(-1-sp.I)/root2,s*(1-sp.I)/root2]
    matrix = sp.Matrix([hermitian_measurement_row(z) for z in inner+outer])
    assert matrix.rank() == 8
    null = matrix.nullspace()
    assert len(null) == 1
    target = sp.Matrix([1,-5,4,0,0,0,0,0,0])
    assert null[0] == target*null[0][0]

    same_rings = [r,sp.I*r,-r,-sp.I*r]+[r*(1+sp.I)/root2,r*(-1+sp.I)/root2,
                                        r*(-1-sp.I)/root2,r*(1-sp.I)/root2]
    assert sp.Matrix([hermitian_measurement_row(z) for z in same_rings]).rank() < 8
    zero_twist = inner+[s,sp.I*s,-s,-sp.I*s]
    assert sp.Matrix([hermitian_measurement_row(z) for z in zero_twist]).rank() == 7

    # For a fixed radius, the constant and linear monomials are indistinguishable.
    for z in same_rings:
        assert sp.simplify(abs(complex(sp.N(z)))**2 - float(r*r)) < 1e-13
    # For no twist, opposite quadratic phases have the same measured moduli.
    for z in zero_twist:
        val = complex(sp.N(z))
        assert abs(abs(1+1j*val**2)**2-abs(1-1j*val**2)**2) < 1e-12

    theta = sp.symbols('theta',real=True)
    angular_rows = sp.Matrix([[1,0],[sp.cos(2*theta),-sp.sin(2*theta)]])
    gram = sp.simplify(angular_rows*angular_rows.T)
    assert sp.simplify(gram.det()-sp.sin(2*theta)**2) == 0
    assert sp.simplify(gram.trace()-2) == 0
    return matrix


def block_check(trials=1500):
    rng = np.random.default_rng(19731)
    success = 0
    for _ in range(trials):
        r,s = rng.uniform(0.15,2.5,2)
        if abs(r-s)<0.05: s += 0.5
        phi = rng.uniform(0,2*math.pi)
        delta = rng.uniform(0.1,1.2)
        psi = phi+delta
        coeff = rng.normal(size=3)+1j*rng.normal(size=3)
        measured = []
        for radius,angle in [(r,phi),(s,psi)]:
            zs = np.asarray([radius*np.exp(1j*(angle+j*np.pi/2)) for j in range(4)])
            vals = np.abs(coeff[0]+coeff[1]*zs+coeff[2]*zs**2)**2
            A = vals.mean()
            B = sum(vals[j]*np.exp(-1j*(angle+j*np.pi/2)) for j in range(4))/4
            C = sum(vals[j]*(-1)**j for j in range(4))/4
            measured.append((A,B,C))
        a0,b0,c0 = coeff
        diag = np.abs(coeff)**2
        x=b0*np.conj(a0)
        y=c0*np.conj(b0)
        z=c0*np.conj(a0)
        for (radius,angle),(A,B,C) in zip([(r,phi),(s,psi)],measured):
            assert np.isclose(A,diag[0]+radius**2*diag[1]+radius**4*diag[2],atol=1e-9)
            assert np.isclose(B,radius*x+radius**3*y,atol=1e-9)
            assert np.isclose(C,2*radius**2*np.real(z*np.exp(2j*angle)),atol=1e-9)
        recovered=np.linalg.solve(np.array([[r,r**3],[s,s**3]]),
                                  np.array([measured[0][1],measured[1][1]]))
        assert np.allclose(recovered,[x,y],rtol=1e-9,atol=1e-9)
        recovered_z=np.linalg.solve(
            np.array([[np.cos(2*phi),-np.sin(2*phi)],
                      [np.cos(2*psi),-np.sin(2*psi)]]),
            np.array([measured[0][2]/(2*r**2),measured[1][2]/(2*s**2)]))
        assert np.allclose(recovered_z,[z.real,z.imag],rtol=1e-9,atol=1e-9)
        success += 1
    for d in [math.pi/4,math.pi/8,math.pi/12]:
        matrix=np.array([[1,0],[math.cos(2*d),-math.sin(2*d)]])
        sv=np.linalg.svd(matrix,compute_uv=False)
        expected=np.sqrt([1+abs(math.cos(2*d)),1-abs(math.cos(2*d))])
        assert np.allclose(sv,expected,atol=1e-12)
    return success


if __name__=='__main__':
    exact_check()
    n=block_check()
    print('VERIFY_OK exact rank, kernel, obstruction witnesses, demixing and angular condition; randomized trials:', n)
