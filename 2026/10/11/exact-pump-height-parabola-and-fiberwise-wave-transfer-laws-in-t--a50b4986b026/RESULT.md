# Exact pump-height parabola and fiberwise wave-transfer laws in the Rabinovich system
## Finding
Consider the classical Rabinovich plasma-wave system
\[
\dot x
=
h y-\nu_1x-yz,
\qquad
\dot y
=
h x-\nu_2y+xz,
\qquad
\dot z
=
-z+xy,
\]
where
\[
h>0,
\qquad
\nu_1>0,
\qquad
\nu_2>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then the three coordinate fibers satisfy the exact transfer laws
\[
\boxed{
\mathbb E_\mu[xy\mid z]=z
},
\]
\[
\boxed{
\mathbb E_\mu[y(h-z)\mid x]=\nu_1x
},
\]
and
\[
\boxed{
\mathbb E_\mu[x(h+z)\mid y]=\nu_2y
}.
\]

Write
\[
m=\mathbb E_\mu[z],
\qquad
q=\mathbb E_\mu[z^2].
\]
Stationarity of two quadratic wave energies gives
\[
\boxed{
\nu_1\mathbb E_\mu[x^2]=hm-q
}
\]
and
\[
\boxed{
\nu_2\mathbb E_\mu[y^2]=hm+q
}.
\]
Consequently,
\[
\boxed{
\operatorname{Var}_\mu(z)
+
\nu_1\mathbb E_\mu[x^2]
=
m(h-m)
}.
\]

This identity places every compact stationary state on an exact pump-height parabola with a nonnegative transverse-wave defect.

The origin atom is the unique compact invariant probability measure with
\[
\mathbb E_\mu[x^2]=0.
\]
Therefore every other compact stationary state satisfies
\[
\boxed{
0<m<h
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(z)
<
m(h-m)
}.
\]

There is also a recurrent slab constraint. The first quadratic identity can be written
\[
\mathbb E_\mu[z(z-h)]
=
-\nu_1\mathbb E_\mu[x^2].
\]
For every non-origin stationary state the right side is strictly negative. Since
\[
z(z-h)<0
\]
exactly when
\[
0<z<h,
\]
one obtains
\[
\boxed{
\mu\{0<z<h\}>0
}.
\]
Thus every genuinely nontrivial compact recurrent state spends positive invariant mass in the height interval selected directly by the pumping amplitude.

The three transfer laws also have exact speed-defect forms. Since
\[
xy-z=\dot z,
\]
\[
y(h-z)-\nu_1x=\dot x,
\]
and
\[
x(h+z)-\nu_2y=\dot y,
\]
conditional orthogonality gives
\[
\boxed{
\operatorname{Var}_\mu(xy)
=
\operatorname{Var}_\mu(z)
+
\mathbb E_\mu[\dot z^2]
},
\]
\[
\boxed{
\operatorname{Var}_\mu(y(h-z))
=
\nu_1^2\operatorname{Var}_\mu(x)
+
\mathbb E_\mu[\dot x^2]
},
\]
and
\[
\boxed{
\operatorname{Var}_\mu(x(h+z))
=
\nu_2^2\operatorname{Var}_\mu(y)
+
\mathbb E_\mu[\dot y^2]
}.
\]
The corresponding covariances are
\[
\operatorname{Cov}_\mu(z,xy)
=
\operatorname{Var}_\mu(z),
\]
\[
\operatorname{Cov}_\mu(x,y(h-z))
=
\nu_1\operatorname{Var}_\mu(x),
\]
and
\[
\operatorname{Cov}_\mu(y,x(h+z))
=
\nu_2\operatorname{Var}_\mu(y).
\]

At the classical multistable chaotic parameters
\[
(\nu_1,\nu_2,h)
=
(1,4,4.92),
\]
every non-origin compact stationary state satisfies
\[
0<\mathbb E_\mu[z]<4.92
\]
and
\[
\boxed{
\operatorname{Var}_\mu(z)
+
\mathbb E_\mu[x^2]
=
\mathbb E_\mu[z]
\left(
4.92-\mathbb E_\mu[z]
\right)
}.
\]

## Assumptions and scope
The theorem concerns the original Rabinovich system for three resonantly coupled plasma waves, with positive pumping amplitude \(h\) and positive normalized damping decrements \(\nu_1,\nu_2\).

Compact support is used to justify the invariant-generator identities and the required second moments. No ergodicity assumption is needed.

The system is historically associated with Rabinovich's 1978 plasma-turbulence work. The checked historical record resolves that foundational publication only to May 1978, not to a day. The structured source date therefore uses 1 August 2008, the earliest checked day-resolved public same-system mathematical source, rather than inventing a day in 1978.

The 2008 global-dynamics article classifies the Rabinovich system first under MSC \(37D45\), followed by \(34C37\), \(37C29\), \(34C28\), and \(37G35\). The first code is used here.

## Proof
Let \(L\) denote the flow generator.

For any continuous function \(\phi\) on the compact \(z\)-projection of the support, choose an antiderivative \(F\) with
\[
F'(z)=\phi(z).
\]
Then
\[
LF
=
\phi(z)(xy-z).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(z)(xy-z)]=0
\]
for every \(\phi\), hence
\[
\mathbb E_\mu[xy\mid z]=z.
\]

