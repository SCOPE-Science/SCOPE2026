# Regular motifs share a universal degree-count covariance threshold in Erdős–Rényi graphs

## Finding

Let
\[
G\sim G(n,p),
\qquad
0<p<1.
\]
For
\[
0\le k\le n-1,
\]
let
\[
N_k
\]
be the number of vertices of degree exactly \(k\).

Fix a simple graph \(H\) with \(h\) vertices, \(e\) edges, and degree sequence
\[
d_1,\ldots,d_h.
\]
Let \(X_H\) denote the number of non-induced copies of \(H\) in \(G\), counted as injective embeddings divided by \(|\operatorname{Aut}(H)|\). Write
\[
b_{N,k}(p)=\binom Nk p^k(1-p)^{N-k},
\]
with the convention that this is zero when \(k\notin\{0,\ldots,N\}\), and write
\[
(x)_d=x(x-1)\cdots(x-d+1),
\qquad
(x)_0=1.
\]

Then the covariance between a degree class and an arbitrary fixed motif has the exact finite formula
\[
\boxed{
\operatorname{Cov}(N_k,X_H)
=
\mathbb E X_H\,b_{n-1,k}(p)
\left[
\sum_{a=1}^h
\frac{(k)_{d_a}}{(n-1)_{d_a}p^{d_a}}
-h
\right].
}
\tag{1}
\]

For a \(d\)-regular motif, \(d\ge1\), this collapses to
\[
\boxed{
\operatorname{Cov}(N_k,X_H)
=
h\,\mathbb E X_H\,b_{n-1,k}(p)
\left[
\frac{(k)_d}{(n-1)_d p^d}-1
\right].
}
\tag{2}
\]

Consequently every \(d\)-regular motif has exactly the same degree-class covariance sign profile, independent of its number of vertices, number of copies, or global shape:
\[
\boxed{
\operatorname{sgn}\operatorname{Cov}(N_k,X_H)
=
\operatorname{sgn}
\left((k)_d-(n-1)_d p^d\right).
}
\tag{3}
\]
Here the positive prefactor in (2) is understood whenever \(X_H\) is nontrivial.

Let \(r_{n,d,p}>d-1\) be the unique real solution of
\[
(r_{n,d,p})_d=(n-1)_d p^d.
\]
For fixed \(d\) and \(p\),
\[
\boxed{
r_{n,d,p}
=
p(n-1)+\frac{(d-1)(1-p)}2+O(n^{-1}).
}
\tag{4}
\]
Thus the sign switch occurs within a constant distance of the mean degree, with a universal first correction depending only on the motif degree.

For triangles, writing \(T=X_{K_3}\), equation (2) becomes
\[
\boxed{
\operatorname{Cov}(N_k,T)
=
3\binom n3p^3 b_{n-1,k}(p)
\left[
\frac{k(k-1)}{(n-1)(n-2)p^2}-1
\right].
}
\tag{5}
\]
The exact continuous sign boundary is
\[
\boxed{
r_{n,2,p}
=
\frac{1+\sqrt{1+4(n-1)(n-2)p^2}}2
=
p(n-1)+\frac{1-p}{2}+O(n^{-1}).
}
\tag{6}
\]

More generally, every cycle has \(d=2\), so all cycle counts have the same normalized covariance sign profile as triangles. Every fixed cubic motif has the same profile determined by \((k)_3\), and similarly for every fixed regular degree.

## Assumptions and scope

The graph is the classical Erdős–Rényi graph with independent edge indicators and fixed finite \(n\).

A copy of \(H\) is non-induced: all edges of \(H\) must be present, while extra edges among the selected host vertices are allowed. This is the convention for which
\[
\mathbb E X_H
=
\frac{(n)_h}{|\operatorname{Aut}(H)|}p^e.
\]

Formula (1) is valid for every fixed simple \(H\), including nonregular motifs. The one-threshold statement is asserted only for regular \(H\) with \(d\ge1\).

The asymptotic expansion (4) keeps \(d\) and \(p\) fixed while \(n\to\infty\). No sparse-edge asymptotic is claimed there.

## Proof

Write
\[
Y_v=\mathbf 1\{\deg(v)=k\},
\qquad
N_k=\sum_{v=1}^nY_v.
\]
Represent every non-induced copy of \(H\) by an injective embedding modulo automorphisms, and write \(I_\alpha\) for the indicator that all \(e\) motif edges of copy \(\alpha\) are open. Then
\[
X_H=\sum_\alpha I_\alpha.
\]

Fix one copy \(\alpha\). If \(v\) does not lie in \(\alpha\), then \(Y_v\) depends only on edges incident to \(v\), whereas \(I_\alpha\) depends only on internal motif edges. These edge sets are disjoint, so
\[
Y_v\ \text{and}\ I_\alpha
\]
are independent.

Now suppose \(v\) occupies motif role \(a\), whose degree inside \(H\) is \(d_a\). Conditional on \(I_\alpha=1\), exactly \(d_a\) edges incident to \(v\) are forced open. Every other edge incident to \(v\) remains an independent Bernoulli\((p)\) edge. Therefore
\[
\Pr(Y_v=1\mid I_\alpha=1)
=
b_{n-1-d_a,k-d_a}(p).
\tag{7}
\]
Unconditionally,
\[
\Pr(Y_v=1)=b_{n-1,k}(p).
\tag{8}
\]

