# Secure coalition numbers of complete bipartite graphs
## Finding
For every finite complete bipartite graph \(K_{s,t}\) with \(1\le s\le t\),
\[
\mathrm{SEC}(K_{s,t})=
\begin{cases}
2,&s=t=1,\\
3,&s=1<t,\\
4,&s=2,\\
s+t-\min\{s-2,4\},&s\ge3.
\end{cases}
\]
Thus the nonstar regime has a sharp four-step stabilization: the deficit \((s+t)-\mathrm{SEC}(K_{s,t})\) is \(1,2,3,4\) for \(s=3,4,5,\ge6\), respectively.

## Assumptions and scope
The graph is finite, simple, and complete bipartite, with shores \(A,B\) of orders \(s,t\) and \(1\le s\le t\). A set \(D\) is secure dominating when it dominates the graph and every vertex outside \(D\) can replace an adjacent defender in \(D\) while leaving a dominating set. Two disjoint non-secure-dominating sets form a secure coalition when their union is secure dominating. A secure-coalition partition is a vertex partition in which every block has a secure-coalition partner, apart from the exceptional singleton-full-vertex case allowed in the defining literature. The complete bipartite graphs considered here have no such exceptional block unless the graph is complete.

For a block or vertex set \(D\), put \(x=|D\cap A|\) and \(y=|D\cap B|\).

## Proof
The first ingredient is the exact secure-domination test
\[
D\text{ is secure dominating}
\iff
\begin{cases}
(x=s\text{ or }y>0),\\
(y=t\text{ or }x>0),\\
(x=s\text{ or }x=s-1\text{ or }y\ge2),\\
(y=t\text{ or }y=t-1\text{ or }x\ge2).
\end{cases}
\]
The first two conditions are ordinary domination. If \(x<s\), an outside vertex of \(A\) must be defended by a vertex of \(B\). After that defender is exchanged, the only possible new domination failure is another outside vertex of \(A\); this is avoided exactly when either there was only one outside vertex of \(A\), namely \(x=s-1\), or at least two vertices of \(B\) were selected, namely \(y\ge2\). The fourth condition is symmetric. This proves the criterion.

For \(s=1<t\), secure dominating sets have occupancy \((0,t)\), \((1,t-1)\), or \((1,t)\). A three-block partition is obtained, when \(t\ge3\), from one block of occupancy \((1,t-2)\) and the two remaining \(B\)-vertices as singleton blocks; when \(t=2\), the singleton partition works. If a partition had at least four blocks, take a \(B\)-only block. It cannot unite with another \(B\)-only block to cover all of \(B\), and its union with the unique block meeting \(A\) leaves at least two \(B\)-vertices outside. Hence it has no secure-coalition partner. Thus \(\mathrm{SEC}(K_{1,t})=3\). The case \(K_{1,1}\cong K_2\) has value \(2\).

For \(s=2\), every block containing both vertices of \(A\) is already secure dominating and therefore cannot be a nontrivial block of a secure-coalition partition. Hence the two \(A\)-vertices lie in distinct blocks. If there were at least three further \(B\)-only blocks, any one of them would fail to find a partner: two \(B\)-only blocks do not cover \(B\), and union with either \(A\)-block still leaves at least two \(B\)-vertices outside, while occupancy \((1,y)\) is secure only when \(y\ge t-1\). Therefore there are at most four blocks. Equality is attained by the singleton partition when \(t=2\); for \(t\ge3\), use blocks of occupancies \((1,t-2),(1,0),(0,1),(0,1)\). Hence \(\mathrm{SEC}(K_{2,t})=4\).

Now assume \(s\ge3\), and for a secure-coalition partition \(\Pi\) define its excess by
\[
E=(s+t)-|\Pi|=\sum_{C\in\Pi}(|C|-1).
\]
For \(3\le s\le5\), choose one hub \(U\subset A\) of order \(s-1\) and leave every other vertex singleton. The hub is not secure dominating; adding the omitted \(A\)-vertex gives all of \(A\), while adding any \(B\)-singleton gives occupancy \((s-1,1)\), which is secure dominating. This yields \(s+t-(s-2)\) blocks.

For \(s\ge6\), choose two disjoint hub blocks with occupancies \((1,2)\) and \((2,1)\), and leave all other vertices singleton. Neither hub is secure dominating, their union has occupancy \((3,3)\), every remaining \(A\)-singleton joins the \((1,2)\) hub to make occupancy \((2,2)\), and every remaining \(B\)-singleton joins the \((2,1)\) hub to make occupancy \((2,2)\). Thus \(E=4\) is attainable.

