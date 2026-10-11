# Zero-free power-deficit radial Bergman kernels

## Finding

For every real exponent \(\gamma>0\) and every deficit parameter \(0\le q\le1\), the radial weighted Bergman kernel for \(1-q|z|^{2\gamma}\) on the unit disk is zero-free. More precisely, writing \(s=z\overline w\), it obeys the uniform half-plane certificate
\[
\operatorname{Re}\left((1-s)^2\mathcal K_{\gamma,q}(s)\right)\ge1,\qquad |s|<1.
\]
The inequality is strict at every point when \(q>0\); when \(q=0\), the left-hand side is identically \(1\), so the universal constant is sharp. An explicit, stronger disk-valued certificate is available for \(0<q<1\):
\[
\left|(1-q)(1-s)^2\mathcal K_{\gamma,q}(s)-1\right|<q.
\]
This family includes arbitrarily large degrees and nonintegral exponents, and reaches the boundary-vanishing weight at \(q=1\).

## Assumptions and scope

Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The Hilbert norm is
\[
\|f\|_{\gamma,q}^2=\frac1\pi\int_{\mathbb D}|f(z)|^2(1-q|z|^{2\gamma})\,dx\,dy.
\]
The weight is positive at every interior point, including the endpoint \(q=1\). Its radial monomials form a complete orthogonal basis, and its reproducing kernel is defined with respect to the displayed normalized measure. All claims are for real \(\gamma>0\), real \(q\in[0,1]\), and pairs of points strictly inside the disk; no assertion is made for arbitrary radial weights.

## Proof

**Step 1: normalized moments.** Orthogonality and the elementary radial integral give, for every integer \(n\ge0\),
\[
\|z^n\|_{\gamma,q}^2=\frac1{n+1}-\frac{q}{n+\gamma+1}
=\frac{(1-q)n+\gamma+1-q}{(n+1)(n+\gamma+1)}.
\]
The reproducing-kernel coefficient and series are therefore
\[
 c_n=\frac{(n+1)(n+\gamma+1)}{(1-q)n+\gamma+1-q},\qquad
\mathcal K_{\gamma,q}(s)=\sum_{n=0}^\infty c_n s^n.
\]
For \(0\le q<1\), the moments are bounded above and below by fixed positive multiples of \(1/(n+1)\); for \(q=1\), the displayed formula gives quadratic coefficient growth. Thus the series converges absolutely and locally uniformly for \(|s|<1\), which justifies its later summation and integration.

**Step 2: an exact integral formula for \(q<1\).** Set
\[
p=1+\frac\gamma{1-q}>1,
\qquad d\mu_p(u)=(p-1)u^{p-2}\,du,\quad 0<u<1.
\]
This is a probability measure. Direct algebra gives
\[
 c_n=\frac{n+1}{1-q}\left(1-q\frac{p-1}{n+p}\right)
=\frac{n+1}{1-q}\left(1-q\int_0^1u^{n+1}\,d\mu_p(u)\right).
\]
Since \(\sum_{n\ge0}(n+1)s^n=(1-s)^{-2}\) for \(|s|<1\), absolute convergence permits termwise integration and gives
\[
(1-q)(1-s)^2\mathcal K_{\gamma,q}(s)
=1-q\int_0^1 u\left(\frac{1-s}{1-us}\right)^2d\mu_p(u).
\tag{1}
\]

**Step 3: the critical contraction inequality.** For fixed \(0<u<1\), the function \(s\mapsto(1-s)/(1-us)\) is analytic on the closed unit disk. By the maximum-modulus principle its largest modulus lies on \(|s|=1\). With \(s=e^{i\theta}\) and \(c=\cos\theta\),
\[
\left|\frac{1-s}{1-us}\right|^2
=\frac{2-2c}{1+u^2-2uc}
\le\frac4{(1+u)^2},
\]
where the last expression is attained on the boundary only at \(s=-1\): the quotient is nonincreasing in \(c\), with derivative \(-2(1-u)^2/(1+u^2-2uc)^2<0\). Consequently, for every \(|s|<1\) and \(0<u<1\),
\[
\left|u\left(\frac{1-s}{1-us}\right)^2\right|
\le\frac{4u}{(1+u)^2}<1.
\tag{2}
\]
Integrating (2) against the probability measure \(\mu_p\) gives
\[
\left|\int_0^1u\left(\frac{1-s}{1-us}\right)^2d\mu_p(u)\right|<1.
\]
For \(0<q<1\), inserting this in (1) proves the disk certificate
\[
\left|(1-q)(1-s)^2\mathcal K_{\gamma,q}(s)-1\right|<q.
\]
Its real part yields
\[
\operatorname{Re}\bigl((1-s)^2\mathcal K_{\gamma,q}(s)\bigr)
>\frac{1-q}{1-q}=1.
\]
At \(q=0\), the moment formula gives \(\mathcal K_{\gamma,0}(s)=(1-s)^{-2}\), so equality holds identically.

