# Exact cherry–root-imbalance dependence in uniform Catalan binary trees

## Finding
For every integer \(n\ge2\), choose uniformly one of the \(C_n=\binom{2n}{n}/(n+1)\) rooted, plane, full binary trees with \(n\) internal vertices. Let \(X_n\) be the number of *cherries* (internal vertices with two leaf children), and let \(K_n\in\{0,\ldots,n-1\}\) be the number of internal vertices in the left subtree of the root. Define its root-split product \(B_n=K_n(n-1-K_n)\) and squared root imbalance \(Q_n=(2K_n-(n-1))^2=(n-1)^2-4B_n\). Then
\[
\mathbb E X_n=\frac{n(n+1)}{2(2n-1)},\qquad
\mathbb E B_n=\frac{4^{n-1}}{C_n}-n,
\]
\[
\boxed{\operatorname{Cov}(X_n,B_n)=\frac{n-2}{4(2n-1)}\frac{4^{n-1}}{C_n}},
\qquad
\boxed{\operatorname{Cov}(X_n,Q_n)=-\frac{n-2}{2n-1}\frac{4^{n-1}}{C_n}}.
\]
The squared-imbalance covariance is exactly zero at \(n=2\) and strictly negative for every \(n\ge3\), with
\[
\operatorname{Cov}(X_n,Q_n)\sim-\frac{\sqrt\pi}{8}n^{3/2}.
\]
Moreover the regression on the entire root split is explicit. For \(0\le i\le n-1\),
\[
\mathbb E[X_n\mid K_n=i]=f(i)+f(n-1-i),\qquad
f(0)=0,\quad f(j)=\frac{j(j+1)}{2(2j-1)}\ \ (j\ge1).
\]
For \(n\ge3\) the correlation is defined and obeys the sharper asymptotic
\[
\boxed{\operatorname{Corr}(X_n,Q_n)\sim-\frac{\pi^{1/4}}{\sqrt2}\,n^{-3/4}}.
\]
Thus root imbalance and cherry abundance have a strictly negative covariance of growing magnitude, yet become asymptotically uncorrelated after normalization.

## Assumptions and scope
Trees are **plane/ordered**, **rooted**, **full binary**, and **uniform by unlabeled shape**: the two child positions are distinct. The sample space has exactly \(C_n\) outcomes, *not* the Yule–Harding permutation-BST distribution and not an independently leaf-labeled phylogenetic model. The root is not itself a cherry for \(n\ge2\). The formula for correlation excludes \(n=2\) because \(X_2\) is deterministic. All finite formulas hold for every integer \(n\ge2\), and the asymptotic results hold as \(n\to\infty\).

## Proof
Let \(C_0=1\), let
\[
F(z)=\sum_{j\ge0}C_jz^j=\frac{1-\sqrt{1-4z}}{2z},\qquad t=\sqrt{1-4z},
\]
so that \(F=1+zF^2\) and \(1-2zF=t\). Each root split has the Catalan convolution law
\[
\Pr(K_n=i)=\frac{C_iC_{n-1-i}}{C_n},\qquad 0\le i\le n-1.
\]
Conditional on that split, its left and right subtrees are independent uniform Catalan trees of the prescribed sizes. Put \(X_0=0\) and
\[
A(z)=\sum_{j\ge0}C_j\mathbb E X_j z^j.
\]
The root contributes exactly one cherry if the whole tree has one internal vertex. Consequently the first-moment decomposition reads
\[
A(z)=z+2zF(z)A(z),\qquad A(z)=\frac zt.
\]
Coefficient extraction gives \([z^j]A(z)=\binom{2j-2}{j-1}\) for \(j\ge1\), hence the claimed \(f(j)\), mean, and conditional regression.

