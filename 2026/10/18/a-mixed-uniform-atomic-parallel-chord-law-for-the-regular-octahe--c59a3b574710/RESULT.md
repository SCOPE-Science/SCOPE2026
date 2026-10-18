# A mixed uniform–atomic parallel-chord law for the regular octahedron

## Finding
Let \(K=\{(x_1,x_2,x_3)\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}\), the regular octahedron of circumradius one. Fix a threefold symmetry direction \(u=(1,1,1)/\sqrt3\). Select a line parallel to \(u\) by taking its perpendicular offset uniformly with respect to planar area among all lines meeting \(K\), and let \(L\) denote the chord length.

Then the **complete** distribution, including its singular component, is
\[
\boxed{\quad L\ \overset{\mathrm d}=\ \frac2{\sqrt3}\begin{cases} U,&\text{with probability }2/3,\\1,&\text{with probability }1/3,\end{cases}\qquad U\sim\operatorname{Uniform}[0,1].\quad}
\]
The mixture choice and \(U\) are independent. In particular, \(L\) has density \(1/\sqrt3\) on \((0,2/\sqrt3)\) and a mass \(1/3\) at \(2/\sqrt3\). No mass is at zero. Equivalently, its distribution function is \(F_L(r)=0\) for \(r<0\), \(F_L(r)=r/\sqrt3\) for \(0\le r<2/\sqrt3\), and \(F_L(r)=1\) for \(r\ge2/\sqrt3\).

The associated **directional covariogram** is, for all \(r\ge0\),
\[
\boxed{\quad \operatorname{Vol}_3\bigl(K\cap(K+ru)\bigr)=\begin{cases}\frac43-\sqrt3\,r+\frac12r^2,&0\le r\le2/\sqrt3,\\0,&r\ge2/\sqrt3.\end{cases}\quad}
\]
(The two branches agree at the endpoint.) Consequently \(\mathbb E L=4/(3\sqrt3)\) and \(\operatorname{Var}(L)=4/27\).

## Assumptions and scope
The line distribution is **uniform in perpendicular offset area**, not an isotropic distribution of directions and not a length-biased chord sample. The stated octahedron has vertices \(\{\pm e_1,\pm e_2,\pm e_3\}\). All eight threefold directions are equivalent by its isometries. Endpoint intersections with zero 3-volume are permitted, but chord lengths are taken only from the positive-area projected domain. The formulas remain valid under simultaneous Euclidean similarity rescaling. Under any invertible linear affine image, choosing the image of this line direction with the induced offset-area measure preserves the mixture weights; chord lengths are uniformly scaled in that direction.

## Proof
Write \(t=r/\sqrt3\). Since \(K=\{x:s\cdot x\le1\text{ for every }s\in\{-1,1\}^3\}\), translate the intersection to its midpoint, \(P_t=(K-t\mathbf1/2)\cap(K+t\mathbf1/2)\). It is described by the eight facet inequalities
\[
s\cdot y\le1-\frac t2\left|s_1+s_2+s_3\right|,\qquad s\in\{-1,1\}^3.
\]
For \(0<t<2/3\), its twelve vertices are exactly the six coordinate permutations of \((1-t,-t/2,0)\) and their negatives. To check exhaustiveness, intersect each of the \(\binom83=56\) triples of bounding planes: singular triples give no isolated vertex; the remaining intersections feasible on a nonempty open subinterval of \((0,2/3)\) are exactly those twelve affine coordinate functions. All are feasible throughout that entire interval. The self-contained exact checker `verify.py` enumerates all triples, tests the linear feasibility inequalities at their sharp parameter endpoints, and verifies equality of the two sets of affine vertices. Thus there are no omitted interior parameter phases.

