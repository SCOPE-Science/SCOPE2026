# Regular-polygon moduli of circular spiral equicoverings

## Finding

Let \(\mu_\circ\) be normalized arclength measure on the Euclidean unit circle. For an integer \(k\ge2\), put
\[
n=3k,\qquad m=k+1,
\]
and consider convex \((n,m)\)-spiral equicoverings in the sense of Roldán-Pensado.

Every such equicovering has its common center strictly inside the unit disk.

Up to cyclic relabeling, every convex equicovering is uniquely described by a boundary phase \(\phi\) and a center \(O\) in
\[
\boxed{
C_{k,\phi}
=
\bigcap_{j=0}^{n-1}
\left\{
x\in\mathbb R^2:
x\cdot u_j\le c_k
\right\},
}
\]
where
\[
c_k=
\cos\!\left(\frac{\pi(k+1)}{3k}\right)
\]
and
\[
u_j=
\left(
\cos\!\left(
\phi+\frac{2\pi j}{n}+\frac{\pi(k+1)}{3k}
\right),
\sin\!\left(
\phi+\frac{2\pi j}{n}+\frac{\pi(k+1)}{3k}
\right)
\right).
\]
The rays are precisely the rays from \(O\) through
\[
P_j=
\left(
\cos\!\left(\phi+\frac{2\pi j}{n}\right),
\sin\!\left(\phi+\frac{2\pi j}{n}\right)
\right),
\]
so their intersections with the support circle form a regular \(n\)-gon.

For \(k=2\),
\[
C_{2,\phi}=\{0\}.
\]
This is the rigid six-sector case.

For \(k\ge3\), \(C_{k,\phi}\) is a centered regular \(3k\)-gon with inradius
\[
\boxed{
c_k=
\cos\!\left(\frac{\pi(k+1)}{3k}\right)
}
\]
and circumradius
\[
\boxed{
R_k
=
\frac{c_k}{\cos(\pi/(3k))}
=
\frac12-
\frac{\sqrt3}{2}
\tan\!\left(\frac{\pi}{3k}\right).
}
\]
Its area is
\[
\boxed{
\operatorname{area}(C_{k,\phi})
=
3k\,c_k^2
\tan\!\left(\frac{\pi}{3k}\right).
}
\]

Two radial consequences follow by rotating this regular polygon. A prescribed point \(O\) is the center of at least one convex \((3k,k+1)\)-spiral equicovering of \(\mu_\circ\) exactly when
\[
\boxed{\|O\|\le R_k.}
\]
It is the center of a convex equicovering for every boundary phase exactly when
\[
\boxed{\|O\|\le c_k.}
\]

Finally,
\[
c_k\longrightarrow\frac12,
\qquad
R_k\longrightarrow\frac12,
\qquad
\operatorname{area}(C_{k,\phi})\longrightarrow\frac{\pi}{4}.
\]
Thus the center moduli converge to the disk of radius \(1/2\).

## Assumptions and scope

The measure \(\mu_\circ\) is normalized one-dimensional arclength on the unit circle. It is a planar mass in the terminology of the source because every affine line meets the circle in at most two points and therefore has \(\mu_\circ\)-measure zero.

A spiral equicovering consists of \(n\) rays from one center, \(n\) consecutive sectors of mass \(1/n\), and \(n\) \(m\)-wedges obtained as unions of \(m\) consecutive sectors. Convexity means that every \(m\)-wedge has angular size at most \(\pi\).

The phase \(\phi\) records the first intersection point of the fan with the support circle. Replacing \(\phi\) by \(\phi+2\pi/n\) only cyclically relabels the same boundary polygon.

The theorem classifies the full convex \((3k,k+1)\)-spiral family for this circular mass. It does not classify equicoverings for arbitrary radial densities or arbitrary planar masses.

## Proof

First, the center of a convex equicovering must lie in the open unit disk.

Suppose the center \(O\) lies outside or on the unit disk. Viewed from \(O\), all directions that meet the support circle lie in a closed angular interval of length at most \(\pi\); the length is strictly smaller than \(\pi\) when \(\|O\|>1\). Its complementary angular interval \(J\) has length at least \(\pi\) and carries zero mass.

Every basic sector has mass \(1/n>0\). Hence two consecutive fan rays cannot both lie in the interior of \(J\), because the sector between two such consecutive rays would have zero mass. Therefore \(J\) is contained in either one sector or two adjacent sectors. Since every involved sector must have positive mass, their total angle is strictly larger than the length of \(J\), hence strictly larger than \(\pi\). An \(m\)-wedge containing those one or two adjacent sectors is therefore nonconvex. This contradicts convexity. Thus
\[
\|O\|<1.
\]

Now fix an interior center \(O\). Every ray from \(O\) meets the unit circle exactly once, and radial projection from the circle to the circle of directions about \(O\) preserves cyclic order. Let \(P_j\) be the circle point on the \(j\)-th ray. The \(j\)-th basic sector meets the support circle in the circular arc from \(P_j\) to \(P_{j+1}\). Since this sector has \(\mu_\circ\)-mass \(1/n\), that arc has central angle
\[
\frac{2\pi}{n}.
\]
Consequently there is a phase \(\phi\) such that
\[
P_j=
\left(
\cos\!\left(\phi+\frac{2\pi j}{n}\right),
\sin\!\left(\phi+\frac{2\pi j}{n}\right)
\right).
\]
Thus every equal-mass fan centered inside the disk is obtained by viewing a regular \(n\)-gon from \(O\).

