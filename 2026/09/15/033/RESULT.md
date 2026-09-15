# Sharp truncation barrier in Dodson's threshold-mass rigidity program (d >= 16)

## Context
The focusing mass-critical nonlinear Schrodinger equation on R^d is i u_t + Delta u + |u|^{4/d} u = 0 with L^2 initial data. Let Q be the unique positive radial ground state, Delta Q - Q + Q^{1+4/d} = 0. At threshold mass ||u_0||_2 = ||Q||_2, blow-up means infinite L^{2(d+2)/d}_{t,x} Strichartz norm forward in time. B. Dodson (arXiv:2106.02723v2, doi:10.1007/s40818-022-00142-5) proved that for 2 <= d <= 15 the only threshold-mass blow-up solutions are the soliton family (1.21) and its pseudoconformal transform (1.22), up to symmetries. Finite-time blow-up in all d is Merle; the radial case is Killip-Li-Visan-Zhang. Dodson Remark 8 states the restriction d <= 15 comes only from Section 10 Theorem 25 and calls it purely technical.

## Definitions
Write the modulation decomposition u = tilde-Q + tilde-epsilon with orthogonality conditions (3.7), scale lambda(s), and remainder epsilon. Let k_n -> infinity index intervals with |I(k_n)| 2^{-2k_n} >= k_n^{-2}. Truncate frequencies at P <= k_n(1-1/(10d)-delta) with deficit delta >= 0 (delta = 0 is Dodson). Let alpha_d = 2+8/d-1/(5d) for d >= 9 and Strichartz loss exponent gamma = 2/(5d). The non-smooth nonlinearity F(z) = |z|^{4/d} z produces remainders ||epsilon||^{1+4/d}_inf (term A) and ||epsilon||^{1+8/d}_inf (term B) in the energy increment (10.41). The bootstrap closes iff each Young-absorbed residual beats 2^{-2k_n}.

## Result (sharp truncation-barrier lemma)
Within Dodson Section 10 framework (truncated energy + fractional chain rule sigma < 1+4/d + Young absorption): term B closes iff delta <= (77-5d)/39 (up to a small O(1/d) normalization correction that does not move the threshold); hence no delta >= 0 works for any d >= 16. Literal Dodson residual exponents (gain times 2d/(d-8)) are 2.10095 at d = 15 (passes) versus 1.83906 at d = 16, 1.63529 at d = 17, 1.2275 at d = 20 (all fail). Term A stays feasible (delta <= about 17/(5d-1) > 0). So term B is the sole obstruction: the proof closes for d <= 15 and cannot close for d >= 16 by truncation or Young-exponent tuning.

## Proof / evidence
Starting from (10.41), the term-B coefficient has gain (8/d-1/5d)(1-1/10d-delta) and loss 2/5d. Young absorption with conjugate pair splitting ||epsilon||^{1+8/d} into ||epsilon||^2 plus residual gives residual exponent (gain-loss)*2d/(d-8); requiring >= 2 yields the delta bound. At delta = 0 this reproduces Dodson (10.43): (8/d-3/5d-7/10d^2)*2d/(d-8) >= 2+3/70 for 8 <= d <= 15. The algebra was swept for d = 8..30 by output/artifacts/check_barrier.py producing output/artifacts/barrier_check.json. Independent audit re-evaluation confirms the numbers; the exact bound carries an additional -7/(78d) term from expanding (1-1/5d)(1-1/10d) versus the stated beta, which is negative-side and preserves infeasibility for all d >= 16.

## Limitations
Bounds only the stated Section 10 architecture with sigma < 1+4/d and Young absorption. Does not decide rigidity for d >= 16, does not rule out proofs via sharper fractional calculus or low-regularity Morawetz/virial replacements, and provides no counterexample. The optimal-Holder origin of exponent 1+8/d is cited from Visan Prop. A.1, not re-proved.

## Reproducibility
Run python3 output/artifacts/check_barrier.py; it prints and writes output/artifacts/barrier_check.json with the residual table and feasibility flags. All equation references are to arXiv:2106.02723v2.

## References
B. Dodson, A Determination of the Blowup Solutions to the Focusing NLS with Mass Equal to the Mass of the Soliton, arXiv:2106.02723v2 (2022), Ann. PDE 2023, doi:10.1007/s40818-022-00142-5, esp. Section 10, Theorem 25, Remark 8, equations (10.41)-(10.44). Merle finite-time classification; Killip-Li-Visan-Zhang radial case; Visan fractional chain rule appendix.
