# Dom-forcing under matching deletions in complete bipartite graphs
## Finding
Let \(2\le m\le n\), let \(0\le t\le m\), and let
\[
G_{m,n,t}=K_{m,n}-M_t,
\]
where \(M_t\) is any matching of size \(t\). Assume \(G_{m,n,t}\) is connected; among these parameters the only excluded triple is \((m,n,t)=(2,2,2)\).

The ordinary zero-forcing number is
\[
Z(G_{m,n,t})=m+n-2-\min\{t,2\}.
\]
The dom-forcing number is
\[
F_d(G_{m,n,t})=
\begin{cases}
Z(G_{m,n,t})+1,&(m,n,t)=(2,2,1),\\
Z(G_{m,n,t})+1,&m=2,\ t=2,\ n\ge3,\\
Z(G_{m,n,t})+1,&(m,n)=(3,3),\ t\in\{2,3\},\\
Z(G_{m,n,t}),&\text{otherwise.}
\end{cases}
\]
Thus the forcing threshold drops by one at the first matching deletion, by one again at the second, and then stabilizes. The additional domination requirement costs one vertex only in three low-shore regimes.

## Assumptions and scope
All graphs are finite, simple, and undirected. A zero-forcing process starts from a blue set \(S\); a blue vertex with exactly one white neighbor forces that neighbor blue. A set is dom-forcing when it is both zero forcing and dominating. The notation \(M_t\) means a matching with endpoints \(a_i b_i\) for \(1\le i\le t\) after labeling the shores as \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\).

The theorem concerns matching deletions only. It does not assert the same formula for arbitrary sets of \(t\) deleted edges.

## Proof
Write \(p\) and \(q\) for the numbers of initially white vertices in \(A\) and \(B\). A blue vertex in \(B\) has either \(p\) or \(p-1\) white neighbors in \(A\), because at most its one matched edge is absent. Hence, if \(p\ge3\), no blue vertex in \(B\) can force into \(A\). Since only such a force can decrease \(p\), the value of \(p\) can then never decrease. Therefore every zero-forcing set leaves at most two vertices white in each shore. Symmetrically, \(q\le2\).

When \(t=0\), three white vertices cannot be cleared. The only new shape after the preceding bound is \((p,q)=(2,1)\) or \((1,2)\): the singleton white shore can be cleared, but the two white vertices on the other shore then remain because every opposite blue vertex sees both. Hence at most two vertices can be white. Leaving \(a_1,b_1\) white gives a forcing set, so \(Z(G_{m,n,0})=m+n-2\).

When \(t=1\), four white vertices would force \((p,q)=(2,2)\). Any first force must exploit the unique missing edge \(a_1b_1\). If the first force goes from \(A\) to \(B\), then \(a_1\) is blue and \(b_1\) is white. After the white vertices of \(B\) are cleared, the two white vertices of \(A\) remain, and the unique missing edge cannot help because its \(A\)-endpoint is already blue. The symmetric case is identical. Thus four whites are impossible. Three whites are attainable: leaving \(a_1,a_2,b_2\) white gives the forcing chain \(b_1\to a_2\), then \(a_2\to b_2\), then a blue vertex of \(B\) forces \(a_1\). Consequently \(Z(G_{m,n,1})=m+n-3\).

When \(t\ge2\), the general shore bound gives \(Z\ge m+n-4\). Except for the disconnected graph \(G_{2,2,2}\), leave
\[
\{a_1,a_2,b_1,b_3\}
\]
white. Then \(b_2\to a_1\), \(a_1\to b_3\), \(b_3\to a_2\), and \(a_2\to b_1\). Thus \(Z=m+n-4\). This proves the zero-forcing formula.

It remains to decide when a minimum zero-forcing set can also dominate. For \(t=0\), the complement of \(\{a_1,b_1\}\) is dominating. For \(t=1\), if \(m\ge3\), the complement of \(\{a_1,a_2,b_2\}\) is dominating; if \(m=2\) and \(n\ge3\), the complement of \(\{a_1,b_1,b_2\}\) is both dominating and zero forcing. The sole remaining \(t=1\) graph is \(G_{2,2,1}\cong P_4\): a minimum zero-forcing set has one vertex and cannot dominate, while \(\{a_1,a_2\}\) is dom-forcing. Hence its dom-forcing number is \(Z+1\).

