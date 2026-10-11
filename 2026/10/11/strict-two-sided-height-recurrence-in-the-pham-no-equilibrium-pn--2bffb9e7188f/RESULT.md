# Strict two-sided height recurrence in the Pham no-equilibrium PNE1 flow
## Finding
Consider the PNE1 family
\[
\dot x=y,\qquad
\dot y=-x+yz,\qquad
\dot z=-x-a x y-b x z+c,
\]
with real \(a,b\) and \(c\ne0\). For every compactly supported invariant Borel probability measure \(\mu\),
\[
\int y^2z\,d\mu=0.
\]
In fact the cancellation is necessarily genuinely two-sided:
\[
\int_{\{z>0\}}y^2z\,d\mu
=
\int_{\{z<0\}}y^2(-z)\,d\mu
>0.
\]
Consequently every nonempty compact invariant set intersects both open half-spaces \(z>0\) and \(z<0\). In particular, every nonconstant periodic orbit crosses the plane \(z=0\).

The conclusion is independent of the values of \(a\) and \(b\); only \(c\ne0\) is essential.

## Assumptions and scope
The vector field is the PNE1 system introduced by Pham, Volos, Jafari, Wei, and Wang. Their reported parameter choice \(a=15\), \(b=1\), \(c=-0.001\) is included, but the theorem applies to every real \(a,b\) and every nonzero real \(c\).

The measure statement assumes compact support. The set statement assumes a nonempty compact invariant set for the complete flow. No existence, uniqueness, ergodicity, mixing, or chaos claim is made. The theorem is conditional: whenever compact recurrent dynamics exists, it must visit both signs of \(z\).

The restriction \(c\ne0\) is sharp for this argument. At \(c=0\), the unperturbed system has the equilibrium line \(x=y=0\), which is contained in a single \(z\)-half-space after restriction to either side of the origin.

## Proof
Let
\[
E(x,y)=\frac12(x^2+y^2).
\]
Along every solution,
\[
\dot E
=x\dot x+y\dot y
=xy+y(-x+yz)
=y^2z.
\]
If \(\mu\) is a compactly supported invariant probability measure, the invariant-measure generator identity applied to the polynomial observable \(E\) gives
\[
0=\int \dot E\,d\mu=\int y^2z\,d\mu.
\]
Splitting the last integral at \(z=0\) yields
\[
A:=\int_{\{z>0\}}y^2z\,d\mu
=
\int_{\{z<0\}}y^2(-z)\,d\mu=:B,
\]
with \(A=B\ge0\).

It remains to prove strict positivity. Suppose \(A=B=0\). Then the continuous nonnegative function \(y^2|z|\) vanishes on the support \(S=\operatorname{supp}\mu\). The support of an invariant probability measure is a compact invariant set, so every trajectory through \(S\) is a bounded complete trajectory satisfying
\[
y(t)^2z(t)=0
\]
for all \(t\).

If \(z(t_0)>0\) or \(z(t_0)<0\) at some time, continuity gives a time interval on which \(z\) keeps that sign. On that interval \(y=0\). Then \(\dot x=y=0\) and \(\dot y=-x+yz=-x=0\), hence \(x=0\) there. Uniqueness then forces \(x=y=0\) along the entire trajectory. The third equation reduces to \(\dot z=c\), so \(z(t)\) is unbounded because \(c\ne0\), contradicting compactness.

Thus any such bounded complete trajectory would have to satisfy \(z\equiv0\). The first two equations then give the harmonic oscillator
\[
\dot x=y,\qquad \dot y=-x,
\]
while invariance of \(z=0\) requires
\[
x(1+a y)=c
\]
for all time. A nonzero harmonic orbit has \(x=R\cos(t+\phi)\) and \(y=-R\sin(t+\phi)\). Substitution gives a trigonometric polynomial whose first cosine coefficient is \(R\) and whose constant coefficient after subtracting \(c\) is \(-c\). It cannot vanish identically when \(c\ne0\). The zero-amplitude harmonic orbit also requires \(c=0\). This contradiction proves \(A=B>0\).

Finally, every nonempty compact invariant set supports at least one invariant probability measure, obtained for example as a weak limit of time averages along an orbit. If such a set were contained in \(z\ge0\) or in \(z\le0\), the strict two-sided measure law would be impossible. Hence every nonempty compact invariant set meets both \(z>0\) and \(z<0\). Continuity gives the periodic-orbit crossing statement.

## Verification
The accompanying `check.py` reconstructs the polynomial identity
\[
\frac{d}{dt}\frac{x^2+y^2}{2}=y^2z
\]
exactly. It also substitutes the general harmonic solution on the hypothetical invariant plane \(z=0\) and verifies that the constraint \(x(1+a y)-c\equiv0\) has constant coefficient \(-c\) and first cosine coefficient \(R\); therefore it cannot hold for \(c\ne0\). The recorded output is `check_output.txt`.

The verification is algebraic and does not depend on numerical integration. The source's numerical Lyapunov exponents, bifurcation diagram, and plotted periodic orbits are not used as proof of the theorem.

## Relationship to prior work
Pham, Volos, Jafari, Wei, and Wang introduced PNE1 by adding the constant perturbation \(c\) to a line-equilibrium quadratic flow. Their paper states the PNE1 equations, observes that \(c\ne0\) removes all equilibria, and numerically studies chaotic and periodic regimes through Lyapunov exponents, a bifurcation diagram, a Poincaré map, and period doubling. The inspected full text does not state an invariant-measure balance or a theorem forcing every compact recurrent set to visit both signs of \(z\).

The closest checked exact stationary-balance result concerns a different quadratic flow with an equilibrium line and a different third equation. Although that flow also admits a \(y^2z\)-type averaged identity, its result does not imply the PNE1 strict sign-straddling theorem. Other checked recurrence-barrier and stationary-height results concern distinct vector fields and likewise do not dominate the present statement.

The mathematical point here is not merely that one plotted attractor crosses \(z=0\). The exact radial-energy coboundary, together with the absence of equilibria created by \(c\ne0\), forces this crossing geometry for every compact invariant set of the whole PNE1 family.

## Limitations
The theorem does not prove that a compact invariant set exists for a given parameter triple. It does not prove that a reported numerical attractor is chaotic, nor does it determine its invariant measure. The strict law gives no quantitative lower bound on the mass, residence time, or distance attained in either half-space. It also does not apply at \(c=0\), where the equilibrium line returns.

Originality is assessed against the inspected source, targeted scientific database searches, and the closest full result located in the comparison corpus. An unindexed source-specific ergodic or occupation-measure treatment could still exist.

The earliest exact public date located for the source is 28 May 2014; some bibliographic services expose later journal-metadata dates. No earlier public preprint date was located in the checked searches.

## References
1. V.-T. Pham, C. Volos, S. Jafari, Z. Wei, and X. Wang, *Constructing a Novel No-Equilibrium Chaotic System*, International Journal of Bifurcation and Chaos 24(05), 1450073 (2014). DOI: 10.1142/S0218127414500734.
2. MaRDI record Q2920780 for the same article, including MSC classifications headed by 34A34.
