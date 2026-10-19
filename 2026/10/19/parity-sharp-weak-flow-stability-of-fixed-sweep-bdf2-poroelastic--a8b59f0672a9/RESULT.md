# Parity-sharp weak-flow stability of fixed-sweep BDF2 poroelasticity splitting

## Finding

Consider the fixed-sweep, relaxed, second-order iterative splitting of Altmann and Deiml, equations (3.6a)--(3.6d) of [1]. On the scalar homogeneous poroelastic system with unit elastic and storage coefficients, fluid coefficient \(b>0\), coupling \(\kappa>0\), and step size \(\tau>0\), write \(\varepsilon=2\tau b/3\) and fix the integer sweep count \(K\geq1\). Define
\[
 a_K(\kappa)=(-1)^{K-1}\frac{\kappa^K}{(2+\kappa)^{K-1}}.
\]
For every fixed pair \((K,\kappa)\) satisfying \(-1<a_K(\kappa)<1/3\), the full four-coordinate homogeneous time-step amplification matrix has all eigenvalues strictly inside the complex unit disk for every sufficiently small *positive* \(\varepsilon\). For every fixed pair with \(a_K(\kappa)<-1\) or \(a_K(\kappa)>1/3\), that matrix has an eigenvalue of modulus strictly greater than one for every sufficiently small positive \(\varepsilon\).

Consequently the sharp open stability ranges in this weak-flow limit are
\[
 \begin{aligned}
 K\text{ odd}:&\quad 3\kappa^K<(2+\kappa)^{K-1},\\
 K\text{ even}:&\quad \kappa^K<(2+\kappa)^{K-1}.
 \end{aligned}
\]
The equality cases are **not** classified by this result. For \(K=2\), the small-positive-flow stability boundary is \(\kappa=2\), versus \(\kappa=1\) from the published sufficient stability condition in [1]. At \(K=2,\kappa=3/2\), the limiting parasitic pair is
\[
 \zeta_\pm=\frac{9\pm3\sqrt5\,\mathrm{i}}{14},\qquad |\zeta_\pm|=\frac3{\sqrt{14}}<1,
\]
although the published sufficient inequality is violated. The physical root has the universal expansion
\[
 \zeta_{\mathrm{phys}}(\varepsilon)=1-\frac{3\varepsilon}{2(1+\kappa)}+O(\varepsilon^2).
\]

## Assumptions and scope

The two-variable system is
\[
 u-\sqrt\kappa\,p=0,\qquad \sqrt\kappa\,\dot u+\dot p+b p=0.
\]
Thus the continuum system is dissipative, with \(\dot p=-b p/(1+\kappa)\). The stiffness and storage matrices are both the positive scalar \(1\); the flow matrix is the strictly positive scalar \(b\), and the coupling operator is \(\sqrt\kappa\). The initial discrete state is any \((u_n,u_{n+1},p_n,p_{n+1})\in\mathbb R^4\), for the purpose of spectral stability of the full recurrence. Consistent differential-algebraic starts form a subset, but an unconditional error-stability claim must also control perturbed states produced later by splitting. The theorem is for fixed \(K\) and fixed \(\kappa\) as \(\varepsilon\downarrow0\), not a uniform-in-\(\kappa\) or PDE assertion.

The scheme relaxes its first \(K-1\) inner pressure updates with the paper's \(\gamma=2/(2+w)\), where
\[
 w=\frac\kappa{1+\varepsilon},\qquad \gamma=\frac2{2+w},\qquad q=\left(-\frac{w}{2+w}\right)^{K-1},
\]
and leaves the last pressure update unrelaxed. The slight dependence of \(w\) on the time step is retained throughout; it is not replaced prematurely by \(\kappa\).

## Proof