It remains to prove the matching lower bounds. For \(s=3\), \(E=0\) would make every block a singleton, but no union of two singletons is secure dominating, so \(E\ge1\). For \(s=4\), \(E\le1\) leaves only singleton blocks and at most one block of order two; every possible union involving a singleton then has order at most three, whereas the occupancy criterion shows that every secure dominating set has order at least four. Hence \(E\ge2\).

For the remaining cases use a shore-singleton lemma. If a shore \(X\) of order \(m\) has no singleton block, and a block \(C\) contains \(q_C\) vertices of \(X\), then
\[
|C|-1\ge \left\lceil\frac{q_C}2\right\rceil.
\]
Indeed, this is immediate for \(q_C\ge2\), while for \(q_C=1\) the block must contain another vertex. Summing gives \(E\ge\lceil m/2\rceil\). Therefore, when \(s=5\) and \(E\le2\), both shores contain singleton blocks. A singleton of \(A\) needs a partner containing at least one vertex of \(A\) and two of \(B\), hence a block of order at least three and excess at least two; symmetrically a singleton of \(B\) needs a partner with at least two vertices of \(A\) and one of \(B\). With \(E\le2\) these cannot be two distinct blocks, and one block cannot satisfy both requirements at order three. Thus \(E\ge3\).

Finally suppose \(s\ge6\) and \(E\le3\). If a shore of order greater than six had no singleton block, the shore-singleton lemma would already give \(E\ge4\). If a shore has order exactly six and no singleton block while \(E=3\), equality in the lemma forces its six vertices into three pure two-vertex blocks and consumes all excess; every vertex of the opposite shore is then singleton, but none can form a secure coalition with a same-shore singleton or with a pure two-vertex opposite-shore block. Hence both shores again contain singleton blocks. A singleton of \(A\) requires a partner with at least one \(A\)-vertex and two \(B\)-vertices, of excess at least two; a singleton of \(B\) requires a partner with at least two \(A\)-vertices and one \(B\)-vertex, again of excess at least two. If these partners are distinct then \(E\ge4\). If they coincide, the common block contains at least two vertices from each shore and is itself secure dominating, which is forbidden for a coalition block. This contradiction proves \(E\ge4\).

The lower and upper constructions now agree in every case, proving the formula.

## Verification
The standalone checker independently implements domination, secure domination, secure coalitions, and canonical set partitions. It verifies the occupancy criterion on \(1110\) shore-occupancy profiles, exhaustively computes the maximum secure-coalition partition order for all \(20\) complete bipartite profiles of total order from \(2\) through \(9\), and checks the explicit constructions for all \(820\) profiles with \(1\le s\le t\le40\). Its output is reproduced in `verification_output.txt`.

The exhaustive computation is corroborative only. The unrestricted result for arbitrary \(s,t\) is established by the analytic argument above.

## Relationship to prior work
Shetty, Udupa, and Rakshith introduced secure coalitions and the secure coalition number in 2025. Their paper proves general existence and bounds, characterizes the extreme values \(1,2,n\), and develops the tree case. The inspected full text contains the star value \(\mathrm{SEC}(K_{1,t})=3\) in its tree analysis and supplies general bounds that already make some small-shore cases close to immediate. It does not state a complete-bipartite classification, and targeted searches for complete-bipartite, biclique, and \(K_{m,n}\) formulations found no theorem implying the displayed formula.

The new structural content is strongest from \(s=5\) onward. The general upper bound from the initiating paper, combined with the direct secure-domination criterion above, only gives \(\mathrm{SEC}(K_{s,t})\le s+t-2\) for \(s\ge4\). The excess argument improves this to the exact values \(s+t-3\) at \(s=5\) and \(s+t-4\) for all \(s\ge6\), and the four-block proof resolves the entire \(s=2\) family.

## Limitations
The theorem is specific to complete bipartite graphs and does not classify secure-coalition partitions of arbitrary complete multipartite graphs. The finite checker stops at total order \(9\), so it is not evidence for the infinite statement by itself. A residual bibliographic risk remains that an equivalent biclique result exists in poorly indexed later literature under different coalition terminology; no such result was found in the checked primary text, semantic literature searches, or exact web searches.

## References
1. Swathi Shetty, Sayinath Udupa N. V., and B. R. Rakshith, *Secure coalitions in graphs*, arXiv:2511.21170. First public version dated 2025-11-26. https://arxiv.org/abs/2511.21170
