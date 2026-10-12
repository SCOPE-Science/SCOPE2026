# Exact condition-optimal scalar actuator for a two-mode discrete-time Gramian

## Finding
Consider the stable two-state single-input system
\[
z_{k+1}=Az_k+vu_k,
\qquad
A=\operatorname{diag}(a,d),
\]
with
\[
|a|<1,\qquad |d|<1,\qquad a\ne d.
\]
Only the actuator direction matters for the condition number of the infinite-horizon controllability Gramian, so normalize
\[
\|v\|_2=1
\]
and write
\[
v=(\cos\theta,\sin\theta)^{\mathsf T}.
\]

The actuator direction minimizing the spectral condition number of the controllability Gramian is characterized exactly by
\[
\boxed{
\cos^2\theta_*
=
\frac{1-a^2}{2-a^2-d^2},
\qquad
\sin^2\theta_*
=
\frac{1-d^2}{2-a^2-d^2}.
}
\]
At this direction the two diagonal modal Gramian energies are equal.

The minimum condition number has the closed form
\[
\boxed{
\kappa_{\min}
=
\frac{1+\rho}{1-\rho},
\qquad
\rho=
\frac{\sqrt{(1-a^2)(1-d^2)}}{1-ad}.
}
\]
If
\[
\alpha=\operatorname{artanh}(a),
\qquad
\beta=\operatorname{artanh}(d),
\]
then
\[
\rho=\operatorname{sech}(\alpha-\beta),
\]
so
\[
\boxed{
\kappa_{\min}
=
\coth^2\!\left(
\frac{|\alpha-\beta|}{2}
\right).
}
\]

This exposes an intrinsic limitation of scalar actuation. Near a repeated stable mode,
\[
\kappa_{\min}
\sim
\frac{4}{(\alpha-\beta)^2},
\]
so rotating the actuator cannot prevent the controllability ellipsoid from becoming badly anisotropic.

For
\[
A=\operatorname{diag}\!\left(0,\frac35\right),
\qquad
v_*=\frac1{\sqrt{41}}(5,4)^{\mathsf T},
\]
the exact optimal Gramian is
\[
W_*=
\frac1{41}
\begin{pmatrix}
25&20\\
20&25
\end{pmatrix},
\]
whose eigenvalues are \(45/41\) and \(5/41\). Thus
\[
\kappa_2(W_*)=9.
\]

## Assumptions and scope
The result concerns a real, stable, diagonal, two-state discrete-time LTI system with one scalar input. The two eigenvalues are distinct. Repeated eigenvalues with one scalar input are uncontrollable in this diagonal model, which is consistent with the divergence of the optimal condition number as the eigenvalues coalesce.

The actuator magnitude is fixed only to remove an irrelevant scale: replacing \(v\) by \(\gamma v\) multiplies the Gramian by \(\gamma^2\) and leaves its condition number unchanged.

The objective is the spectral condition number of the infinite-horizon controllability Gramian. This is a directional uniformity metric: the ratio between the largest and smallest eigenvalues of the inverse Gramian is the same condition number, so it measures the ratio between the worst and best unit-direction minimum control energies.

The theorem does not claim that condition number is the unique appropriate actuator metric. Determinant, trace, smallest eigenvalue, and trace of the inverse encode different design goals.

## Proof
The infinite-horizon controllability Gramian is
\[
W(\theta)
=
\sum_{j=0}^{\infty}A^jvv^{\mathsf T}A^j.
\]
Set
\[
p=\frac1{1-a^2},
\qquad
q=\frac1{1-d^2},
\qquad
r=\frac1{1-ad},
\qquad
x=\cos^2\theta.
\]
Then
\[
W=
\begin{pmatrix}
px&r\sqrt{x(1-x)}\,\sigma\\
r\sqrt{x(1-x)}\,\sigma&q(1-x)
\end{pmatrix},
\]
where \(\sigma\in\{-1,1\}\) records the sign of \(\sin\theta\cos\theta\). The sign does not affect the eigenvalues.

