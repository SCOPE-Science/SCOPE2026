# Sharp complex \(\pi\)-constant for the canonical combinatorial \(C(K)\) representation

## Finding

Let \(\kappa\) be an infinite cardinal and let \(\mathcal F\subset[\kappa]^{<\omega}\) be hereditary and cover \(\kappa\). Let \(X_{\mathcal F}^{\mathbb C}\) be the completion of complex \(c_{00}(\kappa)\) for
\[
\|x\|_{\mathcal F}=\sup_{F\in\mathcal F}\sum_{\alpha\in F}|x(\alpha)|,
\]
and put \(K=\overline{\mathcal F}\subset 2^\kappa\). The canonical complex-linear map
\[
T_{\mathcal F}x(A)=\sum_{\alpha\in A}x(\alpha)\qquad(A\in K)
\]
extends to an injective operator \(T_{\mathcal F}:X_{\mathcal F}^{\mathbb C}\to C(K;\mathbb C)\) with
\[
\|T_{\mathcal F}\|=1,\qquad
\|T_{\mathcal F}x\|_\infty\ge \frac1\pi\|x\|_{\mathcal F}\quad(x\in X_{\mathcal F}^{\mathbb C}).
\]
The constant \(\pi\) is the best possible universal inverse bound: \(\sup_{\mathcal F}\|T_{\mathcal F}^{-1}\|=\pi\), where the inverse is taken on the range. Sharpness already occurs asymptotically for the countable hereditary families
\[
\mathcal F_m=\mathcal P(\{1,\ldots,m\})\cup\{\{n\}:n>m\}
\]
and the vectors \(x^{(m)}_j=e^{2\pi i j/m}\) for \(1\le j\le m\), zero elsewhere: \(\|x^{(m)}\|_{\mathcal F_m}=m\) while
\[
\|T_{\mathcal F_m}x^{(m)}\|_\infty\le \frac1{\sin(\pi/m)},
\]
so \(\|x^{(m)}\|_{\mathcal F_m}/\|T_{\mathcal F_m}x^{(m)}\|_\infty\ge m\sin(\pi/m)\to\pi\).

This is the complex-scalar counterpart of the canonical representation in Proposition 2.2 of Borodulin–Nadzieja, Marsy, and Ryduchowski. Their real argument gives the factor \(2\). In the complex setting the optimal universal factor is \(\pi\).

## Assumptions and scope

Let \(\kappa\) be an infinite cardinal. A family \(\mathcal F\subset[\kappa]^{<\omega}\) is assumed hereditary and to cover \(\kappa\); hence every singleton belongs to \(\mathcal F\). The complex combinatorial space \(X_{\mathcal F}^{\mathbb C}\) is the completion of complex \(c_{00}(\kappa)\) for the usual absolute combinatorial norm. The compact space is \(K=\overline{\mathcal F}\subset2^\kappa\).

The assertion concerns only the canonical unsigned-set-sum representation \(T_{\mathcal F}\). It does not claim that \(\pi\) is the Banach--Mazur distance from \(X_{\mathcal F}^{\mathbb C}\) to an arbitrary subspace of an arbitrary \(C(K)\)-space, nor that every individual family has inverse norm \(\pi\).

## Proof

For \(x\in c_{00}(\kappa;\mathbb C)\) and \(A\in K\),
\[
|T_{\mathcal F}x(A)|
\le \sum_{\alpha\in A}|x(\alpha)|
\le \|x\|_{\mathcal F}.
\]
Thus \(T_{\mathcal F}\) is contractive on the dense subspace \(c_{00}\) and extends to \(X_{\mathcal F}^{\mathbb C}\) with values in \(C(K;\mathbb C)\). Since each singleton lies in \(K\), \(\|T_{\mathcal F}e_\alpha\|_\infty=\|e_\alpha\|_{\mathcal F}=1\), so \(\|T_{\mathcal F}\|=1\).

Fix \(x\in c_{00}(\kappa;\mathbb C)\) and \(F\in\mathcal F\). For \(\theta\in[0,2\pi]\), define
\[
A_\theta=\left\{\alpha\in F:\operatorname{Re}\!\left(e^{-i\theta}x(\alpha)\right)\ge0\right\}.
\]
Heredity gives \(A_\theta\in\mathcal F\). Therefore
\[
\|T_{\mathcal F}x\|_\infty
\ge |T_{\mathcal F}x(A_\theta)|
\ge \sum_{\alpha\in F}
\max\!\left\{\operatorname{Re}\!\left(e^{-i\theta}x(\alpha)\right),0\right\}.
\]
For a complex number \(z\),
\[
\frac1{2\pi}\int_0^{2\pi}
\max\!\left\{\operatorname{Re}\!\left(e^{-i\theta}z\right),0\right\}\,d\theta
=\frac{|z|}\pi.
\]
Averaging in \(\theta\) therefore yields a value of \(\theta\) for which
\[
\|T_{\mathcal F}x\|_\infty
\ge \frac1\pi\sum_{\alpha\in F}|x(\alpha)|.
\]
Taking the supremum over \(F\in\mathcal F\) gives
\[
\|T_{\mathcal F}x\|_\infty\ge \frac1\pi\|x\|_{\mathcal F}.
\]
Density extends this inequality to all \(x\in X_{\mathcal F}^{\mathbb C}\), proving injectivity and \(\|T_{\mathcal F}^{-1}\|\le\pi\) on the range.

