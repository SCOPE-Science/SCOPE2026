# Exact central-section area and six/eight-arc law of the orthogonal tricylinder

## Finding

For any \(R>0\), define the equal-radius orthogonal tricylinder
\[
K_R=\{x\in\mathbb R^3:x_1^2+x_2^2\le R^2,\ x_1^2+x_3^2\le R^2,\ x_2^2+x_3^2\le R^2\}.
\]
A generic central plane \(H=n^\perp\), with unit normal \(n\), meets the boundary of \(K_R\) in **exactly six or eight maximal smooth conic arcs**, with one genuine corner at each consecutive junction. Write \(a\ge b\ge c\) for the decreasing rearrangement of \((|n_1|,|n_2|,|n_3|)\). Away from the zero-measure cases described below,
\[
N(n)=\begin{cases}6,&a<b+c,\\8,&a>b+c.\end{cases}
\]
Every arc is an elliptical arc from exactly one constituent cylinder, and there is an explicit finite **elementary-arctangent formula for its complete section area for every generic normal**, given below. In particular, for a Haar-uniform unoriented central plane,
\[
\Pr\{N=8\}=\frac{12}{\pi}\arctan(3-2\sqrt2)=0.649040687816\ldots,
\qquad \Pr\{N=6\}=1-\Pr\{N=8\}.
\]
This is a law of curved conic **arc count**, not polygon side count. The six-arc probability agrees with the previously known probability that a Haar central section of the unit cube is hexagonal; the equality of the orientation chambers is proved here, whereas the cube probability itself is not claimed as new.

## Assumptions and scope

The three defining cylinders are **infinite** equal-radius solid right circular cylinders with axes along the three coordinate axes. The section is by a plane *through the common center* and the area is ordinary two-dimensional Euclidean area in that plane. Directions are distributed by Haar measure on \(S^2/\{\pm1\}\), not by affine line or translated-plane measure.

For the arc and area formula, it suffices that all \(n_i\ne0\) and \(a\ne b+c\), with any further coincident breakpoints excluded. Those exceptions form a set of spherical measure zero. All generic expressions remain valid when two \(|n_i|\) are equal, provided no actual breakpoint coincidences occur; boundary-case areas are obtained by continuity. At \(a=b+c\), a simultaneous triple-cylinder junction may occur, and the generic count is intentionally not asserted there.

## Proof

### 1. Active cylinders and all breakpoints

For a unit vector \(u\in H\), the section's radial function is
\[
\rho(u)^2=\frac{R^2}{\max_i(1-u_i^2)}
=\frac{R^2}{1-\min_i u_i^2}.
\]
Thus the boundary lies on cylinder \(i\), which has equation \(\sum_{k\ne i}x_k^2=R^2\), exactly when \(u_i^2=\min_k u_k^2\). This is an ellipse in \(H\) when \(n_i\ne0\). A transition between cylinders \(i\) and \(j\) occurs where \(u_i=s u_j\) for \(s\in\{-1,1\}\), provided this tied value is strictly smaller in absolute value than \(u_k\), where \(\{i,j,k\}=\{1,2,3\}\). The two antipodal candidate directions are
\[
\pm v_{ij,s},\qquad
v_{ij,s}=\frac{n\times(e_i-s e_j)}{\|n\times(e_i-s e_j)\|}.
\]
At such a candidate, \(n\cdot u=0\) gives \(n_k u_k=-(n_i+s n_j)u_i\). Since \(n_k\ne0\), the candidate is active if and only if
\[
|n_k|<|n_i+s n_j|.
\tag{1}
\]
For a strict active candidate, the switch is transverse: the derivative of \(u_i^2-u_j^2\) along the unit circle is nonzero because \(u_i=s u_j\ne0\) and \(e_i-s e_j\) has a nonzero projection into \(H\). Hence it is a genuine corner, with one arc between each consecutive pair of breakpoints. No other transitions are possible.

### 2. Sharp six/eight classification

Sign reversals and coordinate permutations let us write \(n=(a,b,c)\) with \(a\ge b\ge c>0\). Consider the six pair/sign choices in (1). For the \((a,b)\)-pair the plus choice is always active and the minus choice is active exactly when \(a>b+c\). For the \((a,c)\)-pair the same holds. For the \((b,c)\)-pair its plus choice is active exactly when \(a<b+c\), whereas its minus choice is never active. Therefore the number of active unoriented breakpoint lines equals three if \(a<b+c\), and four if \(a>b+c\). Each line supplies two antipodal section corners. This proves \(N=6\) or \(N=8\), respectively, and proves that the listed arcs are maximal and exhaustive.

### 3. Elementary formula for every generic section area

Choose any positively oriented orthonormal basis \((e,f)\) of \(H\), so \(e\times f=n\). Form **all** active \(\pm v_{ij,s}\) satisfying (1). Order their polar angles in this basis cyclically:
\[
0\le\theta_1<\cdots<\theta_N<2\pi,\quad
\theta_{N+1}=\theta_1+2\pi,\quad
u_j=e\cos\theta_j+f\sin\theta_j.
\]
Put \(u_{N+1}=u_1\), and let \(i(j)\) be the unique index minimizing \(u_i^2\) at the **angular midpoint** of the open interval \((\theta_j,\theta_{j+1})\). Write \(\Delta_j=\theta_{j+1}-\theta_j\in(0,\pi)\), and \(c_j=|n_{i(j)}|\). Then
\[
\boxed{
\operatorname{Area}(K_R\cap n^\perp)
=\frac{R^2}{2}\sum_{j=1}^{N}
\frac{1}{c_j}\operatorname{atan2}\!\left(
  c_j\sin\Delta_j,\,
  u_j\cdot u_{j+1}-u_{j,i(j)}u_{j+1,i(j)}
\right).}
\tag{2}
\]
Here \(\operatorname{atan2}(y,x)\) is the argument in \((0,\pi)\) for \(y>0\), and the formula uses only square roots, dot/cross products, sorting, and inverse tangents. Formula (2) is independent of the arbitrary oriented basis.