Now let \(t\ge2\). If \(m=2\), every minimum zero-forcing set leaves exactly two vertices white in each shore, so it contains no vertex of \(A\) and cannot dominate the omitted vertices of \(B\). The set
\[
\{a_1\}\cup\bigl(B\setminus\{b_2,b_3\}\bigr)
\]
is dom-forcing, proving \(F_d=Z+1\) for \(m=2,\ t=2,\ n\ge3\).

If \(m=n=3\) and \(t\in\{2,3\}\), a minimum zero-forcing set has two vertices, one in each shore. A dominating such pair must align so that every missing matched edge incident with an omitted vertex is covered; in each possible aligned pair both selected vertices initially see two white neighbors, so no force can start. Thus no minimum zero-forcing set dominates. The set \(\{a_1,a_2,b_1\}\) is both dominating and zero forcing, so again \(F_d=Z+1\).

All remaining cases with \(t\ge2\) have \(m\ge3\) and \(n\ge4\). For \(t=2\), the complement of
\[
\{a_1,a_2,b_2,b_4\}
\]
is a dominating zero-forcing set of size \(m+n-4\). For \(t\ge3\), the complement of
\[
\{a_2,a_3,b_3,b_4\}
\]
has the same property. Therefore \(F_d=Z\) outside the three stated exceptions.

## Verification
The proof above is symbolic and covers every allowed parameter. A standalone verifier independently constructs the graphs and implements domination and the standard color-change rule. It exhaustively computed both \(Z\) and \(F_d\) for every connected parameter profile with \(2\le m\le5\), \(m\le n\le7\), and \(m+n\le10\), totaling 58 profiles. It also checked the explicit proof witnesses for 681 connected profiles with \(2\le m\le12\) and \(m\le n\le15\). The replay output was:

`ALL CHECKS PASSED; exhaustive_connected_profiles=58; witness_profiles=681`

The finite checks corroborate the theorem; they are not used as a substitute for the all-parameter proof.

## Relationship to prior work
Susanth, Dominic, and Premodkumar introduced the dom-forcing number and, in their complete-bipartite theorem, proved \(F_d(K_{m,n})=m+n-2\) for \(m,n\ge2\). Their inspected full text also treats paths, cycles, hypercubes, complete graphs, wheels, stars, and other named families, but does not state a theorem for \(K_{m,n}-M_t\). The present result recovers their \(t=0\) value and determines the exact sensitivity to a matching defect of every possible size.

Jiang and Wan later gave the general criterion that \(F_d(G)=Z(G)\) exactly when some minimum zero-forcing set is dominating, and again determined the complete-bipartite case. That criterion does not determine either the zero-forcing number or the existence of a dominating minimum forcing set after matching edges are removed; the theorem above supplies both pieces and identifies the precise exceptional regimes.

Several isolated members of the family are standard graphs already covered by known formulas, such as \(G_{2,2,1}\cong P_4\), \(G_{3,3,3}\cong C_6\), and \(G_{4,4,4}\cong Q_3\). These boundary coincidences are not claimed as new individual evaluations. The new content is the uniform matching-deletion classification and its saturation and exception structure.

## Limitations
The result is specific to a deleted matching. Arbitrary edge deletions can create multiple missing neighbors at one vertex, invalidating the key two-white-per-shore argument. No claim is made about connected dom-forcing, propagation time, \(k\)-forcing variants, or arbitrary bipartite graphs. Literature searches cannot rule out a poorly indexed equivalent result under substantially different terminology; no such result was found in the checked sources.

## References
1. P. Susanth, C. Dominic, and K. P. Premodkumar, “Dom-forcing sets in graphs,” arXiv:2411.00580v1, first public 2024-11-01; later published in *Asian Research Journal of Mathematics* 22(3), 88–104 (2026), DOI 10.9734/arjom/2026/v22i31058.
2. H. Jiang and H. Wan, “Forcing and domination in graphs,” *AIMS Mathematics* 11(7), 19772–19783 (2026), DOI 10.3934/math.2026802.
3. AIM Minimum Rank–Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648, DOI 10.1016/j.laa.2007.10.009.
