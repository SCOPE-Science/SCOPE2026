# One-sided non-Gaussian area fluctuations of randomly rotated Minkowski sums

## Finding
Let \(K\subset\mathbb R^2\) be any compact full-dimensional convex body, of Euclidean perimeter \(P\) and area \(A\). Let \(\Theta_1,\ldots,\Theta_n\) be independent uniform angles modulo \(2\pi\), and set
\[
M_n=R_{\Theta_1}K+\cdots+R_{\Theta_n}K,\qquad n\ge1,
\]
where the plus sign denotes Minkowski sum. Write its support function as
\[
h_K(\phi)=\frac{P}{2\pi}+\sum_{k\ge1}(a_k\cos k\phi+b_k\sin k\phi),
\qquad \lambda_k=\frac\pi2(k^2-1)(a_k^2+b_k^2)\quad(k\ge2).
\]
Then \(\lambda_k\ge0\) and \(D=\sum_{k\ge2}\lambda_k=P^2/(4\pi)-A\) is the isoperimetric deficit. The entire family obeys the exact finite-sample area formulas
\[
\boxed{\mathbb E\operatorname{Area}(M_n)=\frac{n^2P^2}{4\pi}-nD,\qquad
\operatorname{Var}(\operatorname{Area}(M_n))=n(n-1)\sum_{k\ge2}\lambda_k^2.}
\]
For independent unit exponential variables \(E_2,E_3,\ldots\), the centered areas converge in distribution as \(n\to\infty\):
\[
\boxed{\frac{\operatorname{Area}(M_n)-\mathbb E\operatorname{Area}(M_n)}{n}
\ \Longrightarrow\ W_K=\sum_{k\ge2}\lambda_k(1-E_k).}
\]
The series converges absolutely almost surely. For every non-disk, \(W_K\) has strictly negative third cumulant, sharp essential supremum \(D\), and unbounded negative support; in particular it is non-Gaussian. For a disk all fluctuations vanish. The Laplace transform for \(t\ge0\) is
\[
\mathbb E e^{tW_K}=e^{tD}\prod_{k\ge2}(1+t\lambda_k)^{-1}.
\]
Moreover the variance has the sharp universal upper bound \(n(n-1)D^2\), with equality for a non-disk exactly when the support function has a single nonzero Fourier mode of order at least two (apart from constant and translation modes).

**Explicit regular-polygon family.** For the regular \(m\)-gon \(K_m\) of circumradius one, \(m\ge3\), set \(a=\pi/m\), \(P_m=2m\sin a\), \(\mu_m=\sin a/a\), and \(\beta_m=P_m\mu_m\). Then the only nonzero weights are
\[
\boxed{\lambda_{mj}=\frac{\beta_m}{m^2j^2-1}\quad(j\ge1).}
\]
Consequently the exact area variance is
\[
\boxed{\operatorname{Var}(\operatorname{Area}(M_n))
=\frac{n(n-1)P_m^2}{2}
\left[\frac12+\frac{\sin(2a)}{4a}-\frac{\sin^2a}{a^2}\right],}
\]
and \(W_{K_m}=\beta_m\sum_{j\ge1}(1-E_j)/(m^2j^2-1)\). The regular-polygon limiting law has an explicit Euler-product Laplace transform:
\[
\boxed{\mathbb E e^{tW_{K_m}}=e^{tD_m}\frac{\sin a/a}{\mathcal S((t\beta_m-1)/m^2)},\qquad t\ge0,}
\]
where \(D_m=P_m(\mu_m-\cos a)/2\) and \(\mathcal S(z)=\sinh(\pi\sqrt z)/(\pi\sqrt z)\) for \(z>0\), \(\mathcal S(0)=1\), and \(\mathcal S(z)=\sin(\pi\sqrt{-z})/(\pi\sqrt{-z})\) for \(z<0\). The denominator is strictly positive in the stated range.

## Assumptions and scope
The rotations are independent and Haar-uniform. Minkowski addition is taken in the Euclidean plane. Any nonempty-interior compact convex \(K\) is allowed, including polytopes and nonsmooth bodies. Fourier coefficients are those of the ordinary support function at outward normal \((\cos\phi,\sin\phi)\). Translations change only the first Fourier mode and do not affect the statements. The \(E_k\) in the limit are abstract independent exponentials, *not* independent copies of the finite-sample squared Fourier sums. The bound on the variance is sharp among arbitrary convex bodies of fixed deficit, and is realized, subject to convexity, by \(h(\phi)=r+\varepsilon\cos(k\phi)\) with \(k\ge2\) and \(0<|\varepsilon|\le r/(k^2-1)\).

