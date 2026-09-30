# Independent audit — 2026-09-30

**Record:** `2026/09/20/three-score-ordering-polytope-pairwise-independence--4209dad13b91`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `345a4e63ec9cb661f0f6b131f1f1e5868460b6d1`  
**Disposition:** **PASSED**

## Correctness — PASS

The necessity and attainability arguments were checked independently. Conditional on X_i=x, pairwise independence fixes each of P(X_j<x|X_i=x) and P(X_k<x|X_i=x) at F(x); Frechet bounds then integrate over F(X_i)~U(0,1) to 1/4<=q_i<=1/2. The three pairwise-comparison equations plus total mass force the reversal form (a,b,c,b,c,a) with a+b+c=1/2, and the q-bounds are exactly a,b,c<=1/4. The torus law (U,V,(U+V) mod 1) has product-uniform two-coordinate marginals and gives a triangle vertex; coordinate permutations and mixtures preserve all pairwise product marginals and fill the triangle. The discrete and independently jittered rank-p-value CDF formulas were recomputed from the three possible test-score ranks and are consistent with the claimed sharp envelopes. The repository verifier's rational identities and finite-torus convergence are consistent with these checks.

## Originality — PASS (literature-bounded)

The full 2017 Okolewski paper was obtained through authorized institutional access and all 20 pages were inspected. Its objects are sorted order-statistic distribution functions and their linear combinations under k-dimensional marginal constraints; its explicit pairwise-independent examples concern quantities such as F_{i:n}-F_{i+1:n}, not the labeled six-permutation law. The 2025 open-access Okolewski–Błażejczyk-Okolewska paper likewise treats joint distribution/reliability functions of sorted order statistics. Kemperman's 1997 chapter was located and its publisher preview/intro pages were inspected, but a complete chapter copy was not obtained, so it is not claimed as fully read. No checked source states the exact labeled-ordering triangle or the associated two-calibration rank law.

## Scientific value — PASS

The theorem identifies the complete labeled rank law under pairwise independence, not merely bounds for symmetric order statistics, and turns that geometry into exact finite-sample calibration limits. The explicit torus extremizers make the bounds constructive rather than only existential.

## Evidence and literature

- Kemperman, Bounding Moments of an Order Statistic When Each K-Tuple is Independent (1997): https://doi.org/10.1007/978-94-011-5532-8_34
- Okolewski, Distribution bounds for order statistics when each k-tuple has the same piecewise uniform copula (2017): https://doi.org/10.1080/02331888.2017.1289533
- Okolewski and Błażejczyk-Okolewska, Tight Bounds for Joint Distribution Functions of Order Statistics Under k-Independence (2025): https://doi.org/10.3390/e27121250

## Limitations

- The exact characterization is specific to three observations.
- Extremal joint laws may be singular even though every one- and two-dimensional marginal is regular.
- Kemperman (1997) could only be inspected through the accessible preview/intro pages in this audit; an older label-sensitive formulation under different terminology therefore remains a residual priority risk.

The independent audit finds the record scientifically complete on correctness, originality, and value at the audited tree. The originality verdict is bounded by the literature access and searches described above and does not treat inaccessible material as read.