For \(0<x<1\),
\[
\operatorname{tr}W
=
q+(p-q)x
\]
and
\[
\det W
=
(pq-r^2)x(1-x).
\]
Moreover,
\[
pq-r^2
=
\frac{(a-d)^2}
{(1-a^2)(1-d^2)(1-ad)^2}
>0,
\]
so every interior actuator direction is controllable.

For a positive \(2\times2\) matrix with eigenvalues
\[
0<\lambda_-\le\lambda_+,
\]
minimizing
\[
\kappa_2(W)=\frac{\lambda_+}{\lambda_-}
\]
is equivalent to minimizing
\[
\frac{(\operatorname{tr}W)^2}{\det W},
\]
because
\[
\frac{(\operatorname{tr}W)^2}{\det W}
=
\kappa_2(W)+\frac1{\kappa_2(W)}+2
\]
and the right-hand side is strictly increasing for
\[
\kappa_2(W)\ge1.
\]

Therefore it suffices to minimize
\[
F(x)
=
\frac{(q+(p-q)x)^2}{x(1-x)}
\]
on \(0<x<1\). Since \(F(x)\) diverges at both endpoints, any interior critical point is a global candidate. Differentiation gives the unique critical point
\[
x_*=\frac{q}{p+q}.
\]
Hence
\[
\cos^2\theta_*
=
\frac{q}{p+q}
=
\frac{1-a^2}{2-a^2-d^2},
\]
and similarly
\[
\sin^2\theta_*
=
\frac{1-d^2}{2-a^2-d^2}.
\]

At this point,
\[
p\cos^2\theta_*
=
q\sin^2\theta_*
=
\frac{pq}{p+q}.
\]
Thus, up to a positive scalar, the optimal Gramian is
\[
\begin{pmatrix}
1&\rho\sigma\\
\rho\sigma&1
\end{pmatrix},
\qquad
\rho=\frac{r}{\sqrt{pq}}
=
\frac{\sqrt{(1-a^2)(1-d^2)}}{1-ad}.
\]
Because
\[
(1-ad)^2-(1-a^2)(1-d^2)
=
(a-d)^2>0,
\]
we have
\[
0<\rho<1.
\]
The two eigenvalues are proportional to
\[
1+\rho
\quad\text{and}\quad
1-\rho,
\]
which proves
\[
\kappa_{\min}
=
\frac{1+\rho}{1-\rho}.
\]

Now write
\[
a=\tanh\alpha,
\qquad
d=\tanh\beta.
\]
The hyperbolic subtraction identity gives
\[
1-ad
=
\frac{\cosh(\alpha-\beta)}
{\cosh\alpha\cosh\beta},
\]
whereas
\[
\sqrt{(1-a^2)(1-d^2)}
=
\frac1{\cosh\alpha\cosh\beta}.
\]
Therefore
\[
\rho=\operatorname{sech}(\alpha-\beta).
\]
Using
\[
\frac{1+\operatorname{sech}t}
{1-\operatorname{sech}t}
=
\coth^2\!\left(\frac{|t|}{2}\right)
\]
yields the stated formula.

Finally,
\[
\coth^2\!\left(\frac{|t|}{2}\right)
\sim\frac4{t^2}
\]
as \(t\to0\), giving the near-coalescence asymptotic.

For comparison, the determinant is
\[
\det W=(pq-r^2)x(1-x),
\]
so under the same unit-input constraint its maximizer is always
\[
x=\frac12.
\]
This generally differs from the condition-number optimizer.

## Verification
The embedded `verify.py` checks the exact rational example
\[
a=0,
\qquad
d=\frac35.
\]
For the predicted optimal squared actuator weights
\[
\cos^2\theta_*=\frac{25}{41},
\qquad
\sin^2\theta_*=\frac{16}{41},
\]
it reconstructs
\[
W_*=
\frac1{41}
\begin{pmatrix}
25&20\\
20&25
\end{pmatrix}.
\]
The checker verifies exactly that its eigenvalues are
\[
\frac{45}{41}
\quad\text{and}\quad
\frac5{41},
\]
so the condition number is \(9\).

