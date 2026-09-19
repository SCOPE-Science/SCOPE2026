# Exact underdamped rate law for the pure single-loop minimax feedback method

## Result

Zhang and Xu (arXiv:2609.20327v1) recently introduced a fixed-parameter pure single-loop damped extragradient method for smooth strongly convex--strongly concave minimax optimization. Their theorem gives a last-iterate squared-distance bound with condition-number scale \(\sqrt{\kappa_x\kappa_y}\), but does not characterize the exact linear dynamics of the method on quadratic instances.

For the separable quadratic family
\[
f_\kappa(x,y)=\frac12x^2-\frac{1}{2\kappa}y^2,\qquad \kappa\ge 1,
\]
we have \(L=\mu_x=1\), \(\mu_y=1/\kappa\), hence \(\kappa_x=1\) and \(\kappa_y=\kappa\). Apply Algorithm 1 of arXiv:2609.20327v1 with its prescribed parameters
\[
h=\frac16,\qquad
\alpha=\left(1+\frac{1}{48\sqrt{2\kappa}}\right)^{-1},\qquad
\gamma=4\sqrt{2\kappa}-1,
\]
and initialization \(v_0=0\).

The primal coordinate decouples exactly as
\[
x_{t+1}=\frac{31}{36}x_t.
\]
For the dual-feedback state \(z_t=(y_t,v_t)^\top\), put
\[
s=\kappa^{-1/2},\qquad D=96+\sqrt2\,s,
\]
\[
\alpha=\frac{96}{D},\qquad
\beta=(1-\alpha)\gamma=\frac{8-\sqrt2\,s}{D},\qquad
c=1+\beta=\frac{104}{D},
\]
and
\[
A=1-\frac{s^2c}{6}\left(1-\frac{s^2}{6}\right),
\qquad
B=\frac{\alpha}{6}-\frac{s^2c}{36}.
\]
Then
\[
\boxed{
z_{t+1}=M_\kappa z_t,
\qquad
M_\kappa=
\begin{pmatrix}
A&B\\
-\beta s^2A&\alpha-\beta s^2B
\end{pmatrix}.}
\]
Its determinant has the exact cancellation
\[
\boxed{\det M_\kappa=\alpha A.}
\]

### Theorem 1: the feedback block is underdamped for every \(\kappa\ge1\)

For every \(\kappa\ge1\), the characteristic discriminant of \(M_\kappa\) is strictly negative. Hence its two eigenvalues are a complex-conjugate pair
\[
r_\pm=\rho_\kappa e^{\pm i\theta_\kappa},
\qquad 0<\theta_\kappa<\pi,
\]
and the exact spectral radius is
\[
\boxed{
\rho_\kappa^2
=\alpha A
=\frac{96}{D}
\left[
1-\frac{52}{3D\kappa}\left(1-\frac{1}{6\kappa}\right)
\right].}
\]

The sign of the discriminant was reduced exactly to a degree-nine polynomial on \(s\in(0,1]\). The supplied verification artifact converts its negative into the Bernstein basis on \([0,1]\); all ten Bernstein coefficients are strictly positive, giving an exact algebraic certificate rather than a sampled numerical check.

### Theorem 2: exact asymptotic damping and oscillation scales

As \(\kappa\to\infty\),
\[
\boxed{
\rho_\kappa
=1-\frac{1}{96\sqrt{2\kappa}}
-\frac{3325}{36864\kappa}
+O(\kappa^{-3/2}),}
\]
while
\[
\boxed{
\theta_\kappa
=\frac{\sqrt{510}}{192\sqrt\kappa}+O(\kappa^{-1}).}
\]
Thus the slow block approaches the defective limit
\[
M_\infty=
\begin{pmatrix}
1&1/6\\0&1
\end{pmatrix},
\]
but for every finite \(\kappa\) it is an underdamped conjugate pair. The two small scales have the fixed ratio
\[
\boxed{
\frac{-\log\rho_\kappa}{\theta_\kappa}\longrightarrow \frac{1}{\sqrt{255}}.}
\]
Consequently one full asymptotic oscillation multiplies the amplitude by
\[
\boxed{
\exp\!\left(-\frac{2\pi}{\sqrt{255}}\right)
=0.6747126877\ldots.}
\]
This identifies the auxiliary recursion as a near-Jordan underdamped accelerator on the weak-curvature coordinate.

