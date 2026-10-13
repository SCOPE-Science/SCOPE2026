# A critical endpoint exponent for fractional-unitary query complexity

## Finding

Let \(Q(t,\delta,\varepsilon)\) denote the worst-case query complexity defined for the fractional-power task \(U=e^{iH}\mapsto U^t=e^{itH}\), with controlled access to \(U\) and \(U^\dagger\), diamond-norm error at most \(\varepsilon\), and the spectral promise
\[
\operatorname{spec}(H)\subset[\delta,2\pi),\qquad 0<\delta<1.
\]
Fix \(c>0\) and \(\alpha>0\), let \(\varepsilon\downarrow0\), and allow \(\delta=\delta(\varepsilon)\in(0,1)\) to vary arbitrarily. Consider either endpoint scaling
\[
t_\varepsilon=c\varepsilon^\alpha
\]
or
\[
t_\varepsilon=1-c\varepsilon^\alpha,
\]
whenever these lie in \((0,1)\).

If \(0<\alpha<1\), then in both endpoint regimes
\[
Q(t_\varepsilon,\delta(\varepsilon),\varepsilon)
=
\Theta_{\alpha,c}\!\left(
\frac{1}{\delta(\varepsilon)}
\log\frac{1}{\varepsilon}
\right).
\]
More explicitly,
\[
Q(t_\varepsilon,\delta,\varepsilon)
\ge
\frac{1}{4\delta}
\left[
(1-\alpha)\log\frac{1}{\varepsilon}
+
\log\frac{\pi c}{4}
+
o(1)
\right].
\]

If \(\alpha>1\), then the small-power endpoint becomes trivial: for
\[
t_\varepsilon=c\varepsilon^\alpha,
\]
zero queries suffice for every promised oracle once \(\varepsilon\) is sufficiently small. At the opposite endpoint
\[
t_\varepsilon=1-c\varepsilon^\alpha,
\]
one query suffices once \(\varepsilon\) is sufficiently small.

Therefore \(\alpha=1\) is the sharp exponent separating a logarithmic-query regime from endpoint-trivial approximation. The constant-scale crossover at \(\alpha=1\) is not classified here.

## Assumptions and scope

The query model and success criterion are exactly those of arXiv:2610.01940v1: a query algorithm may use controlled-\(U\), controlled-\(U^\dagger\), arbitrary oracle-independent unitaries and finite ancillas, and success is measured uniformly over the promised oracle family in diamond norm. The logarithm is natural.

The source proves a universal QSVT upper bound
\[
Q(t,\delta,\varepsilon)
\le
\frac{C}{\delta}\log\frac1\varepsilon
\]
for every \(t,\delta\in(0,1)\), and its Remez argument yields, before imposing a fixed endpoint separation,
\[
Q(t,\delta,\varepsilon)
\ge
\frac{1}{4\delta}
\log\frac{\sin(\pi t)}{4\varepsilon}.
\]
The latter is useful whenever its right-hand side is positive.

No claim is made about uncontrolled oracle access, average-case oracles, optimal constants in the \(\Theta\)-law, or the complete \(\alpha=1\) crossover.

## Proof

For the lower-complexity regime, first take
\[
t_\varepsilon=c\varepsilon^\alpha,
\qquad 0<\alpha<1.
\]
As \(\varepsilon\downarrow0\),
\[
\sin(\pi t_\varepsilon)
=
\pi c\varepsilon^\alpha
\left(1+O(\varepsilon^{2\alpha})\right).
\]
Hence
\[
\log\frac{\sin(\pi t_\varepsilon)}{4\varepsilon}
=
(1-\alpha)\log\frac1\varepsilon
+
\log\frac{\pi c}{4}
+
o(1).
\]
Because \(1-\alpha>0\), this expression is eventually positive. Substitution in the source's explicit lower bound gives
\[
Q(t_\varepsilon,\delta,\varepsilon)
\ge
\frac{1}{4\delta}
\left[
(1-\alpha)\log\frac1\varepsilon
+
\log\frac{\pi c}{4}
+
o(1)
\right].
\]
The universal QSVT upper bound gives the matching order
\[
Q(t_\varepsilon,\delta,\varepsilon)
=
O\!\left(\delta^{-1}\log\frac1\varepsilon\right).
\]
These estimates remain valid for arbitrary \(\delta=\delta(\varepsilon)\in(0,1)\).

For the other endpoint,
\[
t_\varepsilon=1-c\varepsilon^\alpha,
\]
one has
\[
\sin(\pi t_\varepsilon)
=
\sin(\pi c\varepsilon^\alpha),
\]
so the identical lower-bound calculation applies, and the same QSVT upper bound completes the \(\Theta\)-statement.

