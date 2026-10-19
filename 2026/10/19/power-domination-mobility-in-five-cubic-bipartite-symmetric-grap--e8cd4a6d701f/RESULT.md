# Power-domination mobility in five cubic bipartite symmetric graphs

## Finding

For the classical Heawood, Möbius–Kantor, Pappus, Desargues and Tutte–Coxeter cubic bipartite graphs, the minimum power-dominating-set token-jumping graph is connected and **self-centered** in every case. In contrast, token sliding is completely frozen for the first two graphs, but connected for the other three.

Write \(\gamma_P(G)\) for the minimum number of power-dominating vertices; \(N_G\) for the number of minimum sets; \(J_G\) for the token-jumping graph on those sets; and \(T_G\) for the token-sliding graph. The following is an exact finite classification:

| Graph \(G\) | \(\gamma_P(G)\) | \(N_G\) | \(|E(J_G)|\) | \(\operatorname{rad}(J_G)=\operatorname{diam}(J_G)\) | \(|E(T_G)|\) | components of \(T_G\) | radii/diameters of nontrivial \(T_G\) components |
|---|---:|---:|---:|---:|---:|---:|---|
| Heawood | 2 | 28 | 84 | 3 | 0 | 28 | none: all isolated |
| Möbius–Kantor | 2 | 40 | 160 | 3 | 0 | 40 | none: all isolated |
| Pappus | 3 | 486 | 7128 | 3 | 1620 | 1 | 7 / 8 |
| Desargues | 3 | 240 | 1800 | 4 | 480 | 1 | 7 / 8 |
| Tutte–Coxeter | 4 | 6540 | 126240 | 4 | 23040 | 1 | 11 / 13 |

More precisely, the token-sliding eccentricity distributions for the three connected cases are: Pappus, \(54\) states of eccentricity \(7\) and \(432\) of eccentricity \(8\); Desargues, \(120\) of each eccentricity \(7\) and \(8\); Tutte–Coxeter, \(1680\), \(3420\), \(1440\) states of eccentricity \(11\), \(12\), \(13\), respectively. In the Heawood and Möbius–Kantor cases no global finite token-sliding diameter is asserted, because the reconfiguration graph is disconnected.

## Assumptions and scope

All graphs are finite, undirected, loopless and explicitly labeled as follows. The Heawood graph has point vertices \(0,\ldots,6\) and line vertices \(7,\ldots,13\); line \(7+j\) is adjacent to points \(j,j+1,j+3\), with point indices modulo \(7\). The Möbius–Kantor and Desargues graphs are \(\operatorname{GP}(8,3)\) and \(\operatorname{GP}(10,3)\): vertices \(u_i,v_i\) have edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), indices modulo \(8\) or \(10\), with labels \(u_i=i\), \(v_i=n+i\). The Pappus graph is the biaffine incidence graph on point vertices \((x,y)\) and line vertices \((m,b)\) over \(\mathbb F_3\), adjacent exactly when \(y=mx+b\); its labels are \(3x+y\) and \(9+3m+b\), respectively. The Tutte–Coxeter graph has vertices for the \(15\) two-element subsets (duads) of a fixed six-element set and its \(15\) decompositions into three disjoint duads (synthemes), with membership as incidence. The labels on both sides follow lexicographic generation by the included programs; the certificate includes all graph edges.

Starting from a vertex set \(S\), the power-domination closure first marks its closed neighborhood \(N[S]\), then repeatedly marks the unique as-yet-unmarked neighbor of any marked vertex having exactly one unmarked neighbor. A set is power dominating if and only if all vertices are eventually marked. A *minimum* set has cardinality \(\gamma_P(G)\). Distinct minimum sets \(S,S'\) are adjacent in \(J_G\) when \(|S\triangle S'|=2\), and in \(T_G\) when, in addition, their two exchanged vertices are adjacent in the original graph. The processes, not a physical-grid interpretation of any particular graph, are the objects of the theorem.

## Proof

The proof is a finite exhaustive certificate with a separately checked structural obstruction.

**1. Complete minimum-set enumeration.** For a graph with \(n\) vertices, encode a set \(S\) as the \(n\)-bit integer \(m(S)=\sum_{v\in S}2^v\). The deterministic closure routine initializes its marked mask to \(m(S)\) together with the bitwise union of all neighbors of vertices of \(S\). Each iteration adds every unique unmarked neighbor of a marked vertex, terminating when the mask is unchanged. It halts in at most \(n\) strict iterations. Since each permitted force only adds a vertex and cannot invalidate other forces, this simultaneous closure reaches all vertices if and only if some (equivalently every maximal) legal forcing schedule does. For each graph, enumerate **every** subset of sizes \(1,2,\ldots,k\) until some power-dominating set appears. Monotonicity of power domination ensures none is missed at a smaller size. The initial empty set is never power dominating in these nonempty graphs. The first successful sizes and full numbers of successes are those in the first two numerical columns of the table.

