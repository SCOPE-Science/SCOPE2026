# Finite-sample scalar-debiasing obstruction for rank-one Gaussian inverse-Hessian sketches

## Finding
For every integer \(m\geq2\), integer \(d>m\), scalar \(h>0\), ridge parameter \(\lambda>0\), and unit vector \(v\in\mathbb R^d\), consider the rank-one positive-semidefinite Hessian \(H=hvv^{\mathsf T}\). Let \(S\in\mathbb R^{m\times d}\) have independent \(N(0,1/m)\) entries. For any **deterministic** scalar regularizer \(\tau>0\), define the inverse-Hessian sketch
\[
W_\tau=S^{\mathsf T}(SHS^{\mathsf T}+\tau I_m)^{-1}S.
\]
There is **no** choice of \(\tau>0\) for which \(\mathbb E W_\tau=(H+\lambda I_d)^{-1}\).

In particular, choose the effective-dimension regularizer
\[
\tau_m=\lambda\left(1-\frac{h}{m(h+\lambda)}\right),
\]
obtained from the Marchenko–Pastur correction for this Hessian. There are scalars \(a_m,b_m\) such that
\[
\mathbb E W_{\tau_m}=a_m vv^{\mathsf T}+b_m(I_d-vv^{\mathsf T}),
\qquad
0<a_m<\frac{1}{h+\lambda},\quad b_m>\frac1\lambda.
\]
The two biases have **opposite signs** and obey the exact identity
\[
b_m-\frac1\lambda=\frac{h}{m\tau_m}\left(\frac1{h+\lambda}-a_m\right).
\]
The expectation is therefore not ordered with the desired inverse in the Löwner order. Along any sequence of dimensions \(d_m>m\), with \(h,\lambda\) fixed and \(m\to\infty\), the sharp leading directional biases are
\[
\lim_{m\to\infty}m\left(\frac1{h+\lambda}-a_m\right)
=\frac{h\lambda}{(h+\lambda)^3},\qquad
\lim_{m\to\infty}m^2\left(b_m-\frac1\lambda\right)
=\frac{h^2}{(h+\lambda)^3}.
\]

## Assumptions and scope
All matrices are real and all expectations concern the indicated Gaussian sketch alone. The regularizer \(\tau\) is fixed independently of \(S\); data-dependent choices, extra multiplicative corrections, determinant-weighted averaging, and non-Gaussian sketches are not covered. The ambient dimension is arbitrary subject to \(d>m\). The unregularized Hessian is rank one, but \(H+\lambda I_d\) is strictly positive definite. All matrix inverses exist because \(\tau>0\).

The effective dimension is exactly \(\operatorname{tr}(H(H+\lambda I_d)^{-1})=h/(h+\lambda)\), so \(\tau_m>0\) and is strictly below \(\lambda\).

## Proof
**1. Exact spectral reduction.** Rotational invariance permits taking \(v=e_1\). Put \(g=Sv\), and let \(z=Sw\) for any unit \(w\perp v\). Then \(g,z\) are independent \(N(0,I_m/m)\). Set \(X=\lVert g\rVert_2^2\), so \(X\stackrel d=\chi_m^2/m\). Sherman–Morrison gives
\[
g^{\mathsf T}(\tau I_m+hgg^{\mathsf T})^{-1}g=\frac X{\tau+hX}.
\]
The conditional expectation in any direction orthogonal to \(v\) is \(m^{-1}\operatorname{tr}(\tau I_m+hgg^{\mathsf T})^{-1}\). Reflection symmetry eliminates expected cross terms. Consequently
\[
\mathbb E W_\tau=a(\tau)vv^{\mathsf T}+b(\tau)(I_d-vv^{\mathsf T}),
\]
where
\[
a(\tau)=\mathbb E\frac X{\tau+hX},\qquad
b(\tau)=\frac1m\left(\frac{m-1}{\tau}+\mathbb E\frac1{\tau+hX}\right)
=\frac{1-ha(\tau)/m}{\tau}.
\tag{1}
\]
The target coefficients are \(a_*=1/(h+\lambda)\) and \(b_*=1/\lambda\). If both coefficients were matched exactly, (1) would **force**
\[
\tau=\lambda\left(1-\frac h{m(h+\lambda)}\right)=\tau_m.
\tag{2}
\]
Thus this is the only possible deterministic scalar regularizer for an unbiased expectation.

