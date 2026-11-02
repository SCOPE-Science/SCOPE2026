# Root-degree ordering of leaf counts in uniform Catalan trees

## Finding
Fix an integer \(m\ge2\). Draw a rooted ordered (plane) tree uniformly from the \(C_m=\frac1{m+1}\binom{2m}{m}\) trees with \(m\) edges. Let \(D\) be its root's number of children and let \(L\) be its total number of leaves (vertices without children). Write \(A_{m,d,k}\) for the number of trees having \(D=d\) and \(L=k\). Then
\[
A_{m,d,k}=\frac{d}{m}\binom{m}{k}\binom{m-d-1}{k-d}
\quad (1\le d<m,\ d\le k\le m-1),
\]
with \(A_{m,m,m}=1\) and all remaining entries zero. Thus, for \(1\le d<m\),
\[
\Pr(L=k\mid D=d)=\frac{\binom{m}{k}\binom{m-d-1}{k-d}}{\binom{2m-d-1}{m-d}},
\quad d\le k\le m-1,
\]
and \(L=m\) almost surely given \(D=m\).

**Stochastic-order theorem.** The array \((A_{m,d,k})_{1\le d,k\le m}\) is totally positive of order two: for \(d<e\) and \(k<\ell\),
\[
A_{m,d,k}A_{m,e,\ell}\ge A_{m,d,\ell}A_{m,e,k}.
\]
Every minor with all four entries positive is strictly positive. Equivalently, the conditional leaf-count distributions are nondecreasing in root degree in monotone-likelihood-ratio order. They are **strictly** increasing in ordinary stochastic order: for any \(d<e\) and any strictly increasing \(h:\{1,\dots,m\}\to\mathbb R\),
\[
\mathbb E[h(L)\mid D=d]<\mathbb E[h(L)\mid D=e].
\]
In particular, \(\operatorname{Cov}(D,h(L))>0\) for every such \(h\). The covariance and correlation for the untransformed statistics are
\[
\operatorname{Cov}(D,L)=\frac{m-1}{m+2}>0,
\qquad
\operatorname{Corr}(D,L)=\sqrt{\frac{2(m+3)(2m-1)}{m(m+1)(2m+1)}}\sim\sqrt{\frac2m}.
\]
The strict positive dependence therefore persists at every finite size while ordinary correlation vanishes as \(m\to\infty\).

## Assumptions and scope
All trees are unlabeled rooted **ordered** trees; the sampling law is uniform over their plane shapes. There are exactly \(m\) edges and \(m+1\) vertices, with \(m\ge2\). A leaf is a vertex with no children, not a vertex of undirected degree one; this distinction matters for the root of a single-vertex tree, which is excluded here. The matrix statement concerns each fixed finite \(m\), and the asymptotic takes \(m\to\infty\). The zero entries and the star-tree boundary \(D=L=m\) are part of the stated theorem.

## Proof
Let \(T(z,u)\) be the ordinary generating series for rooted ordered trees, with \(z\) marking vertices and \(u\) marking leaves. Decomposition at the root gives
\[
T=z\left(u+\frac{T}{1-T}\right).
\]
A tree with root degree \(d\ge1\) is an ordered collection of exactly \(d\) child subtrees, so its \((m,d,k)\) count is \([z^m u^k]T(z,u)^d\). Lagrange inversion, for \(d\le m\), yields
\[
[z^m]T^d=\frac{d}{m}[t^{m-d}]\left(u+\frac{t}{1-t}\right)^m,
\]
whence coefficient extraction in \(u\) gives the displayed formula for \(A_{m,d,k}\), including the exceptional \(d=m\) star. Setting \(u=1\) gives \(\sum_k A_{m,d,k}=\frac dm\binom{2m-d-1}{m-d}\). Dividing proves the conditional distribution.

