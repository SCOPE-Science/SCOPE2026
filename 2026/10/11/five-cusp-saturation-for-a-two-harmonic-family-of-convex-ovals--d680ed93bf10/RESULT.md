# Five-cusp saturation for a two-harmonic family of convex ovals
## Finding
Let
\[
p(t)=R+a\cos(2t)+b\sin(5t),
\]
where
\[
R>0,\qquad a\ne0,\qquad b\ne0,
\]
and assume
\[
\rho(t):=p(t)+p''(t)
=
R-3a\cos(2t)-24b\sin(5t)>0
\]
for every real \(t\). Then \(p\) is the support function of a smooth strictly convex oval \(C\).

For every such oval,
\[
\#\operatorname{cusps}\bigl(E_{1/2}(C)\bigr)
=
\#\operatorname{cusps}\bigl(\operatorname{CSS}(C)\bigr)
=
5.
\]
All ten singularities counted here are ordinary cusps.

The Wigner-caustic cusp normals are fixed throughout the family:
\[
t\equiv\frac{k\pi}{5}\pmod{\pi},
\qquad k=0,1,2,3,4.
\]

For the centre symmetry set put
\[
\lambda=-\frac{3a}{R}.
\]
Strict convexity implies
\[
|\lambda|<1.
\]
Writing
\[
x=\cos t,
\]
the centre-symmetry-set cusp equation becomes
\[
2xQ_\lambda(x^2)=0,
\]
where
\[
Q_\lambda(y)
=
96\lambda y^3
+(80-168\lambda)y^2
+(-100+98\lambda)y
+25-21\lambda.
\]
For every
\[
-1<\lambda<1,
\]
this polynomial has exactly two simple roots in \((0,1)\). Hence there is one cusp corresponding to \(x=0\) and four more corresponding to
\[
x=\pm\sqrt{y_1},\qquad x=\pm\sqrt{y_2}.
\]

Consequently this whole strictly convex two-harmonic family attains equality in the general cusp-count inequality
\[
\#\operatorname{cusps}(\operatorname{CSS}(C))
\ge
\#\operatorname{cusps}(E_{1/2}(C)).
\]

## Assumptions and scope
The support function is expressed in the normal-angle parameter. The radius of curvature of a support function is
\[
\rho=p+p''.
\]
The stated hypothesis
\[
\rho(t)>0
\]
is exactly the strict-convexity condition for this smooth support parametrization.

The Wigner caustic is the locus of midpoints of chords joining parallel tangent pairs. The centre symmetry set is the envelope of those parallel-tangent chords.

The theorem classifies cusp numbers only for the displayed two-harmonic support family. It does not classify arbitrary Fourier supports or arbitrary smooth convex ovals.

A simple sufficient condition for the convexity hypothesis is
\[
R>3|a|+24|b|.
\]
The theorem itself uses the weaker exact assumption \(\rho>0\).

## Proof
For a support function \(p\), the radius of curvature is
\[
\rho(t)=p(t)+p''(t).
\]
For the present family,
\[
\rho(t)
=
R-3a\cos(2t)-24b\sin(5t).
\]
By assumption this is positive, so \(C\) is a smooth strictly convex oval.

The opposite normal parameter is \(t+\pi\), and therefore
\[
\rho(t+\pi)
=
R-3a\cos(2t)+24b\sin(5t).
\]
Adding the two positive quantities gives
\[
2\bigl(R-3a\cos(2t)\bigr)>0
\]
for every \(t\). In particular,
\[
R>3|a|.
\]
Thus
\[
\lambda=-\frac{3a}{R}
\]
satisfies
\[
|\lambda|<1.
\]

For the Wigner caustic, the signed support function of the relevant branch is
\[
p_{1/2}(t)
=
\frac12\bigl(p(t)-p(t+\pi)\bigr)
=
b\sin(5t).
\]
Its signed radius-of-curvature density is therefore
\[
p_{1/2}(t)+p_{1/2}''(t)
=
-24b\sin(5t).
\]
The cusp parameters are exactly its zeros:
\[
\sin(5t)=0.
\]
Modulo the identification \(t\sim t+\pi\), there are exactly five:
\[
t=\frac{k\pi}{5},
\qquad k=0,\ldots,4.
\]
They are ordinary because
\[
\frac{d}{dt}\bigl(-24b\sin(5t)\bigr)
=
-120b\cos(5t)
\]
does not vanish at any of these points.

For the centre symmetry set, the published cusp criterion says that a cusp occurs when the derivative of the curvature ratio of a parallel pair vanishes. Since curvature is the reciprocal of the positive radius of curvature, the same zero set is obtained from
\[
\frac{d}{dt}
\left(
\frac{\rho(t)}{\rho(t+\pi)}
\right)
=0.
\]
After clearing the positive denominator, the numerator is
\[
\rho'(t)\rho(t+\pi)
-
\rho(t)\rho'(t+\pi).
\]
A direct trigonometric simplification gives
\[
-24b
\left(
10R\cos(5t)
-a\bigl(9\cos(7t)+21\cos(3t)\bigr)
\right).
\]
Because \(b\ne0\), the cusp equation is
\[
10\cos(5t)
+
\lambda\bigl(3\cos(7t)+7\cos(3t)\bigr)
=0.
\]
Now put
\[
x=\cos t.
\]
Using the Chebyshev identities for \(\cos(3t)\), \(\cos(5t)\), and \(\cos(7t)\), the left side factors as
\[
2xQ_\lambda(x^2),
\]
with
\[
Q_\lambda(y)
=
96\lambda y^3
+(80-168\lambda)y^2
+(-100+98\lambda)y
+25-21\lambda.
\]

