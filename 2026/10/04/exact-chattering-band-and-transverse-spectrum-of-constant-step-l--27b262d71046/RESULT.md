# Exact chattering band and transverse spectrum of constant-step Lion
## Finding

Consider zero-weight-decay Lion with a constant learning rate on the scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0.
\]
Write the source Lion recurrence as
\[
c_t
=
\beta_1m_{t-1}
+
(1-\beta_1)\lambda x_t,
\]
\[
x_{t+1}
=
x_t
-
\eta\,\operatorname{sign}(c_t),
\]
\[
m_t
=
\beta_2m_{t-1}
+
(1-\beta_2)\lambda x_t,
\]
where
\[
\eta>0,
\qquad
0\le\beta_1,\beta_2<1.
\]

There is an exact continuum of strict alternating-sign period-two orbits if and only if
\[
2\beta_1<1+\beta_2.
\]

For every
\[
\frac{\beta_1}{1+\beta_2}\eta
<
a
<
\left(
1-\frac{\beta_1}{1+\beta_2}
\right)\eta,
\]
define
\[
x_A=a,
\qquad
x_B=a-\eta,
\]
and
\[
m_A
=
\lambda
\left(
a-\frac{\eta}{1+\beta_2}
\right),
\]
\[
m_B
=
\lambda
\left(
a-\frac{\beta_2\eta}{1+\beta_2}
\right).
\]
Then the state
\[
(x_A,m_A)
\]
maps to
\[
(x_B,m_B),
\]
and the next Lion step returns exactly to
\[
(x_A,m_A).
\]

The sign margins are
\[
c_A
=
\lambda
\left(
a-\frac{\beta_1\eta}{1+\beta_2}
\right)
>0,
\]
and
\[
c_B
=
\lambda
\left[
a-
\left(
1-\frac{\beta_1}{1+\beta_2}
\right)\eta
\right]
<0.
\]
Thus the orbit alternates between a positive and a negative sign update.

These are all strict alternating period-two orbits, up to reversing the phase. A two-cycle must move by one positive and one negative step of magnitude \(\eta\), which fixes the two parameter values; periodicity of the momentum recurrence then uniquely fixes \(m_A\) and \(m_B\), and the two sign inequalities give exactly the interval above.

The band is nonempty exactly when
\[
\frac{\beta_1}{1+\beta_2}
<
1-\frac{\beta_1}{1+\beta_2},
\]
equivalently
\[
2\beta_1<1+\beta_2.
\]

Every interior cycle is normally attracting. While its sign pattern remains fixed, one Lion step has state derivative
\[
A
=
\begin{bmatrix}
1&0\\
(1-\beta_2)\lambda&\beta_2
\end{bmatrix}.
\]
The two-step derivative is \(A^2\), whose eigenvalues are
\[
1
\qquad\text{and}\qquad
\beta_2^2.
\]
The unit multiplier is tangent to the continuum of cycles, while the momentum direction contracts by the exact factor
\[
\beta_2^2
\]
every two steps.

The objective does not approach zero on such a cycle. Its two-step time average is
\[
\frac{f(x_A)+f(x_B)}{2}
=
\frac{\lambda}{4}
\left[
a^2+(\eta-a)^2
\right]
=
\frac{\lambda}{2}
\left(
a-\frac{\eta}{2}
\right)^2
+
\frac{\lambda\eta^2}{8}.
\]
Hence even the best cycle in the family has the nonzero average floor
\[
\frac{\lambda\eta^2}{8},
\]
attained at the symmetric orbit
\[
x=\pm\frac{\eta}{2}.
\]

For the default Lion momentum coefficients
\[
\beta_1=0.9,
\qquad
\beta_2=0.99,
\]
the exact chattering band is
\[
0.4522613065\,\eta
<
a
<
0.5477386935\,\eta.
\]
The symmetric period-two orbit lies strictly inside this band, and the exact transverse two-step contraction is
\[
0.99^2=0.9801.
\]

## Assumptions and scope

The theorem uses the original Lion update with zero decoupled weight decay and constant learning rate.

The scalar quadratic is deterministic and strongly convex. The curvature \(\lambda\) affects the momentum values and the objective floor but cancels from the parameter-space chattering interval.

The result classifies strict alternating-sign period-two orbits. Boundary states where the sign input is exactly zero depend on the implementation convention for \(\operatorname{sign}(0)\) and are excluded.

Individual cycles are not asymptotically stable because they form a continuum. They are transversely attracting: nearby states that remain in the same alternating-sign sector keep their two-step parameter coordinate and contract their momentum discrepancy by \(\beta_2^2\).

The theorem does not analyze learning-rate decay, stochastic gradients, multidimensional coordinate coupling, or positive decoupled weight decay.

## Proof

Suppose a strict two-cycle uses a positive update sign at state \(A\) and a negative update sign at state \(B\).

