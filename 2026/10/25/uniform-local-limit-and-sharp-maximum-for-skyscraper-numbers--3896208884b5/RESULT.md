# Uniform local limit and sharp maximum for skyscraper numbers

## Finding

For positive integers \(n\ge2\), let \(f_n(a,b)\) count the permutations of \(\{1,\ldots,n\}\) having \(a\) left-to-right maxima and \(b\) right-to-left maxima. Write \(H_n=\sum_{j=1}^n1/j\), \(\ell_n=\log n\), and \(A_n=\max_{a,b}f_n(a,b)\). We establish the *uniform additive bivariate lattice local limit*

\[
\sup_{a,b\in\mathbb Z}\left|\ell_n\frac{f_n(a,b)}{n!}
-\frac1{2\pi}\exp\left(-\frac{(a-H_n)^2+(b-H_n)^2}{2\ell_n}\right)\right|\longrightarrow0.
\]

The immediate sharp modal consequence is

\[
A_n\sim\frac{n!}{2\pi\log n}.
\]

Every maximizing pair \((a_n,b_n)\) further obeys
\[
a_n=\log n+o(\sqrt{\log n}),\qquad b_n=\log n+o(\sqrt{\log n}).
\]

These claims concern the number of valid *permutation rows* with specified visibility counts, not the number of completed Latin-square skyscraper puzzles.

## Assumptions and scope

All permutations have distinct heights and are uniformly weighted. The maxima on the left and right refer to scanning the same permutation from opposite ends; they are not upper and lower records both scanned from the left. Invalid pairs have \(f_n(a,b)=0\), so the supremum is literally over all integers. Natural logarithms are used. The limit is uniform as an *additive error after multiplication by \(\log n\)*, not a relative approximation in far Gaussian tails.

## Proof

**Exact probability generating function.** Let \((X_n,Y_n)\) denote the left and right visibility counts of a uniformly selected permutation. Splitting at the global maximum, or using the unsigned first-kind Stirling identity in Khovanova–Lewis, gives
\[
f_n(a,b)=\left[{n-1\atop a+b-2}\right]\binom{a+b-2}{a-1},
\]
where the square bracket is the unsigned Stirling number of the first kind, and vanishes outside its natural range. Hence
\[
F_n(z,w):=\mathbb E[z^{X_n-1}w^{Y_n-1}]
=\prod_{j=0}^{n-2}\frac{j+z+w}{j+2}.
\tag{1}
\]
The normalization at \((z,w)=(1,1)\) is exactly one. In particular, there are independent bivariate increments \((U_j,V_j)\), for \(0\le j\le n-2\), with
\[
\Pr((U_j,V_j)=(1,0))=\Pr((U_j,V_j)=(0,1))=\frac1{j+2},\qquad
\Pr((U_j,V_j)=(0,0))=\frac{j}{j+2},
\]
such that \((X_n-1,Y_n-1)\) has their sum's distribution. Thus both means equal \(H_n\), both variances equal \(H_n-H_n^{(2)}\), and their covariance is \(1-H_n^{(2)}\), with \(H_n^{(2)}=\sum_{j=1}^n j^{-2}\). In particular the variances are \(\log n+O(1)\), while the covariance is bounded.

**Convergence on the Fourier scale.** Let \(\phi_n(\theta,\varphi)=F_n(e^{i\theta},e^{i\varphi})\), and \(\mu_n=H_n-1\). For every fixed real \((u,v)\), expansion of the log-characteristic functions of the bounded independent increments at \((\theta,\varphi)=(u/\sqrt{\ell_n},v/\sqrt{\ell_n})\) gives
\[
e^{-i\mu_n(u+v)/\sqrt{\ell_n}}
\phi_n(u/\sqrt{\ell_n},v/\sqrt{\ell_n})
\longrightarrow e^{-(u^2+v^2)/2}.
\tag{2}
\]
Indeed, summing the second cumulants yields the displayed variance/covariance matrix divided by \(\ell_n\), which tends to the identity. The sum of the absolute cubic remainders is \(O(\ell_n)\), because the chance of a nonzero increment is \(2/(j+2)\); evaluated at fixed scaled frequencies the total remainder is \(O(\ell_n^{-1/2})\). This justifies the expansion, including the deterministic first increment.

