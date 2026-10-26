# Scientific review

## Correctness — PASS

The statement is valid for complex Hilbert dimensions at least two, including infinite dimension, and for every \(|q|\le1\). The proof reconstructs every critical step: existence of an isotropic unit vector for a conjugate-homogeneous quadratic form, full interval of diagonal-overlap moduli, the exact phase-aligned two-term envelope, its piecewise optimization, a two-dimensional one-phase lower envelope, and connectedness plus rotation invariance of constrained orthonormal pairs. It treats both degenerate endpoints and supplies a direct-sum antiunitary witnessing strict nonattainment. Differentiation proves the two distinct hole-closure orders. Finite checks in `verification/check.py` confirm formulas for explicit antiunitary matrices, but are not used to infer the universal claim.

## Originality — PASS, with documented risk

Majumdar--Müller (arXiv:2610.16823v1, Section 6) proves the qualitative disk/annulus geometry and the special skew-conjugation hole, but the inspected section neither states the exact radii for all scaled antilinear isometries nor determines the norm-plateau, hole-closing, and boundary-attainment thresholds. Kołaczek--Müller (2024) studies the ordinary \(q=1\) numerical range, so its disk theorem does not imply the exact \(0\le|q|<1\) annuli. Chien--Nakazato (2005) studies complex-linear normal operators; its formulas are not antilinear statements. Relevant previously indexed mathematical findings concern complex-linear \(q\)-radii, not the claimed class. The inaccessible Jia--Liu (2025) full text is a residual priority risk, although its abstract specifies ordinary numerical ranges, not variable \(q\).

## Mathematical value — PASS

The problem is motivated directly by the new qualitative antilinear \(q\)-range classification. It identifies the exact nonconvexity boundary and gives a *complete* quantitative formula on the natural, extensive class of antiunitary/isometric conjugate-linear operators. Two independent geometric transitions, \(|q|=w(A)/\|A\|\) and \(|q|=\sqrt{1-(w(A)/\|A\|)^2}\), quantify how diagonal overlap governs a radius plateau and central hole. The infinite-dimensional endpoint classification additionally detects a genuine norm-attainment effect not visible in the qualitative disk theorem. No claim is made for arbitrary antilinear operators or for publication priority beyond inspected evidence.

Self-review: passed. Independent audit: not yet performed.
