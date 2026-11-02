# Unique optimal fixed-width intervals for correlated Gaussian products and their logarithmic displacement

## Finding

Let \((U,V)\) be centered jointly Gaussian with unit variances and correlation \(-1<\rho<1\), and put \(Z=UV\). For every interval half-width \(h>0\), the function
\[
M_{\rho,h}(c)=\Pr\{|Z-c|\le h\},\qquad c\in\mathbb R,
\]
has exactly one maximizer \(c_{\rho,h}\). It belongs to \((-h,h)\); it is positive, zero, or negative exactly when \(\rho\) is positive, zero, or negative. Its value is characterized exactly by
\[
\frac{K_0((h+c_{\rho,h})/(1-\rho^2))}{K_0((h-c_{\rho,h})/(1-\rho^2))}
=\exp\left(-\frac{2\rho h}{1-\rho^2}\right).
\]
Here \(K_0\) is the modified Bessel function of the second kind, defined by the integral below. For each fixed nonzero correlation, with \(d=1-\rho^2\) and Euler's constant \(\gamma\), the optimal shift has the sharp expansion
\[
c_{\rho,h}=\frac{\rho}{d}h^2\left[\log\frac{2d}{h}-\gamma\right]+o_\rho(h^2)
\qquad(h\downarrow0).
\]
Consequently the optimally placed interval gains a positive amount over the symmetric interval, with sharp equivalent
\[
M_{\rho,h}(c_{\rho,h})-M_{\rho,h}(0)
\sim\frac{\rho^2}{\pi d^{5/2}}h^3\left[\log\frac{2d}{h}-\gamma\right]^2.
\]
For \(\rho=0\) the centered interval is optimal at every width, and the gain is identically zero. In particular, despite the product density's unique (singular) mode at zero for every correlation, its most probable fixed-width interval is strictly shifted for every nonzero correlation.

## Assumptions and scope

The two marginals are standard normal, their joint law is Gaussian with correlation strictly between minus one and one, and the interval half-width is any strictly positive real number. No independence of the marginals is assumed. The exact uniqueness statement holds at all widths; both asymptotic statements hold with \(\rho\ne0\) fixed as \(h\) decreases to zero, not uniformly at correlation endpoints. The relevant classification is probability distribution theory (MSC 60E05).

## Proof

