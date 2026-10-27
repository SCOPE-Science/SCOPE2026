# Scientific review

## Correctness — PASS

All affine self-maps of \(R_n\) are quandle endomorphisms, and the consecutive-residue recurrence proves that they exhaust the endomorphism monoid. Every nonempty subquandle is a coset because two right reflections generate translation by twice a difference, and the cyclic quotient \(H/2H\) has size at most two. For each endomorphism slope \(u\), exactly \(|U|\) intercepts map any given coloring image into \(U\). The torus-braid recurrence identifies the image-size spectrum, and the multiplication map \(u\mapsto u\delta\) has uniform fiber size \(n/r\); the target-index and defect-weight census yields every exponent of the claimed graded polynomial. In particular the image-size strata are disjoint, with integer coefficients and nonnegative exponents for all \(n\ge2\). The included standard-library verifier independently checks all maps for small \(n\), all subquandles for \(n\le10\), and direct braid/endormorphism enumeration over specified moduli. Finite checks are only corroboration.

## Originality — PASS, qualified

The 2026 paper of Ceniceros–Chidley–Vaughn [2] defines the two new polynomials and computes selected examples. It does not supply an all-link ungraded evaluation for the *entire* dihedral endomorphism monoid or the all-parameter graded divisor formula. Yonemura–Nakamura [1] classifies finite subquandles of spherical quandles, rather than polynomial invariants for a filtration of cyclic quandles. Elhamdadi–Jones–Liu [3] treats unfiltered torus-link coloring quivers; its known quandle-endomorphism and coloring-count ingredients are not presented as new here. Direct formula/alias searches and semantically closest available mathematical research records did not identify either exact new result. The 2024 work could in principle be used as an input to a further computation, but the full target-index/defect-weight implication is not supplied there. Mathematical priority is subject to older or unindexed equivalent enumerations.

## Mathematical value — PASS

The broad result proves a structural *degeneracy theorem* for a newly introduced invariant: for every link and any nonempty dihedral subquandle filtration, using all endomorphisms never enhances the underlying stage-by-stage coloring counts. The graded formula then gives a complete, nonconstant contrast on a natural infinite torus-knot family, with a divisor-indexed closed form, multiplicities, a sharp monomial count, and an explicit composite-modulus example. This clarifies when a polynomial construction loses information and exactly which information its grading retains; it is not merely a textbook restatement of coloring counts.

## Closest literature and limitations

[1] K. Yonemura–N. Nakamura, *Classification of Finite Subquandles in Spherical Quandles*, arXiv:2607.17137 (2026-07-19): finite spherical subquandle structure, no graded link invariant.

[2] J. Ceniceros–B. Chidley–J. Vaughn, *Polynomial Link Invariants via Decategorification of Subquandle Quiver Filtrations*, arXiv:2608.05014 (2026-08-05): source of the polynomial definitions, illustrative computations rather than the present all-parameter calculation.

[3] M. Elhamdadi–B. Jones–M. Liu, *Quandle Coloring Quivers of General Torus Links by Dihedral Quandles*, arXiv:2403.04534 (2024-03-07): complete unfiltered quiver context and earlier ingredients, not the filtration/defect-weight calculation.

The conclusions require the *complete* endomorphism set. The graded formula is restricted to \(\{0\}\subset R_n\) and odd positive two-strand torus knots. No general assertion is made that the graded polynomial distinguishes links with equal counting sequences. Earlier or unindexed equivalent formulas remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
