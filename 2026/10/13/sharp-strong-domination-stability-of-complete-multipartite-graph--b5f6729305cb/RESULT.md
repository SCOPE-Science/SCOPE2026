# Sharp strong-domination stability of complete multipartite graphs and optimal deletion witnesses

## Finding

Let \(G=K_{a_1,\ldots,a_r}\) be a finite simple complete multipartite graph with \(r\ge2\) nonempty parts. Put \(s=\min_i a_i\), let \(t=|\{i:a_i=s\}|\), and let \(c=|\{i:a_i=s+1\}|\). A set \(D\subseteq V(G)\) is strongly dominating when every vertex \(v\notin D\) has a neighbor \(u\in D\) with \(\deg_G(u)\ge\deg_G(v)\). Let \(\gamma_{\mathrm{st}}(G)\) be the minimum size of such a set, with \(\gamma_{\mathrm{st}}(\varnothing)=0\), and define the vertex-deletion stability
\[
\operatorname{st}_{\gamma_{\mathrm{st}}}(G)=\min\bigl\{|X|:X\subseteq V(G),\ \gamma_{\mathrm{st}}(G-X)\ne\gamma_{\mathrm{st}}(G)\bigr\}.
\]
Then the **exact stability** is
\[
\boxed{\operatorname{st}_{\gamma_{\mathrm{st}}}(G)=
\begin{cases}
 t,&s=1,\\
 2,&s=3\text{ and }t\ge2,\\
 1,&\text{otherwise}.
\end{cases}}
\]

More strongly, the complete list of *minimum-cardinality destabilizing deletion sets* is as follows.

1. If \(s=1\), the unique minimum deletion set is the union of all singleton parts (the set of all universal vertices).
2. If \(s\ge2\) and \(t=1\), a singleton deletion is optimal exactly when its vertex belongs to the unique smallest part, or when \(s\ge3\) and its vertex belongs to a part of size \(s+1\).
3. If \(s\ge2\), \(t\ge2\), and \(s\ne3\), the minimum deletion sets are precisely the single vertices in the smallest parts.
4. If \(s=3\) and \(t\ge2\), the minimum deletion sets are exactly the two-element subsets lying in one smallest part.

In particular, the number \(W(G)\) of minimum deletion sets is
\[
\boxed{W(G)=
\begin{cases}
 1,&s=1,\\
 s+(s+1)c,&t=1,\ s\ge3,\\
 s,&t=1,\ s=2,\\
 3t,&t\ge2,\ s=3,\\
 st,&t\ge2,\ s\ne3.
\end{cases}}
\]

## Assumptions and scope

All degrees used to test domination are computed **in the graph under consideration**, including after vertex deletion. Part sizes are positive integers; the original graph has at least two parts. After deletion, empty parts are discarded. A one-part graph on \(q\) vertices is edgeless and has strong domination number \(q\); the zero-vertex graph has value zero. Thus the complete-graph endpoint has stability equal to its order.

The result does not address edge deletion, weighted strong domination, strong Roman domination, or arbitrary graphs.

## Proof

**1. A degree-based lemma.** For a complete multipartite graph on \(N\) vertices, a vertex in a part of size \(a_i\) has degree \(N-a_i\). If the minimum part has size \(1\), any vertex in it is universal, so \(\gamma_{\mathrm{st}}=1\). If \(s\ge2\) and there is a unique smallest part \(A\), no vertex outside \(A\) can strongly dominate any vertex of \(A\): outside neighbors have strictly smaller degree. Hence every strongly dominating set contains all \(s\) vertices of \(A\). Conversely, selecting all vertices of \(A\) strongly dominates every outside vertex, so \(\gamma_{\mathrm{st}}=s\). If \(s\ge2\) and at least two parts have size \(s\), one selected vertex from each of two such parts strongly dominates all unselected vertices. No single vertex dominates its own nonadjacent part-mates, so \(\gamma_{\mathrm{st}}=2\). In summary, for at least two nonempty parts,
\[
\gamma_{\mathrm{st}}(G)=
\begin{cases}
1,&s=1,\\
s,&s\ge2\text{ and }t=1,\\
2,&s\ge2\text{ and }t\ge2.
\end{cases}
\]

**2. Singleton minimum parts.** Suppose \(s=1\). Any deletion omitting at least one of the original singleton vertices leaves a universal vertex, so the strong domination number stays at one. Deleting all \(t\) singleton vertices leaves either no vertices, a nonempty edgeless graph of order at least two, or a complete multipartite graph all of whose parts have size at least two. Each has strong domination number other than one. Thus the stability is \(t\), and the all-singleton deletion set is the unique optimum.

