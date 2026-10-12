# SlowMo has an exact local-step parity stability law
## Finding

SlowMo wraps several fast optimizer steps inside a slower momentum update. On a scalar quadratic, the complete outer dynamics reduce exactly to a second-order recurrence whose stability depends on the parity of the number of local steps.

Let
\[
f(x)=\frac12\lambda x^2,
\qquad
\lambda>0.
\]
Use deterministic SGD as the base optimizer with constant fast step
\[
\gamma>0,
\]
take
\[
\tau\ge1
\]
inner steps per SlowMo outer iteration, use slow learning rate
\[
\alpha>0,
\]
and slow momentum
\[
0\le\beta<1.
\]

Define
\[
s=\gamma\lambda
\]
and
\[
q=(1-s)^\tau.
\]
The inner SGD block maps
\[
x_{t,0}
\]
to
\[
x_{t,\tau}=q\,x_{t,0}.
\]

The source SlowMo equations are
\[
u_{t+1}
=
\beta u_t
+
\frac{x_{t,0}-x_{t,\tau}}{\gamma},
\]
and
\[
x_{t+1,0}
=
x_{t,0}
-
\alpha\gamma u_{t+1}.
\]
Writing
\[
x_t=x_{t,0},
\]
the slow buffer can be eliminated exactly:
\[
\boxed{
x_{t+1}
=
\bigl[1+\beta-\alpha(1-q)\bigr]x_t
-
\beta x_{t-1}.
}
\]

Therefore the outer state is Schur stable exactly when
\[
\boxed{
0<
\alpha\bigl(1-(1-s)^\tau\bigr)
<
2(1+\beta).
}
\]

For the source's empirically preferred slow learning rate
\[
\alpha=1,
\]
this gives a sharp parity law.

If
\[
\tau
\]
is even, then
\[
\boxed{
\text{SlowMo is stable}
\iff
0<s<2.
}
\]
The slow momentum does not enlarge the scalar fast-step stability interval.

If
\[
\tau
\]
is odd, then
\[
\boxed{
\text{SlowMo is stable}
\iff
0<s<
1+(1+2\beta)^{1/\tau}.
}
\]
For every
\[
\beta>0,
\]
the upper bound is strictly larger than \(2\). Hence there is a nonempty interval
\[
2<s<
1+(1+2\beta)^{1/\tau}
\]
where each individual SGD step has multiplier
\[
1-s<-1
\]
and is unstable, but the synchronized SlowMo outer dynamics are stable.

At the odd-\(\tau\) upper boundary, the outer recurrence has an eigenvalue
\[
-1.
\]
At the even-\(\tau\) boundary
\[
s=2,
\]
the outer recurrence has an eigenvalue
\[
+1.
\]

When
\[
\beta=0,
\]
the source framework reduces in the single-node case to Lookahead. The odd-\(\tau\) upper bound then collapses to
\[
2,
\]
so the above-\(2\) rescue interval is supplied specifically by slow momentum.

## Assumptions and scope

The theorem concerns the exact SlowMo update with deterministic SGD as the base optimizer on one scalar positive quadratic mode.

The result applies equally to multiple identical workers whose deterministic local trajectories coincide, because exact averaging leaves the same scalar inner map.

The fast and slow learning rates are constant over the analyzed trajectory.

Schur stability refers to the two-dimensional outer state induced by the parameter and slow-momentum buffer. It is an outer-iteration stability statement; unstable inner iterates may become large before synchronization when \(s>2\).

The parity result with the explicit upper bound specializes to \(\alpha=1\). The preceding inequality gives the complete stability condition for arbitrary positive \(\alpha\).

## Proof

After \(\tau\) fast SGD steps,
\[
x_{t,\tau}
=
(1-\gamma\lambda)^\tau x_t
=
q x_t.
\]
The slow-momentum equation becomes
\[
u_{t+1}
=
\beta u_t
+
\frac{1-q}{\gamma}x_t.
\]

From the preceding outer update,
\[
x_t
=
x_{t-1}
-
\alpha\gamma u_t,
\]
so
\[
u_t
=
\frac{x_{t-1}-x_t}{\alpha\gamma}.
\]
Substitution gives
\[
x_{t+1}
=
x_t
-
\alpha\gamma
\left[
\beta\frac{x_{t-1}-x_t}{\alpha\gamma}
+
\frac{1-q}{\gamma}x_t
\right],
\]
hence
\[
x_{t+1}
=
\bigl[1+\beta-\alpha(1-q)\bigr]x_t
-
\beta x_{t-1}.
\]

