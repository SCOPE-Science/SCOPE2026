# Self-review: hypercube geodesic distance shells

## Correctness — PASS

For a length-\(k\) geodesic in the binary cube, coordinate permutation and binary translation reduce its vertices to a prefix chain. Every word with total number of ones \(t\) has minimum distance \(t-\max_j(2u_j-j)\) from that chain. The integer reflection principle yields exactly \(\binom{k}{r}-\binom{k}{r-1}\) words with \(t\) ones at distance \(r\), for each of the \(k-2r+1\) possible \(t\). Unchanged coordinates convolve with a binomial shell polynomial. Largest exponent and endpoint-pair enumeration give eccentricity and exact numbers of minimizing paths. The standalone checker directly enumerates canonical shells through dimension 12 and every oriented rooted geodesic through dimension 6. Its finite computations are corroboration, not an infinite proof.

## Originality — PASS (historical priority qualified)

The recent general minimum-eccentricity shortest-path primary source, Babu et al., arXiv:2610.20769 (2026-10-14), was inspected in its accessible HTML text for results and hypercube-specific claims. Its complexity and structural-parameter results are not the displayed all-shell polynomial or all-optimum-path count. Searches for equivalent chain-distance and ballot-enumerator formulations, together with six published-finding corpus semantic searches and comparison to indexed closest published findings, found no direct equivalent or dominating claim. The principal older domination literature, Blass–Honkala–Karpovsky–Litsyn (2001) and Dvořák–Havel–Mollard (2003), examines paths in hypercubes without the shortest-path restriction. Their full texts were inaccessible, so an implicit relevant formula cannot be excluded. Dragan–Leitert (2017) was also not accessible beyond its bibliographic description. Accordingly this is best-knowledge originality, not a certified priority assertion.

## Value — PASS

A complete hypercube geodesic distance-shell distribution is more informative than the single minimum eccentricity: it specifies how many vertices are within any facility-distance threshold from any shortest path, for all dimensions and lengths. The parity-dependent rigidity of optimal path lengths and the exact large combinatorial counts of all minimizers follow and are motivated by the general graph eccentricity-shortest-path problem. This is an infinite natural graph family with a complete enumeration, not a prescribed finite test case or small routine parameter improvement.

## Closest literature and limitations

- Anand Babu et al. (2026), *Eccentricity Shortest Path: the structural parameter landscape*, arXiv:2610.20769, https://arxiv.org/abs/2610.20769 .
- F. F. Dragan and A. Leitert (2017), *On the minimum eccentricity shortest path problem*, https://doi.org/10.1016/j.tcs.2017.07.004 .
- U. Blass et al. (2001), *Short Dominating Paths and Cycles in the Binary Hypercube*, https://doi.org/10.1007/PL00001292 .
- T. Dvořák, I. Havel and M. Mollard (2003), *On paths and cycles dominating hypercubes*, https://doi.org/10.1016/S0012-365X(02)00524-1 .

The theorem does not address nongeodesic paths, weighted metrics, or multiple-path placement. Inaccessible plausible prior full texts present a residual historical-priority risk; absent independent verification is not mathematical certification.

Self-review: passed. Independent audit: not yet performed.
