# Exact \(K_{2,5}\)-free Turán number for cographs

## Finding
Let \(\operatorname{ex}_{\mathrm{cog}}(n,K_{2,5})\) denote the maximum number of edges in an \(n\)-vertex cograph containing no \(K_{2,5}\) as an ordinary subgraph. Then
\[
\operatorname{ex}_{\mathrm{cog}}(n,K_{2,5})=
\begin{cases}
\binom n2,&1\le n\le6,\\
17,&n=7,\\
20,&n=8,\\
3(n-1)-\delta_{(n-1)\bmod5},&n\ge9,
\end{cases}
\]
where
\[
(\delta_0,\delta_1,\delta_2,\delta_3,\delta_4)=(0,1,2,3,2).
\]

For \(n\ge9\), every extremal graph is connected and has a universal vertex. Write \(m=n-1=5q+r\) with \(0\le r\le4\), and put
\[
B_6=(K_2\cup K_1)\vee(K_2\cup K_1).
\]
After deleting the universal vertex, the component multiset is exactly one of the following:

- \(qK_5\) when \(r=0\);
- \((q-1)K_5\cup B_6\) when \(r=1\);
- \((q-2)K_5\cup2B_6\) when \(r=2\);
- \(qK_5\cup K_3\), or additionally \((q-3)K_5\cup3B_6\) when \(r=3\) and \(q\ge3\);
- \(qK_5\cup K_4\) when \(r=4\).

Thus the six-vertex exceptional extremizer from the \(K_{2,4}\)-free problem propagates into the exact period-five correction for \(K_{2,5}\), and it creates a second extremal structure in one residue class.

## Assumptions and scope
All graphs are finite, simple, and undirected. A cograph is a graph with no induced \(P_4\). The forbidden \(K_{2,5}\) is an ordinary subgraph, not necessarily induced. Equivalently, a graph is \(K_{2,5}\)-free exactly when every pair of vertices has at most four common neighbors.

The classification statement concerns all extremal cographs for \(n\ge9\). The values at \(n=7,8\) are exact but their full extremal-type classification is not part of the claim.

## Proof
First consider a connected \(K_{2,5}\)-free cograph \(G\) of order \(n\ge9\). At the root join of a reduced cotree, if no factor is a singleton then every factor has at least two vertices. Let \(A\) be a smallest factor and let \(B\) be the union of all other factors. Since \(n\ge9\), one has \(|B|\ge5\). Every edge between \(A\) and \(B\) is present, so any two vertices of \(A\) together with any five vertices of \(B\) form a \(K_{2,5}\), a contradiction. Hence \(G\) has a universal vertex \(v\).

Write \(G=K_1\vee H\). For \(x\in V(H)\), the pair \(v,x\) has exactly \(\deg_H(x)\) common neighbors. For \(x,y\in V(H)\), their common-neighbor count in \(G\) is one plus their common-neighbor count in \(H\). Therefore
\[
G\text{ is }K_{2,5}\text{-free}
\quad\Longleftrightarrow\quad
\Delta(H)\le4\text{ and }H\text{ is }K_{2,4}\text{-free}.
\]

Now consider a connected component \(C\) of \(H\). A previously established exact \(K_{2,4}\)-free cograph theorem proves, in particular, that every connected \(K_{2,4}\)-free cograph of order at least seven has a universal vertex. Such a component would contain a vertex of degree at least six, contradicting \(\Delta(H)\le4\). Hence every component of \(H\) has order at most six.

For component order \(d\le5\), the largest possible edge count is \(\binom d2\), attained exactly by \(K_d\). For \(d=6\), the exact \(K_{2,4}\)-free cograph number is eleven. Among the two six-vertex extremal types in that theorem, exactly one has maximum degree at most four, namely
\[
B_6=(K_2\cup K_1)\vee(K_2\cup K_1),
\]
which has eleven edges. Consequently a component of order \(d\in\{1,2,3,4,5,6\}\) contributes at most
\[
w(d)=(0,1,3,6,10,11).
\]

Let \(m=|H|=n-1\). Relative to the baseline \(2d\), the deficits \(2d-w(d)\) for component orders \(1,\ldots,6\) are
\[
(2,3,3,2,0,1).
\]
Reducing component orders modulo five, the minimum total deficit for an order \(m\ge8\) is
\[
\delta_{m\bmod5}\in(0,1,2,3,2).
\]
Indeed, deficit zero uses only \(K_5\) blocks; residue one is optimally supplied by one \(B_6\); residue two by two \(B_6\) blocks; residue three either by one \(K_3\) or by three \(B_6\) blocks; and residue four by one \(K_4\). No smaller deficit is possible from the listed component deficits. Moreover, equality is classified by the same cost table: after deleting zero-deficit \(K_5\) blocks, a minimum-deficit residue is realized only by one \(B_6\) for residue one, two \(B_6\) blocks for residue two, either one \(K_3\) or three \(B_6\) blocks for residue three, and one \(K_4\) for residue four. Hence
\[
e(H)\le2m-\delta_{m\bmod5},
\]
and therefore every connected \(G\) of order \(n\ge9\) satisfies
\[
e(G)\le m+2m-\delta_{m\bmod5}=3(n-1)-\delta_{(n-1)\bmod5}.
\]
The listed component decompositions attain equality and give exactly the stated connected extremizers.

