# Exact residual-scale slowdown in the accelerated double-step-length method

## Finding

Consider Algorithms 1 and 2 of Halilu et al. (2026) [1] in exact arithmetic on the scalar equation \(F_a(s)=as=0\), where \(a>0\). Fix the source parameters \(1<\eta<2\), \(0<r<1\), \(\omega_1,\omega_2>0\), and a positive summable sequence \((\chi_k)_{k\ge0}\). Set \(B=\eta+1\). The method starts at \(\delta_0=1\). Each executed step from a nonzero iterate yields \(\delta_{k+1}=a\). In particular, on every executed iteration after the first, the direction is \(q_k=-\eta s_k\) and the update is \(s_{k+1}=(1-B\alpha_k)s_k\).

For these calibrated iterations define
\[
A(a)=B^2\left(\tfrac12+\frac{\omega_1}{\eta^2}+\frac{\omega_2}{a^2}\right),\qquad
L_k(a)=\frac{B+\sqrt{B^2+2A(a)\chi_k}}{2A(a)}.
\]
Exactly the positive trial lengths \(\alpha\le L_k(a)\) satisfy the acceptance inequality. Algorithm 1 tests \(1,r,r^2,\ldots\), so it accepts \(\alpha_k=r^{m_k(a)}\) with \(m_k(a)=\min\{m\in\mathbb N_0:r^m\le L_k(a)\}\).

For each fixed \(a\), let \(\bar\alpha=B/A(a)\) and \(m_*=\min\{m\in\mathbb N_0:r^m\le\bar\alpha\}\). For all sufficiently late calibrated indices, **if reached**, the accepted index is \(m_*\), including when \(\bar\alpha\) is a grid point. The absolute one-step factor at those indices is \(\rho=|1-Br^{m_*}|<1\); if the factor is zero, that step hits the root. As \(a\downarrow0\), with all other parameters fixed,
\[
1-\rho=\Theta(a^2),\qquad m_*=\frac{2\log(1/a)}{|\log r|}+O(1).
\]
At such stabilized iterations there are exactly \(m_*+1\) trial evaluations per acceptance. An actual run with a positive residual tolerance need not reach a stabilized index.

For the finite-target result take \(s_0=1/a\), giving \(|F_a(s_0)|=1\). For every fixed target \(\tau\) with \(10^{-5}<\tau<1\), the first attainment of \(|F_a(s_k)|\le\tau\) under the source stopping rule requires \(\Theta(a^{-2})\) accepted calibrated steps as \(a\downarrow0\). This assertion does not require grid-index stabilization before reaching the target. It also holds with any fixed residual stopping tolerance smaller than \(\tau\) if that tolerance is used instead.

## Proof

The source direction is \(q_k=-\eta\delta_k^{-1}F_a(s_k)\) and the actual displacement is \(u_k=(\alpha_k+\alpha_k/\eta)q_k\). Write \(v_k=F_a(s_k+u_k)-F_a(s_k)=a u_k\). At any executed step \(s_k\ne0\), the trial length is positive and \(u_k\ne0\). The source update (20) gives
\[
\delta_{k+1}=\frac{v_k^2}{(\alpha_k+\alpha_k/\eta)v_kq_k}=\frac{a^2u_k^2}{a u_k^2}=a.
\]
This verifies that the update is defined and strictly positive, starting from \(\delta_0=1\). In particular, on every calibrated trial its tentative new iterate is \((1-B\alpha)s_k\).

For the merit \(h(s)=|F_a(s)|^2/2\), the left-hand difference in test (21) on a calibrated trial is \(a^2s_k^2(-B\alpha+B^2\alpha^2/2)\). The two right-hand penalties are \(-\omega_1(B/\eta)^2\alpha^2a^2s_k^2\) and \(-\omega_2B^2\alpha^2s_k^2\); the relaxation term is \(\chi_k a^2s_k^2/2\). Divide by \(a^2s_k^2>0\) to obtain
\[
A(a)\alpha^2-B\alpha-\frac{\chi_k}{2}\le 0.
\]
The quadratic has positive leading coefficient and opposite-sign roots, so the positive acceptance interval ends at \(L_k(a)\). This gives the index formula. The initial line search also terminates: its trial displacement and merit change are continuous at \(\alpha=0\), where the relaxation makes acceptance strict for \(s_0\ne0\).

Positivity and summability give \(L_k(a)>\bar\alpha\) and \(L_k(a)\to\bar\alpha\) for fixed \(a\), without requiring monotonicity. If \(m_*=0\), the unit trial always passes. Otherwise \(r^{m_*-1}>\bar\alpha\) and eventually exceeds \(L_k(a)\), while \(r^{m_*}\le\bar\alpha\) continues to pass. This proves stabilization for the indices reached. Also
\[
0<B r^{m_*}\le B\bar\alpha=\frac{a^2}{\omega_2+a^2(\tfrac12+\omega_1/\eta^2)}<2,
\]
so \(\rho<1\). For small \(a\), \(m_*>0\) and \(r\bar\alpha<r^{m_*}\le\bar\alpha=\Theta(a^2)\). The stabilized multiplier then has positive sign. It follows that \(1-\rho=B r^{m_*}=\Theta(a^2)\) and, by taking logarithms, that \(m_*\) has the stated leading log term.

