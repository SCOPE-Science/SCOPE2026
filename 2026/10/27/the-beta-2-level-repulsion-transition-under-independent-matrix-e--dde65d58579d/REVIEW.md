# Review: independent-clock two-site spectral repulsion

## Correctness

PASS. Exact gamma and Gaussian conditional entry laws at fixed reset ages give an independently checkable formula for the spectral gap. Continuity of the diagonal-difference density at zero, the finite-negative-moment threshold at \(\beta=2\), and a polar Jacobian establish all three asymptotic constants with the stated hypotheses. The shared second moment follows from the same entry marginals in both protocols. The accompanying script passed 97 assertion groups, including mixture quadratures, complete two-site spectral-density integrals, and Monte Carlo cross-checks. Numerical checks corroborate rather than replace proof.

## Originality

PASS with priority limitations. Akemann, Majumdar and Päßler, arXiv:2605.26945v1, provide the matrix process and independent-entry stationary law; those are prior. Biroli, Majumdar and Schehr, arXiv:2503.14733v1, explicitly prove the simultaneous-clock two-particle exponent \(\min\{\beta,1\}\) and logarithm at \(\beta=1\); that contribution is not claimed here. The new statement concerns the **independent-clock** exponent \(\min\{\beta,2\}\), its sharp constants and the contrasting equality of second moments. A broader theorem might imply the resulting singular small-ball scaling; absence from targeted sources does not prove universal priority.

## Value

PASS. The gap exponent is a physically motivated random-matrix statistic: it is sensitive to clock independence even though the one-entry marginals and the exact mean-square spectral separation coincide. The integer-threshold transition and logarithmic boundary give a complete all-\(\beta\) characterization in the smallest nontrivial tridiagonal matrix, not an isolated numerical case.

## Limitations

The result is stationary and two-dimensional, assumes independent identical-rate Poisson clocks and specific OU/CIR entry laws, and does not classify large matrix dimensions. The complete common-reset gap law and all stationary entry marginals are established prior results. Independent mathematical and publication-priority review remain pending.

Self-review: passed. Independent audit: not yet performed.
