# Exact residual-scale slowdown in the accelerated double-step-length method

## Finding
Consider the 2026 accelerated double-step-length method (ADSM) on the scalar linear equation
\[
F_a(s)=a s,\qquad a>0,
\]
with a nonzero initial point and the source parameters \(\eta\in(1,2)\), \(r\in(0,1)\), \(\omega_1,\omega_2>0\), and a positive summable sequence \(\{\chi_k\}\). The source initializes \(\delta_0=1\), uses
\[
q_k=-\eta\delta_k^{-1}F_a(s_k),
\]
sets the second step length to \(\alpha_k/\eta\), and updates
\[
s_{k+1}=s_k+\left(\alpha_k+\frac{\alpha_k}{\eta}\right)q_k.
\]
Whenever the first accepted step is nonterminal, its secant update identifies the scalar Jacobian exactly:
\[
\delta_1=a.
\]
The same identity then holds after every subsequent nonterminal step. Thus, from the second iteration onward,
\[
q_k=-\eta s_k,
\qquad
s_{k+1}=\bigl(1-(\eta+1)\alpha_k\bigr)s_k.
\]

For a calibrated nonterminal iterate, define
\[
B=\eta+1,
\qquad
A(a)=B^2\left(\frac12+\frac{\omega_1}{\eta^2}+\frac{\omega_2}{a^2}\right).
\]
The source line-search test is then equivalent, with no approximation, to
\[
A(a)\alpha^2-B\alpha-\frac{\chi_k}{2}\le0.
\]
Therefore a positive trial is accepted exactly when
\[
0<\alpha\le \alpha_{\max,k}(a)
:=
\frac{B+\sqrt{B^2+2A(a)\chi_k}}{2A(a)}.
\]
Because Algorithm 1 tries \(1,r,r^2,\ldots\), its accepted index is exactly
\[
m_k(a)=\min\left\{m\in\mathbb N_0:r^m\le \alpha_{\max,k}(a)\right\}.
\]
Since \(\sum_k\chi_k<\infty\) and \(\chi_k>0\), one has \(\chi_k\to0\), so
\[
\alpha_{\max,k}(a)\longrightarrow
\bar\alpha(a)
=
\frac{1}{B\left(\frac12+\frac{\omega_1}{\eta^2}+\frac{\omega_2}{a^2}\right)}.
\]
The discrete backtracking index consequently stabilizes after finitely many iterations at
\[
m_*(a)=\min\left\{m\in\mathbb N_0:r^m\le\bar\alpha(a)\right\},
\]
including the boundary case in which \(\bar\alpha(a)\) itself is a grid point. The resulting exact eventual one-step factor is
\[
\rho(a)=\left|1-Br^{m_*(a)}\right|<1.
\]
If this factor is zero, the very next calibrated step reaches the root exactly; otherwise it is the eventual Q-factor of the nonterminal scalar iteration.

The decisive effect is residual scaling. For sufficiently small \(a\), \(m_*(a)>0\), and geometric minimality gives
\[
r\bar\alpha(a)<r^{m_*(a)}\le\bar\alpha(a).
\]
Moreover
\[
B\bar\alpha(a)
=
\frac{a^2}{\omega_2+a^2\left(\frac12+\frac{\omega_1}{\eta^2}\right)}.
\]
Hence, for all sufficiently small \(a\),
\[
1-B\bar\alpha(a)
\le \rho(a)
<1-rB\bar\alpha(a),
\]
and therefore
\[
1-\rho(a)=\Theta(a^2).
\]
Equivalently,
\[
m_*(a)=\frac{2\log(1/a)}{|\log r|}+O(1)
\qquad(a\downarrow0).
\]
Thus any fixed reduction of \(|s_k|\) requires \(\Theta(a^{-2})\) accepted calibrated steps as \(a\downarrow0\), while the eventual number of trial evaluations per accepted step grows like \(\Theta(\log(1/a))\).

This is a residual-scale obstruction rather than a conditioning obstruction: every scalar Jacobian \([a]\) has condition number one, and after one nonterminal step the method already has the exact slope \(\delta_k=a\). The slowdown is instead imposed by the source term
\[
-\omega_2\left\|\left(\alpha+\frac{\alpha}{\eta}\right)q_k\right\|^2,
\]
whose strength relative to the merit-function scale grows like \(a^{-2}\). If that term were absent, the limiting scalar acceptance threshold would no longer contain \(a\); the finding does not propose removing it, because it is used in the source convergence analysis.

