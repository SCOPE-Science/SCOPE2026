# Scientific review: Roman-domination polynomial of triangular graphs

## Correctness — PASS

For every \(n\ge5\), the proof partitions Roman functions according to the edges of \(K_n\) labeled two, then the endpoint support of that set. Every edge disjoint from the support is forced to label one, and every other unlabeled edge is freely zero or one. The induced support graph has no isolated vertices, so inclusion-exclusion over isolated endpoints gives the exact coefficient formula. The lower bound \(2\lceil(n-r)/2\rceil+\binom r2\), where \(r\) is the number of uncovered original vertices, has a unique minimizing remainder: \(r=1\) for odd \(n\), \(r=2\) for even \(n\). Equality forces a perfect matching; this proves the minimum-function census and exhausts all extremizers. The independent finite checks exhaustively enumerate all ternary labelings through \(n=5\), all label-two supports through \(n=6\), and check the minimum formula through \(n=18\). Computations are not used as proofs of the universal assertions.

## Originality — PASS, with residual risk

Roman domination on a line graph is the established edge Roman domination of the original graph, so that equivalence is attributed rather than claimed. Leely Pushpam and Mai (2009) and Chang, Chen and Liu (2014) study the edge parameter and general or bipartite minimum bounds, not the complete \(K_n\) all-weight enumerator. Gangabylaiah and colleagues (2021) introduced the Roman domination polynomial and derived formulas for stars, wheels, bicliques, graph joins and coronas, not triangular graphs. The 2022 Roman Census work counts minimal functions on other graph classes, a different distribution; the 2023 finite atlas covers the small \(T_n\) cases but not \(n\ge5\). Published complete-multipartite Roman-polynomial formulas likewise subsume \(T_3\) and \(T_4\), explicitly excluded from this claim, but not the infinitely many higher triangular graphs. Search comparisons included the edge-Roman and Johnson-graph aliases and published mathematical-result records; no directly implying formula was found in the inspected primary results. An unindexed equivalent enumeration under edge Roman domination of complete graphs is a genuine residual risk, not evidence of novelty.

## Value — PASS

The result evaluates every coefficient of a natural established graph polynomial on the classical two-subset Johnson family, not merely a scalar minimum. Its no-isolated-support-graph parametrization turns otherwise exponentially many ternary assignments into an explicit finite binomial sum. The exact classification and parity-dependent multiplicity of all minimum-weight functions provide structural information unavailable from a minimum-weight bound alone. The family and invariant were motivated independently of the computation; no downstream theorem or asymptotic conclusion is claimed.

## Closest literature and limits

The directly comparable sources are *Edge Roman Domination in Graphs* (2009), *Edge Roman domination on graphs* (arXiv:1405.5622), *On the Roman domination polynomial of graphs* (2021), *Roman Census* (arXiv:2208.05261), and the 2023 atlas of Roman polynomials for graphs with at most six vertices. The finite verification covers only stated ranges, and the possibility of an older equivalent formula under different terminology remains. Original scalar Roman domination of triangular graphs is not claimed.

Self-review: passed. Independent audit: not yet performed.
