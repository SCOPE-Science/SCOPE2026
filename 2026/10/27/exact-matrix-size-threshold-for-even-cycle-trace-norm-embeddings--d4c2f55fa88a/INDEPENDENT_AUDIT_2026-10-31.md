# Independent mathematical audit

## correctness

PASS

For k>=2, the trace-norm triangle inequality followed by Minkowski gives R_{k,d}(f)<=k*sqrt(3/2). Equality makes every cyclic edge norm the same positive c and every k-edge arc trace-norm geodesic; hence every shorter arc is geodesic, giving an isometric cycle embedding after scaling. For any norming contraction H of one half-cycle, polar duality makes H*A_i=|A_i| and -H*A_{k+i}=|A_{k+i}| on each right support. A separate norming contraction for arcs containing A_i and A_{k+j} when i!=j forces their right supports orthogonal. The positive sums of B_i and C_i agree, so Tr(B_i C_i)>=Tr(B_i^2)>0, while off-diagonal B_i/C_j pairings vanish. Choosing nonzero pairings gives a k-by-k diagonal rank-k matrix in C^d, forcing d>=k. Diagonal +/- E_ii cycles realize d=k (then any larger d); compactness of normalized finite-dimensional maps makes the below-threshold upper bound strict. Independent exact diagonal L1 distances checked all pairs k=2..17 (7,136 checks).

## originality

PASS

The tested equality-dimension theorem concerns arbitrary nonlinear maps into M_d(C) with nuclear norm, not merely dimension-free metric cotype bounds nor binary-coordinate host embeddings. Jiao–Luo–Wu 2026 gives a scale-optimal but numerically much weaker general bound for Schatten 1 without this finite-matrix saturation classification. Rigobert–Laurent restrict to Abelian Cayley hosts; a noncommutative Schatten embedding need not respect that host restriction. Resultary closest Schatten-4 Hilbertian dimension is a different norm and object. Jiao–Luo–Wu full paper was inaccessible via arXiv/OA/Oxford, so best-of-knowledge PASS retains this direct-source risk.

## value

PASS

Minimum complex matrix dimension of an exact geodesic C_{2k} realization in trace norm is a natural finite-dimensional nonlinear-geometry threshold. The polar-support obstruction is structural, works beyond commuting Hermitian models, and determines equality in a familiar metric-cotype ratio.

The dated certificate retains the supplied scientific assessment, sources and limitations.
