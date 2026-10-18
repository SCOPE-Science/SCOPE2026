# A self-centered token-sliding graph of near-maximum maximal independent sets in odd Möbius ladders

## Finding

For every odd integer \(n\ge5\), let \(M_{2n}\) be the graph with vertex set \(\mathbb Z/(2n)\), joining \(i\) to \(i-1\), \(i+1\), and \(i+n\) modulo \(2n\). Let \(\mathcal R_n\) have as its vertices the maximal independent sets of cardinality \(n-2\) in \(M_{2n}\). Two such sets are adjacent when one occupied vertex is moved along a graph edge to an unoccupied vertex and the resulting set is again maximal independent.

The following are exact, for every odd \(n\ge5\).

1. \(\mathcal R_n\) is isomorphic to the cyclic interval-endpoint graph on \((a,b)\in\mathbb Z/n\times\{1,\ldots,n-3\}\), with edges \((a,b)\)--\((a,b+1)\) and \((a,b)\)--\((a-1,b+1)\) for \(b<n-3\), together with their reverses. All coordinates \(a\) are modulo \(n\).
2. The graph is connected, Eulerian, and bipartite. It has \(n(n-3)\) vertices and \(2n(n-4)\) edges. Its two boundary layers together have \(2n\) vertices of degree two; its interior has \(n(n-5)\) vertices of degree four. For \(n=5\), it is the ten-cycle.
3. For two interval vertices \((a,b)\), \((c,d)\), choose integer representatives of \(a,c\). The exact token-slide distance is
   \[d_{\mathcal R_n}((a,b),(c,d))=\min_{q\in\mathbb Z}\bigl(|c-a+qn|+|c-a+d-b+qn|\bigr).\]
4. Every vertex has eccentricity \(n\), and therefore the radius and diameter are both exactly \(n\). In particular, for every odd \(n\ge7\), this gives a connected, nonregular, self-centered state graph.

The vertex-count formula is not asserted as new; it also follows from an earlier graded enumeration of independent dominating sets of Möbius ladders. The new structural assertion is the complete legal-slide graph, its shortest-path metric, and its uniform eccentricity.

## Assumptions and scope

Throughout, \(n\) is odd and \(n\ge5\). Independent sets are *maximal by inclusion*, equivalently they dominate the graph. All intermediate configurations in a path must be maximal independent sets of exactly \(n-2\) vertices. A token slide replaces one occupied vertex by a neighbor; simultaneous replacement, token jumping, and intermediate nonmaximal sets are not allowed. Reconfiguration vertices are labelled sets, not orbits under graph automorphisms. Let \(h=(n-1)/2\), viewed modulo \(n\), and define the two bipartition classes
\[O_t=2(ht\bmod n)+1,\qquad E_s=2(h(s-1)\bmod n),\qquad s,t\in\mathbb Z/n.\]
As labels of vertices, \(O_t\) and \(E_s\) refer to residues modulo \(2n\). Since \(\gcd(h,n)=1\), both lists are bijections onto the odd and even vertices, respectively.

## Proof

**Bipartite interval coordinates.** Each even vertex \(E_s\) is adjacent to precisely \(O_{s-1}\), \(O_s\), \(O_{s+1}\). The first and last edges arise from the original cyclic rim, and the middle edge from the antipodal rung, using \(2h=n-1\). Let \(B\) be the indices of the selected odd vertices, and \(A\) those of the selected even vertices. Independence says \(A\cap N(B)=\varnothing\), where \(N(B)=B+\{-1,0,1\}\) modulo \(n\). Maximality forces \(A=(\mathbb Z/n)\setminus N(B)\), because every unselected even vertex having no selected odd neighbor could otherwise be added. Thus \(n-2=|B|+n-|N(B)|\), so \(|N(B)|-|B|=2\). The set \(B\) cannot be empty; nor can it have size at least \(n-2\), since then either its cardinality exceeds \(n-2\) or the unselected odd vertices have no selected even neighbor. Write \(b=|B|\), so \(1\le b\le n-3\).

List the nonempty complement gaps after successive members of \(B\) around the cyclic \(n\)-gon, with lengths \(g_1,\ldots,g_r\) (where each \(g_i\ge1\)). A gap of length \(g_i\) contributes exactly \(\min(g_i,2)\) elements to \(N(B)\setminus B\). Because the complement has \(n-b\ge3\) points and the contribution sum is two, there can be only one gap, of length at least three: two gaps would require either a contribution at least three or total complement length two. Hence \(B\) is one cyclic interval \([a,a+b-1]\), with \(1\le b\le n-3\), and
\[N(B)=[a-1,a+b],\qquad A=(\mathbb Z/n)\setminus[a-1,a+b].\]
Here bracketed intervals are cyclic consecutive residues with the displayed lengths. Conversely, every such \(B\) and \(A\) is independent and maximal: every omitted even vertex is adjacent to a selected odd vertex; each omitted odd vertex is in \([a+b,a-1]\): the first is adjacent to \(E_{a+b+1}\), the last to \(E_{a-2}\), and each intervening odd vertex \(O_t\) is adjacent to the selected \(E_t\). Because \(n-b\ge3\), both endpoint even vertices exist (they coincide only when \(n-b=3\)). Therefore all configurations are uniquely
\[S_{a,b}=\{O_a,\ldots,O_{a+b-1}\}\cup\{E_s:s\notin[a-1,a+b]\}.\]
There are exactly \(n\) states in each of the \(n-3\) layers.

