# Exact conditional-temperature and radial covariance laws in the Sprott A/Nosé–Hoover flow
## Finding
Consider the one-parameter Sprott A/Nosé–Hoover system
\[
\dot x=y,\qquad
\dot y=-x-yz,\qquad
\dot z=y^2-a,
\]
with \(a\in\mathbb R\), and write
\[
Q=x^2+y^2+z^2.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the conditional stationary-temperature law
\[
\mathbb E_\mu[y^2\mid z]=a.
\]
If \(a\ne0\), it also satisfies the radial-shell balance
\[
\mathbb E_\mu[z\mid Q]=0.
\]

For \(a>0\), every such measure obeys the exact radial–kinetic covariance identity
\[
\operatorname{Cov}_\mu(y^2,Q)
=
2a\,\mathbb E_\mu[z^2]
=
\frac{1}{2a}\mathbb E_\mu[(LQ)^2]
>0,
\]
where \(L\) is the generator of the flow. Thus no compact invariant probability measure for \(a>0\) can be supported on a single sphere \(Q=\text{constant}\).

For \(a<0\), no compactly supported invariant probability measure exists. For \(a=0\), the compactly supported invariant probability measures are exactly the compactly supported probabilities on the equilibrium line
\[
\{(0,0,z):z\in\mathbb R\}.
\]

For \(a>0\), every compact invariant probability measure gives positive mass to both \(y>0\) and \(y<0\), to both \(z>0\) and \(z<0\), and to both
\[
|y|<\sqrt a
\qquad\text{and}\qquad
|y|>\sqrt a.
\]
Consequently every nonconstant periodic orbit crosses each of
\[
y=0,\qquad z=0,\qquad |y|=\sqrt a
\]
at least twice in each least period.

At the canonical Sprott A value \(a=1\),
\[
\mathbb E_\mu[y^2\mid z]=1,\qquad
\mathbb E_\mu[z\mid Q]=0,\qquad
\operatorname{Cov}_\mu(y^2,Q)
=
2\mathbb E_\mu[z^2]
=
\frac12\mathbb E_\mu[(LQ)^2]
>0.
\]

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the flow and supported on compact invariant subsets of \(\mathbb R^3\). Compact support guarantees integrability of every polynomial and continuously differentiable test function used below. The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The system is the Sprott A flow and, for positive \(a\), is equivalent by the standard scaling used in the literature to the one-dimensional Nosé–Hoover oscillator. The earliest verified public source used for this object is the 1986 Posch–Hoover–Vesely oscillator paper; Sprott identified the same flow as case A in 1994.

## Proof
For every continuously differentiable test function \(h\) for which the generator is integrable, invariance gives
\[
\int Lh\,d\mu=0.
\]

First take a function depending only on \(z\). Since
\[
Lh(z)=h'(z)(y^2-a),
\]
we have
\[
\int \phi(z)(y^2-a)\,d\mu=0
\]
for every continuous \(\phi\) on the compact \(z\)-range of the support, by choosing an antiderivative \(h\) of \(\phi\). This is exactly
\[
\mathbb E_\mu[y^2-a\mid z]=0,
\]
hence
\[
\mathbb E_\mu[y^2\mid z]=a.
\]
In particular,
\[
\mathbb E_\mu[y^2]=a.
\]

Therefore \(a<0\) is impossible for a probability measure. If \(a=0\), then \(y=0\) almost surely. The polynomial identity
\[
L(xy)=y^2-x^2-xyz
\]
then gives
\[
\mathbb E_\mu[x^2]=0,
\]
so \(x=0\) almost surely. The line \(x=y=0\) consists entirely of equilibria when \(a=0\), and every compactly supported probability on that line is invariant. This proves the complete \(a\le0\) classification.

Now assume \(a\ne0\). Direct differentiation gives
\[
LQ=-2az.
\]
For any continuously differentiable \(H\),
\[
L(H(Q))=-2a\,H'(Q)z.
\]
As before, arbitrary continuous functions of \(Q\) can be realized as \(H'\) on the compact \(Q\)-range. Hence
\[
\mathbb E_\mu[z\mid Q]=0.
\]
In particular,
\[
\mathbb E_\mu[z]=0.
\]

A second exact generator identity is
\[
L(zQ)=(y^2-a)Q-2az^2.
\]
After integration,
\[
\mathbb E_\mu[(y^2-a)Q]=2a\,\mathbb E_\mu[z^2].
\]
Since \(\mathbb E_\mu[y^2]=a\), the left-hand side is
\[
\operatorname{Cov}_\mu(y^2,Q).
\]
Also \(LQ=-2az\), so
\[
2a\,\mathbb E_\mu[z^2]
=
\frac{1}{2a}\mathbb E_\mu[(LQ)^2].
\]
This proves the exact covariance formula.

For \(a>0\), the right-hand side is strictly positive. Indeed, if \(z=0\) almost surely, invariance of the support would force every complete trajectory in the support to remain in \(z=0\). Along such a trajectory,
\[
\dot z=y^2-a=0,
\]
so \(y^2=a\) for all time. Continuity then makes \(y\) a nonzero constant on that trajectory, and \(\dot x=y\) makes \(x\) unbounded, contradicting compactness. Thus \(\mathbb E_\mu[z^2]>0\).

The sign-excursion statements now follow from zero means and nondegeneracy. Since \(Lx=y\),
\[
\mathbb E_\mu[y]=0,
\]
while \(\mathbb E_\mu[y^2]=a>0\); therefore both signs of \(y\) have positive mass. We have already shown \(\mathbb E_\mu[z]=0\) and \(\mathbb E_\mu[z^2]>0\), so both signs of \(z\) have positive mass. Finally
\[
\mathbb E_\mu[y^2-a]=0.
\]
The quantity \(y^2-a\) cannot vanish almost surely on a compact invariant support: otherwise every support trajectory would have \(y^2=a\) for all time, again forcing a nonzero constant \(y\) and unbounded \(x\). Hence \(y^2-a\) has both signs with positive mass.

On a nonconstant periodic orbit, the normalized orbit measure is compact and invariant. Each continuous periodic function \(y\), \(z\), and \(y^2-a\) therefore takes both signs. Each must cross zero at least twice on the periodic circle, giving the three crossing statements.

## Verification
The accompanying dependency-free checker uses exact sparse-polynomial arithmetic over rational coefficients. It verifies
\[
Lz=y^2-a,\qquad
LQ=-2az,
\]
\[
L(zQ)=(y^2-a)Q-2az^2,
\]
and
\[
L(xy)=y^2-x^2-xyz.
\]
The stored checker output is `VERIFY_OK`.

The conditional-expectation steps are not finite experiments: they follow from the invariant-measure generator identity applied to arbitrary antiderivatives of continuous functions on compact coordinate ranges. The strictness argument uses invariance of the support of an invariant probability measure under a continuous flow.

## Relationship to prior work
Posch, Hoover, and Vesely studied the equivalent one-dimensional Nosé oscillator in 1986 and documented regular and chaotic trajectories in the thermostat model. Sprott's 1994 case A is the same flow in the later simple-chaotic-flow classification.

Messias and Reinol studied the Sprott A system globally. Their 2017 full-text paper proves that at \(a=0\), the spheres
\[
x^2+y^2+z^2=r^2
\]
are invariant and analyzes their heteroclinic dynamics; for \(a\ne0\), they show those spheres are no longer invariant algebraic surfaces and study hidden chaotic attractors and nested invariant tori. Their 2018 full-text paper proves absence of invariant algebraic surfaces and polynomial first integrals for \(a\ne0\) and establishes periodic-orbit and KAM-torus results for positive small \(a\).

The present result is different in logical form: it is a statement about every compact invariant probability measure, including measures supported on periodic orbits, invariant tori, or more complicated compact recurrent sets. The identity
\[
\operatorname{Cov}_\mu(y^2,Q)
=
\frac{1}{2a}\mathbb E_\mu[(LQ)^2]
\]
quantifies the statistical remnant of the exact spherical first integral that exists at \(a=0\). The inspected same-object sources do not state this conditional-temperature law, the radial-shell conditional law, or the strict radial–kinetic covariance identity.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not classify noncompact invariant measures, and it does not assert ergodicity of the Nosé–Hoover oscillator. In particular, the result is compatible with the familiar noncompact canonical statistical-mechanical measure.

The conditional laws are measure identities, not pointwise conservation laws. For \(a>0\), the result does not classify all invariant tori or chaotic components and does not estimate their Lyapunov exponents.

The 1986 oscillator source was inspected through its publisher abstract and public author-upload metadata rather than through a complete line-by-line reading. The 2004 analytical Sprott-flow paper was available only through indexed metadata/classification during this comparison. Those access limits are retained as bibliographic risks; no whole-document noncoverage claim is made for those sources.

## References
1. H. A. Posch, W. G. Hoover, and F. J. Vesely, “Canonical dynamics of the Nosé oscillator: Stability, order, and chaos,” Physical Review A 33, 4253–4265 (1986), DOI 10.1103/PhysRevA.33.4253.
2. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647.
3. M. Messias and A. C. Reinol, “On the formation of hidden chaotic attractors and nested invariant tori in the Sprott A system,” Nonlinear Dynamics 88, 807–821 (2017), DOI 10.1007/s11071-016-3277-0.
4. M. Messias and A. C. Reinol, “On the existence of periodic orbits and KAM tori in the Sprott A system: a special case of the Nosé–Hoover oscillator,” Nonlinear Dynamics 92, 1287–1297 (2018), DOI 10.1007/s11071-018-4125-1.
5. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 1271–1281 (2004), DOI 10.1016/j.chaos.2003.12.054.
