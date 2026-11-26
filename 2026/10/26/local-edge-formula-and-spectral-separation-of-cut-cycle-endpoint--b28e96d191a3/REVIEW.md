# Independent mathematical audit

## correctness

PASS

Strong regularity and (n−d−1)μ=dm imply (dI−A)[(d−λ+μ)I+A]=μ(nI−J). Applied to the mean-zero edge dipole, this gives the unique mean-zero potential with levels 0, ±1/(μn), ±(m+μ)/(μn). Summing the four level-cut sizes with weights 1, 1, m+μ−1, m+μ−1 (before division by μn) gives the per-edge formula: each of the two wider cuts has size d(m+1)−2m−2 times the number of internal exclusive-neighbor edges on that side, and each singleton cut has size d. The diagonal is 2(m+μ)/(μn) and lies in [0,1], so taking the complementary projector adds the stated constant to every column sum; symmetry gives the row sums. Rook and Shrikhande have respectively 6 and 4 for τ_e on every edge, giving the exact four norms and gap 1/8. The shared parameters give the two nontrivial adjacency eigenvalues ±2 with multiplicities 6 and 9 by the trace. Independent incidence-SVD checks in both examples and K₃,₃ corroborate 105 columns (replay: python3 /workspace/evidence/review_checks.py 3); the exact general argument, not that finite check, establishes the result.

## originality

PASS

The supported contribution is the general strongly regular column formula and its exact cospectral separation; the projection framework, resistance diagonal identities, local graph shapes, and known special-family values are not independent novelty claims.

## value

PASS

A local combinatorial invariant determines each column's endpoint amplification and hence the worst edge for two natural projections. The exact cospectral separation demonstrates that spectral data and common edge resistance miss this information, rather than merely tabulating examples or asserting optimality of the canonical projectors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
