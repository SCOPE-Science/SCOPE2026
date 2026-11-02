# Two sharp aspect ratios for the area-normalized metric radius of flat Klein bottles

## Finding
Let \(K_{a,b}\) be the flat Klein bottle defined below, let \(d\) be intrinsic geodesic distance, and write its **metric radius** (not its injectivity radius) as
\[
R(K_{a,b})=\min_{p\in K_{a,b}}\max_{q\in K_{a,b}}d(p,q).
\]
For all \(a,b>0\), the exact radius and diameter are
\[
\boxed{R(K_{a,b})=\begin{cases}
 a^2/b+b/4,&0<a\le b/2,\\[2pt]
 a/2+b^2/(8a),&a\ge b/2,
\end{cases}}
\qquad
\boxed{\operatorname{diam}(K_{a,b})=\tfrac12\sqrt{a^2+b^2}}.
\]
The minimizing points are exactly the closed curve represented by vertical coordinates \(v=b/4\) and \(v=3b/4\); the maximum-eccentricity points are exactly the two closed glide-axis curves represented by \(v=0\) and \(v=b/2\).

With area \(A=ab\), the **sharp normalized inequality** is
\[
\boxed{\frac{R(K_{a,b})^2}{A}\ge\frac{2}{3\sqrt3}},
\qquad\text{equivalently}\qquad
\boxed{A\le\frac{3\sqrt3}{2}R(K_{a,b})^2}.
\]
Equality occurs for **exactly two** inequivalent similarity classes, with ratios
\[
\boxed{a/b=\frac{1}{2\sqrt3}\quad\text{or}\quad a/b=\frac{\sqrt3}{2}}.
\]
These two flat metrics are not isometric after area normalization. In particular, the flat Klein-bottle area-to-metric-radius optimum has two distinct shapes, unlike the unique flat shape optimizing the systolic area.

More precisely, define the circular distance \(\delta(v)=\operatorname{dist}(2v,b\mathbb Z)\in[0,b/2]\), put \(B=b-\delta(v)\), and let \(t=\min\{\delta(v),a^2/B\}\). The entire pointwise geodesic eccentricity profile is
\[
\boxed{\max_q d((0,v),q)^2=\frac{a^2+B^2}{4}+\frac{1+B^2/a^2}{4}t^2}.
\]
It decreases strictly as \(\delta(v)\) increases from zero to \(b/2\). Its optimizing farthest-point mechanism changes when \(a^2=\delta(v)(b-\delta(v))\); this is a genuine interior transition precisely when \(a<b/2\).

## Assumptions and scope
For \(a,b>0\), equip \(\mathbb R^2\) with its standard Euclidean metric and take the compact quotient
\[
K_{a,b}=\mathbb R^2/\langle g,h\rangle,
\quad g(x,y)=(x+a,-y),\quad h(x,y)=(x,y+b).
\]
The group acts freely and properly discontinuously. A fundamental rectangle has width \(a\), height \(b\), and area \(ab\). We use intrinsic quotient geodesic distance and optimize over every point of the quotient. The parameter \(a/b\) ranges over all positive values; no aspect-ratio restriction is imposed. Horizontal translations are isometries, so pointwise eccentricity only depends on a representative's vertical coordinate. The term *metric radius* means the minimax farthest-point distance, and is distinct from maximum injectivity radius, the length of a shortest nontrivial closed geodesic, or a lattice covering radius.

## Proof
**1. Reduction to two deck parities.** Fix the first point as \(P=(0,v)\), using horizontal translation invariance, and let the second point range over \(Q=(u,y)\) with \(0\le u\le a\), \(y\pmod b\). The even powers of \(g\), combined with vertical translations, give horizontal nearest displacement \(u\) and vertical nearest displacement \(r=\operatorname{dist}(y-v,b\mathbb Z)\). Odd powers give horizontal nearest displacement \(a-u\) and vertical nearest displacement \(w=\operatorname{dist}(y+v,b\mathbb Z)\). Therefore, exactly (with no omitted deck images),
\[
d(P,Q)^2=\min\{u^2+r^2,(a-u)^2+w^2\},
\qquad 0\le r,w\le b/2.
\]
Here every pair \((u,y)\) in the stated rectangle represents a possible quotient point, so both variables may indeed be optimized independently.

