# Scientific review: the rooted antichain expansion

## Correctness — PASS

The lemma that \(A_v\) enumerates rooted ancestor antichains is a disjoint choice at each root. Every non-antichain general-position set has exactly one selected vertex above all its other selected vertices and exactly one child subtree containing those others; the others form a nonempty antichain. The converse follows from uniqueness of tree paths. These two disjoint classes prove the stated weighted polynomial identity for all finite nonempty trees, including the singleton. The direct geodesic brute-force, independent recurrence, root tests, and weighted checks in `verify.py` agree on the documented finite collection. Risk: the finite checks alone do not establish an infinite theorem; they support the written bijective proof.

## Originality — PASS

The nearest directly relevant primary literature is Iršič, Klavžar, Rus and Tuite, *General Position Polynomials* (2024), notably Proposition 2.2 and Sections 2 and 4. It introduces the invariant, gives exponential inclusion–exclusion over maximal general-position sets, and studies special tree families, but does not state the all-tree weighted antichain expansion or its root-by-root polynomial algorithm. Earlier maximum-general-position results concern cardinality, not all-set weight enumeration. Explicit spider and double-star cases are covered by the new theorem but do not cover it in reverse. Searches for equivalent formulations through tree antichains, geodesic convexity, and general-position polynomial recurrences found no dominating published theorem. Residual risk: an earlier paper may encode an equivalent recurrence under a different name; absence from searches is not proof of novelty.

## Value — PASS

The general-position polynomial is a natural invariant introduced specifically to distinguish all-cardinality behavior of vertex configurations. The theorem determines the *entire multivariate invariant on every finite tree*, replacing exponentially sized maximal-set inclusion–exclusion with a compact structural decomposition and polynomial-time coefficients. It substantially extends scattered family-specific enumerations, and its weighted form supports vertex-inhomogeneous counting. It is not merely a special numerical example, a textbook coefficient check, or a renaming of a previously established scalar parameter. Risks: the identity does not address cyclic graphs, and no claim of new graph-distinguishing power beyond the polynomial itself is made.

Self-review: passed. Independent audit: not yet performed.
