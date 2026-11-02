# Spectral-reflection coupling is sharp for two-step Haar-frame finite-difference descent

## Finding

Let \(d\ge2\), let \(H\in\mathbb R^{d\times d}\) be symmetric positive definite with orthonormal eigensystem \((\lambda_i,v_i)_{i=1}^d\), and put \(f(x)=\tfrac12x^{\mathsf T}Hx\). For \(h>0\) and \(0<\alpha<2/\lambda_{\max}(H)\), consider the full-frame, forward-difference zeroth-order iteration
\[
 x_{k+1}=x_k-\alpha\sum_{j=1}^d
 u_{k,j}\frac{f(x_k+h u_{k,j})-f(x_k)}h,
\]
where the columns \(u_{k,j}\) form a Haar-uniform orthogonal matrix \(U_k\). Require each consecutive pair \((U_{2m},U_{2m+1})\) to have two Haar marginals, with *arbitrary dependence within each pair*, while the pairs themselves are independent, identically distributed and independent of deterministic \(x_0\).

Set \(a_i=1-\alpha\lambda_i\) and
\[
 c_i=\frac{h^2}{4(d+2)(d+4)}\left[(\operatorname{tr}H)^2+2\operatorname{tr}(H^2)+4\lambda_i\operatorname{tr}H+8\lambda_i^2\right].
\]
For every integer \(m\ge1\), every admissible coupling satisfies the **simultaneous sharp spectral-mode bounds**
\[
 \mathbb E\bigl[(v_i^{\mathsf T}x_{2m})^2\bigr]
 \ge a_i^{4m}(v_i^{\mathsf T}x_0)^2+
 \alpha^2c_i(1-|a_i|)^2\frac{1-a_i^{4m}}{1-a_i^4},\qquad 1\le i\le d.
\]
Equality for *every mode and every horizon at once* is attained by independently drawing Haar \(U_{2m}\) for each block and setting
\[
 U_{2m+1}=S U_{2m},\qquad
 S=\sum_{i=1}^d s_i v_iv_i^{\mathsf T},\quad
 s_i=\begin{cases}-1,&a_i>0,\\+1,&a_i<0,\\\pm1,&a_i=0.\end{cases}
\]
Consequently the minimum stationary expected objective at *even* times is exactly
\[
 \boxed{\mathcal E_{\rm opt}=\frac{\alpha^2}{2}
 \sum_{i=1}^d \frac{\lambda_ic_i(1-|a_i|)^2}{1-a_i^4}.}
\]
Independent Haar frames instead give
\[
 \mathcal E_{\rm iid}=\frac{\alpha^2}{2}
 \sum_{i=1}^d\frac{\lambda_ic_i(1+a_i^2)}{1-a_i^4}.
\]
The **sharp per-eigenmode stationary variance ratio** is \((1-|a_i|)^2/(1+a_i^2)\), strictly less than one whenever \(a_i\ne0\). Optimal coupling switches from opposite signs to repeated signs *at the individual spectral threshold* \(\alpha\lambda_i=1\). In mixed-sign spectra, neither a globally repeated frame nor a globally negated frame is optimal.

## Assumptions and scope

All function values and matrix operations in the definition are exact. The finite-difference radius \(h\) is fixed and positive; no measurement noise is assumed. One-sided differences use \(d+1\) function values per update (one common base value and \(d\) displaced values). The result compares only couplings that preserve the Haar distribution of each full frame and have independent pairs. It permits arbitrary within-pair dependence, not merely signed-reflection couplings. The covariance comparison refers to every even-time spectral coordinate and its stationary limit; it does not optimize odd-time error, cross-pair dependent schemes, or adaptive couplings based on the current state.

## Proof

