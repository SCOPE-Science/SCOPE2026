# Equality cases in the universal spectral booksize bound

## Statement

For a finite simple graph \(G\) on \(n\) vertices, let \(\lambda(G)\) denote the adjacency spectral radius and let
\[
\operatorname{bk}(G)=\max_{uv\in E(G)} |N(u)\cap N(v)|
\]
be its booksize, with \(\operatorname{bk}(G)=0\) when \(E(G)=\varnothing\).

Liu and Ning proved the universal inequality
\[
\operatorname{bk}(G)\ge 2\lambda(G)-n.
\]

**Theorem.** Equality holds if and only if \(G\) is a balanced complete multipartite graph with at least two parts. Equivalently,
\[
\operatorname{bk}(G)=2\lambda(G)-n
\quad\Longleftrightarrow\quad
G\cong K_{t,t,\ldots,t}
\]
for some integers \(t\ge 1\) and \(r\ge 2\), where there are \(r\) parts and \(n=rt\).

Thus the equality graphs are exactly the Turán graphs \(T_{n,r}\) for divisors \(r\mid n\), \(r\ge 2\).

## Proof

Put
\[
b=\operatorname{bk}(G),\qquad \lambda=\lambda(G),
\]
and assume first that \(b=2\lambda-n\). Since an edgeless graph has \(b=0\), \(\lambda=0\), and \(2\lambda-n=-n\), equality forces \(E(G)\ne\varnothing\).

For every edge \(uv\),
\[
d(u)+d(v)
=
|N(u)\cup N(v)|+|N(u)\cap N(v)|
\le n+b
=
2\lambda.
\tag{1}
\]

Let \(C\) be a connected component with spectral radius \(\lambda(C)=\lambda\). The standard degree-product bound gives
\[
\lambda
\le
\max_{uv\in E(C)}\sqrt{d(u)d(v)}
\le
\frac12\max_{uv\in E(C)}(d(u)+d(v))
\le
\lambda.
\tag{2}
\]
Hence equality holds throughout.

For completeness, recall the equality structure in the first inequality of (2). If \(H\) is connected and
\[
M=\max_{xy\in E(H)}\sqrt{d(x)d(y)},
\]
take a positive Perron vector \(x\) and a vertex \(v\) maximizing \(x_v\). Then
\[
\lambda(H)^2x_v
=
\sum_{u\in N(v)}\sum_{w\in N(u)}x_w
\le
x_v\sum_{u\in N(v)}d(u)
\le
M^2x_v.
\]
If \(\lambda(H)=M\), equality propagates along distance-two steps: vertices at even distance have one common degree, vertices at odd distance have another. Hence \(H\) is regular, or it is bipartite semiregular.

Applying this to \(C\), suppose first that \(C\) is semiregular bipartite with the two degrees \(p,q\). Then \(\lambda=\sqrt{pq}\), while (1) gives
\[
p+q\le 2\lambda=2\sqrt{pq}.
\]
The arithmetic-geometric mean inequality gives the reverse inequality, so \(p=q\). Therefore in all cases \(C\) is \(d\)-regular with
\[
d=\lambda.
\]

Consequently every edge \(uv\in E(C)\) has
\[
d(u)+d(v)=2\lambda=n+b.
\]
Comparing with the two separate upper bounds used in (1) forces
\[
|N(u)\cup N(v)|=n,\qquad |N(u)\cap N(v)|=b.
\tag{3}
\]
But \(N(u)\cup N(v)\subseteq V(C)\), so (3) implies \(V(C)=V(G)\). Thus \(G\) is connected and regular, and every edge is a dominating edge in the sense that
\[
N(u)\cup N(v)=V(G).
\tag{4}
\]

Now consider the complement \(\overline G\). Property (4) says that \(\overline G\) has no induced \(P_3\): if \(x-y-z\) were an induced path in \(\overline G\), then \(xz\in E(G)\), while \(y\) would be adjacent in \(G\) to neither \(x\) nor \(z\), contradicting (4). A graph with no induced \(P_3\) is a disjoint union of cliques. Hence \(\overline G\) is a disjoint union of cliques, so \(G\) is complete multipartite.

