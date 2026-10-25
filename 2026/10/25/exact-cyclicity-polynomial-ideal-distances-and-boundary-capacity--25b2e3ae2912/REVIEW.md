# Scientific review: monomial-circle cyclicity and capacity on complex ellipsoids

## Correctness — PASS

The exact coefficient-space normalization comes from Torkinejad Ziarati, Section 4, equation for monomial norms. The proof checks the weighted AM–GM boundary contact, the **full disconnected character subgroup** for noncoprime exponents, the invariant subspace at every total-degree cutoff, weighted Cauchy–Schwarz attainment and the explicit minimizer. The Stirling leading coefficient is obtained with the exponential factors canceled exactly, not inferred from a finite sample. The Haar moment calculation proves a matching lower and upper bound for the **full** set of probability measures on the boundary zeros. Bounded coordinate multipliers promote approximation of \(1\) to cyclicity. The standalone `CHECK.py` passed its Gamma, finite-degree and boundary-geometry consistency checks. The proof does not use those samples for universal conclusions.

## Originality — PASS, subject to normal historical-priority uncertainty

Torkinejad Ziarati's arXiv:2507.03767v2 explicitly leaves the one-dimensional zero-set problem open on ellipsoids but supplies the norm and capacity framework; those premises are prior, not new. Kosiński–Vavitsas (2023) already classifies **unit-ball** one-dimensional boundary zeros and obtains the same critical exponent \(3/2\), so this exponent alone is not new. Vavitsas (2023) already uses diagonal reductions and capacity ideas for **unit-ball** models. The claim here is restricted to genuine nonball ellipsoids \(p>1\), the specified monomial zero-circle family, exact *unrestricted* total-degree polynomial distances and approximation rates, and an equality with the precisely normalized ellipsoid kernel capacity. None of the inspected ball theorems supplies these \(p,a,b,\beta\)-dependent exact ellipsoid invariants. The closest indexed radial-polydisk one-generator approximation result concerns a linear average and a different Hilbert norm, rather than these monomial-circle ellipsoid invariants. Unindexed work or a straightforward unpublished extension of known ball reductions is a genuine priority risk; no exhaustive uniqueness claim is made.

## Value — PASS

The motivating 2025/2026 ellipsoid paper poses the positive-dimensional boundary-zero cyclicity problem. This result gives a natural and nontrivial complete test family, including any number of connected zero circles; beyond the expected critical exponent it gives the **exact optimal error among all multivariate approximants**, the sharp quantitative convergence regimes, the explicit equilibrium measure, and the **exact nonzero capacity** in the noncyclic phase. Those normalization-sensitive numbers cannot be read off from the earlier qualitative ball classification. The result does not purport to settle the general open problem.

## Limits and closest literature

The all-polynomial minimization depends on the full phase symmetry of a single monomial; an arbitrary stable polynomial does not admit that reduction. The precise kernel normalization is essential for the capacity value, and asymptotics are for fixed parameters only. The prior scientific inputs are Torkinejad Ziarati, *Cyclicity in Poletsky-Stessin Weighted Bergman Spaces*, arXiv:2507.03767 (Sections 3.2, 4, 6); Kosiński–Vavitsas, *Cyclic Polynomials in Dirichlet-Type Spaces in the Unit Ball of \(\mathbb C^2\)* (2023, Theorem 3); and Vavitsas, *A Note on Cyclic Vectors in Dirichlet-Type Spaces in the Unit Ball of \(\mathbb C^n\)* (2023, model and capacity sections). The nearby radial-polydisk approximation record was compared by mathematical implication, using its available summary rather than claiming its full text was inspected.

Self-review: passed. Independent audit: not yet performed.