To derive it, polar area in \(H\) gives
\[
A=\frac{R^2}{2}\sum_j\int_{\theta_j}^{\theta_{j+1}}
\frac{d\theta}{1-u_{i(j)}(\theta)^2}.
\tag{3}
\]
On \(H\), let \(T_i\) be an orientation-preserving linear map whose Gram matrix is
\(T_i^*T_i=I_H-(\operatorname{proj}_H e_i)(\operatorname{proj}_H e_i)^*\). Its two singular values are \(1\) and \(|n_i|\), so \(\det T_i=|n_i|\). The derivative of the polar angle of \(T_i u(\theta)\) is
\[
\frac{|n_i|}{u(\theta)^*T_i^*T_i u(\theta)}
=\frac{|n_i|}{1-u_i(\theta)^2}.
\]
Since consecutive endpoint directions make an oriented angle below \(\pi\), their transformed angle is also in \((0,\pi)\). Its determinant is \(|n_i|\sin\Delta_j\) and its scalar product is \(u_j\cdot u_{j+1}-u_{j,i}u_{j+1,i}\). Integrating the angle derivative evaluates (3) as (2). The sub-\(\pi\) assertion follows because the cyclic list has at least three distinct antipodal breakpoint pairs.

### 4. Haar probabilities

The eight-arc chamber is \(\max_i|n_i|>\sum_{j\ne i}|n_j|\). In each coordinate orthant its three disjoint components are congruent spherical triangles. For the positive orthant component \(x>y+z\), the generating rays are
\[
(1,0,0),\quad(1,1,0),\quad(1,0,1).
\]
The standard solid-angle determinant formula evaluates its area as
\[
\Omega=2\arctan\frac{1}{3+2\sqrt2}
=2\arctan(3-2\sqrt2).
\]
There are \(8\cdot3=24\) such components on the full unit sphere, disjoint apart from null boundaries. Dividing their combined area by \(4\pi\) gives \(\Pr(N=8)=24\Omega/(4\pi)\), hence the stated law.

## Verification

The standalone `verify.py` uses the candidate-direction test (1), computes (2), and independently integrates (3) by a 25,000-point composite midpoint quadrature. It checked 2,000 deterministic Gaussian viewing normals, of which 722 were six-arc and 1,278 eight-arc, matching the independently evaluated inequality \(a<b+c\) in every case. For 64 of these normals, the maximum absolute area discrepancy was \(1.63\times10^{-8}\) at unit radius. A separate 100,000-direction simulation gave eight-arc frequency 0.64643, against the exact 0.649040687816... . Four representative normals additionally passed 50,000-point area checks. Run `python3 verify.py` from the extracted directory with standard Python 3. No probabilistic sample is used as proof of the universal classification or exact probability.

## Relationship to prior work

The classical tricylinder and its volume and surface area have extensive precedents, including Moore (1974), Angell–Moore (1987), and the MathWorld entry [1–3]. These results are **not** claimed as new. Lonke [4] gives general expected face counts for random cube sections, and the explicit 2026 rectangular-box section law [5] establishes that a central section of a unit cube is hexagonal exactly when \(\max_i|n_i|<\sum_{j\ne i}|n_j|\); it also evaluates that known cube probability. Thus the **numerical probability** for six tricylinder arcs coincides with an earlier published numerical probability for hexagonal cube sections. What is added here is the exact geometric identification of all tricylinder switching directions, its six/eight conic-arc phase classification, and the general finite elementary-arctangent **area formula** (2), neither of which follows from the cube-side probability statement alone.

Finch [6] discusses ordinary oblique cylinders and section ellipses but not intersections of three infinite perpendicular cylinders. The unrestricted 1974 and 1987 primary articles [1,2] could not be accessed in full; they remain explicit historical-priority risks rather than evidence of absence. The available excerpts and secondary summary emphasize constituent cylinder intersections and bulk volume rather than formula (2), but **no full-text noncoverage claim** is made for those two papers.

## Limitations

The result concerns **central**, not translated, plane sections. A plane on the null transition set can have merged corner points and is outside the generic arc count. Formula (2) extends by continuity to these planes, but its generic breakpoint-generation algorithm is stated only off the degeneracy set. The area formula does not by itself yield a closed density for the random section area, nor does it claim extremal section areas. Existing literature may contain equivalent formulas under different terminology; the two inaccessible specialist primary papers are a residual historical-priority risk. Verification is numerical and does not replace the geometric proof or an independent scientific audit.

## References

[1] M. Moore, “Symmetrical intersections of right circular cylinders,” *Mathematical Gazette* **58** (1974), 181–185, https://doi.org/10.2307/3615957.

[2] I. O. Angell and M. Moore, “Symmetrical intersections of cylinders,” *Acta Crystallographica* A**43** (1987), 244–250, https://doi.org/10.1107/S0108767387099501.

[3] E. W. Weisstein, “Steinmetz Solid,” *MathWorld*, https://mathworld.wolfram.com/SteinmetzSolid.html (tricylinder volume and twelve curved faces).

[4] Y. Lonke, “On random sections of the cube,” arXiv:math/9812123v1, first public 1998-12-21, https://arxiv.org/abs/math/9812123.

[5] “Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes,” publicly accessible research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.

[6] S. R. Finch, “Oblique Circular Cones and Cylinders,” arXiv:1212.5946v1, first public 2012-12-24, https://arxiv.org/abs/1212.5946.
