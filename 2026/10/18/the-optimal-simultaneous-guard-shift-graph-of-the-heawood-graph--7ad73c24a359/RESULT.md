# The optimal simultaneous-guard shift graph of the Heawood graph is the complement of its line graph

## Finding

Let \(H\) be the point–line incidence graph of the Fano projective plane. Its minimum dominating sets form a family \(\mathcal D\) of exactly \(21\) four-vertex sets. Make a graph \(\mathcal B(H)\) on \(\mathcal D\), joining two distinct sets whenever a bijection takes each old guard either to its own vertex or to an adjacent vertex of \(H\). Then there is a natural isomorphism

\[
\boxed{\mathcal B(H)\cong\overline{L(H)}}.
\]

Here \(L(H)\) is the ordinary line graph of \(H\), whose vertices are the \(21\) incidence edges. In particular, \(\mathcal B(H)\) has \(21\) vertices, \(168\) edges, degree \(16\) at every vertex and diameter \(2\). Moreover every minimum dominating configuration wins the all-guards-move eternal domination game; thus \(\gamma_m^\infty(H)=\gamma(H)=4\). The isomorphism, not merely the domination-number equality or the already-known minimum-state count, is the main assertion.

## Assumptions and scope

All graphs are finite, simple and undirected. A dominating set \(D\subseteq V(H)\) contains or neighbors every vertex. A *simultaneous shift* from \(D\) to \(E\) is a bijection \(f:D\to E\) satisfying \(f(u)=u\) or \(uf(u)\in E(H)\) for every \(u\in D\). There is at most one guard per vertex. An attack occurs at an unoccupied vertex, and a response is a simultaneous shift to another dominating set containing the attacked vertex. A position is *eternally defensible* if every possible infinite attack sequence can be answered this way.

Let \(P\) be the seven points and \(\mathcal L\) the seven lines of the Fano plane; each point belongs to three lines, each line contains three points, and any two distinct points (respectively lines) determine exactly one line (respectively point). For an incident flag \((r,L)\), write \(\mathcal L(r)=\{K\in\mathcal L:r\in K\}\) and define

\[
D_{r,L}= (L\setminus\{r\})\ \cup\ (\mathcal L(r)\setminus\{L\}),
\]

understanding point vertices and line vertices as disjoint types. This has exactly two points and two lines.

## Proof

**1. Minimum configurations.** Every vertex of \(H\) has degree \(3\), so four guards are necessary since \(3\cdot4<14\). More precisely, a dominating four-set containing \(p\) point vertices and \(4-p\) line vertices covers at most \(p+3(4-p)\) point vertices and at most \((4-p)+3p\) line vertices. Both quantities must be at least \(7\), forcing \(p=2\). If the two selected points are \(a,b\), they dominate precisely five distinct line vertices: their incident line-sets intersect only in their unique joining line \(L\). Thus the other two line vertices must be precisely the two lines not through \(a\) or \(b\). Their unique meeting point \(r\) lies on \(L\) and is different from \(a,b\): if \(r\) were outside \(L\), the two lines joining \(r\) to \(a\) and \(b\) would be two of the three lines through \(r\), leaving only one line through \(r\) that avoids both selected points, contrary to the two missing lines. Consequently the four-set is \(D_{r,L}\). Conversely, \(D_{r,L}\) dominates every vertex: the two selected point vertices dominate every line except the two selected line vertices, while those two selected lines dominate the five unselected point vertices (the third point of \(L\) together with all four points outside \(L\)). The constructions are mutually inverse and give exactly \(7\cdot3=21\) minimum dominating sets.

**2. Which simultaneous shifts are impossible.** Suppose two distinct flags \((r,L)\) and \((s,M)\) share the point \(r=s\). Their selected point pairs are disjoint, because distinct lines through \(r\) meet only at \(r\). Neither source point guard can arrive at a target point (no point–point edges); of the two source line guards, only the line \(M\) is incident with either target point. Two target points cannot both be supplied by that one source guard. Hence no shift exists.

If instead \(L=M\) and \(r\ne s\), none of the source selected lines coincides with any target selected line: any common such line would contain both \(r\) and \(s\), forcing it to be \(L\), which is unselected as a line vertex. The source point pair is \(\{s,t\}=L\setminus\{r\}\). Both target selected lines contain \(s\) but not \(t\), because the only line through \(s,t\) is \(L\). Thus the one source point guard at \(s\) cannot supply both destination line guards. No shift exists in this case either.

**3. All other shifts exist.** Flags are transitive under automorphisms of the Fano plane: viewing points as one-dimensional subspaces and lines as two-dimensional subspaces of \(\mathbb F_2^3\), an invertible linear map sends any complete incident flag to any other. It therefore suffices to handle one source flag. Label points by \(0,\ldots,6\), label line \(L_j=\{j,j+1,j+3\}\pmod7\), and label its line vertex by \(7+j\). For source flag \((0,L_0)\), the source guards, in order, are \((1,3,11,13)\). In the following table the right-hand tuple gives the destinations of these four guards, respectively. For each row its four destinations form exactly \(D_{r,L_j}\); each source-to-destination pair is an identity or incidence edge. This is an explicit finite witness for every one of the sixteen flags with \(r\ne0\) and \(j\ne0\).

