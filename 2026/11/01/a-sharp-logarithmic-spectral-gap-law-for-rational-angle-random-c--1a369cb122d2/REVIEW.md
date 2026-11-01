# Self-review

## Correctness — PASS

The four original branch maps and their piecewise probabilities produce a connected reversible \(n\)-state Markov graph with stationary weights proportional to \(\sin((j+1/2)\pi/n)\). Direct trigonometric substitution gives all edge conductances, including the two bridges and two leaves, with no omitted edge. An effective-resistance computation gives two parallel arms, each \((4n^2/\pi^2)\log n+O(n^2)\). The weighted same-parity Poincaré estimate is \(O(n^2)\), strictly smaller than the bottleneck scale; trial potentials and eigenfunction concentration furnish matching Rayleigh bounds \(1-\lambda_2\sim2\pi^2/(n^2\log n)\). Laziness halves the gap. The actual packaged checker compares independent kernel constructions, stationary balance and several eigenvalues. Finite spectra corroborate but do not prove the asymptotic.

## Originality — PASS on inspected evidence

Feres (2007) explicitly constructs the triangular angular map and finite rational dihedral orbits, while Vales and Pinto-de-Carvalho (2020) establish the circular-billiard formulation and qualitative rational/irrational mixing properties. Neither inspected text supplies the present sharp finite-class spectral-gap rate or its leading constant. Vales (2022) covers the same angular law on constant-curvature surfaces with qualitative mixing statements, not quantitative rational spectral gaps. Feres--Zhang (2012) and Chumley et al. (2020) address spectral estimates for geometrically different random scattering laws; their conclusions do not logically imply this particular two-parity, endpoint-resistance asymptotic. Semantic mathematical-record searches for the exact model, parity/graph reduction, logarithmic gap and equivalent terms returned no dominating mathematical claim. Residual risk: additional priority literature could contain a disguised electrical-network formula or the same spectral scaling. Failed searches do not establish global novelty.

## Mathematical value — PASS

The random circular billiard has an intrinsic rational-angle finite class, whose slowest relaxation rate is quantitatively meaningful even though the overall rational-angle process cannot mix across distinct classes. The result demonstrates an anomalous logarithmic slowdown caused by sparse coupling of the two angle-parity strands at grazing reflection angles, identifies its precise leading coefficient, and separates it from ordinary smooth Legendre diffusion approximations. The theorem provides a natural measurable obstruction and benchmark for quantitative random-billiard mixing, not an arbitrary finite-table recomputation.

## Limitations

Only the specified finite angle orbit is treated. The original Feres reflection law is older than the 2020 circular embedding; the new contribution is the logarithmic spectral asymptotic, not the map. Aperiodicity for the unmodified operator fails at even \(n\), so an always-ergodic relaxation statement uses the lazy operator. No full-space or independent validation is asserted. Comprehensive priority review remains open.

Self-review: passed. Independent audit: not yet performed.
