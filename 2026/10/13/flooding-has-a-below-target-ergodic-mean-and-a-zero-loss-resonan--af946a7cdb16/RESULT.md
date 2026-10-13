# Flooding has a below-target ergodic mean and a zero-loss resonance on quadratics
## Finding

Flooding replaces a training loss \(f\) by
\[
\widetilde f(x)=|f(x)-b|+b,
\]
where \(b>0\) is the flood level. Above \(b\) the update is ordinary gradient descent; below \(b\) it reverses direction and becomes gradient ascent.

On the scalar quadratic
\[
f(x)=\frac a2x^2,
\qquad
a>0,
\]
put
\[
r=\sqrt{\frac{2b}{a}}
\]
for the flood radius and
\[
h=\eta a
\]
for the normalized gradient step.

Use the convention
\[
\operatorname{sign}(0)=0
\]
at the kink. Then the exact update is
\[
x^+
=
\begin{cases}
(1-h)x,& |x|>r,\\[4pt]
x,& |x|=r,\\[4pt]
(1+h)x,& 0<|x|<r,\\[4pt]
0,& x=0.
\end{cases}
\]

For
\[
0<h<1,
\]
consider an initial point whose orbit never lands exactly on
\[
|x|=r.
\]
The excluded set is countable. The sign of \(x\) is preserved, and after a finite transient the log-radius
\[
u_t=\log\frac{|x_t|}{r}
\]
lies in the invariant interval
\[
[-B,A),
\qquad
A=\log(1+h),
\qquad
B=-\log(1-h).
\]
On that interval,
\[
u_{t+1}
=
\begin{cases}
u_t+A,&u_t<0,\\[4pt]
u_t-B,&u_t>0.
\end{cases}
\]
Writing
\[
s_t=u_t+B
\]
turns the dynamics into the rigid circle rotation
\[
\boxed{
s_{t+1}
=
s_t+A
\pmod{A+B}.
}
\]

Its rotation number is
\[
\boxed{
\rho(h)
=
\frac{\log(1+h)}
{\log\!\left(\frac{1+h}{1-h}\right)}.
}
\]
For every
\[
0<h<1,
\]
we have
\[
0<\rho(h)<\frac12.
\]

If
\[
\rho(h)=\frac pq
\]
in lowest terms, every post-transient non-boundary orbit is periodic with exact period \(q\).

If
\[
\rho(h)\notin\mathbb Q,
\]
every post-transient orbit is dense and equidistributed in log-radius. This gives exact long-run statistics for the raw loss.

The fraction of iterations above the flood level is
\[
\boxed{
\lim_{T\to\infty}
\frac1T
\#\{0\le t<T:f(x_t)>b\}
=
\rho(h)
<
\frac12.
}
\]
Thus the deterministic orbit spends strictly more time below the target loss than above it.

The exact arithmetic mean raw loss is
\[
\boxed{
\lim_{T\to\infty}
\frac1T\sum_{t=0}^{T-1}f(x_t)
=
\frac{bh}{\operatorname{artanh}(h)}
<
b.
}
\]
The exact geometric mean raw loss is
\[
\boxed{
\exp\!\left(
\lim_{T\to\infty}
\frac1T\sum_{t=0}^{T-1}\log f(x_t)
\right)
=
b(1-h^2).
}
\]
So the flood level is not the time-average raw loss even on the simplest deterministic strongly convex example.

The post-transient loss closure is the exact band
\[
\boxed{
b(1-h)^2
\le
f(x)
\le
b(1+h)^2.
}
\]

There is a particularly simple rational resonance. At
\[
\boxed{
h=\frac{\sqrt5-1}{2},
}
\]
we have
\[
B=2A
\]
and therefore
\[
\rho=\frac13.
\]
Every non-boundary post-transient orbit has period three.

At the natural exact-solve step
\[
\boxed{h=1,}
\]
the behavior changes sharply. Any point above the flood level is sent directly to
\[
x=0.
\]
A nonzero point below the flood level doubles in magnitude until it either lands exactly on the boundary or crosses it. If it crosses, the next step is zero. Consequently every nonzero initialization except
\[
\boxed{
|x_0|=r2^{-n},
\qquad
n=0,1,2,\ldots,
}
\]
reaches zero in finitely many iterations and remains there. The exceptional initializations land exactly on the flood boundary and remain fixed there under the stated kink convention.

