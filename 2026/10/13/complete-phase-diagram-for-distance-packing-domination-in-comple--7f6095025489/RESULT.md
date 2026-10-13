# Complete phase diagram for distance-packing domination in complete multipartite graphs

## Finding

Let
\[
G=K_{n_1,\ldots,n_r}
\]
be a connected complete multipartite graph with
\[
r\ge2,\qquad N=\sum_{i=1}^r n_i,
\]
and let
\[
q=\bigl|\{i:n_i=1\}\bigr|
\]
be the number of singleton parts.

For nonnegative integers \(d,p\), define the full cardinality enumerator
\[
\mathcal P_{d,p}(G;x)
=
\sum_{S}x^{|S|},
\]
where the sum ranges over all vertex sets \(S\) that are both \(d\)-distance dominating and \(p\)-packings.

Then
\[
\boxed{
\mathcal P_{d,p}(G;x)=
\begin{cases}
x^N,&d=0,\ p=0,\\
0,&d=0,\ p\ge1,\\
(1+x)^N-\sum_i(1+x)^{n_i}+r-1+\sum_i x^{n_i},&d=1,\ p=0,\\
\sum_i x^{n_i},&d=1,\ p=1,\\
qx,&d=1,\ p\ge2,\\
(1+x)^N-1,&d\ge2,\ p=0,\\
\sum_i\bigl((1+x)^{n_i}-1\bigr),&d\ge2,\ p=1,\\
Nx,&d\ge2,\ p\ge2.
\end{cases}}
\]

Taking the least exponent with a nonzero coefficient gives the exact parameter
\[
\boxed{
\gamma_d^p(G)=
\begin{cases}
N,&d=0,\ p=0,\\
\infty,&d=0,\ p\ge1,\\
1,&d=1,\ p=0,\ q\ge1,\\
2,&d=1,\ p=0,\ q=0,\\
\min_i n_i,&d=1,\ p=1,\\
1,&d=1,\ p\ge2,\ q\ge1,\\
\infty,&d=1,\ p\ge2,\ q=0,\\
1,&d\ge2.
\end{cases}}
\]

Thus the entire two-parameter family collapses to eight regimes on complete multipartite graphs, and every feasible set is counted explicitly.

## Assumptions and scope

Graphs are finite, simple, and connected. The partite classes of \(G\) are nonempty and \(r\ge2\).

For nonnegative integers \(d,p\), a set \(S\subseteq V(G)\) is \(d\)-distance dominating when every vertex outside \(S\) is at graph distance at most \(d\) from some vertex of \(S\). It is a \(p\)-packing when every two distinct vertices of \(S\) are at distance at least \(p+1\). The number \(\gamma_d^p(G)\) is the minimum size of a set satisfying both conditions, with value \(\infty\) if none exists.

The result includes ordinary domination at \((d,p)=(1,0)\), independent domination at \((1,1)\), and several trivial large-distance regimes. Those individual special cases are classical; the finding is the simultaneous all-parameter classification and full feasible-set enumerator.

## Proof

In a connected complete multipartite graph, two vertices in different parts are adjacent and hence have distance \(1\), while two distinct vertices in the same part have distance \(2\). Therefore every nonzero graph distance is either \(1\) or \(2\).

First consider the packing condition.

If
\[
p=0,
\]
then the required separation is at least \(1\), so every vertex subset is a \(0\)-packing.

If
\[
p=1,
\]
then selected vertices must be pairwise nonadjacent. In a complete multipartite graph this means that every nonempty \(1\)-packing lies entirely in one part.

If
\[
p\ge2,
\]
then selected vertices would have to be pairwise at distance at least \(3\). Since the graph has diameter at most \(2\), every \(p\)-packing has size at most one.

Now consider distance domination.

If
\[
d=0,
\]
no outside vertex can be dominated, because its distance from every selected vertex is positive. Hence the only \(0\)-distance dominating set is
\[
V(G).
\]

If
\[
d=1,
\]
the condition is ordinary domination. A set dominates a complete multipartite graph precisely when it either meets at least two parts or is one whole part. Indeed, meeting two parts immediately dominates every vertex, while a set contained in one part fails to dominate omitted vertices of that same part unless the whole part is selected.

If
\[
d\ge2,
\]
every nonempty set is distance dominating, since the diameter of the graph is at most \(2\).

Combining the three packing regimes with the three domination regimes yields the polynomial case by case.

For
\[
d=0,
\]
the only candidate is \(V(G)\). It is a \(0\)-packing and is not a \(p\)-packing for any \(p\ge1\), because \(N\ge2\). This gives the first two cases.

