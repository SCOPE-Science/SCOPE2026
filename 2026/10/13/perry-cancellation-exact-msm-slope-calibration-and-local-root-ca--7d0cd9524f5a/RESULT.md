# Perry cancellation, exact MSM slope calibration, and local root capture in scalar ASPCGP

## Finding
For the scalar linear equation
\[
E(x)=ax,\qquad a>0,
\]
specialize the 2026 ASPCGP algorithm to the source-admissible no-inertia choice \(\varphi=0\), so \(y_k=x_k\). Let \(\gamma\in(0,2)\) be the relaxed projection factor, \(\tau_k\) the accepted line-search step, \(\zeta_k=1+\tau_{k-1}-\tau_{k-1}^2\) for \(k\ge1\), and \(\Gamma_k\) the accelerated multiple-step-size spectral parameter.

For every nonterminal \(k\ge1\), the source direction
\[
d_k=-\theta_kE(y_k)+\beta_ks_{k-1},\qquad
\theta_k=\frac{\zeta_k}{\Gamma_k}
+\beta_k\frac{E(y_k)s_{k-1}}{E(y_k)^2}
\]
collapses exactly to
\[
d_k=-\frac{\zeta_k}{\Gamma_k}E(y_k).
\]
Thus the Perry contribution cancels independently of the particular admissible \(\beta_k\).

The scalar relaxed projection also satisfies
\[
x_{k+1}=y_k+\gamma\tau_kd_k.
\]
Hence \(s_k=\gamma\tau_kd_k\) and \(p_k=as_k\). Substitution into the source raw MSM update
\[
\widehat\Gamma_{k+1}
=
-\frac{\Gamma_k\lVert p_k\rVert^2}
{\tau_k\zeta_k\,p_kE(y_k)}
\]
gives the exact calibration identity
\[
\boxed{\widehat\Gamma_{k+1}=\gamma a},\qquad k\ge1.
\]
Therefore, if
\[
\Gamma_{\min}<\gamma a<\Gamma_{\max},
\]
the source clipping/reset rule retains this value. The special \(k=0\) direction need not calibrate, but the next nonterminal Perry iteration does; consequently \(\Gamma_2=\gamma a\), and all later nonterminal raw updates reproduce the same value.

After this lock,
\[
d_k=-\frac{\zeta_k}{\gamma}y_k,\qquad
z_k=y_k\left(1-\frac{\tau_k\zeta_k}{\gamma}\right),\qquad
x_{k+1}=(1-\tau_k\zeta_k)y_k.
\]
The linear slope has disappeared completely from the state map.

There is an explicit local finite-capture mechanism. Assume \(\varsigma=1\) and \(\gamma>5/4\). Because \(0<\tau_{k-1}\le1\),
\[
1\le\zeta_k\le\frac54.
\]
For the first line-search trial \(\tau=1\), the source acceptance inequality is guaranteed whenever
\[
|y_k|\le\frac{\gamma}{\sigma\nu\zeta_k}.
\]
Thus the uniform basin
\[
\boxed{|y_k|\le\frac{4\gamma}{5\sigma\nu}}
\]
forces acceptance of the unit step. The new state is
\[
y_{k+1}=(1-\zeta_k)y_k,
\]
so \(|y_{k+1}|\le |y_k|/4\), while the next multiplier becomes
\[
\zeta_{k+1}=1+1-1=1.
\]
The following unit step is again accepted and maps
\[
y_{k+2}=(1-1)y_{k+1}=0.
\]
Thus a calibrated iterate inside the displayed basin reaches the exact scalar root in at most two projection updates, unless the positive stopping tolerance terminates earlier.

## Assumptions and scope
The theorem concerns \(E(x)=ax\) with \(a>0\), zero inertia, and nonterminal iterations for which the source quotients are defined. Exact locking of the stored spectral value requires strict clipping interiority
\[
\Gamma_{\min}<\gamma a<\Gamma_{\max}.
\]
The finite-capture statement additionally assumes \(\varsigma=1\), \(\gamma>5/4\), and entry into the displayed sufficient basin. The basin is not claimed optimal. A positive practical stopping tolerance may terminate before an exact zero iterate is explicitly formed.

No multidimensional cancellation or global finite-termination claim is made.

## Proof
For \(k\ge1\),
\[
\begin{aligned}
d_k
&=-\left(\frac{\zeta_k}{\Gamma_k}
+\beta_k\frac{E(y_k)s_{k-1}}{E(y_k)^2}\right)E(y_k)
+\beta_ks_{k-1}\\
&=-\frac{\zeta_k}{\Gamma_k}E(y_k).
\end{aligned}
\]
For the scalar projection,
\[
\xi_kE(z_k)
=\frac{E(z_k)(y_k-z_k)}{E(z_k)^2}E(z_k)
=y_k-z_k=-\tau_kd_k,
\]
so \(x_{k+1}=y_k+\gamma\tau_kd_k\).

