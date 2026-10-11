# Exact boundary-circle intersection spectrum of regular polygons

## Finding

Let \(P_n\) be a regular Euclidean \(n\)-gon of circumradius \(R>0\), with integer \(n\ge3\). For \(p\in\partial P_n\), define
\[
H_n(p)=\max_{r>0}\#\bigl(\partial P_n\cap\{q:\|q-p\|=r\}\bigr),
\]
where distinct intersection points, including tangencies, are each counted once. Fix an edge, put its midpoint at \((R\cos\alpha,0)\), its endpoints at \((R\cos\alpha,\pm R\sin\alpha)\), and write \(p=(R\cos\alpha,t)\), where \(\alpha=\pi/n\) and \(|t|\le R\sin\alpha\).

If \(n\ge4\) is even, then
\[
H_n(p)=\begin{cases}2,&p\text{ is a polygon vertex},\\4,&p\text{ is not a vertex}.\end{cases}
\]
If \(n\ge3\) is odd, define the **six-intersection half-window**
\[
\tau_n=\frac{2R\sin\alpha}{\cos\alpha}\bigl(1-\cos(\alpha/2)\bigr)^2.
\]
Then, on every edge,
\[
H_n(p)=\begin{cases}6,&|t|<\tau_n,\\4,&\tau_n\le|t|\le R\sin\alpha.\end{cases}
\]
In particular, equality at the threshold does **not** yield six intersections. The fraction of the entire boundary occupied by centers admitting a six-point circle is exactly
\[
\frac{\mathcal H^1(\{p\in\partial P_n:H_n(p)=6\})}{\operatorname{per}(P_n)}
=\begin{cases}
0,&n\text{ even},\\
\dfrac{2(1-\cos(\pi/(2n)))^2}{\cos(\pi/n)},&n\text{ odd},
\end{cases}
\]
and, along the odd orders, this fraction equals \(\pi^4/(32n^4)+O(n^{-6})\). Thus all regular polygons have worst-center multiplicity at most six, with a sharp parity split and an exact, rapidly shrinking exceptional region.

## Assumptions and scope

The polygon is the closed convex hull of its \(n\) equally spaced circumcircle vertices, and the circle center is constrained to its polygonal boundary. The circle radius is positive and freely chosen. In the proof the circumradius is normalized to one, after which \(c=\cos\alpha\) and \(s=\sin\alpha\). A point on the reference edge is \((c,t)\), with \(-s\le t\le s\). Rotational and reflection symmetry reduce to \(0\le t\le s\). Formulae scale by \(R\) as displayed above. A tangent point and a coincident vertex are each one intersection point, not two.

## Proof

**1. Controlling local maxima.** Along each side, squared distance from \(p\) is a strictly convex quadratic, so every strict local maximum of the boundary distance function occurs at a polygon vertex. For a vertex at polar angle \(\theta\), write \(p=\rho(\cos\phi,\sin\phi)\) and let consecutive vertices be separated by \(2\alpha\). Direct scalar products with the two incident edge vectors show that this vertex is a strict local maximum precisely when
\[
\rho\sin(\theta+\alpha-\phi)<s,
\qquad
\rho\sin(\theta-\alpha-\phi)>-s.
\]
For \(n\ge4\), put \(\lambda=\arcsin(s/\rho)\). Here \(\rho=c/\cos\phi\), \(|\phi|\le\alpha\), and \(s/\rho\le1\). The preceding pair of inequalities is equivalent to
\[
\bigl|\operatorname{wrap}_{[-\pi,\pi]}(\theta-\phi-\pi)\bigr|<\alpha+\lambda.
\]
For even \(n\ge4\), the candidate far vertices have angles \(\pi\pm\alpha\), and the next candidates have angles \(\pi\pm3\alpha\). Since
\[
|\phi|+\arcsin(\tan\alpha\cos\phi)\le2\alpha
\]
(the left side is nondecreasing in \(|\phi|\) on \([0,\alpha]\), by differentiation, and equals \(2\alpha\) at the endpoint), no vertex beyond the two far candidates is a strict maximum. At a vertex center, only its diametrically opposite vertex is a strict maximum. For odd \(n\ge5\), \(\arcsin(\tan\alpha)<2\alpha\), since \(\alpha<\pi/4\). Thus only the central opposite vertex and its two neighbors, at angles \(\pi\) and \(\pi\pm2\alpha\), can be strict maxima. For \(n=3\) there are only three vertices anyway. Accordingly, every level circle has at most four intersections in the even case and at most six in the odd case: a continuous piecewise strictly convex boundary-distance profile with at most \(m\) local maxima meets a horizontal level in at most \(2m\) distinct points. Critical levels obey the same bound by considering regular levels immediately above and below.

**2. Even polygons.** The reference side is \(x=c\) and the opposite side is \(x=-c\), with vertical coordinate in \([-s,s]\). For \(p=(c,t)\), \(|t|<s\), the distance from \(p\) to the opposite edge has a strict interior minimum \(2c\); both endpoints have strictly larger distance. Choosing a radius strictly between \(2c\) and both endpoint distances gives two intersections on the opposite edge. The complementary boundary path contains \(p\) and joins those endpoints, hence has at least two additional intersections. The preceding upper bound proves \(H_n(p)=4\). At a vertex, squared distance is strictly increasing along either of the two boundary chains toward the opposite vertex (equivalently the angular local-maximum criterion yields only that maximum); consequently \(H_n(p)=2\). This includes the square.

