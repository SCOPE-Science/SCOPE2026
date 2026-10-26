# Scientific review: third-order design incidence projections

## Correctness

**PASS.** The statement fixes a simple strength-three block design, its unit-edge incidence graph, and canonical real orthogonal projections. The incidence-matrix identity and zero-sum Schur complement yield the exact point potentials for an arbitrary incidence edge. Explicit signs on the distinguished block and both classes of other blocks reduce the absolute column norm to pair and triple incidence counts. All boundary cases, positivity inequalities, projection complementarity, and the \(\ell_1\)/\(\ell_\infty\) dual equality are checked. A standalone checker verifies 1,096 exact current columns, including 116 by independent grounded Laplacian inversion. The general theorem is proved analytically; finite checking alone would not establish it.

## Originality

**PASS, with bibliographic risk.** Direct comparison was made against the inspected relevant sections of Dilworth–Kutzarova–Ostrovskii (arXiv:2305.12582 and 1807.03814), Schild–Rao–Srivastava (arXiv:1708.01632), and Gurel-Gurevich–Nachmias–Sachdeva (arXiv:2605.24130). These provide cycle-space frameworks, Hamming/torus or recursive-graph projection analyses, and general electrical-current localization bounds; none of the examined statements yields the exact three-design incidence formulas. Targeted published-literature searches for three-design incidence transfer-current formulas and equivalent projection terminology did not reveal a covering result. Existing calculations for Johnson *vertex* spectral projectors concern a different edge space and operator. The residual risk is an older or poorly indexed incidence-network formula equivalent after a reduction; a negative search result is not proof of absolute novelty.

## Mathematical value

**PASS.** The formulas classify intrinsic endpoint operator invariants for all finite three-design incidence graphs without an edge-transitive hypothesis. They isolate an exact inverse-pair-incidence correction and quantify how designs with equal point/block sizes but different pair incidences give different norms. The essential mechanism is a structural third-order cancellation in absolute current flow, not a numerical table lookup. Steiner quadruple systems supply a natural infinite family with explicit limits.

## Scope and uncertainty

These are canonical Euclidean-orthogonal cut and cycle projections, not minimum-norm projections among all complements. The theorem does not claim uniformity for arbitrary two-designs or weighted variants. Unsearched prior literature remains a possible bibliographic overlap risk. There is no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
