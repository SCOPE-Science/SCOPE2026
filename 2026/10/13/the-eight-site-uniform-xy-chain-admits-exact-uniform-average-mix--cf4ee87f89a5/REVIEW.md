# Self-review

## Correctness
PASS. For \(q=9\), the positive Bohr frequencies have exactly one rational relation, \(\theta_1-\theta_2-\theta_4=0\), because \(\theta_2=\theta_1^2-2\) and \(\theta_1\) has irreducible cubic \(x^3-3x-1\). The resulting phase closure is a three-torus. The packaged \(4^3\)-point rational measure exactly realizes all \(28\) target coherences. The source identities then give \(\widehat M=J/8\). Exact affine rank \(16\), strict positivity of all phase weights, Kronecker density, equality of relative interiors under convex closure, and Carathéodory give an actual finite time law with at most \(17\) atoms.

The finite checks were replayed from `artifacts/verify.py` and returned `VERIFY_OK`. They are exact integer/rational calculations, not numerical evidence for an infinite claim.

## Originality
PASS. The anchor arXiv:2609.14463v1 explicitly leaves moduli outside its positive and parity-collision families unresolved; \(q=9\) is the smallest such modulus. Direct full-text inspection of the anchor found no \(q=9\) construction. Baptista--Coutinho--Marques provide the general arbitrary-distribution framework and small-path examples, while Kang's earlier note gives a negative certificate for \(P_{11}\); neither implies the \(P_8\) result.

Source-specific, alias, parameter, and implication searches were run in the semantic findings index. No implication-equivalent indexed finding was found. Residual risk remains that an unindexed public note independently settles \(P_8\).

## Value
PASS. This closes the first open modulus in a new arithmetic classification and shows that rational dependence of the positive Bohr frequencies is not itself an obstruction to exact randomized uniform mixing. The proof supplies a concrete exact certificate and a support bound of \(17\), while introducing a relative-interior phase-certificate route that can be tested on other unresolved composite moduli.

The value claim is intentionally narrow: it does not assert a general classification or explicit readout times.

Self-review: passed. Independent audit: not yet performed.
