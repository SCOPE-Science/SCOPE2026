# Same-model review

## Correctness

PASS. Cauchy's formula and the Minkowski surface-area realization yield the exact adversarial convex-body expression
\[
E(u,w)=\max_{v\in S^2}\left|2\sum_iw_i|\langle u_i,v\rangle|-1\right|.
\]
A normal perpendicular to two sampling axes forces the potential below the third weight. Calibration makes at least one weight at most \(1/3\), giving the sharp lower error. For the equal-weight orthogonal frame, the Euclidean \(\ell_1\) range makes the error exactly \(1/3\). Equality forces every weight to be \(1/3\) and each direction perpendicular to both other directions. The same perpendicular tests give the near-optimal weight interval and the explicit angular bound. Two analytic perturbation families attain the weight bounds and force the square-root angular exponent. The proof holds for every full-dimensional convex body, not merely for the tested finite examples.

## Originality

PASS. Kiderlen--Meschenmoser (2009) give the *known* \(1/3\) worst relative error for the orthogonal-coordinate rule and a general fixed-rule zonotope error interval. Fu--Wang--Yan (2023) optimize a different one-sided, unweighted maximum. The 2026 primary source gives the sharp convex-body defect identity and nonexactness, not the finite-three-direction global design optimum. No inspected primary source states or implies the unique **two-sided calibrated global minimizer** together with quantitative near-optimal weight and angular rigidity, and targeted equivalent-formulation searches found no covering statement.

Residual risk: the newly proved optimization argument is concise given the 2009 zonotope formula; an unindexed discussion might have anticipated the classification. The coefficient in the angular estimate is not claimed optimal.

## Value

PASS. Three unoriented projection axes are a natural smallest complete 3D measurement budget, and finite exact Cauchy cubature is impossible. The global design optimum, its uniqueness, and robust near-optimal-frame bounds quantify precisely what is gained or lost by choosing oblique directions or unequal weights. The two different sharp perturbation orders have direct geometric meaning and are not a mere recomputation of the already-known coordinate-grid error.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

Closest sources: An, arXiv:2609.05869v1; Kiderlen--Meschenmoser, DOI:10.5566/ias.v28.p165-177; Fu--Wang--Yan, DOI:10.1002/rsa.21087. Calibration and the three-direction restriction are essential. No sharp angular stability constant, unrestricted scaling, or larger sampling-budget classification is claimed.
