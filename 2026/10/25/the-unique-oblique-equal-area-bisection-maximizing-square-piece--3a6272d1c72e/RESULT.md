# The unique oblique equal-area bisection maximizing square-piece roundness

## Finding
Let \(Q=[-1,1]^2\). In a partition \(Q=K_1\cup K_2\) into **exactly two compact convex sets** with disjoint interiors and equal positive areas, let \(r(K)\) be the radius of the largest Euclidean disk contained in \(K\), and \(R(K)\) the radius of the smallest Euclidean disk containing \(K\). Define the minimum fatness of the partition by
\[
\mathcal F(K_1,K_2)=\min_{j=1,2}\frac{r(K_j)}{R(K_j)}.
\]
There is a unique parameter \(t_*\in(0,1)\) satisfying
\[
4(1-t_*)=(t_*+\sqrt{1+t_*^2})(1+t_*)^3.
\]
The exact optimum is
\[
\boxed{\max\mathcal F(K_1,K_2)=
\frac{2(1+t_*)}{(1+t_*+\sqrt{1+t_*^2})\sqrt{4+(1+t_*)^2}}}
=0.465023362935585\ldots .
\]
Equality holds exactly for bisections by lines through the square's center which, after a symmetry of the square, have equation \(y=t_*x\). Thus the optimal two pieces are congruent, nonsymmetric trapezoids, and the optimal cut is neither parallel to a side nor along a diagonal. The optimal individual circumradius-to-inradius aspect ratio is \(2.150429590649446\ldots\).

Equivalently, \(t_*\) is the only zero in \((0,1)\) of the algebraic polynomial
\[
t^6-2t^5-t^4+20t^3+15t^2+46t-15,
\]
subject to the displayed unsquared equation, which fixes the intended real branch. Its numerical value is \(t_*=0.288678389721968\ldots\).

## Assumptions and scope
All geometry uses the ordinary Euclidean norm; the circles defining \(r\) and \(R\) may have different centers. A two-piece partition means closed, full-dimensional convex pieces with union \(Q\) and disjoint interiors. The interface is not assumed initially to be a straight segment. Exactly equal area is imposed; no equality of perimeter or any restriction on the cut direction is assumed. Scaling or translating the square does not change \(\mathcal F\).

## Proof
**1. Every admissible partition is a line cut through the center.** The two open convex interiors are disjoint. The separating-hyperplane theorem provides a line \(L\) with their interiors in opposite open half-planes, allowing closures in opposite closed half-planes. Since the two closed pieces cover \(Q\), each must equal the corresponding intersection of \(Q\) with that closed half-plane: points of \(Q\) strictly on one side cannot belong to the other piece, and boundary points follow by taking closures. Hence an arbitrary two-piece convex partition is a single straight-line cut. For a fixed line direction, the area on one side varies strictly monotonically as the line is translated through the interior of \(Q\). Central symmetry shows that the line through the origin bisects the area. Therefore this is the unique equal-area cut in that direction. The halves are related by central inversion.

**2. Reduction to one parameter.** Reflecting and rotating through symmetries of the square, take the line \(y=tx\) for a unique representative \(0\le t\le1\). The upper piece is
\[
K_t=\{(x,y): -1\le x\le1,\;tx\le y\le1\}
=\operatorname{conv}\{(-1,-t),(-1,1),(1,1),(1,t)\}.
\]
The other piece is \(-K_t\), so both have the same inradius and circumradius and the minimum fatness is simply \(r(K_t)/R(K_t)\).

**3. Exact inradius.** Write \(s=\sqrt{1+t^2}\). A disk of radius \(r\) with center \((a,b)\) lies in \(K_t\) only if
\[
a\ge-1+r,\quad a\le1-r,\quad b\le1-r,\quad b-ta\ge sr.
\]
For \(t\ge0\), the first, third and fourth inequalities imply
\[
1-r\ge t(-1+r)+sr,
\qquad r\le\frac{1+t}{1+t+s}.
\]
Conversely, take this last value of \(r\) and the center \((a,b)=(-1+r,1-r)\). All four inequalities hold; the right-hand inequality is satisfied since \(0<r<1\). Thus
\[
r(K_t)=\frac{1+t}{1+t+\sqrt{1+t^2}}.
\]
For \(t>0\) this incenter is forced by equality in the three bounding constraints.

