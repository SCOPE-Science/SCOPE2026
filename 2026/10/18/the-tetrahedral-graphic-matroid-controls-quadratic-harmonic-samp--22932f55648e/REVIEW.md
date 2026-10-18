# Scientific review: The tetrahedral graphic matroid controls quadratic-harmonic sampling on the cuboctahedron

## Correctness — PASS
The nine polynomial evaluation columns are a basis of degree-at-most-two spherical harmonics on the sphere after harmless column scalings. Parity and coordinate-plane comparisons prove the full twelve-point evaluation matrix has rank nine. The displayed three-dimensional Gale kernel has direct integer entries, annihilates all nine columns, and is a full left-kernel basis. The six antipodal pairs become six tetrahedral edge differences. Standard graph-incidence rank and rank-nullity prove the formula for **every** erasure pattern. The standalone rational checker independently reproduced all 4096 cases and exact counts, using the actual source file.

## Originality — PASS, with residual risks
The primary comparators were Womersley–Sloan on spherical interpolation, Keiner–Kunis–Potts on full-rank conditions for spherical Fourier matrices, Rupright on gridded harmonic regression, and Ahrens–Beylkin on symmetry-adapted spherical quadratures. Those sources supply the general evaluation framework but not the exact cuboctahedral graph-incidence rank rule. Targeted published-result queries examined aliases involving root-system coordinates, the Gale transform, erasures, tetrahedral edges, and full spherical-harmonic bandlimits. Related published computations on other polyhedra and cuboctahedral topological complexes do not entail the claim. An unidentified equivalent statement may exist under graph-matroid or root-system terminology. A more recent cubed-sphere interpolation source was available only at abstract and grid-definition level through the attempted routes; its grid cardinalities rule out identical node sets, but its full text was not read.

## Mathematical value — PASS
The theorem resolves the exact reconstruction rank for *every* deletion of a canonical symmetric twelve-node grid, with an unexpectedly elementary K4 connectivity certificate. It provides a complete natural sampling classification and a closed generating polynomial, not simply another numerical rank table. The 128 successful and 92 unsuccessful three-erasure patterns (and their exact graphical obstruction) identify the sharp erasure tolerance in noiseless quadrupole sampling.

## Limitations and supporting materials
The claim is restricted to the cubic/octahedral twelve-node orbit and harmonic degrees at most two, and says nothing about stability under noisy measurements or higher-degree bands. The full arithmetic assertions and program invocation are in RESULT.md, VERIFICATION.md and verify_cuboctahedral_erasure.py. General interpolation results are not being advertised as new, and external novelty verification remains desirable.

Self-review: passed. Independent audit: not yet performed.
