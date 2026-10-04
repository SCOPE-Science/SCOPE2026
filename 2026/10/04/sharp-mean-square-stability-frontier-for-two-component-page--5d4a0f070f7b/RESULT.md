# Sharp mean-square stability frontier for two-component PAGE
## Finding

Consider the two-component scalar finite sum
\[
f_\sigma(x)
=
\frac{\mu(1+\sigma h)}{2}x^2-\sigma c x,
\qquad
\sigma\in\{-1,+1\},
\]
where
\[
\mu>0,\qquad 0\le h<1,
\]
and \(c\) is arbitrary. Uniform averaging gives
\[
f(x)=\frac{\mu}{2}x^2,
\]
so the unique minimizer is \(x^\star=0\). When \(c\ne0\), the component gradients need not vanish at \(x^\star\).

Run PAGE with full-batch refresh size \(b=2\), recursive minibatch size \(b'=1\), constant stepsize \(\eta>0\), and the probability prescribed by the original PAGE formula,
\[
p=\frac{b'}{b+b'}=\frac13.
\]
Thus
\[
x_{t+1}=x_t-\eta g_t.
\]
With probability \(1/3\),
\[
g_{t+1}=\nabla f(x_{t+1}),
\]
while with probability \(2/3\), an independent uniform component \(\sigma_t\in\{-1,+1\}\) is sampled and
\[
g_{t+1}
=
g_t+
\nabla f_{\sigma_t}(x_{t+1})
-
\nabla f_{\sigma_t}(x_t).
\]

Put
\[
\alpha=\eta\mu.
\]
Then the exact mean-square stability frontier is
\[
0<\alpha<\alpha_\star(h),
\]
where
\[
\alpha_\star(h)
=
\frac{3+\sqrt{25+32h^2}}
{4(1+2h^2)}.
\]
Equivalently, the exact lifted second-moment operator is Schur stable precisely on this interval.

At
\[
\alpha=\alpha_\star(h),
\]
that operator has eigenvalue \(1\). For every larger positive \(\alpha\), it is not Schur stable.

The threshold does not depend on \(c\). It interpolates between
\[
\alpha_\star(0)=2
\]
and
\[
\lim_{h\uparrow1}\alpha_\star(h)
=
\frac{3+\sqrt{57}}{12}
\approx0.87915.
\]

The comparison with the original PAGE theorem is concrete. On this family the average-smoothness constant used there is
\[
L_{\rm av}=\mu\sqrt{1+h^2}.
\]
Its general sufficient stepsize condition, specialized to \(p=1/3\) and \(b'=1\), gives
\[
\alpha
\le
\frac{1}
{\sqrt{1+h^2}(1+\sqrt2)}.
\]
The exact scalar mean-square frontier above is strictly larger. Likewise, the earlier Loopless-SARAH analysis of the equivalent probabilistic recursive estimator uses a sufficient convex stepsize below \(1/L_{\max}\), where
\[
L_{\max}=\mu(1+h).
\]
These are sufficient general-purpose guarantees, not exact stability boundaries for the present heterogeneous two-component model.

## Assumptions and scope

The theorem uses the PAGE update in which the parameter is stepped first and the gradient estimator is then either refreshed at the new point or recursively corrected using the same sampled component at the old and new points.

The refresh batch contains both components, while the recursive branch samples one component. The refresh probability is fixed at \(1/3\), the value obtained from the original PAGE prescription \(p=b'/(b+b')\) when \(b=2\) and \(b'=1\).

Mean-square stability refers to the complete random linear state \((x_t,g_t/\mu)\). It is equivalent to Schur stability of the exact second-moment lifting. The standard PAGE initialization \(g_0=\nabla f(x_0)\) is included, but the lifted stability statement is for arbitrary square-integrable initial state.

No claim is made for other refresh probabilities, larger minibatches, nonquadratic objectives, multidimensional noncommuting Hessians, proximal variants, or time-varying stepsizes.

## Proof

Scale the estimator by
\[
y_t=\frac{g_t}{\mu}.
\]
The position update is
\[
x_{t+1}=x_t-\alpha y_t.
\]
A full refresh gives
\[
y_{t+1}=x_{t+1}.
\]
On the recursive branch,
\[
\nabla f_{\sigma}(x_{t+1})
-
\nabla f_{\sigma}(x_t)
=
\mu(1+\sigma h)(x_{t+1}-x_t),
\]
so the offset \(c\) cancels exactly and
\[
y_{t+1}
=
\left[1-\alpha(1+\sigma_t h)\right]y_t.
\]

Define the second moments
\[
X_t=\mathbb E[x_t^2],
\qquad
Y_t=\mathbb E[x_ty_t],
\qquad
Z_t=\mathbb E[y_t^2].
\]
Averaging over the refresh coin and the independent component sign gives
\[
\begin{bmatrix}
X_{t+1}\\
Y_{t+1}\\
Z_{t+1}
\end{bmatrix}
=
N(\alpha,h)
\begin{bmatrix}
X_t\\
Y_t\\
Z_t
\end{bmatrix},
\]
where
\[
N(\alpha,h)
=
\begin{bmatrix}
1&-2\alpha&\alpha^2\\
\frac13&\frac{2-4\alpha}{3}&\frac{3\alpha^2-2\alpha}{3}\\
\frac13&-\frac{2\alpha}{3}&
\frac{2-4\alpha+3\alpha^2+2\alpha^2h^2}{3}
\end{bmatrix}.
\]

Write
\[
H=h^2.
\]
The characteristic polynomial
\[
P(z)=\det(zI-N)
=
z^3+c_1z^2+c_2z+c_3
\]
has
\[
c_1
=
-\left(1+\frac{2H}{3}\right)\alpha^2
+\frac{8\alpha}{3}
-\frac73,
\]
\[
c_2
=
-\left(\frac23+\frac{8H}{9}\right)\alpha^3
+
\left(\frac83+\frac{10H}{9}\right)\alpha^2
-
\frac{34\alpha}{9}
+
\frac{16}{9},
\]
and
\[
c_3
=
\frac{4(\alpha-1)}{9}
\left[(\alpha-1)^2+H\alpha^2\right].
\]

For a monic real cubic, the Jury conditions are
\[
|c_3|<1,
\]
\[
1+c_1+c_2+c_3>0,
\]
\[
1-c_1+c_2-c_3>0,
\]
and
\[
J:=1-c_2+c_1c_3-c_3^2>0.
\]

The second condition is the binding one:
\[
1+c_1+c_2+c_3
=
\frac{\alpha}{9}
\left[
2+3\alpha-2(1+2H)\alpha^2
\right].
\]
For positive \(\alpha\), this is positive exactly when
\[
0<\alpha<
\frac{3+\sqrt{25+32H}}
{4(1+2H)}.
\]

It remains to show that the other Jury inequalities stay strict throughout this interval.

First, the binding inequality implies \(\alpha<2\). For \(0<\alpha\le1\),
\[
|c_3|
\le
\frac49.
\]
For \(1<\alpha<2\), the binding inequality gives
\[
H
<
H_{\max}(\alpha)
:=
\frac{2+3\alpha-2\alpha^2}{4\alpha^2}.
\]
Hence
\[
(\alpha-1)^2+H\alpha^2
<
\frac{2\alpha^2-5\alpha+6}{4}
<1,
\]
and again \(|c_3|<4/9\).

Next,
\[
1-c_1+c_2-c_3
=
\frac{
50-70\alpha+45\alpha^2-10\alpha^3
+
4H\alpha^2(5-3\alpha)
}{9}.
\]
If \(\alpha\le5/3\), its \(H\)-coefficient is nonnegative, and the \(H=0\) value is
\[
\frac{
5(5-2\alpha)\left[(\alpha-1)^2+1\right]
}{9}>0.
\]
If \(5/3<\alpha<2\), the expression decreases with \(H\), so the binding upper bound \(H<H_{\max}(\alpha)\) reduces the check to
\[
-4\alpha^3+26\alpha^2-61\alpha+60>0.
\]
Its derivative is negative for every real \(\alpha\), and its value at \(\alpha=2\) is \(10\), so it is positive on the required interval.

For the final Jury quantity, direct algebra gives
\[
\frac{\partial^2J}{\partial H^2}
=
-\frac{16\alpha^4(\alpha-1)(2\alpha+1)}{81}.
\]
When \(1\le\alpha<2\), \(J\) is concave in \(H\). Its endpoint values are
\[
J(\alpha,0)
=
-\frac{
(4\alpha+5)(2\alpha^2-4\alpha-1)
(2\alpha^3-6\alpha^2+6\alpha+1)
}{81}>0
\]
and
\[
J(\alpha,H_{\max})
=
-\frac{
\alpha(4\alpha^2-2\alpha-17)
(2\alpha^3-7\alpha^2+11\alpha+3)
}{162}>0.
\]
Thus \(J>0\) throughout the admissible interval.

When \(0<\alpha<1\),
\[
\frac{\partial J}{\partial H}
=
-\frac{2\alpha^2}{81}B(\alpha,H),
\]
where
\[
B(\alpha,H)
=
16H\alpha^4-8H\alpha^3-8H\alpha^2
+
16\alpha^4-34\alpha^3-6\alpha^2+26\alpha+7.
\]
The coefficient of \(H\) in \(B\) is negative, and
\[
B(\alpha,1)
=
7(1-\alpha)^4
+
54\alpha(1-\alpha)^3
+
106\alpha^2(1-\alpha)^2
+
36\alpha^3(1-\alpha)
+
9\alpha^4
>0.
\]
Therefore \(J\) decreases with \(H\) on \(0\le H\le1\). Its minimum is bounded below by
\[
J(\alpha,1)
=
\frac{1}{81}
\Big[
5(1-\alpha)^6
+
84\alpha(1-\alpha)^5
+
451\alpha^2(1-\alpha)^4
+
906\alpha^3(1-\alpha)^3
+
761\alpha^4(1-\alpha)^2
+
354\alpha^5(1-\alpha)
+
63\alpha^6
\Big]
>0.
\]

All four Jury inequalities therefore hold exactly on the claimed interval. At equality,
\[
P(1)=0,
\]
so \(1\) is an eigenvalue of the second-moment operator. Above the positive root, \(P(1)<0\), which is incompatible with Schur stability.

For an i.i.d. random linear system, Schur stability of the lifted second-moment operator is equivalent to exponential mean-square stability. This completes the proof.

## Verification

The accompanying `verify.py` reconstructs all PAGE branches from the stated component functions, verifies the exact second-moment matrix by branch enumeration, checks the characteristic-coefficient identities, evaluates all four Jury inequalities on a dense deterministic grid below and above the analytic frontier, and confirms the threshold endpoint values.

The grid is only a transcription guard. The necessary-and-sufficient result follows from the exact moment recursion and the analytic Jury proof above.

## Relationship to prior work

Li, Ma, and Giannakis introduced Loopless SARAH in 2019. Its recursive estimator with probabilistic full-gradient refresh is algorithmically equivalent to the full-batch PAGE specialization used here after matching the refresh probability. Their analysis controls estimator mean-square error and proves convergence under sufficient stepsize conditions, but the inspected full text does not give a two-component exact lifted stability phase diagram.

Li et al. introduced PAGE independently and generalized the probabilistic switch to arbitrary minibatch sizes. For \(b=2\) and \(b'=1\), their stated probability formula gives \(p=1/3\), exactly the specialization analyzed here. Their finite-sum theorem uses a sufficient average-smoothness stepsize and does not state the radical stability frontier.

Condat and Richtárik later developed a sharper Lyapunov analysis of PAGE for weakly convex finite sums. Their convex and PŁ results allow much larger steps than the original general nonconvex analysis, but the inspected article does not contain a scalar quadratic, a second-moment spectral calculation, or a necessary-and-sufficient stability boundary.

Targeted searches over both PAGE and Loopless-SARAH aliases, scalar quadratics, second moments, spectral radii, Schur/Jury stability, and the closed-form radical did not identify the present formula.

## Limitations

The theorem fixes two scalar components, full-batch refresh, one-sample recursive correction, and \(p=1/3\). It does not classify arbitrary refresh probability or minibatch size.

The component Hessians commute because the model is scalar. Higher-dimensional noncommuting Hessians can produce different lifted dynamics.

The claim concerns exponential mean-square stability, not monotonic decrease on every sample path.

The exact independence from \(c\) comes from cancellation of affine component offsets in both the full gradient and the recursive gradient difference. More general noninterpolation structure need not cancel.

Equivalent random-linear-system calculations may exist in older stochastic-approximation or control literature under terminology unrelated to PAGE or Loopless SARAH; this is the principal residual originality risk.

## References

1. Bingcong Li, Meng Ma, and Georgios B. Giannakis, “On the Convergence of SARAH and Beyond,” arXiv:1906.02351v1, 2019.
2. Zhize Li, Hongyan Bao, Xiangliang Zhang, and Peter Richtárik, “PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization,” arXiv:2008.10898v1, 2020; ICML 2021.
3. Laurent Condat and Peter Richtárik, “Convergence Analysis of the ProbAbilistic Gradient Estimator Algorithm for Weakly Convex Finite-Sum Optimization,” Journal of Optimization Theory and Applications 210, article 33, 2026, DOI:10.1007/s10957-026-03065-4.