The two faces with outer normals \(\pm(1,1,1)\) are congruent hexagons of Euclidean area \(\sqrt3(4-3t^2)/8\); each of the other six faces is a quadrilateral of area \(\sqrt3(2-t)(2-3t)/8\). These area expressions follow directly by the planar shoelace formula on the displayed affine vertices, multiplying the coordinate-area determinant by \(\sqrt3\). Their distances from the origin are, respectively, \((1-3t/2)/\sqrt3\) and \((1-t/2)/\sqrt3\). Summing the eight oriented face pyramids (divergence theorem) gives
\[
\operatorname{Vol}_3(P_t)=\frac{1}{3\sqrt3}\left[2\left(1-\frac{3t}{2}\right)\frac{\sqrt3(4-3t^2)}8+6\left(1-\frac t2\right)\frac{\sqrt3(2-t)(2-3t)}8\right]
=\frac{(2-3t)(4-3t)}6.
\]
At \(t=0\), this equals the known octahedron volume \(4/3\). At \(t=2/3\), the overlap is planar and its three-dimensional volume is zero; for larger \(t\), the two octahedra have disjoint interiors by the triangle inequality \(\|t\mathbf1\|_1>2\). Substituting \(t=r/\sqrt3\) proves the covariogram identity for every \(r\ge0\).

Let \(\Omega\subset u^\perp\) be the orthogonal projection of \(K\). The intersection of \(K\) with a line at offset \(y\in\Omega\) is an interval of length \(L(y)\). Fubini's theorem, using translations along \(u\), gives the exact chord-survival identity
\[
g(r):=\operatorname{Vol}_3(K\cap(K+ru))=\int_\Omega (L(y)-r)_+\,dy.
\]
The right derivative exists for \(0\le r<2/\sqrt3\), and \(-g'_+(r)=|\{y\in\Omega:L(y)>r\}|\). Thus \(|\Omega|=-g'_+(0)=\sqrt3\), and, for \(0\le r<2/\sqrt3\),
\[
\Pr(L>r)=\frac{-g'_+(r)}{|\Omega|}=1-\frac r{\sqrt3}.
\]
As \(r\) approaches \(2/\sqrt3\) from below, this survival probability tends to \(1/3\). Every chord has length at most \(2/\sqrt3\), because the displacement of two points of \(K\) has \(\ell_1\)-norm at most two. Therefore the remaining probability \(1/3\) is an **atom at the maximal chord length**, and the continuous component is uniform. Integrating its density and atom yields the stated mean and variance. All quantifiers and endpoint conventions follow from this argument.

## Verification
Execute `python3 verify.py` with Python 3 and SymPy. It verifies all nonsingular triples of the eight supporting planes, exact feasibility over the entire open parameter interval, the twelve affine vertices, both facet-area formulas' volume identity, the covariogram normalization, and the atomic/continuous probability weights. Independently, numerical halfspace-intersection and convex-hull volume computations were compared with the polynomial at many parameter values across \((0,2/3)\); these numerical samples are sanity checks, not the infinite-parameter proof. The exact geometric proof and symbolic enumeration are both provided above; the checker is supplementary.

## Relationship to prior work
Bianchi's work on the covariogram of three-dimensional convex polytopes explains the geometric tomography importance of full directional overlap information and the connection to parallel chord lengths, but its determination theorem does not give this body-diagonal octahedron chord law. Ciccariello's analysis of the regular octahedron computes a **rotationally averaged (isotropic)** chord-length density; that angular average is not a distribution conditioned on one prescribed threefold direction and does not supply the singular mass found here. Earlier formulas for octahedral projection widths and random shadows concern different functionals. The cubic-to-quadratic cancellation in the overlap volume and the endpoint atom are the stated contribution; no general covariogram uniqueness theorem is claimed as new.

## Limitations
Only lines parallel to one of the octahedron's threefold directions are covered, not the complete directional family. The result does not claim a new formula for the isotropic octahedral chord distribution, and it does not characterize chord laws of arbitrary convex bodies. Independent validation and definitive historical-priority certification have not been performed; an unindexed older calculation of this particular directional law cannot be excluded.

## References
1. G. Bianchi, *The covariogram determines three-dimensional convex polytopes*, arXiv:0805.1605, first public version 12 May 2008; especially Introduction and Theorem 1.1. https://arxiv.org/abs/0805.1605
2. S. Ciccariello, *The chord-length probability density of the regular octahedron*, arXiv:1401.7950, first public version 30 January 2014; especially Introduction, equations (1)–(3), and its isotropic direction integral. https://arxiv.org/abs/1401.7950
