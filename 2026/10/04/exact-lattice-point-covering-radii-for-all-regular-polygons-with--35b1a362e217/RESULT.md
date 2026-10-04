# Exact lattice-point covering radii for all regular polygons with two modulo four sides

## Finding

For an integer \(N\ge6\) with \(N\equiv2\pmod4\), let
\[
H_N=\operatorname{conv}\left\{\left(\cos\frac{2\pi k}{N},\sin\frac{2\pi k}{N}\right):0\le k<N\right\}.
\]
Let \(Z(H_N)\) be the least \(t>0\) such that every translate and rotation of \(tH_N\) contains a point of \(\mathbb Z^2\). Then
\[
Z(H_N)=\frac{\cos(\pi/(2N))}{\sqrt2\,\cos(\pi/N)}.
\]

The formula recovers the previously published regular-hexagon and regular-decagon values. Combined with the known formula for regular \(4m\)-gons, it gives an exact lattice-point covering radius for every regular polygon with an even number of sides.

## Assumptions and scope

The polygon has circumradius one and the lattice is the standard integer lattice. The motion is arbitrary translation and rotation, exactly as in the lattice-point covering problem introduced in the cited source. Only even regular polygons are addressed here.

Put
\[
\delta=\frac{\pi}{2N},\qquad c=\cos\frac{\pi}{N}=\cos(2\delta),\qquad
q=\frac{c}{\sqrt2\cos\delta}.
\]
The published sufficient criterion says that a centrally symmetric planar body has the lattice-point covering property if the Steiner symmetrization of every rotation contains the unit square. The published necessary criterion says that for a body symmetric in both coordinate axes, covering by its integer translates is equivalent to containing the unit square. These two criteria are used below; the new part is a uniform chord estimate for every \(N\equiv2\pmod4\).

## Proof

The regular polygon is the intersection of the half-planes
\[
x\cos\phi+y\sin\phi\le c,
\]
where the outward side-normal angles \(\phi\) form an arithmetic progression with step \(2\pi/N=4\delta\).

At the unrotated position, the ray \(y=x\) meets the polygon at \((q,q)\). Indeed the nearest side normal to angle \(\pi/4\) differs from \(\pi/4\) by exactly \(\delta\), so its support equation gives
\[
q\sqrt2\cos\delta=c.
\]
Consequently any dilation having the lattice-point covering property must satisfy \(tq\ge1/2\): in the unrotated position the polygon is symmetric in both coordinate axes, and the published necessary criterion forces \(tH_N\) to contain the square \([-\tfrac12,\tfrac12]^2\). Thus
\[
Z(H_N)\ge\frac1{2q}
=\frac{\cos\delta}{\sqrt2\,c}.
\]

It remains to prove the reverse inequality. By the dihedral symmetries of the regular polygon together with the symmetries of the square lattice, it is enough to consider a relative rotation
\[
0\le\theta\le\delta.
\]
We show that, for every such \(\theta\), the vertical chord of the rotated polygon at \(x=q\) has length at least \(2q\). Its Steiner symmetrization about the horizontal axis therefore contains the two points \((q,\pm q)\); central symmetry gives the corresponding two points at \(x=-q\), and convexity gives the whole square \([-q,q]^2\).

The chord estimate follows from one elementary identity. Let \(0<a<\pi/2\), and suppose its upper and lower endpoint sides have outward normals
\[
a+u,\qquad -(a-u),
\]
with common support distance \(c\). Assume
\[
q=\frac{c}{\sin a+\cos a}.
\]
The upper and lower intersection ordinates at \(x=q\) are
\[
y_+=\frac{c-q\cos(a+u)}{\sin(a+u)},\qquad
y_-=-\frac{c-q\cos(a-u)}{\sin(a-u)}.
\]
Writing \(h=(y_+-y_-)/2\), direct simplification gives
\[
h-q=
\frac{c(1-\cos u)
\left[1+\cos u-\sin a(\sin a+\cos a)\right]}
{(\sin a+\cos a)\sin(a+u)\sin(a-u)}.
\]
In the applications below,
\[
a\in\left[\frac{\pi}{6},\frac{\pi}{3}\right],
\qquad |u|\le\frac{\pi}{6}.
\]
All denominator factors are positive. Moreover
\[
1+\cos u\ge1+\frac{\sqrt3}{2}
\]
while
\[
\sin a(\sin a+\cos a)\le\frac{3+\sqrt3}{4},
\]
so the bracket is strictly positive. Hence \(h\ge q\), with equality only when \(u=0\).

