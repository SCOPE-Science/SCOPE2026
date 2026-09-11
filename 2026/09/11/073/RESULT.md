# Certified badly approximable gap 1/500 for the cubic vector (2^{1/3}, 2^{2/3})

## Context

Simultaneous Diophantine approximation in dimension two asks for uniform lower
bounds of the form max_i ||q alpha_i|| >= c q^{-1/2} valid for all denominators
q >= 1. Qualitative theory (Schmidt subspace theorem, Dani correspondence,
hyperplane absolute winning results) implies that every algebraic vector such
as alpha0 = (2^{1/3}, 2^{2/3}) is badly approximable with some ineffective
c > 0, but computes no explicit number for any named cubic pair. Number
theorists and dynamicists seek auditable effective witnesses with excursion
logs because the singular-versus-badly-approximable boundary and effective
Schmidt-winning constants remain active frontiers. Prior explicit work (Briggs
2003) treats only integral bases of the totally real field Q(2cos(2pi/7)) with
dual constants near 0.2857, a disjoint field and disjoint vectors.

## Definitions

Let theta = 2^{1/3} (real cube root) and alpha0 = (theta, theta^2). For integer
q >= 1 and p in Z^2 write delta_i = q theta^i - p_i and
Delta = max(|delta_1|, |delta_2|). The simultaneous badly approximable claim
with constant c is Delta >= c q^{-1/2} for all q, p. For a nonzero integer
triple a = (a0,a1,a2) write L(a) = a0 + a1 theta + a2 theta^2 and
H(a) = max|a_i|. Dani objects: u = [[1,0,theta],[0,1,theta^2],[0,0,1]] and
g_t = diag(e^{t/2}, e^{t/2}, e^{-t}) acting on unimodular lattices g_t u Z^3;
the dual flow g_t^* = diag(e^{-t/2}, e^{-t/2}, e^t) acts on u^{-T} Z^3 with
u^{-T} = [[1,0,0],[0,1,0],[-theta,-theta^2,1]]. First sup-norm minima are taken
over nonzero lattice vectors. Put K = 1 + theta + theta^2 and
S = theta + theta^2.

## Result

For alpha0 = (2^{1/3}, 2^{2/3}), for every integer q >= 1 and every
p = (p1, p2) in Z^2,

  max(|q theta - p1|, |q theta^2 - p2|) >= (1/500) q^{-1/2}.

Equivalently, the Dani lattice orbit in Kleinbock-Margulis normalization has
sup-norm first minimum >= 1/63 on the simultaneous side for all t >= 0, and
the dual orbit has sup-norm first minimum >= 1/10 for all t >= 0. The constant
1/500 is not claimed optimal; numerical evidence suggests the true optimal
simultaneous constant is near 0.29.

## Proof / evidence

Lemma 1 (dual Liouville bound). For every nonzero integer triple a,
|L(a)| >= 1/(K^2 H(a)^2) with K <= 77/20. Proof: x^3-2 is Eisenstein-irreducible
so {1,theta,theta^2} is a Q-basis and L(a) != 0. Multiplication by L(a) has
matrix m_a = [[a0,2a2,2a1],[a1,a0,2a2],[a2,a1,a0]] with determinant
a0^3+2a1^3+4a2^3-6a0a1a2, a nonzero integer of absolute value >= 1. The two
conjugate embeddings send theta to theta w, theta w^2 with |w| = 1, so
|det m_a| = |L(a)||L_2(a)||L_3(a)| with |L_j(a)| <= H(a)K, giving the bound.
Enclosure 1.259 < theta < 1.26 (from 1259^3 < 2*10^9 < 1260^3) yields
K < 1+1.26+1.26^2 = 3.8476 <= 77/20 and S <= 2.85.

