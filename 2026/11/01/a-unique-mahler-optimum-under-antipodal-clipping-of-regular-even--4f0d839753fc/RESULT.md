# A unique Mahler optimum under antipodal clipping of regular even polygons

## Finding

Fix an even integer \(n\ge4\). Let \(P_n\subset\mathbb R^2\) be the regular \(n\)-gon of circumradius one whose vertices are
\[
 v_j=(\cos(2\pi j/n),\sin(2\pi j/n)),\qquad 0\le j<n.
\]
For every real \(h\) with \(\cos(2\pi/n)\le h\le1\), form the centrally symmetric clipped polygon
\[
 K_{n,h}=P_n\cap\{(x,y):|x|\le h\}.
\]
For \(n=4\), impose \(h>0\) as well, to keep nonempty interior. Put \(q_n=\sin^2(\pi/n)\). Its Santaló point is the origin, and the Mahler area product is exactly
\[
 \boxed{\mathcal M_n(h)=\operatorname{area}(K_{n,h})\operatorname{area}(K_{n,h}^{\circ})
 =\left(n-2+\frac2h\right)\left(nq_n-2(1-h)^2\right).}
\]
The product has a **unique maximum at a strict interior clipping depth** \(h=h_n\) for every even \(n\ge4\). For \(n=4\), \(h_4=1/2\), \(\mathcal M_4(h_4)=9\), and the resulting hexagon is affinely regular. For every even \(n\ge6\), \(h_n\) is the unique root in \((\cos(2\pi/n),1)\) of
\[
 \boxed{2+(2n-6)h^2+(4-2n)h^3-n\sin^2(\pi/n)=0.}
\]
As the clipping depth \(1-h\) increases from zero, the Mahler product first increases strictly and subsequently decreases strictly; both adjacent regimes are nonempty. For every even \(n\ge6\), complete deletion of the two targeted vertices has smaller product than the unmodified regular \(n\)-gon.

The sharp large-order consequences are
\[
 \boxed{h_n=1-\frac{\pi^2}{2n^2}+O(n^{-4}),\qquad
 \mathcal M_n(h_n)-\mathcal M_n(1)=\frac{\pi^4}{2n^3}+O(n^{-5}).}
\]
With \(\mathcal R_m=m^2\sin^2(\pi/m)\), the maximal product among all planar convex polygons having at most \(m\) vertices, one also has
\[
 \boxed{\lim_{\substack{n\to\infty\\ n\ \mathrm{even}}}
 \frac{\mathcal M_n(h_n)-\mathcal R_n}{\mathcal R_{n+2}-\mathcal R_n}=\frac38.}
\]
The last limit quantifies the fraction of the optimal regular-\((n+2)\)-gon gain captured asymptotically by this particularly constrained two-corner operation.

## Assumptions and scope

All areas are ordinary Euclidean two-dimensional Lebesgue areas. The polar is \(K^\circ=\{z:\langle z,x\rangle\le1\ \text{for all }x\in K\}\). Central symmetry ensures that the origin is the Santaló point of each nondegenerate \(K_{n,h}\). Opposite vertices are the vertices on the horizontal axis; the cut lines are parallel to each other and perpendicular to that axis. The stipulated lower bound \(h\ge\cos(2\pi/n)\) ensures that the clipping planes pass no farther than the two vertices adjacent to each removed vertex, so only two isolated caps are deleted. At \(n=4\), \(h=0\) degenerates to a segment and is excluded. At \(n\ge6\), both endpoints are admissible as planar bodies; an endpoint may have redundant collinear vertices.

This is a fixed family of truncated polygons, not a claim about arbitrary asymmetric truncations, arbitrary strips, higher dimensions, or the global maximizers of Mahler product in all polygon classes.

## Proof

Write \(\alpha=\pi/n\) and \(c=\cos(2\alpha)=1-2q_n\). The starting polygon has area \(n\sin\alpha\cos\alpha\). For any \(h\in[c,1]\), the removed cap at the vertex \((1,0)\) has horizontal height \(1-h\); the two adjacent edges give its half-width at abscissa \(x\) as \((1-x)\cot\alpha\). Integration gives one cap area \((1-h)^2\cot\alpha\), and there are two congruent opposite caps. Thus
\[
 A_n(h)=n\sin\alpha\cos\alpha-2(1-h)^2\cot\alpha.
\]

The polar of \(P_n\) is the regular polygon with vertices on outward facet normals at angles \((2j+1)\alpha\), each of Euclidean length \(\sec\alpha\); its area is \(n\tan\alpha\). Polarity converts intersection with the strip into the convex hull
\[
 K_{n,h}^{\circ}=\operatorname{conv}\big(P_n^{\circ},(1/h,0),(-1/h,0)\big).
\]
The original polar has the vertical edge between \((1,\tan\alpha)\) and \((1,-\tan\alpha)\), and the opposite edge between \((-1,\tan\alpha)\) and \((-1,-\tan\alpha)\). Throughout the stipulated parameter interval, the two new axial vertices replace precisely these two edges with two triangles. Each triangle has base \(2\tan\alpha\) and height \(1/h-1\), so
\[
 B_n(h)=n\tan\alpha+2\tan\alpha(1/h-1).
\]
The geometric assertion about adjacent polar vertices follows either by dualizing the two planar caps, or by checking that the new strip facets meet the starting polygon on the two edges incident to the targeted vertex and no others. Both arguments include the limiting collinear case. Multiplication of \(A_n(h)\) and \(B_n(h)\) yields the boxed product formula.