**2. Strict signal-side underestimation at the only candidate.** The gamma integration-by-parts identity for \(X\stackrel d=\chi_m^2/m\) is
\[
\mathbb E[(X-1)\phi(X)]=\frac2m\mathbb E[X\phi'(X)].
\]
With \(\phi(x)=(\tau+hx)^{-1}\), combined with (1), this yields
\[
(\tau+h)a(\tau)+\frac{2h\tau}{m}\mathbb E\frac X{(\tau+hX)^2}=1.
\tag{3}
\]
Cauchy–Schwarz and \(\mathbb EX=1\) give the **strict** inequality
\[
\left(\mathbb E\frac X{\tau+hX}\right)^2
<\mathbb E\frac X{(\tau+hX)^2},
\]
because \(X\) has a nondegenerate continuous distribution and \(h>0\). Thus, for \(a=a(\tau_m)\),
\[
(\tau_m+h)a+\frac{2h\tau_m}{m}a^2<1.
\tag{4}
\]
For the target \(a_*=1/(h+\lambda)\), however, the left side of (4) equals
\[
1+\frac{h(2\tau_m-\lambda)}{m(h+\lambda)^2}>1,
\]
since \(\tau_m>\lambda(1-1/m)\geq\lambda/2\) for all \(m\geq2\). The quadratic expression on the left side of (4) is strictly increasing in every nonnegative \(a\); hence \(a_m<a_*\). Equation (1) then gives \(b_m-b_*=h(a_*-a_m)/(m\tau_m)>0\). This contradicts exact simultaneous matching at the unique candidate from (2), and proves the stated impossibility for every deterministic scalar \(\tau>0\).

A finite-sample quantitative consequence of (4), obtained by comparing its monotone quadratic with its value at \(a_*\), is
\[
a_*-a_m>
\frac{h(2\tau_m-\lambda)}{m(h+\lambda)^2\left(\tau_m+h+4h\tau_m/[m(h+\lambda)]\right)}.
\]

**3. Exact leading asymptotics.** Rearranging (3) at \(\tau=\tau_m\) yields
\[
a_*-a_m=\frac h{m(h+\tau_m)}
\left(2\tau_m\mathbb E\frac X{(\tau_m+hX)^2}-\frac\lambda{(h+\lambda)^2}\right).
\tag{5}
\]
Couple \(X_m=m^{-1}\sum_{j=1}^m Z_j^2\) with independent standard-normal \(Z_j\). Then \(X_m\to1\) almost surely, and \(\tau_m\to\lambda\). Since \(\tau_m>\lambda/2\) and \(0\leq X_m/(\tau_m+hX_m)^2\leq1/(4h\tau_m)\), dominated convergence gives
\[
\mathbb E\frac{X_m}{(\tau_m+hX_m)^2}\longrightarrow\frac1{(h+\lambda)^2}.
\]
Equation (5) establishes the asserted signal coefficient. The exact bias relation from step 2 then establishes the nullspace coefficient. This coupling and all coefficients are independent of the choice of \(d_m>m\).

## Verification
The accompanying `verify.py` evaluates the gamma integrals by deterministic quadrature, tests (1), (3), (4), the quantitative bound, and the limiting coefficients for multiple sketch sizes and positive parameter combinations. It also reconstructs the **actual sketched inverse** by solving random finite matrices and checks the signal/nullspace formulas, with a seeded Gaussian Monte Carlo comparison. It completed 893 passing checks; see `verification_output.txt`. Computation checks the algebra and numerical regimes but is not the proof of the strict inequality for all real parameters or the infinite-sequence asymptotics.

Run from the directory containing the files: `python verify.py`. Numerical dependencies are listed in `requirements.txt`.

## Relationship to prior work
Romanov, Zhang and Pilanci (arXiv:2410.01374v1, submitted 2024-10-02) define \(S^{\mathsf T}(SHS^{\mathsf T}+\tilde\lambda I)^{-1}S\) and derive the effective-dimension regularizer used here. Their principal comparisons and bounds concern asymptotic bias, a data-driven choice of sketch size and regularization, and finite-sample concentration. The present theorem asks a different exact finite-sample question: whether **any deterministic scalar regularizer** removes mean bias simultaneously on the signal and nullspace, and what directional signs and sharp coefficients remain at the prescribed correction.

Zhang and Pilanci (PMLR 202, 2023) develop asymptotic shrinkage and non-asymptotic isotropic resolvent error results, including applications to Hessian sketches; their corrected covariance resolvent is not the exact same finite rank-one two-eigenspace expectation. LeJeune et al. (arXiv:2211.03751) analyze asymptotic equivalents of sketched pseudoinverses, including isotropic rank-deficient spectra, but do not state the present finite-dimensional impossibility and signed moment asymptotics. The gamma identities and Cauchy–Schwarz inequality are classical ingredients; novelty is asserted only for their combined consequence for this estimator, subject to the originality risks recorded separately.

## Limitations
The theorem is restricted to a deterministic ridge parameter, independent Gaussian sketches, positive ridge, and rank-one positive-semidefinite Hessians with \(m\geq2\). It does not establish bias signs for adaptive random ridge parameters, arbitrary spectra, orthogonal sketches, or the performance of a full Newton solver. The result is consistent with asymptotic low-bias theorems: neither directional bias remains bounded away from zero as \(m\to\infty\). A related exact finite-sample result may exist under other terminology; no claim of exhaustive literature uniqueness or independent audit is made here.

## References
1. E. Romanov, F. Zhang, M. Pilanci, *Newton Meets Marchenko–Pastur: Massively Parallel Second-Order Optimization with Hessian Sketching and Debiasing*, arXiv:2410.01374v1 (first submitted 2024-10-02), https://arxiv.org/abs/2410.01374.
2. F. Zhang, M. Pilanci, *Optimal Shrinkage for Distributed Second-Order Optimization*, Proceedings of Machine Learning Research 202 (2023), 41523–41549, https://proceedings.mlr.press/v202/zhang23ah.html.
3. D. LeJeune, P. Patil, H. Javadi, R. G. Baraniuk, R. J. Tibshirani, *Asymptotics of the Sketched Pseudoinverse*, arXiv:2211.03751, https://arxiv.org/abs/2211.03751.
