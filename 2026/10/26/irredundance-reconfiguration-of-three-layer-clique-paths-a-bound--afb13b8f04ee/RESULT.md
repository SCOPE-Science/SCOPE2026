# Irredundance reconfiguration of three-layer clique paths: a bounded core and exponentially many frozen optima

## Finding

For each integer \(n\ge4\), let \(G_n=K_n\square P_3\). The following theorem simultaneously determines all irredundant sets, all inclusion-maximal irredundant sets, and the slide reconfiguration graph of maximum-cardinality irredundant sets.

Write the vertices as \(a_i,b_i,c_i\) for \(i\in[n]=\{1,\ldots,n\}\), with each of \(\{a_i\}\), \(\{b_i\}\), and \(\{c_i\}\) inducing a clique, and with matching edges \(a_ib_i\) and \(b_ic_i\). A selected set is encoded by the three index sets \((A,B,C)\).

**All-set and maximal-set enumeration.** If \(I_n(z)\) counts every irredundant set (including the empty set) by cardinality, and \(M_n(z)\) counts inclusion-maximal irredundant sets, then
\[
I_n(z)=(1+2z)^n+nz^2+(1+z)^n-1+2nz\big((1+z)^n-1-z^n\big)+n^3z^3,
\]
\[
\boxed{M_n(z)=n^3z^3+\big(2n^2+2^n+1\big)z^n.}
\]
In particular, the lower and upper irredundance numbers are \(\operatorname{ir}(G_n)=3\) and \(\operatorname{IR}(G_n)=n\), with difference \(n-3\).

**Exact upper-irredundance reconfiguration graph.** Let \(\mathcal R_n\) have the \(\operatorname{IR}(G_n)\)-sets as vertices; two are adjacent when one selected vertex can be replaced by an adjacent, unselected vertex, preserving maximum irredundance. Let \(R_n=K_n\square K_n\). Take two disjoint copies of \(R_n\) and one extra vertex \(h\); join \(h\) to the \(n\) diagonal vertices \((i,i)\) in each copy. Call the resulting graph \(H_n\). Then
\[
\boxed{\mathcal R_n\cong H_n\sqcup 2^nK_1.}
\]
Consequently, \(\mathcal R_n\) has exactly \(2^n+1\) connected components, of which \(2^n\) are isolated vertices, while its unique nontrivial component has \(2n^2+1\) vertices, \(2n^2(n-1)+2n\) edges, and diameter exactly \(4\).

## Assumptions and scope

All graphs are finite, undirected, and simple. A vertex \(v\) selected in \(S\) has a private closed-neighborhood witness if some vertex of \(N[v]\) belongs to no \(N[u]\) for \(u\in S\setminus\{v\}\). The set \(S\) is **irredundant** if every selected vertex has a witness. The empty set is counted as irredundant. **Maximal** means inclusion-maximal; **maximum** means largest cardinality, not merely maximal. In \(\mathcal R_n\), adjacency uses a single slide along an original edge, not an unrestricted jump. Statements above assume exactly \(n\ge4\); no claim about the stated reconfiguration decomposition is made for smaller \(n\).

## Proof

**1. Local neighborhoods.** The complete neighborhoods are
\[
N[a_i]=\{a_j:j\in[n]\}\cup\{b_i\},\quad
N[b_i]=\{b_j:j\in[n]\}\cup\{a_i,c_i\},\quad
N[c_i]=\{c_j:j\in[n]\}\cup\{b_i\}.
\]
They give an exhaustive classification of irredundant triples \((A,B,C)\):

* When \(B=\varnothing\), irredundance is equivalent to \(A\cap C=\varnothing\), **or** \(A=C=\{i\}\) for a single index \(i\). Indeed, any selected outer vertex with a second selected vertex in its own clique must use its middle matched neighbor as a private witness. That witness is lost precisely when the other outer clique contains its index. An outer singleton always has its own selected vertex as a private witness when the middle clique is unoccupied.
* When \(B\ne\varnothing\), no outer clique can contribute two selected vertices, since the selected middle vertex destroys the only possible private witnesses of a multi-vertex outer selection. With both outer cliques represented, the middle clique may contribute only one selected vertex: two selected middle vertices would have no private witness in the middle clique, while the two occupied outer cliques dominate all of their respective layers. Conversely, any triple of singletons \(A=\{i\},B=\{j\},C=\{k\}\) is irredundant: the outer vertices use outer witnesses at indices different from \(j\), and \(b_j\) uses a middle vertex indexed outside \(\{i,k\}\). Such an index exists for \(n\ge3\).
* When \(B\ne\varnothing\) and exactly one outer clique is represented by a singleton, irredundance is equivalent to \(B\subsetneq[n]\). The outer singleton needs an outer private witness indexed outside \(B\), while every selected middle vertex can use its matched vertex in the unoccupied outer clique as a private witness.
* When \(B\ne\varnothing\) and both outer cliques are empty, every selection of \(B\) is irredundant, because each selected middle vertex has an unused outer matched private witness, except that the singleton case also witnesses itself.

The four disjoint types contribute, respectively, \((1+2z)^n+nz^2\), \(n^3z^3\), \(2nz((1+z)^n-1-z^n)\), and \((1+z)^n-1\), proving the asserted formula for \(I_n(z)\).

