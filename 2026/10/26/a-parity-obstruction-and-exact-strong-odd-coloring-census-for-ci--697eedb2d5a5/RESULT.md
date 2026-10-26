# A parity obstruction and exact strong-odd coloring census for circular prisms

## Finding
For each integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the ordinary circular prism with labeled vertices \((i,r)\), \(i\in\mathbb Z/n\mathbb Z\), \(r\in\{0,1\}\). A **strong odd coloring** is a proper vertex coloring in which every color appearing in a vertex's open neighborhood appears there an odd number of times. Its minimum palette size is \(\chi_{\mathrm{so}}\). Then
\[
\chi_{\mathrm{so}}(P_n)=
\begin{cases}
6,&n=3,\\
2,&n\ge4\text{ even},\\
5,&n\ge5\text{ odd}.
\end{cases}
\]
More sharply, for each integer \(n\ge3\), the number \(A_n(4)\) of strong odd colorings using an **available, named palette of four colors** (not necessarily all used) is
\[
A_n(4)=12\mathbf1_{2\mid n}+24\mathbf1_{4\mid n}+48\mathbf1_{6\mid n}.
\]
Every such coloring has either two or four colors actually used; there are no three-color strong odd colorings of a circular prism. Indeed, the entire four-palette transition graph consists of six directed \(2\)-cycles, six directed \(4\)-cycles, and eight directed \(6\)-cycles.

The **complete number of optimal colorings on named palettes** is two for even \(n\ge4\), and \(6!=720\) for \(n=3\). For odd \(n\ge5\), it is exactly \(\operatorname{tr}(T_5^n)\), where the explicit \(260\)-state zero-one transfer matrix \(T_5\) is defined below. Thus every optimal coloring is counted, not only one witness. The first odd counts, for \(n=5,7,9,11\), are respectively \(240,1680,18000,171600\).

## Assumptions and scope
The two layers and all cyclic positions are individually labeled. There is no quotient by graph automorphisms or palette permutations. A palette of size \(q\) consists of \(q\) named symbols; "using a palette" permits unused colors, whereas "optimal" means exactly \(\chi_{\mathrm{so}}\) colors. The cycle \(C_3\) is a triangle (no parallel edges). Throughout, \(n\ge3\) and all graphs are finite, simple, and undirected.

Write column \(i\) of a coloring as \(x_i=(a_i,b_i)\), top and bottom. Because the graph is cubic, the strong odd condition at a vertex means its three neighbor colors are either **all equal** or **pairwise distinct**. For any palette \(Q\) of size \(q\), let \(\mathcal C_q=\{(a,b)\in Q^2:a\ne b\}\), and
\[
\mathcal S_q=\{(x,y)\in\mathcal C_q^2:x_0\ne y_0,\ x_1\ne y_1\}.
\]
Here \(x_0,x_1\) denote the two color coordinates of a column. For consecutive columns \(x,y,z\), define a transition \((x,y)\to(y,z)\) precisely when
\[
z_0\ne y_0,\quad z_1\ne y_1,\quad
|\{x_0,z_0,y_1\}|\in\{1,3\},\quad
|\{x_1,z_1,y_0\}|\in\{1,3\}.
\]
Let \(T_q\) be the zero-one adjacency matrix of these directed transitions, with rows and columns indexed by \(\mathcal S_q\). In particular, \(|\mathcal S_4|=84\) and \(|\mathcal S_5|=260\). For all \(q\ge2\), cyclic compatibility gives the exact identity \(A_n(q)=\operatorname{tr}(T_q^n)\) (no normalization), valid at \(n=3\) as well.

## Proof
**(1) The transfer equivalence.** Properness says \(a_i\ne b_i\), \(a_i\ne a_{i+1}\), \(b_i\ne b_{i+1}\). At \((i,0)\) the neighbor colors are \(a_{i-1},a_{i+1},b_i\); at \((i,1)\) they are \(b_{i-1},b_{i+1},a_i\). Each triple is strong odd exactly when it has one or three distinct entries. Consequently an admissible cyclic column word is equivalent, with no multiplicity, to a length-\(n\) closed walk in the graph of \(T_q\). This proves the trace identity, including the wraparound constraints.

**(2) Four-color periodicity and count.** The allowed pairs of consecutive columns over \(Q=\{0,1,2,3\}\) fall into four classes under simultaneous permutation of the four colors: \(x_0=y_1\) and \(x_1=y_0\) (12 states); exactly the first equality (24 states); exactly the second (24 states); or neither (24 states). For every state there is exactly one admissible successor. The following complete orbit-representative table lists the columns of one periodic successor trajectory for each class, in cyclic order:

| Representative class | Entire periodic column word | Period |
|---|---|---|
| Both equalities | \((0,1),(1,0)\) | \(2\) |
| Only \(x_0=y_1\) | \((0,1),(2,0),(0,3),(1,0),(0,2),(3,0)\) | \(6\) |
| Only \(x_1=y_0\) | \((0,1),(1,2),(3,1),(1,0),(2,1),(1,3)\) | \(6\) |
| Neither equality | \((0,1),(2,3),(1,0),(3,2)\) | \(4\) |