**1. Exact finite-difference noise.** For an orthonormal frame \(U=(u_1,\ldots,u_d)\), quadratic expansion gives
\[
 \mathcal G_h(x,U)=Hx+e_h(U),\qquad
 e_h(U)=\frac h2\sum_{j=1}^d(u_j^{\mathsf T}Hu_j)u_j.
\]
Thus the perturbation is *additive and independent of* \(x\). Changing the sign of any one column of a Haar frame preserves the law and changes that column's summand's sign; therefore \(\mathbb E e_h(U)=0\) and all unequal-column covariance cross terms vanish. Each individual column is uniform on the unit sphere. The sixth spherical moment formula, for all indices \(r_1,\ldots,r_6\), is
\[
 \mathbb E[u_{r_1}\cdots u_{r_6}]=
 \frac{\sum_{\pi}\delta_{r_{\pi_1}r_{\pi_2}}\delta_{r_{\pi_3}r_{\pi_4}}\delta_{r_{\pi_5}r_{\pi_6}}}{d(d+2)(d+4)},
\]
where the sum runs over the \(15\) pair partitions of the six positions. Contracting two tensor index pairs with \(H\) yields
\[
 \operatorname{Cov}(e_h(U))
 =\frac{h^2}{4(d+2)(d+4)}
 \left(\bigl[(\operatorname{tr}H)^2+2\operatorname{tr}(H^2)\bigr]I+4\operatorname{tr}(H)H+8H^2\right).
\]
This matrix is a polynomial in \(H\), hence is diagonal in its eigensystem, with strictly positive diagonal entries \(c_i\) displayed above.

**2. Two-step recurrence and universal lower bound.** Put \(B=I-\alpha H\), so \(Bv_i=a_iv_i\) and \(|a_i|<1\). Two updates within a block give
\[
 x_{2m+2}=B^2x_{2m}-\alpha\bigl(Be_h(U_{2m})+e_h(U_{2m+1})\bigr).
\]
The two noise coordinates in mode \(i\) have equal mean zero and equal variance \(c_i\), regardless of their coupling. Cauchy--Schwarz gives
\[
 \mathbb E[(a_ie_{0,i}+e_{1,i})^2]
 =c_i(1+a_i^2)+2a_i\mathbb E[e_{0,i}e_{1,i}]
 \ge c_i(1-|a_i|)^2.
\]
The block noises are independent and centered. Iterating the scalar variance recurrence and summing \(1+a_i^4+\cdots+a_i^{4(m-1)}\) proves the finite-horizon lower bound, including its deterministic initial-mean term.

**3. Simultaneous attainment and equality condition.** Let \(S\) be the spectral reflection in the finding. It is orthogonal and commutes with \(H\). Because \(H\) commutes with \(S\), the exact error obeys \(e_h(SU)=Se_h(U)\); Haar measure is invariant under left orthogonal multiplication. Consequently \(U\) and \(SU\) both have Haar marginals, and \(e_{1,i}=s_ie_{0,i}\). Hence \(a_ie_{0,i}+e_{1,i}=(a_i+s_i)e_{0,i}\), whose squared coefficient equals \((1-|a_i|)^2\), for all modes simultaneously. For \(a_i\ne0\), equality in the Cauchy--Schwarz bound requires \(e_{1,i}=-\operatorname{sgn}(a_i)e_{0,i}\) almost surely; this characterizes the *optimal error-coordinate alignment*, not a unique coupling of frames.

**4. Stationary comparison.** The two-step deterministic part \(B^2\) is a strict contraction and block noises have finite support radius, giving a unique stationary law for the even-time chain by the convergent affine random series. Taking the geometric-series limit gives \(\mathcal E_{\rm opt}\). Under independent consecutive Haar frames, cross-covariance vanishes and \(\mathbb E[(a_ie_{0,i}+e_{1,i})^2]=c_i(1+a_i^2)\), giving \(\mathcal E_{\rm iid}\). Dividing modewise variances yields the sharp ratio. When different \(a_i\) have opposite signs, one global sign cannot meet both necessary alignment conditions.