### Theorem 3: explicit last-iterate oscillation and first sign reversal

For \(y_0=1\), \(v_0=0\), define
\[
H_\kappa
=\frac{2A-\operatorname{tr}M_\kappa}
{\sqrt{-\operatorname{disc}(M_\kappa)}}.
\]
Then the dual iterate has the closed form
\[
\boxed{
y_t=\rho_\kappa^t
\bigl[\cos(t\theta_\kappa)+H_\kappa\sin(t\theta_\kappa)\bigr],}
\]
and
\[
\boxed{
H_\kappa=\frac1{\sqrt{255}}+O(\kappa^{-1/2}).}
\]
For sufficiently large \(\kappa\), if \(t_{\rm flip}\) is the first integer for which \(y_t\le0\), then
\[
\boxed{
\frac{t_{\rm flip}}{\sqrt\kappa}
\longrightarrow
\frac{192}{\sqrt{510}}
\left(\frac\pi2+\arctan\frac1{\sqrt{255}}\right)
=13.8864733321\ldots.}
\]
Hence the weak coordinate crosses the saddle after \(\Theta(\sqrt\kappa)\) iterations while its spectral envelope is still only moderately damped.

### Consequence: the \(\sqrt\kappa\) scale is intrinsic to this fixed method, but the extra \(\log\kappa\) is not on this family

Theorem 3.1 of arXiv:2609.20327v1 bounds squared distance using the factor
\[
q_\kappa=
\left(1+\frac{1}{96\sqrt{2\kappa}}\right)^{-1}
=1-\frac{1}{96\sqrt{2\kappa}}+O(\kappa^{-1}).
\]
For the exact slow mode above,
\[
\boxed{
\rho_\kappa^2
=1-\frac{1}{48\sqrt{2\kappa}}+O(\kappa^{-1}).}
\]
Thus the source theorem's per-iteration squared-distance contraction exponent is asymptotically a factor two more conservative on this family, while the polynomial \(\sqrt\kappa\) condition-number scale itself is genuinely realized by the prescribed algorithm even though the objective has no primal--dual coupling.

Moreover,
\[
|y_t|^2\le (1+H_\kappa^2)\rho_\kappa^{2t},
\qquad
1+H_\kappa^2\to\frac{256}{255}.
\]
Therefore a sustained relative error bound \(|y_t|^2\le\varepsilon\) for all later iterates is obtained after
\[
T\le
\frac{\log((1+H_\kappa^2)/\varepsilon)}{-2\log\rho_\kappa}
=(48\sqrt2+o(1))\sqrt\kappa\,
\log\!\frac{256/255+o(1)}{\varepsilon}.
\]
There is no \(\log\kappa\) overhead in this exact family. This is consistent with the source paper's own statement that its extra logarithmic condition-number dependence enters when its Lyapunov estimate is converted to relative Euclidean distance; the calculation here quantifies that gap on a concrete instance.

### Extension to arbitrary fixed primal condition number

Fix any \(a=\kappa_x\ge1\) and let \(b=\kappa_y\to\infty\). The uncoupled quadratic
\[
f_{a,b}(x_1,x_2,y)
=\frac12x_1^2+\frac{1}{2a}x_2^2-\frac{1}{2b}y^2
\]
has \(L=1\), \(\mu_x=1/a\), and \(\mu_y=1/b\). Starting the primal coordinates at zero again isolates a two-dimensional dual-feedback block. Direct expansion gives
\[
\boxed{
\rho_{a,b}
=1-\frac{1}{96\sqrt{2ab}}+O(b^{-1}),
\qquad
\theta_{a,b}
=\frac{\sqrt{510}}{192\sqrt{ab}}+O(b^{-1}).}
\]
Thus the same source-specific near-Jordan mechanism realizes the full \(\sqrt{\kappa_x\kappa_y}\) scale along every ray with fixed \(\kappa_x\) and \(\kappa_y\to\infty\).