**Step 4: the boundary deficit \(q=1\).** The exact coefficient reduces to
\[
c_n=\frac{(n+1)(n+\gamma+1)}\gamma.
\]
Using the classical sums for \(\sum(n+1)s^n\) and \(\sum(n+1)^2s^n\) yields
\[
\mathcal K_{\gamma,1}(s)
=\frac{(\gamma+1)+(1-\gamma)s}{\gamma(1-s)^3}.
\]
It follows that
\[
(1-s)^2\mathcal K_{\gamma,1}(s)
=1+\frac1\gamma\frac{1+s}{1-s},
\]
whose real part is strictly larger than \(1\), since
\[
\operatorname{Re}\frac{1+s}{1-s}=\frac{1-|s|^2}{|1-s|^2}>0
\]
for \(|s|<1\).

In every case, the multiplier \((1-s)^2\) is nonzero on \(\mathbb D\); the strictly positive real part of its product with the kernel excludes all kernel zeros. This proves the theorem.

## Verification

The companion `power_weight_verify.py` uses exact rational arithmetic to compare the moment-derived coefficients against the probability-mixture coefficients for a grid of real rational exponents and parameters, including the endpoint case. It independently evaluates the strict contraction on a finite complex sample and checks finite-series approximations of the half-plane statement. Execute it with `python power_weight_verify.py` using the Python standard library. The verification run completed successfully with 4,200 exact rational equalities and passing finite numerical checks. The infinite theorem is proved by Steps 1–4, not by numerical sampling.

## Relationship to prior work

Marinescu and Xing (arXiv:2609.24258v1; first posted September 21, 2026) study the regularity and analyticity of weighted Bergman kernels as weights vary, including a radial example where parameter-regularity fails without boundary-uniform estimates. Their results do not assert any zero-free theorem for the present power-deficit family.

Zeytuncu (arXiv:1009.2806v1, Theorem 1.5 and Section 2) constructs a decreasing radial, positive weight comparable to one whose Bergman kernel **has** zeros, demonstrating that radiality, decreasingness and norm comparability alone do not imply nonvanishing. The present result instead supplies an explicit exact certificate for the full smooth power-deficit family; no contradiction arises.

Perälä (arXiv:1703.05976v1, Section 3) constructs radial weights with prescribed finite numbers of kernel zeros. Its Section 2 records Hedenmalm's zero-free criterion for weights with logarithm subharmonic. In contrast, for \(0<q\le1\) and \(0<r<1\),
\[
\Delta\log(1-qr^{2\gamma})
=-\frac{4q\gamma^2r^{2\gamma-2}}{(1-qr^{2\gamma})^2}<0,
\]
so that cited criterion does not imply the power-deficit result. Boudreaux (arXiv:1802.01099v1) constructs weights equivalent to a given weight with vanishing kernels; it does not classify this prescribed family. The present proof is independent of any unverified global generalization from radial monotonicity or from equivalence of weighted spaces.

## Limitations

The statement applies only to \(1-q|z|^{2\gamma}\) with real \(\gamma>0\) and \(0\le q\le1\). It does not claim zero-freeness for arbitrary decreasing, radial, smooth or comparable weights, nor for sums of several distinct powers. The scalar formula is for the normalized disk area convention and the weighted Hilbert kernel, not the unweighted Bergman kernel of an arbitrary higher-dimensional domain. The numerical checker is finite and does not certify the infinite quantifiers. Literature comparison cannot exclude an unindexed classical equivalent.

## References

- G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258v1 (September 21, 2026), https://arxiv.org/html/2609.24258v1.
- Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806v1 (2010), https://arxiv.org/html/1009.2806v1.
- A. Perälä, *Vanishing Bergman Kernels on the Disk*, arXiv:1703.05976v1 (2017), https://arxiv.org/pdf/1703.05976.
- B. J. Boudreaux, *Equivalent Bergman Spaces With Inequivalent Weights*, arXiv:1802.01099v1 (2018), https://arxiv.org/html/1802.01099v1.
- H. Hedenmalm, *An Off-Diagonal Estimate of Bergman Kernels*, J. Math. Pures Appl. 79 (2000), 163–172, as cited and compared in Perälä (2017).