For consecutive nonstar degrees \(1\le d\le m-2\), at every point of common positive support the ratio is
\[
\frac{A_{m,d+1,k}}{A_{m,d,k}}=\frac{d+1}{d}\frac{k-d}{m-d-1}.
\]
This is strictly increasing with \(k\), and the support of the higher-degree row begins one step later. More generally, if \(d<e<m\), then wherever both rows are positive,
\[
\frac{A_{m,e,k+1}/A_{m,d,k+1}}{A_{m,e,k}/A_{m,d,k}}
=\frac{k-d+1}{k-e+1}>1.
\]
Consequently every positive four-entry minor is strictly positive. A minor involving an absent entry is nonnegative because the interval support \([d,m-1]\) shifts right as \(d\) rises; the final row \(d=m\) is concentrated at \(k=m\). This proves total positivity and monotone-likelihood-ratio order. Strict stochastic order follows since the conditional law for each successive degree shifts to the right and the supports are not identical: the leftmost possible leaf count is exactly \(d\), with positive mass. The displayed strict inequality for increasing \(h\) follows from stochastic dominance; applying the positive-association identity \(2\operatorname{Cov}(D,h(L))=\mathbb E[(D-D')(g(D)-g(D'))]\) with \(g(d)=\mathbb E[h(L)\mid D=d]\) and an independent copy \(D'\) proves strict covariance positivity.

For explicit moments, the conditional law has mean
\[
\mathbb E[L\mid D=d]=\frac{m(m-1)}{2m-d-1},\qquad 1\le d\le m,
\]
by the usual binomial coefficient sum (or differentiating \([z^m]T^d\) in \(u\)). The classical Narayana marginal \(\Pr(L=k)=\binom mk\binom m{k-1}/(mC_m)\) is symmetric under \(k\leftrightarrow m+1-k\). Thus
\[
\mathbb E L=\frac{m+1}{2},\qquad
\operatorname{Var}(L)=\frac{m^2-1}{4(2m-1)}.
\]
At \(u=1\), put \(T=T(z,1)\), so \(z=T(1-T)\). The series marking root degree by its first moment is \(G(z,u)=T(z,u)/(1-T(z,u))^2\). Lagrange extraction gives
\[
\mathbb E D=\frac{3m}{m+2},\quad
\mathbb E[D(D-1)]=\frac{10m(m-1)}{(m+2)(m+3)},\quad
\operatorname{Var}(D)=\frac{2m(m-1)(2m+1)}{(m+2)^2(m+3)}.
\]
Differentiating the defining series gives \(T_u=T(1-T)^2/(1-2T)\) at \(u=1\). Consequently,
\[
G_u(z,1)=\frac{T(1+T)}{(1-T)(1-2T)}
=\frac12+\frac{3}{2(1-2T)}-\frac2{1-T}.
\]
Since \([z^m](1-2T)^{-1}=\binom{2m}{m}\) and \([z^m](1-T)^{-1}=C_m\), the last identity yields
\[
\mathbb E[DL]=\frac{3m-1}{2}.
\]
Subtracting \(\mathbb E D\,\mathbb E L\) proves the covariance. The two variance formulas give the correlation displayed above. Its asymptotic follows by dividing leading powers of \(m\). All formulas also hold at the smallest allowed size \(m=2\).

## Verification
The self-contained `verify.py` enumerates all rooted ordered plane trees with \(m=2,\ldots,9\) edges independently of the coefficient-extraction formula; it checks every \((D,L)\) cell, moment formulas, conditional means, and every adjacent minor. Additional exact rational/binomial comparisons cover \(10\le m\le100\). Executing `python verify.py` passed **15,911 assertions**. Enumeration is finite corroboration; the unrestricted theorem follows from Lagrange inversion and the ratio inequalities proved above.

## Relationship to prior work
Mallows and Wachter (1972) established general valency enumeration of plane trees. Chen, Deutsch and Elizalde (first public preprint October 6, 2004) derived Narayana refinements involving old and young leaves, which supply established leaf-count context. Al Ghabra and coauthors (2023) give general multi-rooted valency enumeration, including root-degree marginals and counts with several marked degree-one vertices. Those broad counting results potentially permit reconstruction of the joint count here using marked leaves; **neither the Narayana marginal nor general degree enumeration is claimed original**. The specific finite-size monotone-likelihood-ratio/TP2 dependence theorem and its strict transformed-covariance conclusion were not found in the inspected primary texts. An implication via nontrivial specializations of general valency formulas remains a priority risk.

## Limitations
The theorem concerns uniform plane trees, not recursive, Cayley, unordered, or height-weighted trees. TP2 is a property of the root-degree and whole-tree leaf-count pair; it does not assert positive association of arbitrary tree statistics. Strictness of two-by-two minors applies only if all four entries are positive, while strictly increasing conditional expectations hold for every distinct root degree. No independent audit or definitive historical priority certification has been performed.

## References
- C. L. Mallows and K. W. Wachter, *Valency enumeration of rooted plane trees*, J. Austral. Math. Soc. 13 (1972), 123–128, https://doi.org/10.1017/S1446788700009228.
- W. Y. C. Chen, E. Deutsch and S. Elizalde, *Old and young leaves on plane trees*, arXiv:math/0410127, first posted 2004-10-06, https://arxiv.org/abs/math/0410127.
- A. Al Ghabra, K. Gopala Krishna, P. Labelle and V. Shramchenko, *Enumeration of multi-rooted plane trees*, arXiv:2301.09765 (2023), https://arxiv.org/abs/2301.09765.
