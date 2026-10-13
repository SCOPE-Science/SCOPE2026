# Scientific review: heterogeneous amplitude-damping allocation in GHZ metrology

## Correctness — PASS

For independent zero-temperature amplitude damping before common-phase encoding, the only phase-sensitive matrix block spans the two extremal computational strings. It has diagonal entries \((1+R)/2,Q/2\) and coherence \(\sqrt Q/2\), giving the exact QFI \(2n^2Q/(1+R+Q)\). At fixed pair sum, direct differentiation of the reciprocal QFI with respect to their product is strictly negative on the interior. Finite pair equalization gives Schur-concavity, strict interior ordering, exact extrema, and both SQL threshold conditions. The monotone uniform-envelope inequality has exactly one root; Taylor expansion with an exponentially small product correction gives the stated asymptotic. An independently constructed density-matrix/eigensystem verifier completed 4,042 checks on the final scientific formulas. Finite tests support but do not replace the analytical result.

## Originality — PASS, with priority uncertainty

The first-public 2026 paper of Farokhi develops noiseless GHZ distributed sensing and QFI directionality; the current fixed-sum noise design is outside its scope. The **complete inhomogeneous amplitude-damped GHZ corner matrix is already contained in** Bugalho et al. (arXiv:2407.21701, Sec. 4.5, Eq. 51). The 2011 paper of Ma et al. already supplies the homogeneous loss-QFI formula and leading shot-noise threshold. Neither is claimed as new. Koczor et al. (2020) optimize probe states numerically against noise and identify benefits of symmetry breaking, but not a fixed-GHZ majorization law over sitewise damping allocations. The result under review is only the strict fixed-sum ordering, exact upper/lower envelope and guarantee/possible/impossible partition. The literature checks did not identify that statement; the 2024 complete matrix formula could nevertheless allow an unindexed implicit derivation, so novelty is not independently certified.

## Value — PASS

A distributed sensor network can experience unequal channel losses even when an aggregate mean-loss statistic is fixed. The theorem gives a global extremal principle and **two sharp operational cutoffs**: under one cutoff an ideal-separable SQL violation is robust to *all* allocation profiles; between cutoffs it depends on channel heterogeneity; above the other no such violation is possible with this GHZ input. A single completely lossy site can erase its common-phase QFI as soon as aggregate damping reaches one, while uniform attenuation remains optimal for the same sum. This distinguishes meaningful physical design regimes, rather than merely tabulating evaluations of a known QFI formula.

## Limits and closest work

The main result assumes an ideal input GHZ state, loss occurring before encoding, independent amplitude-damping channels, fixed \(J_z\), an exact sum of decay probabilities, and comparison against an *ideal* rather than realistically noisy separable benchmark. The earlier homogeneous large-system threshold is explicitly prior work. No assertion is made about optimally redesigned probes, partially monitored environments, or frequency estimation with noise acting during encoding. Related prior papers are Farokhi (2026), Bugalho et al. (2024/2025), Ma et al. (2011), and Koczor et al. (2020). Earlier implicit treatment of heterogeneous fixed-budget extrema remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
