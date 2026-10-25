# Sharp Gaussian alignment frontier for one-vector Ritz spectral preconditioning

## Finding

Let \(d\ge2\), \(\kappa>1\), \(\tau>0\), and
\[
H=\operatorname{diag}(\kappa,1,\ldots,1),\qquad
 g=(\sqrt\tau Z_1,Z_2,\ldots,Z_d)^\mathsf T,
\]
where the \(Z_i\) are independent standard normal random variables. Form the one-product subspace vector \(q=Hg/\|Hg\|_2\), its Rayleigh quotient \(\lambda=q^\mathsf THq\), and the rank-one spectral inverse preconditioner
\[
M=I-(1-\lambda^{-1})qq^\mathsf T.
\]
Write \(\chi\) for the spectral condition number of \(M^{1/2}HM^{1/2}\). This normalization preconditions the eigenvalue \(\kappa\) to one when \(q\) is the exact top eigenvector.

Define
\[
 t_* (\kappa)=\frac{2\kappa+1-\sqrt{4\kappa+5}}{2(\kappa-1)},
 \qquad T_\kappa=\kappa^2\tau\frac{1-t_*(\kappa)}{t_*(\kappa)}.
\]
Then the *exact* strict condition-number improvement probability is
\[
\boxed{\Pr\{\chi<\kappa\}=
I_{T_\kappa/(1+T_\kappa)}\!\left(\frac{d-1}{2},\frac12\right),}
\]
where \(I_z(a,b)\) is the regularized incomplete beta function. Equal conditioning has probability zero. In dimension two this simplifies to
\[
\boxed{\Pr\{\chi<\kappa\}=\frac2\pi\arctan\sqrt{T_\kappa}.}
\]
For every fixed \(d\ge2\) and every fixed \(c>0\), the critical covariance scale is \(\tau=c\kappa^{-3/2}\):
\[
\lim_{\kappa\to\infty}\Pr\{\chi<\kappa\}=
I_{c/(1+c)}\!\left(\frac{d-1}{2},\frac12\right).
\]
In particular for \(d=2\) the limiting probability is one half at \(c=1\), tends to zero if \(\tau\kappa^{3/2}\to0\), and tends to one if \(\tau\kappa^{3/2}\to\infty\) (for each fixed \(d\)).

The failure can be severe: over all unit vectors \(q\) the maximum preconditioned condition number is attained precisely when \(q_1^2=1/3\), and is asymptotic to \(4\kappa^2/27\) as \(\kappa\to\infty\). For \(d\ge3\), every nontrivial \(0<q_1^2<1\) also introduces a third distinct preconditioned eigenvalue. Consequently, generic right-hand sides require three exact-arithmetic conjugate-gradient steps after preconditioning whereas the original one-spike system requires at most two.

## Assumptions and scope

The model has one Hessian eigenvalue \(\kappa\), all other eigenvalues exactly one, one Hessian-multiplied Gaussian sketch, no oversampling or repeated subspace iteration, and the specified rank-one Rayleigh-quotient spectral inverse preconditioner. The covariance of the sketch before multiplication is \(\operatorname{diag}(\tau,1,\ldots,1)\). Gaussian samples vanish only on a null set, so \(q\) is well-defined almost surely. The spectral condition number refers to the symmetric positive definite preconditioned operator, not Euclidean singular values of a nonsymmetric left-preconditioned representation.

The model isolates the rank-one spectral-LMP mechanism used with approximate Ritz vectors. It does **not** assert the same distribution or probability for every Nyström construction, every ensemble-data-assimilation Hessian, multi-column sketches, or adaptive oversampling.

## Proof

**1. Deterministic reduction.** Put \(t=q_1^2\in[0,1]\). By rotational symmetry of the flat eigenspace, the action of \(H\) and of \(M^{-1}=I+(\lambda-1)qq^\mathsf T\) is nontrivial only on the plane spanned by the first coordinate axis and the projection of \(q\) onto its orthogonal complement; when \(d>2\), all remaining eigenvalues of \(M^{1/2}HM^{1/2}\) are one. The Rayleigh quotient is
\[
\lambda=1+(\kappa-1)t.
\]
The sum and product of the two plane eigenvalues are respectively
\[
S=\operatorname{tr}(M H)|_{\mathrm{plane}}=\kappa+2-\lambda,
\qquad D=\det(MH)|_{\mathrm{plane}}=\kappa/\lambda.
\]
Indeed \(M=I-(1-\lambda^{-1})qq^\mathsf T\) has determinant \(1/\lambda\), and \(\operatorname{tr}(MH)=\operatorname{tr}(H)-(1-\lambda^{-1})\lambda\). For \(0<t<1\), the determinant of \(H-M^{-1}\) on the plane is \(- (\kappa-1)^2t(1-t)<0\). Hence the two generalized eigenvalues strictly straddle one. Thus for every \(d\ge2\), with their ratio \(\chi\),
\[
W(\lambda):=\chi+\chi^{-1}+2=\frac{S^2}{D}
=\frac{\lambda(\kappa+2-\lambda)^2}{\kappa}.
\]
At the endpoints the same identity follows by continuity. The function \(r\mapsto r+r^{-1}+2\) is strictly increasing for \(r>1\); the unpreconditioned reference value is \((\kappa+1)^2/\kappa\).

**2. Exact improvement and worst-case thresholds.** Direct factorization gives
\[
\kappa\left[W(\lambda)-\frac{(\kappa+1)^2}{\kappa}\right]
=(\lambda-1)\bigl[\lambda^2-(2\kappa+3)\lambda+(\kappa+1)^2\bigr].
\]
The quadratic factor has roots \(\lambda_*=\kappa+(3-\sqrt{4\kappa+5})/2\) and \(\lambda^*=\kappa+(3+\sqrt{4\kappa+5})/2\). For \(\kappa>1\), \(1<\lambda_*<\kappa<\lambda^*\). Therefore \(\chi<\kappa\) holds **if and only if** \(t>t_*(\kappa)=(\lambda_*-1)/(\kappa-1)\), except for boundary equality.

