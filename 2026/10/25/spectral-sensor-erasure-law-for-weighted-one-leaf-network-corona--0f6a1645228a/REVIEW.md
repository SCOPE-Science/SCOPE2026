# Independent mathematical audit

## correctness

PASS

C: Orthogonal spectral decomposition reduces the 2n Laplacian to the 2x2 symmetric block [[alpha+s,-s],[-s,s]] over each core E_alpha. Its lambda_-<s and lambda_+>=2s are strictly ordered, with disjoint lower/upper spectral ranges, so the PBH test can sum nullity across lifted eigenspaces with multiplicities unchanged. Lower output factor 1+beta rho_- is strictly positive; upper factor vanishes exactly at b_s(alpha), giving the exact rank formula and full-state criterion. For nonnegative gains β=1 kills the upper constant mode at alpha=0. At most one erasure among all pairwise distinct β_i, and connectedness with positive existing edge weight rules out an eigenvector supported on one vertex, proving universal all-modules recovery. Independent exact SymPy rank tests on three-path core s=2 gave ranks 5 for gains (1,1,1) and (2,2,2), rank 6 for (1/2,1/2,1/2) and (1,2,3). The statement excludes heterogeneous s and noisy conditioning.

## originality

PASS

O: Classical PBH and corona spectral lifting are prerequisites; prior path/cycle point-state observability and composite-graph single-input controllability involve different measurement matrices. The core-dependent exact gain erasure rank identity (not merely a sufficient generic leader rule) is not stated in the inspected close literature. Other literature on local aggregate sensors and graph-corona spectral decompositions remains an identifiable specialty risk.

## value

PASS

V: In network observability design the issue of resonance-induced loss despite measuring all modules is physically meaningful; the gain formula gives exact necessary and sufficient test and an all-graph sufficient heterogeneity rule. The correct count of unobservable *dimension* with repeated eigenspaces, not merely binary observable/unobservable, is a reusable structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
