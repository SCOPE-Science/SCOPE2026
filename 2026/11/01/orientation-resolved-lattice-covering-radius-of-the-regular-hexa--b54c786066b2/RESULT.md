# Orientation-resolved lattice covering radius of the regular hexagon and its symmetry-breaking optimum

## Finding

Let \(H_\theta\) be the regular planar hexagon of circumradius one whose vertices have arguments \(\theta+k\pi/3\), \(k=0,\ldots,5\). Its fixed-orientation square-lattice covering radius is
\[
\mu(\theta)=\inf\{r>0:\mathbb R^2=\mathbb Z^2+rH_\theta\}.
\]
It is even and \(\pi/6\)-periodic. For \(0\le\theta\le\pi/12\), writing \(c=\cos\theta\) and \(s=\sin\theta\), its *complete* orientation profile is
\[
\boxed{\mu(\theta)=\max\left\{\frac{(\sqrt3+1)c+(1-\sqrt3)s}{2\sqrt3},\ \frac{(\sqrt3+2)c+s}{3\sqrt3}\right\}.}
\]
The two branches exchange dominance only at
\[
\theta_* =\arctan\left(\frac{4-\sqrt3}{13}\right).
\]
The covering radius is strictly decreasing from \(0\) to \(\theta_*\), and strictly increasing from \(\theta_*\) to \(\pi/12\). Therefore the *global* optimal orientation classes are exactly \(\theta\equiv\pm\theta_*\pmod{\pi/6}\), and
\[
\boxed{\min_{\theta}\mu(\theta)=\sqrt{\frac{11+6\sqrt3}{39}}\approx0.7406217908365096.}
\]
The maximum is \(\max_\theta\mu(\theta)=1/(3-\sqrt3)\), attained exactly for \(\theta\equiv0\pmod{\pi/6}\). The latter maximum is already known; the new result is the pointwise orientation profile, its cusp, and its sharp minimizing orientations and constant.

## Assumptions and scope

The square lattice is exactly \(\mathbb Z^2\), and the hexagon is not rescaled in its definition: every vertex is Euclidean distance one from the origin. The lattice is fixed and only the hexagon rotates. The covering property is for *all* real points, not a finite sample. The Minkowski gauge of the unrotated hexagon is
\[
N(u,v)=\max\left\{|u|+\frac{|v|}{\sqrt3},\ \frac{2|v|}{\sqrt3}\right\},
\]
and \(N_\theta(x)=N(R_{-\theta}x)\). In particular, \(N_\theta(x)\ge\|x\|_2\), since \(H_\theta\) is contained in the Euclidean unit disk. The covering radius equals \(\sup_x\min_{z\in\mathbb Z^2}N_\theta(x-z)\). Reflection and quarter-turn symmetries of the lattice, combined with sixth-turn symmetries of the hexagon, reduce all orientations to \([0,\pi/12]\).

## Proof

**The triangle-cover lemma.** Let \(K\) be a centrally symmetric convex body and \(a,b,d\) three noncollinear points. If \(p\) belongs simultaneously to \(a+rK\), \(b+rK\), and \(d+rK\) and lies in their triangle, the whole triangle belongs to the union of these three translates. Indeed, for each edge \([a,b]\), its midpoint \(m\) belongs to both \(a+rK\) and \(b+rK\): the triangle inequality gives \(N_K(a-b)\le2r\). The triangles \(\operatorname{conv}\{a,m,p\}\) and \(\operatorname{conv}\{b,m,p\}\) lie in their respective convex translates. The six such triangles from the three edges tile \(\operatorname{conv}\{a,b,d\}\). This proves the lemma, including the boundary case.

