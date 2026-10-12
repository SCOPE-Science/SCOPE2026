# Pure multiplicative ascent and the exact local stability frontier of HMGD
## Finding

Consider the core hybrid multiplicative gradient decomposition update
\[
T(\theta)
=
\theta
-
\eta_A L'(\theta)\sigma(m(\theta))
+
\eta_M\operatorname{slog}(m(\theta)),
\]
where
\[
m(\theta)=\frac{\theta L'(\theta)}{L(\theta)},
\qquad
\sigma(z)=\frac{1}{1+e^{-z}},
\]
and
\[
\operatorname{slog}(z)
=
\operatorname{sign}(z)\log(1+|z|).
\]

On the one-dimensional positive strongly convex loss
\[
L(\theta)
=
c+\frac h2(\theta-a)^2,
\qquad
a,c,h>0,
\]
the unique minimizer is \(\theta=a\). Its exact linearized HMGD factor is
\[
q
=
T'(a)
=
1-\frac{\eta_Ah}{2}+\frac{\eta_Mah}{c}.
\]

Therefore the minimizer is locally asymptotically attracting whenever
\[
|q|<1,
\]
equivalently
\[
0
<
\frac{\eta_A}{2}
-
\frac{\eta_Ma}{c}
<
\frac2h.
\]
It is repelling whenever
\[
|q|>1.
\]
The boundary cases \(|q|=1\) are not classified by first-order linearization.

A necessary condition for local attraction is consequently
\[
\eta_M
<
\frac{\eta_Ac}{2a}.
\]
Thus the additive descent component must dominate the signed-log multiplicative correction near a positive minimizer.

The source explicitly describes \(\eta_A=0\) as a purely multiplicative specialization. For that specialization,
\[
q
=
1+\frac{\eta_Mah}{c}
>
1
\]
for every \(\eta_M>0\), so the true minimizer is repelling.

The failure is global on the upper half-line. If \(\theta_0>a\), then every pure multiplicative iterate satisfies
\[
\theta_{k+1}>\theta_k>a
\]
and
\[
\theta_k\longrightarrow\infty.
\]
Moreover,
\[
\frac{\theta_k}{k}
\longrightarrow
\eta_M\log 3,
\]
so the objective value also diverges.

## Assumptions and scope

The result analyzes the core HMGD update stated in the primary source, without optional momentum, manifold modifications, or additional regularization.

The loss is smooth, strongly convex, strictly positive, and defined on the positive scalar domain containing the minimizer \(a>0\). The positive offset \(c\) ensures that the multiplicative gradient
\[
m(\theta)=\frac{\theta L'(\theta)}{L(\theta)}
\]
is well-defined everywhere.

The local attraction and repulsion statements use the standard one-dimensional fixed-point criterion for a continuously differentiable map with \(|T'(a)|\ne1\). Nothing is asserted here about the nonlinear boundary cases \(|T'(a)|=1\).

The global divergence statement concerns only the pure multiplicative specialization and starts strictly above the minimizer.

## Proof

At the minimizer,
\[
L(a)=c,
\qquad
L'(a)=0.
\]
Hence
\[
m(a)=0.
\]
Differentiating
\[
m(\theta)
=
\frac{\theta L'(\theta)}{L(\theta)}
\]
at \(a\) gives
\[
m'(a)
=
\frac{ah}{c}.
\]

The sigmoid satisfies
\[
\sigma(0)=\frac12.
\]
The signed logarithm is differentiable at zero and satisfies
\[
\operatorname{slog}'(0)=1.
\]
Differentiating the core update at \(a\), the derivative of the additive term is
\[
-\eta_A L''(a)\sigma(0)
=
-\frac{\eta_Ah}{2},
\]
because the term containing \(L'(a)\) vanishes. The multiplicative term contributes
\[
\eta_M\operatorname{slog}'(0)m'(a)
=
\frac{\eta_Mah}{c}.
\]
Therefore
\[
T'(a)
=
1-\frac{\eta_Ah}{2}+\frac{\eta_Mah}{c}.
\]

For a one-dimensional continuously differentiable fixed-point map, \(|T'(a)|<1\) implies local asymptotic attraction and \(|T'(a)|>1\) implies repulsion. Solving
\[
-1
<
1-\frac{\eta_Ah}{2}+\frac{\eta_Mah}{c}
<
1
\]
gives
\[
0
<
\frac{\eta_A}{2}
-
\frac{\eta_Ma}{c}
<
\frac2h.
\]

Now set
\[
\eta_A=0,
\qquad
\eta_M>0.
\]
If \(\theta>a\), then
\[
L'(\theta)>0,
\]
and because \(L(\theta)>0\) and \(\theta>0\),
\[
m(\theta)>0.
\]
Hence
\[
\operatorname{slog}(m(\theta))>0,
\]
so
\[
T(\theta)>\theta.
\]
Thus every trajectory starting above \(a\) is strictly increasing.

Suppose such a trajectory were bounded. It would converge to some finite \(\ell>\theta_0>a\). Continuity of the update would force
\[
\operatorname{slog}(m(\ell))=0,
\]
hence
\[
m(\ell)=0.
\]
For this loss the only zeros of \(m\) are \(\theta=0\) and \(\theta=a\), contradicting \(\ell>a\). Therefore
\[
\theta_k\to\infty.
\]

Finally,
\[
m(\theta)
=
\frac{\theta h(\theta-a)}
{c+\frac h2(\theta-a)^2}
\longrightarrow2
\]
as \(\theta\to\infty\). Consequently
\[
\theta_{k+1}-\theta_k
=
\eta_M\operatorname{slog}(m(\theta_k))
\longrightarrow
\eta_M\log3.
\]
Taking Cesàro averages of the increments gives
\[
\frac{\theta_k}{k}
\longrightarrow
\eta_M\log3.
\]
Since \(L(\theta)\to\infty\) as \(\theta\to\infty\), the objective diverges as well.

## Verification

The standalone script `artifacts/verify_hmgd_frontier.py` symbolically differentiates the HMGD map at the minimizer, verifies the exact factor
\[
1-\frac{\eta_Ah}{2}+\frac{\eta_Mah}{c},
\]
and checks representative attracting and repelling parameter choices.

For the pure multiplicative branch, the script also evaluates trajectories starting above the minimizer and confirms convergence of the increment to
\[
\eta_M\log3.
\]
These computations support the analytic proof; they do not replace the quantified argument.

## Relationship to prior work

The primary HMGD paper defines the multiplicative gradient by normalizing the ordinary derivative with the parameter-to-loss ratio, introduces the signed logarithm to extend multiplicative updates beyond strictly positive gradients, and combines additive and multiplicative components through its core hybrid update. It explicitly identifies \(\eta_A=0\) as the purely multiplicative special case.

The primary source discusses stability qualitatively and notes that purely multiplicative schemes can be unstable, but it does not state the exact positive-minimizer linearization above, the additive-dominance frontier, or the global divergence law for the canonical strongly convex loss.

Earlier multiplicative-calculus optimization papers study positive-domain multiplicative descent or multiplicative Newton-type schemes with different update maps. The inspected literature does not imply the signed-log HMGD factor
\[
1-\frac{\eta_Ah}{2}+\frac{\eta_Mah}{c}
\]
or the pure-branch asymptotic speed
\[
\eta_M\log3.
\]

Targeted searches using the primary article identifier, HMGD terminology, signed-log terminology, pure multiplicative updates, local stability, and quadratic test problems did not locate an equivalent published result.

## Limitations

The local frontier is exact for the stated scalar quadratic-with-offset family and the source core update. It is not a global stability theorem for the full hybrid method on arbitrary objectives.

The pure multiplicative divergence result uses a positive minimizer and an initial point above it. Different sign configurations can change the direction of the signed multiplicative correction.

The boundary cases \(|T'(a)|=1\) require higher-order analysis and are deliberately left unclassified.

Optional extensions of HMGD such as momentum or manifold variants are outside the claim.

## References

1. S. Norozpour, *Multiplicative Gradient Decomposition: A Hybrid Additive–Multiplicative Optimization Framework*, Mathematics 14(9), 1572, published 6 May 2026. DOI: 10.3390/math14091572.
2. G. Kıymık, A. Öztürk, *Exponential-Quadratic-Logarithmic Composite Function Optimization In Positive Domains: Leveraging Multiplicative Calculus In Gradient Descent Algorithms*, International Journal of Pure and Applied Sciences 10(1), 2024. DOI: 10.29132/ijpas.1467644.
3. A. Özyapıcı, M. Riza, B. Bilgehan, A. E. Bashirov, *On multiplicative and Volterra minimization methods*, Numerical Algorithms 67, 2014. DOI: 10.1007/s11075-013-9813-9.
4. *Multiplicative Interior Gradient Methods for Minimization over the Nonnegative Orthant*, SIAM Journal on Control and Optimization. DOI: 10.1137/S0363012994262944.
