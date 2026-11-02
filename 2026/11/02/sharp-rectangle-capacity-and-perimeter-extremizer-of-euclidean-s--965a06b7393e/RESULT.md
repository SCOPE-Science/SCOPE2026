# Sharp rectangle capacity and perimeter extremizer of Euclidean stadiums

## Finding
For real parameters \(a>0\) and \(r>0\), let the Euclidean stadium be
\[
 S_{a,r}=([-a,a]\times\{0\})+\{z\in\mathbb R^2:\|z\|_2\le r\}.
\]
Let \(M(a,r)\) be the maximum area of a Euclidean rectangle of arbitrary orientation and location contained in \(S_{a,r}\). Set
\[
 s=a/r,\qquad t=t(s)=\frac{\sqrt{s^2+8}-s}{4}.
\]
Then \(0<t<1/\sqrt2\), and
\[
 \boxed{M(a,r)=4r^2(s+t)\sqrt{1-t^2}.}
\]
Exactly one rectangle achieves this area: the rectangle centered at the origin, with sides parallel and perpendicular to the stadium's central segment and half-side lengths \(r(s+t)\) and \(r\sqrt{1-t^2}\).

Its perimeter is \(P(a,r)=4a+2\pi r\), and the sharp perimeter-normalized theorem over all noncircular stadiums is
\[
 \boxed{\frac{M(a,r)}{P(a,r)^2}\le\frac{1}{8\sqrt{\pi^2-4}}.}
\]
Equality holds if and only if \(a/r=\pi/2-4/\pi\), up to Euclidean similarity. In particular, the circular limit \(a=0\) does not maximize this ratio: its value is \(1/(2\pi^2)\), strictly smaller than the sharp stadium constant.

The fraction of the stadium's total area occupied by its largest inscribed rectangle,
\[
 \eta(s)=\frac{M(a,r)}{4ar+\pi r^2},
\]
is strictly increasing for \(s>0\), and maps \((0,\infty)\) bijectively onto \((2/\pi,1)\). Thus the area fraction determines the stadium's aspect ratio \(a/r\), and, together with its perimeter (or total area), determines both geometric parameters.

## Assumptions and scope
All areas and lengths are Euclidean. An inscribed rectangle is a closed nondegenerate Euclidean rectangle, with no orientation restriction and with all four vertices in the stadium. The stadium is the Minkowski sum of a radius-\(r\) disk and a central segment of length \(2a\). We assume \(a>0\) when stating uniqueness; at \(a=0\), every centered inscribed square of side \(\sqrt2r\) is optimal. There are no sampling hypotheses or asymptotic approximations.

## Proof
**1. Reduction to the symmetry center.** The stadium is convex and centrally symmetric. If a rectangle \(Q\subset S_{a,r}\) has center \(c\), its reflection \(-Q\) is also contained in the stadium. The midpoint Minkowski average \((Q+(-Q))/2=Q-c\) is a congruent rectangle centered at the origin and contained in \(S_{a,r}\). Hence a maximum-area rectangle can be sought among centered rectangles. This observation is also covered by the general symmetry principle in [1, Theorem 7]; its use here is not claimed as novel.

**2. Full elimination of rotated rectangles.** A centered rectangle has vertices \(\pm p,\pm q\) with \(\|p\|=\|q\|=\rho>0\). Conversely, any such pair determines a centered rectangle, since its side vectors \(p+q\) and \(p-q\) are orthogonal. The rectangle's area is \(2|\det(p,q)|\). If \(\rho\le r\), this area is at most \(2r^2\).

For \(r<\rho\le a+r\), the intersection of the circle of radius \(\rho\) with the stadium consists of the two angular arcs \([-\theta(\rho),\theta(\rho)]\) and \([\pi-\theta(\rho),\pi+\theta(\rho)]\), with \(0\le\theta(\rho)<\pi/2\). The boundary angle is given exactly by
\[
\theta(\rho)=
\begin{cases}
\arcsin(r/\rho),&r<\rho\le\sqrt{a^2+r^2},\\
\arccos\!\left(\dfrac{\rho^2+a^2-r^2}{2a\rho}\right),
&\sqrt{a^2+r^2}\le\rho\le a+r.
\end{cases}
\]
Both branches are strictly decreasing on their interiors, and they agree at the junction. There is consequently a unique \(\rho_0\in(r,a+r)\) for which \(\theta(\rho_0)=\pi/4\).

When \(\theta(\rho)\ge\pi/4\), the rectangle area is at most \(2\rho^2\le2\rho_0^2\). That upper bound is attained by a centered axis-parallel square at \(\rho_0\), with corners \((\pm\rho_0/\sqrt2,\pm\rho_0/\sqrt2)\). When \(\theta(\rho)<\pi/4\), the greatest possible absolute sine of the angular separation between \(p\) and \(q\) is \(\sin(2\theta(\rho))\). The unique maximizing rectangle at that radius (as an unoriented set) has corners \((\pm x,\pm y)\) where \(x=\rho\cos\theta(\rho)>y=\rho\sin\theta(\rho)\). Thus **every possible optimal value is no larger than that of some centered axis-parallel rectangle**. This comparison includes every unconstrained orientation and the entire small-radius regime.

