# Independent mathematical audit

## correctness

PASS

Uniform priorities induce a uniform relative order on the residual allowed edges after each accepted edge. For a,b marked vertices on the two sides at stage k, put A=(k-a)(k-b), B=k² and write e=e_out+d with d counting forbidden edges touching the marks. The avoidance ratio against A/B differs from one by [A d-(B-A)e_out]/[A(B-e)]; here d≤Δ(a+b), e_out≤Δk, and B-A=O(k). Thus it is 1+O(k^-2), uniformly in the residual state for large k. Iterating uniform conditional bounds gives the product of the two falling-factorial ratios with relative O(1/K). For a marked forbidden edge the single-deletion baseline is (k-1)/(k+1), itself within relative O(k^-2) of the complete-host avoidance probability. The product to K is K(K+1)/[n(n+1)], times 1+O(1/K); if the tag is alone at K, the remaining product is exactly 2/[K(K+1)]. Given its survival to K, another residual forbidden edge has chance O_Δ(K/n+mK²/n²), by the three- and four-vertex bounds. Even then final tagged survival is O_Δ(K^-2) by survival to a fixed stage above Δ. With K of order n^(1/3) this gives the asserted uniform per-edge estimate. A jam with k≥2 requires a forbidden K_{k,k} with k≤Δ. There are O_Δ(n) copies for each k, by first fixing one left vertex and using bounded neighborhoods and common neighbors. Each copy's vertices survive to a fixed stage with chance O_Δ(n^-2k), so summing overcounts the failure probability by O_Δ(n^-3), absorbable even for m=1. The empty case, limiting constant and Hall bound also follow. Frozen VERIFICATION.md and verify.py were inspected, not run. The 31 recorded checks include exact one-edge and order-enumeration checks; the arrangement examples just calculate finite probabilities and do not test a uniform asymptotic bound.

## originality

PASS

The supported distinction is the relative rare-failure asymptotic for arbitrary degree-bounded forbidden bipartite graphs, including adjacent deletions and m=O(1). Neither matching-only recurrences nor inspected general greedy results imply this scope. The one-deletion and matching special cases are not credited as new; historical priority is qualified by unavailable primary passages and unspecified predecessor records.

## value

PASS

The operationally meaningful question is failure despite existence of a perfect matching, including for only one or a few omitted edges. The result gives the leading coefficient with uniform relative accuracy across patterns, not just an expected unmatched fraction on a symmetric host. Controlling surviving tagged defects and terminal bicliques is a substantive reason the leading coefficient is arrangement-independent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