**Allowed movements.** A token slide in a bipartite graph changes the number \(b\) of selected odd vertices by exactly one. Because the odd-selected indices must remain a single interval, increasing \(b\) can only extend its left or right endpoint. Extending right from \((a,b)\) to \((a,b+1)\) replaces \(E_{a+b+1}\) by \(O_{a+b}\). Extending left to \((a-1,b+1)\) replaces \(E_{a-2}\) by \(O_{a-1}\). These are graph edges in the original ladder and they are present precisely when \(b<n-3\). Their inverses describe all decreases in \(b\). This proves the stated isomorphism without relying on enumeration.

Each consecutive pair of layers induces one cycle of length \(2n\): alternating between \((a,b)\) and \((a,b+1)\), the other edge shifting \(a\) one step. Thus adjacent layers and therefore their union are connected. Every interior vertex has two edges upward and two downward, and each boundary vertex has degree two. Summing degrees gives \(2n(n-4)\) edges. All degrees are even; parity of \(b\) gives a bipartition, proving the stated properties.

**Exact geodesics.** Lift the cyclic coordinate \(a\) to \(A\in\mathbb Z\) and represent \((a,b)\) by the endpoint pair \((L,R)=(A,A+b-1)\). The integer strip \(1\le R-L+1\le n-3\) encodes all interval configurations before reduction modulo the diagonal translation \((L,R)\mapsto(L+n,R+n)\). Every edge increases or decreases precisely one of \(L,R\) by one, within the strip. Hence a path between two chosen lifts has length at least the Manhattan distance \(|L'-L|+|R'-R|\). Conversely, such a geodesic always exists inside the strip. When desired coordinate changes have opposite signs, choosing either coordinate order that moves the width toward its target keeps the width between its two valid endpoint values. When they have the same sign, alternately perform an available desired unit change so that the width stays within the strip: at the lower boundary the change increasing the width must be taken, and at the upper boundary the one decreasing it must be taken; because the final point is also in the strip, a required move of that kind is always available until completion. Thus the lifted distance is exactly the Manhattan distance. Taking the minimum over the target lifts \((c+qn,c+qn+d-1)\) establishes the displayed formula.

**Radius and diameter.** Put \(\delta=d-b\) and choose a target lift whose start displacement \(t=c-a+qn\) belongs to \(\{0,1,\ldots,n-1\}\). Since \(|\delta|\le n-4\), the minimum of the two admissible nearby lifts satisfies \(\min(|t|+|t+\delta|,|t-n|+|t-n+\delta|)\le n\). To see this, for \(\delta\ge0\), if \(t+\delta\le n\) the two displayed expressions sum to \(2n\); otherwise the second is \(\delta<n\). For \(\delta<0\), if \(t+\delta\ge0\) the two sum to \(2n\); otherwise the first is \(-\delta<n\). Hence every distance is at most \(n\).

For any source \((a,b)\), select \(d=b+1\) if \(b<n-3\) and \(d=b-1\) otherwise. In the first case choose \(c-a\equiv(n-1)/2\pmod n\); in the second choose \(c-a\equiv(n+1)/2\pmod n\). In each case the two nearest diagonal lifts have Manhattan distance exactly \(n\), and every other lift has larger distance. Therefore each source has a vertex at distance \(n\). Combined with the universal upper bound, every eccentricity equals \(n\). This proves the theorem.

## Verification

Two standalone, differently structured programs accompany the finding. `verification/verify_direct.py` recursively enumerates all maximal independent \((n-2)\)-sets in the original labelled graph for odd \(n=5,7,9,11,13,15\), independently constructs actual slides, and checks the interval isomorphism, layer degrees, connectivity, and eccentricities. `verification/verify_metric.py` separately enumerates actual sets via combinations for odd \(n=5,7,9,11\), then independently reconstructs the interval graph and compares the displayed formula against *every ordered vertex pair* for odd \(n=5,7,9,11,13,15,17,19,21,25\). Both output `VERIFY_OK` and their results are embedded as text. Exhaustive checks establish only those finite cases; the proof above supplies the infinite quantifiers.

## Relationship to prior work

Bonsma, Kamiński, and Wrochna study token sliding on independent sets with structural conclusions for claw-free host graphs; the odd Möbius ladders here are cubic with induced claws, and our moves additionally preserve maximality. Avis and Hoang study the larger fixed-cardinality independent-set reconfiguration graph without this maximality requirement. Brewster, Mynhardt, and Teshima study reconfiguration of *minimum* independent dominating sets, rather than this specifically fixed near-maximum layer. Agarwal and Basak investigate homotopy types of Möbius-ladder independence and perfect-matching complexes, which do not determine adjacency or shortest paths in this slide graph. OEIS A290608 records ungraded maximal-independent-set enumeration. A prior graded independent-domination enumerator already gives the coefficient \(\frac{2n}{n-2}\binom{n-2}{2}=n(n-3)\) for this layer, but it does not give which transitions are legal, the exact metric, or the self-centered phenomenon. These enumeration formulas are acknowledged rather than presented as new.

## Limitations

This classification is for odd \(n\ge5\), precisely the cardinality \(n-2\), and maximality-preserving one-edge token slides. It does not classify other cardinalities, even Möbius ladders, or the unrestricted token-sliding graph. No claim of absolute publication priority or independent external audit is made. Related descriptions in unindexed literature may exist. Computational certificates are finite verifications, not a substitute for the general proof.

## References

- P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1 (public release 2014-03-03).
- D. Avis, T. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861 (2022).
- R. Brewster, C. Mynhardt, L. Teshima, *Reconfiguration of Minimum Independent Dominating Sets in Graphs*, arXiv:2303.06299 (2023).
- M. Agarwal, P. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601 (2026).
- OEIS A290608, counting maximal independent sets of Möbius ladders (a count, not a slide-distance classification).