**Step 1: exact inner recurrence.** Scale displacement by \(z_n=\sqrt\kappa\,u_n\). For given two preceding time levels, put
\[
 R_n=\frac{4(z_{n+1}+p_{n+1})-(z_n+p_n)}{3(1+\varepsilon)}
\]
and initialize \(p^{(0)}=2p_{n+1}-p_n\). A split solve gives \(\widehat z^{(k+1)}=\kappa p^{(k)}\), \(\widehat p^{(k+1)}=R_n-w p^{(k)}\). During the first \(K-1\) iterations, \(p^{(k+1)}=\gamma\widehat p^{(k+1)}+(1-\gamma)p^{(k)}\); hence the relaxed multiplier is \(1-\gamma(1+w)=-w/(2+w)\). Summation of the geometric progression yields
\[
 p^{(K-1)}=q(2p_{n+1}-p_n)+\frac{1-q}{1+w}R_n.
\]
In the final, unrelaxed solve, \(z_{n+2}=\kappa p^{(K-1)}\) and \(p_{n+2}=R_n-wp^{(K-1)}\). These equations define the full real \(4\times4\) amplification matrix on \((z_n,z_{n+1},p_n,p_{n+1})\).

**Step 2: characteristic polynomial.** Let \(\zeta\) be a spectral parameter and set
\[
 H=\frac{4\zeta-1}{3(1+\varepsilon)},\qquad v=2\zeta-1.
\]
Under the mode \((z_n,p_n)=(Z,P)\zeta^n\), the last inner pressure value is \(qvP+(1-q)H(Z+P)/(1+w)\). The two final-update equations are
\[
 \zeta^2 Z=\kappa\left(qvP+\frac{1-q}{1+w}H(Z+P)\right),
\]
\[
 \zeta^2P=H(Z+P)-w\left(qvP+\frac{1-q}{1+w}H(Z+P)\right).
\]
The exact determinant, including its leading monic term, is
\[
 \boxed{P_\varepsilon(\zeta)=\zeta^4+\zeta^2\left[wqv-\frac{1+\kappa-\varepsilon wq}{1+w}H\right]-\kappa qvH.}
\]
In particular \(q\) is the actual time-step-dependent quantity above, and is not a free constant when differentiating with respect to \(\varepsilon\).

**Step 3: factorization at vanishing flow.** At \(\varepsilon=0\), \(w=\kappa\) and \(\kappa q=a_K(\kappa)\). Direct multiplication factors the quartic as
\[
 P_0(\zeta)=(\zeta-1)(\zeta-\tfrac13)(\zeta^2+2a_K\zeta-a_K).
\]
For a real quadratic \(\zeta^2+b\zeta+c\), the strict Schur/Jury conditions are \(|c|<1\), \(1+b+c>0\), and \(1-b+c>0\). Here they become \(|a_K|<1\), \(1+a_K>0\), \(1-3a_K>0\), together equivalent to \(-1<a_K<1/3\). Thus, in the strict admissible regime, all roots other than the physical root \(1\) are inside the unit disk. Outside its closure, at least one quadratic root lies strictly outside the unit disk.

**Step 4: movement of the physical root.** The exact quartic satisfies
\[
 P_\varepsilon(1)=\frac{\varepsilon(1+wq)}{1+\varepsilon+\kappa},\qquad
 \left.\frac{\partial P_0}{\partial\zeta}\right|_{\zeta=1}=\frac23(1+a_K).
\]
For \(a_K\neq-1\), the implicit-function theorem gives the real analytic branch leaving \(1\) with derivative
\[
 \zeta_{\mathrm{phys}}'(0)=-\frac{3}{2(1+\kappa)}.
\]
In the strict stable region this branch moves below \(1\), and all other eigenvalues stay inside by continuity. Where a parasitic eigenvalue is strictly outside at zero flow, continuity preserves instability for sufficiently small positive flow. These conclusions prove the two asserted open-region implications. The critical equalities, where roots can lie on the unit circle or collide, require a separate higher-order perturbation and are not claimed.

