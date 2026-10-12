# Self-review

## Correctness
**PASS.** The logarithmic objective is strictly convex, so KKT conditions are sufficient and the optimizer is unique. The boundary derivative gives the clamped criterion \(G_j/a_j\le\tau\); free coordinates satisfy \(r_j^2=(G_j/a_j)/\tau\). Sorting these ratios produces one initial clamped block. Substitution cancels the free-block term from the self-consistency equation and yields \(\tau=B_k/A_k\), from which the exact minimum follows. The threshold-index recurrence proves existence and uniqueness. Upward rounding gives \(\lceil r_j\rceil\le2r_j\) and cannot increase the reciprocal factor, proving the factor-two integerization bound.

The packaged verifier checks the threshold conditions, KKT signs, closed-form product identity, and rounding inequality on deterministic positive families. Those checks are corroborative; the analytic argument proves the theorem for all positive coefficients.

## Originality
**PASS.** The closest source is G. H. Low, arXiv:2610.01125v1. Its Eq. (7.51) is exactly the leading gate-cost objective considered here, but the paper states only that its minimum is within a universal constant of Eq. (7.52) and gives the constructive Eq. (7.53). It then treats the larger precision-aware Eq. (7.54) as a geometric program. The full text does not state the threshold index, exact value, or rounded factor-two schedule proved here.

Focused published-result searches covered the exact source identifier, gate-cost allocation, water-filling/threshold aliases, ceiling rounding, downfolded-Hamiltonian resource language, and geometric-program formulations. The closest returned delay and rounding records concern randomized Gauss--Seidel and stratified sampling, not quantum-oracle scheduling. Current and immediately prior own ledgers were also checked for the source identifier and equivalent allocation language; no overlapping claim was found.

The strongest plausible contemporary comparison is Jing--Wang--Yu--Zhang, arXiv:2610.03393v1, which proves degree-optimal query counts in a different multivariate-polynomial access model. It does not contain the additive known-operation term or the lower-bounded delay variables of Eq. (7.51). Ito--Mori--Sakamoto--Fujii, Quantum 10, 2102 (2026), concerns polynomial realizability and likewise does not cover this resource allocation.

Residual risk remains that a generic optimization source contains an equivalent closed form under different terminology or that an unindexed contemporaneous paper independently states it. That risk does not alter the direct same-object comparison with the anchor.

## Value
**PASS.** The new MQSP source explicitly leaves this leading resource tradeoff at a universal-constant construction. The exact solution provides a qualitative design rule absent from that treatment: cheap/high-weight components should run every horizon step, and only components above one endogenous cost-to-weight threshold should be delayed. It also replaces numerical convex optimization for the leading objective by one sort plus linear arithmetic and gives a direct factor-two guarantee after ceiling. The result is a structural resource-allocation lemma for the source's downfolding circuit accounting, not a routine evaluation of a fixed numerical instance.

The claim is deliberately limited to Eq. (7.51). It does not solve the source's fuller precision and conditioning program, exact floor-valued query counts, address-width feedback, or total circuit-cost optimality.

Self-review: passed. Independent audit: not yet performed.
