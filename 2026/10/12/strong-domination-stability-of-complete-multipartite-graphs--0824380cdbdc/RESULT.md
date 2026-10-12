# Strong-domination stability of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected noncomplete complete multipartite graph with \(r\ge2\), positive part sizes, \(s=\min_i n_i\), and \(q=|\{i:n_i=s\}|\). Under the convention that \(u\) strongly dominates an adjacent vertex \(v\) when \(\deg(u)\ge\deg(v)\),
\[
\gamma_{st}(G)=
\begin{cases}
1,&s=1,\\
s,&s\ge2\text{ and }q=1,\\
2,&s\ge2\text{ and }q\ge2.
\end{cases}
\]
For the vertex-deletion stability \(\operatorname{st}_{\gamma_{st}}(G)\), defined as the minimum cardinality of a proper vertex set whose deletion changes \(\gamma_{st}\),
\[
\operatorname{st}_{\gamma_{st}}(G)=
\begin{cases}
q,&s=1,\\
2,&s=3\text{ and }q\ge2,\\
1,&\text{otherwise}.
\end{cases}
\]
Thus a balanced complete multipartite graph \(K_{p,\ldots,p}\) with at least two parts has stability \(2\) exactly for \(p=3\), and stability \(1\) for every other \(p\ge2\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The graph is assumed connected and noncomplete, so at least two partite classes are present and at least one class has size at least two. This excludes the complete-graph convention issue for vertex-deletion stability. Deletion may remove whole partite classes, but the deletion set is proper, so at least one vertex remains.

## Proof
For a vertex in a part of size \(a\), its degree is \(N-a\), where \(N=|V(G)|\). Hence a vertex in a part of size \(b\) can strongly dominate a vertex in a different part of size \(a\) exactly when
\[
N-b\ge N-a,
\]
that is, exactly when \(b\le a\).

This degree-order rule immediately gives \(\gamma_{st}(G)\). If \(s=1\), a vertex in a singleton part is universal, so \(\gamma_{st}(G)=1\). Suppose \(s\ge2\). If the smallest part is unique, no vertex outside it has sufficiently large degree to strongly dominate one of its vertices, so every vertex of that smallest part belongs to every strong dominating set. The whole smallest part strongly dominates every vertex outside it, and therefore \(\gamma_{st}(G)=s\). If at least two smallest parts exist, one vertex chosen from each of two smallest parts strongly dominates every unchosen vertex; one vertex cannot dominate the other vertices in its own part, so \(\gamma_{st}(G)=2\).

Now consider stability. If \(s=1\), let \(q\) be the number of singleton parts. Any deletion of fewer than \(q\) vertices leaves an original singleton part, hence leaves a universal vertex and keeps \(\gamma_{st}=1\). Deleting all \(q\) singleton vertices removes every singleton part. Because the original graph is noncomplete, at least one part of size at least two remains; the resulting graph has strong domination number at least \(2\). Thus \(\operatorname{st}_{\gamma_{st}}(G)=q\).

If \(s\ge2\) and the smallest part is unique, deleting one vertex from it changes the strong domination number: when \(s=2\) a singleton part is created, giving value \(1\), and when \(s\ge3\) the same part remains uniquely smallest with size \(s-1\), giving value \(s-1\). Hence the stability is \(1\).

It remains to consider \(s\ge2\) with at least two smallest parts, where initially \(\gamma_{st}=2\). If \(s=2\), deleting one vertex from a smallest part creates a singleton part and changes the value to \(1\). If \(s\ge4\), deleting one vertex from a smallest part creates a unique smallest part of size \(s-1\ge3\), so the new strong domination number is \(s-1\ne2\). Thus the stability is \(1\) in both cases. If \(s=3\), one deletion cannot change the value: deleting from a smallest part creates a unique part of size \(2\), whose strong domination number is still \(2\); deleting from a larger part either leaves the minimum profile unchanged or creates another part of size \(3\), again giving value \(2\). Deleting two vertices from one smallest part creates a singleton part, so the value becomes \(1\). Hence the stability is \(2\) exactly in this remaining case.

## Verification
A direct exhaustive checker independently constructs every noncomplete complete multipartite graph whose order is at most \(8\), computes \(\gamma_{st}\) from the definition by enumerating candidate strong dominating sets, computes stability by enumerating every proper vertex-deletion set, and compares both values with the formulas above. The replay reports:

`ALL CHECKS PASSED; profiles=51; gamma_checks=51; stability_checks=51; order_range=2..8`

The finite replay is a stress test only; the theorem for arbitrary part sizes follows from the preceding degree-order proof.

## Relationship to prior work
Alikhani, Ghanbari, Mehraban, and Shojaaldini Ardakani introduced the vertex-deletion stability of the strong domination number in arXiv:2601.03891. Their current preprint treats complete bipartite graphs and balanced complete multipartite graphs, and explicitly presents the balanced case as requiring a more complicated dependence on the part size and number of parts. The degree-order argument above instead gives an exact classification for every complete multipartite part-size profile and, in the balanced family, yields the two-valued rule stated here.

Earlier strong-domination literature, including Vaidya and Karkar's 2017 paper, studies the underlying strong domination number but not this 2026 vertex-deletion stability parameter. Searches for the same statement under the aliases “strong domination stability,” “vertex-deletion stability of strong domination,” “balanced complete multipartite,” “Turan graph,” and the notation \(\gamma_s\) or \(\gamma_{st}\) did not locate an earlier theorem implying the classification above.

## Limitations
The result uses the non-strict degree convention \(\deg(u)\ge\deg(v)\) used in the initiating 2026 stability paper. Literature using strict strong domination is a different invariant. Complete graphs are excluded because the initiating paper itself notes a convention issue when no proper deletion changes the value. The external literature search cannot rule out an older poorly indexed equivalent statement under different notation, and the 2026 preprint may later be revised.

## References
1. S. Alikhani, N. Ghanbari, M. Mehraban, H. Shojaaldini Ardakani, *Stability of the Strong Domination Number of Graphs*, arXiv:2601.03891v2, 2026. First public version: 2026-01-07.
2. S. K. Vaidya and S. H. Karkar, *On Strong Domination Number of Graphs*, Applications and Applied Mathematics 12(1), Article 39, 2017.
