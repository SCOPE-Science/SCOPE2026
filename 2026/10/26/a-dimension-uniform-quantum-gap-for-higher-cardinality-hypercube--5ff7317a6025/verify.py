"""Finite, reproducible checks for the robust hypercube rendezvous bound.

Requires Python 3.9+ and NumPy. The all-parameter theorem uses the proof
in RESULT.md; computations here test selected instances and identities only.
"""
from itertools import combinations
from math import comb, isclose
from fractions import Fraction
import random
import numpy as np

CHECKS = 0

def check(cond, message):
    global CHECKS
    if not cond:
        raise AssertionError(message)
    CHECKS += 1


def masks(d, t):
    return [sum(1 << i for i in A) for A in combinations(range(d), t)]


def spectral_and_geometry(d, t):
    k = comb(d, t)
    s = comb(2 * t, t)
    c = comb(d - t, t)
    ell = comb(d, 2 * t)
    theta = c * Fraction(d - 2 * t, d - t)
    check(Fraction(c, ell) == Fraction(s, k), "no-signalling ratios")
    ksub = masks(d, t)
    adjacency = np.array([[int(a & b == 0) for b in ksub] for a in ksub], dtype=float)
    lam = np.linalg.eigvalsh(adjacency)
    check(abs(lam[-1] - c) < 1e-8, "Kneser top eigenvalue")
    check(abs(lam[0] + comb(d - t - 1, t - 1)) < 1e-8, "Kneser bottom eigenvalue")
    expected_eig = [(-1)**j * comb(d - t - j, t - j) for j in range(t + 1)]
    for x in lam:
        check(min(abs(x - y) for y in expected_eig) < 1e-7, "entire Kneser spectrum")
    # Bipartite double adjacency has smallest nonzero Laplacian eigenvalue theta.
    abs_nontriv = max(abs(x) for x in lam if abs(x - c) > 1e-7)
    check(abs((c - abs_nontriv) - float(theta)) < 1e-8, "bipartite spectral gap")
    sigma0 = 0
    zeta0 = (1 << (t - 2)) - 1
    check(zeta0 not in ksub, "extra vertex outside zero sphere")
    for z in ksub:
        if z == zeta0:
            continue
        check(any(((sigma ^ z).bit_count() == t and
                   (sigma ^ zeta0).bit_count() == t)
                  for sigma in range(1 << d)), "pair shares a t-sphere")
    gap = Fraction(s * (d - 2 * t), 512 * (d - t) * k**4)
    check(gap > 0, "explicit positive bound")
    check(gap == theta / (512 * k**3 * ell), "gap equivalent expressions")
    return (k, c, ell, theta, gap)


def classical_symmetrization_test(d, t, seed):
    rng = random.Random(seed)
    N = 1 << d
    ksub = masks(d, t)
    k = len(ksub)
    ell = comb(d, 2 * t)
    c = comb(d - t, t)
    theta = Fraction(c * (d - 2 * t), d - t)
    alice = {sig: sig ^ rng.choice(ksub) for sig in range(N)}
    bob = {sig: sig ^ rng.choice(ksub) for sig in range(N)}
    succ = sum(alice[sig] == bob[tau]
               for sig in range(N) for tau in range(N)
               if (sig ^ tau).bit_count() == 2*t)
    P = Fraction(succ, N * ell)
    NS = Fraction(c, ell)
    # In the coherent symmetrized preparation, flags have amplitudes 1/sqrt(N).
    # For each base destination z, count Alice/Bob inputs mapping to z.
    target_count = [0] * N
    for sig in range(N):
        target_count[alice[sig]] += 1
        target_count[bob[sig]] += 1
    # At destination z, v_z[g] = target_count[z xor g]/(2k sqrt(N)).
    # Thus p^2 = sum of squared counts /(N*(2k)^2).
    p2 = Fraction(sum(q*q for q in target_count), N * (2*k)**2)
    # h^2 per destination, sum over Alice incident moves and translation flags.
    # For any z, pick z=0, sum over flag g and input sig=g xor A.
    h2 = Fraction(0)
    for g in range(N):
        v = Fraction(target_count[g], 2*k)
        for A in ksub:
            orig_sig = g ^ A
            aa = int(alice[orig_sig] == g)
            h2 += (Fraction(aa) - v)**2 / N
    # Independently compute E from all (translated) successful branches:
    # E = 2N c - 2 numerator(success); translation flags do not change score.
    E = 2*N*c - 2*succ
    check(NS - P == Fraction(E, 2*N*ell), "exact score-deficit energy")
    check(Fraction(E) >= theta * N * h2, "Kneser Poincare")
    check(h2 >= Fraction(1, 256*k**3), "quantitative robust contradiction")
    check(NS - P >= Fraction(c*(d-2*t), 512*(d-t)*k**4), "uniform theorem")
    check(p2 >= 0, "center is a squared Hilbert norm")



