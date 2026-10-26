# Second-order universality and triangle-sensitive skewness in random orientation scores

## Finding

Let \(H=(V,E)\) be **any finite simple undirected graph**, possibly disconnected. Orient its edges independently, with the two directions equally likely. Write \(d_v\) for its fixed degrees, \(D_v\) for the random outdegrees, and \(t(H)\) for its number of undirected triangles. The centered-score dispersion is
\[
Q_H=\sum_{v\in V}\left(D_v-\frac{d_v}{2}\right)^2.
\]
Its first three central characteristics obey the **exact all-graph identities**
\[
\boxed{\mathbb E Q_H=\frac{|E|}{2},\qquad
\operatorname{Var}(Q_H)=\frac14\sum_{v\in V}\binom{d_v}{2},\qquad
\mathbb E[(Q_H-\mathbb E Q_H)^3]
=\frac34\left(\sum_{v\in V}\binom{d_v}{3}-t(H)\right).}
\]
Consequently the first two moments depend only on the host degree sequence, while the third centered moment determines the host triangle count exactly, once its degrees are known.

**A stronger second-order statement for regular hosts.** Suppose the graph is \(d\)-regular, with \(n=|V|\) and \(d\ge1\). Let \(N_r\) be the number of vertices of outdegree \(r\), and put \(p_r=2^{-d}\binom dr\), for \(0\le r\le d\). The complete covariance matrix of the score histogram is
\[
\boxed{\operatorname{Cov}(N_r,N_s)
=n\left[p_r\mathbf 1_{\{r=s\}}-p_rp_s
\left(1+\frac{(2r-d)(2s-d)}d\right)\right].}
\]
After normalization by \(\sqrt{np_rnp_s}\), this matrix is the orthogonal projection onto the complement of the constant and linear binomial modes; it has exactly \(d-1\) unit eigenvalues and two zero eigenvalues. Thus **even the entire histogram covariance matrix cannot distinguish any two regular hosts with the same number of vertices and common degree**, whereas the third moment of the above natural quadratic statistic can distinguish their triangle counts.

For example, the triangular prism and \(K_{3,3}\) both have six vertices of degree three and nine edges, and their complete score-histogram covariance matrices coincide. Both have \(\mathbb E Q_H=9/2\) and \(\operatorname{Var}(Q_H)=9/2\), but their third centered moments are respectively \(3\) and \(9/2\), since their triangle counts are respectively two and zero.

## Assumptions and scope

All finite simple undirected graphs are allowed, including isolated vertices and disconnected components. Each present edge independently receives one of its two orientations with probability \(1/2\), and absent edges do not participate. Degrees and triangles always refer to the fixed undirected host, not to a random graph. The histogram projection statement assumes regularity and positive common degree; for \(d=1\), the projection has rank zero. No asymptotic limit, large-graph condition, or connectedness hypothesis is required.

## Proof

Give each undirected edge \(e\) an arbitrary reference orientation, and draw independent random signs \(Z_e\), each uniform on \(\{-1,+1\}\). At an incident vertex \(v\), write \(\epsilon_{v,e}=1\) or \(-1\), with opposite values at the endpoints, so that
\[
S_v:=2D_v-d_v=\sum_{e\ni v}\epsilon_{v,e}Z_e.
\]
Since each \(Z_e\) is centered and has square one,
\[
Q_H=\frac14\sum_v S_v^2
=\frac14\sum_v d_v+\frac12\sum_v\sum_{\{e,f\}\subseteq E(v)}\epsilon_{v,e}\epsilon_{v,f}Z_eZ_f.
\]
Thus \(W:=2(Q_H-\mathbb E Q_H)\) is the latter double sum without its factor \(1/2\). The graph is simple, so distinct incident edge pairs correspond to distinct quadratic Rademacher monomials. Orthogonality immediately gives \(\mathbb EW=0\) and
\[
\mathbb EW^2=\sum_v\binom{d_v}{2}.
\]

To evaluate \(\mathbb EW^3\), observe that a product of three quadratic monomials can have nonzero expectation only if every \(Z_e\) appears an even number of times. Repeated monomials cannot achieve this with three factors. Hence the three **distinct** edge pairs must form a triangle of the line graph of \(H\): three host edges meeting pairwise. In a simple host this configuration has exactly two forms. If all three edges meet at one vertex, the sign coefficient product is \(+1\), and there are \(\sum_v\binom{d_v}{3}\) configurations. Otherwise the three host edges form a triangle, and each host edge's two contributions occur at its opposite endpoints, giving sign product \(-1\); there are \(t(H)\) such configurations. Each configuration appears in all six orderings of the three factors, so
\[
\mathbb EW^3=6\left(\sum_v\binom{d_v}{3}-t(H)\right).
\]
Dividing the second moment by four and the third by eight proves the three identities for \(Q_H\).

