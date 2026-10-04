# Exact cycle-stability frontier for scalar SAM with EMA momentum
## Finding

Consider the scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,\qquad \lambda>0,
\]
and the practical normalized SAM perturbation with radius \(\rho>0\). Couple its perturbed gradient to normalized exponential-moving-average momentum,
\[
g_t=\lambda\bigl(x_t+\rho\,\operatorname{sign}(x_t)\bigr),\qquad
m_t=\beta m_{t-1}+(1-\beta)g_t,\qquad
x_{t+1}=x_t-\alpha m_t,
\]
where \(\beta\in[0,1)\), \(\alpha>0\), and \(\operatorname{sign}(0)=0\). This is the deterministic scalar SAM-with-EMA-momentum subsystem obtained when a scalar adaptive preconditioner is held fixed. Put
\[
s=\alpha\lambda(1-\beta).
\]

There is a unique sign-alternating period-two orbit, and it is locally asymptotically stable, if and only if
\[
0<s<2(1+\beta).
\]
Writing the orbit as \(x_t=(-1)^t c\), its amplitude is
\[
c=\frac{s\rho}{2(1+\beta)-s}.
\]
Thus the amplitude diverges as the stability boundary is approached from below.

The local one-step state spectral radius cannot be smaller than \(\sqrt{\beta}\). That minimum is attained throughout the exact band
\[
(1-\sqrt{\beta})^2\le s\le(1+\sqrt{\beta})^2,
\]
with the band reducing to \(s=1\) when \(\beta=0\).

For the standard initialization \(m_{-1}=0\), every \(x_0\ne0\) alternates in sign and diverges at or above the same boundary. At
\[
s=2(1+\beta)
\]
the magnitude grows linearly, while for \(s>2(1+\beta)\) it grows at least geometrically. In the raw effective step this sharp boundary is
\[
\alpha\lambda=\frac{2(1+\beta)}{1-\beta}.
\]

## Assumptions and scope

The result concerns a one-dimensional positive quadratic, a constant normalized SAM radius, normalized EMA momentum with the factor \(1-\beta\), and a fixed positive scalar parameter preconditioner absorbed into \(\alpha\). It is deterministic. The statement is about the sign-alternating orbit and its local stability, together with a global divergence witness for the standard zero-momentum initialization at and above the boundary.

The convention \(\operatorname{sign}(0)=0\) affects only the exactly stationary state. The period-two orbit has \(c>0\), so its local analysis never evaluates the map at zero.

The fixed-preconditioner assumption deliberately isolates the first-moment momentum mechanism appearing in momentum-accelerated sharpness-aware optimizers. It does not claim the same phase diagram for a time-varying AMSGrad or Adam preconditioner.

## Proof

Use the state
\[
z_t=\begin{bmatrix}x_t\\m_{t-1}\end{bmatrix}.
\]
On either open half-line, the sign is fixed and the update is affine:
\[
z_{t+1}=Az_t+\sigma q,\qquad \sigma=\operatorname{sign}(x_t),
\]
with
\[
A=
\begin{bmatrix}
1-s&-\alpha\beta\\
(1-\beta)\lambda&\beta
\end{bmatrix},
\qquad
q=
\begin{bmatrix}
-s\rho\\
(1-\beta)\lambda\rho
\end{bmatrix}.
\]
The characteristic polynomial of \(A\) is
\[
\chi(r)=r^2-(1+\beta-s)r+\beta.
\]

Let \(z_+\) be the positive-position state of a sign-alternating period-two orbit and \(z_-\) the negative-position state. They obey
\[
z_-=Az_++q,\qquad z_+=Az_- -q.
\]
Adding gives
\[
(I-A)(z_++z_-)=0.
\]
Because
\[
\det(I-A)=\chi(1)=s>0,
\]
we obtain \(z_-=-z_+\). Hence
\[
(I+A)z_+=-q.
\]
Now
\[
\det(I+A)=\chi(-1)=2(1+\beta)-s.
\]
Solving gives
\[
z_+=
\begin{bmatrix}
c\\-2c/\alpha
\end{bmatrix},
\qquad
c=\frac{s\rho}{2(1+\beta)-s}.
\]
This solution is sign-consistent exactly for \(0<s<2(1+\beta)\). At equality the linear system is singular and no finite sign-alternating orbit exists; above it the algebraic solution has the wrong sign.

Since the orbit stays away from zero, sufficiently small perturbations preserve its alternating sign itinerary. The one-step Jacobian is therefore \(A\), so the two-step Jacobian is \(A^2\). For the monic quadratic \(\chi\), the real second-order Jury conditions are
\[
1-\beta>0,\qquad
1-(1+\beta-s)+\beta=s>0,\qquad
1+(1+\beta-s)+\beta=2(1+\beta)-s>0.
\]
Thus \(\rho(A)<1\) exactly for
\[
0<s<2(1+\beta),
\]
which proves that existence and local asymptotic stability have the same sharp frontier.

