# Scientific review: sharp ternary affine point–hyperplane refinement

## Correctness — PASS

The general proof identifies coordinate-zero hyperplanes in the first round, then the \(1+2d+\binom d2\) point witnesses by round two, then all hyperplanes at round three and all points at round four. It explicitly handles the projective scaling of homogeneous normal vectors. A three-point collision is proved at round two and persists through round three because of the bipartite synchronous update. Every marking set of at most \(d\) points has a nontrivial affine stabilizer, establishing the optimal marking number \(d+1\). The direct finite checker covers dimensions 2–6, and the separate incidence-signature checker covers 2–9. These computations corroborate, but do not replace, the unrestricted proof.

## Originality — PASS (priority provisional)

The 2015 graph-class colour-refinement paper (arXiv:1502.01255) and the 2016 individualization-complexity paper (arXiv:1606.04383) provide the framework, but the inspected portions and specific full-text searches do not supply the claimed dimension-independent ternary affine formula. A preceding result for two-dimensional affine *point–line* incidence is narrower and does not, by its statement, imply the higher-dimensional *point–hyperplane* bound or its sharp round count. Research-index queries returned nearby geometric and combinatorial claims with different invariants. Priority against unlocated specialized coherent-configuration literature is unresolved.

## Value — PASS

There is a natural exact question: how many separately marked points, and how many local counting rounds, are needed to make the standard ternary affine point–hyperplane incidence graph discrete? This result gives both answers sharply in every dimension \(d\ge3\). The recovered quadratic-size signed-pair witness family separates an exponential hyperplane set and explains the dimension-free depth. It is not solely a computation at a small rank and does not claim unrelated general identification properties.

## Closest literature and limitations

References: Arvind et al., arXiv:1502.01255 (2015), and Arvind et al., arXiv:1606.04383 (2016); the dimensional-two affine-plane predecessor supplies context, not a higher-rank proof. The theorem excludes other fields and arbitrary dependent marked-point sets. Specialist earlier coverage may exist; independent scientific and publication-priority evaluation remains pending.

Self-review: passed. Independent audit: not yet performed.