Thus an exact-solve learning rate for the underlying quadratic can make Flooding collapse to **zero raw loss**, precisely the behavior Flooding was introduced to prevent.

## Assumptions and scope

The result uses deterministic full-batch gradient descent on the original Flooding objective.

The source objective is nonsmooth at
\[
f(x)=b.
\]
The theorem uses
\[
\operatorname{sign}(0)=0,
\]
the convention also made explicit in later formalizations of Flooding. Under another subgradient selection, only orbits that land exactly on the flood boundary can change.

For the rigid-rotation and ergodic statements,
\[
0<h<1.
\]
The countable exact-boundary-hit set is excluded because those trajectories stop at the kink under the chosen convention.

The finite-time zero-loss statement is the separate endpoint case
\[
h=1.
\]

No stochastic minibatching, momentum, adaptive preconditioning, weight decay, or higher-dimensional coupling is included.

The finding characterizes optimization dynamics; it does not assert that a time-average loss below \(b\) is necessarily harmful for generalization.

## Proof

For
\[
f(x)=\frac a2x^2,
\]
the gradient is
\[
\nabla f(x)=ax.
\]
The Flooding gradient is
\[
\operatorname{sign}(f(x)-b)\,ax
\]
away from the kink. Therefore
\[
x^+
=
\begin{cases}
(1-h)x,&f(x)>b,\\[4pt]
(1+h)x,&f(x)<b.
\end{cases}
\]
Because
\[
f(x)>b
\iff
|x|>r,
\]
this is the displayed piecewise multiplicative map.

Assume
\[
0<h<1.
\]
Both multipliers are positive, so the sign of every non-boundary orbit is invariant.

Let
\[
u=\log\frac{|x|}{r}.
\]
Then
\[
u<0
\]
means the raw loss is below the flood level, while
\[
u>0
\]
means it is above. Hence
\[
u^+
=
\begin{cases}
u+A,&u<0,\\[4pt]
u-B,&u>0,
\end{cases}
\]
where
\[
A=\log(1+h),
\qquad
B=-\log(1-h).
\]

Any point below zero is repeatedly increased by \(A\) until it first crosses zero; at that crossing it lies below \(A\). Any point above zero is repeatedly decreased by \(B\) until it first crosses zero; at that crossing it lies above \(-B\). Thus every non-boundary orbit enters
\[
[-B,A)
\]
in finitely many steps.

On this interval define
\[
s=u+B\in[0,A+B).
\]
If
\[
u<0,
\]
then
\[
s^+=s+A.
\]
If
\[
u>0,
\]
then
\[
s^+=s-B=s+A-(A+B).
\]
Therefore
\[
s^+=s+A\pmod{A+B}.
\]
This proves the exact rotation conjugacy.

The rational-periodic and irrational-equidistributed alternatives are the standard classification of rigid circle rotations.

For an irrational rotation, the invariant probability is normalized Lebesgue measure on
\[
[-B,A).
\]
The raw loss at log-radius \(u\) is
\[
f=be^{2u}.
\]
The fraction above the flood level is the normalized length of
\[
(0,A),
\]
namely
\[
\frac{A}{A+B}
=
\rho(h).
\]
Since
\[
\log(1+h)<-\log(1-h),
\]
this is strictly below one half.

The arithmetic mean is
\[
\frac{b}{A+B}
\int_{-B}^{A}e^{2u}\,du
=
\frac{b}{2(A+B)}
\left(
e^{2A}-e^{-2B}
\right).
\]
Using
\[
e^{A}=1+h,
\qquad
e^{-B}=1-h,
\]
the numerator difference is
\[
(1+h)^2-(1-h)^2=4h.
\]
Hence
\[
\overline f
=
\frac{2bh}{A+B}
=
\frac{bh}{\operatorname{artanh}(h)}.
\]
Because
\[
\operatorname{artanh}(h)>h
\]
for
\[
0<h<1,
\]
the mean is strictly below \(b\).

The average log-radius is the midpoint of the interval:
\[
\overline u
=
\frac{A-B}{2}.
\]
Therefore the geometric mean raw loss is
\[
b e^{2\overline u}
=
be^{A-B}
=
b(1-h^2).
\]

