# Scientific review

**Correctness — PASS.** The coefficient series follows from the Herglotz representation. Expanding its exact moments through order two gives the claimed quadratic form, independently confirmed by the coefficient recurrence in `checker.py`. Each Fourier-block determinant is algebraically \(1\), its trace is \(3-2t(1-t)\), and the all-degree gap follows by elementary eigenvalue calculus and Parseval. Conjugate frequency modes preserve the real-tangent constraint. The cubic remainder is for each fixed \(n\), not uniform in \(n\).

**Originality — PASS (priority caveat).** The 1977 Hummel–Scheinberg–Zalcman strict local maximum is explicitly acknowledged and **not** part of the new priority claim. The 2019 Agler–McCarthy full manuscript establishes general critical-point characterizations but not the all-degree Fourier-block determinant-one Hessian or sharp common constant. Wikström's October 2026 full text provides the global \(n=6\) coefficient theorem and mentions numerical Hessian checking in Section 7.3, not the stated analytic all-degree spectrum. Lei–Zhang's entropy result concerns a different functional. Targeted indexed comparisons show no equivalent reported formula. Original 1977 text was unavailable, so overlap risk remains.

**Value — PASS.** The exact all-degree condition numbers and sharp curvature constant supply quantitative conditioning information at the canonical candidate, applicable to local certified optimization and stability estimates. Unlike a routine restatement of the known strict-local theorem, the complete frequency-resolved quadratic form and optimal uniform constant are new mathematical invariants of the natural full-mass-and-angle perturbation family.

**Limits.** Local within exactly \(n\) atoms; no global result for higher coefficients, no degree-uniform perturbation radius, no independent priority review.

Self-review: passed. Independent audit: not yet performed.