Also
\[
W'(\lambda)=\frac{(\kappa+2-\lambda)(\kappa+2-3\lambda)}{\kappa}.
\]
Its unique interior maximum occurs at \(\lambda=(\kappa+2)/3\), or \(t=1/3\), where \(W_{\max}=4(\kappa+2)^3/(27\kappa)\). Solving \(\chi+\chi^{-1}+2=W_{\max}\) yields the exact maximum
\[
\chi_{\max}=\frac{W_{\max}-2+\sqrt{(W_{\max}-2)^2-4}}2
\sim\frac{4\kappa^2}{27}.
\]

**3. Exact Gaussian law.** With independent \(Z_i\) and \(U=\sum_{j=2}^d Z_j^2\), we have \(U\sim\chi^2_{d-1}\), independent of \(Z_1^2\sim\chi^2_1\), and
\[
t=\frac{\kappa^2\tau Z_1^2}{\kappa^2\tau Z_1^2+U}.
\]
The improvement condition is \(U<T_\kappa Z_1^2\). Since \(U/(U+Z_1^2)\sim\operatorname{Beta}((d-1)/2,1/2)\), the claimed incomplete-beta probability follows. For \(d=2\), the same ratio can be evaluated using the standard Cauchy distribution of \(Z_2/Z_1\), giving the arctangent expression.

**4. Sharp covariance scaling.** As \(\kappa\to\infty\), elementary expansion of the explicit root gives \(t_*(\kappa)=1-\kappa^{-1/2}+O(\kappa^{-1})\), so \(T_\kappa=\tau\kappa^{3/2}(1+o(1))\). Continuity and endpoint limits of the incomplete beta distribution prove all asserted transitions. For \(d=2\), the limit at \(\tau=\kappa^{-3/2}\) is \(2\arctan(1)/\pi=1/2\).

**5. Exact-arithmetic CG consequence.** For \(d\ge3\) and \(0<t<1\), the preconditioned spectrum consists of the two distinct plane eigenvalues strictly on opposite sides of one, plus the eigenvalue one on the \((d-2)\)-dimensional orthogonal complement. Thus it has three distinct eigenvalues versus the two distinct eigenvalues of \(H\). A generic right-hand side has nonzero projections onto all associated eigenspaces. The Krylov minimal-polynomial criterion then gives exactly three CG steps to exact termination after this preconditioner, compared with at most two before it. This statement concerns exact arithmetic and generic right-hand sides, not an assertion that a finite-tolerance PCG implementation always slows down.

## Verification

The standalone `check.py` reproduces the factorization and maximum algebraically, checks 25 exact rational condition comparisons, validates the full preconditioned spectra against the derived invariant in 6,000 independent SPD matrix instances in dimensions 2, 3, 4, 7 and 16, and compares four 200,000-draw Gaussian simulations to the exact two-dimensional probabilities. Run `python check.py` with Python, SymPy, and NumPy. The included `check_output.txt` is the observed result from this package's script; the proof above, not the finite tests, establishes the infinite-dimensional-in-parameter assertions.

## Relationship to prior work

Daužickaitė, Gürol, Destouches, Berre, and Weaver (2026) motivate using ensemble right-hand-side differences to construct randomized Hessian sketches for limited-memory preconditioning. Daužickaitė, Lawless, Scott, and van Leeuwen (2021) describe the spectral-LMP formula and randomized Ritz approximation in variational data assimilation. Giraud and Gratton (2006) investigate sensitivity of spectral preconditioners to inexact eigenpairs using first-order spectral perturbation. The present model provides an exact, non-perturbative condition-number decision boundary and a Gaussian probability transition for a single Hessian-multiplied sketch, rather than a general convergence guarantee for those published algorithms.

## Limitations

The full 2026 source paper was not available for a decisive complete-text comparison in this study; its abstract and introductory material were accessible. Equivalent special-case calculations in earlier perturbation, data-assimilation, or randomized-preconditioning literature remain a priority risk. The result is proved only for a one-spike Hessian and one Rayleigh-quotient spectral-LMP correction. The exact CG step comparison assumes exact arithmetic, a distinct auxiliary right-hand side, and generic nonzero projections. Neither average iteration counts under stopping tolerances nor wall-clock speedups are claimed.

## References

1. I. Daužickaitė, S. Gürol, M. Destouches, L. Berre, and A. T. Weaver, *Accelerating an ensemble of variational data assimilations with randomized preconditioning*, arXiv:2605.23571v1 (first publicly posted 2026-05-22), https://arxiv.org/abs/2605.23571.
2. I. Daužickaitė, A. S. Lawless, J. A. Scott, and P. J. van Leeuwen, *Randomised preconditioning for the forcing formulation of weak-constraint 4D-Var*, Quarterly Journal of the Royal Meteorological Society **147** (2021), 3719–3734, https://doi.org/10.1002/qj.4151.
3. L. Giraud and S. Gratton, *On the sensitivity of some spectral preconditioners*, SIAM Journal on Matrix Analysis and Applications **27** (2006), 1089–1105, https://doi.org/10.1137/040617546.
4. S. Gratton, A. Sartenaer, and J. Tshimanga, *On a class of limited-memory preconditioners for large scale linear systems with multiple right-hand sides*, SIAM Journal on Optimization **21** (2011), 912–935, https://doi.org/10.1137/08074008.
