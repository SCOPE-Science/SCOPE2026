# Review

## Correctness

PASS. After normalization to \(\mathbb Z^2\) and width \(2\), reducedness supplies primitive width directions uniquely selecting each vertex. Width directions for adjacent vertices form a lattice basis: otherwise a nontrivial lattice point in their fundamental parallelogram can be moved into the triangle they span with the origin, producing a nonzero lattice point in the interior of the polar and contradicting minimal width.

This yields the normal form
\[
P=\operatorname{conv}\{\pm(1,r),\pm(-s,1)\},
\qquad 0\le r,s<1.
\]
The diagonal width constraints force the two off-axis coordinates to have opposite signs before this normalization. The exact gauge is
\[
\|(p,q)\|_P
=
\frac{|p+sq|+|q-rp|}{1+rs}.
\]
For \(r<s\), a complete sign split proves that \(\pm e_1\) are the unique shortest nonzero lattice vectors; for \(s<r\), \(\pm e_2\) are unique. Lemma 2.1 identifies these with diameter directions, and Proposition 3.7 rules out completeness because a quadrilateral needs diameter segments ending in both opposite edge pairs. Hence \(r=s\). The zero case is the known incomplete diamond, while every positive equal-parameter case is the published twisted-square example.

The packaged exact-arithmetic checker independently stress-tests all normal-form branches on rational grids and verifies the polar and invariant identities.

## Originality

PASS with a named historical-access risk. The defining Codenotti–Freyer paper is decisive evidence: it exhibits the twisted squares as examples, explicitly gives a complete classification only for triangles, and then poses the broader simultaneous reduced/complete question while listing its known examples. Its inspected full text does not state the symmetric-quadrilateral exhaustion theorem.

Cools–Lemmens was inspected in full at its definitions and classification theorem. It classifies inclusion-minimal lattice polygons with lattice vertices and fixed lattice width, not arbitrary real quadrilaterals satisfying the newer completeness notion. Bárány–Füredi is a plausible older source on lattice diameter, but only its abstract/bibliographic material was accessible; the defining 2024 source characterizes its completeness notion as slightly different. Targeted semantic and public searches under coordinate, symmetry, polar, and terminology aliases found no equivalent theorem.

## Value

PASS. Question 5.3 of the defining paper explicitly asks for structure of bodies that are both lattice reduced and lattice complete. Origin-symmetric quadrilaterals are the smallest symmetric polygonal class in which the paper gives a nontrivial continuum of examples. Showing that this example family is exhaustive is therefore a natural classification result, not an arbitrary parameter computation. The proof also explains structurally why the two twist parameters must coincide, and the polar involution supplies a useful duality coordinate on the resulting moduli interval.

Same-model review: passed. Independent audit: not yet performed.