**3. Exact unique axis-parallel optimizer.** For a centered axis-parallel rectangle with positive half-sides \(x,y\), containment is equivalent to
\[
 y^2+\bigl(\max\{x-a,0\}\bigr)^2\le r^2.
\]
For \(0\le x\le a\), the maximal area \(4xy\) is \(4xr\) and increases with \(x\). For \(a\le x\le a+r\), writing \(x=a+u\), the area is bounded by
\[
 f(u)=4(a+u)\sqrt{r^2-u^2},\qquad 0\le u\le r.
\]
Its derivative has the sign of \(r^2-au-2u^2\), a strictly decreasing function with a unique zero \(u_*=rt\), where \(t=(\sqrt{s^2+8}-s)/4\). Hence \(u_*\) is the unique global axis-parallel maximizer. Its half-sides are \(x_*=a+rt\) and \(y_*=r\sqrt{1-t^2}\), and the displayed formula for \(M\) follows.

Since the critical equation implies \(y_*^2=u_*(a+u_*)\), we have \(x_*>y_*\) strictly when \(a>0\). Thus this maximizer lies in the strict \(\theta<\pi/4\) arc regime, and its area exceeds the possible square-regime maximum. The angular comparison in Step 2 then proves that it is the **unique centered maximizing rectangle**.

Finally, if an off-center maximizing rectangle existed, its centered translate would be the rectangle just constructed. Each corner \((\pm x_*,\pm y_*)\) lies on a strictly curved circular end cap. Such a point cannot be the midpoint of two distinct points of the stadium. But the corresponding centered corner is the midpoint of its original and reflected corners, so the translation must have been zero. This establishes global uniqueness, not merely existence of a centered optimizer.

**4. Sharp perimeter optimization.** From the critical equation \(st+2t^2=1\), we obtain \(s=1/t-2t\), with \(t\) decreasing bijectively from \(1/\sqrt2\) to \(0\) as \(s\) increases from \(0\) to infinity. Substitution gives
\[
 J(t)=\frac{M(a,r)}{P(a,r)^2}
 =\frac{t(1-t^2)^{3/2}}{(2-4t^2+\pi t)^2}.
\]
Direct exact differentiation yields
\[
 J'(t)=\frac{\sqrt{1-t^2}(2t^2+1)(\pi t-2)}{(4t^2-\pi t-2)^3}.
\]
The denominator is negative on \(0<t\le1/\sqrt2\). Hence \(J'(t)>0\) below \(t=2/\pi\) and \(J'(t)<0\) above it. The unique global maximum is attained at \(t=2/\pi\), corresponding to \(s=\pi/2-4/\pi>0\). Substitution gives \(J=1/(8\sqrt{\pi^2-4})\), with the stated equality case.

**5. Strict monotonicity of the filling fraction.** The stadium area is \(4ar+\pi r^2\). Substitution as above yields
\[
 \eta(t)=\frac{4(1-t^2)^{3/2}}{4-8t^2+\pi t},\qquad
 \eta'(t)=\frac{4\sqrt{1-t^2}(4t-\pi)(2t^2+1)}{(4-8t^2+\pi t)^2}<0.
\]
The last inequality holds because \(t\le1/\sqrt2<\pi/4\). Since \(t\) decreases with \(s\), \(\eta\) increases strictly with \(s\). Evaluating at \(t=1/\sqrt2\) and taking \(t\downarrow0\) gives the sharp endpoint values \(2/\pi\) and \(1\). This completes both the inverse assertion and the theorem.

## Verification
The companion `checker.py` uses SymPy to verify symbolically both derivative identities, the sharp constant, the disk endpoint, and the critical equation. Independently of the angular-arc reduction, it samples centered rotated rectangles in six stadiums (4,500 directions/aspect ratios each), rescales trial rectangles to the exact stadium boundary using a radial bisection, compares their feasible areas with the theorem, and checks the proposed maximizing witness directly. It reports `ALL_CHECKS_PASSED` when run with the version of SymPy described by `requirements.txt`. These finite numerical checks are not a substitute for the preceding proof; the area bound for *every* rectangle comes from Steps 1–3.

## Relationship to prior work
Behroozi [1] proves a general centering property for optimal rectangles in centrally symmetric convex sets (Theorem 7), analyzes symmetry-related necessary conditions, and presents algorithms for arbitrary convex sets. The centering reduction in Step 1 is therefore established literature. The new content is the unrestricted orientation rigidity **for the entire noncircular stadium family**, the exact area profile, the sharp perimeter-normalized maximizer (which is not the disk), and the invertible rectangular filling fraction.

Choi, Lee and Ahn [2] present exact algorithms for maximum-area rectangles in polygons. Their polygonal results do not directly express the analytic stadium profile or the sharp constant, and the circular end caps mean that their finite polygon formulation does not itself give the stated exact formulas. Cabello and colleagues [3] provide another earlier exact polygon algorithm. A general optimization algorithm or a known centeredness theorem is not claimed as a new discovery; an earlier specialized stadium calculation could still affect historical priority.

## Limitations
Only Euclidean stadiums, not general rounded rectangles or arbitrary centrally symmetric convex bodies, are classified. Equality and uniqueness are understood for strictly positive central segment length \(2a\); the disk endpoint has a family of rotated optimal squares. Geometric measurements are assumed exact. The theorem contains no noise-stability or algorithmic-complexity guarantee for empirical shape recovery. The literature comparison supports provisional historical originality, not an exhaustive priority certificate.

## References
[1] Mehdi Behroozi, *Largest Inscribed Rectangles in Geometric Convex Sets*, initial public preprint 2019-05-30, arXiv:1905.13246 (preprint version examined: v3).

[2] Yujin Choi, Seungjun Lee and Hee-Kap Ahn, *Maximum-area and maximum-perimeter rectangles in polygons*, Computational Geometry 94 (2021), 101710, DOI:10.1016/j.comgeo.2020.101710.

[3] Sergio Cabello, Otfried Cheong, Christian Knauer and Lena Schlipf, *Finding Largest Rectangles in Convex Polygons*, initial public preprint 2014, arXiv:1405.1223.