The same argument with arbitrary antiderivatives in \(x\) gives
\[
\mathbb E_\mu[
\phi(x)
(
y(h-z)-\nu_1x
)
]
=
0,
\]
so
\[
\mathbb E_\mu[y(h-z)\mid x]=\nu_1x.
\]
Using arbitrary functions of \(y\) similarly gives
\[
\mathbb E_\mu[x(h+z)\mid y]=\nu_2y.
\]

Now consider
\[
S=\frac{x^2+y^2}{2}.
\]
The cubic interaction terms cancel:
\[
\dot S
=
2hxy-\nu_1x^2-\nu_2y^2.
\]
Taking stationary expectations and using
\[
\mathbb E[xy]=\mathbb E[z]=m
\]
gives
\[
\nu_1\mathbb E[x^2]
+
\nu_2\mathbb E[y^2]
=
2hm.
\]

Next consider
\[
D=\frac{x^2-y^2}{2}.
\]
A direct calculation gives
\[
\dot D
=
-\nu_1x^2+\nu_2y^2-2xyz.
\]
Stationarity of
\[
\frac{z^2}{2}
\]
gives
\[
0
=
\mathbb E[-z^2+xyz],
\]
so
\[
\mathbb E[xyz]=q.
\]
Therefore
\[
-\nu_1\mathbb E[x^2]
+
\nu_2\mathbb E[y^2]
=
2q.
\]
Solving the two linear equations yields
\[
\nu_1\mathbb E[x^2]=hm-q,
\]
\[
\nu_2\mathbb E[y^2]=hm+q.
\]

Since
\[
\operatorname{Var}(z)=q-m^2,
\]
the first identity becomes
\[
\operatorname{Var}(z)
+
\nu_1\mathbb E[x^2]
=
m(h-m).
\]

We now classify the zero defect. If
\[
\mathbb E[x^2]=0,
\]
then
\[
x=0
\]
on the invariant support. Along a complete support trajectory the second equation reduces to
\[
\dot y=-\nu_2y.
\]
A nonzero solution of this scalar equation cannot remain bounded for all positive and negative times, so compact completeness forces
\[
y=0.
\]
Then
\[
\dot z=-z
\]
and the same argument forces
\[
z=0.
\]
Thus the invariant measure is the origin atom. The converse is immediate.

For any non-origin invariant measure,
\[
\mathbb E[x^2]>0,
\]
hence
\[
q<hm.
\]
On the other hand Jensen's inequality gives
\[
q\ge m^2.
\]
The inequality
\[
q<hm
\]
rules out
\[
m\le0.
\]
Thus
\[
m>0.
\]
Combining
\[
m^2\le q<hm
\]
with \(m>0\) gives
\[
m<h.
\]

The slab statement follows from
\[
\mathbb E[z(z-h)]
=
q-hm
=
-\nu_1\mathbb E[x^2]
<
0.
\]
The continuous scalar function
\[
z(z-h)
\]
is negative exactly on
\[
0<z<h.
\]
A negative expectation is therefore impossible unless that interval has positive invariant mass.

Finally, each conditional law is an \(L^2(\mu)\) regression identity. For example,
\[
xy=z+\dot z
\]
with
\[
\mathbb E[\dot z\mid z]=0.
\]
Hence the residual \(\dot z\) is orthogonal to every square-integrable function of \(z\), yielding
\[
\operatorname{Var}(xy)
=
\operatorname{Var}(z)
+
\mathbb E[\dot z^2].
\]
The other two speed-defect decompositions follow identically.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the two quadratic derivatives
\[
\frac{d}{dt}\frac{x^2+y^2}{2}
=
2hxy-\nu_1x^2-\nu_2y^2
\]
and
\[
\frac{d}{dt}\frac{x^2-y^2}{2}
=
-\nu_1x^2+\nu_2y^2-2xyz.
\]

