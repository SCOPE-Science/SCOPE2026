# Sharp origin-dependence dichotomy for Fromage on quadratics
## Finding

Consider Fromage with constant learning rate \(\eta>0\) on the centered SPD quadratic
\[
f(x)=\frac12 x^\top Hx,
\qquad
\mu I\preceq H\preceq LI,
\]
and define
\[
\kappa=\frac{L}{\mu}.
\]
For every nonzero state, the Fromage update is
\[
F_\eta(x)
=
\frac{
x-\eta\frac{\|x\|}{\|Hx\|}Hx
}{
\sqrt{1+\eta^2}
}.
\]

The exact one-step norm identity is
\[
\frac{\|F_\eta(x)\|^2}{\|x\|^2}
=
1-
\frac{2\eta}{1+\eta^2}
\frac{x^\top Hx}{\|x\|\|Hx\|}.
\]
The sharp lower bound
\[
\frac{x^\top Hx}{\|x\|\|Hx\|}
\ge
\frac{2\sqrt{\mu L}}{\mu+L}
=
\frac{2\sqrt{\kappa}}{\kappa+1}
\]
therefore gives the sharp worst-case Euclidean contraction factor
\[
q_F(\eta,\kappa)
=
\sqrt{
1-
\frac{4\eta\sqrt{\kappa}}
{(1+\eta^2)(\kappa+1)}
}.
\]
The bound is attained already in two dimensions.

Consequently, every finite learning rate
\[
\eta>0
\]
is uniformly contractive on the entire class of centered SPD quadratics. The unique learning rate that minimizes the sharp one-step bound is
\[
\eta=1,
\]
because \(\eta/(1+\eta^2)\) is uniquely maximized there. The resulting factor is
\[
q_F^\star(\kappa)
=
\frac{\sqrt{\kappa}-1}{\sqrt{\kappa+1}}
=
1-\kappa^{-1/2}+O(\kappa^{-1}).
\]
Iterating the one-step estimate yields
\[
\|x_t\|
\le
\left[q_F^\star(\kappa)\right]^t
\|x_0\|.
\]
Thus the prefactored Fromage update has a sharp \(O(\sqrt{\kappa}\log(1/\varepsilon))\) uniform Euclidean guarantee on this centered quadratic benchmark.

For comparison, remove only Fromage's prefactor and keep the same proportional gradient step:
\[
L_\eta(x)
=
x-\eta\frac{\|x\|}{\|Hx\|}Hx.
\]
This idealized LARS-type map has the sharp factor
\[
q_L(\eta,\kappa)^2
=
1+\eta^2
-
\frac{4\eta\sqrt{\kappa}}{\kappa+1}.
\]
Uniform strict contraction holds exactly when
\[
0<\eta<
\frac{4\sqrt{\kappa}}{\kappa+1}.
\]
Its best learning rate is
\[
\eta_L^\star
=
\frac{2\sqrt{\kappa}}{\kappa+1},
\]
with sharp factor
\[
q_L^\star(\kappa)
=
\frac{\kappa-1}{\kappa+1}.
\]
Hence the normalization prefactor introduced by Fromage both removes the finite centered-quadratic stability ceiling of the proportional update and changes its best sharp one-step condition-number scaling from \(1-O(\kappa^{-1})\) to \(1-O(\kappa^{-1/2})\).

This improvement is intrinsically origin dependent. Let
\[
f_a(x)=\frac{\lambda}{2}(x-a)^2,
\qquad
a>0,
\]
and use the official scalar Fromage rule with
\[
0<\eta<1.
\]
Write
\[
c=\frac{1}{\sqrt{1+\eta^2}},
\qquad
A=(1+\eta)c,
\qquad
B=(1-\eta)c.
\]
Then
\[
A>1,
\qquad
0<B<1.
\]
For positive \(x\), the update is
\[
T(x)=
\begin{cases}
Ax,&0<x<a,\\
ca,&x=a,\\
Bx,&x>a.
\end{cases}
\]
Every positive orbit enters the invariant interval
\[
[Ba,Aa]
\]
after finitely many steps, but no positive orbit converges to the minimizer \(a\).

