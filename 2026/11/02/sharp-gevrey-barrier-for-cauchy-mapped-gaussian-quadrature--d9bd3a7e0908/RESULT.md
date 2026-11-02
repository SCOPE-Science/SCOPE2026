# Sharp Gevrey barrier for Cauchy-mapped Gaussian quadrature

## Finding

For each \(0<a<1/2\), let \(Z\sim N(0,1)\), \(\gamma=1/2-a>0\), and \(I_a=\mathbb E[e^{aZ^2}]=(2\gamma)^{-1/2}\). Map a Cauchy quantile \(x(u)=-\cot(\pi u)\), \(0<u<1\), to the period-one importance integrand
\[
g_a(u)=\sqrt{\frac\pi2}\,\csc^2(\pi u)\exp[-\gamma\cot^2(\pi u)],\qquad g_a(0)=g_a(1)=0.
\]
For an integer \(n\ge1\) and independent uniform shift \(U\in[0,1]\), define the one-shift \(n\)-point trapezoidal estimator
\[
Q_n(U)=\frac1n\sum_{j=0}^{n-1}g_a\left(\frac{j+U}{n}\right).
\]
Then \(Q_n\) is unbiased for \(I_a\), and with \(\widehat g_a(k)=\int_0^1g_a(u)e^{-2\pi iku}\,du\),
\[
\mathbb E[(Q_n-I_a)^2]=\sum_{\ell\in\mathbb Z\setminus\{0\}}|\widehat g_a(\ell n)|^2.
\]
The periodic function \(g_a\) is Gevrey of **exact order \(3/2\)**: its derivatives satisfy \(\|g_a^{(r)}\|_\infty\le A B^r(r!)^{3/2}\) for all integers \(r\ge0\), for suitable constants depending on \(a\), but no such inequality with \(3/2\) replaced by any smaller positive order. Consequently there exist \(c_a,C_a>0\) such that, **for every integer \(n\ge1\)**,
\[
\left(\mathbb E[(Q_n-I_a)^2]\right)^{1/2}\le C_a\exp(-c_a n^{2/3}).
\]
The power \(2/3\) is the sharp **uniform-in-\(n\) stretched-exponential envelope exponent**: for every \(\beta>2/3\) and all positive \(c,C\), the inequality \(\left(\mathbb E[(Q_n-I_a)^2]\right)^{1/2}\le C e^{-cn^\beta}\) fails for infinitely many positive integers \(n\).

## Assumptions and scope

The target expectation is the Gaussian exponential moment in one dimension, with \(0<a<1/2\); \(U\) is one continuously uniform random shift shared by all \(n\) points. The Cauchy proposal is standard, \(q(x)=1/[\pi(1+x^2)]\), and arithmetic and function evaluations are exact. The sharpness assertion concerns an upper envelope **uniform across all positive integer sample sizes** for this specific transformed integrand and fixed sampling rule; it does not assert a matching lower bound at every \(n\), optimality among all quadrature methods, or a uniform bound as \(a\uparrow1/2\).

## Proof

