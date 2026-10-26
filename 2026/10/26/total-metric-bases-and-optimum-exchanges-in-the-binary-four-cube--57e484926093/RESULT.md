# Total metric bases and optimum exchanges in the binary four-cube

## Finding

Let \(Q_4\) be the graph with vertex set \(\{0,1\}^{4}\), adjacent when two words differ in one coordinate. A set \(S\subseteq V(Q_4)\) *totally resolves* this graph if, for every two distinct vertices \(u,v\), there exists \(w\in S\setminus\{u,v\}\) satisfying \(d(w,u)\neq d(w,v)\). Write \(\dim_t(Q_4)\) for the smallest possible cardinality of \(S\). Then

\[
\dim_t(Q_4)=6.
\]

There are exactly \(1600\) total resolving sets of minimum cardinality (total metric bases). Under the full group of \(384\) binary-cube automorphisms, these sets fall into exactly eleven orbits of sizes

\[
32,32,96,96,192,192,192,192,192,192,192.
\]

Form the *optimal exchange graph* whose vertices are these \(1600\) bases and whose edges join sets with one removed vertex and one newly selected vertex. This graph is **connected**, has exactly \(17088\) edges, and has the following complete degree distribution:

| Degree | Number of bases |
|---:|---:|
| \(12\) | \(384\) |
| \(22\) | \(576\) |
| \(26\) | \(576\) |
| \(30\) | \(64\) |

Thus the total metric dimension of the first hypercube beyond the previously calculated three-cube is determined, including every labelled minimum solution and its exchange geometry.

## Assumptions and scope

Only the standard unweighted graph distance on \(Q_4\) is used. Every ordered vertex label \(0,\ldots,15\) means its four-bit binary expansion; \(d(u,v)=\operatorname{wt}(u\oplus v)\). The resolving witness must be distinct from *both* endpoints; ordinary metric resolution is weaker. Exchange adjacency is by symmetric difference of size two, with no intermediate nonoptimal states. All counts refer to labelled cube vertices; automorphism-orbit counts are stated separately. This is one finite-graph theorem, not an assertion about higher-dimensional cubes.

## Proof

For each unordered pair \(\{u,v\}\) define its admissible third-party witnesses by

\[
R_{uv}=\{w\in\{0,\ldots,15\}\setminus\{u,v\}:\operatorname{wt}(w\oplus u)\neq\operatorname{wt}(w\oplus v)\}.
\]

By the definition, \(S\) totally resolves \(Q_4\) **if and only if** it intersects all \(120\) sets \(R_{uv}\). The \(120\) pairs divide by Hamming distance into \(32,48,32,8\) pairs at respective distances \(1,2,3,4\). At odd pair-distance, every third vertex resolves the pair by parity. The nontrivial constraints thus occur at distances two and four; in particular every distance-two pair has exactly six admissible witnesses and every antipodal distance-four pair has eight.

The remaining steps are a **finite exhaustive proof**, with its complete enumeration algorithm supplied as `verify.py` and a separately programmed cross-check as `independent.cpp`. The finite search covers the entire domain, rather than sampling it:

1. Enumerate all \(2^{16}=65536\) subset masks, retaining those of cardinality at most six. For each retained mask, require a nonempty bitwise intersection with every explicitly constructed \(R_{uv}\). Equivalently, the domain can be traversed as the exact \(\binom{16}{k}\) combinations for each \(0\le k\le6\). The counts of passing subsets are \(0,0,0,0,0,0,1600\). Therefore no smaller set works and all \(1600\) minimum bases have been captured.
2. As a cross-check on the constraint logic, the \(48\) distance-two requirements admit exactly \(1608\) six-vertex hitting sets. Precisely eight of them fail one of the eight antipodal constraints. A second routine tests each accepted set by directly iterating all endpoint pairs and all selected third vertices, independently of the precomputed hitting masks.
3. Explicitly enumerate all \(4!\cdot 2^4=384\) automorphisms, mapping \(x\) to a coordinate permutation of \(x\), followed by a binary translation. Apply them to each unclassified accepted mask to compute its full orbit; the orbit sizes are exactly those in the finding, and they partition all \(1600\) accepted masks.
4. For each accepted mask, enumerate its \(6\cdot10=60\) possible single-deletion/single-insertion replacements. Keep precisely those resulting masks appearing in the complete accepted set. This constructs every exchange edge, counts \(17088\) undirected edges, and gives the stated degree histogram. Breadth-first search visits all \(1600\) vertices from one start, proving connectivity.

