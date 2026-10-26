# The strongest partial resets govern stationary density regularity

## Finding

Consider one-dimensional Brownian motion with diffusion generator \(D\partial_{xx}\), interrupted at independent Poisson times of rate \(r>0\). Each reset changes the position \(x\) to \(Qx\), where the multipliers are independent copies of \(Q\in[0,q_+]\) for a fixed \(q_+<1\), independently of the Brownian motion and reset times. The process has a unique invariant law, with even density \(f\). Put \(a=\sqrt{r/D}\) and \(p_0=\Pr(Q=0)\).

**Atomic-reset signature.** If \(p_0>0\), then the two one-sided spatial derivatives exist and
\[
f'(0+)-f'(0-)=-\frac{r}{D}p_0.
\]
Thus an atom at full resetting is recoverable exactly from the cusp in the stationary density, regardless of the other multipliers.

**Strictly partial-reset signature.** If, in addition, the multipliers satisfy \(0<q_-:=\operatorname*{ess\,inf}Q\le Q\le q_+<1\) almost surely, then \(f\in C^\infty(\mathbb R)\), but \(f\) is not real analytic at the origin. More sharply, for every integer \(k\ge0\), \((-1)^k f^{(2k)}(0)>0\), and
\[
\boxed{\lim_{k\to\infty}\frac{1}{k^2}\log\left|f^{(2k)}(0)\right|=-\log q_-}. 
\]
All odd derivatives at zero vanish. The leading growth exponent depends on the *essential smallest* reset multiplier and is independent of how rarely such small multipliers occur, provided the relevant neighborhoods have positive probability.

Equivalently, the nonnegative stationary characteristic function \(\phi(t)=\mathbb E e^{itX}\) has the sharp logarithmic-Fourier tail
\[
\boxed{\lim_{y\to\infty}\frac{\log\phi(ae^y)}{y^2}=\frac{1}{\log q_-}}.
\]
The logarithm on the right is negative; the displayed statement is consistent with the derivative-growth law above.

## Assumptions and scope

Brownian motion is standard under the normalization \(\operatorname{Var}(B_t)=2Dt\). The Poisson rate \(r\), diffusion coefficient \(D\), and upper contraction bound \(q_+<1\) are fixed. Reset multipliers are iid, independent of the driving processes, and supported on \([0,q_+]\). No density, finite support, or nonzero lower bound is assumed for the cusp assertion; the smoothness and sharp-growth assertion additionally requires the strictly positive essential infimum \(q_-\). Conclusions concern the unique stationary law, not a finite-time propagator. The interval of values \(Q\) may include atoms or be continuous.

Let \(L_0,L_1,\dots\) be iid symmetric Laplace variables with density \(\ell(x)=(a/2)e^{-a|x|}\), and \(Q_1,Q_2,\dots\) iid reset multipliers, mutually independent. Define \(P_0=1\) and \(P_j=\prod_{i=1}^{j}Q_i\) for \(j\ge1\). The absolutely convergent stationary perpetuity is
\[
X\overset d=\sum_{j=0}^\infty P_jL_j.
\]
Convergence holds in \(L^2\) since \(P_j\le q_+^j\), and almost surely by absolute summability in expectation.

## Proof

**1. Stationary representation and uniqueness.** Looking backward from a stationary observation time, the time since the latest Poisson reset and successive earlier inter-reset durations are independent exponentials of rate \(r\). Brownian increments over an independent exponential holding time have characteristic function \(r/(r+Dt^2)=1/(1+(t/a)^2)\), hence the Laplace law \(\ell\). Each earlier interval's contribution is multiplied by all subsequent reset factors, giving the asserted perpetuity. Alternatively, this perpetuity satisfies the stationary one-step fixed-point equation \(X\overset d=L+QX'\) with independent copies. Forward-coupled versions driven by the same Brownian motion, reset times and multipliers have position difference multiplied by at most \(q_+\) at each reset, so the difference tends to zero almost surely; this proves uniqueness among probability invariant laws. Since \(L\) has a density, so does \(X\), and symmetry makes \(f\) even.

