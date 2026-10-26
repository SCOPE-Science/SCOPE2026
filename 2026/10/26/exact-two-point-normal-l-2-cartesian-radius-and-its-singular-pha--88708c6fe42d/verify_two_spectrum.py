"""Independent finite diagnostics for a two-spectrum Cartesian-radius identity.

Only finite quadrature checks are made; the accompanying analytic proof covers
all complex Hilbert spaces with a normal two-point spectrum.
"""
import math
import random


def prediction(lam: complex, mu: complex) -> float:
    r, s = sorted((abs(lam), abs(mu)), reverse=True)
    a = (r*r-s*s)/2
    u = abs((lam.conjugate()*mu).imag)
    if a == 0 and u == 0:
        correction = 0.
    elif a == 0:
        correction = u
    else:
        correction = u-a*math.atan(u/a)
    return r*r/2+correction/math.pi


def angular_mean(lam: complex, mu: complex, n: int=8192) -> float:
    total=0.
    for k in range(n):
        theta=2*math.pi*(k+.5)/n
        x=(lam.real*math.cos(theta)+lam.imag*math.sin(theta))**2
        y=(mu.real*math.cos(theta)+mu.imag*math.sin(theta))**2
        total+=max(x,y)
    return total/n


def main() -> None:
    rng=random.Random(20261004)
    examples=[(2+0j, 1*complex(math.cos(.3),math.sin(.3))),
              (1+0j, 1j), (1+0j,-1+0j),
              (2+0j,1+0j), (1+0j,0j), (0j,0j)]
    for k in range(210):
        r=rng.uniform(0.05,3.0)
        s=r if k%17==0 else rng.uniform(0.05,3.0)
        d=rng.uniform(-math.pi,math.pi)
        examples.append((r+0j,s*complex(math.cos(d),math.sin(d))))
    err=0.
    for la,mu in examples:
        observed=angular_mean(la,mu)
        expected=prediction(la,mu)
        err=max(err,abs(observed-expected))
        assert abs(observed-expected)<2e-6*(1+expected), (la,mu,observed,expected)
        radius=max(abs(la),abs(mu))
        assert expected+1e-10>=radius**2/2
        assert expected<=radius**2*(.5+1/math.pi)+1e-10
    # Structural boundary cases, without quadrature.
    for r,s in [(1.,1.),(2.,1.),(4.,0.5), (0.9,0.9)]:
        assert abs(prediction(complex(r,0),complex(-s,0))-max(r,s)**2/2)<1e-12
    print(f"PASS {len(examples)} finite angular tests; maximal discrepancy {err:.3e}")

if __name__=='__main__':
    main()