For the golden-ratio resonance
\[
h=\frac{\sqrt5-1}{2},
\]
one has
\[
1+h=\frac{1+\sqrt5}{2}
\]
and
\[
1-h=(1+h)^{-2}.
\]
Thus
\[
B=2A
\]
and
\[
\rho=\frac13.
\]

Finally set
\[
h=1.
\]
For
\[
|x|>r,
\]
the descent multiplier is zero, so the next iterate is zero. For
\[
0<|x|<r,
\]
the ascent multiplier is two, so magnitudes double until they either hit \(r\) exactly or first exceed it. Exact boundary contact occurs if and only if
\[
|x_0|=r2^{-n}
\]
for some nonnegative integer \(n\). Every other nonzero trajectory crosses the boundary in finite time and is sent to zero on the following step.

## Verification

The accompanying `verify.py` reconstructs the scalar Flooding update directly from the flooded objective's ascent/descent rule.

It checks random trajectories against the logarithmic rotation identity, verifies finite entry into the invariant loss band, reproduces the period-three golden-ratio resonance, and checks the exact-solve finite-time collapse outside the exceptional dyadic boundary set.

For an irrational target rotation number, it solves for the corresponding normalized step and numerically checks the predicted long-run above-threshold fraction and arithmetic mean loss.

Those finite computations are transcription guards only. The orbit classification and exact long-run formulas are proved analytically above.

## Relationship to prior work

Ishida, Yamane, Sakai, Niu, and Sugiyama introduced Flooding to prevent training loss from continuing toward zero after zero training error. Their description says the loss should float around the flood level by alternating descent above the threshold with ascent below it, and informally describes the resulting motion as a random walk. The defining work does not give an exact deterministic orbit classification on a quadratic.

Karakida, Takase, Hayase, and Osawa later proved that a two-step crossing pattern in Flooding can realize a finite-difference gradient-regularization effect. Their result explains a local ascent–descent mechanism but does not determine the global scalar orbit, rational resonances, time fractions, long-run raw-loss mean, or the exact-solve collapse.

Holland and Nakatani later compared Flooding with a softened ascent–descent method. Their analysis includes formal stationarity guarantees and numerical one-dimensional quadratic illustrations of Flooding. Those illustrations show jagged threshold-crossing dynamics but do not provide the exact rotation conjugacy or the time-average and endpoint classification above.

A previously checked exact result for the Fromage optimizer also produces a rigid circle rotation after a logarithmic change of variables on a shifted scalar quadratic. That prior result concerns a different optimizer and a different threshold mechanism. It does not imply Flooding's raw-loss statistics, the systematic mean below the user-specified flood level, or the exact
\[
h=1
\]
zero-loss absorption phenomenon. The rotation lemma here is used as a mechanism; the accepted contribution is the Flooding-specific calibration and collapse law.

Focused searches for Flooding together with scalar quadratic dynamics, rigid rotations, periodicity, ergodic loss means, and exact-solve collapse did not identify an implication-equivalent published statement.

## Limitations

The complete classification is one-dimensional and deterministic.

For irrational rotations, the time-average formulas rely on unique ergodicity of the rigid circle rotation. Rational steps instead produce finite periodic averages that can depend on the phase.

The kink convention affects only the countable family of exact boundary-hitting trajectories.

The exact-solve collapse at
\[
h=1
\]
is a sharp special step-size phenomenon, not a claim that ordinary small-step Flooding generically converges to zero.

The result does not analyze the stochastic minibatch noise that motivated the informal random-walk description in the defining work.

## References

1. Takashi Ishida, Ikko Yamane, Tomoya Sakai, Gang Niu, and Masashi Sugiyama, “Do We Need Zero Training Loss After Achieving Zero Training Error?”, arXiv:2002.08709v1, first submitted 2020-02-20; ICML 2020, PMLR 119.
2. Ryo Karakida, Tomoumi Takase, Tomohiro Hayase, and Kazuki Osawa, “Understanding Gradient Regularization in Deep Learning: Efficient Finite-Difference Computation and Implicit Bias,” arXiv:2210.02720v1, first submitted 2022-10-06.
3. Matthew J. Holland and Kosuke Nakatani, “Soft ascent-descent as a stable and flexible alternative to flooding,” arXiv:2310.10006v1, first submitted 2023-10-16.