**1. Exact transform and periodic regularity.** The Cauchy quantile \(x(u)=-\cot(\pi u)\) has derivative \(x'(u)=\pi\csc^2(\pi u)\). The original target integrand is \((2\pi)^{-1/2}e^{-\gamma x^2}\), hence its transformed density is precisely \(g_a\). A change of variables gives \(\int_0^1g_a=(2\gamma)^{-1/2}\). At either endpoint, as \(u\downarrow0\) (with distance to the endpoint in place of \(u\) at the right),
\[
g_a(u)=\frac{\sqrt{\pi/2}\,e^{2\gamma/3}}{\pi^2u^2}\exp\left(-\frac\gamma{\pi^2u^2}\right)(1+O(u^2)).
\]
The function and all of its derivatives tend to zero at each endpoint; extension by zero at the identified endpoints is smooth and periodic.

**2. Exact Gevrey upper order.** For real \(0<u<\delta\), consider the complex disk \(|z-u|\le\kappa u\), with fixed sufficiently small \(\kappa\in(0,1/8]\). By the elementary Laurent expansion of \(\cot(\pi z)\) and the fact that these disks lie in a cone of angular width less than \(\pi/4\), constants \(b,C>0\) can be chosen so that
\[
|\csc^2(\pi z)|\le C u^{-2},\qquad \operatorname{Re}(\cot^2(\pi z))\ge b u^{-2}.
\]
Cauchy's derivative estimate yields
\[
|g_a^{(r)}(u)|\le C r! (\kappa u)^{-r}u^{-2}e^{-b\gamma/u^2}.
\]
Maximizing the factor \(u^{-r-2}e^{-b\gamma/u^2}\) over positive \(u\) gives \(((r+2)/(2b\gamma e))^{(r+2)/2}\), bounded after multiplication by \(r!\) by \(A B^r(r!)^{3/2}\). The right endpoint is symmetric; on the remaining compact interior strip the function is analytic. Therefore the asserted global \(G^{3/2}\) derivative bound holds.

**3. No smaller Gevrey order.** Suppose instead \(\|g_a^{(r)}\|_\infty\le A B^r(r!)^s\) for some \(1<s<3/2\). Because all derivatives at zero vanish, Taylor's integral remainder of order \(r\) implies \(|g_a(u)|\le A(Bu)^r(r!)^{s-1}\). Optimize over \(r\) using the factorial bounds to obtain \(|g_a(u)|\le A'\exp[-b' u^{-1/(s-1)}]\) for all sufficiently small \(u>0\). Since \(1/(s-1)>2\), this contradicts the positive endpoint asymptotic above, which decays as \(u^{-2}e^{-\gamma/(\pi^2u^2)}\). Orders \(s\le1\) would imply some order strictly between \(1\) and \(3/2\) and are thereby also ruled out.

**4. Fourier aliasing and RMS upper bound.** Periodic smoothness and uniform random shift give the absolutely convergent Fourier series
\[
Q_n(U)=\sum_{\ell\in\mathbb Z}\widehat g_a(\ell n)e^{2\pi i\ell U}.
\]
Uniform integration over \(U\) gives unbiasedness and the displayed exact variance by Parseval. Integrate by parts \(r\) times and use the Gevrey bound to find
\[
|\widehat g_a(k)|\le A\frac{B^r(r!)^{3/2}}{(2\pi|k|)^r},\qquad k\ne0.
\]
Choosing \(r\) of order \(|k|^{2/3}\) and using Stirling's inequality gives \(|\widehat g_a(k)|\le A'e^{-b'|k|^{2/3}}\). The sum over nonzero multiples of \(n\) is bounded by \(C'e^{-c'n^{2/3}}\) in RMS after adjusting constants.

**5. Sharpness of the envelope exponent.** If an RMS bound with any \(\beta>2/3\) held for all \(n\), then, because \(|\widehat g_a(n)|^2\) is a term of the variance for sample size \(n\), every positive-frequency Fourier coefficient would satisfy \(|\widehat g_a(n)|\le C e^{-cn^\beta}\); negative coefficients follow by reality. If necessary replace \(\beta\) by a number between \(2/3\) and \(1\). Differentiating the absolutely convergent Fourier series and bounding \(\sum_{k\ge1}k^r e^{-c k^\beta}\) by a gamma integral gives
\[
\|g_a^{(r)}\|_\infty\le A''B''^r(r!)^{1/\beta},
\]
which contradicts exact Gevrey order since \(1/\beta<3/2\). A faster bound valid for all but finitely many \(n\) could be extended to all \(n\) by increasing \(C\), so every proposed faster envelope fails infinitely often.

## Verification

Execute `python3 verify.py` with the Python standard library. It checks the inverse-CDF density identity at several parameters, symmetry, the Gaussian expectation, Fourier aliasing against integration over 512 shifts for six sample sizes, and numerical endpoint suppression. The supplied executable reports **218 passed finite checks**. Numerical integration checks have finite truncation and rounding error; they do not prove the all-parameter derivative inequalities or the sharp exponent, which follow from the analytical proof above. In particular finite sampled coefficient decay is not used as evidence of a universal lower bound.

## Relationship to prior work

Ouyang, Wang and He, *Quasi-Monte Carlo for unbounded integrands with importance sampling*, arXiv:2310.00650v1 (first public 2023-10-01), develop importance sampling for singular or unbounded QMC integrands; their inspected randomized estimates provide an algebraic power-law regime, not this explicit Gevrey-optimal stretched exponential. Suzuki, Hyvönen and Karvonen, *Möbius-Transformed Trapezoidal Rule*, arXiv:2407.13650v1 (2024), derive algebraic convergence in periodic Sobolev classes and analyze randomization, but the inspected theorem and proof do not give a sharp fixed-target \(n^{2/3}\) Fourier envelope. The boundary-damping alternative of Pan, Ouyang and He, arXiv:2509.07509 (2025), concerns another mapping. Classical Gevrey-Fourier equivalences provide the mechanism; their standard general implications are not claimed new. The mathematical observation here is the exact Gevrey classification and sharp RMS envelope for this natural Gaussian-moment/Cauchy-proposal pairing. Prior unlocated equivalent examples in specialized saddle-point or quadrature literature remain possible.

## Limitations

The result treats a single scalar Gaussian exponential moment, standard Cauchy proposal, and one randomly shifted periodic lattice in exact arithmetic. It does not prove any pointwise matching lower bound for all \(n\), large-deviation estimate, finite-precision numerical stability, or superiority over specially designed alternative quadrature. The bounds' constants can degenerate as \(a\uparrow1/2\). The publication-priority comparison is best-knowledge rather than a proof of uniqueness.

## References

1. Ouyang, Wang, He, *Quasi-Monte Carlo for unbounded integrands with importance sampling*, arXiv:2310.00650v1, https://arxiv.org/abs/2310.00650 (first public 2023-10-01).
2. Suzuki, Hyvönen, Karvonen, *Möbius-Transformed Trapezoidal Rule*, arXiv:2407.13650v1, https://arxiv.org/abs/2407.13650 (2024).
3. Pan, Ouyang, He, *Quasi-Monte Carlo integration over \(\mathbb R^s\) with boundary-damping importance sampling*, arXiv:2509.07509, https://arxiv.org/abs/2509.07509 (2025).
4. Trefethen and Weideman, *The exponentially convergent trapezoidal rule*, SIAM Review 56 (2014), 385–458, https://doi.org/10.1137/130932132.
