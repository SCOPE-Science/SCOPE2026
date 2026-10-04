# Same-model review

## Correctness — PASS
The proof uses two independently sourced prior facts: the illuminating center is the planar \(r^{-2}\)-center and is unique for convex bodies, and a triangle's illuminating center satisfies Shibata's equal angle-to-area ratios. Reflection puts the unique center on the altitude. The base subtriangle has area fraction \(q\), so its central angle is \(2\pi q\), while direct geometry gives \(2\arctan(1/(\lambda q))\). This yields the claimed equation. Strict scalar monotonicity proves uniqueness, implicit differentiation proves monotonicity in aspect ratio, and elementary expansions prove the endpoint laws. The right-isosceles numerical check agrees with Finch.

Risk: the proof depends on the correctness of the published prior uniqueness theorem and the quoted Shibata characterization; both are materially present in inspected sources. The numerical verifier is not used as an infinite proof.

## Originality — PASS
Finch is the closest same-object source inspected in full: it gives the angle/area characterization and a right-isosceles decimal, but not an isosceles-family equation. O'Hara gives broader renormalized-center theory and uniqueness, not location formulas. Targeted searches for streetlight, illuminating-center, \(r^{-2}\)-center, angle/area, right-isosceles, tangent/cotangent, and the benchmark decimal found no statement implying the theorem.

Risk: Shibata's 2009 unpublished manuscript is a plausible covering source, but its historical URL was inaccessible and exact-title searches exposed no family formula. This access gap is retained as a residual risk; it is not counted as evidence of novelty.

## Value — PASS
A natural one-parameter shape family receives a complete scale-free coordinate law rather than one more decimal. The theorem explains how the center moves under aspect-ratio deformation, gives both degeneration regimes, and exactly recovers the canonical right-isosceles benchmark. The claim is intentionally limited to this family and does not overstate a general triangle solution.

Same-model review: passed. Independent audit: not yet performed.
