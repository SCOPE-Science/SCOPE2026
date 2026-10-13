# AdaNorm has a sharp two-level gradient-contrast cap
## Finding

AdaNorm was introduced as a generic wrapper that uses an exponential moving average of past gradient norms to boost a current gradient when its norm is atypically small. On the simplest persistent heterogeneous pattern—alternating large and small gradient norms—the wrapper has an exact closed-form response and a sharp contrast ceiling.

Let
\[
0<\gamma<1,
\qquad
e_0=0,
\]
and define the AdaNorm historical norm by
\[
e_t
=
\gamma e_{t-1}
+
(1-\gamma)\|g_t\|_2.
\]
The corrected gradient is
\[
s_t
=
\begin{cases}
\dfrac{e_t}{\|g_t\|_2}g_t,
&
e_t>\|g_t\|_2,
\\[1ex]
g_t,
&
e_t\le\|g_t\|_2.
\end{cases}
\]

Assume only that the gradient norms alternate:
\[
\|g_{2n-1}\|_2=A,
\qquad
\|g_{2n}\|_2=B,
\qquad
A>B>0.
\]
The gradient directions themselves may vary arbitrarily.

Define
\[
E_A
=
\frac{A+\gamma B}{1+\gamma},
\qquad
E_B
=
\frac{\gamma A+B}{1+\gamma}.
\]
Then for every
\[
n\ge1,
\]
the historical norm is exactly
\[
\boxed{
e_{2n}
=
E_B(1-\gamma^{2n})
}
\]
and
\[
\boxed{
e_{2n-1}
=
E_A-E_B\gamma^{2n-1}
}.
\]

Because
\[
E_A<A,
\]
every high-norm step satisfies
\[
e_{2n-1}<A
\]
and is therefore never corrected.

By contrast,
\[
E_B>B,
\]
so all sufficiently late low-norm steps are corrected. Their first correction occurs at the unique smallest integer
\[
N\ge1
\]
such that
\[
\gamma^{2N}
<
\frac{\gamma(A-B)}{\gamma A+B}.
\]
Equivalently,
\[
\boxed{
N
=
\left\lfloor
\frac{
\log\!\left(\gamma(A-B)/(\gamma A+B)\right)
}{
2\log\gamma
}
\right\rfloor
+
1
}.
\]

For every
\[
n\ge N,
\]
the low-norm corrected gradient has norm
\[
\|s_{2n}\|_2=e_{2n},
\]
which increases monotonically to
\[
E_B
=
\frac{\gamma A+B}{1+\gamma}.
\]

Hence the asymptotic corrected high-to-low norm contrast is
\[
\mathcal C_\gamma(q)
=
\frac{A}{E_B}
=
\frac{(1+\gamma)q}{\gamma q+1},
\qquad
q=\frac AB>1.
\]
This function is strictly increasing in the raw contrast \(q\), but it is uniformly bounded:
\[
\boxed{
1
<
\mathcal C_\gamma(q)
<
\frac{1+\gamma}{\gamma}
}.
\]
The upper bound is sharp because
\[
\lim_{q\to\infty}
\mathcal C_\gamma(q)
=
\frac{1+\gamma}{\gamma}.
\]

Thus AdaNorm converts arbitrarily large persistent two-level norm contrast into a bounded contrast determined only by its EMA parameter.

At the paper's main experimental choice
\[
\gamma=0.95=\frac{19}{20},
\]
the universal cap is
\[
\frac{1+\gamma}{\gamma}
=
\frac{39}{19}
=
2.052631578947\ldots.
\]
Equivalently, even if the low raw norm tends to zero relative to the high norm, its asymptotic corrected norm tends to
\[
\frac{\gamma}{1+\gamma}A
=
\frac{19}{39}A
=
0.487179487179\ldots A.
\]

For example, if
\[
A/B=100
\]
and
\[
\gamma=0.95,
\]
the first low step is already corrected and the asymptotic contrast is only
\[
2.03125,
\]
rather than \(100\).

## Assumptions and scope

The theorem concerns the generic AdaNorm norm-correction front end:
\[
e_t
=
\gamma e_{t-1}
+
(1-\gamma)\|g_t\|_2
\]
followed by norm boosting when
\[
e_t>\|g_t\|_2.
\]

The result is independent of the optimizer that receives the corrected gradient. In particular, it does not require Adam, diffGrad, RAdam, or AdaBelief.

The gradient directions may be arbitrary; only their norms are constrained to the two-level alternating pattern.

The source paper applies the corrected gradient to the first moment while leaving Adam's second moment on the raw gradient. The theorem does not claim that every host optimizer's final parameter update has the same contrast bound.

The case
\[
\gamma=0
\]
is excluded because then
\[
e_t=\|g_t\|_2
\]
and AdaNorm never boosts the current gradient.

