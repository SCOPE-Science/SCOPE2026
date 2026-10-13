# Filter-wise ASAM hides a squared-condition-number mixed-mode one-step barrier
## Finding

Adaptive Sharpness-Aware Minimization (ASAM) modifies the perturbation geometry of sharpness-aware training by using a parameter-dependent normalization. For the source's filter-wise normalization, one filter block with parameter vector \(x\) has
\[
T_x=(\|x\|+\tau)I,
\]
where \(\tau\ge0\) denotes the small additive stabilizer used by the source for numerical stability. The source denotes that stabilizer differently; \(\tau\) is used here to avoid collision with the outer learning rate.

For \(p=2\), the source perturbation becomes
\[
\epsilon(x)
=
\rho
\frac{T_x^2\nabla f(x)}
{\|T_x\nabla f(x)\|}
=
\rho(\|x\|+\tau)
\frac{\nabla f(x)}{\|\nabla f(x)\|}.
\]

Consider the positive quadratic
\[
f_\kappa(x)
=
\frac12(x_1^2+\kappa x_2^2),
\qquad
\kappa>1,
\]
with
\[
A=\operatorname{diag}(1,\kappa),
\qquad
\nabla f_\kappa(x)=Ax.
\]
With no weight decay and a constant outer learning rate \(\alpha>0\), one deterministic ASAM step is
\[
x^+
=
x-\alpha A(x+\epsilon(x)).
\]

Define the unit vector
\[
v_\kappa
=
\left(
\sqrt{1-\kappa^{-2}},
\kappa^{-1}
\right).
\]
Its high-curvature parameter component is only \(1/\kappa\), but its gradient is
\[
Av_\kappa
=
\left(
\sqrt{1-\kappa^{-2}},
1
\right),
\]
so the two gradient coordinates are comparable. This is the mixed mode of interest.

For
\[
x=Rv_\kappa,
\qquad
R>0,
\]
write
\[
s_R=1+\frac{\tau}{R},
\qquad
r_\kappa=\sqrt{2-\kappa^{-2}},
\]
and
\[
m_1=1+\kappa^{-1}-\kappa^{-2},
\]
\[
m_2=2-\kappa^{-2},
\]
\[
m_3=\kappa+1-\kappa^{-2},
\]
\[
m_4=\kappa^2+1-\kappa^{-2}.
\]
Then the exact one-step squared Euclidean ratio is
\[
\boxed{
\frac{\|x^+\|^2}{\|x\|^2}
=
1-2\alpha A_{\kappa,R}
+\alpha^2B_{\kappa,R},
}
\]
where
\[
\boxed{
A_{\kappa,R}
=
m_1+\rho s_R r_\kappa
}
\]
and
\[
\boxed{
B_{\kappa,R}
=
m_2
+
\frac{2\rho s_Rm_3}{r_\kappa}
+
\frac{\rho^2s_R^2m_4}{m_2}.
}
\]

Because both coefficients are positive, this state contracts in Euclidean norm if and only if
\[
\boxed{
0<\alpha<
\alpha_{\kappa,R}
:=
\frac{2A_{\kappa,R}}{B_{\kappa,R}}.
}
\]
It is norm-neutral at equality and expands for every larger positive step.

The stabilizer disappears at large parameter scale:
\[
s_R\longrightarrow1
\qquad
(R\to\infty).
\]
The resulting threshold obeys
\[
\boxed{
\kappa^2\alpha_{\kappa,\infty}
\longrightarrow
C_\rho
:=
\frac{4(1+\rho\sqrt2)}{\rho^2}.
}
\]
Thus this mixed mode imposes a one-step scale of order
\[
\kappa^{-2}.
\]

Pure eigendirections look much safer. For \(x=Re_2\), the exact multiplier is
\[
1-\alpha\kappa\left[1+\rho\left(1+\frac{\tau}{R}\right)\right],
\]
so the large-radius top-eigenvector contraction threshold is
\[
\boxed{
\frac{2}{\kappa(1+\rho)}.
}
\]
The bottom eigendirection has the still larger threshold
\[
\frac{2}{1+\rho}.
\]

