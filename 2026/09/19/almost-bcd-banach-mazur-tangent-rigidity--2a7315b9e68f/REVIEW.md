# Review — Almost BCD forces Banach–Mazur Euclidean cotangent fibers at the sharp square-root scale

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The upper bound has two quantitative inputs. Han–Liu's Theorem B gives the almost-everywhere cotangent estimate \(\mathfrak p_{\rm par}(T_x^*X)\le8\sqrt\delta\) under the stated doubling and Poincaré hypotheses. The normalized defect controls the usual von Neumann–Jordan ratio with the same error, because each term in its maximum denominator is bounded by \(2\|p\|^2+2\|q\|^2\). Passer's finite-dimensional quantitative Jordan–von Neumann theorem then gives
\[
 d_{\rm BM}(E,\ell_2^k)\le1+(18k^2-17k+14)\varepsilon+O_k(\varepsilon^2),
\]
which yields the stated coefficient after \(\varepsilon\le8\sqrt\delta\). His explicit two-dimensional formula gives the displayed closed bound after direct substitution.

The sharpness argument was checked separately. If \(D=d_{\rm BM}(E,\ell_2^k)\), comparison with any Euclidean norm realizing a factor \(D'>D\), followed by the exact Euclidean parallelogram identity, gives \(\mathfrak p_{\rm par}(E)\le4(D'^2-1)\); letting \(D'\downarrow D\) proves the lemma. Han–Liu's nonquadratic perturbations have \(\mathfrak p_{\rm par}(F_\tau^*)\ge \mathcal Q(H)|\tau|/2\) and \(\Delta_{\rm BCD}(F_\tau)\asymp_\psi\tau^2\). Finite-dimensional duality preserves Banach–Mazur distance, so these facts force a linear-in-|τ| Banach–Mazur departure and hence the claimed sharp square-root order.

No numerical experiment is needed for the proof.

## Originality

The Han–Liu preprint was inspected at the statements defining the normalized parallelogram defect, Theorem B, Corollary 4.8, and Theorem 4.11. It supplies the entropy-to-parallelogram estimate and the quadratic perturbation scale, but does not state a Banach–Mazur bound and contains no occurrence of “Banach-Mazur” or a citation to Passer. Passer's paper was inspected at its main finite-dimensional theorem and explicit two-dimensional theorem; it concerns approximate parallelogram laws for normed spaces and predates the BCD framework.

Searches for combinations of almost BCD, Wasserstein barycenters, Banach–Mazur distance, parallelogram defect, Euclidean tangent or cotangent fibers, and the recent source identifier did not locate the stated BCD-to-Banach–Mazur tangent estimate or the transfer of the Han–Liu perturbations to a sharp Banach–Mazur exponent. The current SCOPE archive was also checked by the source identifier and the principal mathematical phrases, without a matching record.

The broader approximate-inner-product literature makes differently phrased overlap possible, especially for the elementary normed-space lemma, but no source located states the combined metric-measure conclusion or the sharp entropy exponent in Banach–Mazur distance. The motivating preprint is recent, so not-yet-indexed parallel work remains a residual originality risk. Originality is therefore asserted only to the best of our knowledge.

## Value

The result converts an analytic entropy error in almost BCD directly into a standard affine-geometric distance from each finite-dimensional cotangent norm to the Euclidean class. It provides an ellipsoid-sandwich interpretation of “almost Riemannian” tangents, an explicit two-dimensional estimate, and a dimension-dependent quantitative modulus in all finite dimensions. The perturbation argument shows that the square-root loss is intrinsic rather than an artifact of the transfer estimate.

## Limitations

The constants and the admissible smallness threshold depend on dimension. The conclusion is almost-everywhere and fiberwise, not a global metric-closeness theorem. No optimal Banach–Mazur constant is claimed. No dimension-free infinite-dimensional statement is asserted. The literature check cannot exclude future or presently unindexed work on the recent almost-BCD condition.