**3. Odd polygons: a forced four intersections.** Write
\[
A=(-1,0),\qquad B_\pm=(-\cos2\alpha,\pm\sin2\alpha).
\]
These are three consecutive far-side vertices, also for \(n=3\). Assume \(0\le t\le s\). The orthogonal projection of \(p=(c,t)\) onto segment \(AB_-\) lies strictly inside it: measured from \(A\), its along-edge coordinate is \(s(1+c)-ct\in(0,2s)\). The distance at this interior minimum is
\[
m_-=c(1+c)+st.
\]
Both endpoint distances \(\|p-A\|\) and \(\|p-B_-\|\) strictly exceed \(m_-\). A circle with a radius between \(m_-\) and both endpoint distances intersects \(AB_-\) twice and also intersects the complementary boundary path, which contains \(p\), at least twice. Hence \(H_n(p)\ge4\) at every boundary point.

**4. Exact six-intersection threshold.** The second opposite edge \(AB_+\) has supporting-line distance \(m_+=c(1+c)-st\le m_-\). Among the three potentially maximal vertices, \(B_+\) is the weakest: \(\|p-B_-\|^2-\|p-B_+\|^2=4t\sin2\alpha\ge0\), while \(\|p-A\|^2-\|p-B_+\|^2=4cs(s+t)>0\). A six-intersection circle would require a radius both greater than the lower edge's minimum \(m_-\) and smaller than \(\|p-B_+\|\); this remains a necessary condition even if \(B_+\) ceases to be a strict maximum.

The exact squared gap factorizes:
\[
\begin{aligned}
F(t)&=\|p-B_+\|^2-m_-^2\\
&=c^2t^2-2cs(c+3)t+(1-c)^3(1+c)\\
&=c^2(t-t_-)(t-t_+),
\end{aligned}
\]
where
\[
t_\pm=\frac{s}{c}\bigl(c+3\pm4\cos(\alpha/2)\bigr).
\]
The smaller root is exactly
\[
t_-=\frac{2s}{c}(1-\cos(\alpha/2))^2=\tau_n/R,
\]
while \(t_+>s\); moreover \(0<t_-<s(1-c)/c<s\). Thus on \([0,s]\), \(F(t)>0\) exactly when \(t<t_-\). When \(t<t_-\), both perpendicular feet on \(AB_+\) and \(AB_-\) lie strictly inside their edges: the respective along-edge coordinates from \(A\) are \(s(1+c)+ct<2s\) and \(s(1+c)-ct>0\). Choose
\[
m_-<r<\|p-B_+\|.
\]
Then the circle cuts both \(AB_+\) and \(AB_-\) twice, and the complementary path through \(p\) twice. These are six distinct crossings. If \(t\ge t_-\), the necessary inequality \(m_-<\|p-B_+\|\) fails; six crossings are impossible and Step 3 gives exactly four as the maximum. Reflection handles negative \(t\), and Step 1 excludes larger multiplicity. The degeneracy \(t=t_-\) does not create six coincident-but-distinct points: at the critical radius an outer vertex contact and an opposite-edge tangency are each counted once, and the maximum is four.

**5. Boundary proportion.** For odd \(n\), the six-center set consists of the open interval of length \(2\tau_n\) about each edge midpoint, while each full edge has length \(2R\sin\alpha\). Dividing lengths gives the formula. The expansion \(1-\cos(\alpha/2)=\alpha^2/8+O(\alpha^4)\) gives the quartic asymptotic.

## Verification

The accompanying `verify.py` uses symbolic trigonometric reduction and 75-decimal-place direct circle–segment intersection calculations. It compares the predicted maximal number of circle intersections against all nonsingular radius chambers determined by polygon vertex distances and interior edge-perpendicular-foot distances. The test includes every order from three to 21, additional orders 25, 33, 51 and 101, and points on both sides of the exact six-intersection threshold, as well as even-polygon vertices and interiors. The script prints `VERIFY_OK`. Direct finite checking is supplementary: the preceding analytic argument covers every integer order and every boundary point.

## Relationship to prior work

Bárány and Roldán-Pensado [1] formulate Erdős's boundary-centered circle-intersection invariant \(N(K)=\min_{p\in\partial K}H_K(p)\) and explicitly introduce the sets \(J(K,m)=\{p:H_K(p)\ge m\}\), as well as their perimeter fractions. They note the regular odd-polygon obstruction \(N(P_n)\ge4\); their main existence, finiteness and Baire-category conclusions do not specify \(J(P_n,6)\) or this all-center extremal profile. The distinct best-center assertion \(N(P_n)=4\) for odd regular polygons follows by combining Steps 1 and 3 but does not imply the worst-center or perimeter-fraction formula. A separate published polygon-complexity bound for the best-center invariant is likewise not a bound on this pointwise spectrum. The contribution here is the complete local phase classification and the exact \(n^{-4}\) density of six-intersection centers, not a new general bound for arbitrary convex curves.

## Limitations

The theorem concerns regular Euclidean polygons and centers constrained to their boundaries; it neither resolves a uniform upper bound for arbitrary convex bodies nor classifies nonregular polygons. The first public-source date is taken from the dated, publicly available journal version [1] rather than its editorial receipt or revision dates. The literature comparison includes potentially incomplete indexing of older constructions; an equivalent unindexed special-family observation cannot be excluded. All claims are mathematical, not independently certified. The finite verifier does not substitute for the proof.

## References

[1] I. Bárány and E. Roldán-Pensado, “A Question from a Famous Paper of Erdős,” *Discrete & Computational Geometry* 50 (2013), 253–261, DOI: 10.1007/s00454-013-9507-z; publicly dated 2013-05-08. Full online article, especially Introduction, Sections 2 and 3.

[2] P. Erdős, “On sets of distances of n points,” *American Mathematical Monthly* 53 (1946), 248–250 (historical formulation cited by [1]).