Lemma 2 (explicit Siegel lemma). If (2A+1)^3 > 6AP+1 then for any integers
q,p1,p2 with max <= P there is a nonzero integer triple a with H(a) <= 2A
annihilating (q,p1,p2). Proof by pigeonhole on (2A+1)^3 values in
[-3AP,3AP]. The tail majorant Abar(q) = ceil(1.12 sqrt(q))+1 satisfies the
Siegel condition for all q >= 2 with P(q) = floor(8q/5)+2, because the
difference F(s) = (2.24s+3)^3-6(1.12s+2)(1.6s^2+2)-1 has all positive
coefficients, hence is positive for all s >= 0.

Lemma 3 plus Cassels product transference. For q >= 3 with Delta <= 1,
|p1| <= 1.26q+1 and |p2| <= 1.5876q+1 are both <= P(q), so Lemma 2 gives a
nonzero annihilator with H <= 2A(q) and (a1,a2) != (0,0) (else a0 q = 0
contradicts q >= 3). Then L(a) = (a1 delta_1+a2 delta_2)/q, so
|L(a)| <= 2H Delta/q. With Lemma 1, Delta >= q/(2K^2H^3). Squaring, the
1/500 bound follows from 4K^4H^6 <= 250000 q^3, machine-verified in exact
integers for all 3 <= q < 40000 (39997 cases, replayable in ~1 s). For
q >= 40000, A(q) <= 1.12 sqrt(q)+2 gives 2A(q)/sqrt(q) <= 2.26 and the integer
check 2*5929*226^3 <= 2*10^11 closes the tail. Remaining cases: Delta > 1 is
trivial since 1 >= 1/(500 sqrt(q)); q = 1 uses |theta-1| > 0.259 >= 1/500;
q = 2 uses 2 theta in (2.518,2.52) so |2theta-3| > 0.48 >= 1/(500 sqrt(2)).

Dani ledger. Simultaneous side: for q = 0 the norm is >= e^{t/2} >= 1; for
r = |q| >= 1 with s = e^{-t}r, the norm is >= max(s, c/s^{1/2}) with
c = 1/500, minimized at s = c^{2/3} with value c^{2/3} > 1/63 since
63^3 = 250047 > 250000 = 500^2. Dual side: for (a1,a2) = (0,0) the norm is
>= e^t >= 1; else with h = max(|a1|,|a2|), y = e^t, N the norm, H(a) <= N phi
with phi(y) = y^{-1}+S y^{1/2}, Lemma 1 gives N^3 >= y/(K^2 phi^2) >= 1/K^4
using K = 1+S >= S+y^{-3/2}, hence N >= K^{-4/3} >= 1/10 since K^4 <= 1000
(77^4 = 35153041 <= 160000000). All closed-form inequalities are audited in
exact integer arithmetic (T1-T9); an independent float scan to 10^6 shows min
sqrt(q) max(||q theta||,||q theta^2||) = 0.2959 at q = 46, margin ~148x.

## Limitations

The constant 1/500 is not optimal; computed evidence places the true optimal
simultaneous constant near 0.29, roughly 100x larger, and determining it is out
of scope. The finite-range audit of 39997 denominators is machine-checked
exact integer arithmetic rather than a closed-form estimate. No completed
census or general criterion is claimed.

## Reproducibility

Stdlib Python only: python3 artifacts/verify_integers.py prints
ALL_INTEGER_CHECKS_OK; python3 artifacts/verify_siegel_range.py prints
SIEGEL_RANGE_OK (checked=39997, ~1 s); python3 artifacts/verify_scan.py [Q]
prints worst ratio and SCAN_OK with zero violations. Hand expansions (norm
determinant, F(s) coefficients) are checkable by hand.

## References

Dani correspondence on badly approximable numbers and bounded orbits;
Kleinbock-Margulis homogeneous dynamics normalization; Davenport-Cassels
transference and geometry of numbers; Schmidt subspace theorem (qualitative
membership only); Beresnevich-Nesharim-Yang and An on HAW/winning Bad sets
(qualitative); Briggs arXiv:math/0211143 / J. Number Theory 103 (2003) 71-76
explicit pairs in Q(2cos(2pi/7)) (disjoint field); Basalov arXiv:1804.05385 on
best-approximation constants Cn (sup over all vectors).
