# Minimum power-dominating pairs and their mobility in the Möbius–Kantor graph

## Finding

Let \(G=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph, with bipartition \(A,B\). Its power-domination number is two, and the minimum power-dominating sets are exactly the pairs \(\{a,b\}\) with \(a\in A\), \(b\in B\), and \(ab\notin E(G)\).

Let \(Q\) be the bipartite complement of \(G\) on \(A,B\) (it has no within-part edges). Then the minimum-set token-jumping graph is the line graph \(L(Q)\). It has 40 vertices and 160 edges, and every vertex has eccentricity three. In contrast, the minimum-set token-sliding graph consists of 40 isolated vertices.

## Definitions and scope

Subscripts below are taken modulo eight. The vertices of \(G\) are \(u_i,v_i\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). Color \(u_i\) by \(i\bmod 2\) and \(v_i\) by \((i+1)\bmod 2\); there are eight vertices of each color. To test power domination, start with the closed neighborhood \(N[S]\) of a seed \(S\), then mark the unique unmarked neighbor of any marked vertex with exactly one unmarked neighbor. A seed is power dominating when this closure marks all vertices. A token jump exchanges one selected vertex for an unselected vertex, keeping a minimum power-dominating set; a token slide additionally requires the exchanged vertices to be adjacent in \(G\).

## Proof

**Classifying the minimum pairs.** The rotations \(i\mapsto i+1\), the reflection \(i\mapsto-i\), and the map \(u_i\mapsto v_{3i},\ v_i\mapsto u_{3i}\) are graph automorphisms. The last map preserves spokes and interchanges the two other edge types since \(9\equiv1\pmod8\). Thus there is one singleton representative \(\{u_0\}\), and each pair is equivalent to one of the pairs with first entry \(u_0\) and second entry listed below. The table starts with the size of the closed neighborhood and lists all subsequent strict increases under parallel forcing.

| Second entry (first entry \(u_0\)) | Sizes of marked sets |
|---|---|
| none | 4 |
| \(u_1\) | 6 |
| \(u_2\) | 7, 8 |
| \(u_3\) | 8, 12, 16 |
| \(u_4\) | 8 |
| \(v_0\) | 6 |
| \(v_1\) | 7, 8 |
| \(v_2\) | 8, 14, 16 |
| \(v_3\) | 7, 8 |
| \(v_4\) | 8, 12, 16 |

The finite table is obtained directly from the adjacency formulas: from the marked set \(D\) set \(D'=D\cup\bigcup_{x\in D,\ |N(x)\setminus D|=1}(N(x)\setminus D)\), stopping at equality. It is reproducible by the short checker in `check_mobius.py`. Parallel and sequential closure agree: a force stays enabled as the marked set grows unless its target has already been marked. Thus any closed superset of the initial set must contain each parallel iterate, and forces within any one parallel step may be performed sequentially, omitting duplicates. The empty seed cannot force in this nonempty graph. Exactly the opposite-color nonadjacent pairs succeed in the table, and the condition is invariant under all the displayed symmetries. These are therefore all the minima.

**Mobility.** The successful pairs are the edges of the 5-regular bipartite graph \(Q\). Two such pairs are joined by a jump exactly when the corresponding edges of \(Q\) share a vertex. Hence \(L(Q)\) has \(8\cdot 5=40\) vertices, degree \(2(5-1)=8\), and \(160\) edges. A slide flips the color of exactly one selected vertex, so the selected pair is no longer a minimum.

For the jump distances, let \(ab,cd\) be disjoint edges of \(Q\), where \(a,c\in A\). A path of length two exists in the line graph exactly if \(ad\) or \(cb\) is in \(Q\). Otherwise, \(a\) and \(c\) have a common \(Q\)-neighbor \(y\), since each has five neighbors in the same part of size eight. This gives a length-three path \(ab,ay,cy,cd\). To see that every edge \(ab\) of \(Q\) has a distance-three partner, pick \(c\in N_G(b)\). One of the three original neighbors of \(c\) is \(b\), which does not belong to \(N_G(a)\). Hence some \(d\in N_G(a)\) is not a neighbor of \(c\) in \(G\). Now \(cd\) is a disjoint edge of \(Q\) with both cross-edges missing in \(Q\), as required. This proves connectivity, radius three, and diameter three.

## Relationship to prior work and limitations

Bjorkman et al., [*Power domination reconfiguration*](https://arxiv.org/abs/2201.01798), give the relevant reconfiguration framework. Scalar power-domination minima for generalized Petersen graphs are a separate question treated by Xu and Kang (DOI: `10.1007/s10878-010-9293-y`) and by Zhao, Shan, and Kang (DOI: `10.7151/dmgt.2137`); no novelty is claimed for the scalar \(\gamma_P=2\). The companion result [on minimum ordinary zero forcing in the Möbius–Kantor graph](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-a-sharp-token-jumping-versus-token-sliding-dichotomy-for-minimum--9228c57633d9) treats six-vertex initial blue sets with no closed-neighborhood initialization. Its mobility statistics do not describe two-vertex power-dominating seeds. The [projective-plane incidence result](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-antiflag-mobility-and-the-two-sensor-boundary-in-projective-plan--cd43734a0963) yields an analogous line graph and slide obstruction for Heawood, but it is not a classification for the Möbius–Kantor graph.

The retained claim is the exact characterization of minimum power-dominating pairs and their mobility for \(\operatorname{GP}(8,3)\). It identifies where the local move rule freezes every optimum even though unrestricted moves connect every optimum in at most three moves. This is a single-graph theorem, not a statement about all generalized Petersen graphs, other state spaces, or other cardinalities. Available comparisons do not establish priority across all sources, particularly where the full scalar-minimum papers were not accessible.