Put \(d=1-\rho^2>0\) and \(A=(\pi\sqrt d)^{-1}\). The Gaussian change-of-variables formula gives the product density for nonzero \(z\):
\[
f_\rho(z)=A\exp(\rho z/d)K_0(|z|/d),
\qquad K_\nu(t)=\int_0^\infty e^{-t\cosh s}\cosh(\nu s)\,ds\quad(t>0).
\]
This identity can also be recovered directly by integrating the joint Gaussian density over \(u\) with \(v=z/u\), taking account of the Jacobian \(1/|u|\), and reducing the resulting integral by substituting \(u^2\). The integral representation proves \(K_1(t)>K_0(t)>0\) for every \(t>0\). Since \(K_0'(t)=-K_1(t)\) and \(|\rho|<1\), differentiating \(\log f_\rho\) shows that the density is strictly increasing on the negative axis and strictly decreasing on the positive axis. It diverges logarithmically at zero and integrates to one.

The interval mass is continuously differentiable in its center, even when it contains zero, because the two endpoints are away from zero in the neighborhood of any center strictly between \(-h\) and \(h\):
\[
M'_{\rho,h}(c)=f_\rho(c+h)-f_\rho(c-h),\qquad c\ne\pm h.
\]
For \(c>h\) this derivative is negative, and for \(c<-h\) it is positive. For \(-h<c<h\) set
\[
G(c)=\log\frac{f_\rho(h+c)}{f_\rho(c-h)}
=\frac{2\rho h}{d}+\log K_0((h+c)/d)-\log K_0((h-c)/d).
\]
The derivative is
\[
G'(c)=-\frac1d\left[\frac{K_1((h+c)/d)}{K_0((h+c)/d)}+\frac{K_1((h-c)/d)}{K_0((h-c)/d)}\right]<0.
\]
Moreover \(G(c)\to+\infty\) as \(c\downarrow-h\) and \(G(c)\to-\infty\) as \(c\uparrow h\). There is therefore exactly one zero, with the derivative of the mass switching from positive to negative. The density divergence makes the endpoint cases \(c=\pm h\) nonmaximal by the same one-sided sign argument. This proves global existence, uniqueness, and the displayed Bessel equation. Since \(G(0)=2\rho h/d\), the sign of the maximizing center is the sign of \(\rho\). Reflection also yields \(c_{-\rho,h}=-c_{\rho,h}\).

For the asymptotics, write \(L_h=\log(2d/h)-\gamma\). The standard Bessel expansions, derivable from the integral representation, are
\[
K_0(t)=-\log(t/2)-\gamma+O(t^2|\log t|),\qquad
K_1(t)=t^{-1}+O(t|\log t|),\qquad t\downarrow0.
\]
For any fixed \(0<\varepsilon<1\), substitution of \(c=\pm\varepsilon h\) into the exact function \(G\) shows that its Bessel logarithm difference has magnitude asymptotic to \(\log((1+\varepsilon)/(1-\varepsilon))/L_h\), with the sign opposing that of \(c\). Because \(hL_h\to0\), the zero satisfies \(c_{\rho,h}/h\to0\). By the mean value theorem, for some \(\xi_h\) between the endpoints \(h\pm c_{\rho,h}\),
\[
\log K_0((h+c_{\rho,h})/d)-\log K_0((h-c_{\rho,h})/d)
=-\frac{2c_{\rho,h}}{hL_h}\big(1+o(1)\big).
\]
The exact root equation gives \(c_{\rho,h}=(\rho/d)h^2L_h(1+o(1))\). To sharpen the additive remainder, use \(c_{\rho,h}=O(h^2L_h)\) in the symmetric Taylor expansion about \(h\). The relative error in the mean-value derivative is \(O(h^2L_h^2)+O(h^2L_h)\), which is \(o(1/L_h)\). Consequently \(c_{\rho,h}=(\rho/d)h^2[L_h+o(1)]\), proving the claimed \(o(h^2)\) remainder.

Finally \(M'_{\rho,h}(0)=2A\sinh(\rho h/d)K_0(h/d)=2A(\rho/d)hL_h(1+o(1))\). Uniformly for \(|c|\le |c_{\rho,h}|=o(h)\), a further differentiation and the Bessel expansions give \(M''_{\rho,h}(c)=-2A/h\,(1+o(1))\). Taylor's theorem at zero, together with the derived optimal center, yields
\[
M_{\rho,h}(c_{\rho,h})-M_{\rho,h}(0)
=2A\frac{\rho}{d}hL_h\,c_{\rho,h}-\frac{A}{h}c_{\rho,h}^2+o(h^3L_h^2)
=A\left(\frac{\rho}{d}\right)^2 h^3L_h^2(1+o(1)),
\]
which equals the coefficient stated in the finding. Both parts of the result have now been proved without finite enumeration.

## Verification

A standalone numerical checker uses Bessel evaluations, a bracketed root solver and quadrature. It tests sign, unique endpoint density balance, symmetry, direct mass improvement, and the small-width displacement across several parameter choices. Running `python checker.py` returns the recorded assertions; these computations are finite diagnostics, not replacements for the analytic arguments. The exact Bessel identities and asymptotics supply the infinite conclusions.

## Relationship to prior work

The density of the product of correlated centered normal variables is classical; it is explicitly given in Robert Gaunt's 2022 open-access survey, which also treats the mode, median, and many distributional properties. The October 2026 work of Gaunt and Sutcliffe develops cumulative distribution functions and absolute moments of variance-gamma laws and supplies the recent context for seeking sharper concentration descriptions. These known formulas are inputs, not new discoveries. The present result concerns global maximization of fixed-width interval probabilities and the displacement/gain expansions; the inspected 2022 survey does not supply that classification. Available records did not establish that the October 2026 work treats interval optimization; its full text could not be inspected, so priority risk remains.

## Limitations

Historical novelty is based on the inspected full text of the 2022 survey, accessible summaries of the newer paper, and targeted literature and mathematical-record searches; absent hits do not establish priority. The explicit density and Bessel asymptotics are standard. No independent mathematical audit has been performed. The result is restricted to two correlated centered Gaussian factors; different marginals, noncentral products, or sums of products are not classified. The numerical checks are not proofs.

## References

1. R. E. Gaunt, *The basic distributional theory for the product of zero mean correlated normal random variables*, Statistica Neerlandica 76 (2022), 450–470, DOI:10.1111/stan.12267, https://onlinelibrary.wiley.com/doi/full/10.1111/stan.12267 .
2. R. E. Gaunt and H. L. Sutcliffe, *Closed-form evaluation of the cumulative distribution function and absolute moments of the variance-gamma distribution*, arXiv:2610.16540, first posted 2026-10-12, https://arxiv.org/abs/2610.16540 .
3. Standard modified Bessel-function integral representation and small-argument expansions for \(K_0\) and \(K_1\), also collected in the appendix to reference 1.
