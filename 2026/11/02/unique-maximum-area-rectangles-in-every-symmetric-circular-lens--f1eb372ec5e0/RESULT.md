# Unique maximum-area rectangles in every symmetric circular lens

## Finding
For a radius \(R>0\) and separation parameter \(0<c<1\), let
\[
K_{R,c}=\overline B((-Rc,0),R)\cap\overline B((Rc,0),R).
\]
Among **all** Euclidean rectangles contained in \(K_{R,c}\), without any restriction on orientation or center, there is exactly one maximizing rectangle as a geometric subset. It is centered at the origin and its edges are parallel to the coordinate axes. Its horizontal and vertical half-sides are, respectively,
\[
B_c=R\frac{\sqrt{c^2+8}-3c}{4},\qquad
A_c=R\sqrt{\frac{B_c}{R}\left(\frac{B_c}{R}+c\right)}.
\]
In particular \(A_c>B_c\), and the maximum area is \(4A_cB_c\). Thus any positive displacement of the circle centers breaks the disk's square-optimum into a unique, strictly elongated rectangle, with its shorter side along the centers' connecting line.

If \(r=A_c/B_c>1\) is the aspect ratio of the maximizing rectangle, then
\[
c=\frac{r^2-1}{r\sqrt{r^2+1}}.
\]
Hence this dimensionless aspect ratio determines the normalized circle separation uniquely. Knowing the maximum area as well also determines \(R\), and hence the lens up to congruence.

Let \(S_c\) denote the maximum area of an inscribed **square**. Then
\[
S_c=R^2\bigl(\sqrt{2-c^2}-c\bigr)^2<4A_cB_c.
\]
The sharp nearly-coincident and nearly-tangent regimes are
\[
4A_cB_c-S_c=\frac{R^2c^2}{2}+O(R^2c^3)\quad(c\downarrow0),
\]
\[
4A_cB_c\sim \frac{8\sqrt6}{9}R^2(1-c)^{3/2},\qquad
S_c\sim4R^2(1-c)^2\quad(c\uparrow1).
\]
Therefore the rectangle-to-square optimal area ratio diverges as
\[
\frac{4A_cB_c}{S_c}\sim\frac{2\sqrt6}{9}(1-c)^{-1/2}.
\]
The optimal rectangle occupies a fraction tending to \(1/\sqrt3\) of the lens area in the near-tangent limit, compared to \(2/\pi\) for a coincident disk. At \(c=0\), maximum-area rectangles are exactly the squares inscribed in the radius-\(R\) disk, in every orientation; uniqueness is deliberately asserted only for \(0<c<1\).

## Assumptions and scope
The disks have the **same** positive radius, their centers are separated by \(2Rc\), and \(0\le c<1\); all rectangles, including arbitrarily rotated and translated rectangles, are admissible. The special case \(c=0\) is treated separately. The degenerate tangent case \(c=1\), with zero-area intersection, is excluded. Area refers to ordinary two-dimensional Euclidean Lebesgue measure; square means a Euclidean rectangle with equal side lengths.

## Proof
By Euclidean scaling take \(R=1\). Write \(K=K_{1,c}\). The intersection of two disks is centrally symmetric and convex. If a rectangle centered at \(t\) with centered vertex vectors \(\pm v,\pm w\) lies in \(K\), then central symmetry and convexity imply \(v=\tfrac12((t+v)+(-(t-v)))\in K\), and similarly \(-v,w,-w\in K\). Thus translating a feasible rectangle to the origin preserves its feasibility and area. This reduction does not presuppose that its side vectors are axis-aligned.

For a centered rectangle choose perpendicular unit side directions \(u=(\cos\theta,\sin\theta)\) and \(u^\perp=(-\sin\theta,\cos\theta)\), with positive half-lengths \(a,b\). Its vertices are \(\pm au\pm bu^\perp\). Every vertex has squared norm \(a^2+b^2\). A point \((x,y)\) lies in both disks exactly when \(x^2+y^2+2c|x|+c^2\le1\). The maximum absolute horizontal coordinate among the four vertices is \(a|\cos\theta|+b|\sin\theta|\). Consequently, the **exact necessary and sufficient** containment condition is
\[
a^2+b^2+2c(a|\cos\theta|+b|\sin\theta|)+c^2\le1.
\]
For \(c>0\), \(a|\cos\theta|+b|\sin\theta|\ge\min(a,b)\) because \(|\cos\theta|+|\sin\theta|\ge1\). Equality for positive half-lengths occurs only when a side lies on the line of centers (modulo sign and exchange of side labels). Thus every optimal rectangle must be axis-aligned: any positive angular excess can be removed and its sides enlarged. Write \(b\) for its horizontal half-length and \(a\) for its vertical half-length, with \(a\ge b\). Containment is equivalent to
\[
a^2+(b+c)^2\le1.
\]
At a maximizer equality holds. The restriction \(a\ge b\) gives \(0<b\le b_{\square}\), where
\[
b_{\square}=\frac{\sqrt{2-c^2}-c}{2}.
\]
It remains to maximize \(F(b)=4b\sqrt{1-(b+c)^2}\) on this interval. Its derivative has the sign of \(1-c^2-3bc-2b^2\), a strictly decreasing function of \(b>0\). It is positive at zero, whereas at \(b=b_{\square}\) it equals \(-cb_{\square}<0\). Hence there is precisely one maximizer \(b_c\) in the **interior** of the interval, with
\[
2b_c^2+3cb_c+c^2=1,\qquad b_c=\frac{\sqrt{c^2+8}-3c}{4}.
\]
The corresponding \(a_c=\sqrt{1-(b_c+c)^2}\) satisfies \(a_c^2=b_c(b_c+c)>b_c^2\). This proves orientation, shape, area and strict nonsquare optimality.