For a fixed copy \(\alpha\), only its \(h\) vertices contribute nonzero covariance with \(I_\alpha\). Hence
\[
\operatorname{Cov}(N_k,I_\alpha)
=
p^e
\left[
\sum_{a=1}^h b_{n-1-d_a,k-d_a}(p)
-hb_{n-1,k}(p)
\right].
\tag{9}
\]
The elementary binomial-ratio identity
\[
\frac{b_{n-1-d,k-d}(p)}{b_{n-1,k}(p)}
=
\frac{(k)_d}{(n-1)_d p^d}
\tag{10}
\]
uses the same zero convention on both sides when \(k<d\). Summing (9) over all potential copies and using
\[
\mathbb E X_H
=(\text{number of potential copies})p^e
\]
proves (1).

If \(H\) is \(d\)-regular, every term in the sum in (1) is identical, giving (2). For real \(x>d-1\), the falling factorial
\[
(x)_d=\prod_{j=0}^{d-1}(x-j)
\]
is strictly increasing from zero to infinity. Hence the root \(r_{n,d,p}\) is unique, and (3) follows.

To locate that root, put
\[
N=n-1,
\qquad
r=pN+c.
\]
For fixed \(d\),
\[
(r)_d
=(pN)^d
\left[
1+\frac{dc}{pN}-\frac{d(d-1)}{2pN}+O(N^{-2})
\right],
\tag{11}
\]
while
\[
p^d(N)_d
=(pN)^d
\left[
1-\frac{d(d-1)}{2N}+O(N^{-2})
\right].
\tag{12}
\]
Equating (11) and (12) yields
\[
c=\frac{(d-1)(1-p)}2+O(N^{-1}),
\]
which proves (4).

For \(H=K_3\), one has \(h=3\), \(d=2\), and
\[
\mathbb E T=\binom n3p^3.
\]
Substitution into (2) proves (5). Solving the quadratic equation
\[
r(r-1)=(n-1)(n-2)p^2
\]
gives (6).

## Verification

The accompanying checker exhaustively enumerates all edge states for complete host graphs on four, five, and six vertices at several rational edge probabilities.

It independently counts edges, triangles, four-cycles, four-cliques, and three-vertex paths as non-induced motifs. The first four are regular motifs of degrees one, two, two, and three; the path is nonregular with degree sequence \((2,1,1)\).

For every tested \(n,p,k,H\), exact rational arithmetic verifies (1). It separately verifies the regular specialization, the predicted sign profile, the triangle formula, and numerical convergence of the real sign boundary to the expansion (4).

The finite replay is supplementary. The all-\(n\) result follows from the edge-set independence and forced-incident-edge calculation in the proof.

## Relationship to prior work

Goldstein studies the number of vertices of a prescribed degree in the Erdős–Rényi graph and develops a Berry–Esseen theorem using size-bias coupling. That work supplies a primary probability reference for the degree-count statistic, but the inspected full text does not introduce triangle or fixed-motif counts as a joint statistic.

Gilmer and Kopparty study the triangle count in \(G(n,p)\) and prove a local central limit theorem for fixed \(p\). Their full public paper treats the triangle count itself and does not formulate covariance with degree-class counts.

Janson's classical functional-limit paper covers broad asymptotic theory for fixed subgraph counts in Erdős–Rényi graphs. Only publisher-level material was available for that paper in the present comparison, so possible implicit overlap through a general random-graph-statistic decomposition remains a residual risk. The present finding is finite and exact, and its regular-motif consequence identifies a sign threshold depending only on motif degree.

The structural content is not a new marginal limit theorem for either statistic. It is the exact cross-statistic identity (1) and, especially, the universality in (2)--(4): all fixed \(d\)-regular motifs share the same degree-class covariance sign boundary.

## Limitations

The edge independence of \(G(n,p)\) is essential. Degree-constrained, inhomogeneous, and dependent-edge random graph models generally do not reduce to the same binomial ratio.

The sign universality is a second-moment statement. It does not imply that the conditional motif-count distribution is monotone in \(N_k\), nor does it determine higher joint cumulants.

For nonregular motifs, formula (1) is exact but its sign can mix contributions from several internal degrees; a single universal threshold need not exist.

A sufficiently general orthogonal-decomposition treatment of random graph statistics could contain (1) as an implicit corollary. No inspected source stated the formula or the regular-motif sign threshold explicitly; this is the main originality risk.

## References

1. L. Goldstein, “A Berry-Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph,” arXiv:1005.4390, first submitted 2010-05-24; *Annals of Applied Probability* 23 (2013), 617–636, DOI 10.1214/12-AAP848.
2. J. Gilmer and S. Kopparty, “A local central limit theorem for triangles in a random graph,” public manuscript dated 2014; *Random Structures & Algorithms* 48 (2016), 732–750, DOI 10.1002/rsa.20604.
3. S. Janson, “A functional limit theorem for random graphs with applications to subgraph count statistics,” *Random Structures & Algorithms* 1 (1990), 15–37, DOI 10.1002/rsa.3240010103.
