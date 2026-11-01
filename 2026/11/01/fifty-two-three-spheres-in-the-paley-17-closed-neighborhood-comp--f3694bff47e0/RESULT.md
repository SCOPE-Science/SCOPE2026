# Fifty-two three-spheres in the Paley-17 closed-neighborhood complex

## Finding
Let \(P_{17}\) be the seventeen-vertex Paley graph and let \(K=\mathcal N[P_{17}]\) be its *closed-neighborhood complex*. Then the geometric realization has the exact integral homotopy type
\[
\boxed{|K|\simeq\bigvee^{52} S^3.}
\]
Therefore
\[
\widetilde H_i(K;\mathbb Z)\cong
\begin{cases}\mathbb Z^{52},&i=3,\\0,&i\neq3.\end{cases}
\]
In particular, \(K\) is simply connected and has torsion-free integral homology. This contrasts with the published computation of the *open*-neighborhood complex of the same Paley graph, which has an integral three-torsion class.

## Assumptions and scope
Work with the additive group \(\mathbb Z/17\mathbb Z\). Write
\[
Q=\{1,2,4,8,9,13,15,16\}.
\]
The simple graph \(P_{17}\) has vertices \(0,1,\ldots,16\), where distinct vertices \(u,v\) are adjacent when \(v-u\pmod {17}\in Q\). The closed neighborhood is \(N[v]=\{v\}\cup(v+Q)\), a set of exactly nine vertices.

The abstract simplicial complex \(K\) consists of all subsets \(\sigma\subseteq \mathbb Z/17\mathbb Z\) for which some \(v\) has \(\sigma\subseteq N[v]\). Its seventeen maximal faces each have nine vertices, so its dimension is eight. This convention is **closed** neighborhood; omitting the center \(v\) changes the complex. The exact result is asserted for this one graph and no others. All statements of homotopy equivalence refer to geometric realizations.

## Proof
**Complete enumeration.** Represent any nonempty face by an integer mask, with bit \(j\) set exactly when vertex \(j\) belongs to the face. For each of the seventeen neighborhoods, enumerate every nonempty subset of its nine vertices and deduplicate masks. Exhaustiveness is checked independently by testing, for all \(2^{17}-1=131071\) nonzero masks, whether it is a subset of any of the seventeen closed-neighborhood masks. Both methods give precisely 6,851 nonempty simplices with face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8)
=(17,136,680,1734,2074,1428,612,153,17).
\]
The alternating face sum is \(-51\), as required by a wedge of 52 odd-dimensional spheres.

**Explicit global matching.** Set the complete vertex-toggle order to
```
(5, 1, 10, 3, 9, 12, 14, 15, 8, 16, 6, 4, 2, 0, 11, 13, 7)
```
Initially mark every nonempty face unmatched. For each vertex \(v\) in that order, scan currently unmatched faces in increasing numerical mask order. If \(v\notin\sigma\), and both \(\sigma\) and \(\sigma\cup\{v\}\) remain unmatched, pair those two faces and immediately remove both. Subsequent stages never reuse a paired face. This deterministic rule creates exactly **3,399 pairs**, leaving **one critical vertex and 52 critical three-simplices**; there are no critical cells in any other dimension.

**Full acyclicity certificate.** For every codimension-one incidence between nonempty simplices, direct the edge from the higher-dimensional face to the lower-dimensional face, *except* for a matching incidence, which is directed upward. There are exactly **33,847** such directed incidences on **6,851** nodes. The standalone verifier generates each incidence once, constructs every indegree, and performs a complete Kahn topological sort. The sort visits all 6,851 nodes; consequently the directed face graph has no directed cycle, so the matching is acyclic. This is an exhaustive directed-graph computation, not an inference from local matching rules alone.

**Integral homotopy conclusion.** Forman's discrete-Morse CW theorem gives a CW complex homotopy equivalent to \(|K|\) with one \(0\)-cell and exactly 52 \(3\)-cells and no other cells. Its two-skeleton is a point. Every attaching map of a \(3\)-cell has domain \(S^2\) and lands in this point, so all 52 attachments are null. Thus the CW complex is precisely a wedge of 52 three-spheres up to homotopy. This step proves the **integral homotopy type**, rather than only mod-two Betti numbers.

## Verification
The supplied `verify.py` uses only the Python standard library. From the graph definition, it reconstructs all faces twice; verifies the strongly regular parameters \((17,8,3,4)\); checks the matching cardinalities and codimension-one conditions; and topologically sorts the complete reversed-matching Hasse graph. It also independently computes sparse simplicial boundary ranks over \(\mathbb F_2\) from the original face complex, obtaining ranks
```
{1: 16, 2: 120, 3: 560, 4: 1122,
 5: 952, 6: 476, 7: 136, 8: 17}
```
for the nonaugmented boundary operators. Those ranks imply mod-two reduced Betti number 52 only in degree three. The matching and acyclicity proof, not the field calculation, establishes the integral homotopy equivalence.

Execute `python3 verify.py` and require the final line `ALL_VERIFY_OK`. The exact finite object is small enough for the entire certificate to be reconstructed from this single script; no external data, cached matrices, web access, or proprietary software are dependencies.

## Relationship to prior work
Matsushita, *Closed neighborhood complexes of graphs* (first public version November 16, 2025), defines exactly this closed-neighborhood construction and establishes general equivalences involving independence complexes of canonical double covers and neighborhood hypergraphs. Theorem 1.2 determines a **suspension** in terms of a double-cover independence complex; the worked exact family in Example 3.5 is the Cartesian product of complete graphs. Neither result supplies the 17-vertex Paley matching or the number 52.

The published *Three-torsion in the neighborhood complex of the Paley graph of order seventeen* computes the **open** Lovász neighborhood complex \(\mathcal N(P_{17})\), not \(\mathcal N[P_{17}]\). Its seventeen neighborhoods have eight vertices each, yielding 3,468 nonempty faces and the homotopy type
\[
\mathcal N(P_{17})\simeq M(\mathbb Z/3,2)\vee\bigvee^{35}S^3.
\]
The inclusion \(\mathcal N(P_{17})\hookrightarrow\mathcal N[P_{17}]\) exists, but the two calculations do not coincide. In particular, the induced map on reduced degree-two integral homology is necessarily zero, since the target group vanishes. This is a consequence of the new homotopy type, not a separate claimed classification of the inclusion map.

Searches under closed neighborhood, vertex-centered graph Čech at radius one, reflexive neighborhood, and double-cover independence formulations found no previously published full homotopy classification of \(\mathcal N[P_{17}]\). A search failure is not a proof of novelty; equivalent unindexed work is possible.

## Limitations
This is an exhaustive **finite** classification for \(P_{17}\), not an infinite Paley-graph formula. It does not determine the induced map in degree three from open to closed neighborhoods, an equivariant sphere decomposition, persistence at other radii, or a simple-homotopy type with a specified minimal simplicial model. The integer homotopy claim uses an explicitly checkable discrete-Morse acyclicity computation; mod-two ranks alone would not be sufficient. Bibliographic searches cannot exclude unindexed equivalent work.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, initial public submission 2025-11-16, https://arxiv.org/abs/2511.12608 .
2. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, public mathematical result with complete proof and verifier, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8 .
3. DistanceRegular.org, *Paley graph P17*, graph parameters and adjacency reference, https://www.math.mun.ca/distanceregular/graphs/paley17.html .
