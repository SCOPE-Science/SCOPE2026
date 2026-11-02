# An ordered single-crossing law for motif–degree covariance in binomial random graphs

## Finding

Let \(G\sim G(n,p)\), \(n\ge3\), \(0<p<1\). For \(0\le k\le n-1\), let \(D_k\) count vertices of degree exactly \(k\). For any fixed nonempty simple graph \(H\) with \(h\in\{2,\ldots,n\}\) vertices, \(e\ge1\) edges, and no isolated vertices, let \(X_H\) count its non-induced, unlabeled copies. Write \(d_v\ge1\) for the degrees in \(H\), \(a_H=|\operatorname{Aut}(H)|\), and \((x)_{\underline d}=x(x-1)\cdots(x-d+1)\), with \((k)_{\underline d}=0\) for integers \(k<d\). Define

\[
P_{n,k}(p)=\binom{n-1}{k}p^k(1-p)^{n-1-k},\qquad
F_{n,H,k}(p)=\sum_{v\in V(H)}\frac{(k)_{\underline{d_v}}}{(n-1)_{\underline{d_v}}p^{d_v}}-h.
\]

Then, **exactly for every listed finite parameter**, the mixed covariance is

\[
\boxed{\operatorname{Cov}(D_k,X_H)=\frac{(n)_{\underline h}}{a_H}\,p^e P_{n,k}(p)F_{n,H,k}(p).}
\]

In particular, after division by the positive factor \(\mathbb E X_H\,P_{n,k}(p)\), this covariance depends on the motif **only through its vertex-degree multiset**, not its adjacency pattern.

Let \(\delta=\min_v d_v\). For \(1\le k\le n-2\), the sign has the following complete classification:

- If \(k<\delta\), the covariance is strictly negative for every \(0<p<1\).
- If \(\delta\le k\le n-2\), there is a **unique** \(p_{n,H,k}\in(0,1)\) such that the covariance is strictly positive for \(p<p_{n,H,k}\), zero at equality, and strictly negative for \(p>p_{n,H,k}\). Moreover, the thresholds are strictly ordered:

\[
0<p_{n,H,\delta}<p_{n,H,\delta+1}<\cdots<p_{n,H,n-2}<1.
\]

The boundary classes satisfy \(\operatorname{Cov}(D_0,X_H)<0\) and \(\operatorname{Cov}(D_{n-1},X_H)>0\) throughout \(0<p<1\).

For fixed \(H\) and fixed \(k\ge\delta\), let \(c_{H,k}\) be the unique positive solution of

\[
\sum_{v\in V(H)}(k)_{\underline{d_v}}c_{H,k}^{-d_v}=h.
\]

Define \(w_v=(k)_{\underline{d_v}}c_{H,k}^{-d_v}\). The critical probability has the **second-order sparse expansion**

\[
\boxed{p_{n,H,k}=\frac{c_{H,k}}{n}+\frac{c_{H,k}}{2n^2}\,
\frac{\sum_v d_v(d_v+1)w_v}{\sum_v d_v w_v}+O_{H,k}(n^{-3}).}
\]

At fixed \(c>0\) with \(p=c/n\), the covariance itself has the limit

\[
\boxed{\lim_{n\to\infty}n^{e-h}\operatorname{Cov}(D_k,X_H)
=\frac{c^{e+k}e^{-c}}{a_H k!}
\left[\sum_v\frac{(k)_{\underline{d_v}}}{c^{d_v}}-h\right].}
\]

For a \(d\)-regular motif, the exact threshold simplifies to

\[
p_{n,H,k}=\left(\frac{(k)_{\underline d}}{(n-1)_{\underline d}}\right)^{1/d}\quad(k\ge d),
\]

so, for triangles, the threshold at degree \(k\ge2\) is \(\sqrt{k(k-1)/((n-1)(n-2))}\). These claims concern **non-induced** motif counts; requiring absent edges for an induced copy changes the conditional degree law.

## Assumptions and scope