For the histogram statement, let \(b_j=2^{-(d-1)}\binom{d-1}{j}\), interpreted as zero outside \(0\le j\le d-1\). For distinct nonadjacent vertices the outdegrees are independent. For adjacent vertices \(u,v\), conditioning on their common edge yields
\[
\Pr(D_u=r,D_v=s)=\frac12(b_{r-1}b_s+b_rb_{s-1}),
\quad
\operatorname{Cov}(\mathbf1_{\{D_u=r\}},\mathbf1_{\{D_v=s\}})
=-\frac14(b_{r-1}-b_r)(b_{s-1}-b_s).
\]
The identity \(b_{r-1}-b_r=2(2r-d)p_r/d\) follows from binomial coefficients. There are \(n\) same-vertex terms and \(nd\) ordered adjacent-vertex terms in the covariance of the \(N_r\)'s. Summing them gives the displayed formula.

Finally define two vectors \(u_0=(\sqrt{p_r})_{r=0}^d\) and \(u_1=((2r-d)\sqrt{p_r/d})_{r=0}^d\). The binomial mean and variance show \(\langle u_0,u_1\rangle=0\) and \(\|u_0\|=\|u_1\|=1\). Whitening the histogram covariance by \(\operatorname{diag}(np_r)^{-1/2}\) therefore gives \(I-u_0u_0^\mathsf T-u_1u_1^\mathsf T\), proving the asserted projection spectrum.

## Verification

Run `python3 check.py` with standard Python. It independently enumerates every orientation of every simple graph on up to four vertices, plus complete graph \(K_5\), triangular prism, \(K_{3,3}\), and the Petersen graph. It constructs outdegree statistics directly from orientations and verifies the moment identities and, for regular graphs, **every** histogram covariance entry against exact integer/rational calculations. The delivered checker reports **444 passing exact assertions**. Exhaustive finite enumeration checks instances only; the all-graph theorem relies on the preceding algebraic proof.

## Relationship to prior work

Sanchez and Kolesnik, *The geometry of random tournaments* (first public arXiv version September 19, 2020, arXiv:2009.09322), develop arbitrary-host tournament score sequences and their possible mean vectors using zonotopes. Their complete accessible paper is about feasible scores and expectations, not third central moments of uniform random orientation-score dispersion, nor the regular-host score-histogram covariance projection. Claesson, Dukes, Franklín, and Stefánsson, *Counting tournament score sequences* (arXiv:2209.03925), enumerate distinct attainable score sequences for complete tournaments, rather than the distribution or covariance on an independently randomly oriented fixed host.

General Rademacher-chaos moment expansions are classical; the algebraic expansion by itself is not a new technique. The specific result here is the precise **degree-sequence invariance through second order, its complete regular-host score-histogram covariance projection, and triangle recovery at third order** for the natural orientation-score statistic on arbitrary simple hosts. The observed no-coverage comparison is bounded to inspected sources and searches, not a uniqueness or priority guarantee.

## Limitations

Edges must be independently and fairly oriented; biased or dependent orientations do not satisfy these formulas as stated. The covariance matrix formula concerns \(d\)-regular hosts, but the dispersion moment identities apply to all simple hosts. The first three moments need not determine the entire score-dispersion distribution. The inference of triangle counts assumes the host degree sequence is available. A broader, unlocated theorem on random zonotope points, tournament statistics, or quadratic Rademacher chaos might imply the moment identity; historical priority requires further independent assessment. No independent audit has been performed.

## References

1. M. Sanchez and B. Kolesnik, *The geometry of random tournaments*, arXiv:2009.09322 (first public version 2020-09-19). https://arxiv.org/html/2009.09322v1
2. A. Claesson, M. Dukes, A. F. Franklín, and S. Ö. Stefánsson, *Counting tournament score sequences*, arXiv:2209.03925 (first public version 2022-09-08). https://arxiv.org/html/2209.03925v2
3. C. Lin and G. Reinert, *Joint Vertex Degrees in an Inhomogeneous Random Graph Model*, arXiv:0912.4812 (2009). https://arxiv.org/abs/0912.4812