**Uniform control up to a fixed target.** The first accepted uncalibrated step from \(s_0=1/a\) gives \(|F_a(s_1)|=1-Ba\alpha_0\) for small \(a\), since \(\alpha_0\le1\). This exceeds any fixed \(\tau<1\) when \(a\) is small enough, and changes the log residual by \(O(a)\). Put \(S=\sum_{k\ge0}\chi_k<\infty\). The inequality \(\sqrt{x+y}\le\sqrt{x}+\sqrt{y}\) gives
\[
L_k(a)\le B/A(a)+\sqrt{\chi_k/(2A(a))}\le c_1a^2+c_2a\sqrt{\chi_k},
\]
with constants independent of \(k,a\), since \(A(a)\ge B^2\omega_2/a^2\). Thus \(B\alpha_k\le 1/2\) uniformly in the calibrated iterations for sufficiently small \(a\). Conversely every accepted calibrated length is at least \(r\bar\alpha\ge c_3a^2\) for small \(a\): if the unit trial fails, the immediately larger grid point fails and the accepted one is greater than \(rL_k(a)\); if the unit trial passes, the bound follows from \(\bar\alpha<1\).

After \(N\) calibrated steps, the log reduction from residual one is \(-\log(1-Ba\alpha_0)+\sum_{k=1}^N[-\log(1-B\alpha_k)]\). Using \(x\le -\log(1-x)\le 2x\) for \(0\le x\le 1/2\) and Cauchy–Schwarz gives the two-sided bound
\[
c_4 a^2 N\ \le\ -\log |F_a(s_{N+1})|\ \le\ c_5 a+c_6 a^2 N+c_7 a\sqrt{NS},
\]
with strictly positive constants independent of \(a,N\). The upper bound is smaller than \(\log(1/\tau)\) for sufficiently small \(a\) whenever \(N\le \delta a^{-2}\) for a sufficiently small fixed \(\delta>0\). The lower bound exceeds \(\log(1/\tau)\) by \(N=\lceil C a^{-2}\rceil\) for large enough fixed \(C\), if the run has not already met the target. It cannot stop beforehand, since stopping requires a smaller residual than \(\tau\). This proves the order uniformly in the possibly long pre-stabilization part of the run.

## Verification and scope

The closed formulas and the uniform log bounds prove the statements. The companion `artifacts/verify_adsm_scalar_scale.py` can be run with Python 3. It contains bounded numerical cross-checks of scalar calibration, the quadratic test, and the stabilized grid law; it does not prove the finite-target complexity or check every positive summable sequence. The supplied `artifacts/verification_output.txt` records `VERIFY_OK`.

The asymptotic estimates fix \(\eta,r,\omega_1,\omega_2,(\chi_k)\), and the target independently of \(a\). The Jacobian \([a]\) has norm condition number one. The slowing penalty involves squared state displacement rather than squared residual, so dividing by the merit scale introduces the factor \(a^{-2}\) even when the direction has the exact Jacobian. If \(\omega_2\) were zero, the limiting calibrated acceptance threshold would not depend on \(a\). No modification to the method, claim of divergence, or multidimensional worst-case bound is asserted.

## Relationship to prior work

The ADSM paper [1] gives Algorithms 1 and 2 and a global convergence analysis, not the exact scalar-grid or uniform finite-target bounds above in the inspected passages. The older inexact double-step-length method [2], as reproduced in [3], already uses a scalar secant update, which recovers the slope on a nonzero scalar linear step. The two-penalty inequality of MIDSL [3, Lemma 3.7, (36)] already compares the state displacement to residual-sized terms and therefore exhibits the same potential scale obstruction. The penalty mechanism and scalar secant recovery are not asserted as unique to ADSM. The claims here concern the specified step coupling and single geometric grid of ADSM, their exact eventual multiplier, and matching accepted-step bounds through a fixed target under that algorithm's stopping rule. The detailed older MIDSL grid was not established by the inspected text extraction, and full-text comparison with [2] and with the constrained monotone method [4] was limited. No global novelty claim is made.

## References

1. A. S. Halilu et al., *An accelerated double-step-length iterative method for nonlinear systems of equations with applications to motion control*, Open Journal of Mathematical Sciences 10 (2026), 755–775, DOI: 10.30538/oms2026.0315, especially (14), (20)–(22), and Algorithms 1 and 2.
2. A. S. Halilu, M. Y. Waziri, and Y. B. Musa, *Inexact Double Step Length Method for Solving Systems of Nonlinear Equations*, Statistics, Optimization & Information Computing 8 (2020), 165–174, DOI: 10.19139/soic-2310-5070-532.
3. A. S. Halilu et al., *Modified iterative double step length model for solving nonlinear systems with application to motion control*, Scientific Reports 15 (2025), 40764, DOI: 10.1038/s41598-025-24537-z.
4. M. Abdullahi et al., *Accelerated double step-length method for solving monotone nonlinear equations with convex-constraint and application*, AIMS Mathematics 11 (2026), 10908–10935, DOI: 10.3934/math.2026448.
