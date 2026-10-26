# Hybrid atomic–continuous spectral zeros: a new fractional boundary law

## Finding
Let \(m\ge1\) be an integer and \(\kappa>0\). Let \((\zeta_j)_{j\in\mathbb Z}\) and \(X\) be independent standard proper complex Gaussian variables. Define
\[
\xi_n=\sum_{j=0}^{m}(-1)^j\binom mj\zeta_{n-j}+\sqrt\kappa\,X,\qquad f(z)=\sum_{n\ge0}\xi_nz^n\quad(|z|<1).
\]
The stationary coefficient sequence has spectral measure \((2-2\cos\theta)^m\,d\theta/(2\pi)+\kappa\delta_0\): an atom located exactly at the sole zero of the continuous spectral density. Put \(t=1-r^2\), \(\alpha=1/(2m+2)\), let \(N(r)\) count the zeros in \(|z|<r\) with multiplicity, and let \(\rho\) be the expected zero intensity per unit Euclidean area. Then
\[
\boxed{\mathbb EN(r)=\frac{r^2}{1-r^2}-\frac{\alpha\kappa^\alpha}{\sin(\pi\alpha)}(1-r^2)^{\alpha-1}+o((1-r^2)^{\alpha-1}).}
\]
For every fixed real \(x\),
\[
\boxed{\lim_{r\uparrow1}\pi(1-r^2)^2\rho\bigl(re^{i(1-r^2)^\alpha x}\bigr)=1-\left(\frac{\kappa}{\kappa+x^{2m+2}}\right)^2.}
\]
Thus an atomic spectral line placed at a continuous zero of order \(2m\) yields the sharp angular scale \((1-r^2)^{1/(2m+2)}\) and the zero-count deficit exponent \((2m+1)/(2m+2)\). For \(m=1\) the deficit has order \((1-r^2)^{-3/4}\), unlike the previously known isolated-atom \((1-r^2)^{-1/2}\) case.

## Assumptions and scope
The variables are mutually independent proper (circular) complex Gaussians of variance one, except for the shared factor multiplied by \(\sqrt\kappa\). The parameter \(m\) is an arbitrary **fixed** positive integer and \(\kappa\) is any **fixed** positive real number; no uniformity as these parameters vary is claimed. The spectral measure is not normalized to mass one, as multiplying all coefficients by a nonzero constant leaves zeros unchanged. The angular profile is a pointwise statement for fixed \(x\in\mathbb R\); no claim about convergence of the full zero process is made.

Write \(w_m(\theta)=(2-2\cos\theta)^m\) and let \(P_r\) denote the ordinary circle Poisson kernel (convolution with \(d\theta/(2\pi)\)). The Poisson extension has the exact finite Laurent-Fourier form
\[
W_m(r,\theta)=P_r*w_m(\theta)=\binom{2m}{m}+2\sum_{j=1}^m(-1)^j\binom{2m}{m+j}r^j\cos(j\theta).
\]
Set \(d(r,\theta)=|1-re^{i\theta}|^2\). The exact diagonal covariance is
\[
K(re^{i\theta},re^{i\theta})=\frac{W_m(r,\theta)}{1-r^2}+\frac{\kappa}{d(r,\theta)}.
\]
These identities completely specify the objects and normalizations used below.

## Proof
**1. Covariance and counting identity.** The finite difference filter has multiplier \((1-e^{i\theta})^m\), giving \(w_m\). The independent common Gaussian factor is a rank-one spectral atom at angle zero. Positivity of \(K\) follows from the nonzero absolutely continuous part. The Edelman–Kostlan identity gives \(\rho=(4\pi)^{-1}\Delta\log K\); its disk integral, or Jensen's circular mean, gives
\[
\mathbb EN(r)=\frac r2\frac{d}{dr}\frac1{2\pi}\int_{-\pi}^{\pi}\log K(re^{i\theta},re^{i\theta})\,d\theta.
\]
Put \(t=1-r^2\), \(r=\sqrt{1-t}\), and \(H=W_m+\kappa t/d\). Since \(K=H/t\), the identity becomes
\[
\mathbb EN(r)=\frac{r^2}{t}-r^2 I'(t),\qquad I(t)=\frac1{2\pi}\int_{-\pi}^{\pi}\log H(\sqrt{1-t},\theta)\,d\theta.
\]
The derivative is taken for \(t>0\), where all denominators are positive.

**2. Uniform elementary bounds.** The finite Fourier formula implies \(W_m(r,\theta)=w_m(\theta)+O_m(t)\) and \(\partial_tW_m=O_m(1)\), uniformly in \(\theta\). Positivity of the Poisson kernel and its mass on an arc separated from zero, together with \(w_m(\theta)\asymp_m|\theta|^{2m}\), imply for some \(c_m>0\) and small \(t\),
\[
W_m(r,\theta)\ge c_m(t+|\theta|^{2m}),\qquad d(r,\theta)\asymp t^2+\theta^2\quad (|\theta|\le\pi).
\]
For the first inequality, the Poisson integral gives \(W_m\ge c_mt\) uniformly; where \(|\theta|^{2m}\) exceeds a sufficiently large multiple of \(t\), the uniform \(O_m(t)\) approximation gives \(W_m\ge c_m|\theta|^{2m}\). Here and below the Fourier-angle distance is represented in \([-\pi,\pi]\).

