# Scientific review

## Correctness — PASS

The claim concerns exactly the Gaussian probability-normalized Fock norm and complex degree-at-most-two polynomials. Gaussian monomial orthogonality independently yields the displayed formulas for both squared quantities. The identity \(U-V=(|a|^2+|b|^2+2|c|^2)^2-|a|^4\) proves that, when all coefficients are present, the coefficient-phase maximizing ratio is uniquely the anti-aligned configuration. All coefficient-zero cases have ratio at most two and cannot attain the claimed value. After scale reduction, the deficit is a convex quadratic in the middle-coefficient squared magnitude, and an exact quartic sign certificate handles the remaining radius. The quartic has a verified double root at the algebraic optimum and exactly two additional real simple roots isolated by rational strict inequalities. Its leading sign and the independent isolating intervals for the concave phase coefficient settle every positive parameter, establishing both sharpness and equality classification. The exact symbolic checker from this package returns `CHECK_OK 29`; its finite examples are supplementary, not substitutes for the polynomial proof.

## Originality — PASS relative to inspected evidence

Bortolotto and Ramos, arXiv:2608.26365v1 (2026-08-26), introduction, proof and comments, establish existence of an unspecified constant for every entire Fock function; this logically yields a non-sharp degree-two bound but does not determine the exact constant, its cubic minimal polynomial or extremizers. Bertolini et al., arXiv:2605.20527v1, abstract and main theorems, study related modulus (rather than the exact square/variance ratio) stability and do not state the present extremal calculation. Searches for Gaussian quartic, squared-Fock coercivity, degree-two sharp constants and the exact cubic found no equivalent statement in the inspected published and mathematical-record corpus. Closest recorded Fourier fourth-moment extrema concern distinct finite-field or other Hilbert-space functionals; they neither imply nor are implied by this Gaussian problem. An unindexed earlier computation remains possible. Search absence alone is not asserted as a proof of uniqueness.

## Value — PASS

The new exact algebraic constant and equality geometry solve the first nontrivial three-coefficient section of a recently highlighted full-space coercivity problem. The degree-one sharp squared constant is only two, so the strict transition at degree two produces a substantive quantitative lower bound on any full-space sharp constant. The extremal anti-alignment and exact quartic certificate make the result useful as a benchmark for Gaussian phase retrieval and any future higher-degree optimization, rather than an arbitrary isolated numerical enumeration.

## Limitations and residual risks

The unrestricted sharp Fock constant and all degree-three-or-higher sharp constants are unknown from this result. An earlier uncatalogued equivalent quartic Gaussian moment inequality could overlap. No independent mathematical audit has taken place; numerical calculations only supplement the symbolic analytical proof.

Self-review: passed. Independent audit: not yet performed.
