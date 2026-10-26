# Complete multipartite strong-domination stability and all minimum changing deletions

## Finding

**Theorem.** Let \(G=K_{s_1,\ldots,s_r}\) be a finite complete multipartite graph with \(r\ge2\), positive integer part sizes, and at least one part of size at least two. Let \(m=\min_i s_i\), let \(a\) be the number of parts of size \(m\), and let \(k\) be the number of singleton parts. For every nonempty graph, a strong dominating set \(D\) requires that every \(v\notin D\) has a neighbor \(u\in D\) with \(\deg_G(u)\ge\deg_G(v)\); write \(\gamma_{\mathrm{st}}(G)\) for its minimum size. Define

\[
\operatorname{st}_{\gamma_{\mathrm{st}}}(G)=
\min\bigl\{|S|:S\subsetneq V(G),\ \gamma_{\mathrm{st}}(G-S)\ne\gamma_{\mathrm{st}}(G)\bigr\}.
\]

Then this minimum exists, and

\[
\boxed{\operatorname{st}_{\gamma_{\mathrm{st}}}(G)=
\begin{cases}
k,&k>0,\\
2,&k=0,\ m=3,\ a\ge2,\\
1,&\text{otherwise}.
\end{cases}}
\]

Moreover **all** minimum changing deletion sets are characterized as follows.

1. If \(k>0\), the unique set is the union of the singleton parts (size \(k\)).
2. If \(k=0\), \(m=3\), and \(a\ge2\), the sets are exactly the two-element subsets of an individual size-three part. There are \(3a\) such sets.
3. In every remaining case, the minimum sets are singleton vertices. The eligible vertices are: all vertices of size-two parts if \(m=2\); all vertices of the unique smallest part and of the size-\(m+1\) parts if \(m\ge3\) and \(a=1\); or all vertices in the smallest parts if \(m\ge4\) and \(a\ge2\).

In particular, for \(r\ge2\), \(p\ge2\),

\[
\operatorname{st}_{\gamma_{\mathrm{st}}}(K_{\underbrace{p,\ldots,p}_{r\text{ parts}}})=
\begin{cases}2,&p=3,\\1,&p=2\text{ or }p\ge4.\end{cases}
\]

## Assumptions and scope

Graphs are finite, simple, and undirected. All degrees in the strong-dominating condition are **recomputed inside the current induced graph**, including after deletions. A deletion set must be a proper subset of the vertex set, so the empty graph is never evaluated. A one-part graph \(K_{s_1}\) is an independent set and is not needed for the theorem. If all parts are singletons, the graph is complete and its strong domination number is always one after any proper deletion; its stability minimum is undefined under this convention and is explicitly excluded.

The size and count classifications refer to vertex sets, not to unlabeled graph-isomorphism types.

## Proof

**Part-size lemma.** For a nonempty complete multipartite graph \(H\) with positive part sizes \(t_1,\ldots,t_q\), set \(b=\min_i t_i\). If \(b=1\), then \(\gamma_{\mathrm{st}}(H)=1\). If \(b\ge2\) is achieved in at least two parts, then \(\gamma_{\mathrm{st}}(H)=2\). If \(b\ge2\) occurs in exactly one part, then \(\gamma_{\mathrm{st}}(H)=b\). These conclusions also hold for \(q=1\), when the last case has value \(t_1\).

Indeed, the degree of a vertex in part \(i\) is \(T-t_i\), where \(T=|V(H)|\). Thus a vertex selected from part \(j\) can strongly dominate an outside vertex in another part \(i\) exactly when \(t_j\le t_i\). A singleton vertex is universal, proving the first case. When two minimum parts exist, selecting one vertex from each gives a two-vertex strong dominating set, and two are necessary since no vertex is universal. If the minimum part is unique and has size \(b\ge2\), no vertex outside it has degree at least that of its vertices. Every one of its vertices must therefore be selected; selecting the entire minimum part strongly dominates every other part, yielding value \(b\).

**Graphs containing singleton parts.** Initially \(\gamma_{\mathrm{st}}(G)=1\). If fewer than \(k\) vertices are deleted, an original singleton vertex remains and is still universal, so the value remains one. Deleting all \(k\) singleton vertices leaves only parts of size at least two. At least one such part remains by hypothesis. The residual graph has no universal vertex (even if just one independent part remains), so its strong domination number is at least two. This proves stability \(k\), and also shows that its unique minimum deletion set contains all \(k\) singleton vertices.

**Graphs without singleton parts.** Put \(m=\min_i s_i\) and let \(a\) count minimum parts. The part-size lemma gives initial value \(2\) when \(a\ge2\), and \(m\) when \(a=1\).

If \(m=2\), the initial value is two. Deleting any vertex from a size-two part creates a singleton part and changes the value to one. Deleting one vertex from any other part leaves minimum size two, still with initial value two: the minimum size-two parts survive, and a newly created size-two part only adds a tie. Thus the changing vertices are exactly those of size-two parts.

If \(m=3\) and \(a=1\), the initial value is three. Deleting a vertex from the unique size-three part creates a unique size-two part and changes the value to two. Deleting from a size-four part creates a second minimum size-three part, again changing the value to two. Deleting a vertex from a larger part leaves the unique minimum size-three part and the value three. This proves the stated classification in this case.

