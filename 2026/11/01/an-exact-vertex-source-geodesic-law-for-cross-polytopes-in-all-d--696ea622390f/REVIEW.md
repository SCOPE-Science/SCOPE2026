# Self-review

## Correctness — PASS

The absolute-coordinate folding is nonexpansive on all rectifiable surface paths, and signs can be restored by an isometry fixing the source. The folded surface consists exactly of two regular simplices sharing an equatorial facet. Their Euclidean development gives a global lower bound on every folded path. The explicitly computed crossing point lies inside the shared facet and hence realizes the straight developed segment, proving equality and the universal squared-distance identity (including the boundary and antipodal cases). The sharp stretch follows from \((1+t)^2\ge4t\), with equality only at the antipode. The probability law and moment follow from the Dirichlet law on congruent facets. Exact-rational tests in 4,002 configurations and 180,000 distribution samples support the proof; finite tests are not substitutes for it.

## Originality — PASS, with priority risk

The material inspected from Miller–Pak covers the source-unfolding and general higher-dimensional geodesic algorithm but does not state the cross-polytope's pointwise identity or the exact excess law. The full relevant statements and final Corollary 3.7 of Saso–Schuerger–Shi cover **three-dimensional** octahedral point-to-point distances and therefore subsume the \(n=3\) specialization. That case is prior art, not an originality claim. The previously documented fixed-vertex octahedron distance distribution similarly concerns \(n=3\); a regular-simplex vertex dilation concerns a different polytope family. The all-dimensional identity, especially \(n\ge4\), and the area-uniform squared-excess law were not found in the searches performed. Historical priority remains subject to independent literature examination and other vocabulary.

## Mathematical value — PASS

This is a complete pointwise intrinsic-to-extrinsic distance identity for a canonical regular polytope family in arbitrarily high dimensions. It gives both a unique sharp stretch point and an exact, dimension-dependent area-uniform detour distribution. The distinction between the worst excess of order \(1/n\) and the mean excess of order \(1/n^2\) is structural; a generic polyhedral shortest-path algorithm does not itself express these formulas. The result is not a numerical instance, arbitrary slice, or reformulation of the octahedral \(n=3\) special case.

## Closest literature, scope, and limitations

Relevant primary works: Miller and Pak, arXiv:math/0312253 (2003); Demaine and O'Rourke, *Geometric Folding Algorithms*, Ch. 24 (2007/2010 online); Saso, Schuerger and Shi, arXiv:2405.20344 (2024). The mathematical scope is a **vertex source** on the cross-polytope's **entire boundary** with Euclidean path length; not arbitrary-source or skeleton-only geodesics. The \(n=3\) pointwise specialization is already implied by published 2024 octahedral formulas. No independence is asserted for this review.

Self-review: passed. Independent audit: not yet performed.
