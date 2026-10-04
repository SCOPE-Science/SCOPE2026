# Connected accurate domination of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), partite classes \(V_1,\ldots,V_r\), order \(N=\sum_i n_i\), \(q=|\{i:n_i=1}\|\), and \(M=\max_i n_i\). A set \(D\subseteq V(G)\) is an accurate dominating set when it dominates \(G\) and \(V(G)\setminus D\) contains no dominating set of cardinality \(|D|\); it is connected accurate when additionally \(G[D]\) is connected.

The complete classification is:

\[
|D|=1\quad\Longrightarrow\quad D\text{ is connected accurate dominating iff its vertex is the unique singleton part.}
\]

For \(s=|D|\ge2\), \(D\) is connected accurate dominating if and only if \(D\) meets at least two partite classes and
\[
N-s<s
\]
or else \(V(G)\setminus D\) is contained in at most one part and is not an entire part of order \(s\).

Consequently,
\[
\gamma_{ca}(G)=
\begin{cases}
1,&q=1,\\
\min_i n_i+1,&q\ne1\text{ and }r=2,\\
N-M,&q\ne1,\ r\ge3,\ 2M>N,\\
\lfloor N/2\rfloor+1,&q\ne1,\ r\ge3,\ 2M\le N.
\end{cases}
\]
The formula recovers the known complete-bipartite value \(\gamma_{ca}(K_{m,n})=m+1\) for \(2\le m\le n\) and the known complete-graph value \(\lfloor N/2\rfloor+1\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. Every part is nonempty and \(r\ge2\). The statement concerns connected accurate domination in the standard sense: accuracy excludes an equally large dominating set wholly inside the complement. The theorem classifies all connected accurate dominating sets and then minimizes their cardinality.

## Proof
First characterize domination in a complete multipartite graph. A nonempty set \(X\) dominates \(G\) exactly when either \(X\) meets at least two parts, or \(X\) equals one entire part. Indeed, a set meeting two parts dominates every vertex, while a set lying in one part fails to dominate any omitted vertex of that same part unless the whole part is selected.

Next characterize connected domination. A one-vertex set is connected and dominating exactly when it is a singleton part. If \(|D|\ge2\), then \(G[D]\) is connected exactly when \(D\) meets at least two parts; in that case it also dominates \(G\).

Let \(s=|D|\ge2\) and put \(C=V(G)\setminus D\). If \(|C|<s\), then \(C\) cannot contain an \(s\)-vertex set at all, so every connected dominating \(D\) is accurate. Assume now \(|C|\ge s\). If \(C\) meets at least two parts, choose an \(s\)-subset of \(C\) meeting two parts; by the first paragraph it dominates \(G\), so \(D\) is not accurate. If instead \(C\) is contained in one part \(V_j\), then an \(s\)-subset of \(C\) can dominate only by being the entire part \(V_j\). This happens exactly when \(C=V_j\) and \(n_j=s\). This proves the all-set criterion.

For \(|D|=1\), a connected dominating singleton must itself be a singleton part. Its complement contains another dominating singleton exactly when another singleton part exists. Hence a connected accurate singleton exists exactly when \(q=1\).

It remains to minimize. If \(q=1\), the value is \(1\). Suppose \(q\ne1\). When \(r=2\), any connected set of size at least two must meet both parts. Taking all vertices of a smaller part except that this would be disconnected, so one needs the whole smaller part together with one vertex of the other part, giving \(\min_i n_i+1\); the all-set criterion shows no smaller connected accurate set exists. Now let \(r\ge3\). If \(2M>N\), taking every vertex outside a largest part gives a connected set of size \(N-M\), its complement is the single largest part of size \(M>N-M\), and so it is accurate. Any smaller set leaves vertices in at least two parts or cannot dominate connectedly, proving optimality. If \(2M\le N\), no set of size at most \(\lfloor N/2\rfloor\) can satisfy the one-part-complement exception without encountering the equal-size whole-part obstruction; while every connected dominating set of size \(\lfloor N/2\rfloor+1\) is automatically accurate because its complement is smaller. Such a connected dominating set exists, so the stated value follows.

## Verification
A standalone verifier enumerates every nondecreasing complete-multipartite part profile through order \(10\). For each profile it checks every vertex subset against the literal definitions of domination, induced connectivity, and accuracy, compares the result with the structural criterion, and compares the minimum accepted size with the closed formula. It also rechecks the published complete-bipartite value for every tested bipartite profile with both parts of size at least two.

The finite census is a stress test only. The arbitrary-order theorem follows from the preceding structural proof.

## Relationship to prior work
Kulli and Kattimani introduced connected accurate domination and gave exact values for several standard graph families. Their Proposition 1 gives the complete-graph value \(\lfloor N/2\rfloor+1\), while Proposition 4 gives \(\gamma_{ca}(K_{m,n})=m+1\) for \(2\le m\le n\). The inspected full text contains no occurrence of “multipartite”. The present theorem retains those scalar cases as prior-covered and extends them to arbitrary complete multipartite graphs, including a full characterization of every connected accurate dominating set and the largest-part phase transition \(2M>N\).

Later work on accurate domination uses primary MSC \(05C69\), confirming domination-type ownership of the topic. That literature concerns accurate domination itself rather than supplying the connected-accurate complete-multipartite classification above.

## Limitations
The theorem is restricted to complete multipartite graphs. The verifier is exhaustive only through order \(10\); it is not an infinite proof. The originality comparison found no arbitrary complete-multipartite connected-accurate theorem, but poorly indexed literature under closely related accurate-domination terminology remains a residual risk. The earliest exact digital public date verified for the inspected connected-accurate source is its author-uploaded public copy dated 2016-01-03; the article itself is a December 2015 journal issue.

## References
1. V. R. Kulli and M. B. Kattimani, “Connected Accurate Domination in Graphs,” Journal of Computer and Mathematical Sciences 6(12) (2015), 682–687. Author-uploaded public copy: ResearchGate publication 288981776.
2. J. Cyman, M. A. Henning, and J. Topp, “On Accurate Domination in Graphs,” Discussiones Mathematicae Graph Theory 39 (2019), 615–627, doi:10.7151/dmgt.2182. Primary MSC includes 05C69.