## Proof

The even subsequence obeys a scalar affine two-step recurrence. Processing a high norm and then a low norm gives
\[
e_{2n}
=
\gamma^2 e_{2n-2}
+
(1-\gamma)(\gamma A+B).
\]
Its fixed point is
\[
\frac{
(1-\gamma)(\gamma A+B)
}{
1-\gamma^2
}
=
\frac{\gamma A+B}{1+\gamma}
=
E_B.
\]
Since
\[
e_0=0,
\]
the exact solution is
\[
e_{2n}
=
E_B(1-\gamma^{2n}).
\]

For the odd subsequence,
\[
e_{2n-1}
=
\gamma e_{2n-2}
+
(1-\gamma)A.
\]
Substituting the even formula and using
\[
E_A
=
\gamma E_B+(1-\gamma)A
\]
gives
\[
e_{2n-1}
=
E_A-E_B\gamma^{2n-1}.
\]

Since
\[
A-E_A
=
\frac{\gamma(A-B)}{1+\gamma}
>
0,
\]
the high steps always satisfy
\[
e_{2n-1}<A.
\]
They are never corrected.

For the low steps,
\[
E_B-B
=
\frac{\gamma(A-B)}{1+\gamma}
>
0.
\]
Moreover \(e_{2n}\) increases strictly to \(E_B\), so there is a unique first corrected low step. The inequality
\[
e_{2n}>B
\]
is equivalent to
\[
E_B(1-\gamma^{2n})>B,
\]
hence
\[
\gamma^{2n}
<
1-\frac{B}{E_B}
=
\frac{\gamma(A-B)}{\gamma A+B}.
\]
Because
\[
0<\gamma<1,
\]
taking logarithms yields the stated smallest integer \(N\).

Once correction is active,
\[
\|s_{2n}\|_2=e_{2n}.
\]
Taking \(n\to\infty\) gives the limiting low corrected norm \(E_B\).

Finally, writing
\[
q=A/B
\]
gives
\[
\mathcal C_\gamma(q)
=
\frac{(1+\gamma)q}{\gamma q+1}.
\]
Differentiation yields
\[
\mathcal C_\gamma'(q)
=
\frac{1+\gamma}{(\gamma q+1)^2}
>
0.
\]
Its limit as
\[
q\to\infty
\]
is
\[
(1+\gamma)/\gamma,
\]
which proves both monotonicity and sharpness of the universal cap.

## Verification

The accompanying `verify.py` replays the AdaNorm historical-norm recurrence for randomized \(A\), \(B\), and \(\gamma\), checks both exact subsequence formulas, verifies the first-correction index, and checks the contrast bound and the \(\gamma=0.95\) constants.

The finite computations are transcription guards. The exact formulas, onset index, monotonicity, and sharp cap are proved algebraically above.

## Relationship to prior work

Dubey, Singh, and Chaudhuri introduced AdaNorm to correct low and atypical batch-gradient norms using an exponential moving average of historical gradient norms. Their method is deliberately generic and is attached in the paper to Adam, diffGrad, RAdam, and AdaBelief.

The source defines
\[
e_t
=
\gamma e_{t-1}
+
(1-\gamma)\|g_t\|_2
\]
and boosts the current gradient to norm \(e_t\) whenever \(e_t\) exceeds the current norm. It explains the mechanism through flat, steep, and narrow-valley scenarios and reports experiments using
\[
\gamma=0.95.
\]

The inspected source does not state the exact response to an alternating two-level norm sequence, the finite onset index for low-gradient correction, or the sharp contrast cap
\[
(1+\gamma)/\gamma.
\]
Focused published-record and web searches for AdaNorm periodic gradients, alternating gradient norms, two-cycle behavior, and exact norm-contrast bounds did not identify an implication-equivalent result.

The theorem quantifies the paper's intended low-gradient correction directly at the wrapper level. It therefore applies before any host optimizer-specific momentum or adaptive denominator is introduced.

## Limitations

The result concerns a persistent two-level norm pattern. More general nonperiodic sequences can have different transient behavior.

The theorem bounds the contrast of the corrected gradients, not necessarily the contrast of final parameter updates after a host optimizer's momentum and second-moment processing.

The directions of the two alternating gradients do not affect the norm law, but they can affect the host optimizer.

The sharp cap is an asymptotic persistent-pattern statement, not a guarantee on the first few iterations.

## References

1. Shiv Ram Dubey, Satish Kumar Singh, and Bidyut Baran Chaudhuri, “AdaNorm: Adaptive Gradient Norm Correction based Optimizer for CNNs,” arXiv:2210.06364v1, 2022; IEEE/CVF Winter Conference on Applications of Computer Vision, 2023.
