# Independence-complex transfer and three-periodic Rips barcodes of bipartite factor complements
## Finding
For any finite simple bipartite graph \(H\) on disjoint nonempty parts \(A,B\), write \(p=|A|\), \(q=|B|\), \(\Delta_A=\max_{a\in A}\deg_H(a)\), and \(\Delta_B=\max_{b\in B}\deg_H(b)\). Suppose
\[
p,q\ge3,\qquad q>2\Delta_A,\qquad p>2\Delta_B.
\]
Put \(G=K_{p,q}\setminus E(H)\), with the unit-edge shortest-path metric and inclusive Vietoris–Rips complexes \(\mathrm{VR}_{\le}(G;r)\). Then
\[
\mathrm{VR}_{\le}(G;2)=\operatorname{Ind}(H)
\]
as *equal abstract simplicial complexes*, not merely as homotopy types. The map
\[
H_1(\mathrm{VR}_{\le}(G;1);\mathbb Z)\longrightarrow H_1(\mathrm{VR}_{\le}(G;2);\mathbb Z)
\]
is zero. If \(H\) has an edge, \(G\) has diameter three and \(\mathrm{VR}_{\le}(G;3)\) is a simplex. Thus the entire persistence module over any field \(\Bbbk\) is determined by \(\operatorname{Ind}(H)\): in degree zero there are \(p+q-1\) bars \([0,1)\) and one infinite bar; in degree one, \(pq-|E(H)|-p-q+1\) bars \([1,2)\) and \(\dim_{\Bbbk}\widetilde H_1(\operatorname{Ind}(H);\Bbbk)\) bars \([2,3)\); in every degree \(j\ge2\), there are \(\dim_{\Bbbk}\widetilde H_j(\operatorname{Ind}(H);\Bbbk)\) bars \([2,3)\). All remaining bars in positive degrees are absent. If \(H\) has no edges, scale two is already the full simplex, so there are no \([2,3)\) bars.

In particular, fix \(n\ge5\) and delete any spanning bipartite \(2\)-factor \(H\) from \(K_{n,n}\). Write its disjoint cycle decomposition as
\[
H=\bigsqcup_{i=1}^{t}C_{2\ell_i},\qquad \ell_i\ge2,\qquad \sum_{i=1}^{t}\ell_i=n.
\]
Define
\[
D=\sum_{i=1}^{t}\left\lfloor\frac{2\ell_i+1}{3}\right\rfloor-1,
\qquad h=\bigl|\{i:3\mid\ell_i\}\bigr|.
\]
Then \(D\ge2\) and
\[
\mathrm{VR}_{\le}(G;2)\simeq\bigvee^{2^h}S^D.
\]
The *complete positive-dimensional barcode* over any field consists of exactly \(n^2-4n+1\) degree-one intervals \([1,2)\) and exactly \(2^h\) degree-\(D\) intervals \([2,3)\), and no others. In particular, deleting one Hamiltonian alternating cycle \(C_{2n}\) produces one sphere of dimension \(\lfloor(2n+1)/3\rfloor-1\), except when \(3\mid n\), when it produces two such spheres. The formula applies to every possible cycle-length partition and does not require any transitivity or coordinate model.

## Assumptions and scope
Graphs are finite, simple, and undirected. In the general statement, \(H\) has vertex set exactly \(A\sqcup B\) with possible isolated vertices, \(p,q\ge3\); \(G\) is the complement of \(H\) *inside the complete bipartite graph*, not the ordinary complement on all vertices. \(\operatorname{Ind}(H)\) consists of vertex subsets containing no edge of \(H\), including the empty face. Distances are measured in \(G\), and all scales use the non-strict inequality \(\le\). For persistence, vertices appear at radius zero and intervals are half-open at the death threshold. The homotopy equivalence does not claim a natural splitting of all attaching maps; the barcode claim additionally uses the proved vanishing of the degree-one scale-inclusion map.

