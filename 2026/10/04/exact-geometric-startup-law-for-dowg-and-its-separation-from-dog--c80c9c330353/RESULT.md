# Exact geometric startup law for DoWG and its separation from DoG
## Finding

Distance over Gradients (DoG) and Distance over Weighted Gradients (DoWG) are parameter-free methods whose adaptive scale is driven by distance from the initialization. On the cleanest coherent-subgradient problem, their distance-growth laws separate exactly.

Consider
\[
f(x)=G|x-D|,
\qquad
G>0,
\qquad
D>0,
\]
on the interval
\[
[0,D],
\]
with
\[
x_0=0
\]
and initial movement scale
\[
r_\varepsilon>0.
\]
Write
\[
R=\frac{D}{r_\varepsilon}.
\]
Until the minimizer is first reached, every subgradient is exactly
\[
g_t=-G.
\]
Projection at the crossing step sends the iterate to \(D\), so the first-hit index is determined by the unprojected pre-hit recurrence.

For DoG, the first update is
\[
x_1=r_\varepsilon.
\]
For every later pre-hit update,
\[
\overline r_t=x_t,
\qquad
\sum_{k=0}^{t}|g_k|^2=(t+1)G^2,
\]
so
\[
x_{t+1}
=
x_t\left(1+\frac1{\sqrt{t+1}}\right).
\]
Consequently, for \(n\ge1\),
\[
\frac{x_n}{r_\varepsilon}
=
\prod_{j=2}^{n}
\left(1+\frac1{\sqrt j}\right).
\]
Its logarithm satisfies
\[
\log\frac{x_n}{r_\varepsilon}
=
2\sqrt n
-
\frac12\log n
+
O(1).
\]
Thus DoG's startup distance grows at the stretched-exponential scale
\[
\frac{x_n}{r_\varepsilon}
=
\Theta\left(\frac{e^{2\sqrt n}}{\sqrt n}\right).
\]
If
\[
\tau_{\rm DoG}(R)
\]
denotes the number of updates required to first reach \(D\), then as \(R\to\infty\),
\[
\tau_{\rm DoG}(R)
=
\frac14(\log R)^2
+
O(\log R\,\log\log R).
\]

DoWG has a different exact growth law. Before the first hit, define
\[
y_t=\frac{x_t}{r_\varepsilon},
\qquad
S_t=1+\sum_{k=1}^{t}y_k^2,
\qquad
p_t=\frac{y_t}{\sqrt{S_t}}.
\]
The initial update again gives
\[
y_1=1,
\qquad
S_1=2,
\qquad
p_1=\frac1{\sqrt2}.
\]
DoWG's distance-squared weighting gives the exact recurrences
\[
y_{t+1}
=
y_t(1+p_t)
\]
and
\[
p_{t+1}
=
\frac{p_t(1+p_t)}
{\sqrt{1+p_t^2(1+p_t)^2}}.
\]

The sequence \(p_t\) increases to the unique positive root \(p_*\) of
\[
p^3+2p^2-2=0.
\]
Therefore
\[
\frac{y_{t+1}}{y_t}
\longrightarrow
\lambda
=
1+p_*
=
1.8392867552\ldots.
\]
Equivalently, \(\lambda\) is the positive root of
\[
\lambda^3-\lambda^2-\lambda-1=0.
\]
This is the Tribonacci constant.

The convergence of \(p_t\) to \(p_*\) is geometric. Hence there is a constant
\[
C_*>0
\]
such that
\[
y_t
=
C_*\lambda^{t-1}(1+o(1)).
\]
It follows that the DoWG first-hit count satisfies
\[
\tau_{\rm DoWG}(R)
=
\frac{\log R}{\log\lambda}
+
O(1),
\]
where
\[
\frac1{\log\lambda}
=
1.6410179299\ldots.
\]

Thus, on one common convex Lipschitz objective and one common initialization scale, DoWG changes the startup adaptation class: DoG needs quadratically many updates in \(\log R\), whereas DoWG needs only linearly many.

## Assumptions and scope

The DoG recurrence is the source distance-over-gradients rule
\[
\eta_t
=
\frac{\overline r_t}
{\sqrt{\sum_{k=0}^{t}\|g_k\|^2}},
\qquad
\overline r_t
=
\max\left(r_\varepsilon,\max_{k\le t}\|x_k-x_0\|\right).
\]

The DoWG recurrence is the source distance-over-weighted-gradients rule
\[
v_t
=
v_{t-1}
+
\overline r_t^2\|g_t\|^2,
\qquad
\eta_t
=
\frac{\overline r_t^2}{\sqrt{v_t}}.
\]

The objective is deterministic, one-dimensional, convex, and \(G\)-Lipschitz. The compact domain \([0,D]\) is compatible with the projected formulations. Only the startup phase before the first hit of the minimizer is analyzed.

The asymptotic comparison is taken as
\[
R=D/r_\varepsilon\to\infty.
\]
It measures how quickly each adaptive rule escapes an increasingly conservative initialization.

The theorem does not compare post-hit behavior, averaged iterates, noisy gradients, or general convergence rates.

## Proof

For DoG, while \(x_t<D\), the gradient is \(-G\) and the iterates increase. Hence
\[
\overline r_t=x_t
\]
for \(t\ge1\), while
\[
\sum_{k=0}^{t}|g_k|^2=(t+1)G^2.
\]
Therefore
\[
\eta_tG
=
\frac{x_t}{\sqrt{t+1}},
\]
which gives
\[
x_{t+1}
=
x_t\left(1+\frac1{\sqrt{t+1}}\right).
\]
The product formula follows by iteration from \(x_1=r_\varepsilon\).