All graphs are finite, simple, and loopless. An unlabeled non-induced copy of \(H\) in \(G\) is an injective edge-preserving map from \(V(H)\) to \(V(G)\), counted modulo \(\operatorname{Aut}(H)\). Edges of \(G\) not prescribed by the copy are unrestricted. Thus the number of potential copies is \((n)_{\underline h}/a_H\) and \(\mathbb E X_H=(n)_{\underline h}p^e/a_H\). The sparse statements keep \(H\) and \(k\) fixed while \(n\) increases; they make no claim when the motif order or degree index grows with \(n\). The exact finite-size sign law holds for all \(n\ge h\) with \(n\ge3\). The boundary \(p\in\{0,1\}\) is excluded.

## Proof

Fix one potential copy \(C\) of \(H\), and write \(J_C\) for the indicator that all its prescribed edges appear. Then \(\mathbb P(J_C=1)=p^e\). Conditional on \(J_C=1\), a vertex \(v\) of the copy has degree \(d_v+Z_v\) where \(Z_v\sim\operatorname{Binomial}(n-1-d_v,p)\). A vertex outside the copy retains its unconditional \(\operatorname{Binomial}(n-1,p)\) degree law, since none of its incident edges belongs to the prescribed copy. Hence

\[
\mathbb P(\deg_G(v)=k\mid J_C=1)=\binom{n-1-d_v}{k-d_v}p^{k-d_v}(1-p)^{n-1-k}
=P_{n,k}(p)\frac{(k)_{\underline{d_v}}}{(n-1)_{\underline{d_v}}p^{d_v}},
\]

where the binomial coefficient is interpreted as zero if its lower argument is out of range. Summing over all \(n\) vertices, subtracting \(\mathbb E D_k=nP_{n,k}(p)\), and multiplying by \(\mathbb P(J_C=1)=p^e\) yields

\[
\operatorname{Cov}(D_k,J_C)=p^eP_{n,k}(p)F_{n,H,k}(p).
\]

There are exactly \((n)_{\underline h}/a_H\) distinct potential copies, and covariance is linear, proving the boxed identity.

The prefactor is strictly positive on the stipulated open parameter domain. If \(k<\delta\), all summands of \(F_{n,H,k}\) vanish, giving \(-h\). Otherwise at least one summand is positive and each nonzero summand is strictly decreasing as a function of \(p\). Therefore \(F_{n,H,k}\) is continuous, strictly decreasing, and diverges to \(+\infty\) as \(p\downarrow0\). For \(k\le n-2\), each ratio \((k)_{\underline d}/(n-1)_{\underline d}\) is strictly below one (including zero terms), so \(F_{n,H,k}(1)<0\). The intermediate value theorem and strict monotonicity prove the unique sign crossing. For \(k=n-1\), each ratio equals \(p^{-d_v}>1\), proving the positive boundary class. For \(k=0\), all ratios vanish, proving the negative boundary class.

For fixed \(p\in(0,1)\), the falling factorial \((k)_{\underline d}\) is nondecreasing in integer \(k\), and increases strictly once \(k\ge d-1\). Hence \(F_{n,H,k+1}(p)>F_{n,H,k}(p)\) for every \(k\ge\delta\). Evaluating at successive zeros, and using strict decrease in \(p\), proves the strict ordering of the critical probabilities.

For the sparse assertions, with fixed \(d\),

\[
(n-1)_{\underline d}=n^d\left(1-\frac{d(d+1)}{2n}+O_d(n^{-2})\right).
\]

Setting \(p=c/n\) gives \(F_{n,H,k}(c/n)=A(c)-h+B(c)/n+O_{H,k,c}(n^{-2})\), locally uniformly for \(c>0\), where

\[
A(c)=\sum_v (k)_{\underline{d_v}}c^{-d_v},\qquad
B(c)=\frac12\sum_v d_v(d_v+1)(k)_{\underline{d_v}}c^{-d_v}.
\]