Now assume \(\alpha>1\). For the small-power endpoint, fix a promised oracle \(U=e^{iH}\). The spectrum of \(U^t\) lies on an arc of angular length at most
\[
L=t(2\pi-\delta).
\]
Choose a scalar phase at the midpoint of this arc. Then
\[
\min_{|\omega|=1}
\left\|U^t-\omega I\right\|_{\mathrm{op}}
\le
2\sin\frac{L}{4}.
\]
For unitary channels,
\[
\left\|\mathcal E_V-\mathcal E_W\right\|_\diamond
\le
2\min_{|\omega|=1}\|V-\omega W\|_{\mathrm{op}},
\]
so
\[
\left\|\mathcal E_{U^t}-\mathcal E_I\right\|_\diamond
\le
4\sin\frac{t(2\pi-\delta)}4
\le
t(2\pi-\delta)
<
2\pi t.
\]
With \(t=c\varepsilon^\alpha\) and \(\alpha>1\),
\[
2\pi c\varepsilon^\alpha=o(\varepsilon).
\]
Thus the zero-query identity circuit is eventually \(\varepsilon\)-successful uniformly over the promised oracle family, so
\[
Q(c\varepsilon^\alpha,\delta,\varepsilon)=0
\]
for all sufficiently small \(\varepsilon\).

At the opposite endpoint, one controlled query implements \(U\). Unitary invariance of the diamond norm gives
\[
\left\|\mathcal E_{U^t}-\mathcal E_U\right\|_\diamond
=
\left\|\mathcal E_{U^{t-1}}-\mathcal E_I\right\|_\diamond
<
2\pi(1-t).
\]
For \(1-t=c\varepsilon^\alpha\) with \(\alpha>1\), the right-hand side is \(o(\varepsilon)\), so one query eventually succeeds.

## Verification

The lower bound uses the source's displayed non-endpoint-restricted inequality before its later specialization to fixed \(t\in[\tau,1-\tau]\). The only asymptotic step is
\[
\sin(\pi c\varepsilon^\alpha)
=
\pi c\varepsilon^\alpha(1+o(1)).
\]
The upper bound for \(0<\alpha<1\) is the source's universal QSVT construction. Endpoint triviality for \(\alpha>1\) is checked directly in diamond norm by an operator-norm arc estimate.

The accompanying checker evaluates the normalized logarithmic lower-bound term for representative \(\alpha<1\) and verifies the elementary endpoint inequalities. Those evaluations are corroborative only; the proof above is analytic.

## Relationship to prior work

Sheridan, Maslov and Mosca introduced the black-box fractional-power problem and established inverse-gap lower bounds for powers bounded away from the endpoints. Motlagh and Wiebe developed a GQSP construction for fractional queries. Liu, Wesołowski, Thompson, Gu and Pira proved the optimal
\[
\Theta_\tau\!\left(\delta^{-1}\log(1/\varepsilon)\right)
\]
law for \(t\) bounded away from \(0\) and \(1\), and explicitly identified uniform dependence on \(t\) as an open direction. Their discussion notes that the identity or one query becomes accurate to order \(\min\{t,1-t\}\), while their appendix retains the sharper lower bound involving \(\sin(\pi t)\).

The present statement isolates a complete power-law consequence of those two endpoint mechanisms: if the distance of \(t\) from an integer is \(\varepsilon^\alpha\), the exponent \(\alpha=1\) is the boundary between the logarithmic-query regime and endpoint-trivial approximation. The searched primary sources do not state this exponent classification.

## Limitations

The result does not settle the source's full conjecture
\[
Q=
\Theta\!\left(
\delta^{-1}
\log\frac{\sin(\pi t)}{\varepsilon}
\right)
\]
uniformly in \(t\). In particular, it leaves the critical scaling \(\alpha=1\) unresolved except for elementary sufficient endpoint bounds.

The result concerns the same worst-case controlled-query model and branch convention as the anchor paper. It does not establish analogous claims for uncontrolled access, average-case spectra, or other branch conventions.

The \(\alpha>1\) statement is an upper bound on query cost near \(t=1\): one query suffices. No claim of exact one-query optimality is made there.

## References

1. A. Y. Liu, A. Wesołowski, J. Thompson, M. Gu, and L. Pira, “Optimal query complexity for fractional quantum evolution,” arXiv:2610.01940v1, 2026.
2. D. Motlagh and N. Wiebe, “Generalized Quantum Signal Processing,” PRX Quantum 5, 020368 (2024), arXiv:2308.01501.
3. L. Sheridan, D. Maslov, and M. Mosca, “Approximating Fractional Time Quantum Evolution,” J. Phys. A: Math. Theor. 42 (2009) 185302, arXiv:0810.3843v2.
