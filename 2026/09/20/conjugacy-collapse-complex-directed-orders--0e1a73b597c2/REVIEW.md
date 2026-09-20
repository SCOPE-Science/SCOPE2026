# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof separates into three standard but compatible ingredients. First, the source paper proves that for every admissible real generator T, the complex field is algebraic over k(T). Since K=k·Qbar is algebraic over k, T remains transcendental over K and C is an algebraic closure of K(T). The K-isomorphism K(T) -> K(U) therefore extends to an automorphism of C. Because this automorphism fixes k and the algebraic numbers, it carries the defining localized ring, its integral closure, and the real-algebraic leading coefficients for P_T exactly to those for P_U.

The continuum lower bound uses T_c=pi+c pi^2 with c in k. Each T_c is transcendental over k. Equality of two cones invokes the source paper's exact equality criterion and yields a quadratic polynomial relation for pi over H_k; since H_k/k is algebraic and pi is transcendental over k, all coefficients vanish and c=d. The upper bound is immediate from the real parameter set.

For the topology statement, every continuous field automorphism of C fixes R pointwise by rational approximation and hence is identity or complex conjugation. Conjugation stabilizes each P_T because its defining local ring is real and integral closure is preserved. Thus no continuous automorphism moves one cone to a distinct cone.

No computational evidence is needed for these algebraic statements.

## Originality

**PASS, to the best of our knowledge.** The full accessible text of arXiv:2609.20494v1 was inspected around the construction, the statement and proof of Theorem 1.2, and the concluding remarks. It classifies when two generators give the same cone and notes a possible extension of that equality question to different coefficient fields. No classification up to field automorphism/order isomorphism, no single-orbit statement, and no continuity obstruction was located in that text.

Targeted searches for directed partial orders on the complex field together with field automorphisms, conjugacy, isomorphism, and positive cones did not locate the theorem above. Earlier work located in the search, including Schwartz--Yang (2023), addresses existence of compatible directed orders rather than automorphism classes of this 2026 explicit family.

The main residual originality risk is substantial but specific: the proof is a short consequence of the source paper's one-variable algebraicity observation plus the classical extension theorem for algebraic closures. An unpublished note, unindexed contemporaneous response, or later revision of the source preprint could therefore contain the same observation. The standard uniqueness/isomorphism-extension theory of algebraic closures is prior work and is not claimed as new.

No highly relevant inaccessible paper was identified that gave concrete evidence of prior coverage. The search is not exhaustive over all historical literature on partially ordered fields.

## Value

**PASS.** The result changes the structural interpretation of the source family's parameter classification. The source exhibits many different embedded cones and characterizes equality; the present theorem shows that all of them nevertheless define the same abstract ordered field up to automorphism. At the same time, continuum many distinct cones remain visible inside the standard complex field, and the conjugacies between distinct cones are forced to be discontinuous. This cleanly separates algebraic order type from the ordinary topology of C.

## Scope and status

The theorem concerns one fixed coefficient field k and only the explicit Wang--Yuan--Zhang--Zhu family. It does not classify all directed orders on C or solve the lattice-order problem. The review is not independent validation, formal verification, or peer review.
