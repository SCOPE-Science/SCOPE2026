# Sharp reactive-coupling stability transition for a heterogeneous Stuart–Landau triangle

## Finding

Consider three globally diffusive Stuart–Landau oscillators with real-linearly spaced growth rates \((52,172,292)\), unit real coupling, unit cubic saturation, no nonlinear frequency shift, and imaginary coupling \(\gamma\in\mathbb R\):
\[
\dot z_j=(\beta_j-|z_j|^2)z_j+(1+i\gamma)\sum_{k\ne j}(z_k-z_j),\qquad j=1,2,3.
\]
There is, for **every** \(\gamma\), the zero-mean relative equilibrium
\[
z_j(t)=e^{-3i\gamma t}u_j,\qquad
(u_1,u_2,u_3)=\left(7,\frac{71+i\sqrt{28083}}{14},\frac{-169-i\sqrt{28083}}{14}\right).
\]
Write
\[
F(X)=1359668165778X^3+52078596448637187X^2
+197990312557568849400X-22858579814530283205625.
\]
This polynomial has exactly one positive zero \(X_*\in(112,113)\), and \(\gamma_*:=\sqrt{X_*}\approx10.5894195778911\). The exact **entire reactive-coupling stability diagram** is:

1. For \(|\gamma|>\gamma_*\), the relative equilibrium is exponentially orbitally attracting: its five nontrivial co-rotating eigenvalues have strictly negative real parts.
2. For \(|\gamma|<\gamma_*\), precisely two co-rotating eigenvalues, counted with algebraic multiplicity, lie in the open right half-plane; three have strictly negative real parts.
3. At \(|\gamma|=\gamma_*\), besides the single rotational zero eigenvalue, there is exactly one simple imaginary-conjugate pair; the other three eigenvalues are strictly in the left half-plane. The pair crosses the imaginary axis transversely as \(|\gamma|\) increases through \(\gamma_*\).

For \(\gamma\ne0\) these states are genuine periodic trajectories with period \(2\pi/(3|\gamma|)\). At \(\gamma=0\), they form a rotational family of stationary equilibria. The result is a spectral transition; a nonlinear secondary periodic or quasiperiodic branch is **not** asserted.

## Assumptions and scope

The state space is \(\mathbb C^3\cong\mathbb R^6\). The coefficients, exponents, and topology of the coupling are exactly those displayed above. The model is smooth and \(S^1\)-equivariant. The triple of radial squares is \((49,169,289)\), an arithmetic progression with difference \(120\), so the growth rates satisfy the linear-growth heterogeneity stipulated by the motivating model. The corresponding side lengths \((7,13,17)\) form a nondegenerate triangle; this makes the zero-mean phase configuration possible. No conclusion is drawn for arbitrary growth-rate triples, oscillator populations larger than three, or nonlinear stability at the critical parameter.

## Proof

**Existence.** The displayed vectors satisfy \(u_1+u_2+u_3=0\), and direct arithmetic gives \((|u_1|^2,|u_2|^2,|u_3|^2)=(49,169,289)\). Consequently \(\beta_j-3=|u_j|^2\). Substitution of the rotating ansatz and the identity \(\sum_{k\ne j}(z_k-z_j)=\sum_kz_k-3z_j\) proves the orbit formula exactly.

**Full real linearization.** Put \(w_j(t)=e^{3i\gamma t}z_j(t)\). The vector \(u\) is a fixed point in the rotating frame, which obeys
\[
\dot w_j=(\beta_j-3-|w_j|^2)w_j+(1+i\gamma)\sum_{k=1}^3w_k.
\]
Identify \(u_j\) with the real column \(U_j=(\operatorname{Re}u_j,\operatorname{Im}u_j)^T\), and set \(G_\gamma=\begin{pmatrix}1&-\gamma\\\gamma&1\end{pmatrix}\). Its real \(6\times6\) Jacobian has blocks
\[
J_{jk}=G_\gamma-2\delta_{jk}U_jU_j^T.
\]
The global rotational tangent \((i u_1,i u_2,i u_3)\) is in its kernel. Expanding \(\det(\lambda I_6-J)\), or using the rank-two determinant lemma on the indicated blocks, gives the exact factorization
\[
\det(\lambda I_6-J)=\lambda q_\gamma(\lambda),
\]
\[
\begin{aligned}
q_\gamma(\lambda)={}&\lambda^5+1008\lambda^4
 +(280071+9\gamma^2)\lambda^3\\
 &+(18011228+6084\gamma^2)\lambda^2\\
 &+(-56497371+939645\gamma^2)\lambda
 +28476162(1+\gamma^2).
\end{aligned}
\]
In particular the rotational eigenvalue is simple for all real \(\gamma\), because the constant coefficient of \(q_\gamma\) is strictly positive.