**2. The circular-distance frontier.** The two centers \(v\) and \(-v\) on the circle of circumference \(b\) are separated by \(\delta=\operatorname{dist}(2v,b\mathbb Z)\in[0,b/2]\). As \(y\) runs around that circle, the attainable distance pairs \((r,w)\) consist of four straight segments: their maximal, coordinatewise nondominated edge is
\[
r+w=B=b-\delta,\qquad r-w=\eta,\qquad -\delta\le\eta\le\delta.
\]
For completeness, all attainable pairs satisfy \(r,w\le b/2\), \(r+w\le B\) and \(|r-w|\le\delta\). Hence any pair is coordinatewise dominated by some point of the displayed edge: take
\[
r'\in[\max\{r,b/2-\delta\},\min\{B-w,b/2\}],\qquad w'=B-r'.
\]
This interval is nonempty by the three preceding inequalities. The squared-distance minimum in Step 1 is increasing in each of \(r,w\), so it is sufficient to optimize along the displayed edge.

**3. Horizontal minimax and the exact eccentricity.** For fixed \(r,w\), the first quadratic in Step 1 is increasing in \(u\), while the second is decreasing. Their intersection is at
\[
u_*=\frac{a^2+w^2-r^2}{2a}=\frac{a^2-B\eta}{2a}.
\]
If \(|\eta|\le a^2/B\), this is in \([0,a]\), and maximizing the lower of the two quadratics gives
\[
\max_{0\le u\le a}d(P,Q)^2
=\frac{a^2+B^2}{4}+\frac{1+B^2/a^2}{4}\eta^2.
\]
If \(|\eta|\ge a^2/B\), the maximizing \(u\) is an endpoint and the value is \(a^2+(B-|\eta|)^2/4\). The first expression is strictly increasing with \(|\eta|\) until \(a^2/B\); the second is strictly decreasing thereafter. With \(|\eta|\le\delta\), the maximum therefore occurs at \(|\eta|=t=\min\{\delta,a^2/B\}\). This proves the complete eccentricity profile in the Finding. All maxima are attained because the quotient is compact.

**4. Strict spatial ordering and the metric radius.** On the branch \(a^2\ge\delta B\), differentiating the squared eccentricity with respect to \(\delta\) gives
\[
-\frac{(b-2\delta)(a^2-\delta B)}{2a^2}\le0.
\]
On the branch \(a^2\le\delta B\), the squared eccentricity simplifies to \((a^2+B^2)^2/(4B^2)\), whose derivative is
\[
\frac{a^4-B^4}{2B^3}\le0,
\]
since \(a^2\le\delta B\le B^2\). In every open interval within \(0<\delta<b/2\), the decrease is strict, and continuity handles switching points. Thus the maximum eccentricity is at \(\delta=0\) and the minimum at \(\delta=b/2\), and there are no other minimizing or maximizing vertical levels. The quotient identification \(v\sim-v\) joins the two representatives \(b/4\) and \(3b/4\) into one closed center curve. The two levels \(0,b/2\) remain separate glide-axis curves.

Substitution of \(\delta=0\) gives \(\operatorname{diam}(K_{a,b})^2=(a^2+b^2)/4\). Substitution of \(\delta=b/2\), \(B=b/2\), yields the two radius branches, because \(t=\min\{b/2,2a^2/b\}\). Their common value at \(a=b/2\) is \(b/2\).

