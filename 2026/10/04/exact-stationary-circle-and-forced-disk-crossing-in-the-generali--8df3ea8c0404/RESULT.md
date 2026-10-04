# Exact stationary circle and forced disk crossing in the generalized Sprott O flow
## Finding
Consider the generalized Sprott O system
\[
\dot x=y,\qquad
\dot y=x-z,\qquad
\dot z=ax+xz+by,
\]
with \(a>0\) and \(b\in\mathbb R\). Define
\[
F(x,y)=x^2+y^2+ax
=\left(x+\frac a2\right)^2+y^2-\frac{a^2}{4}.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the exact stationary-circle identity
\[
\mathbb E_\mu\!\left[\left(x+\frac a2\right)^2+y^2\right]
=\frac{a^2}{4}.
\]
Writing
\[
m=\mathbb E_\mu[x]=\mathbb E_\mu[z],
\]
one has the exact mean-variance parabola
\[
\operatorname{Var}_\mu(x)+\operatorname{Var}_\mu(y)
=-m(a+m).
\]
Consequently
\[
-a\le m\le0.
\]
The endpoint \(m=0\) occurs only for the equilibrium atom at \((0,0,0)\), and the endpoint \(m=-a\) occurs only for the equilibrium atom at \((-a,0,-a)\).

More strongly, the compact invariant probability measures supported on the boundary circle
\[
\left(x+\frac a2\right)^2+y^2=\left(\frac a2\right)^2
\]
are exactly the convex mixtures of those two equilibrium atoms. Every other compact invariant measure therefore assigns positive mass both to the open disk
\[
\left(x+\frac a2\right)^2+y^2<\left(\frac a2\right)^2
\]
and to its strict exterior. In particular, every nonconstant periodic orbit crosses the boundary circle at least twice per least period.

For the canonical Sprott O parameters \(a=1\), \(b=2.7\), the stationary circle is
\[
\left(x+\frac12\right)^2+y^2=\frac14,
\]
with equilibria \((0,0,0)\) and \((-1,0,-1)\).

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the flow and supported on compact invariant subsets of \(\mathbb R^3\). Compact support guarantees integrability of the polynomial generator identities used below and gives complete trajectories on the support. The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The equations are the two-parameter Case O normalization in Sprott's parameter-region survey, whose displayed chaotic parameters are \(a=1\), \(b=2.7\). The archive anchor is Sprott's original 1994 paper introducing the nineteen simple quadratic flows.

## Proof
Let \(L\) denote the generator. Invariance gives
\[
\int Lh\,d\mu=0
\]
for each polynomial \(h\) used below. The coordinate identities
\[
Lx=y,\qquad Ly=x-z
\]
give
\[
\mathbb E_\mu[y]=0,
\qquad
\mathbb E_\mu[x]=\mathbb E_\mu[z]=m.
\]

The key exact coboundary is
\[
L(xy+z-bx)=x^2+y^2+ax=F(x,y).
\]
Therefore
\[
\mathbb E_\mu[F]=0,
\]
which is equivalent to
\[
\mathbb E_\mu\!\left[\left(x+\frac a2\right)^2+y^2\right]
=\frac{a^2}{4}.
\]
Expanding around the mean and using \(\mathbb E[y]=0\) gives
\[
\operatorname{Var}(x)+\operatorname{Var}(y)
=-m(a+m).
\]
The left side is nonnegative, so \(-a\le m\le0\).

If \(m=0\), both variances vanish, so \(x=y=0\) almost surely. Since \(\mathbb E[z]=0\), stationarity of \(yz\), for which
\[
L(yz)=xz-z^2+axy+xyz+by^2,
\]
then gives \(\mathbb E[z^2]=0\). Thus \(\mu\) is the origin atom. If \(m=-a\), again both variances vanish, so \(x=-a\), \(y=0\) almost surely. The same \(yz\) identity gives
\[
0=\mathbb E[-az-z^2],
\]
and \(\mathbb E[z]=-a\) forces \(\operatorname{Var}(z)=0\); hence \(z=-a\) almost surely.

It remains to characterize invariant measures supported on the circle \(F=0\). The support of an invariant compactly supported measure is invariant. Along any trajectory in \(F=0\), differentiation gives
\[
LF=y(4x-2z+a)=0.
\]
If \(y\) vanishes identically on the trajectory, then \(x\) is constant, \(x=z\), and \(\dot z=x(a+x)=0\), so the trajectory is one of the two equilibria.

Otherwise there is an open time interval on which \(y\ne0\). There
\[
z=2x+\frac a2.
\]
Differentiating this relation and using the vector field yields
\[
(2-b)y=2x^2+\frac{3a}{2}x.
\]
If \(b=2\), the right side must vanish, so \(x\) takes values only in the finite set \(\{0,-3a/4\}\) on an open interval, contradicting \(x'=y\ne0\). If \(b\ne2\), substitution into \(F=0\) yields a nonzero quartic polynomial equation in \(x\), whose leading coefficient after clearing denominators is \(4\). But \(x'=y\ne0\) makes \(x\) range over an interval, so a nonzero polynomial cannot vanish identically there. This is again a contradiction.

Hence every complete trajectory contained in \(F=0\) is an equilibrium. The invariant probabilities supported on \(F=0\) are therefore precisely the convex mixtures of the two equilibrium atoms.

Finally, if an invariant measure is not supported on those equilibria, then \(F\) is not zero almost surely. Since \(\mathbb E[F]=0\), it must take both positive and negative values on sets of positive measure. These are exactly the exterior and interior of the stationary circle. The normalized time measure of any nonconstant periodic orbit is such an invariant measure; continuity on the periodic circle then forces at least two crossings of \(F=0\) in every least period.

## Verification
The accompanying standard-library checker uses exact sparse-polynomial arithmetic over rational coefficients. It verifies
\[
L(xy+z-bx)=x^2+y^2+ax,
\]
\[
LF=y(4x-2z+a),
\]
and the \(L(yz)\) identity used in the endpoint rigidity argument. It also verifies both equilibrium points and the nonzero leading quartic coefficient in the boundary-circle contradiction. The stored checker output is `VERIFY_OK`.

No finite experiment is used as an infinite proof. The only qualitative ingredients beyond the exact identities are invariance of the support of a compactly supported invariant measure and the elementary fact that a nonzero polynomial cannot vanish on an interval.

## Relationship to prior work
Sprott's parameter-region survey gives exactly the generalized Case O equations used here and numerically separates stable, periodic, chaotic, and unbounded regions. The present result is an analytic constraint on every compact recurrent statistical state in the entire half-plane \(a>0\), independent of the numerical regime.

Dimitrova and Yordanov study statistics of low-dimensional Sprott flows through approximate second-order and two-point correlation functions and power spectra. The accessible material for that paper concerns spectral scaling and approximate self-affinity; its full text was not available for a complete comparison, so no whole-document noncoverage claim is made.

A later Shilnikov-oriented classification includes Sprott O among the two-equilibrium Sprott systems and analyzes equilibrium types. A finite-time synchronization paper also uses Sprott O as a network node. Those inspected statements concern equilibrium classification or coupled synchronization rather than a universal invariant-measure circle law.

Panchev's analytical Sprott-flow paper is a particularly relevant broader source because it treats all nineteen systems asymptotically and statistically. Only its indexed abstract and classifications were available in this inspection; it is therefore retained as a bibliographic risk rather than declared noncovering.

Targeted semantic searches over Sprott O, invariant-measure, moment, equilibrium-circle, recurrence, disk-crossing, and period aliases returned no same-object statement implying the theorem above. The closest indexed results concern analogous invariant-measure balance laws for different vector fields.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not classify unbounded trajectories or prove existence of a chaotic attractor for any parameter pair.

The disk-crossing conclusion excludes measures supported on the two equilibrium points; arbitrary convex mixtures of those atoms lie on the circle and are stationary. The theorem gives no lower bound on a nonconstant periodic orbit's period.

The full text of the 2001 statistical Sprott-flow paper and the 2004 analytical Sprott-flow paper was not inspected, so possible differently phrased stationary identities in those sources remain a residual bibliographic risk. Targeted searches also cannot exclude non-digitized or unindexed older statements.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note, 2013, https://sprott.physics.wisc.edu/technote/regions.htm.
3. E. S. Dimitrova and O. I. Yordanov, “Statistics of some Low-Dimensional Chaotic Flows,” International Journal of Bifurcation and Chaos 11 (2001), DOI 10.1142/S0218127401003735.
4. G. Chen et al., “The Related Extension and Application of the Ši′lnikov Theorem,” Mathematical Problems in Engineering (2013), Article 287123, DOI 10.1155/2013/287123.
5. S. Yan and W. Li, “Adaptive Finite-Time Synchronization for Complex Dynamical Network with Different Dimensions of Nodes and Time-Varying Outer Coupling Structures,” Complexity (2018), Article 2474150, DOI 10.1155/2018/2474150.
6. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 1271–1281 (2004), DOI 10.1016/j.chaos.2003.12.054.