Because each Lion parameter update has magnitude exactly \(\eta\),
\[
x_B=x_A-\eta,
\]
and the return step gives
\[
x_A=x_B+\eta.
\]
Write
\[
x_A=a,
\qquad
x_B=a-\eta.
\]

Momentum periodicity requires
\[
m_B
=
\beta_2m_A
+
(1-\beta_2)\lambda a,
\]
and
\[
m_A
=
\beta_2m_B
+
(1-\beta_2)\lambda(a-\eta).
\]
Solving these two equations gives
\[
m_A
=
\lambda
\left(
a-\frac{\eta}{1+\beta_2}
\right),
\]
and
\[
m_B
=
\lambda
\left(
a-\frac{\beta_2\eta}{1+\beta_2}
\right).
\]

The first sign input is
\[
c_A
=
\beta_1m_A
+
(1-\beta_1)\lambda a
=
\lambda
\left(
a-\frac{\beta_1\eta}{1+\beta_2}
\right).
\]
Thus \(c_A>0\) exactly when
\[
a
>
\frac{\beta_1\eta}{1+\beta_2}.
\]

The second sign input is
\[
c_B
=
\beta_1m_B
+
(1-\beta_1)\lambda(a-\eta)
=
\lambda
\left[
a-
\left(
1-\frac{\beta_1}{1+\beta_2}
\right)\eta
\right].
\]
Thus \(c_B<0\) exactly when
\[
a
<
\left(
1-\frac{\beta_1}{1+\beta_2}
\right)\eta.
\]

The two inequalities are simultaneously feasible exactly when
\[
2\beta_1<1+\beta_2.
\]
They also imply
\[
0<a<\eta,
\]
so the two parameter values straddle the minimizer.

Conversely, every \(a\) in the open interval makes both signs strict, and the displayed momentum pair then closes the orbit exactly. This proves existence and completeness of the family.

Inside a fixed sign sector, the sign output is locally constant. The one-step affine map therefore has derivative
\[
A
=
\begin{bmatrix}
1&0\\
(1-\beta_2)\lambda&\beta_2
\end{bmatrix}.
\]
The two-step derivative is \(A^2\), and because \(A\) is triangular its eigenvalues are \(1\) and \(\beta_2\). Hence the two-step multipliers are
\[
1
\quad\text{and}\quad
\beta_2^2.
\]

Finally,
\[
\frac{f(a)+f(a-\eta)}{2}
=
\frac{\lambda}{4}
\left[
a^2+(a-\eta)^2
\right].
\]
Completing the square gives the exact floor stated above.

## Verification

The accompanying `verify.py` reconstructs the source Lion recurrence, generates exact period-two states across several parameter choices, checks the sign margins, verifies completeness formulas, measures the transverse two-step multiplier, and reproduces the default chattering interval and objective floor.

The finite calculations are transcription guards. The continuum classification, the if-and-only-if parameter condition, and the Floquet multipliers are proved algebraically above.

## Relationship to prior work

Chen and coauthors introduced Lion as a sign-based optimizer that stores one momentum state and uses two different interpolation coefficients: one before the sign update and one for the persistent momentum. The defining paper emphasizes that the sign operation produces uniform update magnitude and therefore requires a smaller learning rate than Adam-like methods.

Chen, Liu, Liang, and Liu later gave continuous- and discrete-time Lyapunov analyses of Lion and the broader Lion family. Their theory explains Lion through constrained and composite optimization and develops convergence guarantees under its stated regimes.

The inspected defining paper contains no scalar quadratic, periodic-orbit, or cycle classification. The inspected later Lyapunov paper contains no occurrence of “periodic” or “cycle” and does not state the constant-step zero-weight-decay chattering band derived here.

The present finding isolates a discrete phenomenon created jointly by Lion's fixed-magnitude sign update and its asymmetric two-coefficient momentum rule: the algorithm can settle transversely onto a continuum of exact nonzero two-cycles even on the simplest strongly convex quadratic.

## Limitations

The result concerns a constant learning rate. Decaying schedules can shrink the chattering scale.

Zero decoupled weight decay is assumed. Positive weight decay changes the parameter map and can destroy the exact continuum.

The theorem is scalar. In higher dimensions, each coordinate has a sign update but shares the same training schedule and may interact through the Hessian.

The periodic family is a local asymptotic description once an alternating-sign sector is reached; no global basin classification is claimed.

## References

1. Xiangning Chen, Chen Liang, Da Huang, Esteban Real, Kaiyuan Wang, Yao Liu, Hieu Pham, Xuanyi Dong, Thang Luong, Cho-Jui Hsieh, Yifeng Lu, and Quoc V. Le, “Symbolic Discovery of Optimization Algorithms,” arXiv:2302.06675v1, 2023.
2. Lizhang Chen, Bo Liu, Kaizhao Liang, and Qiang Liu, “Lion Secretly Solves Constrained Optimization: As Lyapunov Predicts,” arXiv:2310.05898v1, 2023.