For the root product, the ordinary generating function for internal-vertex size is \(zF'(z)\), so
\[
C_n\mathbb E B_n=[z^{n-1}](zF')^2.
\]
Since \(zF'=t^{-1}-F\), a formal-series identity yields
\[
(zF')^2=t^{-2}+\frac{F-t^{-1}}z,
\qquad [z^{n-1}](zF')^2=4^{n-1}-nC_n.
\]
For the mixed moment, the root itself is not a cherry at \(n\ge2\); its cherries lie in the two subtrees. Thus
\[
C_n\mathbb E(X_nB_n)=2[z^{n-1}](zA')(zF').
\]
Direct substitution yields the exact formal identity
\[
2(zA')(zF')=\frac{(1-t)^2(1+t^2)}{4t^4}
=\frac14\bigl(t^{-4}-2t^{-3}+2t^{-2}-2t^{-1}+1\bigr).
\]
For \(n\ge2\), extracting the coefficient with \(s=n-1\) gives
\[
C_n\mathbb E(X_nB_n)=\frac{n+2}{4}4^{n-1}-n\binom{2n-2}{n-1}.
\]
Subtract \(\mathbb E X_n\,\mathbb E B_n\) and simplify using \(\binom{2n-2}{n-1}=nC_n(n+1)/(2(2n-1))\); this gives the asserted positive product covariance. Because \(Q_n=(n-1)^2-4B_n\), its covariance is negative four times that value. The strict signs follow from the positive factors and \(n-2\).

For correlation, a second derivative of the bivariate cherry enumerator
\[
G(z,u)=1+z\bigl(G(z,u)^2-1+u\bigr)
\]
at \(u=1\) gives \(\partial_uG=z/t\) and \(\partial_{uu}G=2z^3/t^3\), and coefficient extraction yields, for \(n\ge2\),
\[
\operatorname{Var}(X_n)=\frac{n(n-2)(n-1)(n+1)}{2(2n-3)(2n-1)^2}\sim\frac n{16}.
\]
Stirling's formula and the Catalan convolution show
\[
\mathbb E(B_n^2)\sim\frac{n^{7/2}}{4\sqrt\pi}\int_0^1\sqrt{x(1-x)}\,dx
=\frac{\sqrt\pi}{32}n^{7/2}.
\]
Here the bulk split probabilities obey \(\Pr(K_n=\lfloor nx\rfloor)\sim n^{-3/2}/[4\sqrt\pi\{x(1-x)\}^{3/2}]\) for fixed \(0<x<1\). Endpoint contributions are negligible by the uniform Catalan bound \(C_j=O(4^j/(j+1)^{3/2})\) and a truncation/dominated-sum argument. Furthermore \((\mathbb E B_n)^2=O(n^3)=o(n^{7/2})\), so \(\operatorname{Var}(B_n)\sim\sqrt\pi n^{7/2}/32\) and \(\operatorname{Var}(Q_n)=16\operatorname{Var}(B_n)\). Combining these with \(C_n\sim4^n/(\sqrt\pi n^{3/2})\) proves the covariance and correlation asymptotics.

## Verification
The standalone script `verification/verify.py` (Python 3 standard library) enumerates all \(16{,}796\) Catalan trees of size \(n=10\) and all smaller sizes \(2\le n\le10\). It checks the cherry mean, root-product mean, joint covariance, cherry variance, and every conditional root-split regression with rational arithmetic. It additionally verifies the exact convolution identities for every integer \(2\le n\le100\). A replay of the actual script passed \(71{,}631\) assertions. These finite checks corroborate, but do not replace, the preceding all-\(n\) analytic proof; the asymptotic constants are proved from Stirling's formula and convolution estimates rather than finite fitting.

## Relationship to prior work
McKenzie and Steel (2000) establish cherry-count laws under two phylogenetic tree models. Fill and Kapur (2003) treat additive functionals and Catalan-tree shape via general recursive methods. Chang and Fuchs (2009) study pattern-count means, variances and limit laws under the same **uniform plane Catalan model**, including two-leaf fringe patterns, but do not state the root product/squared-imbalance cross-moment or its sign and correlation asymptotics in the inspected text. Choi et al. (2015) analyze joint cherry–pitchfork fringe counts for different tree statistics and model conventions. Existing results therefore provide marginal formulas and generating-function machinery; the exact root-split cross-covariance and its decorrelation exponent are the specific additional conclusion here. The mere presence of the recursive decomposition in prior literature is credited, not claimed new.

## Limitations
The law pertains only to uniform plane Catalan trees, not the Yule–Harding or general leaf-labeled PDA laws. It provides a first-order conditional cherry regression, not a complete conditional distribution or a nonzero limiting correlation. The negative covariance need not imply monotonicity of the conditional regression at every split. The originality comparison is literature-based and cannot exclude equivalent coverage in unlocated general mixed-moment papers; independent mathematical review has not been performed.

## References
1. A. McKenzie and M. Steel, *Distributions of cherries for two models of trees*, Mathematical Biosciences **164** (2000), 81–92, DOI 10.1016/S0025-5564(99)00060-7. Journal issue is dated March 2000; OpenAlex lists 2000-03-01.
2. J. A. Fill and N. Kapur, *Limiting Distributions for Additive Functionals on Catalan Trees*, arXiv:math/0306226v1 (first posted 2003-06-13).
3. H. Chang and M. Fuchs, *Limit theorems for patterns in phylogenetic trees*, author version dated 2009-04-13, https://web.math.nccu.edu.tw/mfuchs/parameters_pt_rev.pdf.
4. K. P. Choi et al., *On joint subtree distributions under two evolutionary models*, arXiv:1508.03139v1 (first posted 2015-08-13).
5. C. Holmgren and S. Janson, work on random fringe subtrees, arXiv:1601.03691v1 (first posted 2016-01-14).