We also check **uniqueness of the center**, rather than merely existence of a centered maximizer. Suppose an optimal axis-aligned rectangle with these half-lengths has center \((\xi,\eta)\). The two vertices on its right side belong to the disk centered at \((-c,0)\); averaging their two disk inequalities gives \((\xi+b_c+c)^2+a_c^2+\eta^2\le1\). Similarly the two vertices on its left side, tested against the disk centered at \((c,0)\), give \((\xi-b_c-c)^2+a_c^2+\eta^2\le1\). Average these inequalities and use \((b_c+c)^2+a_c^2=1\) to obtain \(\xi^2+\eta^2\le0\). Hence the center is uniquely the origin.

The aspect relation follows from \(a_c^2=b_c(b_c+c)\): \(r^2=1+c/b_c\). Substituting \(b_c=c/(r^2-1)\) into \(2b_c^2+3cb_c+c^2=1\) yields \(c=(r^2-1)/(r\sqrt{r^2+1})\). This strictly increases from zero to one as \(r\) increases from one to infinity, establishing the inverse assertion. The optimal square is likewise centered and axis-aligned; imposing \(a=b\) in the exact containment condition yields \(S_c=4R^2b_{\square}^2\).

For completeness, Taylor expansion of the displayed radical formulas gives the small-\(c\) quadratic square gap and, writing \(\varepsilon=1-c\),
\[
b_c=\frac23\varepsilon+O(\varepsilon^2),\qquad
 a_c=\sqrt{\frac23}\,\varepsilon^{1/2}+O(\varepsilon^{3/2}),\qquad b_{\square}=\varepsilon+O(\varepsilon^2).
\]
This proves both thin-lens area asymptotics. The exact area of the unit-radius lens is \(2\arccos c-2c\sqrt{1-c^2}\), with asymptotic \((8\sqrt2/3)\varepsilon^{3/2}\), giving the claimed limiting packing fraction. Every conclusion for general \(R\) follows by scaling.

## Verification
The standalone file `verify_lens.py` checks the exact quadratic root and containment equalities, the aspect-ratio inverse formula, strict improvement over squares, the predicted asymptotic coefficients, and the global area inequality against rotated/translated rectangle parameterizations via deterministic numerical grids and independently scaled feasible candidates. Run with `python3 verify_lens.py`. Numerical tests support but do not replace the all-parameter proof above. All analytic claims are deduced from the exact containment characterization.

## Relationship to prior work
Behroozi, *Largest Inscribed Rectangles in Geometric Convex Sets*, arXiv:1905.13246 (initially public 2019-05-30), studies the unrestricted maximum-area inscribed rectangle problem and gives centering/symmetry properties and general optimization algorithms for convex sets, including intersections of quadratic constraints. Its full accessible HTML text (Sections 3, 4, and 6) does not give the complete exact all-separation lens optimizer, its inverse aspect parameter, or thin-lens nonsquare/square divergence. The centering principle and the circle case are prior context, not claimed as novel.

Basit and Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026 (initially public 2023-07-08), studies extremal area/perimeter problems for intersections of translated disks; its full accessible HTML considers disk-polygons and unrestricted convex polygonal approximants, not Euclidean rectangles inside a two-disk lens. Related indexed results concern mean width of lenses, extremal rectangles inside **polygons**, and intersections of several disks. None of the inspected statements implies the explicit Euclidean-lens rectangle classification. Historical solutions in recreational or optimization literature may nevertheless exist.

## Limitations
The result concerns congruent circular disks and Euclidean rectangles in the plane. It does not classify extremal rectangles of intersections of unequal disks, intersections of three or more disks, or other centrally symmetric convex regions. Numerical evaluation is not used to certify historical novelty. No claim of independent verification or exhaustive priority search is made.

## References
- Mehdi Behroozi, *Largest Inscribed Rectangles in Geometric Convex Sets*, arXiv:1905.13246, initially submitted 2019-05-30, https://arxiv.org/abs/1905.13246 .
- Bushra Basit and Zsolt Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026, initially submitted 2023-07-08, https://arxiv.org/abs/2307.04026 .