**Step 5: parity and the illustrative threshold.** The magnitude \(\kappa^K/(2+\kappa)^{K-1}\) is strictly increasing in \(\kappa>0\), since its logarithmic derivative is \([\kappa+2K]/[\kappa(\kappa+2)]>0\). Its sign is positive for odd \(K\) and negative for even \(K\). The Schur inequalities therefore give the stated parity-dependent thresholds, uniquely defining the positive coupling frontier for each \(K\). For \(K=2\), \(a_2=-\kappa^2/(2+\kappa)\), so \(a_2>-1\) is exactly \(\kappa<2\). The formula at \(\kappa=3/2\) follows by solving the quadratic factor and does not rely on floating-point experiments.

## Verification

The reproducible `verify.py` supplied alongside this result constructs the full four-state amplification matrix directly from the \(K\) split solves, and separately evaluates the proposed characteristic polynomial. It verifies their agreement on a multiparameter grid; checks exact symbolic factorization and the root derivative; and evaluates roots on both sides of the strict parity boundaries. The recorded program run passed 469 algebraic/numerical assertions (NumPy and SymPy). These finite computations corroborate algebraic reconstruction but do not replace the all-parameter proof above. The symbolic identities in Steps 2--4 and the strict Schur inequalities establish the infinite families.

## Relationship to prior work

Altmann and Deiml [1] introduce precisely this second-order fixed-sweep splitting and prove the sufficient iteration constraint \(3\omega^K<(2+\omega)^{K-1}\) for general positive definite spatial systems. They additionally **observe**, in Section 5.1 and Figure 5.1, that even \(K\) often performs substantially better in stability experiments. Neither the observed parity nor that sufficient bound is claimed to be new here. The present theorem gives a necessary-and-sufficient **open small-positive-flow spectral boundary on the scalar mode** and determines the factor-of-three parity change in its algebraic threshold, including a provably stable region outside [1]'s sufficient condition for even \(K\).

The earlier work [2] gives a fixed-sweep method for **first-order Euler integration**, with a different update polynomial and a coupling inequality numerically coinciding with the even-\(K\) scalar boundary. That first-order theorem does not entail the claimed BDF2 spectral factorization or necessity. The higher-order approach [3] uses a stabilization-based fixed-stress iteration and a tolerance-based termination criterion rather than the particular fixed-\(K\), last-sweep-undamped recurrence analyzed here. The one-pass BDF2 result [4] covers the \(K=1\) special case, not the even-\(K\) frontier. The algebraic Schur/Jury criterion itself is classical, not new.

## Limitations

This is a scalar-mode, homogeneous, exact-arithmetic result about linear spectral stability for small positive \(\tau b\) at fixed \(K,\kappa\). The zero-flow limit is used only as an auxiliary polynomial; the asserted stable systems themselves retain \(b>0\) and \(\tau>0\). Equality cases are left unresolved. The source's broader PDE error norms, second-order global convergence theory, noncommuting multidimensional matrices, nonlinear permeability, source forcing, and finite-precision or preconditioning effects are not established here. This mathematical comparison with primary literature is not a claim of exhaustive priority or an independently certified result.

## References

[1] R. Altmann and M. Deiml, *A second-order iterative time integration scheme for linear poroelasticity*, arXiv:2403.12699, first submitted 2024-03-19, Sections 3.6, 4, and 5.1. https://arxiv.org/abs/2403.12699

[2] R. Altmann and M. Deiml, *A novel iterative time integration scheme for linear poroelasticity*, arXiv:2304.12224 (2023), Sections 3--4. https://arxiv.org/abs/2304.12224

[3] R. Altmann, A. Mujahid, and B. Unger, *Higher-order iterative decoupling for poroelasticity*, arXiv:2311.14400 (2023), Sections 2--4. https://arxiv.org/abs/2311.14400

[4] R. Altmann, R. Maier, and B. Unger, *Semi-explicit integration of second order for weakly coupled poroelasticity*, arXiv:2203.16664 (2022). https://arxiv.org/abs/2203.16664
