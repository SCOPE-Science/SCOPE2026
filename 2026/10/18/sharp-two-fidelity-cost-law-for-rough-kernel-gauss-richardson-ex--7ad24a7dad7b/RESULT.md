# Sharp two-fidelity cost law for rough-kernel Gauss–Richardson extrapolation

## Finding

Consider the objective-prior Gauss–Richardson extrapolation (GRE) posterior for a scalar continuum limit. Let the error envelope be \(b(x)=x\), the normalized-error covariance be the exponential (Matérn-\(1/2\)) kernel
\[
k_e(x,y)=\exp(-|x-y|/\ell),\qquad \ell>0,
\]
and the computational cost of a simulation at fidelity \(x\) be \(c(x)=1/x\). Fix the prior scale to \(\sigma^2=1\). For two distinct simulations at \(0<x<y\leq1\), denote the posterior variance of the continuum-limit estimate by \(V(x,y)\). For every budget \(C>2\), put
\[
V_*(C)=\inf\{V(x,y):0<x<y\leq1,\quad x^{-1}+y^{-1}=C\}.
\]
Then
\[
\boxed{\lim_{C\to\infty}C^3V_*(C)=\frac{12\sqrt3}{\ell}.}
\]
Moreover, for **every** family of admissible two-point designs indexed by \(C\to\infty\),
\[
C^3V(x_C,y_C)\longrightarrow\frac{12\sqrt3}{\ell}
\quad\Longleftrightarrow\quad
\frac{y_C}{x_C}\longrightarrow2+\sqrt3.
\]
In particular, the constant ratio \(y/x=2+\sqrt3\) is feasible for all sufficiently large \(C\) and attains the sharp leading coefficient. At every admissible budget, there is also the nonasymptotic lower bound
\[
\boxed{V(x,y)\geq\left(\frac{\ell C^3}{12\sqrt3}+C^2\right)^{-1}.}
\]
Using the entire budget on one simulation at \(x=C^{-1}\) produces posterior variance \(C^{-2}\), so the optimally located **two** simulations gain one full power of the budget in this rough-kernel model:
\[
\frac{V_*(C)}{C^{-2}}\sim\frac{12\sqrt3}{\ell C}.
\]
The statements concern a *fixed-scale model posterior variance*, not an estimated-scale credible interval or a frequentist error guarantee.

## Assumptions and scope

The continuum target is \(f(0)\); the two exact deterministic simulator outputs are \(f(x)\) and \(f(y)\). The GRE objective-prior covariance uses a free intercept and normalized-error kernel \(k_e\), resulting in the two-by-two matrix
\[
K_b(x,y)=\begin{pmatrix}
x^2&xy\rho\\xy\rho&y^2
\end{pmatrix},\qquad
\rho=e^{-(y-x)/\ell}\in(0,1).
\]
Its corresponding continuum posterior variance is
\[
V(x,y)=\bigl(\mathbf1^{\mathsf T}K_b(x,y)^{-1}\mathbf1\bigr)^{-1}.
\]
The covariance is strictly positive definite for distinct points; no observations at zero fidelity are assumed. The boundary \(y\leq1\) keeps the design within the usual bounded fidelity domain. The total computational cost is *exactly* \(C\), and \(\ell\) is fixed as \(C\to\infty\). No assumption is made about the realized numerical outputs \(f(x),f(y)\), since this design criterion does not depend on them when scale is fixed.

## Proof

**Step 1: exact precision identity.** Direct inversion of \(K_b\) gives
\[
J(x,y):=\frac1{V(x,y)}
=\frac{x^{-2}+y^{-2}-2\rho/(xy)}{1-\rho^2}.
\]
Set \(u=1/x>v=1/y\). Rearranging yields the exact positive decomposition
\[
J=\frac{(u-v)^2}{1-\rho^2}+\frac{2uv}{1+\rho}.
\]
In particular, both summands have nonnegative coefficients and are well-defined at distinct positive fidelities.

**Step 2: budget parametrization.** The constraint \(u+v=C\) allows the unique parameter \(w=(u-v)/C\in(0,1)\), giving
\[
u=\frac C2(1+w),\quad v=\frac C2(1-w),\quad
x=\frac2{C(1+w)},\quad y=\frac2{C(1-w)}.
\]
The restriction \(y\leq1\) is equivalent to \(w\leq1-2/C\). Also,
\[
y-x=\frac{4w}{C(1-w^2)},\qquad
\rho=\exp\!\left[-\frac{4w}{\ell C(1-w^2)}\right].
\]
Therefore
\[
J_C(w)=\frac{C^2w^2}{1-\exp[-8w/(\ell C(1-w^2))]}
+\frac{C^2(1-w^2)}{2\{1+\exp[-4w/(\ell C(1-w^2))]\}}.
\]
This identity holds for all admissible \(C,w\), not only asymptotically.

**Step 3: a uniform lower bound for the variance.** For \(t>0\), the elementary inequality \(e^t\geq1+t\) implies
\[
\frac1{1-e^{-t}}\leq1+\frac1t.
\]
Apply it to \(t=8w/[\ell C(1-w^2)]\). Bounding the second precision summand using \(1+\rho\geq1\), we obtain
\[
J_C(w)\leq\frac{\ell C^3}8w(1-w^2)
+C^2\left[w^2+\frac{1-w^2}{2}\right].
\]
The function \(w(1-w^2)\) on \([0,1]\) uniquely attains its maximum \(2/(3\sqrt3)\) at \(w_*=1/\sqrt3\). The square bracket is at most one. Hence, uniformly over all admissible designs,
\[
J_C(w)\leq\frac{\ell C^3}{12\sqrt3}+C^2.
\]
Taking reciprocals gives the stated finite-budget bound and
\[
\liminf_{C\to\infty} C^3V_*(C)\geq\frac{12\sqrt3}{\ell}.
\]
The proof is uniform even for budget-dependent \(w\) approaching either endpoint.

