# Self-review

## Correctness — PASS

The four families of orthogonal Laplacian spectral subspaces, including their dimensions, were reconstructed directly from the adjacency rule. This yields the hub-to-leaf entry \(12h/d(nh)\), positive cross-petal entries, and a rational formula for within-petal entries with numerator \(12hP_{n,k}(h)\). The coefficient identity \(kn+k-n^2+n+1=-[1+j(k+3)+j^2]\) at \(n=k+2+j\) proves exactly one positive quartic zero by Descartes' rule and endpoint signs. Since each denominator is positive, the smallest such root gives the full nonreentrant interval. Positive definiteness of the rational spectral filter settles all diagonals. An independently assembled exact Laplacian-matrix verifier tests the critical symbolic identities and 2,322 rational off-diagonal entries on 23 graphs. No infinite assertion rests on enumeration.

## Originality — PASS with documented residual risk

The closest method-specific primary paper is Zappavigna et al. (2010), which treats sufficient diagonal-Padé preservation conditions for Hurwitz Metzler systems and examples of failures, not an exact endpoint threshold for conservative heterogeneous clique sums. Gottlieb–Shu–Tadmor (2001) gives general SSP limitations; Blanes–Iserles–Macnamara (2022) develops different positivity-preserving integrators and explicitly discusses Padé positivity as an ongoing challenge. Spectral windmill literature is not a timestep-sign theorem. Exact published mathematical-record searches and nearby available results on explicit RK4, Gauss integration on multipartite graphs, and special finite networks were compared by implication. None of the inspected claims determines the within-petal quartic positivity horizon on nonstar clique sums. Full specialized coverage remains a residual literature risk; search absence alone was not treated as proof of uniqueness.

## Value — PASS

The result gives an exact decision procedure and sharp positivity horizon for *all* heterogeneous clique bouquets, a natural hub-and-community diffusion family; its threshold is explicitly computable from a small number of fixed-degree polynomials regardless of graph size. It reveals an unexpected qualitative distinction: stars alone enjoy unconditional positivity, one added edge can remove it, and the first failing petal can be intermediate in size. The graph-specific resolution of the spectral-stability/positivity gap is a motivated result rather than a routine substitution, and no more general downstream theorem is claimed.

## Limitations

The theorem applies to finite simple unweighted one-hub clique sums and completed two-stage Gauss–Legendre endpoints, not weighted block graphs or internal stages. Formula identities were verified symbolically and on selected exact matrices; the unrestricted claim has a separate analytical proof. Literature coverage is finite and cannot certify global novelty. Independent mathematical review is outstanding.

Self-review: passed. Independent audit: not yet performed.
