# Scientific review: exact-degree sampling on simplex-edge midpoints

## Correctness — PASS

The theorem covers integer dimensions \(n\ge5\) and every exact harmonic degree \(k\ge0\). The centered coordinate normalization, two inner products, Johnson adjacency eigenvalues and Gegenbauer addition theorem together give the full three-sector Gram spectrum. Degrees \(0\)–\(2\) are direct calculations; the displayed degree-three, degree-four and degree-five rational eigenvalue factorizations yield the exceptional rank deficiencies. The standalone standard-library checker constructs 54 exact integer numerator polynomials for degrees \(3\)–\(20\), uses the rational-root theorem to exhaust all permitted integer dimensions, and establishes the three claimed exceptional zeros. This is finite *symbolic* exhaustive algebra, not an inference from sampling dimensions. Independently, for all degrees \(k\ge21\), the conic-restriction/Wronskian proof establishes full rank with no computational extrapolation. The complexification and connectivity arguments exclude every real annihilating weight vector. The low-degree symbolic formulas were separately cross-checked against the Gegenbauer definitions in 80 exact dimension-degree combinations.

## Originality — PASS under bounded source comparison

Musin (arXiv:0801.3706, Sections 1–2) treats the very same simplex edge-midpoint two-distance orbit and a degree-at-most-two polynomial dimension bound; his theorem does not imply the all-degree exact harmonic row ranks. Bannai–Okuda–Tagami (arXiv:1308.5101, Sections 1–4) develop the harmonic-index framework and Fisher bounds, not the ranks of the Johnson-orbit evaluation map. Barg–Glazyrin–Okoudjou–Yu (arXiv:1402.3521, Introduction and main statements) establish two-distance tight-frame structural results, not these higher-degree ranks. Zhu et al. (arXiv:1507.05373, Sections 2–7) classify especially tight even-index designs rather than the all-degree spectrum of this orbit. Misawa–Munemasa–Sawa (arXiv:2410.09471, Sections 1–5) concern simultaneous consecutive odd harmonic indices, not the single-degree \(n=16,k=5\) cancellation and exact ranks. The \(n=8\) special case is already encompassed by the antipodal Gosset/equiangular-line sampling case and is not independently claimed as novel. The new contribution assessed here is the **uniform infinite-family classification**, including the \(n=16\) quintic defect and absence of any further rank defects in degrees six and above. Residual risk: an equivalent specialized calculation may be present in older Johnson association-scheme, cubature, or spherical design tables not fully indexed or retrieved. Database nonhits are not proof of novelty.

## Mathematical value — PASS

The edge-midpoint hypersimplex is a canonical extremal two-distance configuration. Exact-degree harmonic interpolation is a natural spectral sampling invariant, and classifying all harmonic-index cancellations matters for cubature and discrete spherical transforms. The \(n=16\) family member gives a non-antipodal fifth-harmonic design with an exact one-dimensional defect; the \(n=8\) cubic and quartic irregularities provide instructive boundary cases, while all larger degrees are uniformly surjective. The theorem gives a complete all-degree classification for an infinite natural family rather than a tiny numerical improvement or arbitrary finite slice.

## Limitations

No independent mathematical audit or validation has been performed. The proof does not address other hypersimplex levels or optimal conditioning of nonzero singular values. Priority remains conditional on the bounded literature comparison described above.

Self-review: passed. Independent audit: not yet performed.