Consider the \(m\)-wedge beginning at \(P_j\). Its final boundary ray passes through \(P_{j+m}\). Put
\[
\Delta
=
\frac{2\pi m}{n}
=
\frac{2\pi(k+1)}{3k}.
\]
For \(k\ge2\),
\[
\Delta\le\pi.
\]
The counterclockwise wedge angle about \(O\) is at most \(\pi\) exactly when
\[
\det(P_j-O,P_{j+m}-O)\ge0.
\]

Rotate coordinates so that the midpoint direction of the circular chord \(P_jP_{j+m}\) is the positive horizontal axis. Then
\[
P_j=(c_k,-s_k),
\qquad
P_{j+m}=(c_k,s_k),
\]
where
\[
c_k=\cos\frac{\Delta}{2},
\qquad
s_k=\sin\frac{\Delta}{2}>0.
\]
Writing the rotated center as \(O=(x,y)\), one gets the exact identity
\[
\det(P_j-O,P_{j+m}-O)
=
2s_k(c_k-x).
\]
Undoing the rotation gives
\[
\det(P_j-O,P_{j+m}-O)\ge0
\quad\Longleftrightarrow\quad
O\cdot u_j\le c_k,
\]
with \(u_j\) as in the Finding. Imposing this for every \(j\) proves
\[
O\in C_{k,\phi}.
\]
The argument is reversible, so every point of \(C_{k,\phi}\) produces a convex equicovering.

When \(k=2\), \(c_k=0\), and opposite inequalities force \(O=0\).

When \(k\ge3\), \(c_k>0\). The normals \(u_j\) are equally spaced by \(2\pi/n\), so the intersection of the half-planes is a regular \(n\)-gon with inradius \(c_k\). Intersecting two adjacent support lines gives the circumradius
\[
R_k=\frac{c_k}{\cos(\pi/n)}.
\]
Writing
\[
a=\frac{\pi}{3k}
\]
and using
\[
c_k=\cos\left(\frac{\pi}{3}+a\right)
=
\frac12\cos a-\frac{\sqrt3}{2}\sin a
\]
gives
\[
R_k
=
\frac12-\frac{\sqrt3}{2}\tan a.
\]
In particular \(0<R_k<1/2\), so every center obtained from the half-plane description is automatically an interior center, as required.

The standard inradius formula for a regular \(n\)-gon yields
\[
\operatorname{area}(C_{k,\phi})
=
n c_k^2\tan\frac{\pi}{n}
=
3k c_k^2\tan\frac{\pi}{3k}.
\]

As \(\phi\) varies, \(C_{k,\phi}\) runs through all rotations of one centered regular \(n\)-gon. The union of all its rotations is exactly the disk of radius \(R_k\), while the intersection of all its rotations is exactly the disk of radius \(c_k\). This proves the two radial characterizations.

Finally,
\[
c_k\to\frac12,
\qquad
R_k\to\frac12,
\qquad
3k\tan\frac{\pi}{3k}\to\pi,
\]
which gives the asserted area limit.

## Verification

The proof is analytic and all-dimensional. No finite computation is used to infer the classification.

The bundled checker verifies, for \(2\le k\le200\), the determinant-to-half-plane identity on many deterministic test centers and phases, the adjacent-side circumradius formula, the trigonometric expression for \(R_k\), and the regular-polygon area formula. It also confirms the degeneracy at \(k=2\), strict positivity and \(R_k<1/2\) for \(k\ge3\), and numerical convergence of the three asymptotic quantities.

The primary source was inspected at its definitions of spiral equicoverings, its convexity criterion, Theorem 1, and its later radial-symmetry deformation. The paper proves existence for every planar mass but does not classify the circular mass or compute a center moduli set.

The earlier open-access paper introducing spiral equicoverings was inspected at its definitions, main parameter theorem, and open problems. It likewise does not contain the circular classification.

## Relationship to prior work

Roldán-Pensado proves that every planar mass admits a convex \((3k,k+1)\)-spiral equicovering for every \(k\ge2\). His proof is topological and existential. For \(k=2\), the paper observes that all three-sector wedges must be half-planes, recovering the classical six-sector configuration.

The present result specializes to the canonical singular mass supported uniformly on the circle and replaces existence by a complete moduli description. Equal sector masses force a regular \(3k\)-gon on the support circle, and the convexity constraints become exactly the supporting half-planes of another regular \(3k\)-gon in center space.

The earlier paper by Espinosa-García, Martínez-Sandoval, and Roldán-Pensado develops general centerpoint-based constructions and the parameter ranges for spiral equicoverings. Its arguments do not state the center polygon above.

Targeted searches for circular spiral equicoverings, regular-polygon center loci, center-moduli formulations, and the exact radii \(c_k\) and \(R_k\) located no prior statement of this classification.

## Limitations

The result is exact for normalized arclength measure on one circle. It does not extend automatically to a smooth radial density in the disk: for such a measure, equal angular mass sectors seen from an off-center point are not determined by equal boundary arcs.

The half-plane center polygon classifies convex spiral equicoverings, not arbitrary non-spiral equicoverings.

The main residual bibliographic risk is that an equivalent regular-polygon center-locus calculation may exist in older fan-partition literature under different terminology.

## References

1. Edgardo Roldán-Pensado, *On convex spiral equicoverings of masses*, arXiv:2609.23746v1, 20 September 2026.
2. Manuel A. Espinosa-García, Leonardo Martínez-Sandoval, and Edgardo Roldán-Pensado, *Equicovering masses in the Euclidean plane*, arXiv:2505.07074v1, 11 May 2025; published in *Boletín de la Sociedad Matemática Mexicana* 32 (2026), article 43.
