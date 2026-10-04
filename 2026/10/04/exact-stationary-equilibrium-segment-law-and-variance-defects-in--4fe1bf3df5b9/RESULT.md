# Exact stationary equilibrium-segment law and variance defects in Sprott K
## Finding
Consider the canonical Sprott K system
\[
\dot x=xy-z,\qquad
\dot y=x-y,\qquad
\dot z=x+\frac3{10}z.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the two exact conditional laws
\[
\mathbb E_\mu[x\mid y]=y,
\qquad
\mathbb E_\mu[x\mid z]=-\frac3{10}z.
\]

Let
\[
s=\mathbb E_\mu[y^2],
\qquad
q=\frac9{100}s.
\]
Then
\[
0\le q\le1
\]
and the stationary mean vector is
\[
\left(
\mathbb E_\mu[x],
\mathbb E_\mu[y],
\mathbb E_\mu[z]
\right)
=
\left(
-\frac{10}{3}q,
-\frac{10}{3}q,
\frac{100}{9}q
\right).
\]
Thus every stationary mean lies exactly on the line segment joining the two equilibria
\[
e_0=(0,0,0)
\]
and
\[
e_1=
\left(
-\frac{10}{3},
-\frac{10}{3},
\frac{100}{9}
\right).
\]

The \(y\)-variance is fixed by the same scalar parameter:
\[
\operatorname{Var}_\mu(y)
=
\frac{100}{9}q(1-q).
\]
Hence the first two \(y\)-moments of an arbitrary compact stationary state coincide with those of the equilibrium mixture
\[
(1-q)\delta_{e_0}+q\delta_{e_1}.
\]

The dynamical departure from that equilibrium mixture is measured by exact variance defects:
\[
\operatorname{Var}_\mu(x)
-
\operatorname{Var}_\mu(y)
=
\mathbb E_\mu[(x-y)^2]
\ge0,
\]
and
\[
\operatorname{Var}_\mu(x)
-
\frac9{100}\operatorname{Var}_\mu(z)
=
\mathbb E_\mu\!\left[\left(x+\frac3{10}z\right)^2\right]
\ge0.
\]
Equality in either defect holds exactly for convex mixtures of the two equilibrium atoms.

There is also an exact RMS ordering:
\[
\mathbb E_\mu[z^2]-\mathbb E_\mu[y^2]
=
\frac7{13}\,
\mathbb E_\mu[(y-z)^2]
\ge0.
\]
Equality here is more rigid: it holds only for the origin atom.

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the Sprott K flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of all polynomial and one-variable antiderivative test functions used below.

The equations are the canonical Case K of Sprott's 1994 list. A later Sprott K treatment writes the same equations explicitly and also considers a multi-parameter fractional-order generalization; the theorem here concerns only the original integer-order canonical flow.

The earliest verified public source date is 1 August 1994.

The two equilibria follow directly from the equations:
\[
e_0=(0,0,0),
\qquad
e_1=
\left(
-\frac{10}{3},
-\frac{10}{3},
\frac{100}{9}
\right).
\]

## Proof
Let \(L\) denote the generator.

For any continuous function \(\phi\) on the compact \(y\)-range, choose an antiderivative \(H\) with
\[
H'(y)=\phi(y).
\]
Then
\[
LH=\phi(y)(x-y).
\]
Stationarity gives
\[
\mathbb E_\mu[\phi(y)(x-y)]=0
\]
for every such \(\phi\), hence
\[
\mathbb E_\mu[x\mid y]=y.
\]

Likewise, for any continuous function \(\psi\) on the compact \(z\)-range and an antiderivative \(K\),
\[
LK=\psi(z)\left(x+\frac3{10}z\right),
\]
so
\[
\mathbb E_\mu[x\mid z]=-\frac3{10}z.
\]

Taking expectations in the coordinate equations gives
\[
\mathbb E[x]=\mathbb E[y],
\]
\[
\mathbb E[x]=-\frac3{10}\mathbb E[z],
\]
and
\[
\mathbb E[xy]=\mathbb E[z].
\]
The first conditional law also gives
\[
\mathbb E[xy]=\mathbb E[y^2]=s.
\]
Therefore
\[
\mathbb E[z]=s,
\qquad
\mathbb E[x]=\mathbb E[y]=-\frac3{10}s.
\]

Since variance is nonnegative,
\[
0
\le
\operatorname{Var}(y)
=
s-\frac9{100}s^2
=
s\left(1-\frac9{100}s\right).
\]
Thus
\[
0\le s\le\frac{100}{9}.
\]
With
\[
q=\frac9{100}s,
\]
the asserted equilibrium-segment formula and
\[
\operatorname{Var}(y)
=
\frac{100}{9}q(1-q)
\]
follow.

For the first defect, stationarity of \(y^2/2\) gives
\[
\mathbb E[xy]=\mathbb E[y^2].
\]
Because
\[
\mathbb E[x]=\mathbb E[y],
\]
we obtain
\[
\operatorname{Var}(x)-\operatorname{Var}(y)
=
\mathbb E[x^2]-\mathbb E[y^2]
=
\mathbb E[(x-y)^2].
\]

If this defect vanishes, then
\[
x=y
\]
on the invariant support. Tangency of the plane \(x=y\) requires
\[
0=\frac{d}{dt}(x-y)=x^2-z,
\]
so
\[
z=x^2.
\]
Then
\[
\dot x=x^2-z=0,
\]
and invariance requires
\[
0=\dot z=x+\frac3{10}x^2
=
x\left(1+\frac3{10}x\right).
\]
Hence the support is contained in
\[
\{e_0,e_1\}.
\]
Conversely every convex mixture of the two equilibrium atoms has zero defect.

For the second defect, stationarity of \(z^2/2\) gives
\[
\mathbb E[xz]
=
-\frac3{10}\mathbb E[z^2].
\]
Since
\[
\mathbb E[x]
=
-\frac3{10}\mathbb E[z],
\]
direct expansion yields
\[
\operatorname{Var}(x)
-
\frac9{100}\operatorname{Var}(z)
=
\mathbb E\!\left[\left(x+\frac3{10}z\right)^2\right].
\]
If this vanishes, then
\[
x+\frac3{10}z=0
\]
on the support, so
\[
\dot z=0.
\]
Thus \(x\) and \(z\) are constant along each support trajectory. The equation
\[
\dot y=x-y
\]
has only the bounded complete solution
\[
y=x
\]
when \(x\) is constant. The preceding equilibrium calculation then gives \(e_0\) or \(e_1\).

Finally, stationarity of \(yz\) gives
\[
0
=
\mathbb E[xz]
+
\mathbb E[xy]
-
\frac7{10}\mathbb E[yz].
\]
Using
\[
\mathbb E[xz]
=
-\frac3{10}\mathbb E[z^2]
\]
and
\[
\mathbb E[xy]
=
\mathbb E[y^2]
\]
gives
\[
\mathbb E[yz]
=
\frac{10\mathbb E[y^2]-3\mathbb E[z^2]}7.
\]
Substitution into
\[
\mathbb E[(y-z)^2]
=
\mathbb E[y^2]
+
\mathbb E[z^2]
-
2\mathbb E[yz]
\]
yields
\[
\mathbb E[z^2]-\mathbb E[y^2]
=
\frac7{13}\mathbb E[(y-z)^2].
\]

If equality holds, then \(y=z\) on the invariant support. Tangency of that plane requires
\[
0=\dot y-\dot z
=
-\frac{13}{10}y,
\]
so
\[
y=z=0.
\]
Then
\[
\dot y=x
\]
forces
\[
x=0.
\]
Thus the origin atom is the unique equality case.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies the generator identities
\[
Ly=x-y,
\qquad
Lz=x+\frac3{10}z,
\]
\[
L\left(\frac{y^2}{2}\right)=xy-y^2,
\]
\[
L\left(\frac{z^2}{2}\right)=xz+\frac3{10}z^2,
\]
and
\[
L(yz)
=
xz+xy-\frac7{10}yz.
\]

It also verifies both equilibria exactly and replays the algebraic coefficient
\[
\frac7{13}
\]
in the RMS-gap identity.

The stored checker output is `VERIFY_OK`.

The conditional identities use arbitrary one-variable antiderivative tests. The equality classifications use invariance of the compact support and bounded completeness. These analytic steps are not finite experiments.

## Relationship to prior work
Sprott's 1994 article introduced the canonical K system as part of the nineteen algebraically simple chaotic flows and reported its equilibria, Lyapunov spectrum, and attractor dimension.

A full 2001 statistical study of Sprott flows was inspected because of its potential to dominate moment claims. It develops autocovariance and power-spectrum models but explicitly studies only generalized B and N systems, not K.

Panchev's 2004 analytical study covers all nineteen Sprott systems and discusses oscillator reductions, asymptotic nondifferential relations, and possible statistical treatment. Only its abstract and bibliographic metadata were securely available, so it remains the principal unresolved literature risk and no whole-document noncoverage claim is made.

Later Sprott K work explicitly reproduces
\[
\dot x=xy-z,\qquad
\dot y=x-y,\qquad
\dot z=x+0.3z
\]
before introducing generalized fractional-order parameters. Its focus is fractional-order dynamics and circuit realization rather than invariant probability measures.

Targeted searches for the two conditional laws, the equilibrium-segment mean formula, the exact mean–variance parabola, and the variance defects did not locate a same-object statement implying the theorem above.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not prove existence or uniqueness of the chaotic attractor, characterize unbounded trajectories, or determine a complete invariant density.

The first two \(y\)-moments cannot distinguish an arbitrary compact stationary state from a suitable equilibrium mixture; that degeneracy is part of the theorem. The variance defects provide only necessary diagnostics for nonequilibrium recurrence, not a full classification.

The complete Panchev 2004 article was not securely available for full-text comparison, so a differently phrased prior derivation remains a specific residual risk.

The novelty claim is restricted to the exact stationary conditional laws, equilibrium-segment/parabola law, and variance-defect structure, not to the equations, equilibria, or previously reported chaotic numerical behavior.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647.
2. E. S. Dimitrova and O. I. Yordanov, “Statistics of some low-dimensional chaotic flows,” International Journal of Bifurcation and Chaos 11, 2675–2682 (2001), DOI 10.1142/S0218127401003735.
3. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 721–728 (2004), DOI 10.1016/j.chaos.2003.12.054.
4. “Circuit Realization of the Fractional-Order Sprott K Chaotic System with Standard Components,” Fractal and Fractional 7, 470 (2023).
