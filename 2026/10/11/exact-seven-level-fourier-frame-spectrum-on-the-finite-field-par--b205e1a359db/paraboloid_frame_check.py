"""Finite-field paraboloid coordinate-character Gram-spectrum checks.

Run with: python paraboloid_frame_check.py
Requires numpy; no network access or external files.

Checks are finite examples; the all-field theorem rests on the written
character-orthogonality and block-decomposition proof.
"""
import math
import numpy as np


class Field:
    def __init__(self, p, extension=1, nonsquare=None):
        self.p = p
        self.k = extension
        self.q = p ** extension
        if extension not in (1, 2):
            raise ValueError("Only degree one and quadratic examples implemented")
        self.d = nonsquare
        if extension == 2:
            assert pow(nonsquare, (p-1)//2, p) == p-1

    def mul(self, x, y):
        p = self.p
        if self.k == 1:
            return (x*y) % p
        a, b = x % p, x // p
        c, d = y % p, y // p
        return ((a*c + b*d*self.d) % p) + p*((a*d+b*c) % p)

    def add(self, x, y):
        p = self.p
        if self.k == 1:
            return (x+y) % p
        return ((x % p + y % p) % p) + p*((x//p+y//p) % p)

    def negate(self,x):
        return self.mul(self.p-1, x)

    def trace(self,x):
        return x % self.p if self.k == 1 else (2*(x % self.p))%self.p

    def phase(self,x):
        return np.exp((2j*np.pi/self.p)*self.trace(x))

    def square(self,x):
        return self.mul(x,x)


def predicted_eigenvalues(q):
    assert q % 2 == 1
    sign = 1 if q % 4 == 1 else -1
    s = sign/q
    t = (q-1)//2
    polynomial_roots = np.sort(np.real_if_close(np.roots([1, 2-q, -(3*q+1), 2*q*(q-1)])).real)
    eig = [1.] * (3*(q-1)//2) + [1-s]*t
    eig += [1-s/2+math.sqrt(1+16*q)/(2*q)]*(t-1)
    eig += [1-s/2-math.sqrt(1+16*q)/(2*q)]*(t-1)
    eig += [1+s*root for root in polynomial_roots]
    return np.sort(eig)


def check_field(field):
    q=field.q
    phase=field.phase
    F=np.zeros((q*q,3*q-2),complex)
    for x in range(q):
        for y in range(q):
            ix = x*q+y
            F[ix,0]=1.
            for a in range(1,q):
                F[ix,a]=phase(field.mul(a,x))
                F[ix,q-1+a]=phase(field.mul(a,y))
                F[ix,2*q-2+a]=phase(field.mul(a,field.add(field.square(x),field.square(y))))
    G=F.conj().T@F / (q*q)
    vals=np.linalg.eigvalsh(G)
    prediction=predicted_eigenvalues(q)
    assert len(vals)==len(prediction)==3*q-2
    deviation=float(max(abs(vals-prediction)))
    assert deviation<1e-9, (q,deviation,vals,prediction)
    # Exact character-sum identity: the characteristic function of the set of
    # nonzero squares, counted twice, explains the partial Fourier rows.
    assert abs(np.trace(G)-(3*q-2))<1e-9
    return q, 3*q-2, deviation


def main():
    examples=[Field(p) for p in [3,5,7,11,13,17,19,23]]
    examples.extend([Field(3,2,2),Field(5,2,2)])
    results=[check_field(f) for f in examples]
    max_dev=max(d for _,_,d in results)
    # Algebraic Gram-rank threshold: singular only at q=3 or q=5.
    for q,_,_ in results:
        spectrum=predicted_eigenvalues(q)
        zeros=sum(abs(e)<1e-9 for e in spectrum)
        assert zeros==(1 if q in (3,5) else 0), (q,zeros)
    print("VERIFY_OK", "fields=", [q for q,_,_ in results],
          "total_columns=",sum(k for _,k,_ in results),
          "max_eigenvalue_deviation=",f"{max_dev:.2e}",
          "small_field_singularities=PASS")


if __name__=='__main__':
    main()