Differentiate the product and set
\[
 G_n(h)=2+(2n-6)h^2+(4-2n)h^3-nq_n.
\]
Direct algebra gives
\[
 \mathcal M_n'(h)=\frac{2G_n(h)}{h^2},\qquad
 G_n'(h)=-2h\,[3(n-2)h-2(n-3)].
\]
If \(n=4\), then \(q_n=1/2\), \(\mathcal M_4(h)=8+4h-4h^2\), so the unique maximum is \(h_4=1/2\), with value nine and equality of both nondegenerate end-regimes established directly.

Now assume even \(n\ge6\). Since \(q_n\le1/4\), \(c=1-2q_n\ge1/2\). At the lower boundary,
\[
 G_n(c)=q_n(4q_n-3)(4nq_n-n-8q_n)>0,
\]
whereas \(G_n(1)=-nq_n<0\). For \(n=6\), the bracket in \(G_n'(h)\) is strictly positive for \(h>1/2=c\). For every even \(n\ge8\), \(h\ge c\ge\cos(\pi/4)>2/3\), while \(2(n-3)/(3(n-2))<2/3\); hence the bracket is again positive. Thus \(G_n\) is strictly decreasing in the interior of the interval, crosses zero exactly once, and \(\mathcal M_n\) increases up to that crossing and decreases afterward as \(h\) increases. Equivalently, as the clipping depth increases, the product increases and then decreases, with the unique maximum at the crossing.

For completeness, direct subtraction at the lower endpoint yields
\[
 \mathcal M_n(c)-\mathcal M_n(1)
 =-\frac{4q_n^2\,[n(1-4q_n)+8q_n]}{1-2q_n}<0
\]
when \(n\ge6\). At \(n=4\), the limiting product as \(h\downarrow0\) is eight.

For the asymptotics, write \(w_n=1-h_n\). The root belongs to \((c,1)\), so \(0<w_n<2q_n\), and the cubic equation becomes
\[
 0=-nq_n+2nw_n+(-4n+6)w_n^2+(2n-4)w_n^3.
\]
It follows uniformly as \(n\to\infty\) that \(w_n=q_n/2+O(q_n^2)\). Since \(q_n=\pi^2/n^2+O(n^{-4})\), this proves the expansion for \(h_n\). Furthermore,
\[
 \mathcal M_n(1-w)-\mathcal M_n(1)
 =\frac{2nq_n w}{1-w}-2nw^2-\frac{4w^3}{1-w}.
\]
Substituting \(w=w_n=q_n/2+O(q_n^2)\) gives \(nq_n^2/2+O(nq_n^3)=\pi^4/(2n^3)+O(n^{-5})\). Finally,
\[
 \mathcal R_n=\pi^2-\frac{\pi^4}{3n^2}+O(n^{-4}),\qquad
 \mathcal R_{n+2}-\mathcal R_n=\frac{4\pi^4}{3n^3}+O(n^{-4}),
\]
which proves the ratio \(3/8\).

## Verification

The included `clip_polygon_checker.py` constructs the regular polygon vertices, clips them independently by two halfplanes, computes the polar from oriented facet equations, and obtains both areas by the shoelace formula. It compares these geometry-derived areas and their product with the analytical formulas across eight even polygon orders and 25 interior depths each. It also checks optimizer location and sample asymptotics. Run `python3 clip_polygon_checker.py` from the directory containing the script. The observed result was `PASS: 629 independent geometric, optimization, and asymptotic checks` (independent implementations, not an external scientific audit). The computations are finite corroboration; the preceding symbolic and geometric proof covers every stated parameter.

## Relationship to prior work

Meyer and Reisner (2011) proved that among polygons with at most a given number of vertices, the regular polygon maximizes Mahler product and supplied equality conditions. That yields the external upper benchmark \(\mathcal R_{n+2}\), but not the exact product or the location of the maximum along the opposite-corner clipping family. Alexander, Fradelizi, and Zvavitch (2017) gave another proof and general higher-dimensional results, again not this constrained one-parameter profile. Lin and Leng (2010) examined vertex removal for the planar symmetric Mahler minimum and proved a product-reducing removal under their geometric hypotheses; endpoint comparisons of this kind do not imply the strict interior maximizer here. Meyer and Reisner (2006) studied the reciprocal polar-volume convexity of shadow systems; those general statements do not supply this two-facet moving-cut identity or the explicit asymptotic gain.

## Limitations

Historical priority beyond the inspected literature and available mathematical research records remains uncertain. The algebraic formula depends on two opposite cuts removing only the selected caps; deeper cuts, odd-order polygons, arbitrary edge directions, and nonregular polygons are not covered. The large-order expansions are for even orders tending to infinity, not a uniform bound for unrelated geometric deformations. The finite computational checks are not a substitute for the proof and do not constitute independent external review.

## References

- M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, Mathematika 53 (2006), 129–148, DOI: 10.1112/S0025579300000061; arXiv:math/0606305, publicly available 2006-06-13.
- Y. Lin and G. Leng, *Convex bodies with minimal volume product in R2 — a new proof*, Discrete Mathematics 310 (2010), 3018–3025, DOI: 10.1016/j.disc.2010.07.008, publicly available online 2010-08-05.
- M. Meyer and S. Reisner, *On the volume product of polygons*, Abh. Math. Semin. Univ. Hambg. 81 (2011), 93–100, DOI: 10.1007/s12188-011-0054-3, publicly available online 2011-04-05.
- M. Alexander, M. Fradelizi and A. Zvavitch, *Polytopes of Maximal Volume Product*, arXiv:1708.07914, publicly available 2017-08-26.
