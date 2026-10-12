# Exact \(B\)-coloring number of crown graphs via Mendelsohn packings
## Finding
For every integer \(n\ge 4\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph. A \(B\)-coloring is a proper edge-coloring in which every copy of \(C_4\) is rainbow, and \(q_B(G)\) is the minimum number of colors in such a coloring. Then
\[
q_B(\operatorname{Cr}_n)=
\begin{cases}
11,&n=6,\\
\left\lceil \dfrac{n(n-1)}3\right\rceil,&n\ne 6.
\end{cases}
\]

There is a structural correspondence behind the formula. Label the bipartition classes \(A=\{a_0,\ldots,a_{n-1}\}\) and \(B=\{b_0,\ldots,b_{n-1}\}\), with \(a_i b_j\in E(\operatorname{Cr}_n)\) exactly when \(i\ne j\). Identify \(a_i b_j\) with the arc \(i\to j\) of the complete loopless digraph \(D_n\). Every color class has at most three edges. A class of three edges is exactly a directed \(3\)-cycle in \(D_n\); a class of two edges is exactly a pair of distinct arcs that can be ordered as \(i\to j, j\to k\), allowing \(k=i\).

Consequently, for \(n\ne6\) the optimum is obtained from a maximum Mendelsohn-triple packing of \(D_n\). If \(n\equiv0\) or \(1\pmod3\), the arcs decompose into directed \(3\)-cycles. If \(n\equiv2\pmod3\), all but two arcs decompose into directed \(3\)-cycles and the leave is a directed \(2\)-cycle; its two arcs receive one additional color. The order \(n=6\) is exceptional because a Mendelsohn triple system of order \(6\) does not exist.

This creates a sharp edge-deletion contrast. The initiating literature records \(q_B(K_{n,n})=n^2\), whereas
\[
q_B(\operatorname{Cr}_n)=\frac{n^2-n}3+O(1).
\]
Deleting only the \(n\) edges of one perfect matching therefore changes the leading constant from \(1\) to \(1/3\).
## Assumptions and scope
Graphs are finite and simple. The statement is restricted to \(n\ge4\). The parameter is the edge-coloring invariant called \(B\)-coloring in the cited literature: adjacent edges must have different colors and every \(4\)-cycle must have four different colors.

The result uses a classical existence theorem for maximum packings of the complete directed graph by Mendelsohn triples. That theorem is not reproved here. The new argument is the exact translation between legal color classes of the crown graph and the directed blocks used by that design-theoretic theorem, together with the exceptional-order analysis.
## Proof
Write \(e_{ij}=a_i b_j\) for \(i\ne j\), and identify \(e_{ij}\) with the arc \(i\to j\).

First characterize a single color class. Properness says that two same-colored edges \(e_{ij}\) and \(e_{k\ell}\) have distinct endpoints, so \(i\ne k\) and \(j\ne\ell\). They are opposite edges of a \(4\)-cycle exactly when both cross edges \(a_i b_\ell\) and \(a_k b_j\) exist. In the crown graph this is equivalent to \(i\ne\ell\) and \(k\ne j\). Therefore two edges can share a \(B\)-color exactly when
\[
j=k\quad\text{or}\quad\ell=i.
\]
In arc language, the two arcs must be composable.

Suppose a color class contains at least three arcs. After reversing the order of the first two if necessary, write two of them as \(i\to j\) and \(j\to k\). A third arc \(u\to v\) must compose with each. Properness forbids \(u=j\) and \(v=j\), because those tail and head positions are already used. Compatibility with \(i\to j\) therefore forces \(v=i\), and compatibility with \(j\to k\) forces \(u=k\). Thus the third arc is uniquely \(k\to i\). No fourth distinct arc can be compatible with the first two while preserving properness. Hence every color class has size at most \(3\), and the classes of size \(3\) are precisely directed \(3\)-cycles.

There are \(N=n(n-1)\) crown edges, so
\[
q_B(\operatorname{Cr}_n)\ge\left\lceil\frac N3\right\rceil.
\]
For \(n\equiv0\) or \(1\pmod3\), with \(n\ne6\), the classical Mendelsohn triple-system existence theorem partitions all arcs of \(D_n\) into directed \(3\)-cycles. Giving one color to each cycle attains \(N/3\) colors.

For \(n\equiv2\pmod3\), the classical maximum-packing theorem gives a packing whose leave is a directed \(2\)-cycle \(x\to y, y\to x\). The two leave arcs are compatible and correspond to two disjoint crown edges that are not opposite in any \(4\)-cycle, so they can receive one common color. The remaining arcs are partitioned into directed \(3\)-cycles. This uses
\[
\frac{N-2}3+1=\left\lceil\frac N3\right\rceil
\]
colors.

It remains to treat \(n=6\). Here \(N=30\), so the general lower bound is \(10\). If a \(10\)-color \(B\)-coloring existed, every color class would have size exactly \(3\); the structural lemma would then partition all arcs of \(D_6\) into Mendelsohn triples, which is a Mendelsohn triple system of order \(6\). The classical existence theorem excludes this order. Thus \(q_B(\operatorname{Cr}_6)\ge11\).

For the matching upper bound, on the labels \(0,1,2,3,4,5\), use the eight directed cycles
\[
(0,1,4),(0,2,5),(0,3,2),(0,5,3),(1,3,5),(1,5,4),(2,3,4),(2,4,5)
\]
and the three two-arc color classes
\[
\{0\to4,1\to0\},\quad\{1\to2,2\to1\},\quad\{3\to1,4\to3\}.
\]
These eleven classes partition all \(30\) arcs and each is legal by the characterization above. Hence \(q_B(\operatorname{Cr}_6)=11\).
## Verification
The standalone verifier `verify.py` performs four independent finite checks. It exhaustively inspects every edge subset of size at most \(4\) for crown orders \(4,5,6\) and confirms the color-class structural lemma. It checks explicit optimal colorings for orders \(4\) through \(8\), including the displayed exceptional construction. It performs an exact-cover search showing that \(D_6\) has no decomposition into directed \(3\)-cycles. Finally, it checks the arithmetic form of the claimed formula through order \(200\).

The replay output is stored in `verification_output.txt`. These finite checks are stress tests; the all-order existence statements use the cited Mendelsohn packing theorem.
## Relationship to prior work
Lu, Ying, and Song study \(B\)-colorings under bipartite exclusions and restate the definition and the extremal identity \(q_B(K_{\Delta,\Delta})=\Delta^2\). Their full paper contains no occurrence of “crown” or “Mendelsohn” and does not state the matching-deleted biclique formula.

Gyárfás and Sárközy introduced the \(B\)-coloring parameter in connection with the \((7,4)\)-conjecture, while subsequent work treats products, planar graphs, and exclusion-driven bounds. The checked literature did not locate a crown-graph exact value.

On the design side, Gardner's classical packing theorem for the complete digraph supplies exactly the directed-triangle decompositions needed after the color-class reduction. That theorem is treated as prior coverage of the design construction itself. The contribution here is the crown-graph \(B\)-coloring reduction, the transfer of the packing leave into a legal color class, and the resulting sharp exceptional-order formula. The accessible design-theory supplement explicitly attributes the packing results to Gardner's 1997 Congressus Numerantium paper.
## Limitations
The proof exploits that the only missing cross edges of the crown graph form one perfect matching. The color-class characterization does not extend unchanged to arbitrary matching-deleted or sparse bipartite graphs. The all-order upper bounds rely on the cited Mendelsohn packing existence theorem; the verifier does not replace that theorem.

A differently phrased older edge-coloring paper could in principle encode the same crown/design correspondence without using the term \(B\)-coloring. Targeted searches under crown, matching-deleted biclique, rainbow \(C_4\), and Mendelsohn terminology did not locate such a statement.
## References
1. Z. Lu, Q. Ying, and H. Song, *(2,F)-Avoiding Coloring and B-Coloring under Bipartite Exclusions*, arXiv:2609.39716v1, 2026.
2. A. Gyárfás and G. N. Sárközy, *“Less” Strong Chromatic Indices and the (7,4)-Conjecture*, Studia Scientiarum Mathematicarum Hungarica 60 (2023), 109–122, DOI:10.1556/012.2023.01539.
3. R. Gardner, *Optimal Packings and Coverings of the Complete Directed Graph with 3-Circuits and with Transitive Triples*, Congressus Numerantium 127 (1997), 161–170.
4. R. Gardner, *Packings and Coverings for Mendelsohn and Directed Triple Systems*, design-theory supplement, revised 2022; the supplement reproduces the packing theorem and identifies Reference 3 as its original source.
