# Exact six-cycle-switch distances between labeled Steiner triple systems of order nine

## Finding
Let \(V=\{0,1,\ldots,8\}\). A Steiner triple system of order nine is a collection \(\mathcal B\subseteq\binom{V}{3}\) in which each unordered pair of points lies in exactly one block. A **six-cycle switch** has the precise definition given below. Let \(d_6(\mathcal B,\mathcal C)\) be the minimum number of such switches required to transform one labeled system into another, with labels fixed throughout, and put \(c(\mathcal B,\mathcal C)=|\mathcal B\cap\mathcal C|\).

**Exact-distance theorem.** For every ordered pair \((\mathcal B,\mathcal C)\) of Steiner triple systems on the same labeled nine-point set,
\[
d_6(\mathcal B,\mathcal C)=
\begin{cases}
0,&c=12,\\
1,&c=6,\\
2,&c\in\{2,3,4\},\\
3,&c\in\{0,1\}.
\end{cases}
\]
These are all possible intersection sizes. In particular, the six-cycle-switch graph has 840 vertices, is 36-regular with 15,120 undirected edges, and has **radius and diameter three**. Every vertex has exactly \(1,36,395,408\) vertices at distances \(0,1,2,3\), respectively. The novelty asserted here is the exact metric-by-intersection formula and resulting sharp diameter, **not** the previously known 840 realizations or their connectivity.

The full intersection/distance table from any fixed system is:

| Common blocks \(c\) | Systems at this intersection | Switch distance |
| ---: | ---: | ---: |
| 12 | 1 | 0 |
| 6 | 36 | 1 |
| 4 | 27 | 2 |
| 3 | 152 | 2 |
| 2 | 216 | 2 |
| 1 | 216 | 3 |
| 0 | 192 | 3 |

## Assumptions and scope
The points are **labeled**. Identifying systems up to isomorphism would collapse all 840 vertices into one class and give a different, degenerate graph. Each system has twelve blocks. Given distinct points \(a,b\), write \(\{a,b,t\}\in\mathcal B\) for their unique common block. On the other six points, consider the two perfect matchings whose edges \(\{x,y\}\) satisfy \(\{a,x,y\}\in\mathcal B\) and \(\{b,x,y\}\in\mathcal B\), respectively. These matchings have no common edge. Hence their union is an alternating simple six-cycle: a two-cycle would violate the Steiner pair property, and a cycle of length four would leave an impossible two-cycle. The **six-cycle switch** interchanges \(a\) and \(b\) in all six blocks through just one of \(a,b\); equivalently it globally transposes the labels \(a,b\) in the system. The shared block \(\{a,b,t\}\) is unchanged. There are no restrictions on intermediate labeled systems beyond being Steiner triple systems.

## Proof
**1. Identify all possible configurations.** The standard affine system \(\mathcal A\) consists of the twelve lines in \(\mathbb F_3^2\): all triples \(\{u,u+d,u+2d\}\) for a nonzero direction \(d\), with the four direction classes \((1,0),(0,1),(1,1),(1,2)\). There are 84 possible three-subsets and 36 pair-coverage constraints. The exhaustive exact-cover search in `verify_exact_cover.py` chooses the first as-yet-uncovered pair, branches over all triples containing it, and never permits a pair to be covered twice. Thus it lists **every** labeled Steiner triple system, without using a classification theorem. Its 8,863 recursive nodes produce exactly 840 distinct solutions. Independently, `verify_affine_cosets.py` obtains 840 distinct images of \(\mathcal A\) under permutations of the nine labels; each is a valid Steiner triple system. Therefore these two complete sets coincide, so the relabeling action is transitive.

**2. Identify the switch metric with a permutation-coset metric.** As shown in the definition, each six-cycle switch is exactly a transposition of two point labels and every transposition is such a switch. The stabilizer of \(\mathcal A\) is
\[
H=\operatorname{AGL}(2,3)=\{u\mapsto Mu+t: M\in\operatorname{GL}(2,3),\ t\in\mathbb F_3^2\},
\]
with \(|H|=9(3^2-1)(3^2-3)=432\); the orbit has \(9!/432=840\) systems and therefore no additional stabilizer elements exist. If \(\mathcal C=\pi\mathcal A\), every permutation taking \(\mathcal A\) to \(\mathcal C\) is in the right coset \(\pi H\). The least number of arbitrary transpositions expressing a permutation \(\sigma\in S_9\) is \(9-\operatorname{cyc}(\sigma)\), where fixed points count as cycles. Indeed, each transposition changes cycle count by one, and splitting nontrivial cycles achieves the bound. Consequently
\[
d_6(\mathcal A,\pi\mathcal A)=\min_{h\in H}\bigl(9-\operatorname{cyc}(\pi h)\bigr).
\]
This identity is exact and includes the lower-bound direction; it is not a heuristic search over paths.

