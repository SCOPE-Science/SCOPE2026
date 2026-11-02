# The exact Haar section-type law of the truncated octahedron

## Finding

Let \(T\subset\mathbb R^3\) be the regular truncated octahedron with the 24 vertices obtained by permuting the coordinates of \((0,\pm1,\pm2)\), where the two displayed signs vary independently. For a uniformly oriented plane through its center, let \(N\) be the number of sides of the polygonal intersection. The exceptional orientations passing through a vertex have probability zero.

Put
\[
\vartheta=\arccos(4/5),\qquad
B=11+3\sqrt{14}+4\sqrt6+2\sqrt{21},\qquad
\beta=\arctan(1/B).
\]
Then \(N\) takes only the values \(6,8,10\), and its **complete probability law** is
\[
\boxed{\begin{aligned}
\mathbb P(N=6)&=4-\frac{18\vartheta}{\pi}+\frac{24\beta}{\pi},\\
\mathbb P(N=8)&=\frac{18\vartheta}{\pi}-3-\frac{48\beta}{\pi},\\
\mathbb P(N=10)&=\frac{24\beta}{\pi}.
\end{aligned}}
\]
Numerically, in order, these are \(0.498450689917704\), \(0.316108855580190\), and \(0.185440454502106\). Moreover
\[
\mathbb E N=\frac{36}{\pi}\arccos(4/5)=7.373979529168803\ldots.
\]

## Assumptions and scope

An unoriented central plane is represented by \(u^\perp=\{x\in\mathbb R^3:u\cdot x=0\}\), with \(u\) Haar-uniform on the unit sphere. The sign of \(u\) does not affect the plane. This is **central-plane sampling**, not motion-invariant affine-plane sampling with variable offset. The solid is full dimensional and has its Euclidean center at the origin. All assertions concern generic orientations; vertex-incident planes belong to finitely many great circles and have zero Haar measure.

## Proof

**1. Exact geometry.** The solid is also
\[
T=[-2,2]^3\cap\{x:|x_1|+|x_2|+|x_3|\le3\}.
\]
Its six coordinate faces are squares; its eight additional faces are regular hexagons. Direct facet intersection gives precisely the 24 stated vertices, with 36 edges joining exactly those unordered vertex pairs whose squared Euclidean distance is \(2\). Each vertex is incident to three such edges. Every vertex has squared radius \(5\), and endpoints \(v,w\) of any edge satisfy \(v\cdot w=4\).

**2. All generic section types.** For generic \(u\), every intersection vertex lies in the relative interior of exactly one edge of \(T\); conversely, an edge contributes one section vertex precisely when the scalar products of its endpoints with \(u\) have opposite signs. Thus
\[
N(u)=\sum_{\{v,w\}\in E(T)}\mathbf1_{\{(u\cdot v)(u\cdot w)<0\}}.
\]
Symmetry under coordinate sign changes and permutations reduces the direction to \(u=(a,b,c)\) with \(a>b>c>0\). Let \(x=b/a\), \(y=c/a\), so \(0<y<x<1\). The only equations \(u\cdot v=0\) for vertices that meet the interior of this chamber are \(x=1/2\), \(y=1/2\), and \(y=x/2\). Enumerating the 36 edges once within each open cell yields the following exhaustive classification:

| Conditions on \(x,y\) | Number of section sides |
|---|---:|
| \(x<1/2,\ y<x/2\) | \(8\) |
| \(x<1/2,\ x/2<y<x\) | \(10\) |
| \(x>1/2,\ y<x/2\) | \(6\) |
| \(x>1/2,\ x/2<y<1/2\) | \(8\) |
| \(x>1/2,\ 1/2<y<x\) | \(6\) |

No additional type can occur off the arrangement: the signs of all vertex scalar products are locally constant there. In particular, the decagonal region is exactly the projective triangle \(0<x<1/2\), \(x/2<y<x\).

