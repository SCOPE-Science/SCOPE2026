# An infinite Kohn–Nirenberg tower with continuous hypersurface Green functions

## Finding

For every integer
\[
m\ge3,
\]
every
\[
1<\beta<\frac{m^2}{2m-1},
\]
and every
\[
\lambda>0,
\]
set
\[
P_{m,\beta}(z)
=
|z|^{2m}
+
\beta |z|^2\operatorname{Re}z^{2m-2},
\]
\[
\rho_{m,\beta}(z,w)
=
|w|^2
+
P_{m,\beta}(z)
+
|z|^{2m+2}
-1,
\]
and
\[
\Omega_{m,\beta}
=
\{\rho_{m,\beta}<0\}.
\]
Let
\[
f_\lambda(z,w)
=
(w-1)^2-\lambda z^2
\]
and let \(A_\lambda\) be the reduced hypersurface that it cuts out in \(\Omega_{m,\beta}\).

Then \(\Omega_{m,\beta}\) is a bounded, connected, smooth, pseudoconvex, \(B\)-regular domain that is not locally convexifiable at
\[
p=(0,1).
\]
The weighted holomorphic flow
\[
S_\tau(z,w)
=
\left(e^{-\tau}z,e^{-m\tau}w\right)
\]
is a sectorial inward deformation for the pair
\[
(\Omega_{m,\beta},A_\lambda).
\]
Therefore the pluricomplex Green function with hypersurface pole is extended-real continuous:
\[
G_{A_\lambda,\Omega_{m,\beta}}
\in
C\!\left(\Omega_{m,\beta},[-\infty,0]\right).
\]

The same theorem also gives the canonical truncation approximation. If
\[
u_j
=
P_{\Omega_{m,\beta}}
\min\{-\log|f_\lambda|,j\},
\]
then
\[
u_j\uparrow\widetilde G_{A_\lambda}
\]
on
\[
\Omega_{m,\beta}\setminus A_\lambda,
\]
and the upper-semicontinuous regularization of the limit is
\[
G_{A_\lambda,\Omega_{m,\beta}}
\]
on all of \(\Omega_{m,\beta}\).

This supplies an infinite Kohn–Nirenberg-type family carrying the global holomorphic inward deformation requested in the recent source's geometric open question. The source gives one isolated model; the family above persists for every
\[
m\ge3
\]
and every
\[
1<\beta<\frac{m^2}{2m-1}.
\]

## Assumptions and scope

The hypersurface Green function and sectorial inward deformation are used in the sense of the recent primary source.

The parameter interval
\[
1<\beta<\frac{m^2}{2m-1}
\]
is a sufficient range in which two needed features coexist transparently: pseudoconvexity and the Kohn–Nirenberg supporting-hypersurface obstruction. No claim is made that this interval is maximal.

The conclusion applies to every
\[
\lambda>0.
\]
The polynomial \(f_\lambda\) is reduced because
\[
f_\lambda
=
\left(w-1-\sqrt\lambda\,z\right)
\left(w-1+\sqrt\lambda\,z\right)
\]
has distinct factors. Its only singular point is
\[
p=(0,1),
\]
which lies on the boundary rather than in the domain.

## Proof

First, the domain is bounded. Since
\[
P_{m,\beta}(z)
\ge
(1-\beta)|z|^{2m},
\]
the positive term
\[
|z|^{2m+2}
\]
dominates for large \(|z|\), and \(|w|^2\) controls the other coordinate.

The Levi matrix is diagonal. Its \(w\)-entry equals \(1\), while
\[
\frac{\partial^2\rho_{m,\beta}}
{\partial z\,\partial\overline z}
=
m^2|z|^{2m-2}
+
\beta(2m-1)\operatorname{Re}z^{2m-2}
+
(m+1)^2|z|^{2m}.
\]
Hence
\[
\frac{\partial^2\rho_{m,\beta}}
{\partial z\,\partial\overline z}
\ge
\bigl(m^2-\beta(2m-1)\bigr)|z|^{2m-2}
+
(m+1)^2|z|^{2m}.
\]
The coefficient in the first term is positive, so the domain is pseudoconvex and is strictly pseudoconvex at every boundary point with
\[
z\ne0.
\]

