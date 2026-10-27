# Scientific review

## Correctness

**PASS (self-review).** The Fock monomial diagonal follows from polar integration. The boundary difference formula is an exact integration-by-parts identity, and the Chebyshev zero bound for finite exponential sums follows by a short induction with Rolle's theorem. Every repeated eigenvalue gives a distinct real zero of the boundary exponential sum, establishing the \(2m\) upper bound. Coercivity yields a degree-\(2m\) monic weighted \(L^1\) minimizer; first variation and the sign-change test prove its \(2m\) distinct positive roots and the half-moment equalities. Exact root counting fixes the negative sign of every subsequent eigenvalue difference. The strict equality case of the triangle inequality proves uniqueness of the half-energy construction. Numeric calculations independently confirm \(m=1,2\), without replacing the proof.

## Originality

**PASS (qualified self-review).** The closest direct geometric analysis, Knutsen (2020), explicitly treats Hermite localization on a single annulus (Section 3.1) and Cantor radial sets (Section 4), but establishes neither the full finite-component multiplicity cutoff nor the unique \(2m\)-fold half-energy construction. The familiar diagonal formula of Daubechies (1988) is inherited. Esmeral García–Maximenko (2025) concern approximation by general radial symbols; Bdarneh (2026) derives radial eigenvalue representations; Svela–Trapasso (2026) address general nonlinear concentration. None of their examined stated results yields this combined geometric bound and attainability classification. Classical exponential-polynomial zero counts and weighted \(L^1\) sign quadrature are antecedents; the new claim is their sharp operator-geometric synthesis. Priority within older sign-quadrature literature remains an explicit risk, as do portions of 2025–26 source text not accessible in full. Absence of a database match is not treated as proof of absolute novelty.

## Value

**PASS (self-review).** The number of physical annular components imposes a sharp, uniform cap on the dimension of a precisely energy-concentrated Hermite eigenspace. The cap is attained at the **largest** eigenvalue for every component count, and the exactly balanced, uniquely specified radial mask makes the result constructive in principle. This resolves a natural inverse design problem for Gaussian short-time Fourier localization, stronger than a numerical eigenvalue-table entry or an unmotivated degree slice.

## Sources, scope and remaining risks

Compared with Daubechies (1988); Knutsen (2020, full open-access article §§2–4); Esmeral García–Maximenko (2025, abstract and abstract-level implications); Svela–Trapasso (2026, open-access HTML sections on concentration and operator structure); Bdarneh (2026, arXiv and representation/abstract material). No claim is made concerning arbitrary nonradial masks, infinitely many annuli, other radial weights, or uniqueness at unspecified spectral levels. Historical-priority certification and independent mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