It also verifies the determinant identity
\[
pq-r^2
=
\frac{(a-d)^2}
{(1-a^2)(1-d^2)(1-ad)^2}
\]
on exact rational test values and verifies that the determinant-optimal direction differs from the condition-optimal direction in the displayed example.

The all-parameter minimization is analytic and is not inferred from finite testing.

## Relationship to prior work
Gramian-based actuator design is classical. Summers, Cortesi, and Lygeros explain the energy interpretation of controllability-Gramian eigenvalues and optimize actuator sets using trace, trace inverse, determinant, smallest eigenvalue, and rank metrics. Their setting is a finite set of possible actuator placements.

Enyioha, Rahimian, Pappas, and Jadbabaie explicitly use the condition number of the controllability Gramian as a quantitative notion of well-conditioned network controllability, and study how that condition number scales with network size and topology.

A later full treatment by Dilip gives a Hadamard-product representation of the controllability Gramian for diagonalizable continuous- and discrete-time systems. For single-input actuator selection it optimizes determinant and trace-inverse metrics over a finite set of candidate actuators. The discrete infinite-horizon entry formula
\[
\frac1{1-\lambda_i\lambda_j}
\]
in that work is the structural starting point for the two-mode calculation here. A full-text search of that paper found no condition-number optimization; its stated actuator objectives are determinant, trace inverse, and trace.

The additional result here changes both the design variable and the objective: the actuator direction varies continuously on the unit circle, and the objective is the Gramian spectral condition number. The exact optimizer equalizes modal diagonal energies, differs from the determinant optimizer unless
\[
a^2=d^2,
\]
and yields the hyperbolic-separation law
\[
\kappa_{\min}
=
\coth^2\!\left(
\frac{|\operatorname{artanh}(a)-\operatorname{artanh}(d)|}{2}
\right).
\]
Targeted searches using condition-number, actuator-direction, diagonal-system, hyperbolic, and Gramian terminology did not locate an implication-equivalent statement.

## Limitations
The state coordinates are the orthonormal modal coordinates of a real diagonal normal system. For nonnormal dynamics, a change of eigenbasis can itself alter the Euclidean Gramian condition number.

Only two modes and one scalar actuator are classified. Higher-dimensional continuous actuator-direction design is a different optimization problem.

The infinite-horizon assumption is essential to the simple Cauchy-type entry formula. Finite-horizon variants have analogous explicit entries but a different optimization law.

Condition number measures directional anisotropy, not overall actuator strength. An actuator can have an excellent condition number while having uniformly weak authority if its magnitude is constrained differently; that scale issue is removed here by fixing only direction and observing the scale invariance of the condition number.

## References
1. T. H. Summers, F. L. Cortesi, and J. Lygeros, “On Submodularity and Controllability in Complex Dynamical Networks,” arXiv:1404.7665v1, submitted 2014-04-30.
2. C. Enyioha, M. A. Rahimian, G. J. Pappas, and A. Jadbabaie, “Controllability and Fraction of Leaders in Infinite Network,” arXiv:1410.1830v1, submitted 2014-10-06; IEEE Conference on Decision and Control, 2014.
3. M. D. Kaba and M. K. Camlibel, “A Spectral Characterization of Controllability for Linear Discrete-Time Systems with Conic Constraints,” SIAM Journal on Control and Optimization 53 (2015), 2350–2372. DOI 10.1137/140960967.
4. A. S. A. Dilip, “The Controllability Gramian, the Hadamard Product, and the Optimal Actuator/Leader and Sensor Selection Problem,” IEEE Control Systems Letters 3 (2019), 883–888. DOI 10.1109/LCSYS.2019.2919278.
