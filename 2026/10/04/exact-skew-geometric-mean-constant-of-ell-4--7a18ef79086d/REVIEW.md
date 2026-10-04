# Same-model review of Exact skew geometric mean constant of \(\ell_4\)

## Correctness
PASS. The definition and quantifiers are explicit. The coordinatewise operator estimate proves the global upper bound in arbitrary \(\ell_4(I)\); the two-coordinate construction converts any maximizing vector for the finite-dimensional matrix norm into unit vectors for which both transformed norms equal that matrix norm. The generalized Rayleigh quotient is exhaustive because every nonzero \((r,q)\in\mathbb R^2\) has a real square root \(u+iv\). Exact expansion of the characteristic polynomial and its discriminant is replayed by `verify.py`.

## Originality
PASS. The defining 2023 preprint and its 2025 journal version were inspected at the definition, global bounds, and concrete examples. They calculate the Hilbert value, the square-plane value, and a mixed \(\ell_\infty\)-\(\ell_1\) example, but not \(\ell_4\). Searches combining the invariant name and notation with \(\ell_4\), matrix-norm language, and the resulting radical expression did not identify an equivalent or stronger formula. The cumulative prior ledger was also searched for the invariant and aliases, with no matching accepted claim.

## Value
PASS. The result supplies a complete two-parameter benchmark for a canonical uniformly convex non-Hilbert space, rather than a single numerical slice. It also exposes a reusable operator-norm reduction and gives a sharp closed form between the known Hilbert and square-plane extremes. This is a motivated exact invariant for the new geometric constant.

## Closest literature and limitations
The closest source is Ni–Liu–Zhou, DOI 10.22541/au.169235474.44030928/v1, followed by the journal version DOI 10.7153/mia-2025-28-22. The result is limited to the real \(\ell_4\) exponent; no claim is made for general \(p\), and database searches cannot exclude all unindexed literature.

Same-model review: passed. Independent audit: not yet performed.
