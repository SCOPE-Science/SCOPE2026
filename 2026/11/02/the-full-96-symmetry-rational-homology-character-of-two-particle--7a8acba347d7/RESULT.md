# The full 96-symmetry rational homology character of two particles on the Möbius–Kantor graph

## Finding
Let \(M=G(8,3)\) be the Möbius–Kantor graph, with vertices \(u_i,v_i\) for \(i\in\mathbb Z/8\) and undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), indices taken modulo eight. Let \(X=\operatorname{UConf}_2(|M|)\) be the space of unordered distinct points on its topological realization. The full graph automorphism group \(G=\operatorname{Aut}(M)\) has order \(96\).

The rational Betti numbers of \(X\) are \((1,9,20)\), and all higher rational homology vanishes. The **complete character of the natural \(G\)-action** on \(H_1(X;\mathbb Q)\) and \(H_2(X;\mathbb Q)\) is given by the following table. Every group element is included; rows group elements with the same order and trace pair, but do not assert that these rows are conjugacy classes.

| Element order | \(\operatorname{tr}(g\mid H_1)\) | \(\operatorname{tr}(g\mid H_2)\) | Number of elements |
| ---: | ---: | ---: | ---: |
| 1 | 9 | 20 | 1 |
| 2 | -3 | 0 | 6 |
| 2 | -1 | -4 | 12 |
| 2 | -1 | 0 | 12 |
| 2 | 1 | -4 | 1 |
| 3 | -3 | 2 | 8 |
| 4 | 1 | 0 | 8 |
| 6 | 1 | 2 | 8 |
| 8 | 1 | 0 | 24 |
| 12 | 1 | 0 | 16 |

For any specified automorphism \(g\), the group-element-level character values are also determined by the explicit oriented-cell trace rules in the proof below, so the table does not hide distinct elements with the same displayed signature.

Writing \(r(u_i)=u_{i+1}\) and \(r(v_i)=v_{i+1}\), let \(R=\langle r\rangle\cong C_8\). Then
\[
\dim H_1(X/R;\mathbb Q)=\dim H_2(X/R;\mathbb Q)=2,
\]
while
\[
\widetilde H_j(X/G;\mathbb Q)=0\quad\text{for all }j\ge0.
\]
Here quotient denotes the ordinary topological orbit space, and all homology of quotients is rational.

## Assumptions and scope
The graph has sixteen vertices and twenty-four edges, is simple, connected, and has girth six. A configuration is an unordered pair of **distinct geometric points**; particles may lie in edge interiors. The cellular calculation uses the unordered discretized configuration complex formed by pairs of graph cells with disjoint closures. This complex includes naturally in \(X\), and the standard suitable-subdivision theorem shows that the inclusion is a homotopy equivalence: paths between distinct essential vertices have at least one edge, and every simple cycle has at least three edges for two particles. The inclusion is \(G\)-equivariant, whether or not a chosen deformation retraction is.

This classification is about the rational representation and rational quotients, not a claim that the configuration space is a wedge of spheres or that its integral cup product has been calculated. The integral first-homology torsion for nonplanar triconnected graphs belongs to earlier work of Ko and Park.

## Proof
Use numerical vertex labels \(u_i=i\) and \(v_i=8+i\) for \(0\le i<8\). Orient each graph edge \([a,b]\) from the smaller to the larger endpoint. The discretized complex has \(120\) vertices \(\{v,w\}\), \(336\) oriented edges \((v,[a,b])\) with \(v\notin\{a,b\}\), and \(228\) oriented squares \(([a,b],[c,d])\) with disjoint edge closures; order the two edge factors lexicographically. Their cellular boundaries are
\[
\partial(v,[a,b])=\{v,b\}-\{v,a\},
\]
\[
\partial([a,b],[c,d])=(b,[c,d])-(a,[c,d])-(d,[a,b])+(c,[a,b]).
\]
The executable certificate forms these exact integer columns and verifies \(\partial_1\partial_2=0\). It computes \(\operatorname{rank}_{\mathbb F_3}\partial_1=119\) and \(\operatorname{rank}_{\mathbb F_3}\partial_2=208\), also corroborated over \(\mathbb F_5\) and \(\mathbb F_{101}\) for the second boundary.

The particle-sum map on chains sends \(\{a,b\}\mapsto a+b\), \((v,[a,b])\mapsto[a,b]\), and every square to zero. It is a chain map from the configuration complex to the ordinary graph complex and is natural for graph automorphisms. Take a spanning-tree fundamental cycle basis of \(M\), consisting of nine simple cycles. Each misses at least one graph vertex; fixing a second particle at such a vertex lifts that fundamental cycle to a one-cycle in the configuration complex. Their images are an independent basis of \(H_1(M;\mathbb Q)\). Thus \(\dim H_1(X;\mathbb Q)\ge9\), while the rank of \(\partial_2\) over \(\mathbb Q\) is at least its rank \(208\) modulo three, giving \(\dim H_1(X;\mathbb Q)\le336-119-208=9\). Consequently the map induces a \(G\)-equivariant isomorphism
\[
H_1(X;\mathbb Q)\cong H_1(M;\mathbb Q).
\]
The exact rational rank of the second boundary is therefore \(208\), and \(\dim H_2(X;\mathbb Q)=228-208=20\). Connectedness follows from \(\operatorname{rank}\partial_1=119\); no higher-dimensional cells exist.

