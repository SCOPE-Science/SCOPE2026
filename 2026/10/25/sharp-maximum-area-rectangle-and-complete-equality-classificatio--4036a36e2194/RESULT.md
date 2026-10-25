# Sharp maximum-area rectangle and complete equality classification for the regular pentagon

## Finding
Let \(P\) be any regular Euclidean pentagon with circumradius \(R>0\). Among **all** closed Euclidean rectangles contained in \(P\), with unrestricted position, orientation, and aspect ratio, the maximum area is
\[
\boxed{M(P)=\frac{5R^2}{4\cos(\pi/5)\cos(\pi/10)}
=R^2(5-\sqrt5)\sin(\pi/5).}
\]
There are exactly five maximizing rectangles. Each has one entire side coincident with one side of \(P\), and its other two corners lie on the two nonadjacent sides of \(P\). The five maximizers are obtained by pentagonal rotations. For circumradius one, their side lengths are \(2\sin(\pi/5)\) and \((5-\sqrt5)/2\).

## Assumptions and scope
The pentagon is closed, nondegenerate, convex, and regular; the rectangle may be any Euclidean rectangle, not necessarily centered in the pentagon, with vertices allowed on its boundary. Degenerate rectangles have zero area and are not maximizing. The geometric area is ordinary two-dimensional Lebesgue area. Homothety reduces the proof to \(R=1\).

For the normalized pentagon write \(\varphi=(1+\sqrt5)/2\), \(r=\cos(\pi/5)\), and
\[
 n_j=\bigl(\cos(\pi/2+2\pi j/5),\sin(\pi/2+2\pi j/5)\bigr),
 \qquad P=\{x\in\mathbb R^2:n_j\cdot x\le r,\ j=0,1,2,3,4\}.
\]
This is a unit-circumradius regular pentagon: its five edge-supporting lines have unit normals \(n_j\) and common inradius \(r\).

## Proof
**1. Unrestricted rectangles reduce to one angular interval.** Write any nondegenerate inscribed rectangle as
\[
 Q=\{c+s a u+t b v:-1\le s,t\le1\},\quad
 u=(\cos\theta,\sin\theta),\quad v=(-\sin\theta,\cos\theta),\quad a,b>0.
\]
Rotating the regular pentagon by multiples of \(2\pi/5\) and interchanging the two rectangle axes (which changes \(\theta\) by \(\pi/2\)) permits \(0\le\theta\le\pi/10\): the corresponding unoriented axes have period \(\pi/10\), since \(2\pi/5-\pi/2=-\pi/10\). Put \(t=\theta-\pi/20\), so \(|t|\le\pi/20\).

Containment is equivalent, for all five side normals, to
\[
 n_j\cdot c+a|n_j\cdot u|+b|n_j\cdot v|\le r.
\tag{1}
\]
The elementary exact vector relations
\[
 n_0+n_1+\varphi n_3=0,\qquad \varphi n_1+n_3+n_4=0
\tag{2}
\]
follow from the fivefold angular differences (or from \(\varphi^2=\varphi+1\)). All coefficients in (2) are positive. Weighting and adding (1) for the first triple and then the second eliminates the center \(c\). Evaluating the absolute scalar products, with their fixed signs on \(0\le\theta\le\pi/10\), gives the two independently necessary inequalities
\[
 2a\cos(t+3\pi/20)+2\varphi b\cos(t-3\pi/20)
 \le (2+\varphi)r,
\tag{3}
\]
\[
 2\varphi a\cos(t+3\pi/20)+2b\cos(t-3\pi/20)
 \le (2+\varphi)r.
\tag{4}
\]
For clarity, the supporting indices used are \((0,1,3)\) and \((1,3,4)\); equation (3) comes from weights \((1,1,\varphi)\), while (4) uses \((\varphi,1,1)\). The trigonometric reductions in (3)–(4) hold at both angular endpoints by continuity.

**2. Universal sharp area bound.** Add (3) and (4), and use \((2+\varphi)\cos(\pi/5)/(1+\varphi)=\sqrt5/2\), to obtain
\[
 a\cos(t+3\pi/20)+b\cos(t-3\pi/20)\le\sqrt5/2.
\tag{5}
\]
Both cosine factors are strictly positive on the stated interval. Arithmetic–geometric mean applied to (5) yields
\[
 \operatorname{area}(Q)=4ab\le
 \frac{5}{4\cos(t+3\pi/20)\cos(t-3\pi/20)}.
\tag{6}
\]
The denominator equals \(\cos^2(3\pi/20)-\sin^2 t\), which is at least
\(\cos(\pi/5)\cos(\pi/10)\), with equality if and only if \(|t|=\pi/20\). Therefore
\[
 \operatorname{area}(Q)\le \frac{5}{4\cos(\pi/5)\cos(\pi/10)}.
\tag{7}
\]
No alignment, centering, or boundary-contact assumption was imposed: (7) holds for every orientation and every contained rectangle.

