# Exact forcing balance laws and a sign trichotomy for the Burke–Shaw flow

Consider the classical Burke–Shaw system
\[
\dot x=-a(x+y),\qquad
\dot y=-kxz-y,\qquad
\dot z=gxy+d,
\]
with \(a,k,g>0\) and \(d\in\mathbb R\).

## Result

Define
\[
W=y^2+\frac{k}{g}z^2,\qquad
H=z+\frac{g}{2a}x^2.
\]
Every solution exists for all forward time, and the following exact identities hold:
\[
\dot W=-2y^2+2\frac{k}{g}dz,\qquad
\dot H=d-gx^2,
\]
together with
\[
\frac{d}{dt}x^2=-2ax^2-2axy,\qquad
\dot x^2=a^2(x+y)^2.
\]

These identities give a sharp trichotomy with respect to the constant forcing \(d\).

### 1. Negative forcing: no bounded forward recurrence

If \(d<0\), then
\[
H(t)=H(0)+dt-g\int_0^t x(s)^2\,ds\le H(0)+dt.
\]
Since \(z=H-\frac{g}{2a}x^2\le H\),
\[
z(t)\le H(0)+dt\longrightarrow-\infty .
\]
Hence no forward orbit is bounded. In particular, there are no periodic orbits or compact invariant sets.

### 2. Zero forcing: global convergence to the equilibrium line

If \(d=0\), then
\[
\dot W=-2y^2\le0.
\]
Thus \(y,z\) are bounded and \(y\in L^2(0,\infty)\). The \(x\)-equation is a stable linear equation driven by bounded \(y\), so \(x\) is bounded. Moreover,
\[
\frac{d}{dt}x^2
=-2ax^2-2axy
\le -ax^2+ay^2,
\]
and therefore \(x\in L^2(0,\infty)\). Consequently \(xy\in L^1(0,\infty)\), while
\[
\dot z=gxy,
\]
so \(z(t)\) converges to a finite limit \(z_\infty\).

Because
\[
\dot y=-kxz-y
\]
is bounded, \(y\) is uniformly continuous; together with \(y\in L^2\), this gives \(y(t)\to0\). Finally, the stable filter
\[
\dot x+a x=-ay
\]
and \(y(t)\to0\) imply \(x(t)\to0\). Hence every solution satisfies
\[
(x(t),y(t),z(t))\longrightarrow(0,0,z_\infty).
\]
Thus the entire forcing-free system converges globally to the equilibrium line
\[
\{(0,0,z):z\in\mathbb R\}.
\]

### 3. Positive forcing: universal averages for every bounded orbit

Assume \(d>0\) and let \((x(t),y(t),z(t))\) be any bounded forward trajectory. Write
\[
A_T(f)=\frac1T\int_0^T f(t)\,dt.
\]
The boundedness of \(H,x,W\) and the balance identities imply
\[
A_T(x^2)\longrightarrow \frac{d}{g},
\qquad
A_T(xy)\longrightarrow-\frac{d}{g}.
\]
Furthermore,
\[
A_T(z)-\frac1k-\frac{g}{kda^2}A_T(\dot x^2)\longrightarrow0.
\]
In particular,
\[
\liminf_{T\to\infty}A_T(z)\ge\frac1k.
\]

For a periodic orbit of period \(P\),
\[
\frac1P\int_0^P x^2\,dt=\frac{d}{g}
\]
and
\[
\frac1P\int_0^P z\,dt
=
\frac1k+
\frac{g}{kda^2P}\int_0^P\dot x^2\,dt.
\]
The second inequality is strict for every non-equilibrium periodic orbit:
\[
\frac1P\int_0^P z\,dt>\frac1k.
\]

Equivalently, if \(\mu\) is any invariant probability measure supported on a compact invariant set, then
\[
\int x^2\,d\mu=\frac{d}{g},\qquad
\int xy\,d\mu=-\frac{d}{g},
\]
and
\[
\int z\,d\mu
=
\frac1k+
\frac{g}{kd}\int (x+y)^2\,d\mu
\ge\frac1k.
\]
Equality holds exactly for invariant measures supported on the two equilibria
\[
E_\pm=
\left(\pm\sqrt{\frac dg},\mp\sqrt{\frac dg},\frac1k\right).
\]

Thus every bounded recurrent regime at \(d>0\), regardless of whether it is periodic or chaotic, has the exact root-mean-square constraint
\[
\sqrt{\langle x^2\rangle}=\sqrt{\frac dg},
\]
while its mean \(z\)-level cannot lie below the equilibrium level \(1/k\).