**2. The cusp.** Let \(\nu\) be the law of \(QX'\) in the independent fixed-point representation. Then \(f=\ell*\nu\). The variable \(X'\) is absolutely continuous, and \(QX'=0\) holds with positive probability only when \(Q=0\), so \(\nu(\{0\})=p_0\). The function \(\ell\) is globally Lipschitz with bounded one-sided derivatives and \(\ell'(0+)-\ell'(0-)=-a^2\). Dominated convergence for right and left difference quotients of \(\ell(x-y)\), integrated against \(\nu(dy)\), shows that the jump in the one-sided derivative of \(f\) at the origin equals \(-a^2\nu(\{0\})\). As \(a^2=r/D\), this is the displayed formula.

**3. Fourier product and comparison.** Conditioning on the reset multipliers in the perpetuity gives
\[
\phi(t)=\mathbb E\prod_{j=0}^\infty\frac{1}{1+(tP_j/a)^2}>0.
\]
For \(q\in(0,1)\), define \(\Phi_q(t)=\prod_{j=0}^\infty(1+(tq^j/a)^2)^{-1}\), and let \(h_q=-\log q>0\). Splitting the logarithmic product at \(j=\lfloor y/h_q\rfloor\) gives
\[
\log\Phi_q(ae^y)=-\frac{y^2}{h_q}+O_q(y+1),\qquad y\to\infty.
\]
Indeed, for \(j\le y/h_q\), \(\log(1+e^{2(y-jh_q)})=2(y-jh_q)+O(e^{-2(y-jh_q)})\), and the remainder terms on either side of the cutoff have uniformly bounded geometric sums. Summing the leading arithmetic progression proves the formula; the stated weaker \(O_q(y+1)\) bound is sufficient.

Assume now \(0<q_-\le Q\le q_+<1\). Every \(P_j\ge q_-^j\) almost surely, so factorwise comparison yields \(\phi(t)\le\Phi_{q_-}(t)\), hence
\[
\limsup_{y\to\infty}y^{-2}\log\phi(ae^y)\le-1/h_{q_-}.
\]
To get a lower bound, fix any \(b\in(q_-,1)\) with \(\eta=\Pr(Q\le b)>0\). The essential-infimum property guarantees \(\eta>0\). Set \(n=\lceil y/h_b\rceil\), and restrict to the event \(Q_1,\dots,Q_n\le b\), of probability \(\eta^n\). Then \(P_j\le b^j\) for \(0\le j\le n\), while \(P_{n+\ell}\le b^n q_+^\ell\) for \(\ell\ge0\). Since \(e^yb^n\le1\), the remaining factors contribute at least the positive constant \(c_+=\prod_{\ell\ge0}(1+q_+^{2\ell})^{-1}\). Thus
\[
\phi(ae^y)\ge c_+\eta^n\Phi_b(ae^y).
\]
After division by \(y^2\), the event-probability cost \(n\log\eta=O_b(y)\) vanishes; hence \(\liminf y^{-2}\log\phi(ae^y)\ge-1/h_b\). Letting \(b\downarrow q_-\) gives the matching bound and the sharp Fourier-tail limit.

**4. All-order smoothness and sharp derivative growth.** The comparison \(0<\phi(t)\le\Phi_{q_-}(t)\), together with the deterministic quadratic logarithmic tail, implies \(\int_{\mathbb R}|t|^m\phi(t)\,dt<\infty\) for every nonnegative integer \(m\). Fourier inversion therefore yields a bounded \(C^\infty\) density and
\[
f^{(2k)}(0)=\frac{(-1)^k}{\pi}\int_0^\infty t^{2k}\phi(t)\,dt.
\]
The integral is strictly positive, which prevents cancellations. Substituting \(t=ae^y\), the portion with \(y\) in any fixed bounded interval contributes at most \(\exp(O(k))\). For large \(y\), the proven Fourier limit bounds the logarithm of the integrand between quadratic functions of the form \((2k+1)y-(h_{q_-}^{-1}\pm\varepsilon)y^2\), up to constants. Completing the square (or evaluating the Gaussian integral after exponentiation) shows
\[
\lim_{k\to\infty}\frac1{k^2}\log\int_0^\infty t^{2k}\phi(t)\,dt=h_{q_-}.
\]
The scale factor \(a^{2k+1}\) changes the logarithm only by \(O(k)\), proving the derivative-growth formula. Finally, \(\log(2k)!=O(k\log k)=o(k^2)\). The Taylor coefficients \(f^{(2k)}(0)/(2k)!\) therefore grow in absolute value faster than every fixed exponential in \(k\), so the Taylor series has zero radius of convergence. In particular \(f\) is not real analytic at the origin.

## Verification

The accompanying `verify.py` uses exact rational path enumeration and independent renewal recursion to check the stationary finite-convolution Fourier identity for both deterministic and two-point random multipliers. It also checks the deterministic contraction sandwiches, moment balance identities, a zero-reset Fourier cusp diagnostic, and quantitative finite-product logarithmic estimates. Its output is recorded in `verify_output.txt`; the infinite-tail and regularity claims follow from the proof above, not from those finite checks.

## Relationship to prior work

Assefa, Keller-Ressel and Palmowski (2026) introduce a general affine-reset polynomial-process framework and calculate moments and cross-moments; the present result concerns spatial regularity and all-order derivative asymptotics of a stationary density for a Brownian random-multiplier specialization. Di Bello et al. (2023), especially their stationary formula (27), already derive the product characteristic function for a **fixed** partial-reset multiplier; that product, and the perpetuity/finite moment recurrences, are not asserted here as novel. Kolb and Wübker (2026) develop invariant-law and conditioned-process results for deterministic partial resetting. Ferreiro-Castilla and Utzet (2010) establish analytic characteristic-function inversion and infinite Laplace convolution representations, providing additional preexisting tools for fixed coefficient sequences. The claimed advance is the **random-multiplier essential-infimum law for high derivatives**, coupled with the exact zero-reset cusp signature. Literature comparisons do not constitute an exhaustive priority guarantee.

## Limitations

The sharp derivative exponent requires a strictly positive essential lower bound on reset multipliers. When \(\operatorname*{ess\,inf}Q=0\) but \(\Pr(Q=0)=0\), neither all-order smoothness nor the indicated sharp exponent is asserted. The cusp statement applies when \(\Pr(Q=0)>0\) even if other reset factors are arbitrarily close to zero. Results do not address position-dependent reset marks, renewal times that are not exponential, or spatially heterogeneous diffusion. No independent audit of the proof or originality has been performed.

## References

1. J. Assefa, M. Keller-Ressel and Z. Palmowski, *Moments of polynomial processes under affine resetting*, arXiv:2610.01363v1, first submitted 2026-10-01, https://arxiv.org/html/2610.01363v1.
2. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722, first submitted 2023-05-23, https://arxiv.org/html/2305.13722v2.
3. M. Kolb and A. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive*, Bulletin of the London Mathematical Society, first published 2026-03-05, https://doi.org/10.1112/blms.70314.
4. A. Ferreiro-Castilla and F. Utzet, *Inversion of analytic characteristic functions and infinite convolutions of exponential and Laplace densities*, arXiv:1009.1543, first submitted 2010-09-08, https://arxiv.org/abs/1009.1543.
