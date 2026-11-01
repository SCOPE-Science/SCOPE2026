# A sharp inclusion-collapse boundary in Mycielski-cycle higher independence

## Finding

Let \(G_n=\mu(C_n)\) be the ordinary Mycielskian of the cycle on \(n\) vertices. Write \(K_n=\operatorname{Ind}_1(G_n)\) and \(L_n=\operatorname{Ind}_2(G_n)\) for the simplicial complexes of, respectively, independent vertex sets and vertex sets whose induced connected components have at most two vertices.

**Theorem.** For each \(n\in\{3,4,5\}\), the canonical inclusion \(K_n\hookrightarrow L_n\) is the inclusion of a simplicial strong deformation retract: specifically, \(L_n\) admits a sequence of elementary simplicial collapses onto \(K_n\), using respectively \(12\), \(28\), and \(105\) elementary pairs. The first succeeding cycle length has a nontrivial and completely computed integral obstruction:

\[
H_j(L_6,K_6;\mathbb Z)\cong
\begin{cases}
\mathbb Z^6,& j=3,\\
0,&j\ne 3.
\end{cases}
\]

Therefore the inclusion \(K_6\hookrightarrow L_6\) is **not** a homotopy equivalence. In particular, at the five-cycle the complex \(L_5\) for the eleven-vertex Grötzsch graph has homotopy type \(S^2\); the sphere type of \(K_5\) itself was previously known and is not asserted as new. The theorem is restricted to these four explicitly stated cycle lengths; it does not claim a description for all larger lengths.

## Assumptions and scope

For each integer \(n\ge3\), define \(G_n\) explicitly on vertices \(v_0,\ldots,v_{n-1},u_0,\ldots,u_{n-1},w\), indices interpreted modulo \(n\), with edges

\[
\{v_i,v_{i+1}\},\qquad
\{u_i,v_{i-1}\},\qquad
\{u_i,v_{i+1}\},\qquad
\{w,u_i\},\qquad 0\le i<n.
\]

There are no additional edges, no loops and no duplicate edges. For every vertex set \(A\subseteq V(G_n)\), inclusion in \(K_n\) is equivalent to \(G_n[A]\) having maximum degree zero, while inclusion in \(L_n\) is equivalent to maximum degree at most one. This equivalence follows because every connected simple graph with maximum degree one is an isolated vertex or an edge. For \(n\ge4\) these complexes can also be written as devoid complexes \(\mathcal D(G_n;\{P_3\})\), with \(P_3\) meaning a three-vertex path as a **not-necessarily-induced** subgraph. The definition by components is used throughout, including the triangular base case \(n=3\).

All homotopy and homology statements use geometric realizations and integral simplicial chains. For the pair, \(C_*(L_n,K_n;\mathbb Z)\) is the quotient chain complex: its basis in degree \(d\) consists exactly of \((d+1)\)-vertex faces of \(L_n\) not in \(K_n\), and a boundary term lying in \(K_n\) becomes zero.

## Proof

**Finite exact collapse for the first three lengths.** Encode a face by a bitmask on the ordered vertex list \(v_0,\ldots,v_{n-1},u_0,\ldots,u_{n-1},w\), with bit index increasing left to right. The attached standard-library verifier constructs every subset for \(n=3,4,5,6\) and checks the maximum-degree membership predicate against an independent connected-component traversal.

To construct a matching on \(L_n\setminus K_n\), process vertex bits in the displayed order. At bit \(i\), among as-yet-unmatched relative faces, match every face \(F\) omitting \(i\) with \(F\cup\{i\}\) whenever both are still unmatched relative faces. Remove these two faces before processing the next bit. This is a fully defined deterministic rule, not a search for a desired Morse result.

For \(n=3,4,5\), exhaustive execution yields no unpaired relative faces. The matched pairs number \(12,28,105\), respectively. More strongly, the verifier explicitly constructs an ordering of these pairs in which, at every step, the lower face has the higher face as its **only remaining strict coface** of any dimension, and the upper face exceeds it by one vertex. Removing each pair is consequently an elementary simplicial collapse. At the end, exactly the original subcomplex \(K_n\) remains. This proves the asserted simple-homotopy equivalences, including compatibility with the actual natural inclusion, rather than merely an equality of Betti numbers.

The face counts (including the empty face in each complex) for \(n=3,4,5\) are, respectively, \((18,42)\), \((47,103)\), and \((103,313)\), ordered \((|K_n|,|L_n|)\). Thus the numbers of faces deleted are exactly twice the stated elementary pair counts. For \(n=5\), an additional acyclic toggle matching on the ordinary independence complex leaves only one unmatched two-dimensional face in its augmented face poset. Alternatively, the established ordinary-Mycielskian suspension theorem and \(\operatorname{Ind}_1(C_5)\simeq S^1\) give \(K_5\simeq S^2\). Either route together with the collapse gives \(L_5\simeq S^2\).