The assertion about unique successors is checked directly for these four representatives from the two conditions in the displayed transition definition. Uniqueness then holds for all \(84\) states by color-permutation equivariance. Repeatedly applying the same rule gives the displayed cycles. In the middle two rows the two three-symbol starting-state classes belong to the same six-cycle families. Therefore the \(12\), \(48\), and \(24\) states form respectively \(6\) cycles of length \(2\), \(8\) of length \(6\), and \(6\) of length \(4\). No cycles of odd length exist. A directed cycle of length \(\ell\) contributes \(\ell\) closed walks of length \(n\) if \(\ell\mid n\) and none otherwise. This proves \(A_n(4)\) exactly. The table also shows that two-symbol cycles use exactly two colors, and the other cycles use all four. A coloring with at most three colors is among the four-palette colorings; hence none uses exactly three.

**(3) Upper bounds.** A proper two-coloring of a connected prism exists exactly when \(n\) is even. When \(n\) is even, every vertex has three neighbors in its opposite bipartition color, so this coloring is strong odd; exactly two named optimal colorings result.

For the odd case, use five symbols \(\{0,1,2,3,4\}\). Each of the following is a cyclic admissible column word, all beginning with the same first two columns:
\[
\begin{aligned}
W_4={}&((0,1),(2,3),(1,0),(4,2)),\\
W_5={}&((0,1),(2,3),(4,0),(1,2),(3,4)),\\
W_7={}&((0,1),(2,3),(4,0),(3,1),(2,4),(1,0),(3,2)).
\end{aligned}
\]
This can be verified by checking successive triples of columns and the cyclic seam against the transition rule. Each word is a closed directed walk based at the same state \(((0,1),(2,3))\); therefore such walks may be concatenated at that state. Every odd \(n\ge5\) is \(5+4t\) or \(7+4t\) for some integer \(t\ge0\). Concatenate the corresponding length-five or length-seven walk with \(t\) copies of the length-four walk. This gives a five-color strong odd coloring for every odd \(n\ge5\).

**(4) Matching lower bounds and the small exception.** For odd \(n\ge5\), the absence of all odd-length closed walks in the four-palette transition graph excludes every coloring with four or fewer colors. Thus the construction in (3) proves the sharp value five. For \(n=3\), the top and bottom triangles are both cliques and every pair of vertices in the triangular prism is at graph distance at most two. Each of the three neighbors of any vertex must have distinct colors: its two same-layer neighbors are adjacent and hence cannot both match the third. Consequently every two vertices at distance at most two have different colors, so all six vertices require six different colors. Conversely six different colors plainly work, giving \(6!\) named optimal colorings.

**(5) Optimal-coloring census.** When \(n\ge5\) is odd, no coloring with fewer than five colors exists, so all admissible five-palette colorings automatically use all five colors. By (1) their number is exactly \(\operatorname{tr}(T_5^n)\), a fixed finite-matrix formula uniform in \(n\). The other two cases are counted in (3) and (4). The supplied independent verifier constructs the matrix directly from the rule and calculates the first values by exact integer arithmetic.

## Verification
Run `python3 verify.py` using standard-library Python. The program exhaustively enumerates all \(84\) legal two-column four-palette states and all their successors, verifies that they form a permutation with the claimed \(2\)-, \(4\)-, and \(6\)-cycle inventory, and checks every transition of the three five-color template words. It also constructs concatenated closed walks for odd lengths through \(99\) and checks vertex-level strong odd coloring directly. Exact transfer-matrix trace counts are independently compared with a separate direct vertex-assignment backtracker for palette sizes \(4,5\) and selected sizes \(n=3,4,5,7\). The general result does not depend on extrapolation from those bounded calculations: its infinite portions follow from the four representative transition rules and the concatenable explicit words.

## Relationship to prior work
Kwon and Park (first public preprint 22 January 2024) introduced strong odd coloring, distinguishing it from ordinary odd coloring and square coloring. Caro, Petruševski, Škrekovski and Tuza (first public preprint 3 October 2024) studied unicyclic graphs, claw-free graphs and graph products, proving general submultiplicative upper bounds under Cartesian products. Their product inequality does not supply the exact odd/even prism transition, a complete classification of four-palette circular-prism colorings, or the optimal-coloring enumerator. Previous exact results for **open** two-row ladders have endpoint constraints and do not cover the cyclic seam; results for Möbius ladders concern twisted, rather than ordinary, prisms. The four-palette obstruction and the odd-prism witness gluing are independent cyclic analyses.

## Limitations
The five-palette optimal-coloring count is presented as an exact \(260\)-state transfer-matrix formula, not a simplified scalar closed form. The novelty comparison is limited to the explicitly inspected literature and available searchable research records; an unindexed or differently named earlier prism result remains a priority risk. No independent mathematical audit has been performed. The verification code checks finite instances and the finite local transition lemma; it is not a proof of any untested general algebraic identity.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, first submitted 22 January 2024. https://arxiv.org/abs/2401.11653
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336v1, submitted 3 October 2024, especially Sections 1, 2 and 4. https://arxiv.org/html/2410.02336v1