Every loop bound, mask construction and membership predicate appears in the supplied executable source, including checks of the asserted totals. A second C++ implementation independently enumerates the complete \(65536\)-mask universe and recalculates the optimum count and exchange degrees. These finite-domain computations constitute a reproducible exhaustive certificate for the finite statements; no extrapolation to an infinite family is used.

For additionally identifying the eleven orbit representatives, with each six-set encoded as \(\sum_{v\in S}2^v\), one may use

| Representative mask | Orbit size | Exchange degree |
|---:|---:|---:|
| 63 | 96 | 22 |
| 126 | 32 | 30 |
| 303 | 192 | 22 |
| 317 | 192 | 26 |
| 318 | 192 | 26 |
| 366 | 192 | 26 |
| 444 | 192 | 12 |
| 828 | 32 | 30 |
| 857 | 192 | 12 |
| 1683 | 192 | 22 |
| 5766 | 96 | 22 |

These integer masks are identifiers for the exact finite calculation, not bare mathematical expressions.

## Verification

Run `python3 verify.py` with Python \(3.8\) or later. It uses the standard library, enumerates every subset of cardinality at most six, checks a second direct metric predicate on every valid minimum set, enumerates all automorphism orbits, and constructs every one-swap adjacency and component. The run ends with `ALL_VERIFY_OK` after printing the actual counts.

As an independently coded check, run `g++ -O3 -std=c++17 -o checker independent.cpp && ./checker`. It enumerates all \(65536\) masks directly rather than by subsets of each cardinality and recomputes the optimum histogram and exchange degrees. It corroborates the optimum enumeration and edge totals; orbit and connectivity checks reside in `verify.py`.

## Relationship to prior work

Ganesan's 2011 paper *Minimal resolving sets for the hypercube* examines **ordinary** metric resolving sets, including \(\dim(Q_4)=4\). It supplies the earliest publicly dated foundational hypercube-resolving source cited here (first posted \(2011\)-\(06\)-\(18\)); it does **not** introduce the stricter total resolving condition or prove the present theorem.

Hedetniemi, Laskar and Mulder (2020) introduce *total metric dimension*, give \(\dim_t(Q_3)=6\), and explicitly ask for the dimension of higher cubes beginning with \(Q_4\) (Question 7). The present result resolves that first case and adds all minimum bases and their exchange graph. The new invariant's 2020 introduction is acknowledged; the separate 2011 source is archival background and should not be misread as the original definition of total metric dimension.

Kelenc and coauthors (2021) compare ordinary, edge and mixed metric dimensions of hypercubes, not third-party total resolution. The equivalent hitting-set formulation was included in novelty searches. No covering prior theorem was identified in the inspected sources or searched research records; this is a qualified best-knowledge comparison, not a guarantee of publication priority.

## Limitations

The theorem is exact only for \(Q_4\). It does not bound \(\dim_t(Q_n)\) for arbitrary \(n>4\), nor does it classify optimum solutions in larger hypercubes. Exhaustive enumeration is an exact finite proof for sixteen vertices, not an infinite proof. An unindexed prior computation could contain an equivalent census or exchange-graph result; independent external audit has not been performed.

## References

1. A. Ganesan, *Minimal resolving sets for the hypercube*, arXiv:1106.3632, first submitted 2011-06-18. https://arxiv.org/abs/1106.3632
2. S. T. Hedetniemi, R. C. Laskar and H. M. Mulder, *New resolvability parameters of graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 1028–1038, DOI 10.1016/j.akcej.2019.12.021. https://doi.org/10.1016/j.akcej.2019.12.021
3. A. Kelenc, A. T. M. Toshi, R. Škrekovski and I. G. Yero, *On metric dimensions of hypercubes*, arXiv:2102.10916 (2021). https://arxiv.org/abs/2102.10916