Finally, a complete multipartite graph with part sizes \(n_1,\ldots,n_r\) has degree \(n-n_i\) at every vertex in part \(i\). Since \(G\) is regular, all part sizes are equal. Thus
\[
G\cong K_{t,t,\ldots,t}.
\]

Conversely, let \(G=K_{t,\ldots,t}\) have \(r\ge2\) equal parts. It is \((r-1)t\)-regular, so
\[
\lambda(G)=(r-1)t.
\]
Every edge joins two different parts and has exactly the vertices in the remaining \(r-2\) parts as common neighbors, hence
\[
\operatorname{bk}(G)=(r-2)t.
\]
Since \(n=rt\),
\[
2\lambda(G)-n=2(r-1)t-rt=(r-2)t=\operatorname{bk}(G),
\]
which proves the converse.

## Consequence for the spectral Turán booksize bound

Liu and Ning also proved that, under their stated size hypothesis,
\[
\lambda(G)\ge \lambda(T_{n,r})
\quad\Longrightarrow\quad
\operatorname{bk}(G)\ge \frac{r-2}{r}n,
\]
and observed that \(T_{n,r}\) attains equality when \(r\mid n\).

The equality graph is in fact unique whenever \(r\mid n\), without needing the size hypothesis for the equality implication:

**Corollary.** Let \(r\ge2\) divide \(n\). If
\[
\lambda(G)\ge\lambda(T_{n,r})
\quad\text{and}\quad
\operatorname{bk}(G)=\frac{r-2}{r}n,
\]
then
\[
G\cong T_{n,r}.
\]

Indeed, when \(r\mid n\),
\[
\lambda(T_{n,r})=\frac{r-1}{r}n.
\]
Therefore
\[
\frac{r-2}{r}n
=
\operatorname{bk}(G)
\ge
2\lambda(G)-n
\ge
2\frac{r-1}{r}n-n
=
\frac{r-2}{r}n.
\]
Equality holds throughout. The theorem makes \(G\) a balanced complete \(q\)-partite graph for some \(q\mid n\), and equality of the spectral radii
\[
\frac{q-1}{q}n=\frac{r-1}{r}n
\]
forces \(q=r\).

## Context and significance

The universal inequality
\[
\operatorname{bk}(G)\ge 2\lambda(G)-n
\]
appears as Theorem 4.1 in Liu--Ning's 2026 preprint *Sharp spectral lower bounds for the booksize of a graph*. Their proof combines
\[
d(u)+d(v)\le n+\operatorname{bk}(G)
\]
with the standard edge degree-product bound for the spectral radius. Their Remark 4.1 records balanced Turán graphs as equality examples for the subsequent spectral Turán theorem, but does not classify equality in Theorem 4.1.

The theorem above shows that there are no other equality graphs: equality in the spectral booksize inequality is rigid and exactly equivalent to balanced complete multipartite structure. In particular, the triangle-free endpoint recovers balanced complete bipartite graphs, while the other equality cases interpolate through all balanced complete multipartite graphs, including complete graphs.

## Limitations

This is an equality classification, not a stability theorem: it does not quantify how close a graph with small positive deficit
\[
\operatorname{bk}(G)-(2\lambda(G)-n)
\]
must be to a balanced complete multipartite graph. Originality is to the best of our knowledge. Exact-formula and synonymous searches for the equality case, balanced complete multipartite extremizers, and spectral booksize rigidity found no prior classification. The full text of Bollobás--Nikiforov's 2005 *Books in graphs* and Berman--Zhang's 2001 paper on the degree-product spectral bound was not inspected in full in this review; their accessible descriptions concern, respectively, edge-density booksize questions and spectral-radius bounds rather than the equality classification above, but they remain residual sources that could contain an unindexed observation.

## References

1. L. Liu and B. Ning, *Sharp spectral lower bounds for the booksize of a graph*, arXiv:2609.20225 (2026). https://arxiv.org/abs/2609.20225
2. A. Berman and X.-D. Zhang, *On the spectral radius of graphs with cut vertices*, Journal of Combinatorial Theory, Series B 83 (2001), 233--240. https://doi.org/10.1006/jctb.2001.2052
3. B. Bollobás and V. Nikiforov, *Books in graphs*, European Journal of Combinatorics 26 (2005), 259--270. https://doi.org/10.1016/j.ejc.2004.01.007