For \(g\in G\), let \(t_k(g)\) denote its signed trace on the \(k\)-cells of the above cube complex. On zero-cells, count fixed unordered vertex pairs; on one-cells, count fixed \((v,e)\) with sign recording reversal of the oriented edge; on two-cells, count invariant unordered disjoint-edge pairs with the product of their orientation signs and with an extra negative sign if \(g\) exchanges the two edge factors. Similarly let \(v(g)\) be the number of fixed graph vertices and \(e(g)\) the signed count of fixed graph edges. The cellular Lefschetz identities and the equivariant first-homology isomorphism yield the **elementwise character formulas**
\[
\chi_1(g)=e(g)-v(g)+1,\qquad
\chi_2(g)=t_0(g)-t_1(g)+t_2(g)-1+\chi_1(g).
\]
Enumerating all graph automorphisms by exact adjacency-preserving backtracking gives \(|G|=96\). Evaluating these formulas gives the displayed ten signature rows, with counts totaling \(96\). The certificate independently checks that every automorphism acts by cellular chain maps in both degrees.

Averaging \(\chi_1\) and \(\chi_2\) over all \(96\) elements gives zero in both degrees. The eight powers of \(r\) give the character sequences
\[
\chi_1(r^k)=(9,1,1,1,1,1,1,1),\qquad
\chi_2(r^k)=(20,0,0,0,-4,0,0,0)
\]
for \(k=0,\ldots,7\), so each \(R\)-invariant homology subspace has dimension two. For a finite group acting cellularly on a finite complex, rational homology of its ordinary orbit space equals invariant rational homology (after equivariant subdivision if needed). This gives both quotient statements.

## Verification
Run `python3 verify.py` with Python 3.9 or newer; the script uses only the standard library. It reconstructs all cells and their signed boundaries, tests the zero boundary composition, verifies modular ranks in four characteristics and a transposed matrix rank, lifts nine independent graph cycles, enumerates all 96 automorphisms, checks both chain-map identities for every group element, evaluates the complete character distribution, and checks all eight rotation traces. The required final success line is `MOBIUS_KANTOR_TWO_POINT_CHARACTER_CERTIFICATE_OK`. The cycle-basis lower bound plus rank-minor upper bound proves rational ranks, not just experimental guesses. The script does not independently prove the general subdivision theorem or the standard transfer result; these are explicitly invoked mathematical theorems.

## Relationship to prior work
Ko–Park's general first-homology theorem (arXiv:1101.2648, Theorem 3.16 and Lemma 3.15) implies the integral first-homology information for triconnected nonplanar graphs; neither that calculation nor its rank-nine specialization is presented as new. Prue–Scrimshaw (arXiv:0909.5511) supplies the suitable-subdivision framework. An–Drummond-Cole–Knudsen (arXiv:2005.08286, first public May 17, 2020) study asymptotic graph configuration homology; An–Knudsen (arXiv:2008.10371) study second homology for planar graphs. Neither establishes the full \(G\)-character for the two-point Möbius–Kantor configuration. Knill (arXiv:2605.30799) computes Lefschetz data on the graph itself, not on the two-point configuration space. Previously indexed graph-specific results for the Petersen, dodecahedral, and cuboctahedral two-particle spaces concern different graphs and do not imply this table. The natural graph \(G(8,3)\) and its 96 automorphisms are classical; novelty claimed here is precisely the full two-degree configuration-homology character and the contrast between the cyclic and full symmetry quotients.

## Limitations
The character table groups elements by (order, trace pair), not by conjugacy class. It identifies the rational \(G\)-representation up to isomorphism through its complete character, but does not list irreducible multiplicities. The rationally acyclic full quotient need not be contractible, and no corresponding integral quotient-homology claim is made. A result in unindexed literature could duplicate part of the calculation; a search without a match is not proof of uniqueness. The computations and proof are reproducible but have not undergone independent review.

## References
1. Ko and Park, *Characteristics of graph braid groups*, arXiv:1101.2648 (2011), especially Lemma 3.15 and Theorem 3.16, https://arxiv.org/abs/1101.2648.
2. Prue and Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (2009), https://arxiv.org/abs/0909.5511.
3. An, Drummond-Cole, and Knudsen, *Asymptotic homology of graph braid groups*, arXiv:2005.08286 (first public 2020-05-17), https://arxiv.org/abs/2005.08286.
4. An and Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (2020), https://arxiv.org/abs/2008.10371.
5. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799 (2026), https://arxiv.org/abs/2605.30799.
6. Drummond-Cole, *Betti numbers of unordered configuration spaces of small graphs*, arXiv:1906.00692 (2019), https://arxiv.org/abs/1906.00692 (covers graphs with at most nine edges).
