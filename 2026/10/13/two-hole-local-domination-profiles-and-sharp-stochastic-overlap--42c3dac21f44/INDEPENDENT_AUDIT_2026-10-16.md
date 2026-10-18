# Independent mathematical audit

## correctness

PASS

For finite connected G, n≥5, designated v with degree n−3 and two nonneighbors u,w, put R=N(v), k=|N(u)∩R|, ell=|N(w)∩R|, t=|N(u)∩N(w)∩R|, e=1_{uw edge}, a=k+e+1,b=ell+e+1,c=2+k+ell−t. Any dominating set containing v must meet both closed neighborhoods A=N[u], B=N[w]. Inclusion–exclusion yields D_v=z[(1+z)^(n−1)−(1+z)^(n−1−a)−(1+z)^(n−1−b)+(1+z)^(n−1−c)], with no dependence on internal edges of R. Feasible t range max(0,k+ell−(n−3))≤t≤min(k,ell), with stated connectedness conditions. For fixed a,b and adjacent c,c+1, h_c−h_(c+1)=z(1+z)^(n−2−c), whose normalized law is one selected vertex plus outside fair coins; h_(c+1) has that outside portion plus a strictly stochastically larger count of inside selections. Convex mixture proves strict first-order dominance as t decreases. Differentiation gives exact mean (n+1)/2+[a2^-a+b2^-b−c2^-c]/[2(1−2^-a−2^-b+2^-c)], and monotonicity c→a+b yields sharp degree-sum upper bound (n+1)/2+a/[2(2^a−1)]+b/[2(2^b−1)], equality exactly e=t=0. Minimum support count is t+2e at size 2, otherwise ab at size 3. Independent direct domination bitmask enumeration checked 1,088 n5/n6 graphs, plus 896 connected parameter profiles and 420 strict adjacent overlap comparisons with exact rational tail calculations. These checks corroborate universal inclusion-exclusion/coupling proof.

## originality

PASS

Chen–He March 2026 DOI 10.12677/aam.2026.153090 proves degree n−2 one-hole local mean and explicitly proposes two nonneighbors/degree n−3 as the next case. Their October 2026 preprint arXiv2610.11446 gives a broad degree-sum upper bound and one-hole formula; its general bound is clearly prior and not claimed new. It neither determines the two-hole full conditional polynomial, strict stochastic order across overlap, nor equality characterization. Other graph-family domination-polynomial findings concern special classes or unconditioned counts. Best-of-knowledge PASS with indexing and elementary inclusion-exclusion proximity risks.

## value

PASS

The directly motivating March article identifies this exact natural degree-defect-two case as open. The finding solves its local-mean question uniformly for every connected such graph, determines every conditioned cardinality coefficient, and proves a strict parameter-comparative stochastic order and sharp attainable extrema plus equality boundary for a known general upper bound. This is a structural family theorem, not an arbitrary finite census nor simply restating a general numerical inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