It verifies the stationary linear solve
\[
\nu_1\mathbb E[x^2]=hm-q,
\qquad
\nu_2\mathbb E[y^2]=hm+q,
\]
and the exact conversion to
\[
\operatorname{Var}(z)
+
\nu_1\mathbb E[x^2]
=
m(h-m).
\]

It also checks the three pointwise residual identities and the abstract orthogonal-regression variance formula.

For the exact rational representation
\[
h=\frac{123}{25},
\qquad
\nu_1=1,
\qquad
\nu_2=4,
\]
the checker verifies the concrete parabola
\[
\operatorname{Var}(z)+\mathbb E[x^2]
=
m\left(\frac{123}{25}-m\right).
\]

The stored checker output is `VERIFY_OK`.

The invariant-measure quantifiers, origin rigidity, strict mean-height interval, and positive slab-mass consequence are analytic proofs rather than finite numerical experiments.

## Relationship to prior work
Rabinovich's 1978 review places low-dimensional stochastic self-oscillation and strange-attractor mechanisms in the context of turbulence and plasma-wave interactions.

A 2008 global mathematical study analyzes the Rabinovich system by Poincaré compactification, identifies parameter sets with first integrals or invariants, describes heteroclinic cycles, and reports a four-wing strange attractor. Its stated results concern global phase portraits and recurrence geometry rather than stationary moment disintegrations.

A 2011 Hamiltonian-geometry study develops Lie–Poisson realizations, equilibrium stability, periodic orbits, and global geometric behavior for the same system.

The complete open 2018 same-system article writes the original plasma-wave equations explicitly, proves boundedness through an absorbing set in transformed coordinates, and studies self-excited and hidden attractors together with finite-time Lyapunov dimension. Full-document searches found no `covariance`, `invariant measure`, or `stationary moment` formulation. The only `moment` occurrence located by search was ordinary prose referring to a moment of time.

The closest published stationary-law record found by semantic search concerns the Rabinovich–Fabrikant system. That is a different vector field. Its heightwise law
\[
\mathbb E[xy\mid z]=-\alpha
\]
does not imply the classical Rabinovich calibration
\[
\mathbb E[xy\mid z]=z
\]
or the pump-height parabola proved here.

The accepted result therefore concerns a different structural layer of the original plasma-wave model: fiberwise wave-transfer calibration, exact first-two-height-moment reduction of both transverse wave energies, and a parameter-selected recurrent slab.

## Limitations
The theorem requires a compactly supported invariant probability measure. It does not prove existence, uniqueness, or stability of a chaotic attractor for arbitrary parameters.

The parabola controls selected stationary second moments but does not determine the invariant distribution or Lyapunov spectrum.

The slab result guarantees positive invariant mass in
\[
0<z<h,
\]
but does not require a recurrent state to cross both slab boundaries.

The historical 1978 source was verified only to month resolution, so the structured source date uses the earliest checked day-resolved same-system source instead of inventing a historical day.

The complete 2018 same-system article was inspected, while the 2008 and 2011 mathematical sources were compared from their published abstracts, metadata, and exposed statements rather than complete locally parsed copies.

Because the generator identities are short, an equivalent observation could remain in unindexed plasma-dynamics literature.

## References
1. M. I. Rabinovich, “Stochastic self-oscillations and turbulence,” *Soviet Physics Uspekhi* 21, 443–469 (1978), DOI 10.1070/PU1978v021n05ABEH005555.
2. J. Llibre, M. Messias, and P. R. da Silva, “On the global dynamics of the Rabinovich system,” *Journal of Physics A: Mathematical and Theoretical* 41, 275210 (2008), DOI 10.1088/1751-8113/41/27/275210.
3. R. M. Tudoran and A. Gîrban, “On the Hamiltonian dynamics and geometry of the Rabinovich system,” *Discrete and Continuous Dynamical Systems - B* 15, 789–823 (2011), DOI 10.3934/dcdsb.2011.15.789.
4. N. V. Kuznetsov, G. A. Leonov, T. N. Mokaev, A. Prasad, and M. D. Shrimali, “Finite-time Lyapunov dimension and hidden attractor of the Rabinovich system,” *Nonlinear Dynamics* 92, 267–285 (2018), DOI 10.1007/s11071-018-4054-z.