When \(k\ge\delta\), \(A\) decreases continuously from \(+\infty\) to zero and has a unique \(c_{H,k}>0\) satisfying \(A(c_{H,k})=h\). At this root,

\[
A'(c_{H,k})=-c_{H,k}^{-1}\sum_v d_vw_v<0.
\]

Uniformity of the expansion near this simple root and the implicit-function expansion give \(np_{n,H,k}=c_{H,k}-B(c_{H,k})/(nA'(c_{H,k}))+O_{H,k}(n^{-2})\), exactly the second-order formula stated. Finally, \((n)_{\underline h}/n^h\to1\) and \(P_{n,k}(c/n)\to e^{-c}c^k/k!\); inserting these limits in the exact finite identity proves the covariance scaling. For a regular motif, every summand of \(F\) is identical, and its zero can be solved explicitly.

## Verification

The standalone standard-library program `verify_degree_motif.py` independently enumerates all labeled simple graphs on \(n\in\{3,4,5,6\}\) vertices, computes actual motif copy counts from injective vertex assignments, and compares exact-rational covariances with the formula for every degree class and three rational edge probabilities. It separately checks strict ordering of the sign thresholds for eight concrete motifs and all eligible orders below thirty. The executed script reported **3,299 checks passed**. These are finite computational cross-checks, not a substitute for the parameter-uniform proof above. The asymptotic coefficient and second-order expansion were also compared numerically against exact roots for triangle, three-vertex path, and four-vertex star motifs; they are proved symbolically above.

## Relationship to prior work

Goldstein and Rinott's 1996 work (open preprint version in 2005) supplies exact covariances between **different degree-frequency counts**, and multivariate normal approximation, but not covariances of degree frequencies with arbitrary subgraph motifs. Goldstein's 2010 preprint refines univariate degree-count normal approximation. Döring and Eichelsbacher (2009) analyze moderate deviations of non-induced subgraph counts. Their statements do not imply an all-motif, all-degree finite-sample covariance sign diagram without additional conditional calculations; none gives the displayed degree-multiset factorization or ordered roots in the material inspected. The classical \(k=0\) case is elementary and is not the point of the result. Generalized subgraph-count results of Janson and Nowicki (1991), and overlap formulas of Ellis and Ferry (2010), are relevant broader context but were not fully checked, so historical priority remains uncertain.

## Limitations

This is a self-review, not independent verification or publication-priority certification. The proof treats independent-edge \(G(n,p)\), not fixed-edge \(G(n,m)\), induced motif counts, or inhomogeneous edges. The exact sign phase uses fixed graph \(H\) on at most \(n\) vertices. The sparse expansion holds for \(H,k\) fixed; it does not assert uniformity when those parameters vary. The general criterion does not yield a radical expression for every nonregular motif, although a unique root is defined rigorously. Broader literature might contain an equivalent conditional covariance theorem.

## References

1. L. Goldstein and Y. Rinott, *Multivariate normal approximations by Stein's method and size bias couplings*, Journal of Applied Probability 33 (1996), 1–17, arXiv:math/0510586, publicly available preprint October 27, 2005, https://arxiv.org/abs/math/0510586.
2. H. Döring and P. Eichelsbacher, *Moderate deviations in random graphs and Bernoulli random matrices*, Electronic Journal of Probability 14 (2009), arXiv:0901.3246, first posted January 21, 2009, https://arxiv.org/html/0901.3246v1.
3. L. Goldstein, *A Berry–Esseen bound with applications to vertex degree counts in the Erdős–Rényi random graph*, arXiv:1005.4390, first posted May 24, 2010, https://arxiv.org/abs/1005.4390.
4. S. Janson and K. Nowicki, *The asymptotic distributions of generalized U-statistics with applications to random graphs*, Probability Theory and Related Fields 90 (1991), 341–375, https://doi.org/10.1007/BF01193750.
5. R. B. Ellis and J. P. Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs*, Discrete Applied Mathematics 158 (2010), 649–658, https://doi.org/10.1016/j.dam.2009.11.012.
