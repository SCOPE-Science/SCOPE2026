# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces the analytic statement to Ortega-Cerdà's published boundary-measure criterion and verifies that criterion using a geometric fact about strictly convex bodies.

The geometric lemma was checked against the following possible failure modes.

1. **Fibers above the edge of the projection.** A nontrivial vertical fiber over a boundary point of the orthogonal projection would lie in a lifted supporting hyperplane of \(K\), producing a boundary line segment. Strict convexity excludes this.

2. **Boundary points inside a projected fiber.** For a full-dimensional convex body and a base point in the interior of the projection, points strictly between the lower and upper fiber endpoints are interior points of \(K\). Hence two boundary points on the same fiber separated by \(ae_n\) must be the two endpoints.

3. **Strict concavity of the section width.** Strict convexity puts the open segment between any two distinct boundary points in \(\operatorname{int}K\). Applying this separately to lower and upper fiber endpoints gives strict convexity of \(\ell\), strict concavity of \(u\), and therefore strict concavity of \(w=u-\ell\).

4. **Nullity of a positive width level.** The superlevel \(C_a=\{w\ge a\}\) is convex. If a point of \(E_a=\{w=a\}\) were interior to \(C_a\), midpoint strict concavity would give \(a>a\). Hence \(E_a\subset\partial C_a\), which is Lebesgue-null in the projection space.

5. **Lifting nullity to surface measure.** Positive width levels are compactly contained in the interior of the projection. The convex lower endpoint function is locally Lipschitz there, so the translate intersection is a finite union of Lipschitz graph images of an \((n-1)\)-dimensional null set and therefore has zero \(\mathcal H^{n-1}\)-measure.

The remaining hypotheses in Ortega-Cerdà's criterion are standard for convex bodies: finite nonzero surface measure, \(n\)-dimensional null boundary, and positive-measure access to both the interior and strict exterior in every boundary neighborhood.

No numerical computation is needed.

## Originality

**PASS, to the best of our knowledge.**

The primary source arXiv:2609.18426 was inspected at the theorem, general boundary criterion, and convex-domain extension. It states nonexistence for every bounded convex open set with \(C^2\) boundary and gives the more general boundary-measure criterion, but it does not state the no-regularity theorem for arbitrary strictly convex bodies. Its \(C^2\) proof uses a positively curved smooth patch and transversality.

Wan's simultaneous arXiv:2609.16674 was inspected at its main theorem and geometric classes. It covers balls, certain convex polytopes, spherical shells, finite unions, products, and affine images; its stated classes do not contain arbitrary strictly convex bodies.

Searches for exact and synonymous formulations involving exponential Riesz bases, strictly convex bodies/domains, rough or nonsmooth convex boundaries, and translated-boundary overlap did not locate a prior theorem implying this result. Older nearby literature includes positive Riesz-basis results for special centrally symmetric convex polytopes and orthogonal/spectral nonexistence results for convex bodies; those are different claims and do not dominate the present Riesz-basis statement.

The main residual risk is recency: both 2026 source preprints are only days old, so a simultaneous observation not yet indexed could exist. No inaccessible paper was found whose available metadata gave concrete reason to believe it already contains the arbitrary-strictly-convex Riesz-basis theorem.

The originality claim is deliberately limited to the geometric translate-overlap lemma in the form used here and its consequence for arbitrary strictly convex bodies. Ortega-Cerdà's analytic obstruction and standard convex-geometric facts are prior work.

## Value

**PASS.**

The result removes all boundary differentiability from a newly established nonexistence theorem on a natural and large geometric class. It identifies strict convexity itself, rather than curvature or \(C^2\) regularity, as sufficient to supply the boundary non-overlap required by the analytic obstruction. The proof is elementary once the general obstruction is available and gives a reusable geometric criterion for rough convex domains.

## Scope and limitations

The argument does not cover arbitrary nonsmooth convex bodies with flat faces, where translated facets can overlap in positive surface measure. It gives no classification of all convex bodies admitting or excluding exponential Riesz bases and says nothing about dimension one.

No independent validation or independent audit is claimed.
