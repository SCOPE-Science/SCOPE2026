# Independent mathematical audit

## correctness

PASS

In assigned RESULT.md blob 09d7ca37deed657b15d6275d04a6dc0761364dec, for m≥2 and n=m+1, the positive N_m-unit polytope P={r≥0:∑_{j≠q}r_j≤1 each q} has exactly nonzero vertices e_1,…,e_n and v=(1/m,…,1/m). If a zero coordinate exists, the corresponding supporting face is simplex; if all positive, the n independent sum-excluding-q constraints must be active, giving v. Independently enumerated n=3,4,5,6 vertices using exact SymPy rational linear algebra, matching n+2 including zero; the general proof is symbolic. Any k≤m positive vertices share a facet F_q, picking q absent among their coordinate e_i labels. For each slice functional, maximize its coordinate-dual norm at a positive vertex. The established full P3 of c0 permits coordinatewise sphere choices compatible with the weighted convex slices, and the common facet gives norm one of the average. Thus Z_m=(⊕c0)_{N_m} has P3^(m). Conversely taking n coordinate-norm slices S_i with α<m^−2 gives off-i norms <α and uniform average norm≤m(1+mα)/(m+1)<1; hence fails P3^(m+1). Every integer m≥2, real spaces, finite convex combinations of unit-ball slices; P2 and optimal obstruction radius are not proved. Finite vertex checks corroborate only small n, not the infinite theorem.

## originality

PASS

PASS on best-of-knowledge bounded comparison: the recent Haller arXiv:2608.11827 preprint explicitly provides the m=2 three-fold c0-sum construction and finite-arity terminology; the submitted exact all-m consecutive separation requires an arbitrary-dimensional new vertex/facet and slice-lifting argument. Full Haller source was unavailable after arXiv/OA search and authorized institutional attempt returned vpn_disconnected, so an all-m theorem in an unread section remains a priority risk.

## value

PASS

Finite-arity sphere-intersection is a natural test complexity question arising immediately from Haller's m=2 example. An explicit strict separation for EVERY consecutive m,m+1, with the natural all-but-one polyhedral absolute sum and a quantitative obstruction, is a motivated complete hierarchy theorem. Its mathematical value is independent of a paper-sized generalization or P2 hierarchy solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