## Assumptions and scope
The claim concerns the source ADSM exactly as stated in its Algorithms 1 and 2, specialized to the one-dimensional linear family \(F_a(s)=a s\), \(a>0\). The formulas apply to nonterminal iterations exactly as Algorithm 2 executes them. For the slowdown family, take \(s_0(a)=1/a\), so \(|F_a(s_0(a))|=1\). Hence any fixed residual tolerance below a prescribed fixed relative target does not stop the run before that target is reached. For sufficiently small \(a\), the first accepted trial also cannot accidentally solve the equation because \(\alpha_0\le1\) and \((\eta+1)a<1\).

The line-search sequence is assumed positive and summable exactly as in the source, so \(\chi_k\to0\). No monotonicity beyond positivity and convergence to zero is required. The result concerns accepted-step and backtracking complexity of this scalar specialization; it does not contradict the source global-convergence theorem or claim a worst-case complexity bound for general nonlinear systems.

## Proof
Let
\[
u_k=s_{k+1}-s_k
=
\left(\alpha_k+\frac{\alpha_k}{\eta}\right)q_k
\]
and
\[
v_k=F_a(s_{k+1})-F_a(s_k)=a u_k.
\]
For a nonterminal accepted step, \(u_k\ne0\). Substitution into the source acceleration update gives
\[
\delta_{k+1}
=
\frac{v_k^2}{\left(\alpha_k+\frac{\alpha_k}{\eta}\right)v_kq_k}
=
\frac{a^2u_k^2}{a u_k^2}
=a.
\]
Thus \(\delta_1=a\) after the first nonterminal step and every later nonterminal update repeats the same value.

Once \(\delta_k=a\),
\[
q_k=-\eta\delta_k^{-1}a s_k=-\eta s_k,
\]
and therefore, with \(B=\eta+1\),
\[
s_k+\left(\alpha+\frac{\alpha}{\eta}\right)q_k
=(1-B\alpha)s_k.
\]
For the source merit function \(h(s)=\tfrac12|F_a(s)|^2\), the left side of the line-search inequality becomes
\[
\frac12a^2s_k^2\bigl((1-B\alpha)^2-1\bigr)
=
a^2s_k^2\left(-B\alpha+\frac{B^2\alpha^2}{2}\right).
\]
The two quadratic penalty terms are
\[
-\omega_1\left\|\left(\alpha+\frac{\alpha}{\eta}\right)F_a(s_k)\right\|^2
=
-\omega_1\frac{B^2}{\eta^2}\alpha^2a^2s_k^2
\]
and
\[
-\omega_2\left\|\left(\alpha+\frac{\alpha}{\eta}\right)q_k\right\|^2
=
-\omega_2B^2\alpha^2s_k^2.
\]
The relaxation term is \(\chi_k a^2s_k^2/2\). Dividing by the positive quantity \(a^2s_k^2\) and collecting terms yields exactly
\[
B^2\left(\frac12+\frac{\omega_1}{\eta^2}+\frac{\omega_2}{a^2}\right)\alpha^2
-B\alpha-rac{\chi_k}{2}\le0.
\]
Because the constant term is negative and the quadratic coefficient is positive, the admissible positive interval ends at the displayed positive root \(\alpha_{\max,k}(a)\). This proves the exact backtracking-index formula.

Positivity and summability of \(\chi_k\) imply \(\chi_k\to0\), hence \(\alpha_{\max,k}(a)\to\bar\alpha(a)\). Let \(m_*(a)\) be the least grid index satisfying \(r^{m_*(a)}\le\bar\alpha(a)\). If \(m_*(a)=0\), then \(1\le\bar\alpha(a)<\alpha_{\max,k}(a)\), so index zero is always accepted. If \(m_*(a)>0\), then \(r^{m_*(a)-1}>\bar\alpha(a)\), while \(r^{m_*(a)}\le\bar\alpha(a)<\alpha_{\max,k}(a)\). Convergence of \(\alpha_{\max,k}(a)\) makes \(r^{m_*(a)-1}\) eventually fail while \(r^{m_*(a)}\) continues to pass, proving finite stabilization even when \(\bar\alpha(a)=r^{m_*(a)}\).

