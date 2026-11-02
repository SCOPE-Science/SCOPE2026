# Complete random central-section polygon law for regular triangular prisms

## Finding

Fix \(h>0\). Let \(P_h\subset\mathbb R^3\) be the right prism whose horizontal bases are equilateral triangles with circumradius \(1\), at heights \(z=\pm h/2\), centered at the origin. Choose an unoriented plane through the origin uniformly in the rotation-invariant distribution; write \(N\) for the number of sides of its intersection with \(P_h\). Outside a null set of degenerate orientations,
\[
\boxed{N\in\{3,4,5\}.}
\]
Define, for \(h>0\),
\[
T(h)=\frac6\pi\arctan\!\left(\frac{h^2}{\sqrt3\left(4+h^2+4\sqrt{1+h^2/3}\right)}\right),
\]
\[
L(h)=\frac6\pi\arccos\!\left(\frac{h^2-2}{h^2+4}\right)+\frac3\pi\arccos\!\left(\frac{4-h^2}{4+h^2}\right).
\]
The **complete polygon-type distribution** is
\[
\boxed{\Pr(N=3)=T(h),\quad\Pr(N=4)=5-L(h)-2T(h),\quad\Pr(N=5)=L(h)-4+T(h).}
\]
In particular \(\mathbb E[N]=L(h)\), and the two extreme-height limits are \(\Pr(N=4)\to1\) as \(h\downarrow0\) and \(\Pr(N=3)\to1\) as \(h\to\infty\). The formula refers to a *central* random plane, not a plane through independent random surface points. For a prism of equilateral base side length \(s\), substitute \(h=\sqrt3 H/s\), with \(H\) the physical prism height.

## Assumptions and scope

The triangular bases have vertices \(u_j=(\cos(2\pi j/3),\sin(2\pi j/3))\), \(j=0,1,2\), and the six spatial vertices are \((u_j,\pm h/2)\). A uniform plane means the normal \(n\) is uniform on the sphere modulo antipodes. Every exceptional orientation passing through a polytope vertex or containing one of its edges has spherical measure zero. The count is the number of genuine vertices of the convex section polygon, equivalently the number of prism edges crossed transversely by the plane.

## Proof

**1. There are exactly three possible section types.** Write \(s_j=n_{xy}\cdot u_j\), and, by reversing the normal if needed, take \(t=h|n_z|/2\ge0\). The top and bottom endpoint signs on the \(j\)-th vertical edge are the signs of \(s_j+t\) and \(s_j-t\). Let \(k\) be the number of indices with \(|s_j|<t\); these are precisely the vertical edges intersected by the plane. Because \(s_0+s_1+s_2=0\), the number of top triangular-base edges crossed is either zero or two, and likewise for the bottom. If \(k=0\), top and bottom triangles both have mixed signs, giving \(N=4\). If \(k=1\), the two remaining \(s_j\) have opposite signs, so both triangular bases have two crossed edges and \(N=5\). If \(k=2\), the remaining \(s_j\) has fixed sign beyond \(\pm t\), hence exactly one triangular base has two crossed edges and \(N=4\). Finally, if \(k=3\), both triangular bases have uniform, opposite signs, giving \(N=3\). This exhausts all nondegenerate orientations.

**2. The triangle probability is an elementary solid angle.** The event \(N=3\) is equivalent to \(h|n_z|/2>\max_j|n_{xy}\cdot u_j|\). Restrict to \(n_z>0\) and intersect its cone with \(z=1\). The resulting planar set is the regular hexagon
\[
H_h=\{(x,y):|u_j\cdot(x,y)|<h/2\ \text{for }j=0,1,2\},
\]
with inradius \(h/2\), circumradius \(r=h/\sqrt3\), and successive vertex directions separated by \(\pi/3\). The spherical cone subdivides into six congruent triangles with unit north-pole vector and the rays \((r,0,1)\), \((r/2,\sqrt3r/2,1)\). The standard exact solid-angle identity
\[
\Omega_{\triangle}=2\arctan\left(\frac{|\det(v_0,v_1,v_2)|}{\|v_0\|\|v_1\|\|v_2\|+(v_0\cdot v_1)\|v_2\|+(v_1\cdot v_2)\|v_0\|+(v_2\cdot v_0)\|v_1\|}\right)
\]
with these three rays gives
\[
\Omega_{\triangle}=2\arctan\left(\frac{\sqrt3r^2}{4+3r^2+4\sqrt{1+r^2}}\right).
\]
Both normal hemispheres contribute equally. Thus \(\Pr(N=3)=2\cdot6\Omega_{\triangle}/(4\pi)=3\Omega_{\triangle}/\pi=T(h)\).

**3. Expected vertex count from spherical sign separation.** Every prism edge contributes one section vertex exactly when its endpoints have opposite dot-product signs against the random normal. For any two nonzero position vectors meeting at angle \(\theta\in[0,\pi]\), this event has spherical probability \(\theta/\pi\): in the circle orthogonal to their span, the two hemispherical sign intervals differ on angular fraction \(\theta/\pi\). The six horizontal edges have endpoint-angle cosine \((h^2-2)/(h^2+4)\); the three vertical edges have endpoint-angle cosine \((4-h^2)/(4+h^2)\). By linearity of expectation over all nine edges, \(\mathbb E[N]=L(h)\).

**4. Recover the other two probabilities.** Since \(N\in\{3,4,5\}\), normalization and \(\mathbb E[N]=L(h)\) give
\[
\Pr(N=5)-\Pr(N=3)=L(h)-4,
\]
which, together with \(\Pr(N=3)=T(h)\), gives the two remaining formulas. The limit statements follow directly from the two elementary functions and their geometric interpretations. This is an exact continuum proof, not a finite configuration enumeration.

## Verification

The attached `verify.py` uses the theorem formulas and an independently implemented sign-change count on all nine geometric edges. It checks probabilities sum to one, stay in \([0,1]\), and match seeded Monte Carlo for several heights. These finite checks corroborate the exact spherical-area and edge-angle arguments; they do not establish the continuum statements.

## Relationship to prior work

Wendel's 1962 theorem on the probability that independent random sphere points lie in a hemisphere illustrates foundational spherical sign combinatorics, but its random inputs differ from the fixed correlated prism vertices. General random central-section and polyhedral shadow results describe geometric sign configurations and expectations, but the exact one-parameter three-type law above was not found in the examined sources or targeted published research-record searches. The proof uses standard solid-angle and spherical-angle identities; these ingredients, and the general edge-crossing expectation principle, are not claimed as original in isolation. The asserted contribution is their **explicit evaluated combination giving the entire triangular-prism distribution for every height**.

## Limitations

Only right equilateral triangular prisms and rotationally uniform central planes are covered. Planes through randomly sampled surface points, oblique prisms, and arbitrary triangular bases have different distributions. Absence of an exact indexed match is not a proof of historical priority; a relevant unindexed section-count calculation could predate this one. No independent audit has been performed.

## References

1. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–112, first published 1962-06-01, DOI: 10.7146/math.scand.a-10655, https://doi.org/10.7146/math.scand.a-10655.
2. R. Schneider and W. Weil, *Stochastic and Integral Geometry*, Springer (2008), standard background on invariant measures and geometric probability; not used as a source of the specific formula.
