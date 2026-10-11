# Fixed-point chord excess and heightwise convective-energy calibration in the Rucklidge system
## Finding
Consider the Rucklidge flow
\[
\dot x=-ax+by-yz,
\qquad
\dot y=x,
\qquad
\dot z=-z+y^2,
\]
with real parameters \(a,b\).

Every bounded complete trajectory has the exact thermal-memory representation
\[
\boxed{
z(t)=\int_0^\infty e^{-s}y(t-s)^2\,ds
}.
\]
Consequently every bounded complete trajectory other than the origin satisfies
\[
\boxed{
z(t)>0
\quad\text{for every }t
}.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. The three coordinate layers obey
\[
\boxed{
\mathbb E_\mu[x\mid y]=0
},
\]
\[
\boxed{
\mathbb E_\mu[y^2\mid z]=z
},
\]
and
\[
\boxed{
\mathbb E_\mu[y(b-z)\mid x]=ax
}.
\]

Write
\[
m=\mathbb E_\mu[z].
\]
Then
\[
\mathbb E_\mu[y^2]=m
\]
and
\[
\boxed{
\operatorname{Var}_\mu(z)
=
m(b-m)+\mathbb E_\mu[x^2]
}.
\]
Thus the variance of the temperature coordinate is the fixed-point chord
\[
m(b-m)
\]
plus the exact transverse kinetic defect
\[
\mathbb E_\mu[x^2].
\]

The heightwise regression has a second exact defect. Since
\[
y^2-z=\dot z,
\]
conditional orthogonality gives
\[
\boxed{
\operatorname{Var}_\mu(y^2)
=
\operatorname{Var}_\mu(z)
+
\mathbb E_\mu[\dot z^2]
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(z,y^2)
=
\operatorname{Var}_\mu(z)
}.
\]
Combining the two identities,
\[
\boxed{
\operatorname{Var}_\mu(y^2)
=
m(b-m)
+
\mathbb E_\mu[x^2]
+
\mathbb E_\mu[\dot z^2]
}.
\]

Both nonnegative defects vanish exactly for invariant measures supported on equilibria.

Suppose now that
\[
b>0.
\]
The equilibria are
\[
E_0=(0,0,0),
\qquad
E_\pm=(0,\pm\sqrt b,b).
\]
For any prescribed
\[
m\in[0,b],
\]
a mixture of \(E_0\) with either \(E_+\) or \(E_-\) has mean height \(m\) and satisfies
\[
\operatorname{Var}(z)
=
\operatorname{Var}(y^2)
=
m(b-m).
\]
Hence the envelope
\[
\boxed{
\operatorname{Var}_\mu(y^2)
\ge
\operatorname{Var}_\mu(z)
\ge
m(b-m)
}
\]
is sharp whenever
\[
0\le m\le b.
\]
Equality throughout occurs exactly for equilibrium-supported measures.

There is also a recurrence barrier above the nonzero-equilibrium height. For every non-equilibrium-supported invariant measure,
\[
\mathbb E_\mu[x^2]>0.
\]
The chord identity is equivalently
\[
\mathbb E_\mu[x^2]
=
\mathbb E_\mu[z(z-b)].
\]
Because compact stationary states are supported in
\[
z\ge0,
\]
the positive right-hand side forces
\[
\boxed{
\mu\{z>b\}>0
}.
\]
Thus every genuinely recurrent stationary state at \(b>0\) must spend positive invariant mass above the height of the two nonzero equilibria.

Finally, every non-equilibrium-supported invariant measure has
\[
\operatorname{Var}_\mu(z)>0,
\qquad
\mathbb E_\mu[\dot z^2]>0,
\]
so
\[
\boxed{
0<
\operatorname{Corr}_\mu(z,y^2)
<
1
}
\]
and, more precisely,
\[
\boxed{
\operatorname{Corr}_\mu(z,y^2)
=
\left(
1+
\frac{\mathbb E_\mu[\dot z^2]}
{\operatorname{Var}_\mu(z)}
\right)^{-1/2}
}.
\]

For the well-studied chaotic parameter choice
\[
(a,b)=(2,6.7),
\]
the theorem says that every non-equilibrium compact stationary state has positive invariant mass in
\[
z>6.7.
\]
This is consistent with the use of the section
\[
z=6.7
\]
in modern periodic-orbit studies of the chaotic Rucklidge flow.

## Assumptions and scope
The theorem concerns the classical Rucklidge system
\[
\dot x=-ax+by-yz,
\qquad
\dot y=x,
\qquad
\dot z=-z+y^2.
\]
The invariant-measure statements require compact support. The memory formula requires only a bounded complete trajectory.

No ergodicity assumption is used. The result applies to equilibrium atoms, compact periodic-orbit measures, compact chaotic invariant measures, and convex mixtures.

The original double-convection article appeared in 1992, but the checked bibliographic material resolved that publication only to April 1992. No day was invented. The structured date therefore uses 12 February 2013, the earliest checked day-resolved public source that writes the Rucklidge equations explicitly.

That 2013 mathematical source lists classification \(34A34\) first. The code \(34A34\) remains an MSC2020 classification and is used here as the primary classification.

## Proof
For a bounded complete trajectory, solve the linear equation
\[
\dot z+z=y^2
\]
backward over a time interval of length \(T\):
\[
z(t)
=
e^{-T}z(t-T)
+
\int_0^T e^{-s}y(t-s)^2\,ds.
\]
Boundedness makes the first term vanish as
\[
T\to\infty,
\]
giving
\[
z(t)
=
\int_0^\infty e^{-s}y(t-s)^2\,ds.
\]
Therefore
\[
z(t)\ge0.
\]
If
\[
z(t_0)=0,
\]
the nonnegative integral forces
\[
y(t_0-s)=0
\]
for every
\[
s\ge0.
\]
Then
\[
x=\dot y=0
\]
on the same past interval, and the state at \(t_0\) is the origin. Uniqueness makes the complete trajectory the origin. This proves strict positivity for every other bounded complete trajectory.

Now let \(\mu\) be compactly supported and invariant, and let \(L\) denote the generator.

For any continuous \(\phi\) on the compact \(y\)-projection of the support, choose an antiderivative \(H\) with
\[
H'(y)=\phi(y).
\]
Then
\[
LH=\phi(y)x.
\]
Invariance gives
\[
\mathbb E_\mu[\phi(y)x]=0
\]
for every \(\phi\), hence
\[
\mathbb E_\mu[x\mid y]=0.
\]

Applying arbitrary antiderivative tests in \(z\) gives
\[
\mathbb E_\mu[
\chi(z)(-z+y^2)
]
=
0,
\]
so
\[
\mathbb E_\mu[y^2\mid z]=z.
\]

Applying arbitrary antiderivative tests in \(x\) gives
\[
\mathbb E_\mu[
\psi(x)(-ax+by-yz)
]
=
0,
\]
hence
\[
\mathbb E_\mu[y(b-z)\mid x]=ax.
\]

Averaging the heightwise law yields
\[
\mathbb E[y^2]=m.
\]

Next differentiate the product
\[
xy.
\]
Using the vector field,
\[
\frac{d}{dt}(xy)
=
x^2-a xy+b y^2-y^2z.
\]
The first regression gives
\[
\mathbb E[xy]=0.
\]
The heightwise law gives
\[
\mathbb E[y^2z]
=
\mathbb E[z^2].
\]
Stationarity of \(xy\) therefore yields
\[
0
=
\mathbb E[x^2]
+
bm
-
\mathbb E[z^2].
\]
Thus
\[
\mathbb E[z^2]
=
bm+\mathbb E[x^2].
\]
Subtracting \(m^2\) proves
\[
\operatorname{Var}(z)
=
m(b-m)+\mathbb E[x^2].
\]

For the height-speed law, write
\[
R=y^2-z=\dot z.
\]
The conditional regression gives
\[
\mathbb E[R\mid z]=0.
\]
Hence \(R\) is orthogonal in \(L^2(\mu)\) to every square-integrable function of \(z\). Since
\[
y^2=z+R,
\]
the Pythagorean identity gives
\[
\operatorname{Var}(y^2)
=
\operatorname{Var}(z)
+
\mathbb E[R^2]
\]
and
\[
\operatorname{Cov}(z,y^2)
=
\operatorname{Var}(z).
\]

It remains to classify equality.

If
\[
\mathbb E[x^2]=0,
\]
continuity makes
\[
x=0
\]
on the invariant support. Every support trajectory then has
\[
\dot y=0,
\]
so \(y\) is constant. The equation
\[
\dot x=y(b-z)
\]
must vanish on the support.

If \(y=0\), then the remaining scalar equation is
\[
\dot z=-z.
\]
A bounded complete support trajectory of this equation must have
\[
z=0.
\]

If \(y\ne0\), then
\[
z=b.
\]
The equation
\[
\dot z=-b+y^2
\]
then forces
\[
y^2=b.
\]
Thus the support consists entirely of equilibria.

Conversely every equilibrium-supported invariant measure has
\[
x=0,
\]
so the first defect vanishes.

Similarly, if
\[
\mathbb E[\dot z^2]=0,
\]
then
\[
\dot z=0
\]
on the support. Hence \(z\) is constant along each support trajectory and
\[
y^2=z.
\]
If \(z=0\), bounded completeness gives the origin. If \(z>0\), continuity fixes the sign of \(y\), so \(y\) is constant, then
\[
x=\dot y=0,
\]
and
\[
y(b-z)=0
\]
forces
\[
z=b.
\]
Again the support consists of equilibria. The converse is immediate.

If
\[
\operatorname{Var}(z)=0,
\]
the invariant support lies in a constant-\(z\) plane. Tangency gives
\[
\dot z=0
\]
there, so the same argument yields equilibrium support. Thus every non-equilibrium-supported invariant measure has positive \(z\)-variance and positive height-speed defect, proving the strict correlation formula.

Finally, for
\[
b>0,
\]
a non-equilibrium-supported measure has
\[
\mathbb E[x^2]>0.
\]
Using
\[
\mathbb E[x^2]
=
\mathbb E[z(z-b)]
\]
and
\[
z\ge0
\]
on compact recurrent support, positivity of the expectation forces positive mass where
\[
z>b.
\]

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the pointwise identities
\[
\dot z=y^2-z
\]
and
\[
\frac{d}{dt}(xy)
=
x^2-a xy+b y^2-y^2z.
\]

It verifies the stationary algebra
\[
\mathbb E[z^2]
=
b\,\mathbb E[z]
+
\mathbb E[x^2]
\]
and therefore
\[
\operatorname{Var}(z)
=
m(b-m)+\mathbb E[x^2].
\]

It also verifies the abstract orthogonal-regression decomposition
\[
\operatorname{Var}(y^2)
=
\operatorname{Var}(z)
+
\mathbb E[\dot z^2]
\]
and the covariance identity.

At
\[
(a,b)=(2,67/10),
\]
the checker verifies the exact nonzero-equilibrium height
\[
b=67/10
\]
and the equilibrium coordinates
\[
(0,\pm\sqrt b,b)
\]
through their squared-coordinate equations.

The stored checker output is `VERIFY_OK`.

The memory representation, conditional expectations, support rigidity, and positive-mass excursion above \(z=b\) are analytic proofs; they are not inferred from finite trajectory experiments.

## Relationship to prior work
Rucklidge's 1992 double-convection article derives third-order ordinary differential equations for weakly nonlinear double convection and shows chaotic solutions created through a homoclinic explosion.

A complete 2013 mathematical article writes exactly
\[
\dot x=-ax+by-yz,
\qquad
\dot y=x,
\qquad
\dot z=-z+y^2,
\]
classifies the equilibria, and develops Hopf bifurcation and first- and second-Lyapunov-coefficient analysis. Full-document searches found no occurrence of `moment`, `variance`, `invariant measure`, or `average`.

A complete open 2021 article studies the same system through Lyapunov exponents, Poincaré return maps, variational extraction of unstable periodic orbits, symbolic encoding, and periodic-orbit bifurcations. Its searchable text contains no `variance`, `invariant measure`, or `conditional` formulation matching the accepted theorem. Its only discussion of averages is the general observation that cycle expansions can compute long-time averages.

A previously indexed same-system result gives a distinct global damping and recurrence balance. Its statement controls a derivative-energy ratio and the sign of \(a\); it does not implication-wise determine the conditional height calibration
\[
\mathbb E[y^2\mid z]=z
\]
or the fixed-point chord-excess law
\[
\operatorname{Var}(z)
=
m(b-m)+\mathbb E[x^2].
\]

The accepted theorem therefore concerns a different structure: exact past-memory positivity, fiberwise convective-energy calibration, and a sharp lower fixed-point chord with dynamical excess.

## Limitations
The invariant-measure statements require compact support. The memory formula requires a bounded complete trajectory.

For
\[
b>0,
\]
the sharp chord inequality
\[
\operatorname{Var}(z)\ge m(b-m)
\]
is informative as a nonnegative lower envelope when
\[
0\le m\le b.
\]
The exact identity remains valid outside that interval, but the chord term is then negative.

The theorem does not prove existence of a chaotic attractor for arbitrary parameters and does not determine the full invariant distribution.

The original 1992 source was verified only to month resolution in the checked bibliographic material; the structured date uses the earliest checked day-resolved same-system source instead of inventing a day.

Because the key generator identities are short, an equivalent formulation could remain in unindexed literature.

## References
1. A. M. Rucklidge, “Chaos in models of double convection,” *Journal of Fluid Mechanics* 237, 209–229 (1992), DOI 10.1017/S0022112092003392.
2. F. S. Dias and L. F. Mello, “Hopf bifurcations and small amplitude limit cycles in Rucklidge systems,” *Electronic Journal of Differential Equations* 2013(48), 1–9 (2013).
3. C. Dong, L. Jia, J. Qi, and H. Li, “Symbolic Encoding of Periodic Orbits and Chaos in the Rucklidge System,” *Complexity* 2021, 4465151 (2021), DOI 10.1155/2021/4465151.