## Proof
**Distance lemma.** Each vertex \(a\in A\) has at least \(q-\Delta_A\) neighbors in \(G\); each \(b\in B\) has at least \(p-\Delta_B\). For distinct \(a,a'\in A\), their \(G\)-neighbor sets have intersection of size at least \(q-\deg_H(a)-\deg_H(a')\ge q-2\Delta_A>0\); hence \(\operatorname{dist}_G(a,a')=2\). Likewise, distinct vertices of \(B\) have distance two. Across the bipartition, retained edges have distance one. If \(ab\in E(H)\), take any \(b'\in N_G(a)\) (there is one); because \(|N_G(b)|\ge p-\Delta_B>\Delta_B\ge |N_H(b')|\), there is \(a'\in N_G(b)\setminus N_H(b')\). The path \(a-b'-a'-b\) in \(G\) has length three. A two-step path from \(A\) to \(B\) is impossible in a bipartite graph, so \(\operatorname{dist}_G(a,b)=3\) for forbidden cross-edges. These observations cover every distinct vertex pair and prove connectedness. Thus the graph-square \(G^2\) has as its only missing edges precisely \(E(H)\), i.e. \(G^2=\overline H\), with the latter complement taken in the complete graph. Taking clique complexes gives exactly \(\mathrm{VR}_{\le}(G;2)=\operatorname{Cl}(\overline H)=\operatorname{Ind}(H)\). If \(E(H)\ne\varnothing\), diameter is exactly three, proving the terminal simplex assertion.

**Persistence, including induced maps.** \(G\) has \(p+q\) vertices and \(pq-|E(H)|\) edges, is connected and bipartite, and has no triangle. Hence its scale-one complex is a connected graph with first integral Betti number \(c=pq-|E(H)|-p-q+1\). Consider any oriented simple cycle, written alternately as \(a_0,b_0,a_1,b_1,\ldots,a_{k-1},b_{k-1},a_0\), where all \(a_i\in A\), \(b_i\in B\), indices are modulo \(k\), and \(k\ge2\). All triangles \([a_i,b_i,a_{i+1}]\) occur in the scale-two complex, as do all triangles in the simplex on \(A\). With the ordinary oriented simplicial boundary,
\[
\partial\sum_{i=0}^{k-1}[a_i,b_i,a_{i+1}]
=\gamma-\sum_{i=0}^{k-1}[a_i,a_{i+1}],
\]
where \(\gamma\) is the oriented edge-cycle. The final sum bounds the fan \(\sum_{i=1}^{k-2}[a_0,a_i,a_{i+1}]\) in the \(A\)-simplex (empty if \(k=2\)), with the sign shown by the oriented boundary formula. Therefore every graph cycle bounds an integral two-chain at scale two, so the indicated map on \(H_1\) is zero, integrally and after extension to any field. At scale zero, there are \(p+q\) isolated vertices; at scale one they are connected. At scale three, the simplex kills every positive-dimensional class. For degree \(j\ge2\), scale one has no classes. The barcode follows by the structure theorem for finite filtered chain complexes over a field. No hidden positive-dimensional birth/death levels exist because the metric assumes only distances zero through three.

**Independence complexes of cycles and the \(2\)-factor specialization.** For a path \(P_m\) with \(m\ge4\), delete its second vertex. The complex \(\operatorname{Ind}(P_m\setminus\{2\})\) is contractible because its first vertex is isolated, and the vertex-deletion cofibre gives \(\operatorname{Ind}(P_m)\simeq\Sigma\operatorname{Ind}(P_{m-3})\). The base cases \(m=1,2,3\) give, respectively, a point, \(S^0\), \(S^0\). Therefore for \(s\ge1\), \(\operatorname{Ind}(P_{3s})\simeq S^{s-1}\), \(\operatorname{Ind}(P_{3s+1})\simeq *\), and \(\operatorname{Ind}(P_{3s+2})\simeq S^s\), with the small cases separately as stated.

For a cycle \(C_m\), \(m\ge4\), delete any vertex and use its two neighbors: the same cofibre has \(\operatorname{Ind}(P_{m-3})\to\operatorname{Ind}(P_{m-1})\to\operatorname{Ind}(C_m)\). If \(m=3s\), \(s\ge2\), this is a map \(S^{s-2}\to S^{s-1}\), which is null-homotopic, so the cofibre is \(S^{s-1}\vee S^{s-1}\). If \(m=3s+1\), the source is contractible and the target is \(S^{s-1}\). If \(m=3s+2\), the target is contractible and the source is \(S^{s-1}\), so the cofibre is \(S^s\). Explicit checks \(C_4,C_5,C_6\) anchor these recurrences. Equivalently, for every \(m\ge4\), \(\operatorname{Ind}(C_m)\) is a wedge of \(2\) spheres if \(3\mid m\) and otherwise one sphere, always of dimension \(\lfloor(m+1)/3\rfloor-1\). This recurrence is classical and is used, not claimed as a new calculation.

When \(H\) is a bipartite \(2\)-factor, every vertex has exactly two forbidden neighbors, so the distance lemma applies since \(n>4\). Its components are the stated even cycles. Independent sets in disjoint graph components combine freely, so \(\operatorname{Ind}(H)=\ast_{i=1}^{t}\operatorname{Ind}(C_{2\ell_i})\), a simplicial join. The join of wedges of spheres here is again a wedge of spheres, with sphere degrees summing after adding one per join and with multiplicities multiplying. The cycle formula therefore gives precisely \(D=\sum_i\lfloor(2\ell_i+1)/3\rfloor-1\) and multiplicity \(2^h\). Since \(\ell_i\ge2\), \(\lfloor(2\ell_i+1)/3\rfloor\ge\ell_i/2\); \(\sum_i\ell_i=n\ge5\) forces \(D\ge2\). Finally \(|E(H)|=2n\), so the graph cycle rank is \(n^2-2n-2n+1=n^2-4n+1\). This puts all new classes at scale two in degree \(D\), establishing the stated complete barcode.

## Verification
The accompanying standard-library-only `verify.py` enumerates exact shortest-path distances, independent subsets, boundary maps over \(\mathbf F_2\), and graph-cycle fillings. It verifies every cycle-length partition of \(n=5,6,7,8\) into parts at least two (seventeen cases) plus two unequal or irregular forbidden graphs. Direct graph-metric checks agree with the claimed pairwise distances. Exact mod-two boundary reduction matches every predicted sphere dimension and multiplicity. All fundamental graph cycles admit explicitly checked mod-two triangle fillings. The proof above establishes the corresponding *integral* fillings and all-parameter claims; these finite checks are corroboration, not substitutes for an infinite proof. Run `python3 verify.py` and compare with `verification_output.txt`.

## Relationship to prior work
The equalities between a graph-power clique complex and an inclusive graph-metric Rips complex, and between a complementary graph's clique complex and an independence complex, are standard; see Adamaszek (2013), Sections 1–2. The three-periodic homotopy classification of the independence complexes of paths and cycles is due to Kozlov and is reproved or discussed in Adamaszek (2012), Sections 1, 3. The contribution here is the simultaneous *dense bipartite forbidden-edge distance criterion*, exact simplicial metric-to-independence realization, zero first-persistence-map statement, and the resulting complete parameterized cycle-factor persistence. The published circle Rips classification concerns cyclic metric graphs and circular complexes rather than the complements of arbitrary bipartite forbidden subgraphs. Published work on graph powers proves a universal existence result for homotopy types and certain collapse criteria, but not these exact dense-bipartite and deleted-factor filtration formulas.

## Limitations
The strict degree bounds are sufficient, not claimed necessary. The theorem does not classify graph metrics violating them, weighted metrics, scales using strict inequalities, or the homotopy-equivalence maps in the two-factor wedge decomposition up to equivariance. The homotopy and integral homology conclusions rest on the stated all-parameter argument; finite binary computation by itself proves only the checked examples. The independence-complex cycle theorem and the abstract graph-power correspondence are prior art. The originality comparison is bounded by accessible indexed literature; alternative formulations in unindexed graph-power or flag-complex sources cannot be ruled out, and no independent audit has yet occurred.

## References
1. Michał Adamaszek and Henry Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669v1 (2015-03-12), *Pacific Journal of Mathematics* 290 (2017), 1–40, DOI: 10.2140/pjm.2017.290.1. The journal paper lists MSC primary 55U10.
2. Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1 (2011-04-03), *Israel Journal of Mathematics* 196 (2013), 295–319, DOI: 10.1007/s11856-012-0166-1, Sections 1–4.
3. Michał Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250v1 (2011-06-30), *Journal of Combinatorial Theory, Series A* 119 (2012), 1031–1047, DOI: 10.1016/j.jcta.2012.01.009, Sections 1–3.
4. Dmitry N. Kozlov, *Complexes of directed trees*, *Journal of Combinatorial Theory, Series A* 88 (1999), 112–122, DOI: 10.1006/jcta.1999.2984, source of the standard independence-complex cycle recurrence.
