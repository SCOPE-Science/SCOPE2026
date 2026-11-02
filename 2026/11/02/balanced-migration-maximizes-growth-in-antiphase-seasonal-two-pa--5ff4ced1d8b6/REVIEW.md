# Self-review

## Correctness — PASS

The theorem is a statement about all constant nonnegative migration pairs with fixed sum and every positive contrast and period, not an inference from finite sampling. Reconstructing the two seasonal matrices yields traceless factors whose squares are scalar. The half-trace of the normalized period map has an exact hyperbolic closed form. Its rational Laplace transform, after the identity \(d^2=h^2-ab\), becomes a positive Volterra resolvent. All coefficients of the resulting convergent causal-convolution series are positive at positive time, establishing strict ordering for every \(ab\) in its full closed domain. The one-way boundary gives precisely the isolated-patch exponent; continuity gives a unique growth/decay product threshold whenever the balanced case grows. Equality, degenerate seasonal eigenvalues, one-way endpoints, and the neutral boundary are explicitly treated. Independent Taylor/scaling-squaring matrix exponentials in `VERIFY.py` corroborate the formula on 2,400 systems; numerical tests are supporting checks, not the theorem's proof.

**Limits and risk:** The strict inequality requires \(h,g,T>0\), fixed \(a+b\), equal half-seasons, and antiphase equal-mean local growth. No nonlinear persistence, stochastic dynamics, unequal local mean, or arbitrary migration matrix is claimed. An algebraic error in the transform would be decisive, so the rational identity was separately checked by symbolic reduction and by direct matrix-exponential comparisons.

## Originality — PASS

The nearest source is Benaïm, Lobry, Sari and Strickler, *When can a population spreading across sink habitats persist?*, arXiv:2311.04706, §§4.2--4.3 and supplementary §S1: it develops the general Floquet model and treats particular asymmetric-rate illustrations, but does not state fixed-total-rate strict monotonicity in the product of the two directed rates or the associated unique viability boundary. Their earlier arXiv:2111.12633, §3.2, explicitly includes non-symmetric dispersal (equations 37--38), but compares asymptotics for fixed directional bias rather than giving an all-bias, all-period optimization theorem. Katriel, arXiv:2104.01589, §2.1, requires symmetric dispersal and therefore does not compare the directions. Benaïm et al., arXiv:2407.07553, study broader period and migration effects without stating the fixed-budget product ordering. Wu et al. (2020) study a nonlinear, time-independent source–sink model in which asymmetric migration may be favorable; that is a different hypothesis class, not a counterexample or implication.

Equivalent-formulation, broader-coverage, exact-table and implication comparisons were performed, including a separate indexed-results search using the migration asymmetry, Floquet, and product-of-exponentials formulations. No available result implies the exact strict ordering and its threshold classification.

**Residual risk:** A specialized spectral or comparison-principle treatment of precisely this two-season two-patch family could have appeared outside the consulted literature or under different notation. The 2019 nonlinear source–sink article was inspected at abstract level, not its complete publisher text. Absolute priority is not independently certified.

## Mathematical value — PASS

Directional bias is a natural control variable for migration management, especially when a total relocation-rate budget is fixed. Merely proving that some dispersal induces growth leaves the directional allocation question unresolved. The theorem proves a sharp universal optimizer and a necessary-and-sufficient, continuous viability corridor for populations whose isolated local means are negative, including equality and the one-way boundary. The positive Volterra representation also exposes a structural reason for monotonicity that does not arise from checking individual parameter examples. This is a complete classification of a physically interpretable infinite parameter family, not a routine special-case recomputation or arbitrary numerical slice.

**Limits and risk:** Applied interpretation is conditional on linear growth, seasonal antiphase, equal seasonal lengths and constant transport rates. In a nonlinear system, a positive invasion exponent alone need not determine eventual abundance without additional hypotheses.

Self-review: passed. Independent audit: not yet performed.
