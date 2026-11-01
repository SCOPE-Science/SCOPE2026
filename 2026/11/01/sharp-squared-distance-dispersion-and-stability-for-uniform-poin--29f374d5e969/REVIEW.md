# Scientific review

## Correctness (PASS)
The only claimed theorem concerns independent volume-uniform points in a nondegenerate Euclidean simplex of dimension \(d\ge2\). The Dirichlet moment formula is derived and contracted to a trace expression for \(\mathbb E\|X-Y\|^2\) and \(\mathbb E\|X-Y\|^4\). A nonnegative exact identity proves the sharp lower endpoint and regular-simplex rigidity. The upper endpoint uses a proved zero-sum scalar quartic lemma and a coordinatewise Cauchy--Schwarz argument; full covariance rank makes the inequality strict. An explicit collapsing family attains the upper endpoint in the limit; a continuous axial contraction of a regular simplex shows no gap in the range. The packaged verifier passes 90,001 exact rational diagnostics. Remaining check risk: no external proof audit has been performed, and finite diagnostics are not substitutes for the analytic argument.

## Originality (PASS, residual historical-priority uncertainty)
The closest pair-distance literature does not imply the claimed optimization. Wang (arXiv:2610.01916, Sections 1--4 and main theorems) studies Brunn--Minkowski properties of radial distance distributions, not simplex fourth-moment extrema. Bäsel (arXiv:2101.03815, Section 9) gives fourth moments for regular polygons only; in dimension two this covers the regular-triangle numerical case but not all triangular shapes. Pure--Durrani--Tong--Pan (arXiv:1903.07757, Sections II--IV) describe an algorithm for pairwise distances in arbitrary *planar* polygons, not all-dimensional shape extremizers or the remainder. Published zero-sum \(\ell_4\) inequalities overlap the scalar ingredient, which is not claimed original. Indexed mathematical results and accessible prior claims were checked for equivalence and stronger implications. Residual risk: obscure earlier normalized-moment extremal inequalities may be difficult to retrieve; indexing and partitioning do not certify uniqueness.

## Mathematical value (PASS)
The dimensionless quantity \(Q-1\) is the coefficient of variation squared of the *squared* interpoint distance, a natural model of shape-induced geometric dispersion. The result classifies the exact possible range for every dimension, proves rigidity at the regular shape, identifies the nonattained worst case, and supplies a quantitative stability certificate rather than only a numerical constant. It is not an arbitrary slice of a table; its hypotheses range over all Euclidean simplex shapes.

## Limits and validation
The result is for positive-volume simplices and no other sampling model. Its upper endpoint is approached only in a degenerate limiting sense. There is no publication-priority guarantee and no independent audit.

Self-review: passed. Independent audit: not yet performed.
