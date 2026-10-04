# Exact stationary mass-balance and harmonic substrate defects in the Selkov oscillator
## Finding
Consider the positive-parameter Selkov oscillator
\[
\dot x=-x+a y+x^2y,\qquad
\dot y=b-a y-x^2y,
\]
with
\[
a>0,\qquad b>0.
\]

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the exact conditional laws
\[
\mathbb E_\mu[x\mid x+y]=b
\]
and
\[
\mathbb E_\mu[x^2\mid y]=\frac{b}{y}-a.
\]

The second law forces
\[
0<y\le\frac{b}{a}
\]
on the invariant support. Define the unique equilibrium substrate level
\[
y_*=\frac{b}{a+b^2}.
\]
Then
\[
\boxed{
\operatorname{Var}_\mu(x)
=
\mathbb E_\mu[(\dot x+\dot y)^2]
=
b\left(
\mathbb E_\mu\!\left[\frac1y\right]-\frac1{y_*}
\right)
}.
\]
All three terms are nonnegative, and they vanish exactly for the equilibrium atom
\[
\delta_{(b,y_*)}.
\]

Consequently every other compact invariant probability measure satisfies
\[
\mu\{x<b\}>0,\qquad
\mu\{x>b\}>0,
\]
and
\[
\mu\{y<y_*\}>0.
\]
In particular every nonconstant periodic orbit crosses the mass-balance line
\[
x=b
\]
and undershoots the equilibrium substrate level \(y_*\).

There is also an exact substrate-speed defect:
\[
\boxed{
\operatorname{Var}_\mu(x^2)
-
\operatorname{Var}_\mu\!\left(\frac{b}{y}-a\right)
=
\mathbb E_\mu\!\left[
\left(\frac{\dot y}{y}\right)^2
\right]
}.
\]
Its equality case is again exactly the equilibrium atom. Thus every genuinely time-dependent compact stationary state has a strictly positive logarithmic substrate-speed contribution to the fluctuation of \(x^2\).

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the autonomous flow and supported on a compact subset of \(\mathbb R^2\). Compact support supplies all polynomial moments used below. The conditional law itself forces the support away from \(y=0\), so the reciprocal and logarithmic-speed quantities are bounded on the support.

The system is the standard two-parameter Selkov form used in modern dynamical-systems treatments of glycolysis. Its unique equilibrium for \(a,b>0\) is
\[
(x_*,y_*)=
\left(
b,\frac{b}{a+b^2}
\right).
\]

The earliest verified public source date used for the Selkov glycolysis model is 1 March 1968. A modern phase-portrait treatment writes exactly the two-parameter system above and classifies it under primary MSC \(34C05\).

## Proof
Set
\[
s=x+y.
\]
The two equations give the exact mass-balance relation
\[
\dot s=b-x.
\]

Let \(\phi\) be any continuous function on the compact \(s\)-range of the support, and choose a continuously differentiable antiderivative \(H\) with
\[
H'(s)=\phi(s).
\]
For the flow generator \(L\),
\[
LH
=
\phi(s)(b-x).
\]
Invariance therefore gives
\[
\mathbb E_\mu[\phi(s)(b-x)]=0
\]
for every continuous \(\phi\), which is equivalent to
\[
\mathbb E_\mu[x\mid s]=b.
\]
In particular,
\[
\mathbb E_\mu[x]=b.
\]

Next let \(\psi\) be continuous on the compact \(y\)-range and choose an antiderivative \(K\). Then
\[
LK
=
\psi(y)\bigl(b-y(a+x^2)\bigr).
\]
Invariance gives
\[
\mathbb E_\mu[
\psi(y)\bigl(b-y(a+x^2)\bigr)
]=0.
\]
Hence
\[
b-y\left(
a+\mathbb E_\mu[x^2\mid y]
\right)
=
0
\]
almost surely. Since a conditional expectation of \(x^2\) is nonnegative,
\[
0<y\le\frac ba
\]
almost surely and
\[
\mathbb E_\mu[x^2\mid y]
=
\frac by-a.
\]

The same bounds hold on the support. Values \(y<0\) or \(y>b/a\) would have neighborhoods of positive measure. A support point with \(y=0\) is also impossible: there \(\dot y=b>0\), so a short backward segment of its support orbit would enter \(y<0\).

Because
\[
x-b=-\dot s,
\]
the first conditional law gives
\[
\operatorname{Var}_\mu(x)
=
\mathbb E_\mu[(x-b)^2]
=
\mathbb E_\mu[\dot s^2].
\]
On the other hand,
\[
\mathbb E_\mu[x^2]
=
b\,\mathbb E_\mu\!\left[\frac1y\right]-a.
\]
Subtracting
\[
\mathbb E_\mu[x]^2=b^2
\]
gives
\[
\operatorname{Var}_\mu(x)
=
b\,\mathbb E_\mu\!\left[\frac1y\right]-a-b^2
=
b\left(
\mathbb E_\mu\!\left[\frac1y\right]
-\frac{a+b^2}{b}
\right).
\]
Since
\[
\frac1{y_*}=\frac{a+b^2}{b},
\]
the harmonic defect follows.

