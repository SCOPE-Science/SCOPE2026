# Review

## Correctness
PASS. The proof reconstructs both procedures from their published definitions. The leave-one-out endpoint identities are exact, the candidate residual comparison is reduced by an explicit factorization, and the integer quantile identities align the two endpoint orders. The accompanying exact-arithmetic verifier checks the original residual inequalities directly on all cells induced by the algebraic breakpoints for multiple rational samples, including the low-\(\alpha\) convention.

## Originality
PASS. The closest primary source is Barber et al., arXiv:1905.02928 / DOI:10.1214/20-AOS1965, because it defines both methods. Its inspected full text treats them separately, assigns different generic guarantees, and contains no sample-mean, intercept, or location specialization. Searches for exact equivalence, sample-mean, location-model, and linear-regression formulations did not reveal a covering finite-sample theorem. A later preprint, arXiv:2508.05272, discusses asymptotic equivalence under stability rather than deterministic finite-sample equality. Residual risk remains that an unindexed specialized note or folklore derivation contains the same identity.

## Value
PASS. The source presents full conformal as having the stronger \(1-\alpha\) guarantee but usually much greater computational cost than jackknife+. The sample-mean model is a canonical and non-artificial location problem. Here the distinction disappears exactly: jackknife+ has the same prediction set and hence the full-conformal guarantee, with an exact coverage grid under no ties. The common-center interval-depth mechanism gives a structural explanation that may guide searches for other exact-coincidence classes.

## Closest literature and limitations
The result is confined to intercept-only least squares with absolute residuals and the source quantile convention. It does not establish equality for general linear or nonlinear regression, and the exact grid coverage requires distinct augmented residuals. Exchangeability yields only marginal coverage. The most relevant literature is Barber et al. (2021), Lei et al. (2018), and the later asymptotic relationship in arXiv:2508.05272.

Same-model review: passed. Independent audit: not yet performed.