We now identify the endpoint sides. The simple bounds
\[
\cos\left(\frac{\pi}{4}+\delta\right)\le q<\frac1{\sqrt2}
\]
show that the line \(x=q\) meets the indicated adjacent sides throughout the reduced rotation interval.

If \(N\equiv2\pmod8\), the active upper and lower side normals are
\[
a+\theta,\qquad -(a-\theta),
\qquad a=\frac{\pi}{4}+\delta.
\]
Because
\[
\sin a+\cos a=\sqrt2\cos\delta,
\]
the chord identity applies with \(u=\theta\), and gives \(h\ge q\).

If \(N\equiv6\pmod8\), the active upper side has normal
\[
\frac{\pi}{4}-\delta+\theta.
\]
The lower endpoint lies on one of the two adjacent lower sides. Before their switch the normals form the pair
\[
a+\theta,\qquad -(a-\theta),
\qquad a=\frac{\pi}{4}-\delta,
\]
so the identity applies with \(u=\theta\). After the switch they form the pair with
\[
a=\frac{\pi}{4}+\delta,\qquad u=\theta-2\delta.
\]
Again \(\sin a+\cos a=\sqrt2\cos\delta\), and now \(|u|\le2\delta\le\pi/6\). At the switch both descriptions give the same lower vertex. Thus every possible chord satisfies \(h\ge q\).

Therefore the Steiner symmetrization of every relative rotation contains \([-q,q]^2\). Scaling by
\[
t_0=\frac1{2q}=\frac{\cos\delta}{\sqrt2\,c}
\]
makes this square the unit square. The published sufficient criterion now gives the lattice-point covering property for \(t_0H_N\), so
\[
Z(H_N)\le t_0.
\]
Together with the lower bound,
\[
Z(H_N)=t_0
=\frac{\cos(\pi/(2N))}{\sqrt2\,\cos(\pi/N)}.
\]

## Verification

The trigonometric formula was independently checked against the two published special cases:
\[
\frac{\cos(\pi/12)}{\sqrt2\cos(\pi/6)}
=\frac1{3-\sqrt3}
\]
for \(N=6\), and
\[
\frac{\cos(\pi/20)}{\sqrt2\cos(\pi/10)}
\]
simplifies to the published regular-decagon expression.

The generic chord identity was expanded directly from the two support-line equations. The sign check is uniform over all admissible parameters; it does not rely on sampling. The two residue classes modulo eight exhaust \(N\equiv2\pmod4\), and the side-switch description in the second class uses the two sides adjacent at the unique lower switching vertex.

The finite numerical checks used during development were only sanity checks and are not part of the proof. The theorem rests on the analytic support-line calculation and the published necessary and sufficient lattice-covering criteria.

## Relationship to prior work

Fei Xue's 2019 paper proves an exact formula for every regular \(4m\)-gon and exact values for the regular hexagon and regular decagon. Its Theorem 4 explicitly restricts the \(4m+2\) equivalence to the two cases \(m=1,2\). Later, Remark 11 writes down the general Steiner-symmetrization vertex pattern and says that all regular \(4m+2\)-gons can be handled similarly, but it does not state a radius formula or prove a uniform inequality for all \(m\).

The result above makes that remaining family explicit and uniform. The key difference is the single support-line chord identity, which replaces the source's separate monotonicity calculations for the hexagon and decagon and works simultaneously in both residue classes modulo eight. The author's 2019 doctoral-thesis abstract likewise advertises smallest dilations for the regular hexagon, regular octagon, and regular \(4m\)-gons rather than an all-\(4m+2\) theorem.

Targeted searches for the exact trigonometric expression, \(Z(H_{14})\), regular \(14\)-gon lattice-point covering, and general regular \(4m+2\)-gon covering radii did not locate a later explicit formula.

## Limitations

The theorem is for the standard integer lattice and regular polygons of even order. It does not address odd regular polygons, nonregular centrally symmetric polygons, or other lattices. The literature risk is not zero: the 2019 paper explicitly remarks that all regular \(4m+2\)-gons can be treated similarly, so an unpublished calculation or a differently indexed later source could contain the same closed form. The claim here is the explicit all-\(N\) formula and its uniform proof, not the general methodological suggestion.

## References

F. Xue, “On the Lattice Point Covering Problem in Dimension 2,” arXiv:1810.03555, first submitted 2018-10-08; Electronic Journal of Combinatorics 26(2) (2019), #P2.9, DOI 10.37236/8245.

F. Xue, “Convex geometry of numbers: covering, successive minima and Banach-Mazur distance,” doctoral thesis, Technische Universität Berlin, 2019, DOI 10.14279/depositonce-9059.
