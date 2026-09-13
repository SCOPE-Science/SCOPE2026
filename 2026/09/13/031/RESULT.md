# Tate duplication Lattes map q=5 over C5: exact Berkovich Fatou list and no wandering

## Context

Let K = C5 be the completion of an algebraic closure of Q5: complete, algebraically closed, value group Q of Q-rank 1, residue field the algebraic closure of F5 of characteristic 5. Let q = 5 and E = K*/q^Z be the Tate elliptic curve, with skeleton circle S_E of length l = -log|q| > 0. Let x: E -> P1 be the quotient by [-1] (degree 2, branched exactly over x(E[2]) = {infty, e1, e2, e3}) and L the degree-4 duplication Lattes map defined by L o x = x o [2]. E and x descend to Q5, so L is defined over Q5 with persistent multiplicative reduction but Q-rank-1 value group. This places L outside the known Q-rank-at-least-2 wandering-disk construction for Lattes maps with persistent bad reduction (Rivera-Letelier 2026, building on Benedetto). The admitted target asks to decide: (A) the Berkovich Fatou set of this single L is empty or consists solely of explicitly listed preperiodic indifferent components with no wandering, or (B) some explicit disk wanders.

## Definitions

Berkovich Fatou set F(L): maximal domain of normality (equicontinuity) in P1,an_K; Julia set J(L): its complement. Lattes skeleton segment Sigma = x(S_E): quotient of the Tate skeleton circle by the folding involution t -> -t, a segment of length l/2 with retraction r. Normalized coordinate s in [0,1/2]; endpoint s=0 is r(infty). Tent map T on Sigma: folded doubling, T(s) = 2s on [0,1/4], T(s) = 1-2s on [1/4,1/2], slope +-2, surjective, preserving normalized Lebesgue measure m. Open Berkovich disks off Sigma are the connected components of V = P1,an \ Sigma, equivalently {+-1}-quotients of residue disks of E^an off S_E.

## Result

Alternative (A) holds with the following exact Fatou list, and (B) is false.

(i) The Berkovich Julia set is exactly the Lattes skeleton segment: J(L) = Sigma = x(S_E).
(ii) The Berkovich Fatou set is exactly its complement F(L) = P1,an \ Sigma, a disjoint union of open Berkovich disks. Every such disk is preperiodic under L, and every periodic cycle is indifferent; there are no attracting cycles. In particular the disk D_infty containing infty is fixed and indifferent with multiplier 4 (|4|_5 = 1).
(iii) No Berkovich disk has infinite pairwise-distinct forward images. There is no wandering Berkovich disk for this L.

The postcritical set is the finite set {e1, e2, e3, infty}: the six simple critical points x(E[4] \ E[2]) map in two steps to the fixed indifferent point infty. The exceptional set is empty.

## Proof and evidence

Critical values and multiplier. Since [2] is etale (char residue 5 does not divide 2), L o x is branched over x(E[4]); removing the branching of x gives 6 simple tame critical points with local degree 2. Their orbits are c -> e_i -> infty -> infty. With local parameters t at 0 in E and z = 1/x at infty, L*z = 4z + ..., so infty is fixed of multiplier 4, indifferent. L^{-1}(infty) = {infty, e1, e2, e3} are four distinct unramified preimages; no point is totally ramified, so E(L) is empty.

Skeleton action. [2] lifts to z -> z^2 on G_m, acting on S_E as the doubling cover t -> 2t; [-1] acts as reflection, so L|_Sigma is the folded doubling tent map T above. Total invariance L^{-1}(Sigma) = Sigma holds via Tate uniformization (disks off S_E lift to disks off the G_m skeleton, and squaring sends disks to disks), so L permutes the components of V, each iterate L^n(D) lying in a single component.

Complement in Fatou. Each component D of V is an open Berkovich disk whose iterates omit the uncountable set Sigma; by non-archimedean Montel normality, {L^n|_D} is normal, so V is contained in F(L).

Equilibrium measure and Julia identification. The second-Bernoulli tree potential H_E(t) = (l/2) B_2(t/l) pushes forward under the folding quotient to normalized Lebesgue measure m on Sigma, which satisfies T_*m = m and L*m = 4m, hence is the unique balanced probability measure, i.e. the Lattes equilibrium measure mu_L supported exactly on Sigma. The torsion ledger L^{-n}(infty) = x(E[2^n]) gives |L^{-n}(infty)| = (4^n-4)/2 + 4 = 2^{2n-1}+2 distinct preimages (n >= 1) with total multiplicity 4^n, whose retractions are folded dyadic points equidistributing to m with star-discrepancy 2^{-n}. Since E(L) is empty, Baker-Rumely / Favre-Rivera-Letelier equidistribution identifies mu_L = m with support Sigma; Julia-as-support gives J(L) = Sigma and F(L) = V exactly.

No attracting, no wandering. Every attracting cycle attracts a critical point (Rivera-Letelier), but all six critical points land in two steps on non-attracting infty, so no attracting cycles exist; every periodic Fatou component is indifferent. For no wandering: each component D has type-II boundary xi = r(D) in Sigma at rational normalized coordinate (value group Q), hence finite T-orbit by the rational-preperiodicity lemma (folded doubling permutes finite dyadic-denominator sets). Following to a periodic boundary cycle and conjugating L^k to the Gauss point over a finite extension presents the first-return fiber map as a rational map R over a finite field F_{5^m}; every residue direction lies in some P1(F_{5^M}) and R preserves the finite set P1(F_{5^{lcm(m,M)}}), so each direction is preperiodic. Thus the component sequence D_n is eventually periodic: every Fatou disk is preperiodic, and no disk wanders. The Q-rank-one hypothesis is used exactly here: rational boundary plus finite-field fibers; the rank>=2 wandering mechanism has no room.

Computation. The artifact tent_ledger.py verifies rational preperiodicity for denominators <= 200, the ledger counts for n <= 6, and discrepancy 2^{-n} for 1 <= n <= 10; rerun reproduced. The no-wandering conclusion is analytic, not brute-force.

## Limitations

The argument invokes standard Berkovich theorems as black boxes without reproving them: Berkovich/Hsia-Montel normality, Baker-Rumely / Favre-Rivera-Letelier equidistribution and Julia-as-support, Rivera-Letelier classification of periodic Fatou components and the attracting-critical rule, and type-II reduction. Map-specific inputs (tent formula, tame simple ramification, multiplier 4, ledger counts, discrepancy decay) are proved or computed here. No claim is made for other Tate parameters, residue characteristics dividing the degree, or higher-rank value groups.

## Reproducibility

Run python3 output/artifacts/tent_ledger.py: expect rational preperiodic check with zero bad points, counts 4, 10, 34, 130, 514, 2050 for n = 1..6, and discrepancies halving from 0.5 at n=1 to ~0.001 at n=10. Skeleton and ledger identities can be rechecked from L o x = x o [2] and L^{-n}(infty) = x(E[2^n]).

## References

R. Benedetto, Dynamics in One Non-Archimedean Variable, GSM 198 (2019), Ch. 10-11. J. Rivera-Letelier, Irrational Fatou components in non-Archimedean dynamics, arXiv:2505.09383v2 (2026). E. Trucco, Wandering Fatou components and algebraic Julia sets, Bull. SMF (2014). Y. Okuyama, Uniform perfectness of Berkovich Julia sets (2021). R. Birkett, Skew products on the Berkovich line (2023). Tate uniformization expositions.