**Uniform Fourier domination.** The identity
\[
|j+e^{i\theta}+e^{i\varphi}|^2
=(j+2)^2-2j(2-\cos\theta-\cos\varphi)-2(1-\cos(\theta-\varphi))
\]
implies, for \(j\ge1\),
\[
\left|\frac{j+e^{i\theta}+e^{i\varphi}}{j+2}\right|
\le \exp\left[-\frac{j}{(j+2)^2}
\big((1-\cos\theta)+(1-\cos\varphi)\big)\right].
\]
The factor at \(j=0\) has modulus at most one. Define
\(s_n=\sum_{j=1}^{n-2}j/(j+2)^2=\log n+O(1)\). Since \(1-\cos t\ge2t^2/\pi^2\) for \(|t|\le\pi\), one obtains
\[
|\phi_n(\theta,\varphi)|
\le\exp[-2s_n(\theta^2+\varphi^2)/\pi^2],
\qquad (\theta,\varphi)\in[-\pi,\pi]^2.
\tag{3}
\]
Consequently, after putting \((u,v)=\sqrt{\ell_n}(\theta,\varphi)\), the modulus of the rescaled Fourier integrand is bounded by \(e^{-c(u^2+v^2)}\) for an absolute \(c>0\) and all sufficiently large \(n\). This bound is integrable on the plane.

**Local limit, including the supremum.** Fourier inversion, multiplied by \(\ell_n\) and rescaled, writes \(\ell_n f_n(a,b)/n!\) as
\[
\frac1{(2\pi)^2}\int_{[-\pi\sqrt{\ell_n},\pi\sqrt{\ell_n}]^2}
 e^{-i(u(a-H_n)+v(b-H_n))/\sqrt{\ell_n}}
 e^{-i\mu_n(u+v)/\sqrt{\ell_n}}\phi_n(u/\sqrt{\ell_n},v/\sqrt{\ell_n})\,du\,dv.
\]
By (2), (3), and dominated convergence, the centered Fourier kernel converges to \(e^{-(u^2+v^2)/2}\) in \(L^1(\mathbb R^2)\), where the finite-domain kernels are extended by zero. The absolute difference of the Fourier transforms is bounded *uniformly in the phase* by the \(L^1\) distance of their kernels. Fourier transforming the standard Gaussian yields the asserted sup-norm local limit.

A pair of integers nearest \((H_n,H_n)\) has scaled probability \((2\pi)^{-1}+o(1)\). Every Gaussian comparison is at most \((2\pi)^{-1}\), so \(\ell_n A_n/n!\to(2\pi)^{-1}\). Finally, if a maximizing pair remained at scaled Euclidean distance at least \(\varepsilon>0\) along a subsequence, its scaled probability would be at most \((2\pi)^{-1}e^{-\varepsilon^2/2}+o(1)\), contradicting the nearest-integer lower bound. This proves both the sharp maximum and localization of every maximizer.

## Verification

The bundled `verify.py` computes the independent bivariate counts by exhaustive permutation enumeration for lengths \(2\) through \(8\), exactly reconstructs the first \(24\) values of OEIS A218531 from unsigned Stirling numbers, and prints finite-size normalized ratios for lengths \(100\), \(1000\), \(10000\), and \(100000\). Run with `python3 verify.py`. The finite computations are evidence for correct normalization and implementation, not a proof of convergence; the preceding Fourier argument supplies the infinite proof.

## Relationship to prior work

Khovanova and Lewis (2013) define the skyscraper numbers and maximal sequence, prove the Stirling–binomial identity, and show that maximizing pairs are balanced. They give finite values, but their paper does not state a local limit, sharp leading asymptotic, or concentration scale for the maximizing counts. Gnedin (2006), discussing *upper and lower* records both scanned from the same end, gives the **same bivariate Stirling–binomial array and its generating function** and states a joint Gaussian convergence-in-distribution result. That prior Gaussian limit does not by itself control lattice point probabilities or their maxima. The present contribution is the *uniform additive lattice local limit* and its sharp modal consequence, with a direct quantitative Fourier domination proof. OEIS A218531 lists the same sequence and an exact finite formula, not this asymptotic.

## Limitations

The approximation is additive uniformly on the \(\log n\)-normalized scale; it is not relative in the extreme tails and does not determine the exact integer maximizing pair for each \(n\). No claim of priority over general-purpose multivariate lattice local-limit theorems is made; such results can imply local limits upon checking the triangular-array hypotheses. The specific sharp asymptotic and maximizing-scale statement were not identified in the inspected sources, but unindexed literature can contain prior equivalent statements. Only self-review has been performed, not independent audit.

## References

1. T. Khovanova and J. B. Lewis, *Skyscraper Numbers*, arXiv:1304.6445v1, first posted 2013-04-23. https://arxiv.org/html/1304.6445v1.
2. A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538v1, first posted 2006-11-17. https://arxiv.org/abs/math/0611538.
3. OEIS Foundation, *A218531: The maximal number of solutions for a given row of a skyscraper puzzle*, https://oeis.org/A218531.
