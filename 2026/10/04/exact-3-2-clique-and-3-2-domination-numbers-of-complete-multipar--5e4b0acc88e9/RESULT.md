# Exact \((3,2)\)-clique and \((3,2)\)-domination numbers of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), all \(n_i\ge1\), and \(N=\sum_i n_i\). Put
\[
s=\left|\left\{i:n_i\ge2\right\}\right|.
\]
For the \((k,d)\)-invariants of Cody and Detore at \((k,d)=(3,2)\),
\[
\omega^3_2(G)=2+\min\{2,s\},
\]
and
\[
\gamma^3_2(G)=
\begin{cases}
N,&s=0,\\
2,&s>0\text{ and }(r=2\text{ or }n_i=2\text{ for some }i),\\
3,&\text{otherwise.}
\end{cases}
\]
Thus every noncomplete complete multipartite graph has \((3,2)\)-domination number at most \(3\). It equals \(3\) exactly when there are at least three parts and every non-singleton part has size at least \(3\).

## Assumptions and scope
Graphs are finite, simple, and connected. A \((3,2)\)-clique is a vertex set \(Q\) such that every three-element subset of \(Q\) is contained in a shortest path of length at most \(2\). A \((3,2)\)-dominating set is a vertex set \(D\) such that for every \(v\notin D\), some shortest path of length at most \(2\) contains \(v\) and at least two vertices of \(D\). The theorem covers all complete multipartite graphs with at least two nonempty parts, including complete graphs.

## Proof
In a complete multipartite graph, vertices in distinct parts are adjacent, while two vertices in the same part are at distance \(2\) unless the graph is complete. Hence a shortest path with three vertices has its two endpoints in one part and its middle vertex in another part. Therefore a three-vertex set is contained in a shortest path of length at most \(2\) if and only if its part multiplicities are exactly \(2+1\).

For the clique number, suppose \(|Q|\ge3\). If \(Q\) contains three vertices from one part, those three do not have multiplicity \(2+1\), so every part contributes at most two vertices to \(Q\). If \(Q\) meets three distinct parts, choosing one vertex from each gives multiplicity \(1+1+1\), again impossible. Thus any \((3,2)\)-clique of size at least three meets at most two parts and uses at most two vertices from each. If no part has size at least two, the largest clique has size \(2\). If exactly one part has size at least two, two vertices from it together with one vertex from another part form a clique of size \(3\). If at least two parts have size at least two, taking two vertices from each of two such parts gives a clique of size \(4\). This proves \(\omega^3_2(G)=2+\min\{2,s\}\).

For domination, first assume that all parts are singletons. Then \(G\) is complete, so every shortest path has at most two vertices. No vertex outside a set \(D\) can lie on a shortest path containing two vertices of \(D\). Hence only \(D=V(G)\) is \((3,2)\)-dominating, and \(\gamma^3_2(G)=N\).

Now suppose \(s>0\). A two-vertex set \(D\) dominates a vertex \(v\notin D\) exactly when \(D\cup\{v\}\) has part multiplicities \(2+1\). If the two vertices of \(D\) lie in the same part, this succeeds for every outside vertex exactly when that part has size \(2\). If the two vertices of \(D\) lie in different parts, this succeeds for every outside vertex exactly when there is no third part, namely when \(r=2\). Consequently \(\gamma^3_2(G)=2\) exactly in the stated cases.

It remains to consider a noncomplete graph with \(r\ge3\) and no part of size \(2\). Some part \(A\) then has size at least \(3\). Choose two vertices \(a_1,a_2\in A\) and one vertex \(b\) outside \(A\), and put \(D=\{a_1,a_2,b\}\). If \(v\notin D\) lies outside \(A\), then \(a_1-v-a_2\) is a shortest path containing two vertices of \(D\). If \(v\in A\setminus D\), then \(v-b-a_1\) is a shortest path containing two vertices of \(D\). Hence \(D\) is \((3,2)\)-dominating. The two-vertex classification already proved rules out a smaller set, so \(\gamma^3_2(G)=3\).

## Verification
The accompanying `verify.py` constructs each complete multipartite graph directly, enumerates its shortest paths of length at most \(2\), and then computes \(\omega^3_2\) and \(\gamma^3_2\) from the definitions without using the theorem's structural lemma. Every integer partition of every order from \(2\) through \(10\) with at least two parts is checked. The finalized replay reports `ALL CHECKS PASSED; multipartite_types=128; max_order=10`.

## Relationship to prior work
Cody and Detore introduced the \((k,d)\)-independence, chromatic, clique, and domination invariants and gave exact results for paths and cycles. Their paper lists primary MSC 05C12 and does not state complete-multipartite formulas for the \((3,2)\)-clique or \((3,2)\)-domination numbers. The earlier general-position-coloring paper of Chandran S.V., Di Stefano, Haritha, Thomas, and Tuite determines the general-position chromatic number of complete multipartite graphs; for diameter-two graphs that concerns the \((3,2)\)-chromatic invariant, not the clique or domination invariants proved here. Earlier general-position-set work determines maximum no-three-on-a-geodesic sets and likewise does not imply either formula above.

## Limitations
The theorem concerns only \((k,d)=(3,2)\) and complete multipartite graphs. The finite exhaustive computation through order \(10\) is a stress test, not the proof of the infinite statement. Search-based originality checks cannot prove absolute absence from all literature; no covering statement was found in the inspected primary papers or semantic searches.

## References
1. Brent Cody and Rose Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351, first public 2026-01-07; primary MSC 05C12.
2. Ullas Chandran S.V., Gabriele Di Stefano, Haritha S., Elias John Thomas, and James Tuite, *Colouring a graph with position sets*, arXiv:2408.13494, first public 2024-08-24.
3. Bijo S. Anand, Ullas Chandran S. V., Manoj Changat, Sandi Klavžar, and Elias John Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460, first public 2018-12-20.