Consequently, fix any
\[
\rho>0
\]
and any
\[
c>C_\rho.
\]
Choose
\[
\alpha=\frac{c}{\kappa^2}.
\]
For all sufficiently large \(\kappa\), both pure eigendirections contract, while for all sufficiently large \(\kappa\) and \(R\), the balanced-gradient mixed state expands after one ASAM step.

The obstruction is therefore not visible from axis-aligned tests. The filter-wise perturbation turns a parameter component of size \(1/\kappa\) into an order-one gradient component, and the outer Hessian action applies another factor of \(\kappa\). This is the mechanism behind the extra condition-number factor.

## Assumptions and scope

The result uses the source's deterministic \(p=2\) ASAM perturbation, the source filter-wise normalization, and the source additive normalization stabilizer. The stabilizer is renamed \(\tau\).

There is one filter block containing both coordinates. The objective is the strictly convex two-dimensional quadratic
\[
f_\kappa(x)=\frac12(x_1^2+\kappa x_2^2).
\]

There is no momentum, stochastic gradient noise, weight decay, or learning-rate schedule. Those mechanisms are deliberately excluded so the geometric effect of filter-wise ASAM can be isolated.

The theorem classifies one-step Euclidean contraction for a natural mixed state and compares it with pure eigendirections. It does not claim that one expanding step implies asymptotic divergence, nor does it classify the full nonlinear ASAM orbit.

## Proof

Because
\[
\|v_\kappa\|=1,
\]
the chosen state has
\[
\|x\|=R.
\]
Also,
\[
Av_\kappa
=
\left(
\sqrt{1-\kappa^{-2}},
1
\right),
\]
hence
\[
\|Av_\kappa\|
=
r_\kappa.
\]

The stabilized one-filter perturbation is
\[
\epsilon(Rv_\kappa)
=
\rho(R+\tau)
\frac{Av_\kappa}{r_\kappa}
=
\rho R s_R
\frac{Av_\kappa}{r_\kappa}.
\]
Therefore
\[
\frac{x^+}{R}
=
v_\kappa
-
\alpha Av_\kappa
-
\alpha\rho s_R
\frac{A^2v_\kappa}{r_\kappa}.
\]

The required inner products are
\[
v_\kappa^\top Av_\kappa=m_1,
\]
\[
v_\kappa^\top A^2v_\kappa=m_2=r_\kappa^2,
\]
\[
(Av_\kappa)^\top A^2v_\kappa=m_3,
\]
and
\[
\|A^2v_\kappa\|^2=m_4.
\]
Expanding the squared norm gives
\[
\frac{\|x^+\|^2}{\|x\|^2}
=
1
-
2\alpha
\left(
m_1+\rho s_Rr_\kappa
\right)
+
\alpha^2
\left(
m_2
+
\frac{2\rho s_Rm_3}{r_\kappa}
+
\frac{\rho^2s_R^2m_4}{m_2}
\right),
\]
which proves the exact ratio.

For \(\alpha>0\), strict contraction is equivalent to
\[
-2\alpha A_{\kappa,R}
+
\alpha^2B_{\kappa,R}
<0.
\]
Since
\[
A_{\kappa,R}>0,
\qquad
B_{\kappa,R}>0,
\]
this is equivalent to
\[
0<\alpha<\frac{2A_{\kappa,R}}{B_{\kappa,R}}.
\]

Now let
\[
R\to\infty.
\]
Then
\[
s_R\to1.
\]
As
\[
\kappa\to\infty,
\]
the numerator of the threshold tends to
\[
2(1+\rho\sqrt2),
\]
while its denominator satisfies
\[
B_{\kappa,\infty}
=
\frac{\rho^2}{2}\kappa^2+O(\kappa).
\]
Therefore
\[
\kappa^2\alpha_{\kappa,\infty}
\to
\frac{4(1+\rho\sqrt2)}{\rho^2}.
\]