Away from the countable set of initial conditions whose orbit lands exactly on \(a\), define
\[
y=\log(x/a),
\qquad
u=\log A,
\qquad
v=-\log B.
\]
On the invariant interval, \(y\in[-v,u]\), and the map becomes
\[
y\mapsto
\begin{cases}
y+u,&y<0,\\
y-v,&y>0.
\end{cases}
\]
After identifying the two endpoints, this is exactly rigid rotation by \(u\) on a circle of circumference \(u+v\). If \(u/(u+v)\) is irrational, the post-transient orbit is dense in the interval after converting back to \(x\); if it is rational and the orbit avoids the exact minimizer, the orbit is periodic.

The centered square-root-conditioned bound is therefore a sharp property of Fromage's origin-based relative geometry, not a translation-invariant quadratic convergence theorem.

## Assumptions and scope

The centered result uses a deterministic SPD quadratic, one parameter block, the Euclidean/Frobenius norm, and the Fromage prefactor exactly as specified in the defining paper and official implementation. The factor \(q_F\) is a sharp worst-case one-step bound and therefore gives a valid global geometric upper bound; it is not claimed to equal every trajectory's asymptotic rate.

The LARS comparison removes only the Fromage prefactor and keeps the same norm-ratio direction. It is a mathematical comparison map rather than a claim about every practical LARS variant, which may include trust coefficients, weight decay, schedules, or layer-specific conventions.

The shifted-scalar statement assumes \(a>0\), a positive initial state, and \(0<\eta<1\), which keeps the scalar state positive. Qualitative failure of fixed-rate proportional updates to converge exactly on shifted one-dimensional objectives was already established in earlier proportional-update analysis; the result here identifies the exact Fromage-prefactor dynamics and its rigid log-rotation structure.

No stochastic gradients, momentum, multiple parameter blocks, weight decay, or projection bound are included.

## Proof

For \(x\ne0\), set
\[
c_H(x)
=
\frac{x^\top Hx}{\|x\|\|Hx\|}.
\]
Expanding the Fromage step gives
\[
\begin{aligned}
\|F_\eta(x)\|^2
&=
\frac{1}{1+\eta^2}
\left\|
x-\eta\frac{\|x\|}{\|Hx\|}Hx
\right\|^2\\
&=
\|x\|^2
\left[
1-\frac{2\eta}{1+\eta^2}c_H(x)
\right].
\end{aligned}
\]

To minimize \(c_H\), note that every eigenvalue \(\lambda\in[\mu,L]\) satisfies
\[
\lambda^2+\mu L
\le
(\mu+L)\lambda.
\]
Applying this eigenwise gives
\[
\|Hx\|^2+\mu L\|x\|^2
\le
(\mu+L)x^\top Hx.
\]
Divide by \(\|x\|\|Hx\|\) and put
\[
r=\frac{\|Hx\|}{\|x\|}.
\]
Then
\[
c_H(x)
\ge
\frac{r+\mu L/r}{\mu+L}
\ge
\frac{2\sqrt{\mu L}}{\mu+L}.
\]
The second inequality is arithmetic-geometric mean.

Sharpness is attained for
\[
H=
\begin{bmatrix}
\mu&0\\
0&L
\end{bmatrix}
\]
and any nonzero vector whose squared components satisfy
\[
\frac{x_L^2}{x_\mu^2}
=
\frac{\mu}{L}.
\]
Substitution gives equality in both inequalities. This proves the exact formula for \(q_F\).

Since
\[
\frac{\eta}{1+\eta^2}
\]
has its unique maximum over \(\eta>0\) at \(\eta=1\), the optimal sharp Fromage bound follows directly.

Without the prefactor,
\[
\frac{\|L_\eta(x)\|^2}{\|x\|^2}
=
1+\eta^2-2\eta c_H(x).
\]
The same sharp minimum cosine produces
\[
q_L^2
=
1+\eta^2-
\frac{4\eta\sqrt{\kappa}}{\kappa+1}.
\]
The condition \(q_L<1\) is equivalent to
\[
0<\eta<
\frac{4\sqrt{\kappa}}{\kappa+1}.
\]
Minimizing the quadratic in \(\eta\) gives
\[
\eta_L^\star
=
\frac{2\sqrt{\kappa}}{\kappa+1}
\]
and
\[
q_L^\star
=
\frac{\kappa-1}{\kappa+1}.
\]

For the shifted scalar problem, the gradient has sign \(\operatorname{sign}(x-a)\). With positive \(x\), the official norm-ratio step has magnitude \(\eta x\), followed by multiplication by \(c\). Therefore
\[
T(x)=Ax
\]
below \(a\) and
\[
T(x)=Bx
\]
above \(a\). At \(x=a\), the gradient is zero, so the implementation leaves the additive step unchanged and still applies the prefactor, giving
\[
T(a)=ca<a.
\]