**3. Sharp disk-count coefficient.** Factor \(H=W_m(1+\kappa t/(dW_m))\). Its logarithmic derivative is
\[
I'(t)=\frac1{2\pi}\int\frac{W_{m,t}}{W_m}\,d\theta+\frac1{2\pi}\int \frac{\kappa}{dW_m+\kappa t}\left(1-t\frac{d_t}{d}-t\frac{W_{m,t}}{W_m}\right)d\theta.
\]
The first integral is \(O_m(t^{-1+1/(2m)})=o(t^{\alpha-1})\). Indeed, integrate the bound \(C_m/(t+|\theta|^{2m})\). Also, \(d_t=-1+\cos\theta/r\), so both \(t|d_t|/d\) and \(t|W_{m,t}|/W_m\) remain bounded for \(0<t<t_0\). For each fixed \(x\ne0\), in the substitution \(\theta=t^\alpha x\),
\[
\frac{dW_m}{t}\longrightarrow x^{2m+2},\quad
 t\frac{d_t}{d}\longrightarrow0,\quad
 t\frac{W_{m,t}}{W_m}\longrightarrow0.
\]
The rescaled principal integrand is dominated by \(C_m/(1+|x|^{2m+2})\) using the lower bounds in Step 2. The outer region \(|\theta|\ge\delta\) contributes only \(O(1)\). Dominated convergence therefore gives
\[
\lim_{t\downarrow0}t^{1-\alpha}I'(t)=\frac1{2\pi}\int_{\mathbb R}\frac{\kappa}{\kappa+x^{2m+2}}\,dx
=\frac{\alpha\kappa^\alpha}{\sin(\pi\alpha)}.
\]
The last equality is the standard beta integral \(\int_0^\infty(1+u^p)^{-1}du=(\pi/p)\csc(\pi/p)\) with \(p=2m+2\). Substitution in the exact counting identity proves the first boxed formula.

**4. Angular profile.** For \(x\ne0\), set \(\theta=t^\alpha x\). The same uniform approximations give
\[
H=t^{1-2\alpha}\left(x^{2m}+\frac\kappa{x^2}+o(1)\right),\qquad
\frac{tH_t}{H}\longrightarrow\frac\kappa{\kappa+x^{2m+2}},\qquad
\frac{t^2H_{tt}}H\longrightarrow0.
\]
All these partial derivatives hold at fixed \(\theta\) before substituting the scaling. The radial part of the Laplacian is \(4r^2\partial_{tt}-4\partial_t\); the angular part is \(r^{-2}\partial_{\theta\theta}\). The latter contributes \(o(t^{-2})\) to \(\Delta\log H\), since \(\partial_{\theta\theta}\log H=O_{m,\kappa,x}(t^{-2\alpha})\). Consequently
\[
\frac{t^2}{4}\Delta\log H\longrightarrow-\left(\frac\kappa{\kappa+x^{2m+2}}\right)^2.
\]
The contribution of \(-\log t\) is exactly \(1/(\pi t^2)\) to \(\rho\). At \(x=0\), use the alternative factorization \(K=(\kappa/d)(1+dW_m/(\kappa t))\). Because \(d(r,0)=O(t^2)\) and \(W_m(r,0)=O(t)\), direct differentiation of the finite Fourier polynomial shows \(\Delta\log(1+dW_m/(\kappa t))=O_{m,\kappa}(1)\) at angle zero; the term \(-\log d\) is harmonic in the open disk. Thus \(t^2\rho(r)\to0\), completing the second boxed statement.

## Verification
The standalone `check_hybrid.py` reproduces finite-filter covariances and tests the exact covariance-based intensity by independent radial and angular differentiation at multiple shrinking scales. It also evaluates the *exact* circular Jensen derivative by high-precision quadrature and compares its scaled limit with the beta-integral coefficient for several values of \(m\) and \(\kappa\). Tests are corroboration; the proof of all integers \(m\ge1\), all positive \(\kappa\), and the infinite radial limit is analytical in Steps 1–4.

## Relationship to prior work
Noda–Shirai (arXiv:2106.02860v1, 5 June 2021) study stationary Gaussian Taylor zeros. Their Theorem 1.3 addresses finitely dependent processes with purely continuous spectral densities having higher-order zeros; their Example 2.6 computes the distinct **isolated-atom-plus-flat-background** case, equivalent here to \(m=0\), with deficit exponent \(1/2\). Neither construction has an atom co-located with a zero of its continuous background. The present exponent \((2m+1)/(2m+2)\), beta-integral coefficient and angular profile are not instances of the formulas stated for those two separately treated models.

Shirai (arXiv:2501.02586, first posted 5 January 2025) provides a general integral representation of the one-point zero intensity for spectral measures (Proposition 3.1), which applies in principle to this mixed measure, but his quantitative boundary-density Theorem 2.1 assumes absolute continuity. The representation is an important starting point rather than a worked-out hybrid singular-limit formula. Existing smooth-zero angular-layer results also exclude atoms; unlike them, here the local balance is between the atomic Poisson peak and an order-\(2m\) continuous zero. General covariance identities alone do not specify the emerging fractional exponent or constant without the singular asymptotic analysis.

## Limitations
This is an expected one-point and disk-count theorem for the explicit finite-difference family with a fixed common Gaussian factor, not a result on fluctuations or higher correlation functions. The two parameters are fixed in every limit. The pointwise angular profile does not imply a limiting zero point process. A more general smooth continuous density vanishing to order \(2m\) is plausible but is not claimed or proved here. No independent audit has been performed. Historical priority beyond the cited and searched literature remains a possibility.

## References
1. K. Noda and T. Shirai, *Expected number of zeros of random power series with finitely dependent Gaussian coefficients*, arXiv:2106.02860v1 (5 June 2021), especially Theorem 1.3 and Example 2.6. https://arxiv.org/abs/2106.02860
2. T. Shirai, *The density of zeros of random power series with stationary complex Gaussian coefficients*, arXiv:2501.02586 (first posted 5 January 2025), especially Theorem 2.1 and Proposition 3.1. https://arxiv.org/abs/2501.02586