**5. Optimal area normalization and two equality shapes.** Write \(s=a/b>0\). Squaring the radius and dividing by \(ab\) yields the exact dimensionless profile
\[
F(s)=\frac{R(K_{a,b})^2}{ab}=\begin{cases}
(4s^2+1)^2/(16s),&0<s\le1/2,\\
(4s^2+1)^2/(64s^3),&s\ge1/2.
\end{cases}
\]
The one-sided derivatives are respectively
\[
F'(s)=\frac{(4s^2+1)(12s^2-1)}{16s^2},\qquad
F'(s)=\frac{(4s^2+1)(4s^2-3)}{64s^4}.
\]
Thus the first branch has its unique minimum at \(s=1/(2\sqrt3)\), and the second at \(s=\sqrt3/2\). Both points lie strictly inside their respective branches, and direct substitution gives the same value \(2/(3\sqrt3)\). Each branch tends upward away from its unique minimizer, so these are precisely the two global equality ratios. Distinct normalized ratios give nonisometric metrics: the shortest length of a loop representing an orientation-reversing deck transformation is exactly \(a\), and at fixed area \(a=\sqrt{As}\) distinguishes the two ratios. This completes the proof.

## Verification
The accompanying standalone `checker.py` uses exact rational arithmetic to enumerate the vertices of finite-window Dirichlet–Voronoi polygons around eleven sample anchors, computing the farthest squared distances by a method independent of the frontier calculation. Every value equals the theorem's rational eccentricity formula exactly. It also checks the deck-parity reduction, exact monotonic sample values, endpoint radii and both equal sharp area ratios. Run `python3 checker.py` with Python 3's standard library. These are finite diagnostics, **not** a proof of the universal assertions. The complete proof is the preceding five steps.

## Relationship to prior work
Davis and Recio-Mitter (first public arXiv version, 16 December 2019) classify Dirichlet domains and cut loci of flat Klein bottles in connection with geodesic motion-planning complexity. Their Section 3 gives explicit vertices for the unit-square two-dimensional quotient; that square-specific case is **prior established**. Our assertion does not claim those vertices or the deck-distance construction as new. It instead optimizes eccentricity over the entire aspect-ratio moduli, obtains a global area-to-metric-radius inequality, identifies *two* unequal optimal shapes, and proves the farthest-point mechanism's aspect-dependent transition.

Eyll's work on the Klein bottle's systolic inequalities and conformal metrics (2025), and Katz–Sabourau's nonpositively-curved systolic area theorem (2026), optimize the area relative to lengths of shortest noncontractible closed curves, not the minimax farthest-point metric radius. Their systolic conclusions do not imply the two shape-specific equality classes above. Related calculations of conditional random geodesic-distance means and pointwise injectivity-radius distributions do not determine this metric minimax functional. Historical priority for the exact new statements remains provisional; no claim of independent mathematical certification is made.

## Limitations
All conclusions use the intrinsic Euclidean flat metric in the stated fixed-point-free Klein quotient; they are not asserted for arbitrary curved or Finsler Klein metrics. The optimizer classification concerns exact area and distance, not statistical estimation from noisy data. The finite checker does not exhaust infinitely many parameters or deck configurations and is not a substitute for the proof. Searches of indexed literature cannot establish historical uniqueness, so specialized earlier work might still contain an equivalent formula or inequality.

## References
1. D. M. Davis and D. Recio-Mitter, *The geodesic complexity of n-dimensional Klein bottles*, arXiv:1912.07411v1 (first posted 2019-12-16); *New York Journal of Mathematics* 27 (2021), 296–318. https://arxiv.org/abs/1912.07411
2. J. Eyll, *Stability of Systolic Inequalities for the Möbius Strip and Klein Bottle*, *Journal of Geometric Analysis* 35 (2025), article 365, doi:10.1007/s12220-025-02197-9. https://link.springer.com/article/10.1007/s12220-025-02197-9
3. M. G. Katz and S. Sabourau, *Klein bottle and optimal systolic inequality for nonpositively curved surfaces*, *Annals of Global Analysis and Geometry* 70 (2026), article 11, doi:10.1007/s10455-026-10057-0. https://link.springer.com/article/10.1007/s10455-026-10057-0