Now consider the real weighted flow
\[
S_t(z,w)
=
(e^{-t}z,e^{-mt}w).
\]
The two terms in \(P_{m,\beta}\) have weighted degree \(2m\), while the added radial term has degree \(2m+2\). Direct differentiation gives
\[
\left.\frac{d}{dt}
\rho_{m,\beta}(S_t(z,w))
\right|_{t=0}
=
-2m\bigl(\rho_{m,\beta}(z,w)+1\bigr)
-
2|z|^{2m+2}.
\]
On the boundary,
\[
\left.\frac{d}{dt}\rho_{m,\beta}(S_t(z,w))\right|_{t=0}
\le
-2m.
\]
Thus the boundary is smooth, and the real flow points uniformly and strictly inward.

In fact,
\[
\rho_{m,\beta}(S_t(z,w))
=
e^{-2mt}\bigl(\rho_{m,\beta}(z,w)+1\bigr)
-1
+
\left(e^{-(2m+2)t}-e^{-2mt}\right)|z|^{2m+2}.
\]
For every
\[
t>0
\]
and every point of \(\Omega_{m,\beta}\), the right side is negative. Hence the flow contracts the domain toward the origin, which also proves connectedness.

The weakly pseudoconvex boundary set is contained in
\[
\{z=0,\ |w|=1\}.
\]
This is a real one-dimensional circle and therefore has zero two-dimensional Hausdorff measure. The \(B\)-regularity criterion used in the recent primary source for its Kohn–Nirenberg model therefore applies verbatim.

We next verify the divisor conditions. The hypersurface is reduced, as noted above. It meets the domain: for sufficiently small real
\[
t>0,
\]
the point
\[
\left(t,1-\sqrt\lambda\,t\right)
\]
lies on \(A_\lambda\), and
\[
\rho_{m,\beta}
\left(t,1-\sqrt\lambda\,t\right)
=
-2\sqrt\lambda\,t
+\lambda t^2
+(1+\beta)t^{2m}
+t^{2m+2}
<0.
\]

To obtain a complex sector, write the boundary directional derivative of
\[
\tau\longmapsto
\rho_{m,\beta}(S_\tau q)
\]
as a real part of a complex linear function of \(\tau\). Its real-axis coefficient is uniformly negative by the bound above, while its imaginary coefficient is uniformly bounded on the compact boundary. Choosing a sufficiently narrow sector around the positive real axis preserves a uniform negative first-order boundary derivative. A uniform Taylor estimate then gives, for all sufficiently small \(\tau\) in that sector,
\[
S_\tau(\Omega_{m,\beta})
\subset
\Omega_{m,\beta},
\]
the displacement estimate
\[
\sup_{q\in\overline\Omega_{m,\beta}}
|S_\tau(q)-q|
=
O(|\tau|),
\]
and, near the boundary trace of the divisor,
\[
\operatorname{dist}
\left(
S_\tau(q),
\partial\Omega_{m,\beta}
\right)
\ge
c|\tau|.
\]
Points a fixed positive distance from the boundary stay in the domain by compactness, so the boundary estimate extends to the whole domain as required by the definition.

At the only singular point of the divisor,
\[
p=(0,1),
\]
one has the exact escape formula
\[
f_\lambda(S_\tau p)
=
\left(e^{-m\tau}-1\right)^2.
\]
It is not identically zero and has finite order two at the origin. Thus all sectorial inward deformation requirements hold.

It remains to prove that the domains are genuinely nonconvexifiable. Near \(p\), put
\[
\eta=2(w-1).
\]
The boundary equation becomes
\[
\operatorname{Re}\eta
+
P_{m,\beta}(z)
+
|z|^{2m+2}
+
\frac14|\eta|^2
=
0.
\]
Suppose there were a local holomorphic supporting hypersurface through \(p\). Since the complex tangent there is
\[
\{\eta=0\},
\]
it can be written
\[
\eta=h(z),
\qquad
h(0)=h'(0)=0.
\]

Let \(k\) be the degree of the first nonzero homogeneous term of \(h\). If
\[
k<2m,
\]
the real part of that holomorphic term changes sign and dominates the boundary polynomial along some ray, contradicting support. If
\[
k>2m
\]
or \(h\) is identically zero to this order, choose a ray satisfying
\[
\cos((2m-2)\theta)=-1.
\]
Along that ray,
\[
P_{m,\beta}(re^{i\theta})
=
(1-\beta)r^{2m}
<0,
\]
again contradicting support.

