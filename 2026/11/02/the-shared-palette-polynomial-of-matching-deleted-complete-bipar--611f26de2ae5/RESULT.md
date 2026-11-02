# The shared-palette polynomial of matching-deleted complete bipartite graphs

## Finding
For integers \(m,n\ge 2\) and \(0\le t\le\min(m,n)\), let \(G_{m,n,t}\) be the graph obtained from \(K_{m,n}\) by deleting a matching of size \(t\). Let \(\mathcal C_{m,n,t}(q,u)\) count proper conflict-free vertex colorings with colors chosen from a fixed palette of \(q\) named colors, weighting a coloring by \(u^s\), where \(s\) is the number of colors used on **both** bipartition classes. Unused colors are allowed. The following formula computes this two-variable invariant for every nonnegative integer \(q\), without enumerating color assignments.

Write \(S(p,k)\) for the Stirling numbers of the second kind, with \(S(0,0)=1\), and let \(A(p,k)\) count partitions of a \(p\)-element set into \(k\) blocks, each of size at least two. Put \(A(0,0)=1\). All Stirling quantities with negative arguments, or infeasible arguments, are zero. Let \((a)_j\) denote the falling factorial, taken to be zero when \(j>a\) for a nonnegative integer \(a\). Define
\[
Z(p,t,k)=\sum_{j=0}^{\lfloor t/2\rfloor}
 {t\choose 2j}\frac{(2j)!}{2^j j!}
 (p-t)_{t-2j}\, A(p-2t+2j,k-t+j).
\]
For \(p\ge t\), and \(r\ge t\) the number of vertices on the opposite shore, set
\[
W_s(p,t,r;k)=
\begin{cases}
S(p,k)-A(p,k)-tA(p-1,k-1)+\mathbf1_{\{r=t\}}Z(p,t,k),&s=0,\\
S(p-1,k)-A(p-1,k),&s=1,\\
S(p-s,k),&s\ge 2.
\end{cases}
\]
The **complete shared-palette coloring polynomial** is
\[
\boxed{\mathcal C_{m,n,t}(q,u)=\sum_{s=0}^{t}{t\choose s}u^s
 \sum_{k=0}^{m-s}\sum_{\ell=0}^{n-s}
 W_s(m,t,n;k)W_s(n,t,m;\ell)(q)_{s+k+\ell}.}
\]
In particular, \(\mathcal C_{m,n,t}(q,1)\) is the number of proper conflict-free \(q\)-colorings, and \([u^s]\mathcal C_{m,n,t}(q,u)\) counts those having exactly \(s\) shared colors. For example,
\[
\boxed{\mathcal C_{4,4,4}(4,u)=216+144u^2+24u^4.}
\]
The minimum number of colors is also determined:
\[
\boxed{\chi_{\mathrm{pcf}}(G_{m,n,t})=
\begin{cases}
2,&(m,n,t)=(2,2,2),\\
3,&(m,n,t)=(2,2,1),\\
3,&t=2,\ \min(m,n)=2<\max(m,n),\\
3,&(m,n,t)=(3,3,3),\\
4,&\text{otherwise}.
\end{cases}}
\]
Every listed three-color exception has exactly six named optimal colorings; the two-color exception has exactly four named optimal colorings.

## Assumptions and scope
All graphs are finite, simple, and undirected, and \(m,n\ge2\), ensuring that no vertices are isolated. The shores are \(X=\{a_1,\ldots,a_m\}\) and \(Y=\{b_1,\ldots,b_n\}\), with \(a_i b_j\) an edge exactly when \(i\ne j\) or \(i>t\) or \(j>t\). Thus \(a_i b_i\) is missing for \(1\le i\le t\) and all other cross-edges are present. A coloring is *proper conflict-free with respect to open neighborhoods* if it is proper and every vertex \(v\) has some color occurring exactly once among its neighbors. Colorings are functions from the labeled vertex set to a fixed palette; two colorings obtained by renaming colors are distinct if their assignments differ. For a proper coloring the only color permitted on both shores can be shared by exactly one matched nonedge \(\{a_i,b_i\}\), and there can be at most \(t\) such colors.

