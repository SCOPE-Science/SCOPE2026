# Scientific review

## Correctness
**PASS.** The affine chart at each hypersimplex vertex is proved to be the rank-one determinantal semigroup ring by an explicit integral transportation decomposition. The two rational box-slice normal fans are obtained by greedy maximization, and every new vertex has primitive coordinate normals forming a lattice basis; thus both sources are smooth and projective. No new rays implies no exceptional divisors. Comparing the local fan subdivisions with the row-line and column-line incidence resolutions gives the exact exceptional fibers. The single toric ray relation gives the Gorenstein threshold, and the strong smallness inequality follows from the smaller fiber dimension. The package's exact-arithmetic checker exhausts all cases through \(n=9\); its finite output is supplementary, not a proof for all parameters.

## Originality
**PASS, with stated risk.** The closest prior work includes Cox--Little--Schenck's toric resolutions, Jojić's shelling/h-vector theory for dual hypersimplices, and Wang--Yu's exact intersection-cohomology calculations. Those results are acknowledged: this contribution is neither the general existence of toric resolutions nor the already computed toric \(h\)-vector. Full-text comparisons to Jojić and Wang--Yu did not show the simultaneous explicit upper/lower **projective smooth fan refinements**, their local exceptional fiber identification, or their exact crepancy/perverse-small thresholds. Search coverage cannot exclude unindexed equivalent coherent refinements.

## Value
**PASS.** The uniform matroid hypersimplex is a natural projective toric variety in the Grassmannian. The result constructs two global smooth birational models with exceptionally small geometry, exhibiting two complementary projective-space fibers at each singularity and identifying the precise crepant boundary. This geometry goes beyond a textbook local rank-one cone, a known Betti count, or a numerical finite census.

## Closest literature and limitations
Jojić (2007, DOI: 10.2298/PIM0795085J) already determines the dual-hypersimplex toric \(h\)-vector via shellings. Wang--Yu (2017, arXiv:1707.04581) already determines corresponding IH and Chow ranks. Cox--Little--Schenck (2011, DOI: 10.1090/gsm/124) provides the general projective toric fan and resolution theorems. The local determinantal incidence resolution is standard. No assertion is made for nonuniform matroid varieties, uniqueness of resolutions, or independent validation. Residual originality risk remains for unindexed equivalent projective subdivisions.

Self-review: passed. Independent audit: not yet performed.