**4. Exact circumradius.** Set \(A=(-1,-t)\), \(B=(1,1)\), \(C=(-1,1)\), and \(D=(1,t)\). Every enclosing disk must contain \(A\) and \(B\), giving the lower bound \(|A-B|/2\). The disk with diameter \(AB\) contains \(C\) on its boundary, because \((A-C)\cdot(B-C)=0\). It contains \(D\), since \((A-D)\cdot(B-D)=-2t(1-t)\le0\), the closed-diameter-disk criterion. By convexity of the disk, it contains all of \(K_t\). Consequently
\[
R(K_t)=\frac12\sqrt{4+(1+t)^2}.
\]

**5. Unique optimizer.** Combining the preceding formulas,
\[
f(t)=\frac{r(K_t)}{R(K_t)}
=\frac{2(1+t)}{(1+t+\sqrt{1+t^2})\sqrt{4+(1+t)^2}}.
\]
A direct logarithmic differentiation, with \(s=\sqrt{1+t^2}\) and \(u=1+t\), yields
\[
\frac{f'(t)}{f(t)}
=\frac{1-t}{su(u+s)}-\frac{u}{4+u^2}
=\frac{H(t)}{su(u+s)(4+u^2)},
\]
where \(H(t)=4(1-t)-(t+s)(1+t)^3\). Every denominator is positive and \(H\) is strictly decreasing on \([0,1]\): the first term decreases strictly, while \(t+s\) and \((1+t)^3\) both increase strictly and remain positive. Also \(H(0)=3>0\) and \(H(1)=-8(1+\sqrt2)<0\). Hence there is one and only one zero \(t_*\in(0,1)\), \(f\) increases before it and decreases after it, and the stated value and unique equality orientations follow.

Squaring the defining equation after isolating the radical produces the stated degree-six polynomial. The unsquared equation rather than the polynomial alone fixes the root and does not require any extraneous-root classification. This completes the proof.

## Verification
The proof is analytic and uses no finite enumeration in place of an infinite argument. The accompanying `verify.py` independently checks the polynomial identity algebraically using integer-polynomial arithmetic, brackets the unique root by bisection of the original decreasing function, and evaluates the exact formulas at representative directions. The root and displayed constants are decimal approximations of quantities defined exactly above, not premises of the theorem. At \(t=0\), a side-parallel bisection has fatness \(1/\sqrt5=0.447213595\ldots\); at \(t=1\), a diagonal bisection has fatness \(\sqrt2-1=0.414213562\ldots\). Both are strictly below the oblique optimum.

## Relationship to prior work
Pach and Tardos (2026) provide an existence theorem for equal-area, bounded-fatness subdivisions of arbitrary planar convex bodies. Their universal guarantee neither specifies an exact optimal two-piece constant for the square nor an optimal direction; the available abstract does not resolve the present sharper classification. Damian and O'Rourke (2003) formulate circumradius/inradius circularity for polygon partitions and explicitly identify the tradeoff between piece count and optimal circularity as a direction for further investigation. Their square bounds concern partitions with an unrestricted number of pieces, not the precisely two-piece equal-area problem here. Recent published results on the maximum achievable inradius in two-part divisions and the minimum maximum diameter in regular-polygon bisections optimize *different* functionals: one alone does not determine the maximizer of their ratio. In fact, the inradius and circumradius above are both strictly increasing along the admissible direction parameter, yet their quotient is uniquely maximized at an interior oblique angle.

## Limitations
The theorem is restricted to **two** convex equal-area pieces of a square in Euclidean geometry. It makes no claim about unequal-area cuts, more than two pieces, general rectangles or polygons, nonconvex pieces, higher dimensions, or the universal fat-partition constant. The 2026 Pach–Tardos full manuscript was not accessible during the comparison; only its dated abstract was available, so a precise previously unnoticed two-piece example there remains an originality risk.

## References
1. J. Pach and G. Tardos, *Cutting a convex body into fat parts and approximating Euclidean distance by graph distances*, arXiv:2609.20702v1, first public 17 September 2026, https://arxiv.org/abs/2609.20702.
2. M. Damian and J. O'Rourke, *Partitioning Regular Polygons into Circular Pieces I: Convex Partitions*, 2003, arXiv:cs/0304023v1, https://arxiv.org/abs/cs/0304023. In particular, Sections 1.1, 5 and 6 of the expanded version.
3. *Most Circular Partition of a Square*, The Open Problems Project, Problem 59, https://topp.openproblem.net/p59 (background on the unrestricted-number variant).