We now count the roots of \(Q_\lambda\) in \((0,1)\). Its endpoint values are
\[
Q_\lambda(0)=25-21\lambda>0
\]
and
\[
Q_\lambda(1)=5(1+\lambda)>0
\]
for
\[
|\lambda|<1.
\]
For \(\lambda\ne0\), its discriminant is
\[
\operatorname{disc}_y Q_\lambda
=
-6400
\bigl(\lambda^2+2\lambda-4\bigr)
\bigl(147\lambda^2+630\lambda+500\bigr).
\]
On
\[
-1<\lambda<1
\]
the first quadratic factor is negative and the second is positive; hence the discriminant is positive. Thus \(Q_\lambda\) has three distinct real roots and no root can be created or destroyed inside \((0,1)\) except by crossing an endpoint, which the endpoint formulas exclude.

The root count is therefore constant separately on
\[
(-1,0)
\quad\text{and}\quad
(0,1).
\]
At
\[
\lambda=\frac12
\]
one has
\[
Q_{1/2}(0)>0,\qquad
Q_{1/2}\left(\frac12\right)=-6<0,\qquad
Q_{1/2}(1)>0,
\]
so exactly two roots lie in \((0,1)\). At
\[
\lambda=-\frac12
\]
one similarly has
\[
Q_{-1/2}(0)>0,\qquad
Q_{-1/2}\left(\frac12\right)=-4<0,\qquad
Q_{-1/2}(1)>0,
\]
again giving exactly two roots in \((0,1)\). At \(\lambda=0\),
\[
Q_0(y)=80y^2-100y+25
\]
has the two roots
\[
\frac{5-\sqrt5}{8},
\qquad
\frac{5+\sqrt5}{8},
\]
both in \((0,1)\).

Hence \(Q_\lambda\) always has exactly two simple roots in \((0,1)\). Each yields two values
\[
x=\pm\sqrt y
\]
in \((-1,1)\), and the prefactor \(x\) supplies one more root \(x=0\). Because \(t\mapsto\cos t\) is one-to-one on \([0,\pi]\), there are exactly five centre-symmetry-set cusp parameters modulo \(\pi\).

All these critical points are simple. The endpoint factors are nonzero, the discriminant excludes multiple \(Q_\lambda\)-roots, and
\[
25-21\lambda>0
\]
makes the root \(x=0\) simple. Therefore the corresponding centre-symmetry-set singularities are ordinary cusps.

## Verification
The supplied `verify.py` performs an exact symbolic replay.

It verifies the curvature densities of the source oval and Wigner caustic, derives the centre-symmetry-set critical equation from the ratio of opposite radii, expands the Chebyshev factorization, computes the exact discriminant of \(Q_\lambda\), and checks the endpoint and sample-sign identities used in the root-count proof.

It also evaluates several admissible normalized parameter choices and confirms that exactly two \(Q_\lambda\)-roots lie in \((0,1)\).

The numerical checks are regression tests only. The infinite parameter statement follows from the exact discriminant and endpoint argument.

## Relationship to prior work
The archive-era Wigner-caustic literature defines the Wigner caustic as the midpoint locus of parallel-tangent chords and studies its cusp singularities. The 2012 public preprint used here is classified primarily under \(58K40\).

A later paper on coherent tangent bundles gives two statement-level ingredients used here: for a generic convex curve, Wigner cusps occur when the curvature ratio of a parallel pair equals \(1\), while centre-symmetry-set cusps occur at critical points of that ratio; it also proves that the centre symmetry set has at least as many cusps as the Wigner caustic.

That later paper is especially close to the present result because one of its figures uses the explicit support
\[
p(t)=31+2\cos(2t)+\sin(5t),
\]
which is a member of the family above. The figure is prior art for that individual example. The present finding does not claim novelty for the existence of a five-cusp picture at that parameter point. Instead it proves that every strictly convex member of the full three-parameter two-harmonic family with \(ab\ne0\) has exactly five Wigner cusps and exactly five centre-symmetry-set cusps, and it gives the exact polynomial certificate controlling the centre-symmetry-set count.

Targeted searches for the two-harmonic family, the exact cubic \(Q_\lambda\), five-cusp equality families, and the support \(R+a\cos(2t)+b\sin(5t)\) did not locate a published all-parameter classification.

## Limitations
The theorem concerns cusp counts, not the global topology, self-intersections, or metric geometry of the two caustics.

The coefficients \(2\) and \(5\) are essential to the present calculation. No claim is made that an arbitrary even-plus-odd two-mode support has a parameter-independent cusp count.

The convexity hypothesis is assumed rather than solved as an exact semialgebraic condition in \((R,a,b)\). The simpler sufficient condition
\[
R>3|a|+24|b|
\]
is not asserted to be necessary.

The closest later source already illustrates one concrete member of this family. The originality claim is restricted to the all-parameter classification and its exact root certificate.

## References
1. W. Domitrz, M. Manoel, and P. de M. Rios, *The Wigner caustic on shell and singularities of odd functions*, arXiv:1207.1068v1, first public 2012-07-04; Journal of Geometry and Physics 71 (2013), 58--72. DOI: 10.1016/j.geomphys.2013.04.005.
2. W. Domitrz and P. de M. Rios, *Singularities of equidistants and global centre symmetry sets of Lagrangian submanifolds*, Geometriae Dedicata 169 (2014), 361--382. DOI: 10.1007/s10711-013-9861-2.
3. M. Domitrz and M. Zwierzyński, *The Gauss--Bonnet theorem for coherent tangent bundles over surfaces with boundary and its applications*, Journal of Geometric Analysis 30 (2020), 3243--3274. DOI: 10.1007/s12220-019-00197-0.