**Exact Hurwitz test.** The leading Hurwitz determinants of the monic quintic, in order, are
\[
\begin{aligned}
\Delta_1={}&1008,\\
\Delta_2={}&4(747\gamma^2+66075085),\\
\Delta_3={}&16(1136187\gamma^4+45986583240\gamma^2+301112958309785),\\
\Delta_4={}&12F(\gamma^2),\\
\Delta_5={}&341713944(1+\gamma^2)F(\gamma^2).
\end{aligned}
\]
The first three determinants and the constant coefficient of the quintic are positive for every real \(\gamma\). Since every nonconstant coefficient of \(F\) is positive and \(F(0)<0\), the function \(F\) is strictly increasing on \([0,\infty)\). Direct integer evaluations give \(F(112)<0<F(113)\), proving that \(X_*\) is uniquely defined. The strict Hurwitz inequalities are all satisfied exactly when \(F(\gamma^2)>0\), proving exponential orbital stability above the threshold.

For \(F(\gamma^2)<0\), the Routh array's first-column signs are \((+,+,+,+,-,+)\): specifically, its first-column entries are \(1,\Delta_1,\Delta_2/\Delta_1,\Delta_3/\Delta_2,\Delta_4/\Delta_3,\Delta_5/\Delta_4\), with the last entry equal to the positive constant term of \(q_\gamma\). There are two sign changes and no vanishing row entries, so precisely two roots lie in the open right half-plane. There are no imaginary roots in this regime, since the necessary fifth-order imaginary-root Hurwitz condition is \(\Delta_4=0\).

At the unique threshold, the Routh auxiliary polynomial is
\[
\frac{\Delta_3}{\Delta_2}\lambda^2+28476162(1+\gamma_*^2).
\]
It yields the imaginary pair
\[
\lambda=\pm i\sqrt{\frac{28476162(1+X_*)\Delta_2}{\Delta_3}},
\]
where \(\Delta_2,\Delta_3\) are evaluated at \(\gamma^2=X_*\); the positive frequency is approximately \(13.1899333206\). Polynomial division leaves a cubic whose coefficients are \(1,a_1,a_2-\nu,a_3-a_1\nu\), where \(a_j\) are the quintic coefficients and \(\nu=28476162(1+X_*)\Delta_2/\Delta_3\). At the threshold \(a_3-a_1\nu=\Delta_3/\Delta_2>0\) and \(a_1(a_2-\nu)-(a_3-a_1\nu)=\Delta_2>0\), so the cubic is Hurwitz by the cubic criterion. Hence the imaginary pair is simple and the other three roots are strictly stable. Since \(F'(X_*)>0\) and \(\gamma_*\ne0\), the Hurwitz determinant vanishes simply with respect to \(|\gamma|\). Near an isolated simple imaginary pair with the remaining spectrum strictly stable, that determinant is a nonzero smooth multiple of the pair's real part. Thus the pair crosses transversely. This completes the spectral classification.

## Verification

The accompanying `verify.py` independently assembles the six real Jacobian blocks from the displayed exact configuration, expands the characteristic polynomial, calculates all five principal Hurwitz determinants, checks arithmetic-progression geometry and the isolating signs for \(X_*\), and evaluates the stable and unstable sign regimes. It uses exact symbolic arithmetic for all identities and inequalities. Its floating-point evaluations serve only to display approximate threshold and imaginary frequency; the theorem follows from exact expressions and monotonicity.

Reproduce with Python 3 and SymPy by running `python verify.py` in the directory containing the extracted source file. The expected completion marker is `EXACT_CERTIFICATE_OK`.

## Relationship to prior work

Zhao and Uchida (2026) establish the zero-order-parameter polygonal relative equilibria for globally coupled Stuart–Landau systems and numerically survey their configuration-dependent transverse stability. In particular, their triangular sector in the plotted parameter window is unstable. That numerical observation does not decide whether a three-active-oscillator polygon can become stable when the reactive coupling varies outside the scanned range. The present result identifies an exact and sharp boundary for a fully heterogeneous three-oscillator family satisfying their linear-growth-rate assumption. The underlying existence of polygonal relative equilibria and stability of individual examples are not claimed as new. Earlier general studies of heterogeneous globally coupled amplitude oscillators and controlled three-oscillator splay states have different hypotheses and do not supply this fixed-family threshold in the evidence examined.

## Limitations

This is a local spectral statement, not a nonlinear Hopf- or torus-bifurcation theorem at the critical parameter. It does not classify the global basins, other attractors, or any population with additional inactive oscillators. The coefficient values are a motivated exact-geometry choice and do not imply a universal parameter formula for all triangles. Historical-priority assessment is limited to the cited literature and database checks; independent review has not been carried out.

## References

1. L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1 (first public 2026-10-06), https://arxiv.org/html/2610.08239.
2. W. S. Lee, E. Ott, and T. M. Antonsen, Jr., *Phase and amplitude dynamics in large systems of coupled oscillators: Growth heterogeneity, nonlinear frequency shifts, and cluster states*, arXiv:1304.3974 (2013), https://arxiv.org/abs/1304.3974.
3. I. Schneider, *Delayed feedback control of three diffusively coupled Stuart-Landau oscillators: a case study in equivariant Hopf bifurcation*, Philosophical Transactions A **371** (2013), 20120472, https://doi.org/10.1098/rsta.2012.0472.