**The first nonzero relative complex.** For \(n=6\), complete enumeration gives \(254\) faces of \(K_6\) and \(866\) faces of \(L_6\), both counts including the empty face. The relative chain complex therefore has \(612\) basis faces. The same deterministic matching contains \(301\) pairs and leaves exactly ten critical faces. In dimensions \(3,4,5\), the critical counts are \(7,2,1\), with no others. Under the bit-order encoding above, the sorted critical face masks are

\[
\begin{array}{c|l}
3&154,308,360,801,1539,2092,3078\\
4&936,2664\\
5&3016
\end{array}
\]

A complete topological sort of the Hasse digraph, with the matching incidences reversed, visits all \(612\) relative faces. Hence the matching is acyclic. Every original oriented boundary coefficient is computed by deleting bit \(i\) with coefficient \((-1)^q\), where \(q\) is the number of smaller retained bits. The program then performs the standard integral algebraic Morse elimination of the \(301\) matched incidence pairs, checking that **every eliminated pivot is a unit** in \(\mathbb Z\), that the chain identity \(\partial^2=0\) holds before and after elimination, and that no unaccounted critical faces remain. These are exact integer operations; no floating-point rank tests are involved.

With the listed critical bases, the surviving differentials are exactly

\[
\partial_4=
\begin{pmatrix}
0&0\\0&0\\1&1\\1&1\\0&0\\-1&-1\\0&0
\end{pmatrix},
\qquad
\partial_5=\begin{pmatrix}1\\-1\end{pmatrix}.
\]

The two columns of \(\partial_4\) equal a primitive vector \(a=(0,0,1,1,0,-1,0)^T\). Therefore \(\operatorname{coker}\partial_4\cong\mathbb Z^6\), with **no torsion**, and \(\ker\partial_4=\mathbb Z(1,-1)=\operatorname{im}\partial_5\). Because \(\partial_5\) is injective, all other relative homology groups are zero. This proves the claimed full integral relative homology and the failure of equivalence at \(n=6\).

## Verification

Run `python3 verification/check.py` with a standard Python 3 interpreter. No downloaded data, nonstandard packages, random input, or network access are needed. The script must complete with `ALL_CHECKS_PASS`; its canonical text output is saved at `verification/output.txt`.

Independent checks include: two separately implemented face predicates evaluated on every one of the \(2^{2n+1}\) possible vertex subsets for each of the four lengths; direct verification of every elementary free-face removal for \(n\le5\); acyclicity of the relative Hasse digraph for every length; unit-pivot integral chain cancellation for \(n=6\); and a separate mod-two rank computation from the unreduced original relative simplicial boundary matrices. For \(n=6\), the latter gives relative mod-two Betti number \(6\) in degree \(3\) and zero in all other degrees, consistent with—but not a substitute for—the integral calculation.

## Relationship to prior work

Taylan's 2015 full-text treatment of graph devoid complexes gives the general framework \(\mathcal D(G;\mathcal F)\), elementary matching tools, and explicit classifications for **paths, cycles, and forests**, but does not identify the collapse boundary for the cyclic Mycielski family or its relative integral obstruction. In the triangle-free cases here, \(\operatorname{Ind}_2(G_n)=\mathcal D(G_n;\{P_3\})\); the base graph \(G_n\) is neither a simple cycle nor a forest.

Paolini and Salvetti's work develops higher independence complexes in the context of Artin groups. Deshpande and Singh give homotopy classifications for several other graph families, including cycles, paths, fully whiskered graphs and multipartite graphs. Neither inspected work states the present canonical inclusion-collapse/relative-homology theorem. Goyal, Shukla and Singh prove the ordinary-Mycielskian suspension phenomenon; their result and Carnero Bravo's later generalization determine ordinary independence homotopy information but not the interaction of ordinary and two-independence complexes under the **natural inclusion**. Thus the previously known \(K_5\) sphere homotopy type is used only as an input to the new statement about \(L_5\).

## Limitations

The collapse is proven only for \(n\in\{3,4,5\}\), and the obstruction is calculated at \(n=6\); no statement about all \(n\ge6\) is made. The proof does not classify the absolute homotopy type of \(L_6\), nor the integral homotopy group of any quotient. Exhaustive computation is used only on the four explicitly bounded finite instances. No claim of an independent external mathematical review or exhaustive publication-priority determination is made.

## References

1. Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type Of Devoid Complexes Of Graphs*, arXiv:1501.06754, first submitted January 27, 2015. https://arxiv.org/html/1501.06754v1
2. Giovanni Paolini and Mario Salvetti, *Weighted sheaves and homology of Artin groups*, arXiv:1703.02586, first submitted March 2017. https://arxiv.org/abs/1703.02586
3. Shuchita Goyal, Samir Shukla, Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, first submitted May 16, 2019. https://arxiv.org/abs/1905.06926
4. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first submitted January 15, 2020. https://arxiv.org/abs/2001.05448
5. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432, first submitted January 19, 2026. https://arxiv.org/abs/2601.13432