For \(x=Re_2\), the gradient and perturbation are collinear:
\[
\epsilon(x)
=
\rho(R+\tau)e_2.
\]
Hence
\[
x^+
=
R
\left[
1-\alpha\kappa
\left(
1+\rho\left(1+\frac{\tau}{R}\right)
\right)
\right]e_2.
\]
The corresponding exact contraction threshold is
\[
\frac{2}
{\kappa[1+\rho(1+\tau/R)]},
\]
which tends to
\[
\frac{2}{\kappa(1+\rho)}
\]
as \(R\to\infty\). The same calculation for \(e_1\) removes the factor \(\kappa\).

Finally choose
\[
c>C_\rho
\]
and
\[
\alpha=\frac{c}{\kappa^2}.
\]
The mixed-state threshold satisfies
\[
\kappa^2\alpha_{\kappa,\infty}\to C_\rho<c,
\]
so the mixed state is eventually expansive. The pure top-eigenvector condition requires only
\[
\frac{c}{\kappa^2}
<
\frac{2}{\kappa(1+\rho)},
\]
which holds for all sufficiently large \(\kappa\); the bottom eigenvector condition is weaker still. Continuity in \(s_R\) then gives the same separation for all sufficiently large finite \(R\).

## Verification

The accompanying `verify.py` reconstructs the source one-filter ASAM step directly.

It checks the closed one-step ratio against direct coordinate updates, verifies the exact contraction threshold, confirms the large-\(\kappa\) constant
\[
C_\rho=\frac{4(1+\rho\sqrt2)}{\rho^2},
\]
and checks explicit parameter choices where both pure eigendirections contract but the balanced-gradient state expands.

The computations are transcription and asymptotic guards. The exact formulas, if-and-only-if one-step threshold, and asymptotic separation are proved above.

## Relationship to prior work

Kwon and coauthors introduce ASAM to make sharpness-aware training adaptive to parameter scale. Their filter-wise normalization assigns each filter a norm-based scaling, and their practical implementation adds a small identity term to that scaling for stability. Their \(p=2\) algorithm uses the normalized perturbation
\[
\rho
\frac{T_w^2\nabla L(w)}
{\|T_w\nabla L(w)\|}.
\]
The source develops the scale-invariance motivation, generalization analysis, and empirical tuning of the perturbation radius and stabilizer. The inspected paper does not state a condition-number-dependent quadratic one-step stability frontier or compare pure eigendirections with a balanced-gradient mixed mode.

A later analysis of standard, fixed-radius SAM studies convex quadratics and explains oscillatory or bouncing behavior near sharp directions. That work concerns a different perturbation geometry: fixed-radius SAM uses a perturbation whose Euclidean magnitude does not grow proportionally to \(\|x\|\). Filter-wise ASAM with one block is homogeneous when \(\tau=0\), and the mixed-mode calculation above depends on that state-proportional radius. The fixed-radius results therefore do not imply the squared-condition-number one-step obstruction proved here.

Focused published-record searches for ASAM quadratic stability, filter-wise mixed modes, the normalization stabilizer, condition-number scaling, and equivalent cycle or nonexpansion formulations did not identify an implication-equivalent result.

## Limitations

This is a one-step Euclidean norm result, not a global convergence theorem.

The objective is a two-dimensional positive quadratic and there is exactly one filter block.

The mixed vector is chosen because its two gradient coordinates are comparable; no claim is made that it is the globally worst direction over all states.

Momentum, stochasticity, weight decay, multiple filter blocks, and scheduled learning rates may change the full dynamics.

The large-\(R\) limit shows that the source stabilizer cannot remove this mechanism uniformly over parameter scale; it does not imply that the stabilizer is ineffective in finite-scale training.

## References

1. Jungmin Kwon, Jeongseop Kim, Hyunseo Park, and In Kwon Choi, “ASAM: Adaptive Sharpness-Aware Minimization for Scale-Invariant Learning of Deep Neural Networks,” arXiv:2102.11600v1, first submitted 2021-02-23; Proceedings of Machine Learning Research 139, 5905--5914.
2. Maksym Andriushchenko and Nicolas Flammarion, “Towards Understanding Sharpness-Aware Minimization,” arXiv:2210.01513v1, first submitted 2022-10-04.
