# Opposite count–length correlations in circular nearest-neighbor networks

## Finding

Place \(n\ge5\) independent, uniform points on a circle of circumference one, measuring distances by the shorter circular arc. Each point directs an edge to its unique nearest neighbor, an almost-surely well-defined rule. Let \(M_n\) count reciprocal nearest-neighbor pairs, \(W_n\) sum their geodesic lengths once each, \(L_n\) sum the lengths of all directed edges, and \(U_n=L_n-2W_n\) sum lengths of nonreciprocal directed edges.

The precise finite-sample moments are
\[
\mathbb E M_n=\frac n3,\qquad \operatorname{Var}(M_n)=\frac{2n}{45},\qquad
\mathbb E W_n=\frac19,\qquad \operatorname{Var}(W_n)=\frac{44}{1125(n+1)},
\]
\[
\operatorname{Cov}(M_n,W_n)=\frac{16}{675}>0,\quad
\operatorname{Cov}(M_n,L_n)=-\frac1{36}<0,\quad
\operatorname{Cov}(M_n,U_n)=-\frac{203}{2700}<0.
\]
Their normalized relationships remain substantial as the sample grows:
\[
\operatorname{Corr}(M_n,W_n)=\frac{4\sqrt{22}}{33}\sqrt{\frac{n+1}{n}}
\longrightarrow\frac{4\sqrt{22}}{33},
\]
\[
\operatorname{Corr}(M_n,L_n)=-\frac{\sqrt{135}}{36}\sqrt{\frac{n+1}{n}}
\longrightarrow-\frac{\sqrt{135}}{36}.
\]
Thus having more reciprocal pairs is associated with *greater total reciprocal-pair length* but *smaller total directed nearest-neighbor length*. In particular, reciprocal pairs and all directed edges exhibit opposite-sign length dependence on the same structural count.

## Assumptions and scope

Write the cyclic gap lengths as \(G_0,\ldots,G_{n-1}\), with positive sum one, subscripts taken modulo \(n\). The gap vector is \(\operatorname{Dirichlet}(1,\ldots,1)\). Ties have probability zero. Let
\[
J_i=\mathbf 1\{G_i<G_{i-1},\ G_i<G_{i+1}\}.
\]
Then \(M_n=\sum_iJ_i\), \(W_n=\sum_iG_iJ_i\) and \(L_n=\sum_i\min(G_{i-1},G_i)\). A gap corresponding to a reciprocal pair must be shorter than both neighbors, so its shorter-geodesic length is exactly \(G_i\). The theorem is proved for every integer \(n\ge5\); special cyclic-overlap cases of three and four points are excluded from its uniform formulas.

## Proof

**Exponential representation.** Let \(X_0,\ldots,X_{n-1}\) be independent rate-one exponentials and put \(S=\sum_iX_i\). Then \(G_i=X_i/S\), the entire normalized gap vector is independent of \(S\), and \(\mathbb ES=n\), \(\mathbb ES^2=n(n+1)\). Define \(J_i=\mathbf1\{X_i<X_{i-1},X_i<X_{i+1}\}\), \(B_i=J_iX_i\), and \(T=\sum_iB_i\). Thus \(T=SW_n\) with \(S\) independent of \((M_n,W_n)\). Consequently
\[
\operatorname{Cov}(M_n,T)=n\operatorname{Cov}(M_n,W_n),\qquad
\operatorname{Var}(T)=n(n+1)\operatorname{Var}(W_n)+n(\mathbb E W_n)^2.
\]

**Local expectations and covariances.** Exponential races give \(\mathbb EJ_i=1/3\), and conditioning on \(J_i=1\) makes \(X_i\) exponential of rate three. Therefore
\[
\mathbb EB_i=\frac19,\qquad \mathbb EB_i^2=\frac{2}{27},\qquad
\operatorname{Var}(B_i)=\frac5{81}.
\]
Adjacent local-minimum indicators cannot both equal one, hence
\(\operatorname{Cov}(B_i,B_{i+1})=-1/81\).
For two indicators whose indices differ by two, integrating the five independent exponentials, where \(a=X_i\), \(b=X_{i+2}\), yields
\[
\mathbb E[B_iB_{i+2}]
=\int_0^\infty\!\int_0^\infty ab\,e^{-2a-2b-\max(a,b)}\,da\,db
=\frac{22}{1125},
\]
\[
\mathbb E[J_iB_{i+2}]
=\int_0^\infty\!\int_0^\infty b\,e^{-2a-2b-\max(a,b)}\,da\,db
=\frac{11}{225}.
\]
For \(n\ge5\), all distinct terms separated by more than two circular steps depend on disjoint exponentials. The local joint-event calculation also gives \(\mathbb P(J_iJ_{i+2}=1)=2/15\). Therefore
\[
\operatorname{Var}(M_n)
=n\left[\frac29+2\left(-\frac19\right)+2\left(\frac{2}{15}-\frac19\right)\right]=\frac{2n}{45}.
\]
For the unnormalized mutual-pair length,
\[
\operatorname{Var}(T)=n\left[\frac5{81}+2\left(-\frac1{81}\right)+2\left(\frac{22}{1125}-\frac1{81}\right)\right]
=n\left(\frac1{81}+\frac{44}{1125}\right).
\]
Since \(\mathbb ET=n/9\), the exponential normalization identities imply
\(\mathbb EW_n=1/9\) and \(\operatorname{Var}(W_n)=44/[1125(n+1)]\).