It remains to rule out disconnected extremizers. Every connected \(K_{2,5}\)-free cograph of order \(k\) has at most \(3k-3\) edges. For \(k\le6\) this follows from \(\binom k2\le3k-3\). For \(k=7\), a universal vertex gives at most seventeen edges; without a universal vertex the root join is a \(3+4\) split and a direct common-neighbor count gives at most seventeen. For \(k=8\), a universal vertex gives at most eighteen edges, while without one the root join must be a \(4+4\) split; each side then has maximum degree at most one, giving at most twenty edges. For \(k\ge9\), the bound follows from the formula already proved for connected graphs.

Thus a graph with at least two components has at most \(3n-6\) edges. This is strictly below the claimed value unless \((n-1)\bmod5=3\). In that residue class equality would require exactly two components, each itself attaining \(3k-3\). The possible orders of such connected components are all congruent to one modulo five: this is immediate for orders one and six, while for order at least nine it follows from the connected formula. Their two orders therefore sum to two modulo five, whereas here \(n\equiv4\pmod5\), impossible. Hence every extremizer for \(n\ge9\) is connected.

For \(n\le6\), the forbidden graph has seven vertices, so \(K_n\) is uniquely edge-maximal and gives \(\binom n2\). At \(n=7\), the construction \(K_1\vee B_6\) has seventeen edges; the same universal/nonuniversal root analysis bounds every connected graph by seventeen, and disconnected graphs have fewer. At \(n=8\), the graph
\[
(2K_2)\vee(2K_2)
\]
has twenty edges and is \(K_{2,5}\)-free. A nonuniversal connected cograph must have a \(4+4\) root split, and the four cross common neighbors force each side to have maximum degree at most one, so twenty is optimal; universal and disconnected cases are smaller.

## Verification
A standalone verifier independently enumerates all simple graphs through six vertices to recover the local component maxima
\[
0,1,3,6,10,11
\]
under the conditions cograph, \(K_{2,4}\)-free, and maximum degree at most four. It then solves the component knapsack problem through order five hundred, including all optimal component-count vectors, and reconstructs explicit extremal graphs through order forty to check induced-\(P_4\)-freeness, the \(K_{2,5}\) common-neighbor criterion, edge counts, and the alternative three-\(B_6\) residue-three construction.

The replay result is recorded in `verification/replay.txt`. These finite checks are stress tests; the all-order theorem follows from the proof above.

## Relationship to prior work
Zimmermann studies exactly the bipartite Turán problem restricted to cographs. His Pumping Theorem gives eventual periodic linearity and the linear coefficient \(s-1+(t-1)/2\); for \((s,t)=(2,5)\) this predicts coefficient three but not the exact period, correction, finite threshold, or extremal structures. His all-order structural theorem for \(K_{2,t}\) is stated only for \(t\in\{2,3\}\), and the paper explicitly notes that larger \(t\) can have small extremizers without a complete vertex.

A later public result determines the complete \(K_{2,4}\)-free cograph problem, including the exceptional six-vertex graph \(B_6\). The present theorem is not a specialization of that result: it uses the \(K_{2,4}\) theorem as the local remainder problem after removing a universal vertex, and the exceptional block changes the exact period-five optimization for \(K_{2,5}\). Targeted searches for \(K_{2,5}\)-free cographs, exact cograph Turán numbers, the periodic correction, and the exceptional-block formulation located the \(K_{2,4}\) result as the closest statement but no covering \(K_{2,5}\) theorem.

## Limitations
The theorem is restricted to cographs and ordinary-subgraph avoidance of \(K_{2,5}\). It does not address unrestricted Zarankiewicz numbers or induced \(K_{2,5}\)-avoidance. The originality comparison includes the initiating paper in full text and the closest public \(K_{2,4}\) result in full text; a finite dynamic-programming table associated with the initiating work could overlap individual small values without implying the closed all-order formula or extremal classification.

## References
1. Jakob Paul Zimmermann, *Bipartite Turán problem on cographs*, arXiv:2601.07406, first public 2026-01-12; especially the Pumping Theorem, the forbidden-star theorem, the \(K_{2,t}\) theorem for \(t\in\{2,3\}\), and the proof of the universal upper bound.
2. *Exact \(K_{2,4}\)-free Turán number for cographs*, public research record bb5427755569 (2026), including the all-order formula, the universal-vertex lemma for connected order at least seven, and the two six-vertex extremal types.
