# Smooth but nonanalytic core of Brownian proportional-reset equilibria

## Finding

Let \(f\) be the stationary position density of one-dimensional Brownian motion with diffusivity \(D>0\) and independent rate-\(r>0\) Poisson events that update position by \(X\mapsto aX\), where \(0<|a|<1\). Put \(c=|a|\), \(\ell=\sqrt{D/r}\), and \(L=-\log c\). Then \(f\) is infinitely differentiable on the entire real line, real-analytic at every nonzero position, but **not real-analytic at the origin; indeed it belongs to no finite-order Gevrey class there**. Its complete Taylor jet is

\[
 f^{(2n)}(0)=(-1)^n f(0)\ell^{-2n}c^{-n^2}
 \prod_{j=0}^{n-1}(1-c^{2j+1}),\qquad
 f^{(2n+1)}(0)=0\quad(n\ge0).
\]

The density is positive at zero, so none of the displayed even derivatives vanish. In particular, the formal Taylor series around zero has **radius of convergence zero**, although every fixed-degree Taylor polynomial is a valid local asymptotic approximation.

There is a quantitative resolution of that apparent paradox. Define

\[
 T_{n-1}(x)=\sum_{j=0}^{n-1}\frac{f^{(2j)}(0)}{(2j)!}x^{2j},\quad
 t=\log(\ell/|x|),\quad n=\lfloor t/L\rfloor.
\]

For every nonzero \(x\) with \(0<|x|\le\ell c\) (hence \(n\ge1\)),

\[
 \boxed{\ |f(x)-T_{n-1}(x)|\le f(0)
   \exp\!\left(L-\frac{t^2}{L}\right).\ }
\]

Thus a number of Taylor terms growing logarithmically as the observation point approaches the origin achieves a super-algebraically small, explicit error, despite the divergence of the infinite Taylor series at every nonzero argument.

## Assumptions and scope

Between Poisson jumps, \(dX_t=\sqrt{2D}\,dB_t\) on the full line. At each jump, \(X_t=aX_{t-}\). The Brownian motion and rate-\(r\) Poisson clock are independent; \(D>0\), \(r>0\), and \(a\in(-1,0)\cup(0,1)\) are deterministic. The stationary law is unique. The displayed claims are about its density, not about first-passage distributions. Signed and positive resetting multipliers with the same absolute value have identical stationary one-point densities, but not necessarily identical multitime laws. The cases \(a=0\) and \(|a|=1\) are excluded: at \(a=0\) the stationary density is Laplace with a cusp; at \(|a|=1\) there is no stationary probability law under nonzero diffusion.

For clarity, write \((q;q)_j=\prod_{k=1}^{j}(1-q^k)\), with \((q;q)_0=1\), and \((q;q)_\infty=\prod_{k=1}^{\infty}(1-q^k)\) when \(0<q<1\). All formulas hold simultaneously for every admissible real parameter triple.

## Proof

**1. Stationary construction and arbitrary-order smoothness.** Successive independent Brownian increments over exponential waiting times have centered Laplace distributions of scale \(\ell\). At equilibrium the law can be represented as

\[
 X_\infty\ \stackrel{d}=\ \sum_{j=0}^{\infty}a^j Z_j,
 \qquad \mathbb E e^{iuZ_j}=\frac{1}{1+\ell^2u^2},
\]

where the \(Z_j\) are independent. This series converges in \(L^2\), since \(\sum_j a^{2j}<\infty\), and yields the unique stationary law of the contractive reset recursion. Its characteristic function is

\[
 \phi(u)=\prod_{j=0}^{\infty}\frac{1}{1+\ell^2c^{2j}u^2}.
\]

For any integer \(m\ge0\), choose more than \((m+1)/2\) factors from this product. Each is bounded by a constant times \(|u|^{-2}\) for large \(|u|\), and all remaining factors are at most one. Hence \(\int_{\mathbb R}|u|^m\phi(u)\,du<\infty\). Fourier inversion proves \(f\in C^\infty(\mathbb R)\), with

\[
 f^{(m)}(x)=\frac{1}{2\pi}\int_{\mathbb R}(-iu)^m e^{-iux}\phi(u)\,du.
\]

The transform is positive and integrable, so \(f(0)>0\). It is even, hence all odd derivatives at zero vanish.

**2. Exact derivative recursion.** The stationary adjoint equation, justified classically by the preceding smoothness, is

\[
 Df''(x)-rf(x)+\frac{r}{c}f(x/a)=0.
\]

Differentiating \(2j\) times and evaluating at zero yields

\[
 f^{(2j+2)}(0)=\ell^{-2}(1-c^{-(2j+1)})f^{(2j)}(0).
\]

Iterating from \(f(0)\) and collecting powers of \(c\) gives the claimed jet because \(\sum_{j=0}^{n-1}(2j+1)=n^2\).

**3. Exact analytic singular locus.** Finite partial fractions of the characteristic-function product, followed by dominated convergence, give the known exponential representation

\[
 f(x)=\frac{1}{2\ell(c^2;c^2)_\infty}
 \sum_{j=0}^{\infty}\frac{(-1)^jc^{j^2}}{(c^2;c^2)_j}
 \exp\!\left(-\frac{|x|}{\ell c^j}\right).
\]