## Proof
**(1) Area and Fourier energies, including nonsmooth bodies.** The support function \(h=h_K\) is Lipschitz on the circle. The planar area formula holds with weak derivative:
\[
\operatorname{Area}(K)=\frac12\int_0^{2\pi}(h(\phi)^2-h'(\phi)^2)\,d\phi.
\]
For smooth positively curved bodies this follows from the normal parameterization of the boundary and Green's theorem. For general bodies, mollify support functions by averaging rotations and pass to the limit in \(W^{1,2}\) (or integrate against the curvature measure). Parseval gives \(A=P^2/(4\pi)-\sum_{k\ge2}\lambda_k\); thus \(\sum_{k\ge2}\lambda_k=D<\infty\).

**(2) Exact finite-sample law and moments.** Minkowski sums add support functions and rotations shift their arguments. Therefore the \(k\)-th harmonic of \(M_n\) is the corresponding harmonic of \(K\) multiplied by \(S_{k,n}=\sum_{j=1}^{n}e^{ik\Theta_j}\) up to a unit complex factor, while the constant coefficient becomes \(nP/(2\pi)\). Applying (1) to \(M_n\) gives the pathwise identity
\[
\operatorname{Area}(M_n)=\frac{n^2P^2}{4\pi}-\sum_{k\ge2}\lambda_k|S_{k,n}|^2.
\tag{1}
\]
All terms in the sum are nonnegative and the sum is bounded by \(n^2D\); interchanges are valid. For each positive integer \(k\), \(\mathbb E|S_{k,n}|^2=n\). Expand the centered square as
\[
|S_{k,n}|^2-n=\sum_{i\ne j}e^{ik(\Theta_i-\Theta_j)}.
\]
Orthogonality of circle characters shows for positive integers \(k,\ell\)
\[
\mathbb E[(|S_{k,n}|^2-n)(|S_{\ell,n}|^2-n)]
=n(n-1)\mathbf1_{k=\ell}.
\tag{2}
\]
Indeed the nonzero expectations in the double sum require exactly the same unordered index pair and opposing orientation, and matching frequencies. Hence (1) and (2) imply both formulas; passage to infinitely many frequencies is justified by \(\sum\lambda_k<\infty\) and \(\sum\lambda_k^2<\infty\).

**(3) Non-Gaussian limit.** For any finite set of *distinct positive* Fourier frequencies, the real and imaginary components of \(e^{ik\Theta_j}\) have mean zero, variance \(1/2\), and pairwise zero cross-covariances. The multivariate central limit theorem therefore yields independent proper standard complex Gaussian limits for \(S_{k,n}/\sqrt n\). Their squared moduli are independent unit exponentials. The tail of the centered, scaled series in (1) obeys the exact bound
\[
\mathbb E\left|\sum_{k>J}\lambda_k\left(\frac{|S_{k,n}|^2}{n}-1\right)\right|^2
=\left(1-\frac1n\right)\sum_{k>J}\lambda_k^2\longrightarrow0
\quad(J\to\infty),
\]
uniformly in \(n\ge1\). A converging-together argument proves the displayed law. Its limiting series converges absolutely almost surely since \(\mathbb E\sum\lambda_k E_k=\sum\lambda_k<\infty\). Independent exponential cumulants and the summability yield the third cumulant \(-2\sum_{k\ge2}\lambda_k^3<0\) for a nondisk. All exponentials are nonnegative, proving \(W_K\le D\); an event where finitely many exponentials are small and the tail is small has positive probability, proving \(\operatorname{ess\,sup}W_K=D\). Any positive weight multiplies an unbounded exponential, so the lower support is unbounded. The Laplace product follows from independence and bounded convergence for positive transforms.

**(4) Sharp variance rigidity.** The nonnegative Fourier energies satisfy \(\sum\lambda_k^2\le(\sum\lambda_k)^2=D^2\), with equality for nonzero \(D\) precisely when at most one energy is positive. Such support functions describe the stated single-mode class, provided the curvature measure is nonnegative. The displayed smooth positive-radius examples attain equality for every allowed frequency.

**(5) Regular-polygon spectrum.** For the unit-circumradius regular \(m\)-gon, the side length is \(2\sin a\) and \(P_m=2m\sin a\). With \(\delta\) chosen modulo \(2a\), the mixed-area formula gives
\[
2V(K_m,R_\delta K_m)=P_m\cos(a-|\delta|),\quad -a\le\delta\le a.
\]
This follows directly by summing the other polygon's support value at each of the \(m\) outward side normals. The constant Fourier coefficient of the even \(2a\)-periodic function \(\cos(a-|\delta|)\) is \(\mu_m=\sin a/a\); its cosine coefficients at frequencies \(mj\) are exactly \(-2\mu_m/(m^2j^2-1)\), obtained by integrating \(\cos(a-t)\cos(mjt)\) over \(0\le t\le a\). Comparing \(\operatorname{Area}(K_m+R_\delta K_m)=2A_m+2V(K_m,R_\delta K_m)\) with (1) for two terms gives \(\lambda_{mj}=P_m\mu_m/(m^2j^2-1)\) and vanishing at every other frequency. Alternatively, the exact variance follows because for independent relative rotations the pairwise mixed-area kernels have mean \(\mu_m\) and are uncorrelated between distinct index pairs, even when they share one index; integration gives the variance \(\frac12+\sin(2a)/(4a)-\mu_m^2\) for one kernel. The deficit is \(D_m=P_m(\mu_m-\cos a)/2\). Applying Euler's sine/sinh infinite products to the Laplace product, with \(\prod_{j\ge1}(1-1/(m^2j^2))=\sin a/a\), proves the claimed closed transform.

## Verification
Run `python verify.py` (standard Python 3 library, no dependencies) to check independent convex-hull reconstruction of sums of randomly rotated triangle, square, and pentagon vertices; the mixed-area kernel; the regular-polygon spectral sum for five polygon orders; and the exact nine-copy moment predictions using 16,000 random trials. The output ends `ALL_ROTATIONAL_MINKOWSKI_CHECKS_PASSED`. Finite checks do not prove the all-body limit; the proof above establishes it.

## Relationship to prior work
Ruan and Chirikjian (2020) derive normal-parameterized Minkowski sums of smooth positively curved bodies; their deterministic framework does not imply the stated iid-rotation area moments or limiting exponential series. Schneider (2022) studies intrinsic-volume expectations and Gaussian limits for random zonotopes generated by independently sampled segments; those random segments are not identical full-dimensional bodies subject to one common rigid rotation per summand. Prior spectral laws for randomly rotated segments therefore belong to a different sampling model. Previously studied repeated random *reflection symmetrizations* also have a different dependent iterative construction, while area variation of a fixed body plus one rotated test body is not an iid \(n\)-fold area limit. Standard support-function Fourier formulas and the multivariate CLT are used, not claimed as discoveries. Novelty beyond the inspected literature remains provisional.

## Limitations
The result concerns iid Haar rotations of a single fixed planar convex body. It does not treat correlated or biased rotations, random scale factors, three-dimensional bodies, finite-sample distribution functions for arbitrary \(K\), or universal convergence rates. The continuous limit is with \(n\to\infty\); simulations corroborate only finite samples. Previously unindexed equivalent stochastic-geometry statements remain a historical-priority risk. Independent audit has not been performed.

## References
1. S. Ruan and G. S. Chirikjian, *Closed-Form Minkowski Sums of Convex Bodies with Smooth Positively Curved Boundaries*, arXiv:2012.15461v1, publicly posted 2020-12-31. https://arxiv.org/abs/2012.15461
2. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774v1, publicly posted 2022-02-14. https://arxiv.org/abs/2202.06774
3. D. Coupier and Yu. Davydov, *Random symmetrizations of convex bodies*, arXiv:1211.1785, 2012. https://arxiv.org/abs/1211.1785
4. R. J. Gardner, D. Hug, W. Weil, *The Orlicz–Brunn–Minkowski theory: A general framework, additions, and inequalities*, arXiv:1301.5267, 2013. https://arxiv.org/abs/1301.5267
