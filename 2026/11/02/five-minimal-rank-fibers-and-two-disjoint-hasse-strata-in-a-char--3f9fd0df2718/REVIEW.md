# Scientific review

## Correctness — PASS

The smoothness domain is precisely the complement of the zeroes of the initial factor and the cubic discriminant. A direct coefficient extraction from the tenth-degree branch polynomial cubed yields the full characteristic-seven Cartier matrix, whose determinant equals the displayed multiplicity-two Hasse factorization. The restrictions of the cubic and discriminant to the parabola prove that the rank-drop divisors cannot intersect on the smooth base. On the rank-one two-dimensional block, the Frobenius twist is essential: computing the scalar of the second Cartier iterate, rather than treating an ordinary matrix trace as a semilinear invariant, gives the factor with exactly five admissible roots. All parameter and field quantifiers are covered by polynomial identities over the algebraic closure. Symbolic identities were replayed from `verify_symbolic.py`, and a separate no-SymPy implementation `verify_fields.py` calculated Cartier iterates and ranks on every smooth marked point over the fields of sizes seven and forty-nine and at all five deep points over the field of size 343. The finite enumerations are corroboration, not an infinity argument.

## Originality — PASS, with residual risk

Kudo--Nakagawa--Takagi explicitly give this genus-four automorphism-six family, its elliptic quotient, the general support pattern for its Cartier matrix, and a superspeciality-enumeration algorithm (2022/2023). Their journal correction was inspected. Their theorems do not state the full characteristic-seven marked-parameter \(a\)-number and \(7\)-rank stratification, the multiplicity-two Hasse component, or the exact five rank-one points. Kudo--Harashita's older nonexistence of superspecial genus-four curves in characteristic seven implies only the absence of \(a=4\), not the much more precise classification. Existing searches for equivalent curve models, coefficients, stable-rank formulas, and stronger prior genus-four theorems did not locate an implication of the new statement. Accessible related research claims involve other families and characteristics. Residual priority risk: an unindexed computation of the same specialized family may exist; no absolute uniqueness is asserted.

## Mathematical value — PASS

A full two-parameter geometric rank stratification, rather than an isolated finite-field example, is a natural refinement of published superspeciality investigations. It locates the elliptic quotient's Hasse divisor and a different double divisor controlling the three-dimensional complement, shows those components do not meet in the smooth base, identifies the deeper nilpotence locus, and obtains an exact Frobenius-orbit census for its five minimal-rank fibers. This can guide arithmetic-geometric studies of the family's nonordinary and Prym degeneration strata even without classifying full Newton polygons or isomorphism types. The explicit double Hasse component and rank-one locus are not consequences of merely knowing that there are no superspecial genus-four curves in characteristic seven.

## Closest sources and limits

- Kudo, Nakagawa and Takagi, *Efficient Search for Superspecial Hyperelliptic Curves of Genus Four with Automorphism Group Containing* \(\mathbb Z_6\), arXiv:2210.14822 and DOI 10.1007/s11786-023-00571-w; the 2023 correction DOI 10.1007/s11786-023-00573-8 was also examined. Their family is identical; their stated targets are different.
- Kudo and Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114. Its superspecial nonexistence theorem is strictly weaker for this question.
- Yui (1978) and Elkin (2011) furnish general methods and bounds; no exact specialization to the five rank-one marked parameters was identified.

The theorem is only about smooth coefficient-marked fibers in characteristic seven, not geometric isomorphism classes. Earlier unindexed equivalent calculations remain possible.

Self-review: passed. Independent audit: not yet performed.
