# Decoupled weight decay lowers the exact chattering threshold in AdamW
## Finding

Consider the scalar quadratic
\[
f(x)=\frac h2x^2,
\qquad
h>0,
\]
and the decoupled branch of source AdamW with constant schedule multiplier, zero first-moment memory
\[
\beta_1=0,
\]
second-moment coefficient
\[
0\le\beta_2<1,
\]
base learning rate
\[
\alpha>0,
\]
denominator constant
\[
\varepsilon>0,
\]
and per-step decoupled weight-decay factor
\[
0\le\delta<1.
\]
Here \(\delta\) is the source paper's weight-decay coefficient under unit schedule multiplier.

Define
\[
c=\frac{\alpha h}{\varepsilon}.
\]

There is an exact symmetric nonzero parameter two-cycle whenever
\[
c>2-\delta.
\]
Its amplitude is
\[
a
=
\frac{\alpha}{2-\delta}
-
\frac{\varepsilon}{h},
\]
and the parameter trajectory is
\[
x_t=(-1)^t a.
\]

This two-cycle exists for every
\[
0\le\beta_2<1.
\]
Indeed, along the cycle the squared gradient is constant:
\[
g_t^2=h^2a^2.
\]
Starting from the source initialization \(v_0=0\),
\[
v_t=(1-\beta_2^t)h^2a^2,
\]
so bias correction gives
\[
\widehat v_t=h^2a^2
\]
at every update. The adaptive part therefore reduces exactly to
\[
\frac{g_t}{\sqrt{\widehat v_t}+\varepsilon}
=
\frac{h x_t}{h a+\varepsilon}.
\]

The AdamW update along this trajectory is
\[
x_{t+1}
=
(1-\delta)x_t
-
\alpha
\frac{h x_t}{h a+\varepsilon}.
\]
The condition \(x_{t+1}=-x_t\) is equivalent to
\[
\frac{\alpha h}{h a+\varepsilon}
=
2-\delta,
\]
which gives the amplitude above. Positivity of \(a\) is exactly
\[
c>2-\delta.
\]

The same threshold appears in the linearization at the minimizer. Since the second moment enters only quadratically in \(x\), the parameter multiplier at \(x=0\) is
\[
1-\delta-\frac{\alpha h}{\varepsilon}
=
1-\delta-c.
\]
It crosses \(-1\) exactly at
\[
c=2-\delta.
\]

For the memoryless-second-moment slice
\[
\beta_2=0,
\]
the result is sharper. The full parameter map is the one-dimensional odd map
\[
F(x)
=
(1-\delta)x
-
\alpha
\frac{h x}{h|x|+\varepsilon}.
\]

If
\[
c\le2-\delta,
\]
then every nonzero \(x\) satisfies
\[
|F(x)|<|x|,
\]
so every trajectory converges to the minimizer.

If
\[
c>2-\delta,
\]
the symmetric two-cycle \(\{a,-a\}\) is locally asymptotically stable. Its one-step derivative at either cycle point is
\[
d
=
1-\delta
-
\frac{(2-\delta)^2}{c},
\]
and the existence condition implies
\[
-1<d<1.
\]
Hence the exact two-step multiplier is
\[
d^2
=
\left[
1-\delta
-
\frac{(2-\delta)^2}{c}
\right]^2
<1.
\]

This gives a counterintuitive consequence of decoupling. With no decay,
\[
\delta=0,
\]
the memoryless threshold is
\[
c=2.
\]
With any positive decoupled decay,
\[
0<\delta<1,
\]
the threshold becomes
\[
c=2-\delta<2.
\]
Therefore in the strip
\[
2-\delta<c\le2,
\]
the same memoryless adaptive method converges to the minimizer without decay but has a stable nonzero two-cycle after adding decoupled weight decay.

The exact cycle objective is
\[
f(a)
=
\frac h2
\left(
\frac{\alpha}{2-\delta}
-
\frac{\varepsilon}{h}
\right)^2.
\]
For fixed \(\alpha\), \(h\), and \(\varepsilon\), this floor increases strictly with \(\delta\) throughout the existence region.

## Assumptions and scope

The update is the decoupled-weight-decay branch of Algorithm 2 in the defining AdamW paper, with unit schedule multiplier.

The first-moment coefficient is set to
\[
\beta_1=0
\]
to isolate the interaction between adaptive normalization and decoupled shrinkage. The exact two-cycle existence statement allows arbitrary
\[
0\le\beta_2<1
\]
because bias correction exactly cancels the second-moment transient on the constant-amplitude orbit.

The global convergence and local cycle-stability classification is proved for
\[
\beta_2=0.
\]
No claim is made here about the full basin geometry for positive second-moment memory.

The denominator follows the defining AdamW paper:
\[
\sqrt{\widehat v_t}+\varepsilon.
\]

The theorem concerns deterministic scalar quadratic dynamics, not stochastic training or generalization.

## Proof

With
\[
\beta_1=0,
\]
the bias-corrected first moment equals the current loss gradient:
\[
\widehat m_t=g_t=h x_{t-1}.
\]

Assume a symmetric candidate orbit of amplitude \(a>0\):
\[
x_{t-1}=(-1)^{t-1}a.
\]
Then
\[
g_t^2=h^2a^2
\]
for every \(t\). The second-moment recurrence is
\[
v_t
=
\beta_2v_{t-1}
+
(1-\beta_2)h^2a^2,
\qquad
v_0=0.
\]
Thus
\[
v_t
=
(1-\beta_2^t)h^2a^2,
\]
and the source bias correction gives
\[
\widehat v_t
=
\frac{v_t}{1-\beta_2^t}
=
h^2a^2.
\]

