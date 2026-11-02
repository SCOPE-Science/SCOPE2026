# Scientific review

## Correctness

**PASS.** The problem fixes a simple torus, edge-specific nonnegative conductances, two positive directional prices, and a single linear budget. Strict log-determinant concavity with an injective graph-Laplacian weight map gives uniqueness without assuming symmetry; symmetry reduces the optimum to two positive parameters. The exact Fourier product, monotonic finite price equation, and cyclic resolvent are reconstructed. Uniform local expansions of the cyclic resolvent and periodic quadrature prove the integral crossover and its first correction; the formula for the correction has the correct sign. The standard-library verifier completed 124 independent finite checks, including integer matrix-tree cofactors. Numerical convergence alone is not used to prove the asymptotic theorem.

## Originality

**PASS on inspected evidence, with specialist priority risk.** Tzeng--Wu (2000) already prove the anisotropic toroidal spanning-tree product; Izmailian--Kenna (2015) already derive finite-size free energies; Khosoussi et al. (2016) supply general determinant network-design machinery. None of the inspected relevant statements gives the unrestricted unequal-price optimum or the \(Q=\kappa n\) integral crossover with its explicit first finite-size correction. Closest related results for effective-resistance optimization on square tori and spanning-tree optimization on fixed-width prisms have distinct objectives or graph sequences, so neither implies the new singular square-torus result. A specialized source with an equivalent hidden price-dependent limit may exist; this literature check does not establish absolute priority.

## Mathematical value

**PASS.** Price-driven loss of one coordinate direction is a natural network-design singularity. The result resolves finite-volume optimal allocation and a noncommuting thermodynamic/high-price limit, including a genuine crossover from inverse-first-power to inverse-second-power conductance ratios and an explicit positive first correction. This is a structural limiting law rather than just a determinant recomputation or a special numerical instance. It is specific to square tori and two directional prices.

Self-review: passed. Independent audit: not yet performed.