**3. Unique nonsingleton minimum.** Suppose \(s\ge2\) and \(t=1\). Initially \(\gamma_{\mathrm{st}}=s\). Removing a vertex from the unique smallest part creates a unique minimum of size \(s-1\), so the new number is \(s-1\). Hence the stability is one. For a vertex outside that part, deletion changes the minimum-size multiplicity precisely when its original part has size \(s+1\). In this case two parts become tied at size \(s\), producing strong domination number two; this differs from the original \(s\) precisely for \(s\ge3\). Deletions from larger parts have no effect. This proves the listed vertex set and its count \(s+(s+1)c\) when \(s\ge3\), or \(s\) when \(s=2\).

**4. Repeated nonsingleton minimum.** Suppose \(s\ge2\) and \(t\ge2\). Initially \(\gamma_{\mathrm{st}}=2\). Deleting one vertex from a smallest part makes it uniquely smallest of size \(s-1\). The new strong domination number is one for \(s=2\), two for \(s=3\), and \(s-1\ge3\) for \(s\ge4\). Deleting one vertex from a larger part leaves at least two parts of minimum size \(s\), and hence cannot change the value two. Therefore if \(s\ne3\), the stability is one and exactly the \(st\) vertices of minimum parts are minimum deletion sets.

Finally let \(s=3\) and \(t\ge2\). Every one-vertex deletion leaves strong domination number two, as just shown. Deleting two vertices from one three-vertex part creates a singleton, so the number becomes one. Conversely, a two-vertex deletion containing no such pair creates no singleton. If it creates a part of size two, either that part is a unique minimum (forcing strong domination number two), or the minimum is attained in multiple parts (also giving two). If it creates no part of size two, the original three-vertex minimum remains repeated, and again the number is two. Hence exactly the \(t\binom32=3t\) same-part pairs are minimum deletion witnesses. This completes both formulas and the classification.

## Verification

A standalone dependency-free checker in `artifacts/verify.py` constructs the multipartite graph explicitly and determines its strong domination number from its vertex-degree inequalities, without using the structural lemma. It examines every integer-partition profile of orders \(2\) through \(11\) with at least two parts, every deletion subset until the first change, and the count of minimum witnesses. All \(183\) profiles and \(36{,}315\) relevant deletion subsets agree. The checker also independently compares the explicit instances \(K_{4,4,4}\) and \(K_{3,3,3}\) against their post-deletion graphs. Execute `python artifacts/verify.py` from the package root; `artifacts/verification_output.txt` records the actual output. Finite enumeration supports but is not used as an infinite proof.

## Relationship to prior work

Alikhani, Ghanbari, Mehraban, and Shojaaldini Ardakani study the same strong-domination stability parameter in *Stability of the Strong Domination Number of Graphs* (arXiv:2601.03891; first public 7 January 2026). Its inspected versions discuss balanced multipartite graphs and complete bipartite graphs. The present result covers **every** nonempty complete multipartite part-size profile, with the precise minimum witnesses and their number. It is not a consequence of the cited balanced-case claims: some printed conclusions there disagree with direct degree-based calculations. For example, deleting one vertex from \(K_{4,4,4}\) changes \(\gamma_{\mathrm{st}}\) from two to three, while deleting two vertices from the same part of \(K_{3,3,3}\) changes it from two to one, and no single deletion changes the latter. These are proved here directly rather than obtained from a disputed prior assertion.

The enumeration of super-dominating, Roman-dominating, and paired-dominating sets in multipartite graphs concerns distinct predicates; it does not imply vertex-deletion stability under **degree-qualified** strong domination.

## Limitations

The result is restricted to finite simple complete multipartite graphs. The notion of stability depends on the stated convention for the empty graph; without permitting deletion of every vertex, the complete-graph endpoint must be handled separately. Originality searches can miss equivalent formulations or later corrections to the motivating preprint. No independent external audit is asserted.

## References

1. S. Alikhani, N. Ghanbari, M. Mehraban, H. Shojaaldini Ardakani, *Stability of the Strong Domination Number of Graphs*, arXiv:2601.03891v2, 29 August 2026, https://arxiv.org/html/2601.03891v2. First public version arXiv:2601.03891v1, 7 January 2026, https://arxiv.org/html/2601.03891v1.
