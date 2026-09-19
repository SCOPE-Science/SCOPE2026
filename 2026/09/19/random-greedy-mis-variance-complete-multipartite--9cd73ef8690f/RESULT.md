# Sharp variance of random greedy maximal independent sets on complete multipartite graphs

Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph, with
\(r\ge 2\), \(n_i\ge 1\), and \(n=\sum_i n_i\). Run the random greedy maximal
independent-set algorithm: inspect the vertices in a uniformly random order and
accept a vertex exactly when it has no previously accepted neighbor. Let \(X_G\)
be the size of the resulting maximal independent set.

## Exact law

The first inspected vertex is accepted. Every later vertex in the same
multipartite class is nonadjacent to it and is eventually accepted, whereas
every vertex in another class is adjacent to the first accepted vertex and is
rejected. Hence the output is exactly the part containing the first vertex.

Consequently, for every integer \(s\ge 1\),
\[
 \Pr(X_G=s)=\frac{s}{n}\,\#\{i:n_i=s\},
\]
and, for every integer \(k\ge 1\),
\[
 \mathbb E[X_G^k]=\frac1n\sum_{i=1}^r n_i^{k+1}.
\]
In particular,
\[
 \boxed{\operatorname{Var}(X_G)
 =\frac1n\sum_i n_i^3-\left(\frac1n\sum_i n_i^2\right)^2.}
\]

The distribution is therefore the size-biased distribution of the
multipartite class sizes.

## Sharp finite-order extremum

For \(n\ge 3\), define
\[
 \rho_n=\frac{3n+\sqrt{9n^2-16n}}8,
 \qquad
 a_n=\lceil \rho_n\rceil .
\]
Then among all connected complete multipartite graphs on \(n\) vertices,
\[
 \boxed{
 \max_G \operatorname{Var}(X_G)
 =\frac{a_n(n-a_n)(a_n-1)^2}{n^2}.
 }
\]
Moreover the maximizer is unique up to isomorphism:
\[
 \boxed{
 G\cong K_{a_n,1,\ldots,1}
 =\overline K_{a_n}\vee K_{n-a_n}.
 }
\]
Thus the unique extremal graph is a complete split graph with one independent
part of size \(a_n\) and \(n-a_n\) singleton parts.

Since \(a_n/n\to 3/4\),
\[
 \max_G\operatorname{Var}(X_G)
 =\left(\frac{27}{256}+o(1)\right)n^2.
\]

### Proof

Write \(M=\max_i n_i\), choose a part of size \(M\), and put \(R=n-M\).
Condition on the first vertex not lying in that chosen part. Let \(Z\) be the
size of the part containing that first vertex under this conditioning, and set
\(\mu=\mathbb E Z\). The law of total variance gives
\[
 \operatorname{Var}(X_G)
 =\frac{R}{n}\operatorname{Var}(Z)
 +\frac{MR}{n^2}(M-\mu)^2. \tag{1}
\]
Because \(1\le Z\le M\),
\[
 (Z-1)(M-Z)\ge0,
\]
and taking expectations yields the elementary bounded-variance estimate
\[
 \operatorname{Var}(Z)\le (M-\mu)(\mu-1). \tag{2}
\]

Suppose first that \(M\ge n/2\). Put \(L=M-1\) and \(t=\mu-1\). Combining
(1) and (2),
\[
\begin{aligned}
 n\operatorname{Var}(Z)+M(M-\mu)^2
 &\le (L-t)(ML+Rt)\\
 &=ML^2-(2M-n)Lt-Rt^2\\
 &\le ML^2.
\end{aligned}
\]
Therefore
\[
 \operatorname{Var}(X_G)
 \le \frac{MR(M-1)^2}{n^2}. \tag{3}
\]
Equality in (3) forces \(t=0\), hence \(Z=1\) almost surely; equivalently,
all parts except the chosen part are singletons. Thus, for every possible
largest part \(M\ge n/2\), the variance is maximized uniquely by the part
multiset
\[
 (M,1,\ldots,1).
\]

It remains to exclude a global maximizer with \(M<n/2\). Since
\(1\le X_G\le M\), the same elementary bounded-variance argument gives
\[
 \operatorname{Var}(X_G)\le \frac{(M-1)^2}{4}<\frac{n^2}{16}. \tag{4}
\]
For \(n\ge 12\), take \(a=\lceil3n/4\rceil\) and
\(b=n-a=\lfloor n/4\rfloor\). Then
\(b\ge n/5\), \(a\ge3n/4\), and \(a-1\ge2n/3\), so the complete split graph
\(K_{a,1^b}\) has
\[
 \operatorname{Var}(X)
 =\frac{ab(a-1)^2}{n^2}
 \ge \frac{n^2}{15}>\frac{n^2}{16}.
\]
For \(3\le n\le11\), every admissible \(M<n/2\) satisfies
\[
 \frac{(M-1)^2}{4}
 \le \frac{(\lfloor(n-1)/2\rfloor-1)^2}{4}
 < \frac{(n-1)(n-2)^2}{n^2},
\]
where the last term is the variance of \(K_{n-1,1}\); the final strict
inequality is a direct check for these nine orders. Hence no global
maximizer has \(M<n/2\).

