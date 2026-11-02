# Clebsch edge-metric bases: four symmetry types and a seven-move exchange diameter

## Finding

Let \(C\) be the five-regular Clebsch graph on \(V=\mathbb F_2^4\), represented by integers \(0,\ldots,15\) in four-bit notation, with edges \(\{x,x\oplus d\}\) for \(d\in\{1,2,4,8,15\}\), where \(\oplus\) denotes bitwise XOR. For an edge \(e=\{a,b\}\) and vertex \(v\), put \(\delta(v,e)=\min\{d_C(v,a),d_C(v,b)\}\). An **edge-metric basis** is a minimum-cardinality vertex subset \(S\) for which the vectors \((\delta(v,e))_{v\in S}\) differ for every pair of distinct edges \(e\).

The minimum size \(\operatorname{edim}(C)=9\) is **known** from the literature and is not a new assertion here. The complete minimum-configuration and exchange classification is as follows.

**Theorem.** The Clebsch graph has exactly \(1600\) labelled edge-metric bases. Under its natural affine automorphism group \(2^4\!:\!S_5\) of order \(1920\), these bases form exactly four orbits of sizes \(160,240,240,960\). These four orbits are distinguished by the degree multisets of the seven-vertex induced subgraphs on their omitted vertices:

| Orbit size | Omitted-set induced degrees, sorted | Legal one-vertex replacements per basis | Eccentricity in the exchange graph |
|---:|---|---:|---:|
| 160 | \((1,1,1,2,2,2,5)\) | 27 | 6 |
| 240 | \((0,1,1,1,1,3,3)\) | 15 | 7 |
| 240 | \((2,2,2,2,3,3,4)\) | 15 | 7 |
| 960 | \((1,1,1,2,2,3,4)\) | 15 | 7 |

Connect two edge-metric bases when exactly one selected vertex is replaced with an unselected vertex (equivalently their intersection has size eight). The resulting undirected simple **basis-exchange graph** has exactly \(1600\) vertices and \(12960\) edges. It is connected, has radius \(6\) and diameter \(7\), and has degree distribution \(15^{1440},27^{160}\). Its centers are precisely the \(160\) members of the high-degree affine orbit. Thus every optimum edge-identification deployment can be changed into every other in at most seven individually valid optimum-preserving replacements, and seven replacements are sometimes necessary.

## Assumptions and scope

Everything is in the finite, simple, unweighted, undirected graph \(C\) just defined. Vertex labels are the sixteen binary words and the five XOR directions specify all forty graph edges without reliance on a drawing. Edge distance is the minimum of the distances to the endpoints, not distance in the line graph. Bases are subsets (not ordered tuples); they distinguish all \(\binom{40}{2}=780\) pairs of edges. An exchange removes exactly one vertex and inserts exactly one different vertex, and every intermediate set must remain an edge-metric basis of size nine. Eccentricity, radius and diameter use shortest-path distance in that undirected exchange graph. The quoted affine action consists of translations followed by linear transformations that permute the five direction vectors.

## Proof

The calculations below give a complete finite proof with two separately implemented standalone checkers, `verify.py` and `verify_alt.cpp`, supplied with this result. All enumerated universes are explicitly bounded; neither random sampling nor extrapolation is used.

**1. The graph and the edge-distinguishing relation.** The five directions \(D=\{1,2,4,8,15\}\) have pairwise distinct nonzero values. Thus each of the sixteen vertices has five distinct neighbors and the sorted list of undirected edges has forty entries. Every nonzero four-bit vector is either in \(D\) or the XOR of two distinct members of \(D\), so \(d_C\) takes values zero, one or two. An element \(v\) distinguishes two edges \(e,f\) exactly when \(\delta(v,e)\ne\delta(v,f)\). Both programs construct precisely this predicate, while the C++ program independently obtains all vertex distances by breadth-first search rather than from the closed distance-two expression.

**2. Exact minimum and its multiplicity.** Index the \(780\) unordered edge pairs and let \(Q_v\) be the \(780\)-bit vector whose bit at \(\{e,f\}\) is one precisely when \(\delta(v,e)\ne\delta(v,f)\). A vertex subset \(S\) distinguishes every edge pair if and only if the bitwise union \(R(S)=\bigvee_{v\in S}Q_v\) is the all-one vector. With the empty-set mask set to zero, the recurrence
\[
R(S)=R(S\setminus\{v\})\mathbin{\mathrm{OR}}Q_v
\]
for the least labelled \(v\in S\) computes this predicate for every one of the \(2^{16}=65536\) subsets. The complete enumeration yields no qualifying subsets of cardinality at most eight and exactly \(1600\) qualifying subsets of cardinality nine. The independent C++ program enumerates every subset of cardinality at most nine and, for each, checks uniqueness of all forty explicit ternary distance words. It produces the same outcome. This also independently corroborates the previously reported minimum nine.

