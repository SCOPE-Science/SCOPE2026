# AdaSGDMax has an exact overshoot-rate reciprocity
## Finding

AdaSGDMax replaces AdaSGD's current global second-moment normalization by a running maximum. On an isotropic quadratic, that max operation makes its response to an excessively large base learning rate exactly solvable.

Consider
\[
F(x)=\frac12\lambda\lVert x\rVert_2^2,
\qquad
\lambda>0,
\]
in dimension \(d\ge1\). Use the theoretical source-form AdaSGDMax recurrence with no momentum and second-moment coefficient
\[
\beta=0.
\]
Let
\[
\eta>0
\]
be the source base learning-rate parameter and let
\[
x_0\ne0.
\]
Define
\[
c=\eta\sqrt d,
\qquad
r_0=\lVert x_0\rVert_2,
\qquad
z=\frac{c}{r_0}.
\]

Because the current gradient is
\[
g_t=\lambda x_t,
\]
the instantaneous scalar second moment is
\[
v_t=\lambda^2\lVert x_t\rVert_2^2.
\]
AdaSGDMax stores
\[
\widehat v_t=\max_{0\le j\le t}v_j.
\]
Writing
\[
R_t=\max_{0\le j\le t}\lVert x_j\rVert_2,
\]
the source learning rate is
\[
\eta_t
=
\frac{\eta}{\sqrt{\widehat v_t/d}}
=
\frac{\eta\sqrt d}{\lambda R_t}.
\]
Therefore the exact vector recurrence is
\[
\boxed{
x_{t+1}
=
\left(1-\frac{c}{R_t}\right)x_t.
}
\]

This has a complete three-regime classification.

If
\[
0<z<2,
\]
the first update does not exceed the initial radius, so
\[
R_t=r_0
\]
for every \(t\). Hence
\[
\boxed{x_t=(1-z)^t x_0.}
\]
The contraction factor is
\[
|1-z|.
\]
The special value
\[
z=1
\]
hits the minimizer in one update.

At
\[
\boxed{z=2,}
\]
one has
\[
\boxed{x_t=(-1)^t x_0,}
\]
so the method is a neutral two-cycle. This is the exact resonance corresponding to the exceptional boundary in the source convergence theorem.

Now suppose
\[
z>2.
\]
The first step is
\[
x_1=(1-z)x_0=-(z-1)x_0.
\]
Define the overshoot amplification
\[
A=z-1>1.
\]
Then
\[
\lVert x_1\rVert_2=A r_0>r_0,
\]
so the running maximum jumps once to
\[
R_1=A r_0.
\]
Thereafter the source multiplier is
\[
1-\frac{c}{R_1}
=
1-\frac{A+1}{A}
=
-\frac1A.
\]
Since its magnitude is below one, no later iterate can exceed \(R_1\), so this multiplier remains fixed forever. Thus, for every \(t\ge1\),
\[
\boxed{
x_t=(-1)^tA^{2-t}x_0.
}
\]
In particular,
\[
\boxed{x_2=x_0.}
\]
The first two steps make zero net progress, but after the running maximum has been reset by the overshoot, all later radii contract geometrically with factor
\[
\boxed{q=\frac1A.}
\]

Therefore the transient and asymptotic effects obey the sharp reciprocity law
\[
\boxed{Aq=1.}
\]
Since the quadratic objective scales with squared radius, equivalently
\[
\boxed{
\frac{F(x_1)}{F(x_0)}=A^2,
\qquad
\frac{F(x_{t+1})}{F(x_t)}=\frac1{A^2}
\quad(t\ge1).
}
\]
Thus AdaSGDMax can stabilize an arbitrarily large base learning rate on this mode, but it pays for the resulting fast post-reset contraction with an exactly reciprocal first-step objective spike.

## Assumptions and scope

The theorem analyzes the theoretical AdaSGDMax variant used in the defining paper's convergence section, not practical AdaSGD.

The second-moment coefficient is \(\beta=0\), and the source theoretical simplification omits momentum and bias correction. This is an admissible endpoint of the stated recurrence and isolates the running-maximum mechanism exactly.