The non-singleton partition numbers have the explicit finite expression
\[
A(p,k)=\sum_{j=0}^{p}(-1)^j{p\choose j}S(p-j,k-j).
\]
The formulas hold when \(t=0\), for unbalanced shores, and for any integer palette size \(q\ge0\), with the conventional empty-coloring count \(0\) on these nonempty graphs.

## Proof
**1. Shared-color reduction.** Suppose a color appears at \(a_i\) and \(b_j\). Properness forces \(i=j\le t\). Any other occurrence on either shore would be adjacent to one of these vertices; hence the color is used on exactly that deleted matched pair. Conversely, a shared color assigned to such a pair is proper. Choose its set \(I\subseteq[t]\) of \(s\) indices. All other color classes are private to a single shore, and form set partitions of the \(m-s\) and \(n-s\) residual vertices, with \(k\) and \(\ell\) private blocks. Distinct color classes require distinct palette colors, giving precisely \((q)_{s+k+\ell}\) assignments for the unlabelled blocks, including the \(s\) shared blocks distinguished by their pair indices.

**2. Local witness analysis.** Consider the partition of a shore of size \(p\) and the conflict-free requirements at the vertices on the opposite shore of size \(r\). There are \(t\) matched indices. An opposite vertex with index exceeding \(t\) sees the entire shore; one with index \(i\le t\) sees all shore vertices except the vertex at index \(i\). When \(s\ge2\), at least one of the \(s\) shared colors remains as a singleton after any one matched exclusion, so every partition of the \(p-s\) private vertices is allowed: \(S(p-s,k)\).

When \(s=1\), an opposite vertex corresponding to the shared pair loses its only shared singleton. That vertex therefore requires a private singleton on the shore; this is also sufficient for all other opposite vertices because they still see the shared singleton. Thus the admissible private partitions are counted by \(S(p-1,k)-A(p-1,k)\).

For \(s=0\), if the shore has at least two singleton blocks, removing any one vertex leaves another singleton, and every opposite neighborhood has a unique color. If it has exactly one singleton, it works exactly when that singleton lies at an *unmatched* index: a vertex opposite a matched singleton would lose the only witness. With no singleton, removing a vertex can create a singleton only when that vertex was in a doubleton block, and an opposite vertex with an unmatched index never removes a vertex. Hence the zero-singleton case works precisely when \(r=t\) and every one of the \(t\) distinguished matched shore vertices lies in a doubleton block.

The number of partitions with at least two singletons is \(S(p,k)-A(p,k)-pA(p-1,k-1)\); the number with exactly one singleton at an unmatched index is \((p-t)A(p-1,k-1)\). Their sum is the first three terms in \(W_0\).

**3. Doubleton count.** To count zero-singleton partitions with every distinguished index in a size-two block, pair \(2j\) of the \(t\) distinguished indices among themselves. Choose those \(2j\) indices in \({t\choose2j}\) ways, pair them in \((2j)!/(2^j j!)\) ways, and partner the remaining \(t-2j\) distinguished indices injectively with unmatched indices in \((p-t)_{t-2j}\) ways. Every remaining index is unmatched and must be partitioned into blocks of size at least two. The number of remaining blocks is \(k-(t-j)\), proving the formula for \(Z(p,t,k)\). The construction is uniquely reversible, so no overcount occurs.

**4. Product rule.** For each chosen set \(I\) of shared pairs the two opposite-shore witness conditions depend only on their respective private partitions and on \(s=|I|\). Thus their counts multiply, yielding the two factors \(W_s\). Multiply by the falling factorial that assigns distinct names to all blocks, sum over \(k,\ell\), and select \(I\) in \({t\choose s}\) ways. This proves the polynomial for every allowed parameter and every nonnegative integer \(q\).

**5. Minimum palettes.** One color cannot properly color a graph containing edges. Four colors suffice: when \(t\le1\), choose one unmatched vertex on each shore as a singleton-color witness, assign a second private color to any remaining vertices on that shore, and use disjoint palettes on the two shores. When \(t\ge2\), use two distinct shared colors on two deleted matched pairs and assign one exclusive color to each shore's remaining vertices. For the lower bound with at most three colors, split according to the number \(s\) of shared colors. If \(s=0\), one shore must be monochromatic, which yields conflict-free witnesses only for the two-by-two perfect-deletion case. If \(s=1\), each shore needs at least one further private singleton, forcing both shores to have size two and \(t=1\) at three colors. If \(s=2\), there is at most one additional private color, so both shores can have residual vertices only if that color were illegally shared; precisely one shore must be exhausted, forcing \(t=2\) and the exhausted shore size two. If \(s=3\), all three colors are shared, so both shores consist exactly of three deleted pairs. These cases give exactly the listed exceptions; direct coloring of the small two-by-two and three-by-three cases, and of the two-by-arbitrary cases, establishes their attainability. Their named optimal counts follow by either the displayed polynomial or direct block naming: respectively four for \((2,2,2)\), and six for every three-color case.

