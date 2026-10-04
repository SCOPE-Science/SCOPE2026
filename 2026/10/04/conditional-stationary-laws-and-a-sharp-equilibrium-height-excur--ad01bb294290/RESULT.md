# Conditional stationary laws and a sharp equilibrium-height excursion in the Liu chaotic system
## Finding
Consider the Liu system
\[
\dot x=a(y-x),\qquad
\dot y=x(b-kz),\qquad
\dot z=h x^2-cz,
\]
with
\[
a,b,c,k,h>0.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the two conditional stationary laws
\[
\mathbb E_\mu[y\mid x]=x
\]
and
\[
\mathbb E_\mu[x^2\mid z]=\frac ch\,z.
\]
In particular, the support of every such measure lies in
\[
z\ge0.
\]

There is also an exact equilibrium-height defect:
\[
\mathbb E_\mu\!\left[
\left(z-\frac{b}{2k}\right)^2
\right]
=
\frac{b^2}{4k^2}
+
\frac{ah}{kc}\,
\mathbb E_\mu[(y-x)^2].
\]
Since
\[
\dot x=a(y-x),
\]
this can equivalently be written
\[
\mathbb E_\mu\!\left[
\left(z-\frac{b}{2k}\right)^2
\right]
=
\frac{b^2}{4k^2}
+
\frac{h}{akc}\,
\mathbb E_\mu[(\dot x)^2].
\]

Equality holds exactly for convex mixtures of the three equilibrium atoms
\[
E_0=(0,0,0),
\]
\[
E_\pm=
\left(
\pm\sqrt{\frac{bc}{hk}},
\pm\sqrt{\frac{bc}{hk}},
\frac bk
\right).
\]

Every compact invariant probability measure not supported on these three equilibria assigns positive mass to
\[
z>\frac bk,
\]
and positive mass to each of
\[
y>x
\qquad\text{and}\qquad
y<x.
\]

Consequently every nonconstant periodic orbit lies in \(z\ge0\), reaches a height strictly above \(b/k\), and crosses the plane \(y=x\) at least twice in each least period.

For the classical parameters
\[
a=10,\qquad b=40,\qquad c=2.5,\qquad k=1,\qquad h=4,
\]
the nonzero equilibria are
\[
(\pm5,\pm5,40),
\]
the conditional height law is
\[
\mathbb E_\mu[x^2\mid z]=\frac58z,
\]
and the defect becomes
\[
\mathbb E_\mu[(z-20)^2]
=
400+16\,\mathbb E_\mu[(y-x)^2]
=
400+\frac4{25}\mathbb E_\mu[(\dot x)^2].
\]
Thus every non-equilibrium compact recurrent statistical state reaches \(z>40\).

## Assumptions and scope
The theorem concerns Borel probability measures invariant under the classical Liu flow and supported on compact subsets of \(\mathbb R^3\). Compact support guarantees integrability of all polynomial and continuously differentiable test functions used below.

All five parameters are assumed positive. The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The height \(b/k\) is not an arbitrary normalization: it is the common height of the two nonzero equilibria. In the published same-object dynamical analysis, the frozen-\(z\) planar subsystem changes from a saddle regime below \(b/k\) to stable planar regimes above that threshold. The theorem below shows that every non-equilibrium compact recurrent statistical state must actually visit above this distinguished height.

## Proof
Let \(L\) denote the generator of the flow. If \(\mu\) is invariant and compactly supported, then
\[
\int L H\,d\mu=0
\]
for every continuously differentiable \(H\).

Take a test function depending only on \(x\). If \(H'(x)=\phi(x)\), then
\[
LH=a\phi(x)(y-x).
\]
Since every continuous \(\phi\) on the compact \(x\)-range has an antiderivative,
\[
\mathbb E_\mu[y-x\mid x]=0.
\]
Therefore
\[
\mathbb E_\mu[y\mid x]=x.
\]

Similarly, if \(K'(z)=\psi(z)\), then
\[
LK=\psi(z)(h x^2-cz).
\]
Thus
\[
\mathbb E_\mu[h x^2-cz\mid z]=0,
\]
which gives
\[
\mathbb E_\mu[x^2\mid z]=\frac ch\,z.
\]
The left side is nonnegative, while \(c/h>0\), so \(z\ge0\) almost surely. Because the support of a measure cannot contain a point in an open set of zero measure, the entire support lies in \(z\ge0\).

The first conditional identity also gives
\[
\mathbb E_\mu[xy]=\mathbb E_\mu[x^2].
\]

Now define the polynomial
\[
F
=
-hxy+\frac h2x^2+bz-\frac k2z^2.
\]
Direct differentiation gives the exact coboundary
\[
LF
=
kc\,z^2-bc\,z-ah(y-x)^2.
\]
After integration,
\[
\mathbb E_\mu[z^2]
-\frac bk\,\mathbb E_\mu[z]
=
\frac{ah}{kc}\,
\mathbb E_\mu[(y-x)^2].
\]
Completing the square yields
\[
\mathbb E_\mu\!\left[
\left(z-\frac{b}{2k}\right)^2
\right]
=
\frac{b^2}{4k^2}
+
\frac{ah}{kc}\,
\mathbb E_\mu[(y-x)^2].
\]

It remains to identify the equality case. Equality holds if and only if
\[
y=x
\]
almost surely. Hence the compact invariant support lies in the plane \(y=x\). Along a complete support trajectory in this plane,
\[
\frac{d}{dt}(y-x)=x(b-kz).
\]
Therefore every support point satisfies either \(x=0\) or \(z=b/k\).

If \(x=0\), then also \(y=0\). The trajectory through \((0,0,z_0)\) satisfies
\[
z(t)=z_0e^{-ct}.
\]
Unless \(z_0=0\), this complete trajectory is unbounded backward in time, contradicting compact invariance of the support. Thus this branch contributes only \(E_0\).

If \(x\ne0\), continuity keeps \(x\ne0\) for a short time, so invariance of \(y=x\) forces
\[
z=\frac bk
\]
through that interval. Hence \(\dot z=0\), giving
\[
h x^2-\frac{bc}{k}=0.
\]
Together with \(y=x\), this yields exactly \(E_+\) and \(E_-\). Conversely, every convex mixture of the three equilibrium atoms is invariant and realizes equality.

For a measure not supported on the equilibria,
\[
\mathbb E_\mu[(y-x)^2]>0,
\]
so the exact defect gives
\[
\mathbb E_\mu\!\left[z\left(z-\frac bk\right)\right]>0.
\]
Since \(z\ge0\) on the support and
\[
z\left(z-\frac bk\right)\le0
\]
throughout \(0\le z\le b/k\), positive expectation is possible only if
\[
\mu\!\left(z>\frac bk\right)>0.
\]

Finally, invariance applied to \(x\) gives
\[
\mathbb E_\mu[y-x]=0.
\]
For a non-equilibrium measure the square of \(y-x\) has positive expectation, so \(y-x\) must take both signs on sets of positive measure.

A nonconstant periodic orbit carries its normalized orbit measure, whose support is the entire orbit. The preceding conclusions therefore hold pointwise for the nonnegativity of \(z\) and give visits to \(z>b/k\). The continuous periodic function \(y-x\) takes both signs, so it crosses zero at least twice on the periodic circle.

## Verification
The accompanying standard-library checker uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies
\[
Lx=a(y-x),
\]
\[
Lz=h x^2-cz,
\]
and the critical polynomial certificate
\[
L\left(
-hxy+\frac h2x^2+bz-\frac k2z^2
\right)
=
kc\,z^2-bc\,z-ah(y-x)^2.
\]

It also checks the three stated equilibrium substitutions and the canonical parameter reductions
\[
E_\pm=(\pm5,\pm5,40),
\qquad
\frac ch=\frac58,
\qquad
\frac{ah}{kc}=16,
\qquad
\frac{h}{akc}=\frac4{25}.
\]

The stored checker output is `VERIFY_OK`. The conditional-expectation steps use arbitrary antiderivatives on compact coordinate ranges; they are not finite sampling arguments. Equality rigidity additionally uses invariance of the support under the complete flow.

## Relationship to prior work
The original Liu paper introduced the three-dimensional chaotic system and studied its Lyapunov exponents, Poincaré map, fractal dimension, continuous spectrum, and compound butterfly structure.

A later full same-object analysis writes exactly
\[
\dot x=a(y-x),\qquad
\dot y=bx-kxz,\qquad
\dot z=-cz+h x^2,
\]
with the classical values \(a=10\), \(b=40\), \(c=2.5\), \(k=1\), \(h=4\), and the same three equilibria. That work studies the complementary-cluster energy-barrier criterion and Hopf bifurcations. In particular, it identifies \(z=b/k\) as the first threshold in the frozen-\(z\) planar linearization: below it the planar origin is a saddle, while above it the planar subsystem enters stable regimes.

The present theorem has a different logical form. It applies simultaneously to every compactly supported invariant probability measure, including measures on periodic orbits and more complicated recurrent components. The threshold \(b/k\) from the prior local phase analysis becomes a universal global recurrence barrier: every non-equilibrium compact recurrent state must put positive stationary mass strictly above it.

A 2008 same-object paper analyzes Hopf bifurcation and the stability of bifurcating periodic solutions, while a 2024 same-object paper studies Jacobi stability and the onset of chaos. The inspected statements from these sources do not imply the conditional stationary laws or the exact height-defect identity above.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not classify unbounded trajectories, prove existence of a nontrivial recurrent component for every positive parameter choice, or give a lower bound on a periodic orbit's period.

The excursion conclusion is one-sided in height: every non-equilibrium compact recurrent state visits \(z>b/k\), but the theorem does not assert that it also visits below \(b/k\).

The original 2004 paper was inspected through its publisher bibliographic record and abstract rather than full text. The 2008 Hopf-bifurcation article was inspected at abstract and bibliographic level. The 2013 same-object article was inspected in full text, including the system definition, equilibria, planar threshold analysis, Hopf section, conclusion, and references. A differently phrased or unindexed older stationary identity could remain undiscovered.

## References
1. C. Liu, T. Liu, L. Liu, and K. Liu, “A new chaotic attractor,” Chaos, Solitons & Fractals 22(5), 1031–1038 (2004), DOI 10.1016/j.chaos.2004.02.060.
2. X. Zhou, Y. Wu, Y. Li, and Z. Wei, “Hopf bifurcation analysis of the Liu system,” Chaos, Solitons & Fractals 36(5), 1385–1391 (2008), DOI 10.1016/j.chaos.2006.09.008.
3. M. T. Yassen, M. M. El-Dessoky, E. Saleh, and E. S. Aly, “On Hopf bifurcation of Liu chaotic system,” Demonstratio Mathematica 46(1), 111–122 (2013), DOI 10.1515/dema-2013-0426.
4. Q. Liu and X. Zhang, “Jacobi Stability Analysis of Liu System: Detecting Chaos,” Mathematics 12(13), 1981 (2024), DOI 10.3390/math12131981.