The objective is an isotropic positive quadratic. All iterates stay on the line spanned by \(x_0\), so the vector dynamics reduce without approximation to one radial mode.

The result concerns deterministic dynamics. It does not classify stochastic gradients, nonisotropic Hessians, or nonzero second-moment memory.

## Proof

For \(\beta=0\), the source theoretical second moment is
\[
v_t=\lVert g_t\rVert_2^2
=\lambda^2\lVert x_t\rVert_2^2.
\]
The running-max statistic is therefore
\[
\widehat v_t=\lambda^2R_t^2,
\qquad
R_t=\max_{0\le j\le t}\lVert x_j\rVert_2.
\]
Substituting the source global learning rate into the gradient update gives
\[
x_{t+1}
=x_t-
\frac{\eta\sqrt d}{\lambda R_t}\lambda x_t
=
\left(1-\frac{c}{R_t}\right)x_t.
\]

If \(0<z<2\), then
\[
\lVert x_1\rVert_2
=|1-z|r_0<r_0.
\]
Assuming \(R_t=r_0\), the same fixed multiplier \(1-z\) strictly decreases the radius, so induction yields
\[
R_t=r_0,
\qquad
x_t=(1-z)^t x_0.
\]

If \(z=2\), the multiplier is \(-1\). The radius remains exactly \(r_0\), proving the neutral two-cycle.

If \(z>2\), put \(A=z-1\). Then
\[
x_1=-Ax_0,
\qquad
R_1=Ar_0.
\]
At every later step, provided that running maximum remains \(Ar_0\), the multiplier equals
\[
1-\frac{c}{Ar_0}
=-\frac1A.
\]
Its magnitude is below one, so all later radii are at most \(R_1\), proving self-consistently that the maximum never changes again. Iterating the fixed multiplier gives
\[
x_t
=\left(-\frac1A\right)^{t-1}x_1
=(-1)^tA^{2-t}x_0.
\]
The formulas for \(x_2\), \(q\), and the objective ratios follow immediately.

## Verification

The accompanying `verify.py` reconstructs the source running-max second-moment rule on isotropic quadratics.

It checks the exact subcritical geometric law, the one-step annihilation point, the neutral resonance, the supercritical one-overshoot reset, the identity \(x_2=x_0\), and the reciprocal transient/contraction law across deterministic parameter grids.

The numerical checks are transcription guards. The complete classification is proved algebraically above.

## Relationship to prior work

Wang and Wiens introduce AdaSGD as SGD with an Adam-inspired *global* adaptive learning rate. Because the practical AdaSGD rate can increase, they explicitly note that it need not converge on convex losses and introduce AdaSGDMax, which replaces its second-moment statistic by a running maximum.

Their Theorem 3.1 proves that, on strongly convex deterministic quadratics, AdaSGDMax converges for every positive base learning rate except the boundary case where the limiting effective step is \(2/\lambda_{\max}\). The proof further explains that once the adaptive step enters the ordinary gradient-descent stability interval, the max statistic freezes and the method thereafter behaves exactly like gradient descent.

Those statements are prior work and cover the qualitative convergence phenomenon. The inspected theorem and proof do not state the exact isotropic transient law above: for a supercritical base rate, one overshoot raises the running maximum once, the second iterate returns exactly to its starting point, and the overshoot amplification is the reciprocal of every subsequent contraction factor.

Focused published-record searches for AdaSGDMax overshoot transients, max-gradient normalization, and reciprocal amplification/contraction did not identify an implication-equivalent statement.

## Limitations

The theorem uses the zero-memory endpoint \(\beta=0\).

The Hessian is isotropic, so it does not address competition among eigenmodes in a nonisotropic quadratic.

The exact reciprocal law is deterministic and does not include stochastic-gradient noise.

A very large base learning rate can therefore be asymptotically stable while still producing an arbitrarily large first-step objective spike; the theorem should not be read as a numerical-overflow guarantee.

## References

1. Jiaxuan Wang and Jenna Wiens, “AdaSGD: Bridging the gap between SGD and Adam,” arXiv:2006.16541v1, first submitted 2020-06-30.