**2. Inclusion-maximal sets.** In the case \(B=\varnothing\), the only maximal selections are the two full outer cliques and the nonempty proper complementary partitions \(A\sqcup C=[n]\). An exceptional coincident singleton pair \(A=C\) extends by a middle singleton and therefore is not maximal. With no outer selection and \(B\ne\varnothing\), only the entire middle clique is maximal. With exactly one outer singleton, \(B\) can be enlarged until it omits exactly one index; every such set is maximal, and there are \(2n^2\) of them. With both outer singletons, \(B\) must be a singleton, giving \(n^3\) maximal triples. This list is exhaustive by Step 1; adding any further vertex to one of its listed members violates at least one of the listed conditions.

There are \(2^n-2\) nonempty proper complementary partitions, three full cliques, and \(2n^2\) singleton-plus-almost-full-middle sets, all of size \(n\); the other \(n^3\) maximal sets have size three. Since \(n\ge4\), the sizes are distinct, proving the formula for \(M_n(z)\), and \(\operatorname{ir}(G_n)=3\), \(\operatorname{IR}(G_n)=n\).

**3. Slide adjacency of maximum sets.** Denote the full middle clique by \(h\). The size-\(n\) families are \(h\); two full outer cliques; the \(2^n-2\) complementary outer partitions; and, for each outer layer \(L\in\{a,c\}\), sets
\[
U^L_{i,k}=\{L_i\}\cup\{b_j:j\in[n],\ j\ne k\},\qquad i,k\in[n].
\]
For fixed \(L\), a legal slide between two such sets changes exactly one of \(i\) and \(k\): changing \(i\) slides within the outer clique, and changing \(k\) slides within the middle clique. Therefore these \(n^2\) sets induce precisely \(K_n\square K_n\).

A slide from \(h\) reaches \(U^L_{i,k}\) exactly when \(i=k\), by exchanging \(b_i\) for its outer matched vertex. The two rook-graph families have no direct slide between them because an outer vertex is never adjacent across the two outer layers. Every complementary partition and both full outer cliques are isolated: a slide within an outer layer creates a repeated index, and a slide to the middle layer cannot create any of the classified maximum-size types when \(n\ge4\). These are all possibilities for a one-vertex exchange, so \(\mathcal R_n\cong H_n\sqcup2^nK_1\).

Each rook graph has \(n^2(n-1)\) edges; the hub contributes another \(2n\). Every rook-graph vertex is at distance at most one from a diagonal vertex in its copy, hence at distance at most two from \(h\). Vertices in opposite copies can only connect through \(h\); a pair of off-diagonal vertices on opposite sides has distance exactly four. Vertices within one copy have distance at most two. Thus \(\operatorname{diam}(H_n)=4\), proving all component counts and dimensions.

## Verification

The accompanying standalone program `verify.py` implements the private-neighbor predicate directly from closed neighborhoods. It independently enumerates all \(2^{3n}\) vertex subsets for \(n=4,5,6,7\), compares with the four-case classification and both counting polynomials, then computes inclusion-maximal sets and the actual slide edges, components, edge counts, and diameter. The complete executed domain comprises \(2{,}396{,}160\) subsets; all tests passed. This enumeration checks four finite instances but is not a proof of the universal statement, which follows from Steps 1–3.

Reproduction: run `python verify.py` with a standard Python 3 installation from the directory containing this file.

## Relationship to prior work

Mynhardt and Roux investigated the slide-based \(\operatorname{IR}\)-graph framework, including general realizability and structural restrictions; the present theorem resolves a concrete Cartesian-product family by an explicit complete enumeration and graph isomorphism rather than a general existence result. Kuenzel and Rall characterized well-dominated Cartesian products, proving in particular that \(K_n\square P_3\) is not well-dominated for \(n\ge4\). That non-well-dominatedness statement does not yield the private-neighbor classification, polynomial, or slide component structure here.

The published exact irredundance classification of complete multipartite graphs applies to a different class: \(K_n\square P_3\) is not complete multipartite, since its nonadjacent outer vertices cannot all occupy one independent part while each outer layer is a clique. The related claw-free maximal-irredundance enumeration algorithms do not directly apply: for \(n\ge2\), the center \(b_i\) and leaves \(a_i,c_i,b_j\) (\(j\ne i\)) induce a claw. Searches and comparisons are detailed in `AUDIT.json`; no priority claim beyond the examined sources is made.

## Limitations

The theorem is restricted to \(n\ge4\); the smaller case \(n=3\) has a different maximum-set slide structure because size-three triples and size-\(n\) selections coincide. The computational checks do not constitute infinite verification. Independent mathematical audit and comprehensive priority verification have not been performed; unindexed work or stronger differently formulated results may exist.

## References

1. C. M. Mynhardt and A. Roux, *Irredundance Graphs*, arXiv:1812.03382, initially public 2018-12-08. https://arxiv.org/abs/1812.03382
2. K. Kuenzel and D. F. Rall, *A characterization of well-dominated Cartesian products*, arXiv:2306.04105, initially public 2023-06-07. https://arxiv.org/abs/2306.04105
3. *Enumeration of maximal irredundant sets for claw-free graphs*, Theoretical Computer Science (2018), DOI: 10.1016/j.tcs.2018.02.014. https://doi.org/10.1016/j.tcs.2018.02.014
