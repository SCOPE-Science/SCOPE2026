# Scientific review: sharp tetrahedral-volume envelope of twisted regular polygonal prisms

## Correctness — PASS

The domain \(n\ge3\), \(R>0\), \(h>0\), \(\theta\in\mathbb R\) and the convex hull of its two rotated regular bases are unambiguous. The unrestricted maximum reduces to polytope vertices because the absolute simplex determinant is separately convex. Every vertex-supported tetrahedron has a layer split; a one-versus-three split is bounded using the sharp area of a triangle on a circle, while a two-versus-two split is exactly the determinant of two polygon chords times \(h/6\). The odd/even difference-body computation gives the exact chord-length and angular lattice; the triangle comparison proves the two-versus-two candidate dominates for every parameter, with the triangular tie explicitly retained. This is an infinite analytical proof rather than an inference from enumeration.

The packaged standalone checker enumerates all four-vertex subsets for \(3\le n\le13\), five twist values per order and two scalings, and reproduces the formula in all 110 cases. It checks, but does not certify, the universal proof. The checks are finite regression evidence only.

## Originality — PASS, with residual risks

The closest primary full text, Akopyan–Glazyrin (2014), proves general structural conditions for largest-volume simplices in ordinary prisms, not exact extremal volumes in all relatively rotated two-base regular-polygon hulls. The relevant published regular-polygon translative convex-hull result concerns a single body translated against itself, through a directional chord-width product, whereas the new extremum is a determinant of chords from two *independently rotated* bodies. The published maximal rectangle result covers the aligned regular-even-polygon benchmark, which therefore is not separately asserted as novel. Full angular dependence, both parities, unrestricted containing-body tetrahedra, and the mod-four twist-response reversal remain the claim.

Searches included twisted prism, antiprism, two parallel rotated regular polygons, cross-determinant of chords, maximum-volume simplex, and explicit formula aliases. No located source implies this whole formula; an unindexed equivalent or classical special-angle identity remains a priority risk. Search absence alone is not used as a uniqueness theorem.

## Mathematical value — PASS

Twisting is a natural one-parameter deformation from regular prisms to antiprismatoids. The maximum simplex volume is a natural affine-dimensional quality measure of these solids. Determining its sharp *entire angular envelope for every number of polygon sides* gives a reproducible benchmark, fixes all optimal twists, and reveals an order-dependent qualitative reversal: alignment is optimal if and only if the number of sides is divisible by four. These are new geometric consequences not supplied by an aligned-prism benchmark. The result requires neither a generalization to arbitrary polygons nor a downstream theorem to be a complete exact classification of this naturally parameterized invariant.

## Closest literature and limitations

The closest general prism paper is Akopyan and Glazyrin, *On maximum volume simplices in polytopes* (2014), especially their Section 4. The closest public regular-polygon determinant-adjacent computations are *Exact translative convex-hull profile of every regular polygon* and *Exact maximum-area rectangles in every regular even polygon*. Their implications and nonimplications are recorded in AUDIT.json. The theorem assumes equal concentric regular bases in parallel planes. Its statement does not classify all continuous equality families, and independently audited priority and proof validity are outstanding.

Self-review: passed. Independent audit: not yet performed.