## Proof details

### Forward completeness

From
\[
\dot W=-2y^2+2\frac{k}{g}dz
\]
and \(2dz\le z^2+d^2\),
\[
\dot W\le W+\frac{k}{g}d^2.
\]
Gronwall's inequality bounds \(y\) and \(z\) on every finite time interval. The equation
\[
\dot x+a x=-ay
\]
then bounds \(x\) on every finite interval as well. Since the vector field is polynomial, a maximal solution cannot terminate at finite positive time while all three coordinates remain finite. Hence solutions are forward complete.

### Positive-forcing average identities

For bounded trajectories,
\[
\frac{H(T)-H(0)}{T}
=
d-gA_T(x^2)\longrightarrow0,
\]
which gives \(A_T(x^2)\to d/g\). Likewise,
\[
\frac{x(T)^2-x(0)^2}{T}
=
-2aA_T(x^2)-2aA_T(xy)\longrightarrow0,
\]
so \(A_T(xy)\to-d/g\).

Finally,
\[
\frac{W(T)-W(0)}{T}
=
-2A_T(y^2)+2\frac{k}{g}dA_T(z)\longrightarrow0,
\]
hence
\[
A_T(z)-\frac{g}{kd}A_T(y^2)\longrightarrow0.
\]
But
\[
y^2=(x+y)^2-x^2-2xy
\]
and \(\dot x^2=a^2(x+y)^2\), so substitution of the already established averages yields
\[
A_T(z)-\frac1k-\frac{g}{kda^2}A_T(\dot x^2)\longrightarrow0.
\]

For a compactly supported invariant probability measure, integrating the infinitesimal-generator identities for \(H,x^2,W\) gives the corresponding exact measure identities. If equality \(\int z\,d\mu=1/k\) holds, then \(x+y=0\) on the support. Invariance then forces every bounded orbit in the support to be one of \(E_\pm\): on \(x+y=0\), preservation of that relation requires either \(x=0\) or \(z=1/k\); the \(x=0\) orbit has \(\dot z=d>0\) and cannot remain in a compact invariant set, while \(z=1/k\) forces \(x^2=d/g\).

## Context and originality boundary

The Burke–Shaw equations and standard chaotic parameter choices are documented in the modern Lorenz-type-system literature. Panchev, Spassova and Vitanov studied the Burke–Shaw family together with temporal and parametric asymptotes, while a later mechanical analysis decomposed the system into torque contributions and concluded that the full collection of torque types is required for chaos.

The contribution here is restricted to the exact two-function balance mechanism above and its combined consequences: forward completeness for arbitrary forcing, unavoidable escape for \(d<0\), global convergence to the equilibrium line for \(d=0\), and parameter-exact long-time constraints for every bounded trajectory and compactly supported invariant measure when \(d>0\).

No exact statement of this combined sign trichotomy or the identities
\[
\langle x^2\rangle=d/g,\qquad
\langle z\rangle
=
1/k+\frac{g}{kd}\langle(x+y)^2\rangle
\]
was located in the literature checked. The full text of Panchev–Spassova–Vitanov (2007) was not inspected; its abstract explicitly mentions temporal asymptotes for the Burke–Shaw system, so it is the strongest unresolved prior-coverage risk. The full text of Shukla et al. (2026) was also not inspected; its abstract overlaps the qualitative role of the external forcing/torque in chaos, but does not expose the global convergence or invariant-average formulas proved here.

## Reproducibility

`artifacts/verify_burke_shaw_balances.py` symbolically differentiates \(W,H,x^2\) along the vector field and verifies the four algebraic identities used in the proof. `artifacts/verification.txt` records the zero residuals.

## References

1. S. Panchev, T. Spassova, N. K. Vitanov, “Analytical and numerical investigation of two families of Lorenz-like dynamical systems,” *Chaos, Solitons & Fractals* 33 (2007), 1658–1671. DOI: https://doi.org/10.1016/j.chaos.2006.03.037
2. “The fractional-order Lorenz-type systems: A review,” *Fractional Calculus and Applied Analysis* (2022). DOI: https://doi.org/10.1007/s13540-022-00016-4
3. V. K. Shukla, A. K. Pandey, S. Acharya, A. Kumar, N. K. Tripathi, P. K. Mishra, “Mechanical Analysis of Burke-Shaw Chaotic System,” *Discontinuity, Nonlinearity, and Complexity* 15(1) (2026), 99–107. DOI: https://doi.org/10.5890/DNC.2026.03.007