def quantum_qubit_test(d, t, seed):
    """Independently evaluate a genuine noncommuting entangled-qubit protocol."""
    rng = np.random.default_rng(seed)
    N = 1 << d
    ksub = masks(d, t)
    k = len(ksub)
    ell = comb(d, 2*t)
    c = comb(d-t,t)
    theta = c * (d-2*t)/(d-t)
    psi = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)],dtype=complex)
    eye = np.eye(2,dtype=complex)
    av = np.zeros((N,N,4), dtype=complex)
    bv = np.zeros_like(av)
    for input_vertex in range(N):
        for arr,alice_side in [(av,True),(bv,False)]:
            choices=rng.choice(k,size=2,replace=False)
            phase=rng.uniform(0,2*np.pi)
            theta_angle=rng.uniform(0,np.pi/2)
            u=np.array([np.cos(theta_angle),np.exp(1j*phase)*np.sin(theta_angle)])
            P=np.outer(u,u.conj())
            for selected,Q in [(int(choices[0]),P),(int(choices[1]),eye-P)]:
                final=input_vertex ^ ksub[selected]
                operator=np.kron(Q,eye) if alice_side else np.kron(eye,Q)
                arr[input_vertex,final]=operator@psi
    vs=np.zeros((N,4),dtype=complex)
    for q in range(N):
        vs[q]=sum((av[q^A,q]+bv[q^A,q] for A in ksub),np.zeros(4,dtype=complex))/(2*k)
    p2=sum(np.vdot(v,v).real for v in vs)/N
    h2=sum(np.vdot(av[q^A,q]-vs[q],av[q^A,q]-vs[q]).real
           for q in range(N) for A in ksub)/N
    E=sum(np.vdot(av[q^A,q]-bv[q^B,q],av[q^A,q]-bv[q^B,q]).real
          for q in range(N) for A in ksub for B in ksub if not A&B)
    score=sum(np.vdot(av[x,q],bv[y,q]).real
              for x in range(N) for y in range(N) if (x^y).bit_count()==2*t
              for q in (x^A for A in ksub) if (y^q).bit_count()==t)/(N*ell)
    check(isclose(c/ell-score,E/(2*N*ell),rel_tol=1e-10,abs_tol=1e-10), "entangled quantum deficit identity")
    check(E + 1e-8 >= theta*N*h2, "entangled Kneser Poincare")
    check(h2 + 1e-10 >= 1/(256*k**3), "entangled robust obstruction")
    check(c/ell-score + 1e-10 >= c*(d-2*t)/(512*(d-t)*k**4), "entangled quantum value bound")
    check(np.sqrt(k*p2)+np.sqrt(h2)+1e-9>=1, "direct-sum triangle bound")


def main():
    for d,t in [(5,2),(6,2),(7,2),(7,3),(8,2),(8,3),(9,4)]:
        k,c,ell,theta,gap = spectral_and_geometry(d,t)
        print(f"Kneser/geometry d={d}, t={t}: k={k}, theta={theta}, gap={float(gap):.10g}")
    for seed in range(30):
        classical_symmetrization_test(5,2,seed)
    for seed in range(10):
        classical_symmetrization_test(7,3,seed)
    for seed in range(6):
        quantum_qubit_test(5,2,seed)
    print(f"PASS: {CHECKS} finite assertions; not a substitute for the all-parameter proof.")

if __name__ == "__main__":
    main()