Because \(\det(A)=\beta\), the larger eigenvalue modulus is at least \(\sqrt{\beta}\). Equality occurs when the two roots are a complex-conjugate pair or a repeated real pair. The discriminant condition
\[
(1+\beta-s)^2-4\beta\le0
\]
is equivalent to
\[
(1-\sqrt{\beta})^2\le s\le(1+\sqrt{\beta})^2.
\]
Hence the minimum local one-step factor is exactly \(\sqrt{\beta}\).

Finally eliminate momentum using
\[
m_{t-1}=\frac{x_{t-1}-x_t}{\alpha}.
\]
The scalar recurrence is
\[
x_{t+1}=(1+\beta-s)x_t-\beta x_{t-1}-s\rho\,\operatorname{sign}(x_t).
\]
With \(m_{-1}=0\) and \(x_0>0\), the first step is
\[
x_1=(1-s)x_0-s\rho.
\]
At and above \(s=2(1+\beta)\), this is negative. Writing \(x_t=(-1)^t y_t\), the positive magnitudes satisfy
\[
y_{t+1}=(s-1-\beta)y_t-\beta y_{t-1}+s\rho.
\]
At the boundary this becomes
\[
y_{t+1}=(1+\beta)y_t-\beta y_{t-1}+2(1+\beta)\rho.
\]
For \(d_t=y_t-y_{t-1}\),
\[
d_{t+1}=\beta d_t+2(1+\beta)\rho,
\]
so \(d_t\) approaches a positive constant and \(y_t\) grows linearly. Above the boundary, if \(y_t>y_{t-1}>0\), then
\[
y_{t+1}>(s-1-2\beta)y_t+s\rho,
\]
and \(s-1-2\beta>1\); the magnitudes therefore increase at least geometrically. The case \(x_0<0\) follows by odd symmetry.

## Verification

The accompanying `verify.py` independently reconstructs the affine state map, checks the exact period-two points on rational and floating-point parameter sets, evaluates the characteristic roots against the Jury boundary, checks the rate-optimal band, and simulates the boundary and supercritical zero-momentum trajectories.

These finite checks are only transcription and algebra guards. The infinite-iteration statements follow from the exact affine equations, the Jury criterion, and the magnitude recurrence above.

## Relationship to prior work

Foret et al. introduced practical SAM. Bartlett, Long, and Bousquet proved that ordinary SAM on convex quadratics approaches a top-curvature sign-alternating cycle and analyzed that no-momentum dynamics. Wen, Ma, and Li also characterized the no-momentum quadratic alignment/cycle mechanism. Si and Yun studied practical constant-radius SAM, including one-dimensional quadratic behavior and large-step nonconvergence.

Momentum has been analyzed in sharpness-aware optimization from other angles. Kim et al. studied its effect on SAM diffusion near saddle points and explicitly treated broader momentum dynamics as a direction needing further investigation. Sun et al.'s AdaSAM combines the SAM gradient with normalized EMA momentum and an adaptive preconditioner, proving a stochastic nonconvex convergence guarantee rather than a scalar periodic-orbit phase diagram. Becker, Altrock, and Risse's MSAM instead changes the perturbation direction to accumulated momentum, so its update is structurally different.

The present result isolates the fixed-preconditioner EMA-momentum subsystem and gives an exact necessary-and-sufficient alternating-cycle frontier, exact orbit amplitude, optimal local spectral band, and sharp divergence behavior. Targeted searches did not identify these statements in the inspected sources. A residual risk remains that an equivalent calculation exists under different heavy-ball or switched-affine terminology.

## Limitations

The theorem does not analyze a time-varying adaptive preconditioner, stochastic gradients, minibatching, multidimensional mode switching, nonquadratic objectives, or generalization. The local-stability statement requires staying in the alternating-sign neighborhood of the nonzero orbit. The supercritical divergence statement is for the standard initialization \(m_{-1}=0\).

The stability calculation uses the normalized EMA convention \(m_t=\beta m_{t-1}+(1-\beta)g_t\). Other momentum normalizations require rescaling and are not covered verbatim. The spectral optimum is a local linear rate around the orbit, not a global iteration-complexity optimum.

## References

1. Pierre Foret, Ariel Kleiner, Hossein Mobahi, and Behnam Neyshabur, “Sharpness-Aware Minimization for Efficiently Improving Generalization,” arXiv:2010.01412v1, 2020.
2. Peter L. Bartlett, Philip M. Long, and Olivier Bousquet, “The Dynamics of Sharpness-Aware Minimization: Bouncing Across Ravines and Drifting Towards Wide Minima,” arXiv:2210.01513v1, 2022.
3. Hoki Kim, Jinseong Park, Yujin Choi, and Jaewook Lee, “Stability Analysis of Sharpness-Aware Minimization,” arXiv:2301.06308v1, 2023.
4. Hao Sun et al., “AdaSAM: Boosting Sharpness-Aware Minimization with Adaptive Learning Rate and Momentum for Training Deep Neural Networks,” arXiv:2303.00565v1, 2023.
5. Dongkuk Si and Chulhee Yun, “Practical Sharpness-Aware Minimization Cannot Converge All the Way to Optima,” arXiv:2306.09850v1, 2023.
6. Marlon Becker, Frederick Altrock, and Benjamin Risse, “Momentum-SAM: Sharpness Aware Minimization without Computational Overhead,” arXiv:2401.12033v1, 2024.