Taking logarithms,
\[
\log\frac{x_n}{r_\varepsilon}
=
\sum_{j=2}^{n}
\log\left(1+j^{-1/2}\right).
\]
Uniform Taylor expansion gives
\[
\log(1+u)
=u-\frac{u^2}{2}+O(u^3)
\]
for \(u=j^{-1/2}\). Since
\[
\sum_{j=2}^{n}j^{-1/2}
=
2\sqrt n+O(1),
\]
\[
\sum_{j=2}^{n}j^{-1}
=
\log n+O(1),
\]
and
\[
\sum_{j=2}^{\infty}j^{-3/2}<\infty,
\]
we obtain
\[
\log\frac{x_n}{r_\varepsilon}
=
2\sqrt n-\frac12\log n+O(1).
\]
If \(L=\log R\), the first crossing therefore satisfies
\[
2\sqrt{\tau_{\rm DoG}}
=
L+O(\log L),
\]
which yields
\[
\tau_{\rm DoG}(R)
=
\frac14L^2+O(L\log L).
\]
Substituting \(L=\log R\) gives the stated form.

For DoWG, the source update at \(t=0\) gives
\[
x_1=r_\varepsilon.
\]
During the pre-hit phase,
\[
\overline r_t=x_t
\]
for \(t\ge1\), and
\[
v_t
=
G^2r_\varepsilon^2
\left(
1+
\sum_{k=1}^{t}y_k^2
\right)
=
G^2r_\varepsilon^2S_t.
\]
Hence
\[
x_{t+1}-x_t
=
\frac{x_t^2G}{Gr_\varepsilon\sqrt{S_t}}
=
r_\varepsilon\frac{y_t^2}{\sqrt{S_t}},
\]
so
\[
y_{t+1}
=
y_t(1+p_t).
\]
Moreover,
\[
S_{t+1}
=
S_t+y_{t+1}^2,
\]
which gives
\[
p_{t+1}
=
\frac{p_t(1+p_t)}
{\sqrt{1+p_t^2(1+p_t)^2}}.
\]

Let
\[
F(p)
=
\frac{p(1+p)}
{\sqrt{1+p^2(1+p)^2}}.
\]
For \(p>0\), direct squaring shows
\[
F(p)>p
\]
exactly when
\[
p^3+2p^2-2<0.
\]
The cubic is strictly increasing on \((0,\infty)\), so it has a unique positive root \(p_*\). Since
\[
p_1=1/\sqrt2
\]
and the cubic is negative there, while \(F\) is increasing, the sequence \(p_t\) is increasing and bounded above by \(p_*\). Its limit must therefore equal \(p_*\).

The derivative at the fixed point is
\[
F'(p_*)
=
\frac{1+2p_*}{(1+p_*)^3}
<1.
\]
Thus the fixed point is locally contracting, and monotone convergence implies
\[
\sum_{t=1}^{\infty}|p_t-p_*|<\infty.
\]
Using
\[
y_t
=
\prod_{k=1}^{t-1}(1+p_k)
\]
then shows that
\[
\frac{y_t}{(1+p_*)^{t-1}}
\]
converges to a positive finite constant \(C_*\). This proves the geometric asymptotic and the logarithmic first-hit law.

Finally, substituting
\[
\lambda=1+p_*
\]
into the fixed-point cubic gives
\[
\lambda^3-\lambda^2-\lambda-1=0.
\]

## Verification

The accompanying `verify.py` directly replays both source recurrences under a constant negative subgradient, checks the DoG product formula, checks the reduced DoWG one-dimensional map, encloses the positive cubic root, verifies monotone convergence of \(p_t\), and tests the predicted first-hit scaling over increasing values of \(R\).

The finite computations are transcription guards. The product formulas, fixed-point characterization, geometric convergence, and asymptotic hitting laws are proved above.

## Relationship to prior work

Ivgi, Hinder, and Carmon introduced DoG with a step size proportional to the largest observed distance from initialization and inversely proportional to the square root of accumulated squared gradient norms. Their paper notes empirically that the distance estimate can grow rapidly before stabilizing, but does not state the constant-subgradient product law or its stretched-exponential asymptotic.

Khaled, Mishchenko, and Jin introduced DoWG by weighting squared gradients with squared distance estimates. They explicitly motivate the change as more aggressive adaptation than DoG and prove a pointwise step-size comparison, while also cautioning that the two methods follow different trajectories after their first step, so pointwise step dominance alone does not determine their relative behavior.

A later DAoG study likewise describes DoWG as more aggressive and discusses the tradeoff between early acceleration and training stability. That work develops a new decayed adaptive rule rather than an exact constant-subgradient trajectory classification.

The present result supplies that missing trajectory-level comparison on a canonical coherent signal: DoG has stretched-exponential startup distance, whereas DoWG has an exact geometric ratio converging to the Tribonacci constant.

## Limitations

The comparison concerns a deterministic one-dimensional constant-subgradient startup phase.

The exact geometric constant is not claimed to govern DoWG on general smooth or stochastic objectives.

The result measures first-hit adaptation to an unknown distance scale, not final optimization accuracy or post-hit stability.

DoWG's faster startup on this example does not imply universal superiority; more aggressive adaptation can also reduce stability on other problems.

## References

1. Maor Ivgi, Oliver Hinder, and Yair Carmon, “DoG is SGD's Best Friend: A Parameter-Free Dynamic Step Size Schedule,” arXiv:2302.12022v1, 2023.
2. Ahmed Khaled, Konstantin Mishchenko, and Chi Jin, “DoWG Unleashed: An Efficient Universal Parameter-Free Gradient Descent Method,” arXiv:2305.16284v1, 2023.
3. “DAoG: decayed adaptation over gradients for parameter-free step size control,” Artificial Intelligence Review, 2025.