**Step 4: matching construction.** Fix \(w=w_*=1/\sqrt3\). Then \(y\leq1\) for all \(C\geq3+\sqrt3\). Since \(1-e^{-z}\sim z\) as \(z\downarrow0\), the exact formula of Step 2 gives
\[
\lim_{C\to\infty}\frac{J_C(w_*)}{C^3}
=\frac{\ell}8w_*(1-w_*^2)=\frac{\ell}{12\sqrt3}.
\]
Thus \(C^3V_C(w_*)\to12\sqrt3/\ell\), matching the global bound. Furthermore,
\[
\frac yx=\frac{1+w_*}{1-w_*}=2+\sqrt3.
\]

**Step 5: uniqueness in the asymptotic sense.** Suppose admissible \(w_C\) give \(C^3V_C(w_C)\to12\sqrt3/\ell\). Then \(J_C(w_C)/C^3\to\ell/(12\sqrt3)\). Dividing the uniform bound in Step 3 by \(C^3\), we find
\[
\liminf_{C\to\infty} w_C(1-w_C^2)\geq\frac2{3\sqrt3}.
\]
The reverse inequality always holds, and the maximizer is unique. Compactness of \([0,1]\) therefore forces \(w_C\to1/\sqrt3\), hence \(y_C/x_C\to2+\sqrt3\). Conversely, whenever this ratio tends to the specified value, \(w_C\to w_*\); the exact precision formula converges uniformly in a compact neighborhood of \(w_*\), so \(C^3V_C(w_C)\to12\sqrt3/\ell\). This proves the equivalence.

Finally, for a single design point with cost \(1/x=C\), the normalized-error covariance is the scalar \(x^2\); the objective-prior posterior variance equals \(x^2=C^{-2}\). This yields the stated one- versus two-fidelity comparison.

## Verification

Execute `python checker.py` from the accompanying files. The script checks the exact two-by-two inverse and precision decomposition symbolically; independently evaluates the variance by covariance inversion and by the precision decomposition across valid parameter grids; tests the universal finite-budget inequality; and verifies the sharp limiting constant at increasing budgets. The recorded run completed **114 symbolic and numerical consistency checks**.

The universal lower bound, all-budget quantifiers, the existence of the matching construction, and uniqueness of the limiting ratio are proved in Steps 1–5, not inferred from these finite checks.

## Relationship to prior work

Oates, Karvonen, Teckentrup, Strocchi and Niederer introduced GRE, its objective-prior posterior variance and cost-constrained fidelity selection in arXiv:2401.07562v1 (15 January 2024). Their Section 2.7 and Example 10 consider the *same* first-order envelope \(b(x)=x\), inverse-fidelity cost \(c(x)=x^{-1}\), and fixed-length-scale Matérn versus Gaussian kernels, but optimize over a finite 20-point candidate grid. They note that a rough kernel appears to favor concentrating resources on the finest fidelity within that discrete experiment. The present statement concerns continuous *two-point* optimal location as the budget diverges, giving an explicit sharp cubic law and unique ratio; it is not an assertion that their finite-grid computations are incorrect.

Older Ornstein–Uhlenbeck optimal-design studies address constant-trend estimation with stationary exponential covariance, and typically optimize spacing for a fixed sample size, rather than the fidelity-dependent covariance \(xy\exp(-|x-y|/\ell)\) under a reciprocal-fidelity cost. The later sparse GRE preprint develops high-dimensional extrapolation sparsity and adaptive model selection; its publicly retrieved sections retain a general design objective, but no exact two-fidelity cubic constant was identified. Equivalence hidden in more general Gaussian-design theory remains possible and is a priority limitation, not evidence of uniqueness.

## Limitations

The bound is specific to two distinct, noise-free fidelities with *exact* aggregate reciprocal cost; it is not an optimality result over arbitrary numbers of experiments or over an inequality budget with unsaturated expenditure. The result uses the Matérn-\(1/2\) (exponential) kernel, a first-order error envelope, fixed positive length scale, and known fixed GP scale. It describes formal GRE posterior variance, not a guaranteed error of every deterministic simulator or calibrated empirical credible intervals. If the posterior scale is estimated from the same two outputs, the estimated uncertainty need not have this design law. No claim is made about other Matérn smoothness parameters, other cost exponents, higher-dimensional fidelity vectors, or finite-precision inversion of nearly singular covariance matrices.

## References

1. C. J. Oates, T. Karvonen, A. L. Teckentrup, M. Strocchi, and S. A. Niederer, *Probabilistic Richardson Extrapolation*, arXiv:2401.07562v1 (first public 15 January 2024), Sections 2.1–2.2 and 2.7, https://arxiv.org/abs/2401.07562 ; journal version, https://doi.org/10.1093/jrsssb/qkae098 .
2. M. Zagoraiou and A. Baldi Antognini, *Optimal designs for parameter estimation of the Ornstein–Uhlenbeck process*, Applied Stochastic Models in Business and Industry 25 (2009), 583–600, https://doi.org/10.1002/asmb.749 (first online 3 December 2008).
3. C. J. Oates, R. Howey and T. Karvonen, *Sparse Probabilistic Richardson Extrapolation*, arXiv:2604.02072 (2 April 2026), https://arxiv.org/abs/2604.02072 .
