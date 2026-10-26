# Review of the quartic rectification finding

## Correctness — PASS

The claim is a finite-state analytical calculation, not an extrapolation. For the four-site two-particle sector, the six transition states split into four adjacent pairs and two opposite pairs; their rates are explicitly tabulated in `RESULT.md`. Stationary elimination gives the rational current, the one-parameter quadratic coefficient, and the complete even-in-bias response at site rates \((2,3,4,11)\). Positivity follows from the explicit even denominator bound \(E\ge44850>|O|\) throughout the claimed open bias interval. The separate three-site exact current proves minimality. The standalone verification program reconstructs the Markov generator and independently checks the symbolic equalities using exact arithmetic. Numerical exploration was used to select a tractable example, not as proof of the infinite assertion over all biases.

## Originality — PASS, with limitations

The closest contemporary work is Sakai–Akimoto, arXiv:2512.03316v1. Its accessible revised full text (Sections II and III.D; Appendix C and E) poses quadratic bias-reversal breaking as the expected response outside bond-ratio uniformity or reflection correspondence. The new general four-rate quadratic coefficient factors into opposite-site differences and a cubic cancellation surface; the four-site family contains two explicit non-reflective cancellation points, with a rigorously positive quartic response at one. The 2006 Juhász–Santen–Iglói treatment of random-site hopping studies scaling and phase separation, not this exact cancellation. Finite-state matrix-tree formulas give an algorithm to compute such currents but do not assert the specific exceptional zeros. Semantic overlap searches of published mathematical findings returned no source implying this statement. Search incompleteness and implicit generic-enumeration coverage remain residual priority risks; the revised motivating source was materially inspected but the original version was only date-verified.

## Value — PASS

The question is motivated by the contemporary conjecture about whether quadratic rectification is forced by the absence of inversion and local bond-uniformity. The exact smallest-ring counterexample distinguishes cancellation of a response coefficient from a true symmetry, gives a nontrivial open-interval sign result, and supplies a testable finite-size benchmark for perturbative transport approximations. The phase boundaries at \(t=2,3,11\) include nonsymmetry-protected cancellations at two values. This is a structural finite-size boundary, not a renaming exercise or a minute numerical improvement.

## Scope and residual risks

The model uses a site-trap escape-rate parameterization and finite-density exact Markov dynamics. The observation does not characterize large-ring disorder averages. The mathematical proof is self-reviewed; broader priority assessment and independent validation have not occurred. The contextual source is not treated as authority for the new result.

Self-review: passed. Independent audit: not yet performed.
