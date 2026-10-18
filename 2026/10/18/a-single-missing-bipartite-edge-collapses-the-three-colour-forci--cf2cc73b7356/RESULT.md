# A single missing bipartite edge collapses the three-colour forcing seed threshold

## Finding
Let \(n\ge4\) and \(0\le t\le n\) be integers. On labeled sides \(A=\{a_1,\dots,a_n\}\) and \(B=\{b_1,\dots,b_n\}\), let
\[
G_{n,t}=K_{n,n}-\{a_i b_i:1\le i\le t\}.
\]
Thus \(t\) edges of a matching are removed. An initially assigned vertex has one of three named colours. An uncoloured vertex becomes coloured when its already coloured neighbours display exactly two distinct colours; it receives the third colour. A *forcing partial assignment* is one for which repeated applications of this rule give a proper total three-colouring. Let \(s_3(G)\) be the minimum number of initially coloured vertices in such an assignment, and let \(f_3(G,k)\) count forcing partial assignments with exactly \(k\) seeds, distinguishing vertex labels and the three named colours.

**Theorem.** For every \(n\ge4\),
\[
 s_3(G_{n,0})=n,\qquad f_3(G_{n,0},n)=6(2^n-2),
\]
whereas, for every \(1\le t\le n\),
\[
\boxed{s_3(G_{n,t})=3,\qquad f_3(G_{n,t},3)=12t(n-1).}
\]
Moreover, all minimum forcing assignments on \(G_{n,t}\), \(t\ge1\), are **exactly** these: choose one deleted edge \(a_i b_i\), assign its endpoints the same colour \(c\), and assign one third vertex \(a_j\) or \(b_j\), with \(j\ne i\), a different colour \(d\); leave every other vertex uncoloured.

Consequently, if \(F_{G,3}(x)=\sum_k f_3(G,k)x^k\), then its first nonzero term is \(6(2^n-2)x^n\) for \(G=G_{n,0}\), but \(12t(n-1)x^3\) for \(G=G_{n,t}\) when \(t\ge1\). In the probabilistic forced-colouring model of Farr, in which each of three colours is assigned independently at each vertex with probability \(p\) and a vertex remains blank with probability \(1-3p\), this says
\[
 \operatorname{FC}_3(G_{n,0};p)=6(2^n-2)p^n+O(p^{n+1}),
\]
\[
 \operatorname{FC}_3(G_{n,t};p)=12t(n-1)p^3+O(p^4)\quad(1\le t\le n)
\]
as \(p\to0\). In particular, deleting **one edge** from \(K_{n,n}\) changes the minimum forcing domain from \(n\) to \(3\), and the leading coefficient subsequently grows linearly with the size of a deleted matching.

## Assumptions and scope
All graphs are finite, simple and undirected. The three named colours are \(\{1,2,3\}\); the graph is permitted to use fewer than three colours in a completed colouring. Initially assigned adjacent vertices with the same colour cannot produce a proper final colouring. The forcing rule uses **distinct colours appearing among neighbours**, not the number of coloured neighbours. The theorem concerns \(n\ge4\) and deleted edges forming a matching of size at most \(n\). It does not assert a complete formula for all coefficients of \(F_{G,3}(x)\), nor an assertion for smaller side sizes or other palettes.

## Proof
First suppose \(t=0\). If a non-total assignment forces at least one vertex, the first newly coloured vertex lies, say, in \(B\), and already sees two distinct colours on \(A\). Every vertex subsequently coloured in \(B\) must receive the third colour; all initially coloured vertices of \(B\) must likewise have that third colour, because each is adjacent to every vertex of \(A\). Hence any initially blank vertex of \(A\) sees at most one colour in \(B\) and can never be forced. It follows that \(A\) was already entirely coloured. Thus any successful non-total assignment has at least \(n\) seeds. Conversely, colouring all of \(A\) with exactly two of the three colours forces every vertex of \(B\) to the third. With exactly \(n\) seeds, either side may be the seeded one, there are \(3\) choices of the two-colour subset, and \(2^n-2\) surjective assignments of those colours. This proves \(s_3(G_{n,0})=n\) and the stated count.

Next suppose \(t\ge1\). A first forced vertex requires two already seeded, differently coloured neighbours on the same opposite side. Thus no assignment with fewer than two seeds succeeds. With exactly two seeds, if they lie on opposite sides or have equal colours, no first force is possible. If both lie on \(A\) in different colours, any initially forced vertex of \(B\) receives the third colour, while no vertex of \(A\) can be forced from monochromatically coloured vertices of \(B\). Since \(n\ge4\), at least two vertices of \(A\) are still blank, and the process cannot finish. The same argument holds with the sides reversed. Therefore \(s_3(G_{n,t})\ge3\).

For a successful three-seed assignment, two seeds must lie on the same side and have distinct colours; assume these lie at \(a_i,a_j\), with colours \(c,d\) and \(i\ne j\). If all three seeds lie in \(A\) and display three different colours, choose \(b_k\) whose index is not among the three seeded indices. Such a vertex exists because \(n\ge4\), and it is adjacent to all three seeded vertices, so the partial assignment has no proper total extension. If the three seeds lie in \(A\) and use just two colours, every forced vertex of \(B\) gets their third colour. An uncoloured vertex remains in \(A\), where it can then see only one colour, so completion is impossible. Thus the third seed must lie in \(B\).