For complex \(z\) in the open right half-plane, the same expression with \(x\) replaced by \(z\) converges uniformly on compact subsets: the absolute coefficient series is bounded by a constant times \(\sum_j c^{j^2}\), while \(|e^{-z/(\ell c^j)}|\le1\). It therefore extends \(f\) holomorphically from \((0,\infty)\) to \(\Re z>0\). Evenness proves real analyticity on \(( -\infty,0)\) as well.

Set \(P_n=\prod_{j=0}^{n-1}(1-c^{2j+1})\). Since \(0<c<1\), \(P_n\to P_\infty>0\). The exact derivatives give

\[
 \log|f^{(2n)}(0)|=Ln^2+O_{c,D,r}(n)
 \qquad(n\to\infty).
\]

Every finite Gevrey order \(s\ge1\) would instead impose a bound \(|f^{(2n)}(0)|\le A B^{2n}((2n)!)^s\), whose logarithm is only \(O(n\log n)\). Hence no such class is possible. In particular, the Taylor coefficients have unbounded \((2n)\)-th roots and the Taylor series has radius zero. This also proves that zero is the unique point of failure of real analyticity.

**4. Quantitative finite Taylor error.** By Fourier inversion, \(f(x)\) is the cosine transform of the nonnegative function \(\phi\). The elementary cosine-Taylor inequality

\[
 \left|\cos y-\sum_{j=0}^{n-1}\frac{(-1)^jy^{2j}}{(2j)!}\right|
 \le\frac{|y|^{2n}}{(2n)!}
\]

holds for all real \(y\). Integrating against \(\phi/(2\pi)\) and using the derivative formula yields

\[
 |f(x)-T_{n-1}(x)|
 \le\frac{|f^{(2n)}(0)|}{(2n)!}|x|^{2n}
 \le f(0)\exp(Ln^2-2nt).
\]

For \(n=\lfloor t/L\rfloor\), \(Ln^2-2nt=-t^2/L+L(n-t/L)^2\le-t^2/L+L\). This gives the stated bound. No claim of exact optimal truncation order is required.

## Verification

The accompanying `CHECKER.py` independently checks finite-Laplace-convolution partial fractions with exact rational arithmetic for three contraction factors and nine finite-product orders; it also compares the derived all-order derivatives with the independently evaluated exponential series, verifies odd-derivative cancellations, and checks both the cosine-Taylor error inequality and the logarithmic error envelope at representative parameter values. In the reproduced environment it completed **202 diagnostics**, with all passing.

These are finite checks of the formulas, not numerical proofs of \(C^\infty\) smoothness, non-Gevrey regularity, convergence of the residue series, or the universal quantifiers. Those statements follow from the preceding analytic arguments.

## Relationship to prior work

Biroli, Feld, Hartmann, Majumdar and Schehr (2024), Section II, derive the same stationary density and its exponential series, describe a Gaussian-shaped small-position core, and note an alternating-series cancellation necessary for the linear cusp term to vanish; they report numerical checks but no proof of that cancellation. Their characteristic-function and stationary-density formulas are accepted as prior work, not claimed here. Tal-Friedman, Roichman and Reuveni (2022) had already given the Laplace-sum representation for positive proportional resetting; Pierce (2022) studied the corresponding pantograph equation. Grzywny, Palmowski, Szczypkowski and Trojan (first public December 2024), Proposition 2.22, prove \(C^\infty\) regularity for stationary densities of a much broader stable-process partial-resetting class; global smoothness is accordingly **not** separately claimed as novel. Their Proposition 2.22, adjacent moment formulas and Section 2.4 do not assert the exact origin jet, Gevrey obstruction, or the logarithmically adapted local Taylor estimate. Ferreiro-Castilla and Utzet (2010) provide general inverse-transform expansions for infinite convolutions of exponential/Laplace laws. Those known results motivate, but do not state, the all-order jet, zero-radius/non-Gevrey classification, or quantitative variable-order Taylor approximation proved here.

The first-order cancellation also follows from Euler's classical \(q\)-binomial identity and is **not** an originality claim in isolation. The theorem concerns the full regularity/approximation dichotomy, not a newly discovered elementary product identity.

## Limitations

Analyticity away from zero follows readily from the known exponential series, and global smoothness is known in a broader setting (Grzywny et al.); the original contributions asserted are the complete origin jet, the exact nonanalytic/Gevrey obstruction, and the explicit log-squared small-position approximation bound. These statements use deterministic strict contraction and nondegenerate Brownian forcing. No analogous claim is made for random multipliers, different waiting-time laws, additional drift, non-Brownian noise, or analytic behavior of multitime distributions. The analytic result does not establish publication priority: older general pantograph and infinite-convolution theorems may provide a route to the same conclusions, and independent expert review has not occurred.

## References

1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (first publicly available 2024-06-12), https://arxiv.org/abs/2406.08387 .
2. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363, https://arxiv.org/abs/2205.03363 .
3. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215, https://arxiv.org/abs/2204.07215 .
4. T. Grzywny, Z. Palmowski, K. Szczypkowski and B. Trojan, *Stationary states for stable processes with partial resetting*, arXiv:2412.15626v1 (first publicly available 2024-12-20), Proposition 2.22 and Section 2.4, https://arxiv.org/abs/2412.15626 .
5. A. Ferreiro-Castilla and F. Utzet, *Inversion of analytic characteristic functions and infinite convolutions of exponential and Laplace densities*, arXiv:1009.1543, https://arxiv.org/abs/1009.1543 .