## Verification
The supplementary standalone `verify.py` uses Python 3 and only the standard library. Run `python3 verify.py` in the same directory. It independently constructs each graph, tests properness and the exact open-neighborhood singleton-color condition on every named \(q\)-coloring, and records the number of shared matched-pair colors. The resulting exact coefficient arrays were compared with the derived formula in **136 cases**, including every \(2\le m,n\le4\), every allowable \(t\), and \(1\le q\le4\), plus eight additional cases. The predicted chromatic classification and small optimal-coloring counts were compared with the formula in **447 cases** with \(2\le m,n\le10\). The script printed `VERIFY_OK` and the exact \(K_{4,4}-M_4\) profile \(\{0:216,1:0,2:144,3:0,4:24\}\). These are finite checks; the general theorem is proved by the partition argument above.

## Relationship to prior work
Fabrici, Lužar, Rindošová, and Soták (2022) defined proper conflict-free coloring with respect to open neighborhoods. Caro, Petruševski, and Škrekovski (2022) studied structural bounds and elementary graph families; Ahn, Im, and Oum (2022) established complexity for fixed palettes on bipartite graphs. The cited papers' inspected statements do not supply the matching-deleted-biclique shared-palette polynomial. A previously published exact result for crown graphs determines the minimum required number of colors \(2,3,4\); that numerical specialization is **not** claimed as new. Its text expressly leaves full optimal four-color configuration classification untreated, whereas the present polynomial counts all palettes, arbitrary partial deletions and unbalanced sizes, and refines by the exact number of shared colors. A published neighborhood-parity odd-coloring theorem for crowns counts the optimal odd-colorings, which is a different local condition; its known optimum count is not claimed as new here. A theorem on proper conflict-free colorings of complete multipartite graphs cannot be specialized directly: deleting a matching changes the cross-adjacency and permits shared matched-pair colors. Search and inspection did not identify a formula with the present full parameter domain and statistic; this is not a proof of publication priority.

## Limitations
The result is specific to deletions forming a matching from a complete bipartite graph, with both original shores of size at least two, and uses open neighborhoods. It does not treat arbitrary missing-edge patterns, list coloring, or recoloring connectivity. It is a counting identity for integer named palette sizes, not an identity enumerating isomorphism classes of colorings modulo automorphisms. The finite numerical verifier cannot rule out an unindexed earlier equivalent formula. No independent mathematical audit is claimed.

## References
1. I. Fabrici, B. Lužar, S. Rindošová, R. Soták, *Proper conflict-free and unique-maximum colorings of planar graphs with respect to neighborhoods*, arXiv:2202.02570 (first publicly posted 2022-02-05); https://arxiv.org/abs/2202.02570.
2. Y. Caro, M. Petruševski, R. Škrekovski, *Remarks on proper conflict-free colorings of graphs*, arXiv:2203.01088 (2022); https://arxiv.org/abs/2203.01088.
3. J. Ahn, S. Im, S.-i. Oum, *The proper conflict-free \(k\)-coloring problem and the odd \(k\)-coloring problem are NP-complete on bipartite graphs*, arXiv:2208.08330 (2022); https://arxiv.org/abs/2208.08330.
4. *Proper conflict-free chromatic number of crown graphs*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/9/30/SCOPE-exact-proper-conflict-free-chromatic-number-of-crown-graphs--24fe2313d105 (2026).
5. *Neighborhood-parity odd colorings of crown graphs*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-neighborhood-parity-odd-colorings-of-crown-graphs--fe94e840e8ec (2026).
6. *Exact proper conflict-free colorings of complete multipartite graphs*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-proper-conflict-free-colorings-of-complete-multipartite-gr--5943975f038c (2026).
