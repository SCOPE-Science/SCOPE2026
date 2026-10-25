# Sharp obtuseness probability for randomly projected Euclidean triangles

## Finding
Let \(T\) be any nondegenerate Euclidean triangle, embedded in a plane in \(\mathbb R^3\). Orthogonally project \(T\) onto a Haar-uniform random two-dimensional plane, and let \(P(T)\) be the probability that the projected triangle has an obtuse angle. Define, for \(0<\theta<\pi/2\),
\[
 x=\sin^2(\theta/2),\qquad
 p(\theta)=\frac{2x}{\pi}\int_0^1
 \frac{\sqrt{1-u^2}}{\sqrt{(1-xu^2)(1-x(1+u^2))}}\,du.
\]
Extend by \(p(\pi/2)=1/2\) and \(p(\theta)=1-p(\pi-\theta)\) for \(\pi/2<\theta<\pi\). If the angles of \(T\) are \(\alpha,\beta,\gamma\), then the complete probability law and sharp shape inequality are
\[
 P(T)=p(\alpha)+p(\beta)+p(\gamma)\ \ge\ 3p(\pi/3)
 =0.470339624536\ldots,
\]
with equality **if and only if** \(T\) is equilateral. In addition, \(P(T)<1\) for every nondegenerate \(T\), and the supremum \(1\) is approached by triangles with one angle tending to \(\pi\). The function \(p\) is strictly increasing on \((0,\pi)\) and strictly convex on \((0,\pi/2)\). Thus the exact attainable probability range is \([3p(\pi/3),1)\).

## Assumptions and scope
The triangle is fixed, with three distinct noncollinear vertices and positive side lengths. Randomness comes **only** from the target two-plane, equivalently its normal uniformly distributed on the unit sphere. The projected triangle is nondegenerate outside a null set. The claim concerns ordinary Euclidean angles of the projected image, not angles of a random triangle selected inside a domain, not a one-dimensional shadow, and not perspective projection. The result is similarity-invariant and does not depend on where \(T\) sits in \(\mathbb R^3\).

## Proof
**1. Local projected obtuseness.** Choose two unit edge directions at a vertex, separated by \(\theta\in(0,\pi)\). Let \(n\) be the random unit normal, and \(Q_n=I-nn^{\mathsf T}\). The projected angle is obtuse exactly when
\[
 \langle Q_nu,Q_nv\rangle=\cos\theta-(n\cdot u)(n\cdot v)<0.
\]
Put \(c=\cos(\theta/2)\), \(s=\sin(\theta/2)\), and write \(u=(c,s,0)\), \(v=(c,-s,0)\), \(n=(n_1,n_2,n_3)\). Using \(n_1^2+n_2^2+n_3^2=1\), the event is precisely
\[
 n_2^2+c^2n_3^2<s^2. \tag{1}
\]
Consequently its probability \(p(\theta)\) depends only on the original angle. For \(\theta=\pi/2\), exchange of \(n_1\) and \(n_2\) gives \(p=1/2\). Replacing \(v\) by \(-v\) reverses the projected inner-product sign, so \(p(\pi-\theta)=1-p(\theta)\). The exceptional equality case has spherical measure zero.

**2. The exact integral.** Suppose \(0<\theta<\pi/2\), so \(0<s<c\). In the original triangle plane write \(n=(r\cos\phi,r\sin\phi,\pm\sqrt{1-r^2})\). Its azimuth \(\phi\) is uniform on \([0,2\pi)\), and the radial cumulative distribution is \(\Pr(r\le a)=1-\sqrt{1-a^2}\). The projected inner-product test is equivalent to
\[
 r^2(\cos^2\phi-s^2)>\cos\theta.
\]
The event is possible precisely for azimuths in the two arcs with angular half-width \(\theta/2\) about \(0\) and \(\pi\). Integrating the radial upper tail gives
\[
 p(\theta)=\frac2\pi\int_0^{\theta/2}
 \sqrt{\frac{\sin^2(\theta/2)-\sin^2\phi}
 {1-\sin^2(\theta/2)-\sin^2\phi}}\,d\phi.
\]
The substitution \(\sin\phi=\sin(\theta/2)u\) yields the stated integral, with both denominators strictly positive for \(0<x<1/2\). An independently convenient representation, obtained by integrating (1) along polar latitudes, is
\[
 p(\theta)=1-\frac2\pi\int_0^{\pi/2}
 \sqrt{\frac{1-x(1+\sin^2 t)}{1-x\sin^2t}}\,dt.
\]