## Proof outline

The recurrence follows by substituting \(\nabla_x f=x\) and \(\nabla_y f=-s^2y\) into the predictor, feedback, and correction steps. Eliminating the predictor yields the displayed \(2\times2\) matrix. Its determinant simplifies to \(\alpha A\) because the two terms containing \(\beta s^2AB\) cancel.

The characteristic polynomial is
\[
r^2-(\operatorname{tr}M_\kappa)r+\alpha A=0.
\]
The exact Bernstein certificate proves its discriminant is negative on the full interval \(s\in(0,1]\), so both roots have modulus \(\sqrt{\alpha A}\). Taylor expansion at \(s=0\) gives the stated radius and angle. The second-order real recurrence for \(y_t\) then gives the sinusoidal closed form, with \(H_\kappa\) determined by \(y_0=1\) and \(y_1=A\). Expanding \(H_\kappa\) at \(s=0\) yields \(1/\sqrt{255}\), and the first sign reversal follows from the first zero of \(\cos(t\theta)+H\sin(t\theta)\). The fixed-\(\kappa_x\) extension is the same calculation after replacing \(s^2\) by \(1/\kappa_y\) and using \((\kappa_x\kappa_y)^{-1/2}\) in \(\alpha\).

## Reproducibility

`artifacts/verify_near_jordan_feedback.py` uses exact SymPy algebra for the discriminant/Bernstein certificate and NumPy for direct eigenvalue and recurrence checks. The recorded output is in `artifacts/verification_output.txt`. The verification was executed with Python 3, SymPy 1.14.0, and NumPy 2.3.5.

## Originality boundary

Linear recurrences, companion-matrix spectral analysis, acceleration on quadratics, and underdamped interpretations of momentum methods are standard and are not claimed as new. Earlier accelerated minimax work also establishes optimal or near-optimal rates for other update structures. The contribution claimed here is specific to the newly proposed feedback extragradient of arXiv:2609.20327v1: its exact decoupled quadratic block, the all-\(\kappa\) underdamped certificate, the exact spectral-radius formula, the near-Jordan damping/phase constants, the first-sign-reversal law, and the resulting separation between the genuine \(\sqrt{\kappa_x\kappa_y}\) scale and the nonintrinsic \(\log\kappa\) overhead on this family.

To the best of our knowledge, these formulas and this source-specific sharpness mechanism have not previously been stated. The motivating preprint is recent, so contemporaneous follow-up remains a material originality risk.

## Limitations

- This is an exact worst-case characterization of the prescribed fixed parameters on a separable quadratic family, not a lower bound for all first-order methods.
- The family has no primal--dual coupling; the result therefore identifies behavior created by the algorithm's weak-curvature feedback itself, not by game coupling.
- The first-sign-reversal time describes oscillatory trajectory geometry and is not itself a convergence criterion.
- The spectral-radius law is an asymptotic-rate statement. Finite-time behavior can be influenced by phase and nonnormality.
- The explicit all-\(\kappa\) discriminant certificate is given for \(\kappa_x=1\); the arbitrary fixed-\(\kappa_x\) extension is asymptotic as \(\kappa_y\to\infty\).

## References

1. M. Zhang and Z. Xu, *Near-Optimal Pure Single-Loop Extragradient Method for Strongly Convex--Strongly Concave Minimax Optimization*, arXiv:2609.20327v1, 2026.
2. T. Yoon and E. K. Ryu, *Accelerated Minimax Algorithms Flock Together*, SIAM Journal on Optimization 35(1), 2025, DOI: 10.1137/22M1504597.
3. C. J. Li, A. Yuan, G. Gidel, Q. Gu, and M. I. Jordan, *Nesterov Meets Optimism: Rate-Optimal Separable Minimax Optimization*, arXiv:2210.17550, 2022.
