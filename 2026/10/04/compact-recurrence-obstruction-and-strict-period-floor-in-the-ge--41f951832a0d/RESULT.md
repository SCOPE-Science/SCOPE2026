# Compact-recurrence obstruction and strict period floor in the generalized Sprott M flow

## Finding
For the generalized Sprott M flow \(\dot x=-z,\ \dot y=-x^2-y,\ \dot z=a+bx+y\) with \(a>0\), let \(r_\pm=(b\pm\sqrt{b^2+4a})/2\). Every compactly supported invariant probability measure \(\mu\) has support in \(y<0\) and obeys \(\mathbb E_\mu[z]=0\), \(\mathbb E_\mu[x^2]=a+b\mathbb E_\mu[x]\), hence \(\operatorname{Var}_\mu(x)=(r_+-m)(m-r_-)\) for \(m=\mathbb E_\mu[x]\), and the exact derivative-energy law \(\mathbb E_\mu[(a+bx+y)^2]=b\mathbb E_\mu[z^2]\). Consequently, if \(b\le 0\), every compactly supported invariant probability measure is a convex combination of the two equilibrium point masses at \(E_\pm=(r_\pm,-r_\pm^2,0)\), so there is no non-equilibrium compact recurrence. If \(b>0\), every compact invariant measure not supported on \({E_-,E_+}\) gives positive mass both to \(r_-<x<r_+\) and to \(x<r_-\) or \(x>r_+\), and positive mass to each of \(z>0\) and \(z<0\). Every nonconstant periodic orbit has least period \(P>2\pi/\sqrt b\), stays in \(y<0\), crosses \(z=0\) at least twice per least period, and visits both the interior and exterior \(x\)-regions.

## Assumptions and scope
Consider the two-parameter Sprott M family
\[
\dot x=-z,\qquad \dot y=-x^2-y,\qquad \dot z=a+bx+y,
\]
with \(a>0\) and \(b\in\mathbb R\). Sprott's parameter-space normalization gives this family and the canonical chaotic choice \(a=b=1.7\). Let \(\mu\) be a compactly supported invariant Borel probability measure. For periodic-orbit statements, \(P\) denotes the least positive period.

Define
\[
p(x)=x^2-bx-a=(x-r_-)(x-r_+),\qquad r_\pm=\frac{b\pm\sqrt{b^2+4a}}2,
\]
and \(w=a+bx+y=\dot z\). The two equilibria are \(E_\pm=(r_\pm,-r_\pm^2,0)\).

## Proof
Invariance gives zero mean to the generator of every smooth observable on the compact support. Applying this to the coordinate functions gives
\[
\mathbb E[z]=0,\qquad \mathbb E[y]=-\mathbb E[x^2],\qquad \mathbb E[x^2]=a+b\mathbb E[x].
\]
Writing \(m=\mathbb E[x]\),
\[
\operatorname{Var}(x)=a+bm-m^2=(r_+-m)(m-r_-),
\]
so \(m\in[r_-,r_+]\), and equivalently \(\mathbb E[p(x)]=0\).

There is also a pointwise support constraint. Along any bounded complete trajectory,
\[
y(t)=-\int_0^\infty e^{-s}x(t-s)^2\,ds.
\]
The integral cannot vanish: otherwise \(x\) would vanish on the whole backward half-orbit, forcing \(z=0\), while the simultaneous equations for \(y\) and \(z\) would contradict \(a>0\). Hence every bounded complete trajectory has \(y(t)<0\), and therefore every compact invariant support lies in \(y<0\).

For the derivative-energy identity, set
\[
H(x)=\frac{x^3}{3}-\frac b2x^2-ax.
\]
Direct differentiation along the vector field gives
\[
LH=-zp(x),\qquad L\!\left(\frac{z^2}{2}\right)=zw,
\]
and
\[
L(zw)=w^2-bz^2-zp(x)-zw.
\]
After integration against \(\mu\), the first two identities cancel the last two mixed terms, yielding
\[
\mathbb E[w^2]=b\mathbb E[z^2].
\]
If \(b<0\), nonnegativity forces \(w=z=0\) on the invariant support; invariance then forces \(p(x)=0\), hence support on \(E_-\) and \(E_+\). If \(b=0\), the same identity gives \(w=a+y=0\); invariance gives \(x^2=a\), and continuity of the orbit forces \(x\) constant and \(z=0\), again leaving only the two equilibria. Thus for \(b\le0\), every compact invariant probability measure is a convex combination of the two equilibrium point masses.