Put
\[
A=\frac{(\sqrt3+1)c+(1-\sqrt3)s}{2\sqrt3},\qquad
B=\frac{(\sqrt3+2)c+s}{3\sqrt3},\qquad
\eta=\frac{4-\sqrt3}{13}.
\]
Define two points in rotated (hexagon) coordinates:
\[
q_A=\left(\frac{c+s/\sqrt3}{2},\frac{c-\sqrt3s}{2}\right),\qquad
q_B=\left(\frac{c+s/\sqrt3}{2},\frac{(4-\sqrt3)c-s}{6}\right),
\]
and in lattice coordinates \(p_A=R_\theta q_A\), \(p_B=R_\theta q_B\). In the whole range \(0\le\theta\le\pi/12\), both \(p_A,p_B\) belong to \([0,\tfrac12]^2\), hence to the triangle \(T=\operatorname{conv}\{0,e_1,e_2\}\). For clarity, the first coordinates are
\[
(p_A)_1=\tfrac12-\tfrac12(1-1/\sqrt3)cs,
\quad
(p_B)_1=\tfrac12c^2+\tfrac16s^2+\tfrac13(\sqrt3-2)cs,
\]
and the second coordinates are
\[
(p_A)_2=\tfrac12-\tfrac12(1-1/\sqrt3)s^2-\tfrac12(\sqrt3-1)cs,
\quad
(p_B)_2=\tfrac16(4-\sqrt3)c^2+\tfrac13cs+\tfrac1{2\sqrt3}s^2.
\]
Their indicated bounds follow directly from \(0\le s\le\sin(\pi/12)\), \(0\le cs\le1/4\), \(c^2\ge(2+\sqrt3)/4\), and \(s^2\le(2-\sqrt3)/4\); all four coordinates are strictly positive except possible endpoint values. In particular \((p_B)_2\le (4-\sqrt3)/6+1/12+(2-\sqrt3)/(8\sqrt3)<1/2\).

Substitution in the six linear forms defining \(N\) gives
\[
\begin{array}{c|ccc}
 &N_\theta(p)&N_\theta(p-e_1)&N_\theta(p-e_2)\\\hline
p=p_A&A&A&\max\{A,c/\sqrt3+s\}\\
p=p_B&B&B&\max\{B,F\}
\end{array},
\quad
F=\left(\frac23+\frac{\sqrt3}{9}\right)c+
\left(-1+\frac{2\sqrt3}{9}\right)s.
\]
Here are the sign checks underlying the substitution, so this table does not rely on numerical sampling. Both \(q_A,q_B\) have positive components; after subtracting \(R_{-\theta}e_1=(c,-s)\) their first components are negative and their second components positive; after subtracting \(R_{-\theta}e_2=(s,c)\) the first components are positive and second negative. The only potentially competing half-plane term at \(p-e_1\) is \(2(v+s)/\sqrt3\), which is at most the displayed \(A\) or \(B\). For the two witnesses, respectively, the differences are
\[
A-\frac{2(v_A+s)}{\sqrt3}
=\frac{3-\sqrt3}{6}c+\frac{1-\sqrt3}{2}s\ge0,
\]
\[
B-\frac{2(v_B+s)}{\sqrt3}
=\frac{6-2\sqrt3}{9}c-\frac{4\sqrt3}{9}s\ge0.
\]
Both inequalities follow from \(0\le\tan\theta\le2-\sqrt3\), the second strictly at the right endpoint. The competing term at \(p\) is controlled by \(u\ge v/\sqrt3\), seen from the displayed positive coordinates. The remaining terms are the two entries shown in the table.

The differences governing the two active regimes are
\[
A-(c/\sqrt3+s)=\frac{(3-\sqrt3)c-(9-\sqrt3)s}{6},
\quad
B-F=\frac{-(3-\sqrt3)c+(9-\sqrt3)s}{9}.
\]
Both vanish exactly when \(\tan\theta=(3-\sqrt3)/(9-\sqrt3)=\eta\). Hence for \(0\le\theta\le\theta_*\), the point \(p_A\) has gauge distance exactly \(A\) from each of \(0,e_1,e_2\); for \(\theta_*\le\theta\le\pi/12\), \(p_B\) has gauge distance exactly \(B\) from each of those three vertices.

By the triangle-cover lemma, the corresponding three lattice translates cover \(T\) at radius \(r=\max\{A,B\}\). The complementary triangle \(\operatorname{conv}\{e_1+e_2,e_1,e_2\}\) is the central reflection of \(T\) and has the same covering certificate, because \(H_\theta=-H_\theta\). Thus all of \([0,1]^2\), and by periodicity all of \(\mathbb R^2\), is covered. This establishes \(\mu(\theta)\le r\).