For sharpness, for \(m\ge2\) take
\[
\mathcal F_m=\mathcal P(\{1,\ldots,m\})\cup\{\{n\}:n>m\}
\]
on \(\mathbb N\), and let \(z_j=e^{2\pi i j/m}\) for \(1\le j\le m\). Define \(x^{(m)}_j=z_j\) on the first \(m\) coordinates and zero elsewhere. Then \(\|x^{(m)}\|_{\mathcal F_m}=m\).

For any subset \(S\subset\{1,\ldots,m\}\), write \(w=\sum_{j\in S}z_j\). If \(w\ne0\), choose \(\theta\) so that \(e^{-i\theta}w=|w|\). Then
\[
|w|
=\sum_{j\in S}\operatorname{Re}(e^{-i\theta}z_j)
\le\sum_{j=1}^m\max\{\operatorname{Re}(e^{-i\theta}z_j),0\}.
\]
The roots with nonnegative projection onto \(e^{i\theta}\) form one consecutive block \(B_\theta\) around the regular \(m\)-gon, up to possible endpoint roots, and
\[
\sum_{j=1}^m\max\{\operatorname{Re}(e^{-i\theta}z_j),0\}
=\operatorname{Re}\!\left(e^{-i\theta}\sum_{j\in B_\theta}z_j\right)
\le\left|\sum_{j\in B_\theta}z_j\right|.
\]
A block of \(k\) consecutive \(m\)-th roots has modulus
\[
\frac{|\sin(k\pi/m)|}{\sin(\pi/m)}\le\frac1{\sin(\pi/m)}.
\]
Hence every subset sum has modulus at most \(1/\sin(\pi/m)\). The closure of \(\mathcal F_m\) adds no set carrying nonzero coordinates of \(x^{(m)}\), so
\[
\|T_{\mathcal F_m}x^{(m)}\|_\infty\le\frac1{\sin(\pi/m)}.
\]
Consequently
\[
\frac{\|x^{(m)}\|_{\mathcal F_m}}
{\|T_{\mathcal F_m}x^{(m)}\|_\infty}
\ge m\sin(\pi/m)\longrightarrow\pi.
\]
Thus no universal constant smaller than \(\pi\) can replace \(\pi\).

## Verification

The lower estimate uses only heredity, the elementary half-plane average
\[
\frac1{2\pi}\int_0^{2\pi}\max\{r\cos\theta,0\}\,d\theta=\frac r\pi,
\]
and density of \(c_{00}\). The sharpness estimate uses the geometric-series formula for consecutive roots of unity. Boundary cases with roots exactly on the perpendicular diameter do not affect the estimate because including or excluding a zero-projection endpoint leaves the projected sum unchanged.

The proof is infinite-dimensional and symbolic. Finite numerical checks were used only as stress tests and are not evidence for the theorem.

## Relationship to prior work

Borodulin–Nadzieja, Marsy, and Ryduchowski prove the corresponding real canonical embedding and obtain
\[
\frac12\|x\|_{\mathcal F}\le\|T_{\mathcal F}x\|_\infty\le\|x\|_{\mathcal F}
\]
by splitting coefficients into positive and negative parts. The present finding identifies the exact universal replacement for that real factor when the same combinatorial norm is taken over complex scalars.

Earlier work of Brech, Ferenczi, and Tcaciuc treats real and complex combinatorial spaces in isometry questions, and Brech and Piña study Banach--Stone-type rigidity for these spaces. Those works establish that the complex scalar version is a natural object, but the inspected material does not supply the sharp canonical \(C(K)\) representation constant proved here.

## Limitations

The result is specific to the canonical set-sum map. It does not determine optimal distortions for noncanonical embeddings. The sharpness statement is universal and asymptotic; it does not assert that every hereditary family attains inverse norm \(\pi\). Two older papers on isometries of combinatorial spaces were compared from their abstracts and available publisher material rather than by a complete line-by-line full-text inspection, leaving a residual terminology risk, although their stated results concern isometry classification rather than this representation constant.

## References

1. P. Borodulin–Nadzieja, M. Marsy, K. Ryduchowski, *Non-separable combinatorial Banach spaces*, arXiv:2610.01919v1, 2026.
2. C. Brech, V. Ferenczi, A. Tcaciuc, *Isometries of combinatorial Banach spaces*, arXiv:1907.06815, 2019.
3. C. Brech, C. Piña, *Banach-Stone-like results for combinatorial Banach spaces*, arXiv:2007.11071, 2020; Annals of Pure and Applied Logic 172 (2021), 102989.
