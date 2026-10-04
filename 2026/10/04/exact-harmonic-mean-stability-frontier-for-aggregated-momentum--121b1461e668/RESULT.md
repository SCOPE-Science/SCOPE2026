# Exact harmonic-mean stability frontier for Aggregated Momentum
## Finding

Consider Aggregated Momentum with \(K\ge1\) velocity buffers and a constant learning rate \(\gamma>0\):
\[
v_t^{(i)}
=
\beta_i v_{t-1}^{(i)}
-
\nabla f(x_{t-1}),
\qquad
i=1,\ldots,K,
\]
\[
x_t
=
x_{t-1}
+
\frac{\gamma}{K}
\sum_{i=1}^K v_t^{(i)},
\]
where
\[
0\le\beta_i<1.
\]
Let
\[
f(x)
=
\frac12
(x-x^\star)^\top A(x-x^\star),
\qquad
A\succ0,
\]
and write
\[
L=\lambda_{\max}(A).
\]

Define the damping-vector stability number
\[
s_\star
=
\frac{2K}{
\displaystyle\sum_{i=1}^K\frac{1}{1+\beta_i}
}.
\]
Equivalently,
\[
s_\star
=
2\,\operatorname{HM}
(1+\beta_1,\ldots,1+\beta_K),
\]
where \(\operatorname{HM}\) is the harmonic mean.

Then the complete AggMo linear state converges geometrically to the quadratic minimizer from every initial state if and only if
\[
0<\gamma L<s_\star.
\]
At the boundary
\[
\gamma L=s_\star,
\]
the top-curvature modal block has the eigenvalue
\[
z=-1.
\]
For
\[
\gamma L>s_\star,
\]
the method is not Schur stable.

Thus the absolute quadratic stepsize ceiling is exactly the harmonic mean of the single-buffer ceilings:
\[
2(1+\beta_{\min})
\le
s_\star
\le
2(1+\beta_{\max}).
\]
For a genuinely heterogeneous damping vector both inequalities are strict. In particular, aggregating a low-damping buffer with a high-damping buffer does not increase the absolute scalar stability ceiling beyond that of the highest-\(\beta\) buffer. Its passive-damping benefit must therefore come from the location and geometry of the roots inside the stable region, rather than from moving the outer Schur boundary past the most permissive single buffer.

For the geometric family proposed in the source paper,
\[
\beta_i=1-a^{i-1},
\qquad
0<a<1,
\]
one has
\[
s_\star(K,a)
=
\frac{2K}{
\displaystyle\sum_{i=1}^K\frac{1}{2-a^{i-1}}
},
\]
and
\[
\lim_{K\to\infty}s_\star(K,a)=4.
\]
For the stated practical vectors,
\[
[0,0.9,0.99]
\]
gives
\[
s_\star=2.957371920219007,
\]
while
\[
[0,0.9,0.99,0.999]
\]
gives
\[
s_\star=3.1632074969779493.
\]

## Assumptions and scope

The theorem concerns the equal-weight AggMo update from the defining paper, with a common constant learning rate for all velocity buffers. The objective is a strictly convex quadratic and the damping coefficients satisfy \(0\le\beta_i<1\).

The result is a full-state linear-stability statement. It allows arbitrary initial buffer values, although the original algorithm initializes all buffers at zero. For repeated damping coefficients, buffer-difference modes remain at the repeated eigenvalue \(\beta_i\) and are automatically stable.

The theorem does not optimize the convergence rate within the stable region. It does not cover separate per-buffer learning rates, stochastic gradients, time-varying damping, nonquadratic objectives, or semidefinite quadratics with a nontrivial nullspace.

## Proof

Because \(A\) is symmetric positive definite, its orthonormal eigenbasis decouples the algorithm into scalar curvature modes. Fix one eigenvalue \(\lambda>0\) and define
\[
s=\gamma\lambda.
\]
The corresponding modal state obeys
\[
v_t^{(i)}
=
\beta_i v_{t-1}^{(i)}
-
\lambda x_{t-1},
\]
\[
x_t
=
(1-s)x_{t-1}
+
\frac{\gamma}{K}
\sum_{i=1}^K
\beta_i v_{t-1}^{(i)}.
\]

Let \(z\) be an eigenvalue of this \((K+1)\)-dimensional modal map. Away from the stable buffer poles \(z=\beta_i\), the velocity equations give
\[
v^{(i)}
=
-\frac{\lambda x}{z-\beta_i}.
\]
Using
\[
x_t
=
x_{t-1}
+
\frac{\gamma}{K}
\sum_{i=1}^K v_t^{(i)}
\]
then yields the scalar characteristic equation
\[
z-1
+
\frac{s z}{K}
\sum_{i=1}^K
\frac{1}{z-\beta_i}
=
0.
\]
Multiplying by \(\prod_i(z-\beta_i)\) gives the monic characteristic polynomial
\[
P_s(z)
=
(z-1)
\prod_{i=1}^K(z-\beta_i)
+
\frac{s z}{K}
\sum_{i=1}^K
\prod_{j\ne i}(z-\beta_j).
\]
This polynomial formula also covers repeated damping coefficients.

At \(s=0\), the roots are
\[
1,\beta_1,\ldots,\beta_K.
\]
All buffer roots are strictly inside the unit disk. The root at \(1\) moves inside for small positive \(s\), because implicit differentiation of the rational characteristic equation at \((z,s)=(1,0)\) gives
\[
\left.\frac{dz}{ds}\right|_{s=0}
=
-\frac1K
\sum_{i=1}^K
\frac{1}{1-\beta_i}
<0.
\]
Hence the system is Schur stable for sufficiently small \(s>0\).

