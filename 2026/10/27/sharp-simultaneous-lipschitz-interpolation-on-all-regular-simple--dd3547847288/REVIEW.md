# Scientific review

## Correctness — PASS

The complete operator-norm reduction uses the exact \(\ell_1/2\) Kantorovich--Rubinstein formula on unit equilateral vertex data. Symmetrization applies to every linear right inverse, including ones using signed coefficients. All possible point pairs reduce to three nontrivial ratios, with the endpoint parameter regimes separately excluded. The unique crossing switches at the exact condition \(\sqrt r=p+q\), which is never equality at integer \(r\), yielding the full piecewise formula. An explicit positive operator attains the bound. The fixed-face-size limit and its unique \(17\)-cardinality extremum follow from verified derivative signs and an integer-rational radical comparison. Full point-pair tests and unsymmetrized small linear programs support the analytic calculation.

## Originality — PASS, subject to residual bibliographic risk

The nearest exact prior calculation covers only edge midpoints, corresponding to \(k=2\). It does not imply the face-distance patterns or optimum at \(k\ge3\), and it has no global optimization over face cardinalities. Bruè--Di Marino--Stra's published general extension theorem and Albiac--Ansorena--Cúth--Doucha's free-space complementability criterion concern general machinery, not the new constants. Borodachov's simplex spline-recovery problem uses derivative data and controls approximation error rather than Lipschitz extension norm. Targeted published-literature and research-database searches did not identify a formula covering the higher-face result or the unique extremal cardinality \(17\). This is not an assertion of exhaustive literature coverage.

## Mathematical value — PASS

This gives a natural and complete two-parameter class of exact simultaneous interpolation constants, including the codimension-one exception, the positive optimal kernels, and strict improvement over naive face averaging. The unexpected finite face-cardinality extremum at \(17\), with a sharp global constant not attained in any finite simplex, supplies substantial structural information independent of one-off numeric computations. It is useful as a precisely calibrated stability benchmark for high-dimensional simplex face interpolation and finite Lipschitz-free complementability.

## Closest literature and limitations

Bruè, Di Marino and Stra, arXiv:1801.07533, Theorem 4.1; Albiac, Ansorena, Cúth and Doucha, arXiv:2005.06555, Lemma 2.7; Borodachov, arXiv:2212.11070, Sections 1--2. The exact edge-midpoint case \(k=2\) is prior and explicitly excluded from the new theorem. Extensions to mixed face sizes, nonregular simplices or Banach-valued data remain unproved. Less-indexed equivalent work remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