| Destination flag \((r,j)\) | Guard destinations, ordered from \((1,3,11,13)\) |
|---|---|
| \((1,1)\) | \((12,7,4,2)\) |
| \((1,5)\) | \((8,7,5,6)\) |
| \((2,1)\) | \((1,9,4,13)\) |
| \((2,2)\) | \((8,3,5,13)\) |
| \((2,6)\) | \((8,9,0,6)\) |
| \((3,2)\) | \((7,10,5,2)\) |
| \((3,3)\) | \((7,9,4,6)\) |
| \((4,1)\) | \((1,10,11,2)\) |
| \((4,3)\) | \((8,3,11,6)\) |
| \((4,4)\) | \((8,10,5,0)\) |
| \((5,2)\) | \((12,3,11,2)\) |
| \((5,4)\) | \((12,9,4,0)\) |
| \((5,5)\) | \((1,9,11,6)\) |
| \((6,3)\) | \((12,3,4,13)\) |
| \((6,5)\) | \((1,10,5,13)\) |
| \((6,6)\) | \((12,10,0,2)\) |

The two preceding steps show, for any *distinct* flags, that a shift is possible exactly when their point coordinates differ and their line coordinates differ. Two incidence edges of \(H\) are adjacent in \(L(H)\) exactly when they share a point or line endpoint. Identifying \(D_{r,L}\) with the incidence edge \(rL\) proves the boxed graph isomorphism. Every flag-edge in \(H\) meets exactly four other edges, so \(\mathcal B(H)\) has degree \(21-1-4=16\) and \(21\cdot16/2=168\) edges. Any two nonadjacent vertices of \(\mathcal B(H)\) share a neighbor: at most \(5+5=10\) of the \(21\) flags fail to be disjoint from at least one of their two flags. Thus the diameter is \(2\).

**4. Infinite defense, from every minimum configuration.** Fix \(D_{r,L}\). For an attacked point vertex \(v\notin D_{r,L}\), select a line \(M\ne L\) through \(v\) and a different point \(s\in M\) such that \(s\ne r\). Such a choice always exists: when \(v=r\), take either other line through \(r\); when \(v\ne r\), take a line through \(v\) avoiding \(r\). Then \(v\in D_{s,M}\), and the flags share neither point nor line coordinate, so the previous paragraph supplies a shift. For an attacked line vertex \(K\notin D_{r,L}\), choose \(s\in K\) with \(s\ne r\), then choose a line \(M\) through \(s\) different from both \(K\) and \(L\). This is possible because three lines pass through \(s\). Then \(K\in D_{s,M}\), and again both flag coordinates differ from the source, yielding a legal shift. Since the response is another minimum configuration to which the same rule applies, induction handles arbitrary finite prefixes and thus all infinite attack sequences. The domination lower bound gives \(\gamma_m^\infty(H)=4\).

## Verification

Two independent, dependency-free Python 3 programs accompany this result. `verify_cyclic.py` constructs the seven lines as translated difference sets and enumerates every dominating four-set and every guard-matching permutation; it checks the bijection, all \(168\) shift edges, the line-graph-complement identity, diameter \(2\), and winning responses to all attacks at all states. `verify_vectors.py` constructs Fano incidence using nonzero vectors of \(\mathbb F_2^3\), enumerates dominating sets with bit masks, and independently checks shifts using recursive matching, flag coordinates, and attack responses. Both finish with `VERIFY_OK`. Their outputs are stored separately. Computations are complete finite verification of this one graph, not a proof of an analogous claim for other projective planes or all vertex-transitive graphs. The sixteen listed moves are also independently checkable by hand from the displayed incidence convention.

## Relationship to prior work

Goddard, S. M. Hedetniemi and S. T. Hedetniemi (2005) introduced the all-guards-move eternal-security model and proved results for basic graph families; their claimed equality between eternal security and domination for all Cayley graphs was subsequently corrected. Braga, de Souza and Lee (2016) give an eighteen-vertex Cayley counterexample to that blanket assertion, and explain why the original argument fails. Neither article computes the simultaneous-shift graph of Heawood minimum-dominating configurations. Counting the \(21\) configurations is treated as background rather than as a priority claim. Carr, Clarke, MacGillivray and Morris (2026) prove equality for vertex-transitive graphs with an efficient dominating set, a hypothesis impossible here because \(14\) is not divisible by the closed-neighborhood size \(4\); their paper does not state the present configuration-graph identification. Published finite-object records on Heawood matchings and its graph complexes use different state spaces and transformations, so their conclusions do not imply this isomorphism.

## Limitations

The claim is restricted to the Fano-plane incidence graph and the precise simultaneous-shift rule; it does not classify single-moving-guard security, arbitrary numbers of guards, or other incidence graphs. The proof and independent programs justify the stated finite classification, but a lack of indexed matches cannot establish universal publication priority. An equivalent unpublished or unindexed enumeration is a residual originality risk. No independent external validation or audit has been performed.

## References

1. W. Goddard, S. M. Hedetniemi and S. T. Hedetniemi, “Eternal Security in Graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* **52** (2005). Author-uploaded full text: https://www.researchgate.net/publication/249799004_Eternal_Security_in_Graphs (public upload dated 2014-11-18).
2. A. Braga, C. C. de Souza and O. Lee, “A Note on the Paper ‘Eternal security in graphs’ by Goddard, Hedetniemi, and Hedetniemi (2005),” *J. Combin. Math. Combin. Comput.* **96** (2016), 13–22. https://combinatorialpress.com/jcmcc-articles/volume-096/a-note-on-the-paper-eternal-security-in-graphs-by-goddard-hedetniemi-and-hedetniemi-2005/ (dated 2016-05-31).
3. M. Carr, N. E. Clarke, G. MacGillivray and J. Morris, “Eternal domination in Cayley graphs,” arXiv:2607.04024 (2026), https://arxiv.org/abs/2607.04024.