It remains to find the first possible unit-circle crossing. Let
\[
z=e^{\mathrm i\theta},
\qquad
0<|\theta|<\pi.
\]
The characteristic equation can be written
\[
1-z
=
\frac{s}{K}
H(z),
\qquad
H(z)
=
\sum_{i=1}^K
\frac{z}{z-\beta_i}.
\]
For
\[
D_i
=
1-2\beta_i\cos\theta+\beta_i^2,
\]
one has
\[
H(z)
=
\sum_{i=1}^K
\frac{1-\beta_i\cos\theta}{D_i}
-
\mathrm i\sin\theta
\sum_{i=1}^K
\frac{\beta_i}{D_i}.
\]
If a real positive \(s\) produced a nonreal unit-circle root, then
\[
\frac{1-z}{H(z)}
\]
would be real. But
\[
\operatorname{Im}
\bigl((1-z)\overline{H(z)}\bigr)
=
-\sin\theta
\sum_{i=1}^K
\frac{1-\beta_i}{D_i},
\]
which is nonzero because every \(\beta_i<1\). Therefore no nonreal point of the unit circle can be a characteristic root for positive \(s\).

The point \(z=1\) is not a root for \(s>0\). At \(z=-1\),
\[
2
=
\frac{s}{K}
\sum_{i=1}^K
\frac{1}{1+\beta_i},
\]
so the unique unit-circle crossing occurs at
\[
s=s_\star
=
\frac{2K}{
\displaystyle\sum_{i=1}^K(1+\beta_i)^{-1}
}.
\]
By continuity of polynomial roots and the absence of any earlier unit-circle crossing, every modal eigenvalue lies strictly inside the disk for
\[
0<s<s_\star.
\]

For necessity beyond the boundary, note that a real monic Schur polynomial of degree \(K+1\) must satisfy
\[
(-1)^{K+1}P_s(-1)>0.
\]
Direct evaluation gives
\[
(-1)^{K+1}P_s(-1)
=
\left(
\prod_{i=1}^K(1+\beta_i)
\right)
\left[
2
-
\frac{s}{K}
\sum_{i=1}^K
\frac{1}{1+\beta_i}
\right].
\]
This quantity is zero at \(s=s_\star\) and negative for \(s>s_\star\). Hence Schur stability is impossible above the boundary.

For the full quadratic, the modal parameter is \(s=\gamma\lambda\). Since every eigenvalue satisfies
\[
0<\lambda\le L,
\]
all modes are stable exactly when
\[
0<\gamma L<s_\star.
\]

Finally, because a harmonic mean lies between the smallest and largest entries,
\[
2(1+\beta_{\min})
\le s_\star
\le 2(1+\beta_{\max}).
\]
For the geometric family \(\beta_i=1-a^{i-1}\), the summands \((2-a^{i-1})^{-1}\) converge to \(1/2\); their Cesàro mean therefore converges to \(1/2\), which proves
\[
s_\star(K,a)\to4.
\]

## Verification

The accompanying `verify.py` reconstructs the exact AggMo modal matrix and characteristic polynomial. It verifies the closed boundary identity at \(z=-1\) using rational arithmetic, checks the no-nonreal-unit-circle formula numerically at many angles, computes characteristic roots with a standalone Durand–Kerner solver on both sides of the threshold, and reproduces the stated default-vector constants.

The numerical root calculations are only verification guards. The infinite-dimensional-in-time stability statement follows from the exact characteristic equation, the unit-circle exclusion argument, and the sign condition at \(z=-1\).

## Relationship to prior work

Lucas, Sun, Zemel, and Grosse introduced Aggregated Momentum as a collection of differently damped velocity buffers and motivated it by passive suppression of oscillations. Their quadratic appendix writes the exact \((K+1)\)-state linear system and computes convergence rates numerically. In their open-questions section they explicitly identify closed-form spectral analysis of the reduced modal block as a remaining theoretical direction.

Ma and Yarats later compared QHM with AggMo and observed that an extended two-buffer AggMo with separate weights can recover QHM. Their discussion is about algorithmic equivalence and empirical damping rather than an exact Schur boundary for the original equal-weight multi-buffer method.

The present result resolves one sharply defined part of the earlier open spectral problem: the complete outer stability boundary has a closed form for every damping vector, even though the individual roots inside the disk generally do not. Focused searches for AggMo quadratic stability, harmonic-mean bounds, Schur criteria, unit-circle root loci, and closed learning-rate ceilings did not identify this formula.

## Limitations

The theorem gives the exact outer stability boundary, not the learning rate that minimizes the spectral radius. Interior root geometry and optimal convergence-rate tuning can still be nontrivial for \(K>1\).

The result assumes a common learning rate and equal averaging across buffers. The extended AggMo family with separate per-buffer learning rates has a different characteristic equation.

The objective Hessian is fixed and symmetric positive definite. Stochastic gradients, multiplicative noise, nonnormal linearizations, and nonquadratic effects are outside scope.

The harmonic-mean formula does not say that heterogeneous damping is useless. It only shows that passive damping cannot increase the absolute quadratic Schur ceiling beyond the largest single-buffer ceiling; improvements in oscillation suppression or convergence rate can still occur strictly inside that ceiling.

## References

1. James Lucas, Shengyang Sun, Richard Zemel, and Roger Grosse, “Aggregated Momentum: Stability Through Passive Damping,” arXiv:1804.00325v1, 2018.
2. Jerry Ma and Denis Yarats, “Quasi-hyperbolic momentum and Adam for deep learning,” arXiv:1810.06801v1, 2018.
