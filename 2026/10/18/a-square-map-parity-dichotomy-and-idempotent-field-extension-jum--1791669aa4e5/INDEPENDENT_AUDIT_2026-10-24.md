# Independent mathematical audit

## correctness

PASS

For any char-two field K and nonempty generating S⊂(F2)^d\{0}, translate matrices P_s commute and satisfy P_s²=I, so binary adjacency A=∑P_s obeys A²=(|S| mod2)I by vanishing cross terms. Evolution square Q(x)=A x^{[2]}, whence Q(Q(x))=(|S| mod2)x^{[4]}. Even valency implies Q²=0, hence no nonzero idempotent. For odd valency, A²=I and B=A+I is square-zero. An idempotent satisfies coordinatewise x^4=x, so its coordinates must lie in K∩F4 (F2 if F4 absent, F4 otherwise). In F2 its condition is Bu=0, yielding 2^{N−rank B}; in F4 writing x=u+omega v gives v=Bu and Bv=0 automatically, yielding exactly all 2^N binary parameters u+omega Bu. This includes infinite char-two coefficient fields and is independent of F4 root choice. Hypercube odd d rank B=N/2 by a square-zero truncated group-ring variable change; for complete cubelike S=G\{0}, B=J rank1. Independent GF2/GF4/GF8 direct square-product/idempotent enumeration covered 15 small cases with ranks and formulas; proof is algebraic for all fields, not an experimental extrapolation.

## originality

PASS

Inspected Giacomelli’s full Expander Evolution Algebras (arXiv:2605.12672v1) including its Cayley construction §9.1 and growth/persistence Theorems 4.3/4.5; these use graph-neighborhood support but do not account for char-two coefficient cancellation. The square-map parity identity provides a concrete boundary/counterexample to unrestricted support persistence; it is not presented as novelty of the Cayley construction itself. Costoya–Muñoz–Tocino–Viruel 2023 primary full PDF concerns automorphism groups, not this explicit idempotent-element count. García-Martínez–Pérez-Rodríguez 2026 discuss existence of idempotents over complex fields in a different algebraic regime. A 2026 survey by Kaygorodov–Martín González–Viruel reports average idempotent numbers over finite fields, a potentially relevant stronger result whose full arXiv text was inaccessible this run; available synopsis gives no same cubelike all-characteristic-two theorem. The F2 perfect-algebra subcase has prior census and is excluded from independent novelty.

## value

PASS

A natural, connected cubelike Cayley family exhibits a sharp dynamical parity distinction and a genuinely discrete extension-of-scalars jump in finite idempotent-element counts, an intrinsically useful invariant not implied by graph expansion alone. The construction supplies an explicit structural obstruction to a proposed graph-support persistence principle and field-uniform parametrization; this goes beyond restating a standard quadratic identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
