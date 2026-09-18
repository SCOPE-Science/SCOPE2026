# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

Han--Liu's Theorem B(iii) was checked at the full theorem statement: under local doubling and a local weak Poincare inequality, \(\mathrm{BCD}_{\delta}(K,\infty)\) gives \(\mathfrak p_{\rm par}(T_x^*X)\le8\sqrt\delta\) almost everywhere. Their Corollary 4.8 was also checked directly in the normed-space case; after division by \(2\|p\|^2+2\|q\|^2\), it records the corresponding von Neumann--Jordan ratio and the bound \(C_{\rm NJ}(F^*)\le1+8\sqrt\delta\).

The passage from parallelogram defect to the symmetric von Neumann--Jordan constant was checked independently. For the ratio
\[
R(u,v)=\frac{\|u+v\|^2+\|u-v\|^2}{2\|u\|^2+2\|v\|^2},
\]
the denominator dominates the normalizing maximum used by Han--Liu, so \(|R-1|\le\mathfrak p_{\rm par}\). The involution \((u,v)\mapsto((u+v)/2,(u-v)/2)\) replaces \(R\) by \(1/R\), exactly matching Passer's symmetric convention.

Passer's Theorem 3.4 was inspected directly. It gives
\[
d_{\rm BM}(E,\ell_2^m)\le1+(18m^2-17m+14)\varepsilon+O_m(\varepsilon^2)
\]
for an \(m\)-dimensional real normed space with von Neumann--Jordan constant \(1+\varepsilon\). Substitution of \(\varepsilon\le8\sqrt\delta\) therefore yields the stated coefficient and \(O_m(\delta)\) remainder. Passer's Theorem 2.9 gives the exact two-dimensional rational-square-root expression used in the record. Finite-dimensional Banach--Mazur duality transfers the estimate from \(F^*\) to \(F\).

The sharpness argument was checked against Han--Liu's Lemma 4.10 and Theorem 4.11. They prove \(\mathfrak p_{\rm par}(F_\tau^*)\ge \mathcal Q(H)|\tau|/2\) for nonquadratic perturbations and \(\Delta_{\rm BCD}(F_\tau)\asymp_H\tau^2\). The elementary inequalities
\[
C_{\rm NJ}(E)\le d_{\rm BM}(E,\ell_2^{\dim E})^2,
\qquad
C_{\rm NJ}(E)-1\ge\frac12\mathfrak p_{\rm par}(E)
\]
were rederived from the definitions. They imply a linear lower bound for Banach--Mazur distance along the perturbation family, while the defining formula for \(F_\tau\) gives the matching linear upper bound. Hence the square-root dependence on \(\Delta_{\rm BCD}\) is genuinely sharp in exponent.

## Originality

The complete Han--Liu preprint was inspected at Theorem B, Corollary 4.8, the perturbation expansion, Lemma 4.10, and Theorem 4.11. It proves quantitative parallelogram control and states that the square-root exponent there is sharp, but searches of the full text found no Banach--Mazur formulation or quantitative ellipsoidal/tangent-ball conclusion.

Passer's paper supplies the pre-existing approximate Jordan--von Neumann theorem and is explicitly treated as prior art. Searches covered combinations of "almost BCD", "barycenter curvature-dimension", "Wasserstein barycenter", "parallelogram defect", "von Neumann--Jordan", "Banach--Mazur distance", "Euclidean tangent", and "ellipsoid". No source was found combining the BCD entropy error with Banach--Mazur Euclideanity or deriving the sharp \(\sqrt\delta\) Banach--Mazur scale. Searches of the current SCOPE archive by the same objects and claim family found no overlap.

No inaccessible paper was identified whose title or accessible metadata specifically suggests this quantitative bridge. Because Han--Liu's motivating preprint is dated 17 September 2026, unindexed or unpublished parallel work remains a meaningful residual risk.

## Value

The result converts an infinitesimal algebraic defect into a standard affine-geometric distance. It says that almost barycentric entropy convexity does not merely make tangent norms approximately satisfy one identity: it forces their unit balls to lie quantitatively close, up to linear equivalence, to ellipsoids. The normed-space specialization provides a direct global shape theorem, the two-dimensional case is explicit at finite error, and the perturbation family proves the square-root rate cannot be improved in general.

## Limitations

The dimension dependence in the coefficient is not claimed optimal. In dimensions above two, Passer's available general estimate is asymptotic for small defect. Banach--Mazur control of tangent fibers does not by itself produce a global metric or measured-Gromov--Hausdorff stability theorem for the ambient space. Very recent parallel work may not yet be indexed.
