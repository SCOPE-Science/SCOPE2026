# Scientific review: symmetric genus-five Howe family in characteristic three

## Correctness — PASS

The branch conditions in `RESULT.md` are equivalent to separability and geometric disjointness; their eight branch points yield genus five by Riemann–Hurwitz. The Klein-four quotient gives an isogeny of degree a power of two to two elliptic Jacobians and one genus-three Jacobian, which preserves their characteristic-three invariants. Direct coefficient extraction yields the genus-three Hasse block with determinant \(b^2-c\) invertible across the smooth domain. Consequently its Frobenius-stable rank is exactly three or two, not merely the rank of a one-step matrix. The addition of ranks and \(a\)-numbers, the Newton slopes, and finite-field inclusion–exclusion have no missing boundary case. A separate exact gcd/matrix program checked all parameters over four fields, returning `VERIFY_OK`; these calculations are checks, not proof of the infinite statement.

## Originality — PASS

The closest mathematical texts are Moriya–Kudo (2023), Kudo (2024), Kawakita (2024), and Ohashi (2026). The first two construct plane sextic models and analyze their singularities, with the second treating the disjoint elliptic quotient type but excluding characteristic three. The later arithmetic papers consider Serre-bound examples and superspecial constructions in different characteristics, without the displayed complete rank-locus and counting formulas. A prior reciprocal-quartic genus-three calculation only covers a restricted quotient slice, not the genus-five fiber-product census. Standard quotient decomposition and Cartier extraction are expressly acknowledged as prior tools. Exact unindexed calculations remain a possible overlap risk; search non-detection is not a mathematical uniqueness proof.

## Mathematical value — PASS

The symmetric two-parameter family comes from a fixed supersingular elliptic quotient and a shared involution of the base, a motivated geometric sublocus of genus-five Howe covers. The result gives the complete Newton polygon stratification: a normal-crossings union of two rank-drop divisors with one deeper point. It also determines precise marked-parameter counts over every ternary field, with a nontrivial parity transition arising from the split versus nonsplit discriminant boundary. This precise arithmetic classification is the value claim, not the already-standard Jacobian decomposition.

## Limits

Only coordinate-marked smooth parameters of the displayed two-dimensional family are counted, not isomorphism classes. Individual Weil polynomials and full Ekedahl–Oort invariants are not computed. Older unindexed literature may contain an equivalent calculation; independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
