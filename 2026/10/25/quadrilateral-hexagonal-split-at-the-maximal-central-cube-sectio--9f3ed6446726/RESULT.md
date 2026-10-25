# Quadrilateral–hexagonal split at the maximal central cube-section area

## Finding

Let \(Q=[-1,1]^3\), and draw \(U\) from normalized spherical area measure on \(S^2\). Let \(A(U)\) be the ordinary Euclidean area of \(Q\cap U^\perp\), and let \(N(U)\) be the number of vertices of this section (defined almost surely, away from the finitely many degeneracy arcs). Ball's known maximal-section theorem gives \(A(U)\le4\sqrt2\). For an **absolute area deficit** \(\delta>0\), the following distinct sharp tail laws hold:

\[
\boxed{\begin{aligned}
\Pr\{A(U)>4\sqrt2-\delta,\ N(U)=4\}
 &=\frac{3\sqrt2}{16\pi}\,\delta^2+o(\delta^2),\\
\Pr\{A(U)>4\sqrt2-\delta,\ N(U)=6\}
 &=\frac{3\sqrt2(2+\pi)}{32\pi}\,\delta^2+o(\delta^2).
\end{aligned}}
\]

The total upper tail consequently equals
\[
\boxed{\Pr\{A(U)>4\sqrt2-\delta\}
=\frac{3\sqrt2(4+\pi)}{32\pi}\,\delta^2+o(\delta^2).}
\]
More particularly, the conditional combinatorial type in an extreme-area section has a nontrivial limit:
\[
\boxed{\lim_{\delta\downarrow0}\Pr\{N(U)=4\mid A(U)>4\sqrt2-\delta\}
=\frac{2}{4+\pi},\qquad
\lim_{\delta\downarrow0}\Pr\{N(U)=6\mid A(U)>4\sqrt2-\delta\}
=\frac{2+\pi}{4+\pi}.}
\]
These ratios are for central sections of the cube, not orthogonal shadows or translated random cuts.

## Assumptions and scope

The cutting plane is uniformly distributed among **planes through the cube center**, namely \(U^\perp\) for Haar-uniform \(U\). Both \(U\) and \(-U\) describe the same plane, with no effect on the probabilities. Area is two-dimensional Euclidean Lebesgue measure and the cube side is \(2\); scaling the cube by \(c>0\) scales absolute area deficits by \(c^2\). The only generic section types are centrally symmetric quadrilaterals and hexagons. The event of a plane containing a cube vertex has measure zero and may be assigned either boundary convention.

## Proof

**1. Exact area and type, independently of the asymptotic.** By symmetry assume the unit normal has coordinates \(a\ge b\ge0\) and \(a\ge c\ge0\), with \(a^2+b^2+c^2=1\). Write \(y=b/a\), \(z=c/a\), hence \(0\le y,z\le1\) and \(a=(1+y^2+z^2)^{-1/2}\). A central section meets all six cube faces in a segment if and only if \(a<b+c\), equivalently \(y+z>1\). Otherwise it is a parallelogram. Thus generically
\[
N(U)=\begin{cases}4,&y+z<1,\\6,&y+z>1.\end{cases}
\]
The exact area is
\[
\mathcal A(y,z)=4\sqrt{1+y^2+z^2}
\left(1-\frac{(y+z-1)_+^2}{4yz}\right),
\tag{1}
\]
with the limiting value understood if \(yz=0\). To derive (1), let \(X_1,X_2,X_3\) be independent uniforms on \([-1,1]\). The density of \(aX_1+bX_2+cX_3\) at zero is the section area divided by \(8\), since the normal has unit length. Conditioning on \(bX_2+cX_3\) shows the density equals \(1/(2a)\) if \(a\ge b+c\), and otherwise equals
\[
\frac1{2a}\left(1-\frac{(b+c-a)^2}{4bc}\right).
\]
Indeed, the two corner triangles omitted by \(|bX_2+cX_3|\le a\) have total probability \((b+c-a)^2/(4bc)\). Multiplication by \(8\) yields (1). This area identity is also independently checked by explicit intersections of cube edges with a plane in the verification program.

**2. Haar measure and localization.** In the positive-octant chart where the first coordinate is largest, the parametrization
\[
U=\frac{(1,y,z)}{\sqrt{1+y^2+z^2}},\qquad 0\le y,z\le1,
\]
has spherical area element \((1+y^2+z^2)^{-3/2}\,dy\,dz\). There are \(8\) coordinate-sign choices and \(3\) choices for the largest coordinate; dividing by the spherical area \(4\pi\) gives, for any event determined by \(\mathcal A\) and the section type,
\[
\Pr(E)=\frac6\pi\int_0^1\int_0^1
\mathbf1_E(y,z)\,(1+y^2+z^2)^{-3/2}\,dy\,dz.
\tag{2}
\]
Ball's maximal-section theorem, or its three-dimensional equality characterization, identifies the maximizing normals as permutations and sign changes of \((1,1,0)/\sqrt2\). In the chart of (2), this maximum occurs only at the two corners \((y,z)=(1,0)\) and \((0,1)\). Compactness and continuity imply that, for sufficiently small \(\delta\), the event \(\{\mathcal A>4\sqrt2-\delta\}\) lies in arbitrarily small neighborhoods of these corners. Symmetry interchanges the corners. Hence it suffices to analyze \((1,0)\), and its contribution is doubled.