If \(x<a\), repeated multiplication by \(A>1\) reaches or crosses \(a\) in finitely many steps; the first crossing is below \(Aa\). If \(x>a\), repeated multiplication by \(B<1\) reaches or crosses \(a\) in finitely many steps; the first crossing is above \(Ba\). Direct substitution shows that \([Ba,Aa]\) is invariant.

For states that do not hit \(a\), the logarithmic coordinate satisfies
\[
y\mapsto y+u
\]
below zero and
\[
y\mapsto y-v
\]
above zero. Both branches are the same transformation
\[
y\mapsto y+u \pmod{u+v}.
\]
Thus the post-transient dynamics are a rigid circle rotation. The set of initial conditions that hit \(a\) is a countable union of inverse images. An orbit that hits \(a\) cannot converge to \(a\), because its next state is always \(ca\ne a\); an orbit that never hits \(a\) follows a nontrivial rigid rotation and likewise cannot converge to \(a\). The rational and irrational cases give periodic and dense behavior respectively.

## Verification

The accompanying `verify.py` reconstructs both centered maps, checks the exact norm identities, verifies the sharp two-eigenvalue witness, tests the strict-contraction regions on deterministic condition-number grids, and checks the shifted scalar piecewise map and its logarithmic rotation identity.

These computations are transcription and boundary guards. Sharpness and the infinite-time statements follow from the analytic inequalities and circle-rotation conjugacy above.

## Relationship to prior work

Bernstein, Vahdat, Yue, and Liu introduced Fromage from a relative-distance analysis for neural-network parameter blocks. Their update scales the gradient to the parameter norm and then applies the factor
\[
(1+\eta^2)^{-1/2}.
\]
The defining paper explains that the prefactor distinguishes Fromage from LARS and is intended to compensate compounding norm growth. The inspected paper and official implementation do not give the sharp SPD-quadratic condition-number law above.

Gitman, Dilipkumar, and Parr gave an earlier convergence analysis of proportional updates such as LARS and PercentDelta. Their one-dimensional shifted-quadratic analysis already establishes that a fixed proportional learning rate need not converge exactly to a nonzero minimizer, and their broader theory studies convergence regions for strongly convex objectives. The present claim does not treat that qualitative nonconvergence as new. Instead, it isolates the exact effect of Fromage's later normalization prefactor: unconditional centered-quadratic contraction, a sharp square-root-conditioned one-step factor, and the exact prefactored shifted-scalar rotation.

Normalized-gradient methods were also studied before Fromage, including continuous-time analyses with condition-number-dependent behavior. Those results use different step geometry and do not imply the discrete Fromage norm-ratio-plus-prefactor identity.

Focused searches for Fromage quadratic convergence, proportional updates, normalized gradients, sharp condition-number factors, and translation dependence did not identify the complete dichotomy stated here.

## Limitations

The sharp \(O(\sqrt{\kappa}\log(1/\varepsilon))\) statement is a repeated one-step Euclidean upper bound on centered SPD quadratics. It is not a lower bound on the best possible asymptotic Fromage trajectory.

The origin is structurally privileged by the parameter norm in the update. The shifted example shows that one must not transfer the centered theorem to arbitrary translated objectives.

The shifted rotation classification is scalar and assumes \(0<\eta<1\). Larger learning rates can change sign and require a different symbolic partition.

Practical Fromage operates blockwise in neural networks and may use a parameter-norm bound. Those features are outside this theorem.

An equivalent sharp centered formula may exist in older normalized-gradient or numerical linear-algebra literature under terminology not mentioning Fromage; this remains the principal originality risk.

## References

1. Jeremy Bernstein, Arash Vahdat, Yisong Yue, and Ming-Yu Liu, “On the distance between two neural networks and the stability of learning,” arXiv:2002.03432v1, 2020.
2. Official `jxbz/fromage` implementation, file `fromage.py`, blob revision `840c6ce062237a62b31741457dc693644d448096`.
3. Igor Gitman, Deepak Dilipkumar, and Ben Parr, “Convergence Analysis of Gradient Descent Algorithms with Proportional Updates,” arXiv:1801.03137v1, 2018.
4. Ryan Murray, Brian Swenson, and Soummya Kar, “Revisiting Normalized Gradient Descent: Fast Evasion of Saddle Points,” arXiv:1711.05224v1, 2017.
