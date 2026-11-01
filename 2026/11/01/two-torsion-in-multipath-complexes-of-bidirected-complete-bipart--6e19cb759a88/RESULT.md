# Two-torsion in multipath complexes of bidirected complete bipartite graphs

## Finding

For \(n\ge 2\), let \(D_n=\overleftrightarrow{K_{2,n}}\) be the directed graph with hubs \(a,b\), leaves \(w_1,\ldots,w_n\), and both arcs between each hub and each leaf. Its *ordinary multipath complex* \(X(D_n)\) has one simplicial vertex for each arc; a collection is a face exactly when its arcs form a vertex-disjoint union of directed simple paths (isolated graph vertices are permitted). Then the **exact reduced integral homology** at the two specified parameters is

\[
\widetilde H_i(X(D_4);\mathbb Z)\cong
\begin{cases}
\mathbb Z^7\oplus\mathbb Z/2\mathbb Z,&i=2,\\
0,&i\ne2,
\end{cases}
\]

and

\[
\widetilde H_i(X(D_5);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&i=2,\\
\mathbb Z^{31},&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]

Furthermore, **each \(D_n\) is itself a single, unstable dynamical module** in the terminology of Caputi, Collari, Di Trani and Smith. Thus \(D_4\) (and independently \(D_5\)) is a counterexample to their conjecture that a dynamical module whose multipath complex has homology torsion must be stable. This statement is about simplicial homology of the multipath complex, *not* about path homology of a digraph or a matching complex of its underlying undirected graph.

## Assumptions and scope

The underlying graph \(K_{2,n}\) is simple and has exactly two hubs and \(n\) leaves. Each undirected edge supplies **two** oppositely directed arcs. The multipath condition forbids repeated incoming or outgoing arcs at every vertex and forbids **all** directed cycles, including directed digons. No graph contraction, quotient, or orientation change is performed.

The two integral-homology calculations are for the *finite* cases \(n=4\) and \(n=5\) only. The dynamical-module assertion holds for all integers \(n\ge2\); it is not an all-parameter homology computation. The word 'stable' refers to Definition 4.2 of the cited 2024 paper, not to a topological stability condition.

## Proof

**Step 1: every \(D_n\) is a nonstable dynamical module.** In the cited definition, a dynamical region \(R\) is connected, contains an arc, and obeys two conditions: a boundary vertex must be stable (source or sink) *within* \(R\), and any directed cycle of the ambient digraph meeting an arc of \(R\) must lie wholly within \(R\). Take any selected arc \(u\to v\) in a dynamical region of \(D_n\). Since \(u\to v\to u\) is a directed two-cycle, the reverse arc \(v\to u\) must also be in \(R\). Both endpoints are consequently unstable within \(R\) (their incoming and outgoing degrees are positive). Neither endpoint can be a boundary vertex, so all arcs incident to either endpoint must belong to \(R\). Repeating this forcing along the connected graph exhausts all arcs of \(D_n\). Therefore no proper nonempty dynamical region exists, and \(D_n\) is a minimal dynamical region, hence a module. Every vertex has positive incoming and outgoing degree, so this module is not stable.

**Step 2: construct the entire simplicial chain complexes.** Label the hubs \(0,1\), leaves \(2,\ldots,n+1\), and the \(4n\) arcs, for \(j=0,\ldots,n-1\), in the order

\[
0\to(j+2),\quad(j+2)\to0,\quad1\to(j+2),\quad(j+2)\to1.
\]

A subset of these arcs is a face if and only if its arcs have indegrees and outdegrees at most one and its successor function has no periodic orbit. All these tests are exact finite operations. Each chosen arc touches exactly one of the two hubs, and a hub supports at most one incoming and one outgoing chosen arc. Therefore **no face has more than four arcs**. Exhaustive enumeration of the \(\binom{4n}{k}\) subsets for \(0\le k\le4\) gives the face vectors:

| Complex | Vertices | Edges | Triangles | Tetrahedra | Total including empty |
|---|---:|---:|---:|---:|---:|
| \(X(D_4)\) | 16 | 80 | 144 | 72 | 313 |
| \(X(D_5)\) | 20 | 130 | 320 | 240 | 711 |

As a redundant arithmetic check, both enumerated vectors agree with the following polynomial expressions evaluated at \(n=4\) and \(n=5\):

\[
(f_0,f_1,f_2,f_3)
=\bigl(4n,\;6n^2-4n,\;4n(n-1)^2,\;n(n-1)^2(n-2)\bigr).
\]

**Step 3: compute the full *integer* boundary operators.** Use the ordered arc sets above to orient every simplex. For an ordered simplex \([e_0,\ldots,e_k]\), the signed boundary is

\[
\partial_k[e_0,\ldots,e_k]
=\sum_{j=0}^{k}(-1)^j[e_0,\ldots,\widehat e_j,\ldots,e_k].
\]

The checker constructs \(\partial_1,\partial_2,\partial_3\) on the complete unreduced integral simplicial chains and verifies \(\partial_1\partial_2=0\) and \(\partial_2\partial_3=0\). It calculates their Smith normal forms over \(\mathbb Z\), *not* just numerical ranks or field reductions:

| Complex | Nonzero Smith factors of \(\partial_1\) | of \(\partial_2\) | of \(\partial_3\) |
|---|---|---|---|
| \(X(D_4)\) | fifteen 1s | sixty-five 1s | seventy-one 1s, **one 2** |
| \(X(D_5)\) | nineteen 1s | one hundred eleven 1s | two hundred eight 1s, **one 2** |

Thus the rational ranks of \((\partial_1,\partial_2,\partial_3)\) are respectively \((15,65,72)\) and \((19,111,209)\). In the first case the respective matrix shapes are \(16\times80\), \(80\times144\), \(144\times72\); in the second case they are \(20\times130\), \(130\times320\), \(320\times240\). Every rank and Smith invariant is checked by execution of the attached source file.

**Step 4: pass from Smith forms to homology.** The torsion of the cokernel of \(\partial_3\) is the same as the torsion of \(H_2\). Indeed, the chain condition gives an exact sequence

\[
0\longrightarrow H_2\longrightarrow
C_2/\operatorname{im}\partial_3
\xrightarrow{\ \partial_2\ }
\operatorname{im}\partial_2\longrightarrow0,
\]

and \(\operatorname{im}\partial_2\) is a subgroup of a free abelian group, hence torsion-free. The single Smith factor 2 consequently produces exactly one \(\mathbb Z/2\mathbb Z\) summand of \(H_2\), with no other torsion. The ranks of \(H_1,H_2,H_3\) are obtained by subtracting adjacent differential ranks from chain ranks. They are \((0,7,0)\) for \(n=4\), and \((0,0,31)\) for \(n=5\). Finally, \(\operatorname{rank}\partial_1=f_0-1\) in each case, so both complexes are connected. All higher chains vanish. This proves the asserted complete integral homology groups.

## Verification

Run `python verify.py` with Python 3.10+ and the dependency pinned in `requirements.txt`. The checker requires no external data or network access. It constructs **all** simplices, verifies closure under face deletion, checks the independent counting formulas, constructs the **entire signed integral differentials**, checks boundary squared zero, and computes Smith normal forms exactly using SymPy's integer-domain implementation. As a separate check it performs bit-packed elimination over \(\mathbb F_2\), obtaining mod-two reduced Betti vectors \((0,8,1)\) and \((0,1,32)\) in degrees one, two and three. These agree with the universal coefficient theorem and the single two-torsion summand in degree two. The executable additionally checks the forced-arc closure used in the module argument for each starting arc.

All checks were executed successfully. This is an exhaustive finite computation for the two stated cases, not an experiment extrapolated to arbitrary \(n\), and does not depend on any previously generated verification logs or files.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith's *On the homotopy type of multipath complexes* explicitly proposes the above torsion-versus-stability conjecture immediately after its Theorem 1.1. The same paper defines dynamical regions and modules in Definitions 4.2 and 4.4. Its Section 3.2 treats the complete bipartite **one-way** orientation with arcs only from one part to the other, so its chessboard-complex formula does **not** apply to these bidirected graphs.

Caputi, Collari and Smith's January 2026 *Multipath complexes of bidirectional polygonal digraphs* establishes homology results for bidirected **paths and simple cycles**, and explains why the matching-complex blow-up comparison requires absence of directed cycles. Neither result determines the complete second integral homology of a bidirected \(K_{2,4}\) or \(K_{2,5}\). Caputi, Collari and Ramos's 2024 quiver-minor theorem bounds possible torsion exponents in bounded-genus families, but does not compute these two Smith forms or settle the stability conjecture.

Ordinary matching complexes, two-matching complexes, oriented one-way chessboard complexes and multipath complexes are different constructions; their torsion assertions do not automatically imply the present claim. The contribution is the **exact two-torsion in two naturally adjacent bidirected bipartite modules** and the resulting counterexample to a stated conjecture, not a claim of an all-width classification.

## Limitations

There is no claim about the homotopy type, homotopy groups, cup products, or arbitrary widths \(n\), beyond the module lemma. A Smith-form calculation determines integral homology and certifies nonzero torsion, but does not by itself identify a global homotopy decomposition. Literature coverage is bounded by accessible indexed sources; an unindexed equivalent computation cannot be ruled out. The verification uses exact external integer-algebra software (SymPy), independently cross-checked by mod-two elimination and signed chain identities; it is not independent expert review.

## References

1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first publicly posted 2026-01-09, https://arxiv.org/pdf/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656; *Mathematika* 70 (2024), e12235, https://doi.org/10.1112/mtk.12235. Open full text: https://irep.ntu.ac.uk/id/eprint/50523/1/1844094_Smih.pdf.
3. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1, https://arxiv.org/pdf/2401.01248.