If \(m\ge4\) and \(a=1\), initially the value is \(m\). Deleting from the unique minimum part creates a unique minimum of size \(m-1\ge3\), changing the value to \(m-1\). Deleting from a size-\(m+1\) part creates a tie at size \(m\), changing the value to two. Deleting elsewhere preserves the unique minimum size \(m\) and its strong domination number. These are precisely the changing singleton deletions.

If \(m\ge4\) and \(a\ge2\), initially the value is two. Deleting from any minimum part yields a *unique* new minimum of size \(m-1\ge3\), changing the strong domination number to \(m-1\). Deleting from any other part either creates one more part of size \(m\) or leaves the original minimum parts unchanged; in either case the value remains two. Hence only vertices of minimum parts are changing singleton sets.

Finally, suppose \(m=3\) and \(a\ge2\). The initial value is two. Any single deletion either creates one unique size-two minimum part (if it strikes a size-three part) or leaves at least two size-three minimum parts. In both cases the part-size lemma gives value two. Deleting two vertices from the same size-three part produces a singleton vertex, hence value one. To classify **all** changing pairs, observe that a two-vertex deletion with no singleton part leaves all parts of size at least two. It can create a size-two part only by taking one vertex from an original size-three part or two vertices from an original size-four part. If exactly one size-two part is created, the strong domination number remains two by the unique-minimum clause; if several are created, the repeated-minimum clause likewise gives two. If none is created, at least the original size-three minimum parts remain (or the smaller size-three parts created by deletion), and the strong domination number is again two. Thus no pair lacking a singleton can change the value. The only way to create a singleton in two deletions is to remove two vertices from one size-three part. Exactly \(a\binom32=3a\) such vertex pairs exist.

These exhaustive cases establish both the stability formula and the complete minimum-deletion classification. The balanced specialization follows immediately. \(\square\)

## Verification

The accompanying `verify_strong_stability.py` uses a direct adjacency-mask definition of strong domination, recomputes degrees after each deletion, and exhaustively checks the theorem's parameter, minimum deletion sets, and original strong domination number for every integer partition of total order three through eleven with at least two positive parts: 182 part-size profiles. The script enumerates actual vertex sets, not only part-size transitions. Run `python3 verify_strong_stability.py`; expected final line: `VERIFY_OK`. Finite tests are independent corroboration, not an infinite proof.

For example, \(K_{2,2,2}\) has initial strong domination number two, while deleting one vertex creates a universal vertex in \(K_{1,2,2}\), making the new number one. For \(K_{3,3,3}\), all single-vertex deletions retain value two, but deleting two vertices from one part creates a universal vertex and changes the number to one.

## Relationship to prior work

Alikhani, Mehraban, and Shojaaldini Ardakani, *Stability of the Strong Domination Number of Graphs*, arXiv:2601.03891v1 (first publicly submitted 2026-01-07), introduced the stability parameter and studied complete bipartite and balanced complete multipartite graphs. Its Section 2.1 asserts \(\operatorname{st}_{\gamma_{\mathrm{st}}}(K_{p,p,p})=p+1\) and proposes further determination for general balanced multipartite graphs (Theorem 2.12 and Remark 2.14). Under the paper's own strong-dominating definition, the elementary induced-degree examples above conflict with that numerical assertion already at \(p=2\) and \(p=3\). The present classification proves the actual deletion behavior directly from the definition, for arbitrary part sizes, including all balanced cases; it does not rely on those prior numerical assertions.

Alikhani and Ghanbari, *Strong domination number of a modified graph*, arXiv:2212.01860v1 (2022), Theorem 2.1, gives general upper and lower bounds for a single vertex deletion of an arbitrary graph. Those inequalities do not specify which vertices change the value for complete multipartite graphs, nor their exact deletion stability and minimum deletion-set enumerator. The earlier foundational paper by Zaherifar, Alikhani, and Ghanbari, *On the Strong Dominating Sets of Graphs* (Journal of Algebraic Systems 11 (2023), 65–76), concerns strong domination and enumeration in specific families; its full text was not available in this review and its detailed coverage remains a bibliographic risk.

## Limitations

The result concerns strong domination under **vertex deletion**, not strong Roman domination, ordinary domination stability, edge modifications, or other graph classes. All claims are proved under the explicitly stated proper-deletion convention. The complete-graph case has no changing proper deletion, and no finite stability is asserted for it. Independent mathematical review has not been performed. The literature comparison is evidence of a gap, not a proof of publication priority; a theorem phrased through degree orders or domination-critical sets might exist elsewhere.

## References

1. S. Alikhani, M. Mehraban, H. Shojaaldini Ardakani, *Stability of the Strong Domination Number of Graphs*, arXiv:2601.03891v1, submitted 2026-01-07. https://arxiv.org/abs/2601.03891
2. S. Alikhani, N. Ghanbari, *Strong domination number of a modified graph*, arXiv:2212.01860v1, submitted 2022-12-04. https://arxiv.org/abs/2212.01860
3. H. Zaherifar, S. Alikhani, N. Ghanbari, *On the Strong Dominating Sets of Graphs*, Journal of Algebraic Systems 11 (2023), 65–76, DOI:10.22044/JAS.2022.11646.1595.