**3. Four affine symmetry types.** The XOR of all five elements of \(D\) is zero and any four are linearly independent. Therefore every permutation of these five directions determines a unique invertible linear map of \(\mathbb F_2^4\); composing with sixteen translations gives \(16\cdot120=1920\) distinct automorphisms. To classify the \(1600\) enumerated bases, apply all these maps to the first not-yet-classified basis and mark its resulting orbit. Repeating until no basis remains yields four disjoint complete orbits, with sizes \(160,240,240,960\). The verifier also records concrete basis masks `0x77e`, `0x16bd`, `0x777` and `0x77b` (with the above four orbit sizes respectively). Applying the automorphisms and computing the induced degrees of the omitted seven vertices gives exactly the four listed, distinct degree signatures. Since the orbit sizes add to \(1600\), no further bases or symmetry types exist. The full classical automorphism group of the Clebsch graph has order \(1920\), so these are also its full-automorphism orbits; the classification would remain true for the specified affine action even without this identification.

**4. Exchanges and shortest paths.** Starting from each of the \(1600\) basis bitmasks, check all \(9\cdot7=63\) possible remove-one/add-one masks against the complete basis set. These checks yield degree \(27\) at exactly \(160\) bases and degree \(15\) at the other \(1440\). The total number of undirected exchanges is
\[
\frac{160\cdot27+1440\cdot15}{2}=12960.
\]
Every neighbor relation is checked in both directions. A complete breadth-first search starting at each of the \(1600\) vertices reaches all \(1600\) vertices and gives eccentricity six at exactly \(160\) sources and seven at the other \(1440\). Hence the exchange graph is connected, its radius is six and diameter is seven; the source eccentricity groups coincide exactly with the degree groups and the stated symmetry orbits. The C++ implementation independently reconstructs edges by the one-vertex-replacement test and runs all-source breadth-first searches, agreeing with every metric value.

The exhaustive search algorithms, loop ranges and assertion checks in the supplied programs are the finite certificates underlying Steps 2–4. They are not just examples or sampled simulations.

## Verification

Run `python3 verify.py` with Python 3.10 or later. It must print `EDGE_RESOLVING_OK`, `EXCHANGE_OK`, `ORBITS_OK` and end with `ALL_VERIFY_OK`. This program examines all \(65536\) vertex subsets, all \(780\) edge pairs, the full minimum-basis exchange relation and all \(1920\) affine maps. It reports the four orbit representatives and induced-degree signatures.

Independently compile and execute `g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt`. This program computes shortest paths from the graph adjacency relation, tests all \(50643\) subsets of size at most nine by direct edge-signature uniqueness, reconstructs exchanges and verifies every eccentricity. It ends with `INDEPENDENT_VERIFY_OK`. Agreement includes minimum size nine, \(1600\) optimum subsets, \(12960\) exchange edges, one component, radius six and diameter seven. Two implementations and the displayed finite reduction check all numerically critical claims; they do not substitute for an independent scholarly audit.

## Relationship to prior work

Kelenc, Tratnik and Yero introduced edge metric dimension and the precise vertex-to-edge distance predicate in their paper first submitted to arXiv on 31 January 2016 [1]. Milivojević Danas, Kratica, Savić and Maksimović explicitly list the Clebsch graph's **edge metric dimension nine** in Table 8 of their 2020 comparison article [2]. That established scalar is acknowledged, not presented as new. The paper [2] gives the minimum and mixed-metric bounds, but neither a count or symmetry classification of all minimum edge-metric bases nor the connectivity and metric classification of their replacement graph. The standard group order and Clebsch folded-cube identification are independently documented in [3]. These references do not logically determine the new counts and exchange distances. Existing published descriptions could still contain equivalent results under other terminology; priority is not independently certified.

## Limitations

The result is a complete classification only for the sixteen-vertex, five-regular Clebsch graph with the edge-distance convention stated above. It is not a theorem for arbitrary folded cubes, strongly regular graphs or a general class of reconfiguration graphs. Exact finite computation supplies the key classification and metric certificates; no simpler closed-form characterization independent of the exhaustive finite check is claimed. Published-literature coverage is best-knowledge rather than a proof that no equivalent unindexed result exists. No independent scholarly validation has been carried out.

## References

1. A. Kelenc, N. Tratnik and I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291v1, 31 January 2016, https://arxiv.org/html/1602.00291v1 .
2. M. Milivojević Danas, J. Kratica, A. Savić and Z. Lj. Maksimović, *Some new general lower bounds for mixed metric dimension of graphs*, arXiv:2007.05808v1, 11 July 2020, Table 8, https://arxiv.org/html/2007.05808v1 .
3. A. E. Brouwer, *Clebsch graph*, https://aeb.win.tue.nl/graphs/Clebsch.html (graph structure and automorphism group).