The problem is now one-dimensional. For a complete split graph
\(K_{a,1^{\,n-a}}\),
\[
 V_n(a)=\frac{g_n(a)}{n^2},
 \qquad
 g_n(a)=a(n-a)(a-1)^2,
 \qquad 1\le a\le n-1.
\]
A direct difference calculation gives
\[
 g_n(a+1)-g_n(a)
 =-a\bigl(4a^2-3na+n\bigr). \tag{5}
\]
For \(n\ge3\), the smaller positive root of
\(4x^2-3nx+n\) is below \(1\), and the larger root is \(\rho_n\).
Thus (5) changes sign exactly as \(a\) passes \(\rho_n\).
The number \(\rho_n\) cannot be an integer for \(n\ge3\): if
\(\rho_n=a\in\mathbb Z\), then
\[
 n=\frac{4a^2}{3a-1}.
\]
Since \(\gcd(a,3a-1)=1\), this would force \(3a-1\mid4\); the only positive
possibility relevant to the equation is \(a=1,n=2\). Therefore \(g_n\) has the
unique integer maximizer
\[
 a_n=\lceil\rho_n\rceil,
\]
which proves the theorem.

## Consequences and checks

For a complete bipartite graph \(K_{a,b}\), \(n=a+b\),
\[
 \operatorname{Var}(X_{K_{a,b}})
 =\frac{ab(a-b)^2}{n^2}.
\]
The 2026 triangle-free bound of Shaikh,
\[
 \operatorname{Var}(X_G)\le |E(G)|\left(\frac{n-2}{n}\right)^2,
\]
therefore reduces on \(K_{a,b}\) to
\[
 |a-b|\le n-2,
\]
with equality exactly when \(\min\{a,b\}=1\), i.e. for stars. This is
consistent with the published equality statement for the triangle-free bound.

Also,
\[
 \operatorname{Var}(X_G)=0
 \quad\Longleftrightarrow\quad
 n_1=\cdots=n_r,
\]
so within complete multipartite graphs the random greedy output has
deterministic size exactly for the equal-part graphs.

A standalone verification script exhaustively simulates every vertex ordering
for every connected complete multipartite type of order \(3\) through \(8\),
and independently enumerates all multipartite integer partitions through order
\(40\) to check the sharp extremal formula and unique extremizer. These finite
checks support, but are not used in place of, the proof.

## Literature context and originality scope

Shaikh's 2026 preprint studies the variance of the same random greedy MIS size
for triangle-free graphs and proves the sharp edge-sensitive inequality above,
with connected stars as equality cases. Earlier work of Krivelevich,
Mészáros, Michaeli, and Shikhelman develops the random greedy MIS process and
exact/asymptotic expectation results for several graph families.

The complete multipartite law above is elementary once the first inspected
vertex is observed, and no novelty is claimed for that observation by itself.
The originality claim concerns the sharp finite-\(n\) variance maximization over
all connected complete multipartite graphs, including the explicit unique
extremal split graph and the \(27/256\) asymptotic constant. Searches for random
greedy/maximal independent sets together with complete multipartite graphs,
complete split graphs, complete bipartite graphs, variance, random sequential
adsorption, and size-biased part sizes did not locate an equivalent or stronger
finite-order extremal theorem.

Originality is therefore asserted only **to the best of our knowledge**.

## Limitations

The extremal theorem is restricted to connected complete multipartite graphs
and \(n\ge3\). It does not claim a variance extremum over all graphs, over all
graphs with a fixed edge count, or over all graphs of a fixed chromatic number.

The full text of arXiv:2609.14826 was not inspected here; its abstract and
bibliographic record were inspected and explicitly state a triangle-free
theorem with the bound and equality cases quoted above. Because complete
multipartite graphs with at least three nonempty parts generally contain
triangles, that theorem does not imply the present multipartite extremal
classification, but an uninspected discussion or special-case calculation in
the full text remains a residual coverage risk. Very recent parallel work and
older work using different terminology for random sequential adsorption are
additional residual originality risks.

## References

1. M. Shaikh, *Variance of random greedy independent sets in triangle-free
   graphs*, arXiv:2609.14826 (2026).
   https://arxiv.org/abs/2609.14826
2. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman,
   *Greedy maximal independent sets via local limits*,
   Random Structures & Algorithms 64 (2024), 986--1015.
   https://doi.org/10.1002/rsa.21200
