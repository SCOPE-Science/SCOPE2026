# Scientific review: bielliptic cyclic trigonal genus-four strata

## Correctness — PASS

The theorem is quantified over every smooth coefficient-marked member of the two-parameter genus-four family over an algebraic closure of characteristic seven. The discriminant criterion follows by reduction to the cubic in the squared coordinate; the genus follows by Riemann–Hurwitz. The four differentials were checked at all finite branch points and at infinity. The Cartier coefficient extraction gives a determinant \(3(ab+1)^2\Delta^2\), and the rank-one block on the nonordinary hyperbola has the explicitly oriented Frobenius second product \(B^{[7]}B\). Exact factorization leaves 24 simple roots outside the discriminant. Both standalone algebraic and independently written finite-field programs reproduced the stated identities and stratification. Finite enumerations were not used in place of a proof over the algebraic closure.

## Originality — PASS, with residual risk

The closest inspected primary text is Ogasawara–Ohashi–Sakata–Harashita, *Superspecial genus-4 double covers of elliptic curves*, arXiv:2403.08139v1, especially its introduction, double-cover model, Cartier section, and enumeration section. It classifies smoothness and enumerates superspecial covers, not the smooth ordinary-elliptic-quotient family’s 24-point \(7\)-rank-one locus. Borges–Gonçalves, arXiv:2212.03987, treats Fermat-type and related \(p\)-rank calculations; the inspected full arXiv paper, including the main theorem and Section 6 on related families, does not state or imply this classification. The 2025 Sohn paper (DOI:10.23091/japm.2025.059) is a plausible source for the genus-four \(a\)-number statement; full text could not be inspected, so its potential overlap is not dismissed. The Hasse determinant alone is not treated as the new contribution: the exact characteristic-seven stable Frobenius rank stratification and eight cubic orbits are.

Searches of mathematical research records, primary articles, and direct equation/parameter/duality aliases found no matching or implication-dominating full-rank classification. Failed searches do not prove universal priority. Existing computations of superspecial curves do not imply the \(7\)-rank-one count because every smooth member here has ordinary elliptic quotient and is not superspecial. The uninspected 2025 paper and possible unindexed special-family studies remain priority risks.

## Mathematical value — PASS

The construction is motivated by the natural involution and genus-one quotient rather than an arbitrary polynomial slice. The result fully resolves the ordinary/nonordinary divisor, its constant \(a\)-number jump, and the deeper \(7\)-rank-one stratum on the smooth base. It distinguishes Cartier rank from stable semilinear Frobenius rank and gives the exact field-of-definition orbit structure of every exceptional coefficient-marked fiber. It does not claim a moduli-isomorphism classification, a Newton-polygon classification, or an optimality principle.

## Reproducibility and limits

`verify_symbolic.py` proves all polynomial identities, the factorization of the exceptional polynomial and disjointness from the discriminant. `verify_fields.py` independently computes Cartier coefficients over all coefficient pairs of three finite fields. Both ran successfully. The independent finite-field check is corroboration, while the symbolic argument establishes the theorem over the algebraic closure. Mathematical independence of the review and third-party validation have not been established.

Self-review: passed. Independent audit: not yet performed.