It remains only
\[
k=2m.
\]
Take all
\[
2m-2
\]
directions
\[
\theta_j
=
\frac{\pi}{2m-2}
+
\frac{j\pi}{m-1},
\qquad
0\le j\le2m-3.
\]
They all satisfy the same negative identity for \(P_{m,\beta}\), and
\[
\sum_{j=0}^{2m-3}
e^{i2m\theta_j}
=
0.
\]
Therefore the real part of the degree-\(2m\) holomorphic correction is nonpositive on at least one of those rays. On that ray the leading boundary term remains negative, a contradiction.

Hence no local holomorphic supporting hypersurface exists at \(p\). A local biholomorphic convexification would pull back a supporting complex hyperplane, so \(\Omega_{m,\beta}\) is not locally convexifiable there.

The recent continuity theorem for reduced hypersurfaces on \(B\)-regular domains admitting a sectorial inward deformation now gives both the Green-function continuity and the monotone truncation convergence asserted above.

## Verification

The primary source was checked at its definition of sectorial inward deformation, its continuity theorem, its explicit bounded Kohn–Nirenberg example, and its open question asking for broad nonconvexifiable classes carrying a global inward holomorphic deformation.

The algebra needed for the family was reconstructed independently. The Levi entry, the real-flow derivative, the exact real-flow formula, the divisor intersection, and the singular-point escape are explicit identities.

The supporting-hypersurface obstruction was checked in all three possible degrees of the leading holomorphic correction. The degree-\(2m\) case uses the complete set of negative Kohn–Nirenberg directions, whose \(2m\)-th powers sum to zero.

The older continuity theorem for strongly star-shaped domains was also inspected. Its hypersurface corollary concerns finite unions of complex hyperplanes through the origin and does not cover the reduced singular divisors used here.

No numerical experiment is used.

## Relationship to prior work

The recent paper proves a general continuity theorem under sectorial inward deformation and supplies one bounded nonconvexifiable Kohn–Nirenberg-type example with weighted degree eight. It then asks for geometric conditions producing broad classes of nonconvexifiable domains with a global holomorphic inward flow.

The present family extends that isolated construction simultaneously in the finite type
\[
2m
\]
and in the anisotropy parameter \(\beta\). The same weighted Euler flow works for every member, while the exact interval
\[
1<\beta<\frac{m^2}{2m-1}
\]
keeps pseudoconvexity and the supporting-hypersurface obstruction compatible.

Nguyen's 2005 continuity result treats strongly star-shaped domains for hypersurfaces that are finite unions of complex hyperplanes through the origin. The divisors
\[
(w-1)^2-\lambda z^2=0
\]
are translated, reducible hypersurfaces whose branches meet at a boundary point, so that earlier corollary does not imply the present result.

Kolář's work develops local invariants and nonconvexifiability criteria for generalized Kohn–Nirenberg models, but it does not supply the pluricomplex Green continuity or the global sectorial deformation asserted here.

Targeted searches under weighted-flow, sectorial-deformation, generalized Kohn–Nirenberg, and hypersurface-Green formulations did not locate a result covering this full family.

## Limitations

The interval
\[
1<\beta<\frac{m^2}{2m-1}
\]
is not claimed to be optimal.

The complex-sector constants are obtained uniformly by compactness and a first-order inward estimate; no closed-form optimal sector angle is asserted.

The result concerns the specific natural divisor family
\[
(w-1)^2-\lambda z^2=0.
\]
It does not classify every hypersurface pole on these domains.

## References

1. H. H. Dao, Q. D. Nguyen, and D. H. Tran, *Continuity of pluricomplex Green functions with hypersurface poles on certain B-regular domains*, arXiv:2610.00909v1, 2026.
2. Q. D. Nguyen, *Continuity of pluricomplex Green functions with poles along a hypersurface*, Arkiv för Matematik 43 (2005), 181–200.
3. M. Kolář, *Generalized models and local invariants of Kohn–Nirenberg domains*, Mathematische Zeitschrift 259 (2008), 277–286; arXiv:math/0703058.
4. N. Sibony, *Une classe de domaines pseudoconvexes*, Duke Mathematical Journal 55 (1987), 299–319.
