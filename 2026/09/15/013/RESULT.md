# Zeta-function structure for the B2-irreducible Dolbeault-Dirac triple

## Context

The B2-irreducible quantum flag manifold B = O(SO_q(5))^{co(O_q(L))} with 0<q<1
carries a Dolbeault-Dirac spectral triple (B,H,D) constructed by Diaz Garcia,
O Buachalla, and Wagner. The anti-holomorphic forms decompose into four branches
(c0, c1, d2, d3) whose eigenvalues are explicit q-number products with Weyl-group
multiplicities, and left multiplication by B extends to a bounded representation.
Prior work stops at the spectrum, multiplicities, and 0+-summability; no
zeta-function continuation, pole lattice, pole order, or dimension-spectrum
computation existed for this triple.

## Definitions

Let L = log(q^{-1}) > 0 and L_q = (2 pi i / L) Z. Let ker D be the one-dimensional
space of constants, projected out of every zeta function. For b in B acting by
left multiplication, zeta_b(s) = Tr(b |D|^{-s}). Write zeta_1 for b = 1. A fixed
row/column sector zeta is S(s) = sum_n P(n) E(n)^{-s/2} with P a degree-3
polynomial, E(n) = K q^{-2n} B_1(q^n), B_1 a polynomial with B_1(0) > 0 positive
on the lattice points {q^n}.

## Result

(a) All-b holomorphy: for every b in B, zeta_b converges absolutely for
Re(s) > 0 and is holomorphic there; hence the future dimension spectrum has no
pole with Re(s) > 0.
(b) Exact b=1 factorisation: each eigenvalue branch factors as
E(n,l) = K q^{-2(n+l)} B(q^n,q^l) with K > 0 and B an explicit polynomial with
B(0,0) = 1. For c0, E^{c0} = q^{-2N}(1-q^2)^{-2}[(1-q^4 w)(1-w)
+ q u^2 (1-q^2 v^2)(1-v^2)] with u=q^n, v=q^l, w=u^2 v^2, N=n+l.
(c) Real Tauberian law: as s -> 0+, s^6 zeta_1(s) -> 640 / (log q^{-1})^6.
(d) Sector continuation: every fixed row/column sector zeta extends
meromorphically to all of C with poles contained in union_{j>=0}(-j + L_q) and
exact pole order 4 at every point of the principal lattice L_q.

## Proof / evidence

Lemma (q-number bounds): [m]_1 = q^{-(m-1)}(1-q^{2m})/(1-q^2), so
q^{-(m-1)} <= [m]_1 <= q^{-(m-1)}/(1-q^2) for m >= 1.
(a) Each branch satisfies E >= c q^{-2N} with uniform c = q > 0 while Weyl
multiplicities grow at most polynomially of degree 4, so zeta_1(Re s) converges
for Re(s) > 0; |Tr(P_mu b P_mu)| <= ||pi(b)|| dim P_mu gives
|zeta_b(s)| <= ||pi(b)|| zeta_1(Re s) with uniform convergence on Re(s) >= sigma.
(b) Substituting the q-number identity into each branch and factoring q^{-2N}
leaves a polynomial bracket valued 1 at (0,0); positivity off the kernel bounds
B between positive constants on lattice points. Verified symbolically and to
1e-9 numerically.
(c) B^{-s/2} = 1 + O(s) uniformly and K^{-s/2} = 1 + O(s), reducing to top
homogeneous Weyl part 8(2n^3 l + 3n^2 l^2 + n l^3)/3; Eulerian asymptotics
sum n^a e^{-s'n} ~ a!/s'^{a+1} yield 80 per signed family, 8 families = 640.
(d) 1D lemma: Taylor-expand B_1(u)^{-s/2} to order M; each term is
Eulerian-rational in q^{s+j} with poles iff s+j in L_q; the remainder converges
for Re(s) > -(M+1); M arbitrary gives C. At s_0 in L_q only j=0 is singular of
exact order d+1=4 with nonzero coefficient.

## Limitations

Bulk 2D meromorphic continuation of zeta_1, exact pole orders of the full double
sum, general-b continuation, and the complete two-sided dimension spectrum with
attainment remain open and are not claimed. The s^{-6} law is a real boundary
growth rate, not a certified bulk meromorphic pole order. Scripts in
output/artifacts/ reproduce factorisation, shell decay, and coefficient checks.

## Reproducibility

Admitted input: Diaz Garcia-O Buachalla-Wagner Theorem 16 and Corollary 15
(eigenvalues, Weyl multiplicities, bounded representation). Reproduce with
output/artifacts/zeta1_factorisation.py, branches_factor.py,
emergent_checks.py, test_domination.py at q=0.7.

## References

- F. Diaz Garcia, R. O Buachalla, E. Wagner, A Dolbeault-Dirac Spectral Triple
  for the B2-Irreducible Quantum Flag Manifold, Comm. Math. Phys. 2022,
  DOI 10.1007/s00220-022-04435-5; arXiv:2109.09885.
- B. Das, R. O Buachalla, P. Somberg, A Dolbeault-Dirac Spectral Triple for
  Quantum Projective Space, DOI 10.4171/dm/771; arXiv:1903.07599.
