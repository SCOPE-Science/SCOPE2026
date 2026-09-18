# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The proof was checked at the two points where loss of boundary smoothness could have invalidated the argument.

First, the translated-boundary lemma does not use normals, differentiability, or curvature. After aligning a nonzero translation with one coordinate axis, a strictly convex body has vertical section endpoints \(a\) and \(b\), with \(a\) strictly convex and \(b\) strictly concave on the interior of the projected body. Hence the chord length \(L=b-a\) is strictly concave. Any point shared by the boundary and its translate by \(t e_n\) projects to the level set \(L=t\). Restrictions of a strictly concave function to lines meet a fixed level in at most two points, so Fubini gives zero base measure. Local Lipschitz regularity of \(a\) then upgrades this to zero \((n-1)\)-dimensional Hausdorff measure for the translated-boundary intersection.

The possible projection-boundary case was also checked: two distinct points of a vertical section above a projection-boundary point would lie in a supporting hyperplane and create a nontrivial boundary segment, contradicting strict convexity.

Second, the remaining hypotheses of Ortega-Cerdà's Remark 6.4 hold for every convex body: its boundary is Lebesgue-null with finite positive surface measure, interior points occur with positive measure in every boundary neighborhood, and a supporting hyperplane gives a positive-measure exterior half-neighborhood. Thus the cited criterion applies with \(\nu=\mathcal H^{n-1}|_{\partial K}\).

The dimension restriction \(n\ge2\) is essential and is stated explicitly.

## Originality

**PASS, to the best of our knowledge.**

The closest source is Ortega-Cerdà, arXiv:2609.18426. Its main convex extension assumes \(C^2\) boundary; Section 8 uses a positive-curvature patch to obtain singleton supporting faces and translated-boundary non-overlap. Remark 6.4 states a general boundary-measure criterion, but the paper does not state the regularity-free strictly convex corollary.

Wan, arXiv:2609.16674, was also checked. Its stated classes include balls, selected convex polytopes, spherical shells, finite unions, affine images, and products, but not arbitrary strictly convex bodies.

Searches using combinations of “Riesz basis of exponentials”, “strictly convex”, “strict convex body”, “complete interpolating sequence”, and “Paley-Wiener” did not locate an earlier theorem asserting nonexistence for all bounded strictly convex bodies without boundary regularity. Searches of the current SCOPE repository for “Riesz basis exponentials” and “strictly convex” found no overlapping record.

No originality is claimed for standard convex-section facts or for Ortega-Cerdà's abstract boundary criterion. The originality claim is restricted to the geometric translation lemma in this application and the resulting regularity-free strict-convexity theorem.

Residual risk: both 2026 source preprints are extremely recent, and a contemporaneous observation not yet indexed could overlap. No inaccessible source was identified as specifically likely to contain this exact result.

## Value

**PASS.**

The theorem removes all smoothness assumptions in a natural geometric class immediately adjacent to a new \(C^2\)-convex nonexistence theorem. It covers strictly convex bodies with nonsmooth boundary, including \(\ell^p\) balls for \(1<p<2\), and isolates a short geometric mechanism—strict concavity of chord lengths—that may be reusable in other translation-overlap criteria.

The result is complementary rather than dominating: the published \(C^2\) theorem also handles smooth convex bodies with flat pieces. This distinction is stated explicitly.

## Literature inspected

- J. Ortega-Cerdà, arXiv:2609.18426, including Theorem 1.1, Remark 6.4, and Section 8.
- Z. Wan, arXiv:2609.16674, including Theorem 1.1 and the listed geometric classes.
- A. Debernardi and N. Lev, JEMS 24 (2022), for the contrasting positive polytope theorem.

No independent validation, formal verification, or peer review is asserted.