**3. Attainment.** Set
\[
 a=\sin(\pi/5),\quad b=(5-\sqrt5)/4,\quad
 c=\bigl(0,\cos(\pi/5)-b\bigr),\quad \theta=0.
\tag{8}
\]
Direct substitution in (1) gives equality for all five support normals. Thus this rectangle is contained in \(P\); its upper edge is the entire horizontal pentagon edge and its lower corners are on the two nonadjacent pentagon edges. Its area is
\(4ab=(5-\sqrt5)\sin(\pi/5)=5/[4\cos(\pi/5)\cos(\pi/10)]\). The upper bound is sharp.

**4. Uniqueness of equality.** Equality in (7) requires \(|t|=\pi/20\); the two angular endpoints represent the same class under the permitted pentagonal rotation and axis interchange. For \(\theta=0\), equality in arithmetic–geometric mean and in (5) fixes the two positive side half-lengths uniquely, giving (8). Since (3) and (4) are positive weighted sums of valid supporting inequalities, their equalities force the four supporting inequalities with indices \(0,1,3,4\) individually to be equalities. The index-\(0\) equation fixes \(c_y=r-b\), and the index-\(1\) and index-\(4\) equations force \(c_x=0\). Hence (8) is the unique optimizer of that orientation. The five pentagonal rotations give five distinct rectangles and exhaust every equality case.

Scaling by \(R\) multiplies their areas by \(R^2\), completing the proof.

## Verification
The standalone program `checks/pentagon_rectangle_check.py` was executed successfully. Its symbolic part checks exactly the two positive vector dependencies, the sine/cosine coefficient identities in (3)–(4), the golden-ratio simplification in (5), the equality of the two closed area formulas, and all five supporting constraints of the constructed rectangle. It also performs 19 numerical constrained optimizations across the fundamental angular interval. The analytic inequalities (3)–(7), not finite sampling, establish the universal result. The script requires the scientific Python packages declared in `requirements.txt`.

## Relationship to prior work
Cabello, Cheong, Knauer and Schlipf (first arXiv posting 2014-05-06, arXiv:1405.1223), Section 3, give a general exact algorithm for finding maximum-area rectangles in arbitrary convex polygons; they do not state this pentagonal constant or its five equality cases. Knauer et al. (2012) supply earlier approximation methods for general convex polygons, not a stated special-pentagon classification. A 2017 Math Stack Exchange discussion specifically describes the correct side-aligned pentagonal configuration and its numerical area, but expressly assumes that an optimal rectangle has this orientation; its attempted arguments therefore do not establish the unrestricted global bound. The present contribution is the unconditional orientation-free inequality (5), the sharp formula (7), and the exhaustive equality classification, **not** the prior side-aligned candidate construction.

A separately indexed 2026 finding gives maximum-area rectangles in regular **even** polygons, which does not imply the odd pentagonal statement. An exact general algorithm is not the same statement as an evaluated constant and rigidity theorem; nevertheless it can in principle algorithmically compute this five-vertex special case and is important prior methodological coverage.

## Limitations
This theorem concerns only regular pentagons (and their similar copies), not arbitrary convex pentagons or regular odd polygons in general. It concerns maximum **area**, not maximum perimeter or maximum-area parallelograms. The 2017 discussion anticipates the maximizing shape conditionally, so novelty is confined to the complete global proof and uniqueness, not the numerical guess. Full bibliographic exclusion of other independent proofs is not guaranteed; the 2012 approximation article was compared through its accessible abstract, not a full reading. No independent audit has been performed.

## References
1. S. Cabello, O. Cheong, C. Knauer, L. Schlipf, *Finding Largest Rectangles in Convex Polygons*, arXiv:1405.1223, initial posting 2014-05-06, especially Section 3, https://arxiv.org/abs/1405.1223.
2. C. Knauer, L. Schlipf, J. M. Schmidt, H. R. Tiwary, *Largest inscribed rectangles in convex polygons*, Journal of Discrete Algorithms 13 (2012), 78–85, DOI 10.1016/j.jda.2012.01.002.
3. *How to find the maximum area of a rectangle within a pentagon*, Mathematics Stack Exchange, question posted 2017-03-01, answers 2017-03-02 and 2017-03-06, https://math.stackexchange.com/questions/2166282/how-to-find-the-maximum-area-of-a-rectangle-within-a-pentagon.