**3. Evaluate the finite coset identities completely.** `verify_affine_cosets.py` generates all 432 affine permutations explicitly from the 48 invertible two-by-two matrices over \(\mathbb F_3\) and nine translations. It iterates over all \(9!=362,880\) permutations to obtain the 840 cosets, determines the twelve-block image and its common-block count, and takes the above minimum over every one of the 432 stabilizer elements for each coset. The resulting pair \((c,d_6)\) has precisely the seven rows displayed under **Finding**. Each loop bound is explicit and finite. This proves the complete shortest-distance formula from \(\mathcal A\).

**4. Extend to all pairs and cross-check exhaustively.** The relabeling action preserves common-block counts and switches, and is transitive on configurations by Step 1. Applying an inverse relabeling to any first system reduces its pair to the preceding calculation. As a logically independent check, `verify_exact_cover.py` constructs adjacency solely by a six-common-block comparison after its exact-cover generation, then performs breadth-first searches from **all 840** roots, verifying the distance formula against **all 705,600 ordered pairs**. The graph-adjacency test is valid because the coset calculation gives 36 distinct transposition neighbors and the exact-cover enumeration finds exactly 36 six-common-block neighbors per vertex. In particular, every such neighbor must be a legal six-cycle switch.

**5. Sharpness.** Disjoint systems exist (192 from any one root) and have distance three by the certified table. For a direct example, on the coordinate labeling \((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)\), the successive label transpositions \((0\ 1)\), \((2\ 4)\), \((3\ 6)\) produce systems with respectively six, two, and zero blocks in common with \(\mathcal A\). The first two swaps alone cannot reach the last system since all disjoint targets have certified distance three. Thus the diameter cannot be two. Every distance layer is nonempty, so radius is also three.

## Verification
The attached standard-library-only scripts `verify_exact_cover.py` and `verify_affine_cosets.py` use distinct mathematical models. Run from a directory containing the two scripts with `python3 verify_exact_cover.py` and `python3 verify_affine_cosets.py`. The corresponding recorded standard outputs are `verify_exact_cover.out` and `verify_affine_cosets.out`. Both were executed directly and their outputs reproduced exactly after package extraction. The first script verifies all root-to-target shortest paths by BFS; the second verifies an exact group-theoretic minimization for every coset. The programs constitute finite exhaustive proofs together with Steps 1–4, not a claim about unexamined orders.

## Relationship to prior work
The existence and uniqueness up to isomorphism of \(\operatorname{STS}(9)\), its affine structure, and the intersection-size spectrum are classical. Grannell, Griggs and Murphy [1, Theorem 4, pp. 5–6 of the author preprint] **already proved** that the labeled six-cycle-switch graph \(R(9,6)\) is connected, gave the transposition interpretation, and recorded its 840 vertices. Thus neither connectivity nor order nor the switching definition is claimed to be new. Lindner and Rosa's intersection theorem, stated in [2, Theorem 2.1], gives the possible numbers of shared blocks for order nine, but does not distinguish shortest switch distances. Khosrovshahi and Maimani [3] classify individual small trades, rather than the shortest-path metric in the labeled switching graph. Later published work [4] treats switching on order-nineteen systems, with different objects and parameters.

The present exact **intersection-to-distance function**, including its three-step obstruction for zero or one shared block, is not a corollary of the previously published connectivity assertion and intersection possibilities alone. The nearest older complete proof [1] was inspected directly. No literature search proves publication priority; unknown equivalent calculations, especially for the coset graph of \(S_9\) modulo \(\operatorname{AGL}(2,3)\), remain possible.

## Limitations
The theorem concerns only **nine** labeled points and precisely six-cycle switches. It does not establish analogous formulas for systems of larger order, other trade types, or isomorphism-class switching graphs. The proof invokes an explicitly exhaustive finite evaluation of 840 cosets (cross-checked by exact cover and all-roots BFS); it is not a symbolic all-order formula. Priority remains subject to alternative terminology or unindexed sources. Independent external scientific validation has not been performed.

## References
1. M. J. Grannell, T. S. Griggs and J. P. Murphy, *Switching cycles in Steiner triple systems*, Utilitas Mathematica **56** (1999), 3–21. Author's full preprint: https://grannell.net/Papers/SWITCH2.pdf.
2. Y. M. Chee, A. C. H. Ling and H. Shen, *The fine intersection problem for Steiner triple systems*, arXiv:0807.2500 (first posted 2008-07-16), §2, Theorem 2.1, quoting the classical theorem of C. C. Lindner and A. Rosa. https://arxiv.org/abs/0807.2500.
3. G. B. Khosrovshahi and H. R. Maimani, *On 2-(v,3) Steiner trades of small volumes*, Ars Combinatoria **52** (1999), 199–220. https://combinatorialpress.com/article/ars/Volume%20052/volume-52-paper-17.pdf.
4. G. Erskine and T. S. Griggs, *Cycle switching in Steiner triple systems of order 19*, Journal of Combinatorial Designs **33** (2025), 195–204, doi:10.1002/jcd.21975.