To compute the mixed covariance, the contributions from coincident indices are \(\operatorname{Cov}(J_i,B_i)=2/27\); from adjacent indices they are each \(\operatorname{Cov}(J_i,B_{i\pm1})=-1/27\); and from distance two they are each
\[
\operatorname{Cov}(J_i,B_{i\pm2})=\frac{11}{225}-\frac1{27}=\frac8{675}.
\]
Every other contribution is zero, so
\[
\operatorname{Cov}(M_n,T)
=n\left[\frac2{27}-\frac2{27}+\frac{16}{675}\right]
=\frac{16n}{675},
\]
which proves the positive reciprocal-length covariance after division by \(n\).

**Directed-length comparison, verified independently.** Put \(Q=\sum_i\min(X_{i-1},X_i)\); then \(Q=SL_n\). Each term has mean \(1/2\) and variance \(1/4\); overlapping adjacent terms have covariance \(1/12\). Thus \(\mathbb EL_n=1/2\), \(\operatorname{Var}(Q)=5n/12\), and \(\operatorname{Var}(L_n)=1/[6(n+1)]\).
For any fixed \(J_i\), covariance with each of the two minima using \(X_i\) is \(-1/18\); covariance with either adjacent *outer* minimum is \(1/24\); all other terms are independent. The outer value follows because conditional on \(J_i=1\), \(X_{i-1}=X_i+E\) for an independent unit exponential \(E\), so the mean of \(\min(X_{i-2},X_{i-1})\) is \(1-(3/4)(1/2)=5/8\). Consequently,
\[
\operatorname{Cov}(M_n,L_n)
=\frac1n\operatorname{Cov}(M_n,Q)
=2\left(-\frac1{18}\right)+2\left(\frac1{24}\right)
=-\frac1{36}.
\]
The decomposition \(L_n=2W_n+U_n\) now proves
\(\operatorname{Cov}(M_n,U_n)=-1/36-32/675=-203/2700\).
Inserting the established variances gives both correlation formulas.

## Verification

The standalone `verify.py` independently evaluates exact rational first and second moments by enumerating every ordering of independent exponential gaps for sizes \(3\) through \(8\) (\(46{,}230\) rank configurations in total). It uses independent exponential order-statistic spacings to compute conditional product moments; no floating-point simulation enters the equalities. All displayed equalities for \(n=5,6,7,8\) are reproduced, including the comparison covariance for directed length. Execute `python3 verify.py` from the extracted package. The infinite-size assertions follow from the proof, not from enumeration.

## Relationship to prior work

Wade's nearest-neighbor graph length theorems [1] establish macroscopic limiting edge weights for directed and undirected nearest-neighbor graphs, including the effect of counting reciprocal edges once. Bahadır and Ceyhan [2], following Enns, Ehlers, and Misi [3], determine the unweighted reciprocal-pair count distribution and its variance on a real interval. Those cited results do not present the finite-sample circular reciprocal-length variance or its covariance with reciprocal-pair count. The directed-length covariance is a contextual comparison: it can also be recovered by integrating an existing radius-isolation covariance formula and is **not** claimed separately as new. The new contribution is the weighted reciprocal-pair second moment and its opposite-sign dependence relative to directed and nonreciprocal lengths.

## Limitations

The theorem uses a *geodesic circle* and iid uniform points with \(n\ge5\); boundary effects on an ordinary interval are different. No claim is made for nonuniform points, higher dimensions, or other edge-weight exponents. This is an analytic finite-dimensional calculation, not an asymptotic independence theorem. Previously published general stochastic-geometry results may imply the constants through an additional specialization, and older component-enumeration literature was not fully accessible; novelty therefore remains subject to independent literature assessment.

## References

[1] A. R. Wade, *Explicit laws of large numbers for random nearest-neighbour type graphs*, initial arXiv public version 23 March 2006, arXiv:math/0603559; *Advances in Applied Probability* **39** (2007), 326–342. https://arxiv.org/abs/math/0603559

[2] S. Bahadır and E. Ceyhan, *On the Number of Reflexive and Shared Nearest Neighbor Pairs in One-Dimensional Uniform Data*, initial arXiv public version 6 May 2016, arXiv:1605.01940; *Probability and Mathematical Statistics* **38** (2018), 123–137. https://arxiv.org/abs/1605.01940

[3] E. G. Enns, P. F. Ehlers and T. Misi, *A cluster problem as defined by nearest neighbours*, *Canadian Journal of Statistics* **27** (1999), 843–851. https://doi.org/10.2307/3316135