Since
\[
B\bar\alpha(a)
=
\frac{1}{\frac12+\frac{\omega_1}{\eta^2}+\frac{\omega_2}{a^2}}<2,
\]
the stabilized multiplier has modulus below one. For small \(a\), it is positive, so \(\rho(a)=1-Br^{m_*(a)}\). Minimality of \(m_*(a)\) gives the two-sided bound above. Finally,
\[
B\bar\alpha(a)
=
\frac{a^2}{\omega_2+a^2\left(\frac12+\frac{\omega_1}{\eta^2}\right)}
\sim\frac{a^2}{\omega_2},
\]
which proves \(1-\rho(a)=\Theta(a^2)\). Taking logarithms of \(r^{m_*(a)}\asymp a^2\) gives the backtracking-index asymptotic. For a fixed target reduction \(0<\varepsilon<1\), the accepted-step count is asymptotic in order to \(\log(1/\varepsilon)/(1-\rho(a))\), hence \(\Theta(a^{-2})\).

## Verification
The bundled script `artifacts/verify_adsm_scalar_scale.py` independently evaluates the source line-search inequality and the derived quadratic acceptance test over randomized scalar states and parameters, checks exact one-step secant calibration, verifies eventual grid-index stabilization for a positive summable choice of \(\chi_k\), and checks the predicted small-scale \(a^2\) contraction and logarithmic backtracking laws.

These computations are consistency checks. The quantified result follows from the exact algebra above, not from finite experiments.

## Relationship to prior work
The primary 2026 ADSM paper introduces the single accelerated direction, fixes the second step length to \(\alpha_k/\eta\), derives the secant-style scalar acceleration update, and combines them with the two-penalty inexact line search. It proves global convergence under its assumptions but does not derive the scalar acceptance polynomial, the eventual geometric-grid index, or the residual-rescaling rate law above.

The 2020 inexact double-step-length method is the closest ancestor of the secant update: it already uses a single direction, two independently selected step lengths, a scalar Jacobian approximation, and an inexact line search. The newer ADSM changes the iteration by imposing the specific relation between its two lengths and by inserting the correction factor into the single direction. The exact scale law here uses that new coupling and therefore is not a restatement of the older method's convergence result.

The 2025 Picard-Mann double-step method is also close in objects and motivation, but its update retains a different combined-step construction and acceleration formula. The April 2026 constrained monotone double-step method uses a Broyden/Frobenius acceleration and a different simultaneous two-parameter line search. Neither inspected method states or implies the exact ADSM scalar threshold and its \(\Theta(a^{-2})\) residual-scale slowdown.

## Limitations
The result is intentionally narrow: it is an exact diagnostic for a scalar linear family. It does not assert divergence, invalidate the source global-convergence theorem, or show that the same rate law is worst-case in higher dimensions. For the small-scale slowdown statement the explicit initialization \(s_0(a)=1/a\) keeps the starting residual fixed at one, so a fixed source residual tolerance does not terminate the run before any prescribed fixed relative reduction that remains above that tolerance.

The 2020 predecessor was available through its abstract and through explicit formulas reproduced and discussed in the later full-text papers; a complete publisher-hosted copy was not available in the inspected sources. This leaves a residual bibliographic risk that an uninspected passage contains a related scalar calculation, although targeted searches found no such statement and the newer fixed step-length relation is absent from the older method description.

## References
1. A. S. Halilu et al., *An accelerated double-step-length iterative method for nonlinear systems of equations with applications to motion control*, Open Journal of Mathematical Sciences 10 (2026), 755–775, DOI:10.30538/oms2026.0315.
2. A. S. Halilu, M. Y. Waziri, and Y. B. Musa, *Inexact Double Step Length Method For Solving Systems Of Nonlinear Equations*, Statistics, Optimization & Information Computing 8 (2020), 165–174, DOI:10.19139/soic-2310-5070-532.
3. A. S. Halilu et al., *Modified iterative double step length model for solving nonlinear systems with application to motion control*, Scientific Reports 15 (2025), 40764, DOI:10.1038/s41598-025-24537-z.
4. M. Abdullahi et al., *Accelerated double step-length method for solving monotone nonlinear equations with convex-constraint and application*, AIMS Mathematics 11 (2026), 10908–10935, DOI:10.3934/math.2026448.