If this defect vanishes, then \(x=b\) on the invariant support. Every support trajectory therefore has constant \(x\), so \(\dot x=0\) there. The first equation yields
\[
y=\frac{b}{a+b^2}=y_*.
\]
Thus the support is the unique equilibrium. Conversely the equilibrium atom realizes equality.

For a non-equilibrium invariant measure,
\[
\operatorname{Var}_\mu(x)>0.
\]
Since its mean is \(b\), it must put positive mass on each side of \(x=b\). Also
\[
\mathbb E_\mu\!\left[\frac1y\right]
>
\frac1{y_*}.
\]
If \(y\ge y_*\) almost surely, the reverse inequality would hold, so
\[
\mu\{y<y_*\}>0.
\]

Finally define
\[
h(y)=\frac by-a.
\]
The conditional law says
\[
h(y)=\mathbb E_\mu[x^2\mid y].
\]
Moreover,
\[
x^2-h(y)
=
-\frac{\dot y}{y}.
\]
The conditional-variance decomposition therefore gives
\[
\operatorname{Var}_\mu(x^2)
=
\operatorname{Var}_\mu(h(y))
+
\mathbb E_\mu[
(x^2-h(y))^2
],
\]
which is the displayed logarithmic-speed defect.

If its rightmost term vanishes, then \(\dot y=0\) on the invariant support. Thus \(y\) is constant along each support orbit and \(x^2\) is constant there. A bounded complete support trajectory cannot have \(x=0\), because then \(\dot x=ay>0\). Hence \(x\) is constant along the trajectory. Since
\[
\dot x+\dot y=b-x,
\]
we get \(x=b\), and the trajectory is the unique equilibrium. The converse is immediate.

## Verification
The accompanying exact checker verifies
\[
\dot x+\dot y=b-x,
\]
the cleared-denominator identity
\[
y\left(
x^2-\left(\frac by-a\right)
\right)
=
-\dot y,
\]
and the equilibrium equations at
\[
\left(
b,\frac{b}{a+b^2}
\right).
\]

It also checks the algebraic reduction
\[
\mathbb E[x^2]-b^2
=
b\left(
\mathbb E[1/y]-\frac{a+b^2}{b}
\right)
\]
under
\[
\mathbb E[x^2]=b\,\mathbb E[1/y]-a.
\]

The stored checker output is `VERIFY_OK`.

The checker validates the algebraic certificates only. The conditional-expectation statements, support exclusion, and equality classifications are analytic consequences of invariance and are not inferred from finite numerical sampling.

## Relationship to prior work
Sel'kov's 1968 paper introduced a simple kinetic model of glycolytic self-oscillation and analyzed the parameter dependence of self-excitation, periods, and amplitudes. The complete eight-page article was inspected as the historical primary source.

A modern phase-portrait treatment writes exactly
\[
\dot x=-x+ay+x^2y,\qquad
\dot y=b-ay-x^2y
\]
and classifies its finite and infinite phase portraits, including parameter regions with stable limit cycles. Its publicly accessible article page and figure material do not state invariant-measure conditional laws; access to the complete article text was restricted, so whole-document noncoverage is not asserted.

A full open 2021 mathematical study treats the closely related basic Selkov system, proving global statements about bounded and unbounded oscillatory solutions and periodic orbits. Targeted searches of that complete article found no occurrences of “invariant measure”, “average”, or “moment”. Its normalization is different from the two-parameter form used here, so no claim is based merely on term matching.

Targeted scientific searches compared the accepted statement against formulations using stationary moments, conditional expectations, the mass-balance variable \(x+y\), harmonic substrate means, logarithmic substrate speed, periodic-orbit crossings, and the nullcline relation \(y=b/(a+x^2)\). No published statement was located that implication-wise supplies the accepted pair of disintegrations and their two equality-rigid defects.

## Limitations
The theorem concerns compactly supported invariant probability measures. The Selkov literature also contains unbounded solutions; those are outside this stationary compact-recurrence statement.

The result constrains conditional first and second moments and two exact fluctuation defects. It does not determine a complete invariant density, the period of a limit cycle, or the parameter region in which a periodic orbit exists.

The full text of the 2022 exact-normalization phase-portrait article was not accessible in the inspected source, although its abstract, equations, classification, and figure captions were available. This remains a residual originality risk.

Because the identities arise from short generator calculations, an equivalent observation could occur incidentally in unindexed biochemical-dynamics literature under different notation.

## References
1. E. E. Sel'kov, “Self-Oscillations in Glycolysis 1. A Simple Kinetic Model,” European Journal of Biochemistry 4, 79–86 (1968), DOI 10.1111/j.1432-1033.1968.tb00175.x.
2. J. Llibre and A. Nabavi, “Phase portraits of the Selkov model in the Poincaré disc,” Discrete and Continuous Dynamical Systems - B 27, 7607–7623 (2022), DOI 10.3934/dcdsb.2022056.
3. P. Brechmann and A. D. Rendall, “Unbounded solutions of models for glycolysis,” Journal of Mathematical Biology 82, 1 (2021), DOI 10.1007/s00285-021-01560-y.
