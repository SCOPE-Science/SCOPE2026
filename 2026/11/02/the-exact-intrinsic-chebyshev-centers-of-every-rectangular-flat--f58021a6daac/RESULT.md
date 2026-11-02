# The exact intrinsic Chebyshev centers of every rectangular flat pillowcase

## Finding
Let \(A\ge B>0\), and form the rectangular flat torus
\[
T_{A,B}=\mathbb R^2/(A\mathbb Z\oplus B\mathbb Z)
\]
with the quotient Euclidean length metric. Its central-inversion quotient
\[
P_{A,B}=T_{A,B}/(p\sim-p)
\]
is the rectangular flat pillowcase, a flat metric two-sphere with four cone points of angle \(\pi\). The source eccentricity of a point is \(e([p])=\max_{[q]\in P_{A,B}}d_{P_{A,B}}([p],[q])\).

The exact intrinsic Chebyshev radius is
\[
\boxed{\operatorname{rad}(P_{A,B})=\frac{A^2+B^2}{4A}.}
\]
There are **exactly two** Chebyshev centers, the inversion classes of
\[
\boxed{p_1=(A/4,B/4),\qquad p_2=(A/4,3B/4).}
\]
They are nonsingular points and lie in one isometry orbit. In equivalent two-center language, **every** optimal unordered pair of centers for covering the rectangular flat torus by two equal closed geodesic disks is, up to translation, the half-period-diagonal pair
\[
\boxed{\{q,q+(A/2,B/2)\}.}
\]
In particular, if the two periods are originally \(a,b>0\) in either order, the radius is \((a^2+b^2)/(4\max\{a,b\})\).

## Assumptions and scope
Distances are infima of lengths of paths in the flat quotient metric; no metric from an embedding of the pillowcase into three-dimensional space is used. The sides \(A,B\) denote the full translation periods, not the sides of a folded physical pillow. The torus quotient is taken first, then by inversion. Centers on the torus may be anywhere and the covering disks have equal radii; no a priori pairing or lattice-symmetry restriction is imposed. All periods are strictly positive, including \(A=B\).

## Proof
**1. Quotient eccentricity is an unrestricted torus two-center covering problem.** For torus points \(p,q\), the intrinsic quotient metric obeys
\[
d_{P_{A,B}}([p],[q])=\min\{d_T(p,q),d_T(p,-q)\}
=\min\{d_T(p,q),d_T(-p,q)\},
\]
using that inversion is an isometry. Therefore \(e([p])\) is the covering radius in \(T_{A,B}\) of the two-point set \(\{p,-p\}\). Every unordered torus pair \(\{u,v\}\) can be translated to an antipodal pair: choose \(m\) with \(2m=u+v\) on the torus (the doubling map is onto), and translate by \(-m\). Translation preserves distances. Thus minimizing eccentricity is exactly the unrestricted equal-two-disk covering problem on \(T_{A,B}\).

**2. Sharp lower bound from two vertical fibers.** Suppose two closed geodesic disks of radius \(r\), centered at \(c_1=(x_1,y_1)\) and \(c_2=(x_2,y_2)\), cover the entire torus. Set
\[
R=\frac{A^2+B^2}{4A},\qquad R\le A/2.
\]
If \(r\ge A/2\) then \(r\ge R\). Assume \(0\le r<A/2\). On the horizontal coordinate circle of period \(A\), choose the two positions \(x_1+r\) and \(x_1-r\). At either such position the vertical intersection with the *first* disk is a single point, because its horizontal distance from the first center equals \(r\). To cover the remaining vertical circle, the *second* disk must cover that entire vertical circle, by closedness; a proper closed circular arc together with a single point cannot cover the whole circle.

A radius-\(r\) disk covers an entire vertical fiber of period \(B\) only if \(r\ge B/2\), and then only if the fiber's horizontal distance from its center is at most
\[
t=\sqrt{r^2-B^2/4}.
\]
Thus \(r\ge B/2\) and both fibers \(x_1\pm r\) lie in a single horizontal arc of length \(2t\) centered at \(x_2\). Since \(t<r<A/2\), their shortest separation on the horizontal circle is \(\min(2r,A-2r)\). The arc cannot span the \(2r\) option, and hence
\[
A-2r\le 2t,
\quad\text{or}\quad
r+\sqrt{r^2-B^2/4}\ge A/2.
\]
Because \(r<A/2\), squaring the equivalent inequality \(\sqrt{r^2-B^2/4}\ge A/2-r\) yields
\[
Ar\ge(A^2+B^2)/4,\qquad r\ge R.
\]
This proves the lower bound without any assumption on the relative placement of the centers.

**3. Sharp upper bound via a triangular tiling.** Take torus centers \(c_1=(0,0)\) and \(c_2=(A/2,B/2)\). Their lifts form the periodic set
\[
\Lambda\cup\bigl(\Lambda+(A/2,B/2)\bigr),
\qquad \Lambda=A\mathbb Z\oplus B\mathbb Z.
\]
The plane has a tiling by congruent triangles whose vertices belong to this set; one representative has vertices
\[
v_1=(0,0),\quad v_2=(0,B),\quad v_3=(A/2,B/2).
\]
Its circumcenter is \(c=(t,B/2)\), where
\[
t=\frac{A^2-B^2}{4A},\qquad
\|c-v_1\|=\|c-v_2\|=\|c-v_3\|=R.
\]
For any point \(z\) in this triangle, with barycentric coefficients \(\lambda_i\ge0\), \(\sum\lambda_i=1\), \(\sum\lambda_i v_i=z\), the exact variance identity gives
\[
\sum_{i=1}^3\lambda_i\|z-v_i\|^2
=R^2-\|z-c\|^2\le R^2.
\]
At least one triangle vertex therefore lies at distance at most \(R\). This applies in each triangle of the tiling and proves that the two stated torus disks cover the entire torus. Together with Step 2, it proves the radius formula.

