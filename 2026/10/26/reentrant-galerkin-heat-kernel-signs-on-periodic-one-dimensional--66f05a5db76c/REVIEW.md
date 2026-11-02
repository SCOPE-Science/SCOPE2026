# Independent mathematical audit

## correctness

PASS

The frozen package defines M=(ell/6)(4I+A_n), K=(1/ell)(2I−A_n), Q=6I−36(4I+A_n)^(-1), and P=exp(sQ), s=t/ell². The periodized inverse of 4I+A gives Q_(0,3)>0 for all n>=6, hence p_(0,3)(s)>0 at sufficiently small s; simple zero eigenvalue gives eventual positivity. At s=1/3, spectral interval [-4,0] for Q/3 bounds degree-21 exponential Taylor entry error by 4^22/22!. The source exact-rational finite certificate covers ALL integer 6<=n<=50, with a strict negative margin; the analytic Laurent symbol F(z) on circles |z|=2 and 1/2 has coefficient bound 3^10 2^(-|j|), which bounds all n>50 alias corrections to the lattice coefficient and proves p_(n,3)(1/3)<−0.0069 for every n>=6. For n=6 the exact Fourier polynomial 6p_(6,3)=(1−x²)H(x) and Descartes root-count transform give exactly two positive-time zero crossings and unique all-entry nonnegativity horizon s=−(5/6)log alpha, alpha in (1/2,3/5). The n=3,4,5 Fourier formulas rule out a positive–negative–positive entry. Independent eigen-decomposition for n=6,7,8,13 gave p3(1/3)≈−0.014714194, −0.007317761, −0.007063876, −0.007356104, respectively. These floating checks only corroborate the proved exact-rational plus analytic infinite-family bound.

## originality

PASS

Jin–Lazarov–Thomée–Zhou arXiv:1510.02825, Theorems 3.1–3.2, prove small-time positivity failure and eventual positivity under assumptions, not one entry with reentrant +/−/+ behavior at the universal t=ell²/3 or the six-node exact horizon. The published SCOPE result on backward-Euler-filtered Crank–Nicolson instead concerns a composition of rational time-stepping filters (different operator) on a lumped-mass lattice; not a stronger result for the consistent-mass exponential semigroup. Originality of exact reentrant coefficient and n=6 minimality is plausible but qualified: a directly relevant 2015 Chatzipantelidis–Horváth–Thomée paper could not be read in full (Oxford VPN disconnected).

## value

PASS

A physically meaningful sign reversal in the same nodal heat-propagation coefficient despite symmetry, row-sum conservation and eventual positivity demonstrates a sharp consistent-mass semidiscretization phenomenon. The universal negative witness, minimum six-node size, and complete six-node nonnegativity horizon are exact natural invariants, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
