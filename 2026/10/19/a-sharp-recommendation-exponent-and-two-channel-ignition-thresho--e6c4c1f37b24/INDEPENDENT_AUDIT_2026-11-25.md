# Independent mathematical audit

## correctness

PASS

At the fully inactive state the derivative of each supplying channel is d[−log(1−z d^{α−1})], weighted by d p_d / E d; the active matrix has diagonals B_L(r), off-diagonals B_L(λr), and eigenvalues B_L(r) ± B_L(λr). In RESULT.md line 64, 'their sum' must mean the sum of the two B_L terms, not the sum of the eigenvalues; the stated threshold uses the correct Perron eigenvalue. It grows strictly from zero and exceeds one at the upper endpoint by −log(1−u)>u (or diverges from d=1 if λ=0). Uniformly in L, its linear term at small r is (1+λ)r H_{L,τ−1−α}/H_{L,τ−1} with relative O(r); the harmonic sum gives both sharp vanishing rates and constants. In the convergent case compact uniform convergence and the same strict endpoint gap bracket the positive limit root. At α=0, −d log(1−z/d) decreases strictly with d, yielding the exact cutoff reversal. At r=1/2, the isolated multiplier lies in (1/2,log 2]; increasing leakage therefore gives a unique interior ignition point, with λ_c=2−4/e at L=1. Independent bounded finite differencing reproduced the Jacobian to 6.23e−9 at one point; sample roots at τ=2.5, λ=0.5, α=0 increased from 0.50714609 at L=1 to 0.55845947 at L=64. Frozen code was inspected, not executed. All quantifiers are for the local incidence multiplier of the deterministic map, not nonlinear stability at equality, branching criteria, or eventual cascade size.

## originality

PASS

The primary paper supplies the recurrence and its recommendation modification; its stated threshold is small-appeal and decoupled. The exponent boundary is already suggested by the degree-moment calculation, and spectral coupling is standard. The supported distinct contribution is the exact finite-appeal coupled threshold for this recurrence, especially the strict cutoff reversal absent from the first-order criterion, together with the sharp cutoff rates and physically admissible leakage window. The inspected alternative models and indexed results do not supply this combination or the exact finite-cutoff ordering.

## value

PASS

A researcher applying this published map can misread first-order cutoff independence at complete suppression as an exact fact. The strict reverse cutoff effect and the admissible leakage window answer concrete questions left by that approximation; the sharp regimes delimit when a finite-cutoff threshold extrapolates to a positive limit. The value is confined to analyzing this deterministic mean-field incidence map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