For the reverse inequality, use the same selected witness \(p\). Its distance to the first three lattice corners is \(r\). The supporting functional \(\ell_\theta(x)=(1,1/\sqrt3)\cdot R_{-\theta}x\) satisfies \(\ell_\theta(x)\le N_\theta(x)\) and \(\ell_\theta(p)=r\). Since both \(\ell_\theta\) and \(-\ell_\theta\) are bounded above by the centrally symmetric gauge,
\[
N_\theta(p-e_1-e_2)\ge \ell_\theta(e_1+e_2)-r\ge r.
\]
The last inequality follows from the explicit nonnegative differences
\[
\ell_\theta(e_1+e_2)-2A=\frac{2(3-\sqrt3)}3s\ge0,
\]
\[
\ell_\theta(e_1+e_2)-2B=\frac{3-\sqrt3}{9}c+
\frac{9-5\sqrt3}{9}s>0.
\]
Every other integer lattice point \(z\notin\{0,e_1,e_2,e_1+e_2\}\) is Euclidean distance at least one from \(p\in[0,1/2]^2\). Consequently \(N_\theta(p-z)\ge1>r\), where \(r\le A(0)=1/(3-\sqrt3)<1\) (or directly from the two displayed trigonometric expressions). Thus \(p\) is at gauge distance at least \(r\) from the entire lattice. This proves \(\mu(\theta)\ge r\), completing the exact formula.

Finally, \(A\) is strictly decreasing on \([0,\pi/12]\), while \(B\) is strictly increasing on \([0,\pi/12)\) (its derivative vanishes only at \(\pi/12\)). They cross exactly once at \(\theta_*\). Elementary simplification gives
\[
A(\theta_*)^2=B(\theta_*)^2=(11+6\sqrt3)/39.
\]
The maximum on the reduced angular interval occurs at \(\theta=0\), because \(A(0)>B(\pi/12)\), and all equality classes follow from the reduction by symmetries.

## Verification

The standalone `verify.py` uses only the Python standard library. It checks the two symbolic-constant identities to floating-point precision, 2,001 orientations against both explicit three-corner certificates and all nearby noncorner lattice points, and a \(61\times61\) grid of the fundamental square for each of 31 orientations. It also checks strict piecewise monotonicity on a 2,000-point diagnostic grid. Its deterministic output is `PASS: 119356 deterministic covering-profile diagnostics`. These finite checks support but do not replace the preceding universal proof.

## Relationship to prior work

F. Xue (2019), *On the Lattice Point Covering Problem in Dimension 2*, proves that a regular hexagon of circumradius one has least dilation \(1/(3-\sqrt3)\) with the lattice-point covering property **under all rotations and translations**. It does not identify the pointwise fixed-orientation radius, its minimizing rotation, or its symmetry-breaking cusp. A published extension, *Exact lattice-point covering radii for all regular polygons with two modulo four sides*, similarly evaluates the **supremum over rotations**, not the complete orientation profile. Its hexagonal specialization agrees exactly with the maximum here; it cannot imply the smaller minimum or the two-branch identity from the supremum alone.

G. Codenotti, A. Freyer and K. Krivokuća (2026) study inclusion-minimal integer-lattice coverings and Brunn–Minkowski inequalities for covering radii. Their general covering framework motivates the fixed-shape optimization but does not present the sharp square-lattice rotation profile of the regular Euclidean hexagon. Related discussions of covering hexagonal norms and affine hexagons do not establish the exact fixed-Euclidean-shape angle dependence displayed above.

## Limitations

The lattice is exactly square, the shape is exactly a regular centrally symmetric hexagon, and the dimension is two. Other lattices, affine hexagons, and nonregular polygons are not covered. The worst-orientation value is prior art. The originality claim concerns only the previously unlocated fixed-orientation law and minimizing-angle classification; an older formulation in terms of normed-plane Voronoi cells, critical lattice holes, or covering density might be equivalent and remains a historical-priority risk. There has been no independent mathematical audit.

## References

F. Xue, *On the Lattice Point Covering Problem in Dimension 2*, Electron. J. Combin. 26(2) (2019), P2.9; arXiv:1810.03555; DOI 10.37236/8245.

G. Codenotti, A. Freyer and K. Krivokuća, *Minimal covering bodies and Brunn-Minkowski type inequalities for the covering radius*, arXiv:2606.14442, first publicly posted 2026-06-12.

*Exact lattice-point covering radii for all regular polygons with two modulo four sides*, published research record dated 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-lattice-point-covering-radii-for-all-regular-polygons-with--35b1a362e217.