The source decoupled update is therefore
\[
x_t
=
(1-\delta)x_{t-1}
-
\alpha
\frac{h x_{t-1}}{h a+\varepsilon}.
\]
Requiring sign reversal with equal magnitude gives
\[
-1
=
1-\delta
-
\frac{\alpha h}{h a+\varepsilon}.
\]
Solving yields
\[
a
=
\frac{\alpha}{2-\delta}
-
\frac{\varepsilon}{h}.
\]
This is positive exactly when
\[
\frac{\alpha h}{\varepsilon}>2-\delta.
\]

At the minimizer, the second-moment state is quadratic in the parameter perturbation, so the first-order parameter update is
\[
x^+
=
\left(
1-\delta-\frac{\alpha h}{\varepsilon}
\right)x.
\]
Hence the parameter multiplier crosses \(-1\) at the same threshold.

Now set
\[
\beta_2=0.
\]
Then
\[
\widehat v=h^2x^2
\]
at every nonzero state, so
\[
F(x)
=
x
\left[
1-\delta
-
\frac{\alpha h}{h|x|+\varepsilon}
\right].
\]
For \(z>0\), define
\[
M(z)
=
1-\delta
-
\frac{\alpha h}{hz+\varepsilon}.
\]
The function \(M\) is strictly increasing, with
\[
M(0)=1-\delta-c,
\qquad
\lim_{z\to\infty}M(z)=1-\delta.
\]

If
\[
c\le2-\delta,
\]
then
\[
M(0)\ge-1.
\]
For every finite \(z>0\),
\[
-1<M(z)<1,
\]
so
\[
|F(x)|<|x|
\]
for every nonzero \(x\). The magnitudes therefore decrease to a limit \(L\ge0\). If \(L>0\), continuity gives a strict contraction factor at \(L\), contradicting convergence of the magnitudes to a positive limit. Hence
\[
x_t\to0.
\]

If
\[
c>2-\delta,
\]
the positive cycle point is the unique solution of
\[
M(a)=-1.
\]
For \(x>0\),
\[
F'(x)
=
1-\delta
-
\frac{\alpha h\varepsilon}{(hx+\varepsilon)^2}.
\]
At \(x=a\),
\[
ha+\varepsilon
=
\frac{\alpha h}{2-\delta},
\]
so
\[
d
=
F'(a)
=
1-\delta
-
\frac{(2-\delta)^2}{c}.
\]
Because
\[
c>2-\delta,
\]
one has
\[
d>-1,
\]
while
\[
d<1-\delta<1.
\]
The map is odd, so
\[
F'(-a)=F'(a)=d.
\]
The two-step multiplier is therefore
\[
d^2<1,
\]
proving local asymptotic stability.

Finally,
\[
a(\delta)
=
\frac{\alpha}{2-\delta}
-
\frac{\varepsilon}{h}
\]
has derivative
\[
\frac{d a}{d\delta}
=
\frac{\alpha}{(2-\delta)^2}>0,
\]
so the cycle amplitude and its objective floor increase strictly with decoupled decay whenever the cycle exists.

## Verification

The accompanying `verify.py` replays the source bias-corrected second-moment recurrence on the exact alternating orbit for multiple positive \(\beta_2\) values and confirms that \(\widehat v_t=h^2a^2\) at every step.

For the \(\beta_2=0\) slice it verifies the exact scalar map, checks global magnitude contraction below the threshold, checks the two-cycle formula above the threshold, and compares the analytic two-step multiplier with finite perturbations.

The computations are transcription guards. The threshold, global convergent side, exact orbit, and local cycle multiplier are proved analytically above.

## Relationship to prior work

Loshchilov and Hutter introduced decoupled weight decay because adaptive gradient normalization makes ordinary \(L_2\) regularization inequivalent to true weight decay. Their AdamW algorithm applies parameter shrinkage outside the adaptive gradient normalization. The defining paper proves this inequivalence and studies regularization and generalization, but it does not analyze period-two dynamics on quadratics.

Bock and Weiß later proved that Adam can exhibit period-two limit cycles even on quadratic objectives and extended earlier nonconvergence results to bias-corrected Adam. Their analysis concerns Adam without a decoupled weight-decay term. The inspected paper contains no AdamW or weight-decay analysis.

The result here isolates the interaction between those two lines of work. In the memoryless first-moment slice, decoupled shrinkage does not merely damp the adaptive dynamics: it moves the exact period-two threshold from
\[
c=2
\]
to
\[
c=2-\delta,
\]
creating a parameter region in which adding decoupled weight decay changes convergence to a stable nonzero cycle.

## Limitations

The strongest dynamical classification is for
\[
\beta_2=0.
\]
Positive second-moment memory is covered only for exact existence of the symmetric parameter orbit and for the first-order minimizer threshold.

The first-moment coefficient is fixed at
\[
\beta_1=0.
\]
This is a deliberate memoryless-direction slice, not a claim about default AdamW momentum.

The objective is one-dimensional and deterministic.

The theorem is about optimization dynamics, not about whether weight decay improves statistical generalization.

## References

1. Ilya Loshchilov and Frank Hutter, “Decoupled Weight Decay Regularization,” arXiv:1711.05101v1, 2017.
2. Sebastian Bock and Martin Georg Weiß, “Non-Convergence and Limit Cycles in the Adam optimizer,” arXiv:2210.02070v1, 2022.