Since \(p_k=as_k\),
\[
\widehat\Gamma_{k+1}
=-\Gamma_k\frac{a^2s_k^2}{\tau_k\zeta_k a^2s_ky_k}
=-\Gamma_k\frac{s_k}{\tau_k\zeta_ky_k}.
\]
Using
\[
s_k=\gamma\tau_kd_k
=-\gamma\tau_k\frac{\zeta_ka}{\Gamma_k}y_k
\]
yields \(\widehat\Gamma_{k+1}=\gamma a\).

After lock, \(d_k=-(\zeta_k/\gamma)y_k\). For the unit line-search trial,
\[
z=y\left(1-\frac{\zeta}{\gamma}\right),\qquad
d=-\frac{\zeta}{\gamma}y.
\]
The assumption \(\gamma>5/4\ge\zeta\) makes \(1-\zeta/\gamma>0\). The left side of the source line-search test equals
\[
\frac{a\zeta}{\gamma}
\left(1-\frac{\zeta}{\gamma}\right)y^2.
\]
The right side is
\[
\sigma\frac{\zeta^2}{\gamma^2}y^2
\min\left\{\mu,\nu a|y|
\left(1-\frac{\zeta}{\gamma}\right)\right\}.
\]
Bounding the minimum by its second argument shows that acceptance is guaranteed by
\[
|y|\le\frac{\gamma}{\sigma\nu\zeta}.
\]
Since \(\zeta\le5/4\), the stated uniform basin follows. A unit step sets the next \(\zeta\) to one and contracts by at most one quarter; the next accepted unit step therefore maps the state to zero.

## Verification
The bundled script `artifacts/verify_scalar_aspcgp.py` checks the exact Perry cancellation, scalar projection identity, raw MSM calibration, invariance of the calibrated value, the bound \(1\le\zeta\le5/4\), and a source-style two-step capture example with \(\gamma=7/5\), \(\varsigma=1\), \(\sigma=1\), and \(\nu=3/10\).

The finite sampling in the script is only a consistency check. The quantified statements are established by the algebra above.

## Relationship to prior work
Liu, Wu, Shao, and Wu introduce ASPCGP and prove sufficient descent, trust-region properties, and global convergence. The source defines all formulas used above but does not state the scalar Perry cancellation, the state-independent identity \(\widehat\Gamma=\gamma a\), the curvature-free locked map, or the local two-step capture.

The related 2025 accelerated spectral CG-type projection framework of Liu, Li, Shao, and Zhang uses a different restart construction and adaptive line search. The 2023 modified optimal Perry method of Sabi'u, Shah, Stanimirović, Ivanov, and Waziri optimizes a scaled Perry parameter but does not contain the ASPCGP accelerated MSM update. The accelerated multiple-step-size optimization literature motivating the source's spectral construction treats gradient-descent transformations rather than this Perry-projection coupling.

Targeted searches for the source DOI/title together with scalar linear equations, Perry cancellation, MSM calibration, slope locking, and finite termination found no statement implying the final claim.

## Limitations
The result is one-dimensional and linear. It does not show that Perry coefficients are irrelevant in higher dimensions, nor does it establish a new global rate for nonlinear ASPCGP.

Strict clipping interiority is essential for the stored spectral value to equal the raw calibrated value. The finite-capture basin is sufficient rather than maximal, and practical stopping can occur earlier. An unindexed implementation note or later scalar discussion could reduce originality, but no such coverage was found in the inspected material.

## References
1. P. Liu, X. Wu, H. Shao, and T. Wu, *An Accelerated Spectral Perry-Type Conjugate Gradient Projection Method for Unconstrained Nonlinear Equations with Applications*, CSIAM Transactions on Applied Mathematics 7(4), 776–800, 2026. DOI: 10.4208/csiam-am.SO-2023-0039.
2. P. Liu, L. Li, H. Shao, and B. Zhang, *An Accelerated Spectral CG-Type Projection Method With Restart Strategy for Nonlinear Monotone Equations and Applications in Compressed Sensing*, Numerical Linear Algebra with Applications 32(5), e70035, 2025. DOI: 10.1002/nla.70035.
3. J. Sabi'u, A. Shah, P. S. Stanimirović, B. Ivanov, and M. Y. Waziri, *Modified Optimal Perry Conjugate Gradient Method for Solving System of Monotone Equations with Applications*, Applied Numerical Mathematics 184, 431–445, 2023. DOI: 10.1016/j.apnum.2022.10.016.
4. B. Ivanov, P. S. Stanimirović, G. V. Milovanović, S. Djordjević, and I. Brajević, *Accelerated Multiple Step-Size Methods for Solving Unconstrained Optimization Problems*, Optimization Methods and Software 36(5), 998–1029, 2021. DOI: 10.1080/10556788.2019.1653868.