**2. Exact transitions.** Index the complete list \(\mathcal P_G\) of minimum sets; for each indexed state \(S\) and each ordered choice of a selected vertex \(x\) and an unselected vertex \(y\), test whether \((S\setminus\{x\})\cup\{y\}\) belongs to \(\mathcal P_G\). This constructs \(J_G\) without guessing a path. Retain an edge for \(T_G\) precisely if \(xy\) is a graph edge. Each undirected edge is counted once. The artifact `power_certificate.json` includes the complete lists of encoded minimum sets and all indexed undirected transitions for both rules, as well as the original graph edges. All list entries are generated afresh by `power_main.py` from the formulas above. The second verifier, `power_crosscheck.cpp`, independently enumerates all fixed-size masks in numeric order using Gosper's procedure, computes closure with its own implementation, and reconstructs both transition graphs.

**3. Connectivity and distances.** Breadth-first search in each reconfiguration graph determines its components and shortest-path eccentricities. For the graphs of orders at most \(20\), `power_main.py` performs BFS from every state. For Tutte–Coxeter, the five adjacent transpositions of the six underlying symbols generate an \(S_6\)-action on the duads and synthemes preserving incidence. The induced actions preserve power domination and both exchange rules; consequently eccentricity is constant on a group orbit. There are exactly \(16\) minimum-set orbits under this action, and BFS from one member of each yields the claimed distance distribution. Independently, `power_crosscheck.cpp` performs BFS from **all** \(6540\) Tutte–Coxeter minimum sets, without using the symmetry reduction, recovering exactly the same radius, diameter and eccentricity multiplicities. Both verifiers construct components directly by full reachability.

**4. Why sliding freezes in two cases.** The complete enumeration also shows that each minimum power-dominating pair in Heawood and Möbius–Kantor contains exactly one vertex of each class of their graph bipartition. Moving either selected vertex along a graph edge flips its bipartition class, leaving both selected vertices on one side. No such pair is minimum power dominating. Therefore both token-sliding graphs are edgeless, without relying on the computational distance routine.

The combination of exhaustive cardinality checks, explicit certificate, two implementations of the state census, and independent all-source shortest paths proves each finite numerical assertion. No infinite-family theorem is inferred.

## Verification

Using only Python 3's standard library, run `python3 power_main.py --json --certificate`. It writes `power_main_summary.json` and `power_certificate.json`; the recorded console output is in `power_main.out`. Independently compile and run `g++ -std=c++17 -O3 power_crosscheck.cpp -o power_crosscheck && ./power_crosscheck`; the independently recorded output is `power_crosscheck.out`. Compare graph sizes, minima, reconfiguration-edge counts, component counts, radii, diameters and eccentricity histograms in both outputs. The finite certificate is indexed in the **original** `minimum_sets` list order, not numerical mask order. For each stored transition pair of indices, the corresponding minimum-set masks differ in exactly two bits; a sliding transition also requires those two vertices to be adjacent in `graph_edges`.

The arithmetic uses finite bitmasks, exact integer comparisons and unweighted BFS only. The maximum vertex set has \(30\) vertices and all relevant seed subsets have size at most \(4\). The certificate contains all \(6540\) Tutte–Coxeter optima and all \(126240\) token-jumping transitions, rather than a sample. Independent all-source BFS corroborates the symmetry-reduced eccentricities.

## Relationship to prior work

Benson and collaborators, *Zero forcing and power domination for graph products* (arXiv:1510.02421; first publicly posted 2015-10-08), formulate power domination as zero forcing from the closed neighborhood and give general lower bounds. Those bounds concern minimum cardinalities, not counts or reconfiguration metrics for the five graphs. Xu and Kang, *On the power domination number of the generalized Petersen graphs* (2011, DOI:10.1007/s10878-010-9293-y), examine scalar minima for subclasses of generalized Petersen graphs. Any already-established scalar values are background, not independently claimed as new here. Bjorkman and collaborators, *Power domination reconfiguration* (arXiv:2201.01798, 2022 preprint; published 2026), develop the token-jumping framework for power domination and discuss token sliding, complete graphs, bipartite graphs, cycles, paths, wheels and construction families. Their inspected sections do not specify the five graph instances and their exact pair of mobility graphs. The retained contribution is the joint **minimum-configuration and sharp-distance classification**, especially the frozen-versus-connected token-sliding contrast across these classical symmetric graphs.

## Limitations

This is a finite classification of five explicitly specified graphs; it does not give formulas for all cubic symmetric graphs, higher orders, other power-domination variants, or a universal threshold. The two implementations and finite certificate are reproducible but do not constitute independent external peer review. Published work may contain an equivalent enumeration under other language or inaccessible appendices; in particular, the full text of Xu–Kang (2011) could not be materially inspected. Therefore priority is not independently certified. A numerical agreement of two programs alone would not prove completeness without the exhaustive loops and closure specification given above.

## References

1. K. F. Benson, D. Ferrero, M. Flagg, V. Furst, L. Hogben, V. Vasilevska, B. Wissman, *Zero forcing and power domination for graph products*, arXiv:1510.02421 (first posted 2015-10-08); https://arxiv.org/abs/1510.02421.
2. G. Xu and L. Kang, *On the power domination number of the generalized Petersen graphs*, Journal of Combinatorial Optimization **22** (2011), 282–291, DOI:10.1007/s10878-010-9293-y.
3. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798 (first posted 2022-01-05); https://arxiv.org/abs/2201.01798.
4. M. Zhao, E. Shan, L. Kang, *Power domination in the generalized Petersen graphs*, Discussiones Mathematicae Graph Theory **40** (2020), 695–712, DOI:10.7151/dmgt.2137 (abstract and references materially accessible; full theorem text not verified).
