# Three exact stationary conditional laws and an equilibrium-height slab obstruction in the Lü flow
## Finding
Consider the Lü system
\[
\dot x=a(y-x),\qquad
\dot y=cy-xz,\qquad
\dot z=xy-bz,
\]
with
\[
a>0,\qquad b>0,\qquad c>0.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the three exact conditional laws
\[
\mathbb E_\mu[y\mid x]=x,
\]
\[
\mathbb E_\mu[xz\mid y]=cy,
\]
and
\[
\mathbb E_\mu[xy\mid z]=bz.
\]

They imply the integrated stationary relations
\[
\mathbb E_\mu[x^2]=b\,\mathbb E_\mu[z],
\]
and
\[
c\,\mathbb E_\mu[y^2]
=
b\,\mathbb E_\mu[z^2].
\]

More sharply,
\[
\mathbb E_\mu[z(z-c)]
=
\frac cb\,
\mathbb E_\mu[(y-x)^2]
\ge0.
\]
Equivalently,
\[
\mathbb E_\mu\!\left[\left(z-\frac c2\right)^2\right]
=
\frac{c^2}{4}
+
\frac cb\,\mathbb E_\mu[(y-x)^2].
\]

Equality holds exactly for convex mixtures of the three equilibrium atoms
\[
e_0=(0,0,0)
\]
and
\[
e_\pm=
\left(
\pm\sqrt{bc},
\pm\sqrt{bc},
c
\right).
\]

Therefore every compact invariant probability measure that is not such an equilibrium mixture gives positive mass to the complement of the equilibrium-height slab
\[
0\le z\le c.
\]
In particular, every nonconstant periodic orbit attains either
\[
z<0
\]
or
\[
z>c.
\]

For the classical chaotic parameters
\[
(a,b,c)=(36,3,20),
\]
the nonzero equilibria have height \(20\) and horizontal magnitude \(\sqrt{60}\), while every non-equilibrium compact recurrent statistical state must place positive mass outside
\[
0\le z\le20.
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the Lü flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of all polynomial and one-variable antiderivative test functions used below. Every support trajectory is bounded and complete.

The parameters are assumed positive. This contains the classical chaotic regime and guarantees three real equilibria:
\[
e_0=(0,0,0),
\qquad
e_\pm=
\left(
\pm\sqrt{bc},
\pm\sqrt{bc},
c
\right).
\]

The original Lü article uses
\[
(a,b,c)=(36,3,20)
\]
as a representative chaotic parameter triple and varies \(c\) to display periodic and chaotic windows.

The earliest verified public source date for the system is 1 March 2002.

## Proof
Let \(L\) denote the generator.

Take any continuous function \(\phi\) on the compact \(x\)-range and choose an antiderivative \(H\) satisfying
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
a\,\phi(x)(y-x).
\]
Invariance and \(a>0\) give
\[
\mathbb E_\mu[\phi(x)(y-x)]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[y\mid x]=x.
\]

Likewise, for any continuous \(\psi\) on the compact \(y\)-range, an antiderivative \(K\) gives
\[
LK
=
\psi(y)(cy-xz).
\]
Thus
\[
\mathbb E_\mu[xz\mid y]=cy.
\]

For any continuous \(\eta\) on the compact \(z\)-range, an antiderivative \(M\) gives
\[
LM
=
\eta(z)(xy-bz),
\]
hence
\[
\mathbb E_\mu[xy\mid z]=bz.
\]

Multiplying the first conditional law by \(x\) and integrating yields
\[
\mathbb E_\mu[xy]
=
\mathbb E_\mu[x^2].
\]
Integrating the third law gives
\[
\mathbb E_\mu[xy]
=
b\,\mathbb E_\mu[z].
\]
Therefore
\[
\mathbb E_\mu[x^2]
=
b\,\mathbb E_\mu[z].
\]

Multiplying the second conditional law by \(y\) gives
\[
\mathbb E_\mu[xyz]
=
c\,\mathbb E_\mu[y^2].
\]
Multiplying the third conditional law by \(z\) gives
\[
\mathbb E_\mu[xyz]
=
b\,\mathbb E_\mu[z^2].
\]
Hence
\[
c\,\mathbb E_\mu[y^2]
=
b\,\mathbb E_\mu[z^2].
\]

Finally,
\[
\mathbb E_\mu[(y-x)^2]
=
\mathbb E_\mu[y^2]
+
\mathbb E_\mu[x^2]
-
2\mathbb E_\mu[xy].
\]
Since
\[
\mathbb E_\mu[xy]
=
\mathbb E_\mu[x^2],
\]
this becomes
\[
\mathbb E_\mu[(y-x)^2]
=
\mathbb E_\mu[y^2]
-
\mathbb E_\mu[x^2].
\]
Using the preceding moment identities gives
\[
\frac cb\,\mathbb E_\mu[(y-x)^2]
=
\mathbb E_\mu[z^2]
-
c\,\mathbb E_\mu[z]
=
\mathbb E_\mu[z(z-c)].
\]

It remains to classify equality. If
\[
\mathbb E_\mu[(y-x)^2]=0,
\]
then the invariant support is contained in the plane
\[
y=x.
\]
Along that plane,
\[
\dot x=0.
\]
Tangency of the plane requires
\[
0
=
\frac d{dt}(y-x)
=
x(c-z).
\]

If \(x=0\), then \(y=0\) and
\[
\dot z=-bz.
\]
The only bounded complete trajectory on this axis is the origin.

If \(x\ne0\), tangency forces
\[
z=c.
\]
Since \(x\) is constant, invariance of \(z=c\) requires
\[
0=\dot z=x^2-bc,
\]
so
\[
x=y=\pm\sqrt{bc}.
\]
Thus the equality support is contained in
\[
\{e_0,e_+,e_-\}.
\]
Conversely every convex mixture of those equilibrium atoms is invariant and has zero defect.

Now suppose a compact invariant measure is not an equilibrium mixture. Then
\[
\mathbb E_\mu[z(z-c)]>0.
\]
But
\[
z(z-c)\le0
\]
for every
\[
0\le z\le c.
\]
Therefore the measure must give positive mass to
\[
z<0
\qquad\text{or}\qquad
z>c.
\]
A nonconstant periodic orbit carries a normalized invariant orbit measure that is not an equilibrium mixture, so the same conclusion holds for its trajectory.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic.

It verifies
\[
L\left(\frac{x^2}{2}\right)
=
a(xy-x^2),
\]
\[
L\left(\frac{y^2}{2}\right)
=
cy^2-xyz,
\]
and
\[
L\left(\frac{z^2}{2}\right)
=
xyz-bz^2.
\]

It also verifies the polynomial coboundary certificate corresponding to
\[
b\,\mathbb E[z(z-c)]
=
c\,\mathbb E[(y-x)^2].
\]

The equilibrium substitutions
\[
y=x,\qquad z=c,\qquad x^2=bc
\]
are replayed symbolically, as is the classical parameter product
\[
bc=60
\]
at
\[
(a,b,c)=(36,3,20).
\]

The stored checker output is `VERIFY_OK`.

The conditional laws use arbitrary one-variable antiderivative tests and therefore are not finite sampling statements. The equality classification uses invariance of the compact support and bounded completeness.

## Relationship to prior work
Lü and Chen introduced the system as a new chaotic attractor connecting the Lorenz and Chen attractors. Their original article gives the equations, the classical parameters, Lyapunov data, and parameter windows containing periodic and chaotic behavior.

The later “Bridge the Gap” analysis embeds the Lü flow into a unified Lorenz–Chen transition family and studies equilibrium structure, linear stability, bifurcation, and numerical orbit geometry. It does not formulate invariant-probability conditional laws.

Leonov and Kuznetsov give a detailed full-text comparison of Lorenz, Chen, and Lü systems, including explicit coordinate/time scalings, the generalized Lorenz representation, homoclinic analysis, Lyapunov-exponent issues, and open problems. The three conditional stationary laws and the equilibrium-height slab defect above are not stated in the inspected text.

Two papers on boundedness of Lü trajectories construct Lyapunov functions and establish boundedness results in parameter regions, culminating in a global-boundedness theorem. Their accessible descriptions concern absorbing or bounded sets rather than stationary disintegration or the exact defect above. Complete text of the 2016 article was unavailable in the inspected lawful sources, so it remains an explicit literature risk rather than a basis for a whole-document noncoverage claim.

Targeted semantic searches using the exact conditional identities, the moment defect, Lorenz/Chen/Lü equivalence language, and invariant-measure terminology returned no same-object statement implying the theorem above.

## Limitations
The theorem concerns compactly supported invariant probability measures and compact recurrent dynamics. It does not prove existence of a chaotic attractor for every positive parameter triple or classify unbounded trajectories.

The slab conclusion is deliberately one-sided: a non-equilibrium recurrent state must place positive mass outside
\[
0\le z\le c,
\]
but the theorem does not force which side of the slab is visited.

The coordinate/time transformations among Lorenz-like systems can transport identities after explicit rescaling. The originality comparison therefore includes generalized-Lorenz and Lorenz–Chen–Lü equivalence literature; no inspected source states the present conditional laws in an equivalent normalization.

The complete 2016 global-boundedness article was unavailable in the inspected lawful sources after bounded access attempts. A differently phrased stationary-moment observation in that or other unindexed literature remains a residual risk.

## References
1. J. Lü and G. Chen, “A New Chaotic Attractor Coined,” International Journal of Bifurcation and Chaos 12, 659–661 (2002), DOI 10.1142/S0218127402004620.
2. J. Lü, G. Chen, D. Cheng, and S. Čelikovský, “Bridge the Gap Between the Lorenz System and the Chen System,” International Journal of Bifurcation and Chaos 12, 2917–2926 (2002), DOI 10.1142/S021812740200631X.
3. G. A. Leonov and N. V. Kuznetsov, “On differences and similarities in the analysis of Lorenz, Chen, and Lu systems,” Applied Mathematics and Computation 256, 334–343 (2015), arXiv:1409.8649, DOI 10.1016/j.amc.2014.12.132.
4. F. Zhang, C. Mu, and X. Li, “On the boundness of some solutions of the Lü system,” International Journal of Bifurcation and Chaos 22, 1250015 (2012), DOI 10.1142/S0218127412500150.
5. F. Zhang, X. Liao, and G. Zhang, “On the global boundedness of the Lü system,” Applied Mathematics and Computation 284, 332–339 (2016), DOI 10.1016/j.amc.2016.03.017.