**3. Exact decagon probability.** The spherical area measure under the radial chart \((x,y)\mapsto(1,x,y)/\sqrt{1+x^2+y^2}\) is
\[
(1+x^2+y^2)^{-3/2}\,dx\,dy.
\]
Each of the 48 signed coordinate-order chambers has the same area \(\pi/12\). Consequently the probability of a decagon is
\[
\frac{12}{\pi}\int_0^{1/2}\int_{x/2}^{x}\frac{dy\,dx}{(1+x^2+y^2)^{3/2}}.
\]
The domain is a spherical triangle with rays \((1,0,0)\), \((4,2,1)\), and \((2,1,1)\). For three rays \(r_1,r_2,r_3\), its solid angle is
\[
\Omega=2\arctan\frac{|\det(r_1,r_2,r_3)|}{\|r_1\|\|r_2\|\|r_3\|+(r_1\cdot r_2)\|r_3\|+(r_2\cdot r_3)\|r_1\|+(r_3\cdot r_1)\|r_2\|}.
\]
The determinant here is \(1\), and the denominator is \(B\); therefore the integral is \(\Omega=2\beta\). As an independent analytic evaluation, integration first in \(y\) yields
\[
\Omega=\arctan\sqrt{\frac32}-\arctan\frac{\sqrt{21}}2+\arctan2-\frac\pi4.
\]
Hence \(\mathbb P(N=10)=12\Omega/\pi=24\beta/\pi\).

**4. The other probabilities from an exact first moment.** For unit vectors \(v/\sqrt5,w/\sqrt5\) separated by angle \(\vartheta\), a Haar-uniform \(u\) gives opposite signs of \(u\cdot v\) and \(u\cdot w\) with probability \(\vartheta/\pi\): intersect the normal sphere with the plane spanned by \(v,w\) and count the two opposite angular intervals. Every edge has the same endpoint angle \(\vartheta=\arccos(4/5)\). Linearity of expectation across 36 edges gives \(\mathbb E N=36\vartheta/\pi\). Finally, using the exhaustive support \(\{6,8,10\}\), normalization and this first moment give
\[
\mathbb P(N=8)=\frac{\mathbb EN-6}{2}-2\mathbb P(N=10),\qquad
\mathbb P(N=6)=1-\mathbb P(N=8)-\mathbb P(N=10),
\]
which simplifies to the asserted formulas. All steps are exact.

## Verification

The self-contained file `verify.py` enumerates 24 vertices and 36 edges using exact integers, checks the six possible vertex-orthogonality walls (three geometric walls), verifies one rational interior representative in every open chamber cell, independently evaluates the decagon spherical angle by two formulas, and checks probability normalization and the exact edge-crossing expectation. A seeded 90,000-direction Gaussian/Haar simulation provides a separate numerical consistency test. Run with `python verify.py` using Python 3's standard library. The script reports `ALL_CHECKS_PASSED`. The finite computation checks arithmetic and enumeration; the chamber proof and solid-angle calculation provide the all-orientation argument.

## Relationship to prior work

Brandenburg, De Loera, and Meroni, *The Best Ways to Slice a Polytope* (first posted 2023-04-27), establish general slicing-chamber theory and examine the three-dimensional permutahedron, which is the same regular truncated octahedron up to Euclidean similarity. Their Example 5.1 describes extremal affine sections and eight possible affine side counts, but does not provide the Haar probability law for **central** sections given here. The present result uses the finite-arrangement idea while carrying out the geometric probability and exact spherical-area calculation for this specific natural solid.

De Leo's *Topology of plane sections of periodic polyhedra with an application to the Truncated Octahedron* (2005) concerns plane sections of periodically extended surfaces and their global topological dynamics, not directly the distribution of side counts of one central solid. Its abstract was available; the complete text was not inspected in this comparison. The latter is a residual historical-priority risk rather than evidence of novelty.

## Limitations

The sampling measure fixes the plane through the center and makes only its orientation random. No claim is made for invariant random affine planes, deformed truncated octahedra, or complete Euclidean shape distributions within each polygon type. The formulas concern the exact Archimedean model. A bounded literature comparison cannot exclude older specialized stereological or crystallographic tables; independent historical and mathematical verification remains worthwhile.

## References

1. M.-C. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1 (2023-04-27), https://arxiv.org/abs/2304.14239 . See Theorem 1.1 and Example 5.1.
2. R. De Leo, *Topology of plane sections of periodic polyhedra with an application to the Truncated Octahedron*, arXiv:math/0502219 (2005-02-10), https://arxiv.org/abs/math/0502219 .