Write \(e\) for the remaining third colour. If the seeded vertex of \(B\) has colour \(e\), then all vertices of \(B\) subsequently forced by the two initial colours on \(A\) also receive \(e\). No initially blank vertex of \(A\) can then see two colours, so completion is impossible. Therefore the seeded vertex of \(B\) has colour \(c\) or \(d\). Properness requires that this vertex be nonadjacent to the corresponding seeded vertex of \(A\). The only missing cross-edges are the deleted matching edges. Hence the three seeds consist of both endpoints of one deleted edge with a common colour, together with one additional vertex at a different index and with a different colour. The same reasoning applies when two seeds lie in \(B\).

Conversely, seed \(a_i,b_i\) with \(c\) for some deleted edge and seed \(a_j\), \(j\ne i\), with \(d\ne c\). Every \(b_k\) for \(k\notin\{i,j\}\) sees both \(c\) and \(d\), since all omitted edges are matching edges, and is immediately forced to \(e\), the third colour. Since \(n\ge4\), at least two such vertices are now coloured \(e\). Every initially blank \(a_\ell\), \(\ell\notin\{i,j\}\), sees \(b_i\) of colour \(c\) and at least one of these \(e\)-coloured \(b_k\) with \(k\ne\ell\); it is therefore forced to \(d\). Finally \(b_j\) sees \(a_i\) of colour \(c\) and some \(a_\ell\) of colour \(d\), so it is forced to \(e\). The resulting assignment is proper: only the deleted matched pair shares \(c\) across the sides, while all remaining vertices of \(A\) have \(d\) and all remaining vertices of \(B\) have \(e\). Seeding \(b_j\) instead is symmetric.

Every successful three-seed assignment has a unique deleted matched pair of equal-colour seeds. There are \(t\) choices for that pair, \(3\) choices for its colour, \(2\) choices for the additional distinct colour, \(2\) choices for the side of the third seed, and \(n-1\) choices for its index. Their product is \(12t(n-1)\), proving the classification and coefficient formula. Finally, the leading terms of \(\operatorname{FC}_3\) follow from its seed-size expansion: a size-\(k\) forcing assignment contributes \(p^k(1-3p)^{2n-k}\), so the first nonzero coefficient is the number of minimum-seed assignments.

## Verification
Run \(\texttt{python3 verify.py}\) using Python 3.9 or newer. The checker independently builds graph adjacencies, applies the distinct-neighbour-colour forcing rule to closure, checks that the resulting total assignment is proper, and enumerates every initial partial assignment with up to three seeds. For every \(n\in\{4,5,6,7\}\) and \(t\in\{1,\dots,n\}\), it checks the stated if-and-only-if classification and the exact count \(12t(n-1)\). It separately exhausts all assignments with fewer than \(n\) seeds on \(K_{n,n}\) for \(n\in\{4,5,6\}\), and verifies a witness with exactly \(n\) seeds. The actual package program printed \(\texttt{ALL CHECKS PASSED}\), after \(401389\) partial assignments were tested. The theorem for all \(n\ge4\) is proved above and does not depend on an extrapolation from these finite checks.

## Relationship to prior work
G. E. Farr's 2026 paper defines the forced-colouring probability and domain-size generating polynomial, proves that the smallest forcing domain gives the order of vanishing at \(p=0\), and treats arbitrary bipartite graphs for the two-colour palette. Published work subsequently determined the complete forced three-colouring polynomial of \(K_{a,b}\); the \(t=0\) baseline in the present theorem is consequently already covered, and is stated here for quantitative comparison, not claimed as new. Published formulas for paths and cycles include the six-cycle \(G_{3,3}\), but not the \(n\ge4\) graphs in this theorem. A separate classification of neighbourhood-parity colourings on crown graphs studies a different, non-forcing colouring requirement and does not imply the result here.

The new contribution is the complete classification and count of minimum three-colour forcing assignments **for every nonempty matching deletion**, including the one-edge perturbation and the coefficient's exact dependence on \(t\). The existing complete-bipartite classification cannot be applied after edge deletion, and the known maximum-degree-two formulas do not cover \(n\ge4\). Searches also considered colour-propagation/partial-colouring aliases and defining sets, but no theorem implying this exact matching-deletion classification was identified.

## Limitations
The analysis is specific to three colours, matching deletions, and \(n\ge4\). It does not determine the remaining coefficients of the forced-colouring polynomial, nor minimal domains for nonmatching sets of removed edges. The finite computational census independently checks only the explicitly reported parameter range. Bibliographic search cannot establish absolute priority; alternative terminology or unindexed equivalent work remains possible. No independent audit is claimed.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first posted 15 September 2026. https://arxiv.org/html/2609.17108
2. *Forced three-colouring polynomial of complete bipartite graphs*, public research record, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69
3. *Exact forced 3-colouring polynomials at maximum degree two*, public research record, September 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd
4. *Neighborhood-parity odd colorings of crown graphs*, public research record, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-neighborhood-parity-odd-colorings-of-crown-graphs--fe94e840e8ec