**3. Uniform local area deficits.** Put \(y=1-s\) and \(z=t\) near the corner, with \(s,t\ge0\). The quadrilateral chamber is \(s>t\); the hexagonal chamber is \(t>s\). In the first,
\[
4\sqrt2-\mathcal A(1-s,t)=2\sqrt2\,s+O((s+t)^2).
\tag{3}
\]
In the second,
\[
4\sqrt2-\mathcal A(1-s,t)
=\sqrt2\left(t+\frac{s^2}{t}\right)+O((s+t)^2).
\tag{4}
\]
Both estimates are uniform as \(s+t\to0\) within their closed respective chambers: for the second, \(s\le t\) makes \((t-s)^2/t\le t\) and controls the product-expansion remainder uniformly. In both chambers, the leading deficit is bounded above and below by fixed positive multiples of \(s+t\). Shrinking the neighborhood if necessary, the exact deficit is likewise comparable to \(s+t\). Thus, on the event with deficit below \(\delta\), \(s+t=O(\delta)\).

**4. Blow-up and exact constants.** Set \(s=\delta u\), \(t=\delta v\). By (3) and (4), the quadrilateral and hexagonal sublevel sets converge away from null boundaries to the bounded domains
\[
\mathcal D_4=\{u\ge v\ge0:\ 2\sqrt2\,u<1\},
\qquad
\mathcal D_6=\{v>u\ge0:\ \sqrt2(v+u^2/v)<1\}.
\]
The spherical density converges uniformly on these bounded domains to \(2^{-3/2}\). The preceding comparability permits dominated convergence for the rescaled indicator functions. Their areas are
\[
|\mathcal D_4|=\frac12\left(\frac1{2\sqrt2}\right)^2=\frac1{16}
\]
and, using \(u=rv\) with \(0\le r\le1\),
\[
\begin{aligned}
|\mathcal D_6|
&=\int_0^1\int_0^{1/(\sqrt2(1+r^2))}v\,dv\,dr
=\frac14\int_0^1\frac{dr}{(1+r^2)^2}\\
&=\frac1{16}+\frac\pi{32}=\frac{2+\pi}{32}.
\end{aligned}
\]
The prefactor from (2), the two equivalent corners, and the limiting density is
\[
\frac6\pi\times2\times2^{-3/2}=\frac{3\sqrt2}\pi.
\]
Multiplying by the two domain areas proves the two exact joint tails. Summing them proves the total tail. Dividing each joint tail by the total proves the conditional limiting proportions. This argument also shows why applying only a smooth quadratic Hessian approximation at a maximizer would miss the leading behavior: the maximum lies on the boundary between polygonal section types. \(\square\)

## Verification

The standalone script `verify_cube_section_tail.py` requires Python 3, NumPy and SciPy. From this directory run `python3 verify_cube_section_tail.py`. It reconstructs each central section from its intersections with all 12 cube edges and computes its two-dimensional convex-hull area and vertex count. For 540 independently sampled directions, including near-maximal directions on both sides of the combinatorial boundary, it compares the geometry against (1). Separately, exact finite-threshold spherical integrals in the \((y,z)\) chart are evaluated by root finding and quadrature, and their joint probabilities converge to the two predicted leading constants for decreasing \(\delta\). Successful output ends with `ALL_CUBE_SECTION_TAIL_CHECKS_OK`. These finite checks corroborate, but do not substitute for, the limiting proof above.

## Relationship to prior work

Ball's cube slicing theorem [1] supplies the sharp maximum and its maximizing directions, but no probability distribution of almost-maximizing central sections. Lonke [2] calculates expected face counts of Haar-random cube sections, which in three dimensions determines the **unconditional** quadrilateral–hexagon probability, not the conditional extreme-area split. Ambrus [3] classifies critical central cube sections and provides the standard convolution-density formula for their area; the inspected results do not give upper-tail asymptotics or limiting conditional section types. A published formula for the Haar hexagon probability of rectangular-box sections [4] covers the zero-threshold type probability but not area-weighted or extreme-area type probabilities. The present claim is the quantitative two-type blow-up law at the Ball maximizers; the known maximizing area and unconditional type probabilities are explicitly not claimed as new.

## Limitations

The constants concern three-dimensional cubes, **central** planes with Haar-distributed normals, and the limit of absolute area deficit \(\delta\downarrow0\). They do not apply unchanged to uniformly translated affine planes, random shadows, other dimensions, or different normal distributions. The error \(o(\delta^2)\) is not quantified uniformly under perturbations of the cube. Historical-priority verification is limited by indexed literature and accessible primary texts; an equivalent unindexed or differently formulated result cannot be excluded. No independent mathematical audit is claimed.

## References

1. K. Ball, *Cube slicing in \(\mathbb R^n\)*, Proceedings of the American Mathematical Society **97** (1986), 465–473, DOI `10.1090/S0002-9939-1986-0840631-0`.
2. Y. Lonke, *On random sections of the cube*, arXiv:`math/9812123`, first posted 1998-12-21; subsequently Discrete & Computational Geometry **23** (2000), 157–169.
3. G. Ambrus, *Critical central sections of the cube*, arXiv:`2107.14778`, first posted 2021-07-30; Proceedings of the American Mathematical Society.
4. *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, published indexed geometry result (2026), consulted in full for the statement and proof of the unconditional type law.
