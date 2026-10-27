# Scientific review

## Correctness: PASS

The killed generator is the exclusion generator minus its diagonal configuration-dependent collision hazard. Strictly positive rates make the labeled exclusion chain irreducible, and finite-state Perron–Frobenius theory reduces equality of its Doob transform and exclusion to a constant positive eigenfunction, equivalently a constant hazard. Comparing occupied sets differing by one site shows that every symmetrized edge weight must coincide when two or more vacancies are present; when exactly one vacancy remains, constancy is equivalent to equal weighted degrees. The degree-map rank gives the exact exceptional dimension. The canonical marked killing construction proves independent exponential collision timing and the conditional pair-mark law. A standalone script completed 45 exact rank and finite generator/semigroup checks. Numerical examples support but do not substitute for the proof.

## Originality: PASS (qualified)

Shiatis, arXiv:2610.00741v1, supplies the general change-of-measure and killed-generator/Doob-transform mechanism. These are explicitly credited and not claimed here. The exact inverse classification by occupancy, exceptional weighted-degree cone, and the separation between collision-time and collision-pair independence were not stated in the inspected primary source. Johnston--Shiatis, arXiv:2501.15483v4, addresses nearest-neighbor ASEP traffic on a ring rather than the present complete directed rate family. Targeted searches of the relevant mathematical index and published literature yielded no exact covering statement. An equivalent inverse observation implicit in classical finite-state Doob transforms or weighted inclusion matrices is the principal residual risk, so originality has not been independently certified.

## Mathematical value: PASS

The equality question is natural: exclusion is directly simulable, while conditioning independent walkers to avoid all future collisions ordinarily changes their dynamics. The complete classification determines exactly which nonreversible generators make the two laws identical. The abrupt enlargement from a one-dimensional symmetrized-rate family at \(k\le n-2\) to a \(\binom n2-n+1\)-dimensional family at \(k=n-1\), plus an explicit positive four-site anisotropic witness, distinguishes survival-time independence from colliding-pair independence. This is a complete structural boundary, not just a parameter substitution or a numerical example.

## Closest literature and limitations

Sources: R. Shiatis, *Exclusion vs Noncolliding Dynamics in Markov Processes*, arXiv:2610.00741v1, Theorem 1.4 and Section 2; S. G. G. Johnston and R. Shiatis, *The Integrable Snake Model*, arXiv:2501.15483v4, Theorem 2.9 and Section 7. The finite positive-rate assumption is essential for the simple irreducibility argument. Sparse site graphs and arbitrary infinite spaces are not classified. The script is a finite checker, not an exhaustive proof over all sizes. The principal source is a general antecedent, so implicit corollary coverage deserves independent attention.

Self-review: passed. Independent audit: not yet performed.