**3. Strict convexity.** For \(u\in[0,1]\) and \(0<x<1/2\), the function
\[
 \frac{x}{\sqrt{(1-xu^2)(1-x(1+u^2))}}
\]
has positive first derivative and positive second derivative with respect to \(x\); this follows directly by differentiating the two positive factors, or from their nonnegative power series and the leading factor \(x\). Integration against \(\sqrt{1-u^2}\,du\) therefore makes \(p\), considered as a function of \(x\), strictly increasing and strictly convex. Also \(x(\theta)=(1-\cos\theta)/2\) satisfies \(x'(\theta)=\sin\theta/2>0\) and \(x''(\theta)=\cos\theta/2>0\) for \(0<\theta<\pi/2\). Hence \(p(\theta)\) is strictly increasing and strictly convex there. Its reflected continuation is strictly increasing on \((\pi/2,\pi)\).

**4. The sharp lower bound.** A nondegenerate projected triangle can have at most one obtuse angle, so the three vertex events are disjoint. This proves \(P(T)=p(\alpha)+p(\beta)+p(\gamma)\). If \(T\) is acute, Jensen's inequality and \(\alpha+\beta+\gamma=\pi\) give
\[
 P(T)\ge3p((\alpha+\beta+\gamma)/3)=3p(\pi/3),
\]
with equality exactly for equal angles. If \(T\) is right or obtuse, its largest vertex angle contributes at least \(1/2\), and the other two contributions are positive.

To show rigorously that \(3p(\pi/3)<1/2\), specialize the integral to \(x=1/4\):
\[
 p(\pi/3)=\frac{1}{\pi\sqrt3}\int_0^1
 \frac{\sqrt{1-u^2}}{\sqrt{(1-u^2/4)(1-u^2/3)}}\,du.
\]
For \(0\le w\le1\),
\[
 (1+w/2)^2(1-w/4)(1-w/3)-1
 =\frac{w(w^3-3w^2-12w+20)}{48}\ge0.
\]
The last polynomial is nonnegative since \(w^3-3w^2-12w+20\ge5\) on that interval. Thus the reciprocal square-root factor is at most \(1+u^2/2\). Using \(\int_0^1\sqrt{1-u^2}\,du=\pi/4\) and \(\int_0^1u^2\sqrt{1-u^2}\,du=\pi/16\), one obtains
\[
 p(\pi/3)<\frac9{32\sqrt3}<\frac16.
\]
This strictly separates all nonacute initial triangles from the equilateral minimum.

**5. The sharp upper endpoint.** Every nondegenerate planar triangle admits an invertible linear map to an equilateral triangle. Divide that map by its largest singular value. Its singular values become \(1,k\) for some \(0<k\le1\), and a suitable orthogonal projection from \(\mathbb R^3\) onto a tilted plane restricts to exactly these singular values and singular directions, up to an irrelevant planar rotation. Therefore at least one viewing direction makes the image equilateral, and a positive-measure neighborhood makes it acute: \(P(T)<1\). Conversely, for triangles with angles tending to \((\pi,0,0)\), the identity \(p(\pi-\theta)=1-p(\theta)\), together with \(p(\theta)\to0\) as \(\theta\downarrow0\), gives \(P(T)\to1\). Continuity through continuous shape deformations yields the claimed complete interval of attainable values.

## Verification
Run `python3 verify_projection.py` from a directory containing that file. The script requires only the Python standard library. It numerically compares the two independently derived integral formulas at seventeen acute angles, checks the exact upper-bound polynomial and Jensen's inequality on sampled angle triples, and compares direct spherical-normal simulations of five triangle shapes with the integral predictions. Its deterministic run completed 2,022 direct consistency/inequality checks and 125,000 simulated random projected triangles; the equilateral integral evaluated to \(0.470339624536\ldots\). Numerical checks do not certify the infinitely quantified theorem; Steps 1–5 provide the proof.

## Relationship to prior work
Feldman and Klain's *Angles as probabilities* (arXiv:0809.3459, first posted September 19, 2008) derives random-projection **face-count** probabilities and simplex-angle sum identities; its fully inspected theorem and proof do not address the Euclidean angle signs of projections of a fixed planar triangle. Standard accounts of orthogonal projection note that an arbitrary triangle admits an equilateral orthogonal shadow, but do not give its viewing-probability distribution or a sharp shape minimizer. Classical geometric-probability papers on obtuse triangles sampled from a ball or rectangle use random vertex locations rather than a fixed triangle and random viewing direction. No assertion of exhaustive bibliographic priority is made.

## Limitations
The result concerns dimension-three ambient space and an orthogonal shadow in a random two-plane. It does not establish an analogous inequality for higher-codimension Haar projections, perspective projection, random-vertex sampling, or higher polygons. The exact minimum is defined by a one-dimensional integral, not an elementary closed form. The literature comparison is based on the material actually inspected; equivalent older treatments under alternative projected-angle terminology may exist. Independent historical-priority verification and independent proof review have not been performed.

## References
- D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459v1, September 19, 2008, https://arxiv.org/abs/0809.3459.
- G. R. Hall, *Acute triangles in the n-ball*, Journal of Applied Probability 19 (1982), 712–715, https://doi.org/10.2307/3213533 (publisher abstract compared; full article not inspected).
- E. W. Weisstein, *Orthogonal Projection*, MathWorld, https://mathworld.wolfram.com/OrthogonalProjection.html (online reference, viewed in the course of the comparison).