Its characteristic polynomial is
\[
z^2
-
\bigl[1+\beta-\delta\bigr]z
+
\beta,
\qquad
\delta=\alpha(1-q).
\]
For a real monic quadratic
\[
z^2+a_1z+a_2,
\]
the second-order Jury conditions are
\[
1+a_1+a_2>0,
\qquad
1-a_1+a_2>0,
\qquad
1-a_2>0.
\]
Here they reduce to
\[
\delta>0,
\qquad
2(1+\beta)-\delta>0,
\qquad
1-\beta>0.
\]
Because
\[
0\le\beta<1,
\]
the exact stability condition is
\[
0<\delta<2(1+\beta).
\]

Now set
\[
\alpha=1.
\]
Stability is equivalent to
\[
-1-2\beta<q<1.
\]

For even \(\tau\),
\[
q=(1-s)^\tau\ge0.
\]
Thus
\[
q<1
\]
is equivalent, for \(s>0\), to
\[
0<s<2.
\]

For odd \(\tau\), the upper condition
\[
q<1
\]
holds for every \(s>0\). The lower condition is automatic for
\[
0<s\le1,
\]
and for
\[
s>1
\]
it becomes
\[
-(s-1)^\tau>-1-2\beta.
\]
Equivalently,
\[
s<
1+(1+2\beta)^{1/\tau}.
\]

At equality in the upper odd-\(\tau\) bound,
\[
\delta=2(1+\beta),
\]
so the characteristic polynomial vanishes at \(z=-1\). For even \(\tau\) at \(s=2\),
\[
q=1
\]
and \(\delta=0\), so \(z=1\) is a root.

## Verification

The accompanying `verify.py` reconstructs the source SlowMo inner and outer updates, eliminates the slow-momentum buffer, and compares the analytic Schur condition with direct eigenvalue calculations over randomized parameter choices.

It separately checks both parity boundaries for \(\alpha=1\), verifies that odd synchronization periods admit a stable interval above the ordinary scalar SGD limit when \(\beta>0\), and confirms the boundary eigenvalues.

The computations are transcription guards. The exact stability theorem follows from the Jury inequalities proved above.

## Relationship to prior work

Wang, Tantia, Ballas, and Rabbat introduce SlowMo as a wrapper that performs multiple base-optimizer steps between global synchronizations and then updates a slower momentum buffer from the accumulated parameter displacement. Their algorithm explicitly uses the normalized displacement
\[
(x_{t,0}-x_{t,\tau})/\gamma
\]
and the outer step
\[
-\alpha\gamma u_{t+1}.
\]

The defining paper proves smooth nonconvex convergence under diminishing effective steps and studies the empirical effects of \(\alpha\), \(\beta\), and \(\tau\). It reports that \(\alpha=1\) works well across its experiments. The inspected full text does not give a fixed-quadratic Schur stability region, a parity split in \(\tau\), or a regime where slow momentum stabilizes individually unstable local SGD steps.

The source also observes that, on one node with zero slow momentum factor, the framework reduces to Lookahead. Lookahead itself averages or interpolates the result of several fast steps but has no persistent slow-momentum state. The \(\beta=0\) slice of the theorem recovers that distinction: its odd-period upper stability bound is exactly \(s<2\), whereas every \(\beta>0\) creates an odd-period stable interval above \(2\).

Later empirical work on local SGD studies communication-frequency tradeoffs and reports benefits from adding SlowMo, but the inspected literature does not state the exact scalar parity-stability law above.

Focused published-record searches for SlowMo quadratic stability, local-step parity, and a slow-momentum rescue of unstable inner SGD did not identify an implication-equivalent result.

## Limitations

The theorem analyzes a deterministic scalar quadratic mode.

The above-\(2\) rescue is an outer-state result. The fast inner iterates are individually expansive and may attain large intermediate magnitudes before the outer synchronization.

The theorem does not address stochastic-gradient noise, heterogeneous workers, decentralized mixing, or base optimizers other than SGD.

A larger stability region does not by itself imply a better convergence rate or better generalization.

## References

1. Jianyu Wang, Vinayak Tantia, Nicolas Ballas, and Michael Rabbat, “SlowMo: Improving Communication-Efficient Distributed SGD with Slow Momentum,” arXiv:1910.00643v1, first submitted 2019-10-01; ICLR 2020.
2. Michael R. Zhang, James Lucas, Geoffrey Hinton, and Jimmy Ba, “Lookahead Optimizer: \(k\) steps forward, 1 step back,” arXiv:1907.08610v1, first submitted 2019-07-19.