**4. Rigidity of every optimal pair.** Let \(r=R\) be optimal, and put
\[
t=\sqrt{R^2-B^2/4}=A/2-R=\frac{A^2-B^2}{4A}.
\]
First suppose \(A>B\), so \(R<A/2\). As in Step 2, the fibers \(x_1\pm R\) both must be covered by the second disk alone, hence lie in its horizontal covering arc of length \(2t=A-2R\). They have *exactly* this shorter circular separation. Therefore the horizontal center of that arc is forced:
\[
x_2\equiv x_1+A/2\pmod A.
\]
If \(A=B\), then \(R=A/2=B/2\). The fiber at \(x_1+A/2\) meets the first disk at only one point. The second disk can contain this full vertical fiber only when its horizontal distance is zero; hence again \(x_2\equiv x_1+A/2\pmod A\).

For either case, inspect the vertical fiber at \(x=x_1+R-\varepsilon\), where \(\varepsilon>0\) decreases to zero. The first disk intersects it in a closed vertical arc centered at \(y_1\), of half-length
\[
h_1(\varepsilon)=\sqrt{R^2-(R-\varepsilon)^2}\longrightarrow0.
\]
The second disk has horizontal distance \(t+\varepsilon\) to that fiber and intersects it in a vertical arc centered at \(y_2\), with half-length
\[
h_2(\varepsilon)=\sqrt{R^2-(t+\varepsilon)^2}<B/2,
\qquad h_2(\varepsilon)\longrightarrow B/2.
\]
The nonempty complement of this latter arc is an open arc centered at the vertical antipode \(y_2+B/2\); as \(\varepsilon\to0^+\) it shrinks to that antipode. Full coverage of each fiber forces it to lie in the first disk's shrinking arc, so necessarily
\[
y_1\equiv y_2+B/2\pmod B.
\]
Thus every optimal torus pair has difference \((A/2,B/2)\) modulo periods.

**5. Exactly two quotient centers.** For a quotient source \([p]\), its torus covering pair is \(\{p,-p\}\). Step 4 shows that \([p]\) minimizes eccentricity exactly when
\[
2p\equiv(A/2,B/2)\pmod\Lambda.
\]
There are four solutions modulo \(\Lambda\):
\[
(A/4,B/4),\ (A/4,3B/4),\ (3A/4,B/4),\ (3A/4,3B/4).
\]
Inversion groups them into precisely two orbits, represented as in the theorem. None is an inversion fixed point (the four cone points), and Step 4 proves that no further minimizer exists.

## Verification
The standalone standard-library script `verify.py` performs exact rational checks of the circumcenter, three equal vertex distances, the horizontal tangency identity, the extreme witness, and the radius inequalities for seven rational aspect-ratio configurations, including the square. It also performs independently sampled finite torus-distance covering comparisons on an \(80\)-by-\(80\) grid. Running `python3 verify.py` must print `VERIFY_OK`. These finite tests corroborate the formulas but do not establish either continuum-wide optimality or uniqueness; those are proved in Steps 2–5.

## Relationship to prior work
Hedden, Herald, and Kirk give the torus-inversion quotient description of the pillowcase (section 3.1 of their 2013 preprint); their mathematical aim is a representation-space model for knot invariants, not an intrinsic Chebyshev-center classification. Musin and Nikitenko study maximizing the separation of congruent circle centers (packing) on a square flat torus. Their problem and optimality direction differ from minimizing the covering radius of two disks on every rectangular torus. Published exact two-disk results for *planar regular polygons* apply to convex subsets of the plane with boundary; they do not imply the corresponding result for a torus with periodic identification or its inversion quotient.

The new assertion is the exact all-aspect-ratio Chebyshev radius and the complete two-point minimizer locus on the rectangular inversion quotient, equivalently a rigidity theorem for unrestricted two-disk covers of rectangular flat tori. It is not a claim to have originated flat tori, pillowcases, general two-center covering problems, or triangle circumradius arguments.

## Limitations
The theorem is restricted to flat *rectangular* tori and their inversion quotients, not arbitrary oblique lattices, nonflat sphere metrics, or more than two covering centers. It does not provide the full eccentricity function for nonoptimal sources. Historical priority remains provisional: an earlier unindexed treatment of two-disk flat-torus coverings might contain this formula or an equivalent stronger result. The proof is analytical; finite test agreement is not an independent mathematical audit.

## References
1. O. R. Musin and A. V. Nikitenko, *Optimal packings of congruent circles on a square flat torus*, arXiv:1212.0649v1 (2012-12-04), https://arxiv.org/abs/1212.0649. The optimization here is packing, not covering.
2. M. Hedden, C. Herald and P. Kirk, *The pillowcase and perturbations of traceless representations of knot groups*, arXiv:1301.0164v1 (2013-01-02), https://arxiv.org/abs/1301.0164. Section 3.1 defines the relevant quotient.
3. D. Protasov, A. Tolmachev and V. Voronov, *Optimal partitions of the flat torus into parts of smaller diameter*, arXiv:2402.03997 (2024-02-06), https://arxiv.org/abs/2402.03997. Different metric optimization invariant.