As an exact mixed-spectrum example, let \(H=\operatorname{diag}(2,1)\), \(\alpha=3/4\), \(h=1\), and \(x_0=0\). Then \((a_1,a_2)=(-1/2,1/4)\), so the optimal reflection is \(S=\operatorname{diag}(1,-1)\). The two stationary even-time coordinate variances under this coupling are \(15/128\) and \(351/2720\), compared with \(75/128\) and \(39/160\) for independent frames. The optimal and independent stationary objective values are respectively \(1977/10880\) and \(453/640\); their ratio is \(659/2567\).

## Verification

The standalone `verify.py` computes the sixth sphere moments by enumeration of all \(15\) pair partitions, contracts them for four exact spectra, checks the sharp reflection bounds with rational arithmetic in additional spectra, verifies the original one-sided finite-difference recurrence and reflection identity, and checks non-diagonal covariance and Haar sampling numerically. Run `python verify.py` after installing `numpy` as specified in `requirements.txt`. Numeric tests are supplementary; Steps 1--4 above prove the universal claims. The checker uses corrected positive-diagonal QR normalization to draw Haar frames.

## Relationship to prior work

Kozak, Molinari, Rosasco, Tenorio and Villa (first posted 2021-07-08) define the same one-sided orthogonal-subspace forward-difference method with *independent* frames. Their Section 4.2 explicitly sets aside a tailored quadratic convergence analysis. Their bounds do not optimize couplings between successive frame draws. Rando, Molinari, Villa and Rosasco (2022) study structured stochastic zeroth-order descent under independently sampled directions and derive rates, rather than sharp two-step fixed-marginal coupling risk. Feng and Wang (2022) study orthogonal-direction gradient and Hessian estimator variance, predominantly using *central* differences; their full-frame quadratic central-gradient estimator is exact, so it does not imply the nonzero one-sided additive-noise covariance or the step-dependent spectral reflection. Kühn and Rosenow (2023) examine temporal anticorrelation from epoch-based SGD sampling on quadratic losses, a relevant general mechanism, but their accessible abstract does not establish the present exact Haar-frame coupling optimization. Classical Cauchy--Schwarz correlation bounds are acknowledged as a critical ingredient, not claimed as novel. A general published theorem covering this precise structured one-sided estimator and all Haar-marginal frame couplings was not identified; publication priority remains subject to independent checking.

## Limitations

The result is exact only for quadratic objectives, full Haar orthogonal frames, fixed positive one-sided difference radius, stable constant steps, deterministic starts, and independently repeated two-step blocks. It is not a convergence theorem for general smooth functions or noisy function oracles. Constructing the optimal spectral reflection needs knowledge of Hessian eigenspaces, which can be expensive or unavailable in genuinely black-box optimization; the sharp lower bound is therefore also an information-rich benchmark. A central-difference rule can remove the particular quadratic truncation error but uses a different function-evaluation design. The theorem does not claim globally minimal noise among arbitrary cross-block, history-dependent, or non-Haar algorithms. The stationary calculation applies to even-time subsampling, not necessarily odd-time risk. Numerical checks cannot establish literature uniqueness or replace independent scientific validation.

## References

1. D. Kozak, C. Molinari, L. Rosasco, L. Tenorio, and S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941, first submitted 2021-07-08; full text https://arxiv.org/html/2107.03941v2 .
2. Y. Feng and T. Wang, *Stochastic Zeroth Order Gradient and Hessian Estimators: Variance Reduction and Refined Bias Bounds*, arXiv:2205.14737, first submitted 2022-05-29; text https://arxiv.org/abs/2205.14737 .
3. M. Rando, C. Molinari, S. Villa, and L. Rosasco, *Stochastic Zeroth order Descent with Structured Directions*, arXiv:2206.05124, first submitted 2022-06-10; text https://arxiv.org/abs/2206.05124 .
4. M. Kühn and B. Rosenow, *Correlated Noise in Epoch-Based Stochastic Gradient Descent: Implications for Weight Variances*, arXiv:2306.05300, first submitted 2023-06-08; abstract https://arxiv.org/abs/2306.05300 .