For
\[
d=1,\ p=0,
\]
all dominating sets are allowed. The subsets meeting at least two parts are counted by
\[
(1+x)^N-1-\sum_i\bigl((1+x)^{n_i}-1\bigr)
=
(1+x)^N-\sum_i(1+x)^{n_i}+r-1.
\]
Adding the whole-part dominating sets gives
\[
(1+x)^N-\sum_i(1+x)^{n_i}+r-1+\sum_i x^{n_i}.
\]

For
\[
d=1,\ p=1,
\]
a feasible set must lie in one part and dominate, hence it must equal that whole part. The polynomial is therefore
\[
\sum_i x^{n_i}.
\]

For
\[
d=1,\ p\ge2,
\]
a feasible set has size at most one. A singleton dominates exactly when its vertex is universal, which in a complete multipartite graph occurs exactly in singleton parts. Hence the polynomial is
\[
qx.
\]

For
\[
d\ge2,\ p=0,
\]
every nonempty subset is feasible, giving
\[
(1+x)^N-1.
\]

For
\[
d\ge2,\ p=1,
\]
every nonempty independent subset is feasible. Such a set lies in a unique part, so the polynomial is
\[
\sum_i\bigl((1+x)^{n_i}-1\bigr).
\]

Finally, for
\[
d\ge2,\ p\ge2,
\]
the feasible sets are exactly the \(N\) singletons, giving
\[
Nx.
\]

The formula for \(\gamma_d^p(G)\) follows by taking the smallest nonzero exponent in each case. In the ordinary-domination case, a singleton dominating set exists exactly when \(q\ge1\); otherwise any two vertices from different parts dominate, so the minimum is \(2\).

## Verification

The accompanying script `artifacts/verify.py` enumerates every nondecreasing complete-multipartite part-size profile of total order \(2\) through \(8\). For every profile and every parameter pair
\[
0\le d,p\le4,
\]
it checks every vertex subset directly from the graph-distance definitions.

The resulting coefficient vector is compared with the displayed closed polynomial. The least feasible cardinality is also compared implicitly through the first nonzero coefficient.

Replay output:

`ALL CHECKS PASSED; profiles=58; parameter_cases=1450; subset_checks=202100; orders=2..8; d,p=0..4`

The finite computation is corroborative only. The arbitrary-order result follows from the distance-\(1\)/distance-\(2\) structure proved above.

## Relationship to prior work

Bujtás, Iršič Chenoweth, Klavžar, and Zhang revived the \(d\)-distance \(p\)-packing domination parameter in recent work. Their first paper, first public on July 24, 2025, determines the parameter on paths and cycles, proves complexity results, and develops bounds for trees. Their strong-product follow-up, first public on October 3, 2025, studies exact product formulas and nonexistence phenomena. The journal metadata for these papers lists primary MSC \(05C69\).

Neither inspected paper states a complete-multipartite classification. The complete-multipartite result here is not inferred from a product theorem; it instead uses the exact two-level distance metric of the family.

Some cells of the table are classical facts in different language. In particular,
\[
\gamma_1^0
\]
is ordinary domination and
\[
\gamma_1^1
\]
is independent domination. These special cases are not claimed as separate novelties. The new statement is the full parameter-plane phase diagram together with the enumerator of every feasible set in every regime.

Targeted database searches under the current terminology, the older \((p,d)\)-domination terminology, and the distance-independent-domination specialization did not locate an equivalent complete-multipartite theorem.

## Limitations

The collapse to finitely many regimes depends on the fact that all nonzero distances in a complete multipartite graph are \(1\) or \(2\). The formulas therefore do not extend unchanged to multipartite graphs with missing cross edges or to graph products with diameter larger than \(2\).

The result is structurally simple. Its value lies in resolving the whole two-parameter family and all feasible-set counts at once, not in a technically deep proof.

Originality is literature-based. The parameter dates to 1994 under the older name \((p,d)\)-domination, so a poorly indexed special-case statement under historical terminology remains a residual risk.

## References

1. C. Bujtás, V. Iršič Chenoweth, S. Klavžar, and G. Zhang, “The \(d\)-distance \(p\)-packing domination number: complexity, cycles, and trees,” arXiv:2507.18272v1, first public July 24, 2025; Aequationes Mathematicae 100 (2026), article 25, DOI 10.1007/s00010-026-01266-w.
2. C. Bujtás, V. Iršič Chenoweth, S. Klavžar, and G. Zhang, “On \(d\)-distance \(p\)-packing domination number in strong products,” arXiv:2510.02749v1, first public October 3, 2025; Annals of Combinatorics (2026), DOI 10.1007/s00026-026-00814-0.
3. L. W. Beineke and M. A. Henning, “Some extremal results on independent distance domination in graphs,” Ars Combinatoria 37 (1994), 223–233.
