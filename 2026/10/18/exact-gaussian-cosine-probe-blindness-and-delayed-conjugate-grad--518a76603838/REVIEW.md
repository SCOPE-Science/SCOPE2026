# Scientific review

## Correctness — PASS

The beta law follows from independent orthogonal Gaussian chi-square energies, including both inverse-CDF branches. The sparse-rank phase statement follows from beta concentration and a rationalized cosine expression, with separate finite/large probe-degree regimes. The universal Gaussian expectation bound is independent of the number of probes. For the Chebyshev nodes, positive inverse-eigenvalue-weighted Lobatto masses make the Chebyshev error polynomial energy-orthogonal to every allowed CG variation, proving the exact finite-step ratio. Direct high-precision orthogonality and CG checks (938 total verification checks) support the analytic proof. Scope is exact arithmetic and specially chosen SPD diagonal matrices/RHS.

## Originality — PASS

The closest source, Osborne et al. (2026, arXiv:2605.13343v1), defines the same flattened cosine objective, analyzes its geometric scale invariance, and specifies Gaussian probes with two Jacobi sweeps; its full inspected manuscript does not state this exact beta CDF, the sparse-spectrum visibility transition or the uniform-in-batch CG counterexample. Yang et al. (2025, arXiv:2510.27517v1) address SAI losses rather than this full quantitative conjunction. Classical Kantorovich angular maxima, beta ratios, and Chebyshev CG extremality are prior work; combining them with the actual Gaussian training objective, probe count, and smoothing to obtain the specified separation is the assessed claim. Closely indexed CG, Gaussian-section, and preconditioning findings had distinct objectives. Remaining risk: equivalent results could exist under other terminology; uniqueness cannot be certified by database partition or negative searches.

## Value — PASS

The global probe loss is presented as a numerical preconditioner-quality indicator; identifying its exact blindness scale and proving that its apparent alignment can coexist with arbitrarily many ineffective CG steps addresses a material diagnostic-design gap. The failure persists even if arbitrary additional Gaussian probes are flattened into the same cosine, and the stated Jacobi smoothing does not alter the example. The beta CDF also gives finite-size quantitative interpretation of probe scores.

## Closest literature and limitations

Osborne et al., arXiv:2605.13343v1, §6 and supplementary §3; Yang et al., arXiv:2510.27517v1, objective comparison; classical Gaussian-beta/Kantorovich and Chebyshev-CG theory. Limits: real Gaussian probes, fixed diagonal SPD operators, the one-global-cosine functional, identity preconditioning, exact arithmetic, and adversarial RHS. This is **not** a finding that any learned model produces a bad preconditioner or that typical physical solves are slow. Independent review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