Now assume \(b>0\). If an invariant measure is not supported on the two equilibria, then \(p(x)\) is not almost surely zero. Since \(\mathbb E[p(x)]=0\), and \(p(x)<0\) exactly on \(r_-<x<r_+\), the measure must assign positive mass both to that interval and to its strict exterior. Likewise \(\mathbb E[z]=0\); if \(z\) vanished almost surely, invariance would reduce the support to the equilibria. Hence every other compact invariant measure gives positive mass to both signs of \(z\).

For a nonconstant periodic orbit, the invariant measure is normalized time measure. Since \(w=\dot z\), the exact energy law is
\[
\int_0^P \dot z^2\,dt=b\int_0^P z^2\,dt,
\qquad \int_0^P z\,dt=0.
\]
The orbit is nonconstant, so \(z\not\equiv0\). Wirtinger's inequality gives \(P\ge2\pi/\sqrt b\). Equality would force \(z\) to be a first harmonic of frequency \(\sqrt b\), hence \(x\) to be a constant plus a nonzero first harmonic. Eliminating \(y,z\) from the flow gives the exact jerk equation
\[
\dddot x+\ddot x+b\dot x=x^2-bx-a.
\]
For a first-harmonic \(x\), the left side has no second harmonic while \(x^2\) has a nonzero second harmonic, a contradiction. Therefore \(P>2\pi/\sqrt b\). The sign and slab-crossing conclusions follow from the support facts above and continuity of a periodic trajectory.

## Verification
The included `verify.py` uses exact rational sparse-polynomial arithmetic from Python's standard library. It reconstructs the vector field and checks the three generator identities used in the energy cancellation, the scalar jerk elimination identity, and the canonical \(a=b=17/10\) equilibrium polynomial. Replaying the packaged checker returns `VERIFY_OK`.

## Relationship to prior work
Sprott's 1994 paper introduced the nineteen simple quadratic chaotic flows, tabulated Case M, its critical points, Lyapunov exponents, and fractal dimension, and discussed numerical parameter variation. The substantive article pages were inspected in full. Sprott's later parameter-space note explicitly gives the generalized Case M equations above and numerically maps stable, periodic, chaotic, and unbounded regions. Neither inspected source states the invariant-measure variance law, the derivative-energy identity, the \(b\le0\) compact-recurrence obstruction, or the strict universal period floor.

The 1999 ABS modification replaces the quadratic term by an absolute value and is functionally equivalent to a different ABS jerk equation; it is not an equivalent formulation of the quadratic Case M used here. Broader jerk literature studies numerical chaotic examples and nonchaotic parameter regions, but the inspected statements do not imply this exact compact-recurrence theorem. Semantic database searches for Sprott M, invariant measures, the exact jerk form, recurrence balance, and period bounds returned only analogous results for other vector fields.

## Limitations
The theorem does not assert that non-equilibrium compact recurrence exists for every \(b>0\); it proves only that \(b>0\) is necessary and gives exact constraints whenever such recurrence exists. It does not determine stability, entropy, basin size, or the sharp infimum of periods if the lower bound is not approached. The literature search cannot rule out an older result hidden under substantially different terminology or unavailable indexing.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI: 10.1103/PhysRevE.50.R647.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows” (2013; revised 2014), https://sprott.physics.wisc.edu/technote/regions.htm.
3. L. Finco and J. C. Sprott, “More Simple Chaotic Flows with ABS nonlinearity” (1999), https://sprott.physics.wisc.edu/chaos/finco/abs.html.
4. J. C. Sprott, “Some simple chaotic jerk functions,” American Journal of Physics 65, 537–543 (1997), DOI: 10.1119/1.18585.
5. F. Zhang, J. Heidel, and R. Le Borne, “Determining nonchaotic parameter regions in some simple chaotic jerk functions,” Chaos, Solitons & Fractals 36, 862–873 (2008), DOI: 10.1016/j.chaos.2006.07.005.
