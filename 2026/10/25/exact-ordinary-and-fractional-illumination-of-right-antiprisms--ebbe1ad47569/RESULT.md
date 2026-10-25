# Exact ordinary and fractional illumination of right antiprisms

## Finding
For every integer \(n\ge3\) and height \(h>0\), let \(A_{n,h}\) be the right antiprism whose vertices are the two unit-circumradius regular \(n\)-gons in horizontal planes at heights \(h\) and \(-h\), the lower polygon rotated by \(\pi/n\). Put \(m=\lfloor n/2\rfloor\). Then its ordinary illumination number and finite fractional illumination number are exactly
\[
\boxed{\ I(A_{n,h})=2\lceil n/m\rceil=\begin{cases}4&n\text{ even},\\6&n\text{ odd},\end{cases}\quad I^*(A_{n,h})=\frac{2n}{m}.\ }
\]
Thus every odd antiprism with \(n\ge5\) has a strict fractional-versus-integral gap, and the additive gap tends to \(2\) as odd \(n\to\infty\). Both invariants are independent of the positive height. More strongly, no direction illuminates vertices on both polygonal bases, at most \(m\) vertices on any one base can be illuminated at once, and *every cyclic consecutive block of at most \(m\) vertices* is simultaneously illuminable.

## Assumptions and scope
Write \(\theta=2\pi/n\). Coordinates are
\[
 v_j^+=(\cos(j\theta),\sin(j\theta),h),\qquad
 v_j^-=(\cos((j+1/2)\theta),\sin((j+1/2)\theta),-h)
\quad(0\le j<n).
\]
The convex hull \(A_{n,h}\) is a three-dimensional antiprism for every \(h>0\), with two polygonal base facets and \(2n\) triangular side facets. Ordinary illumination means choosing the fewest *directed vectors* so that each boundary point can move strictly into the interior along at least one of them. In fractional illumination a finite family of directed vectors has nonnegative weights; the sum of weights of vectors illuminating each boundary point must be at least one. The infimum of the total weights is \(I^*\). In particular, a line allowing its two opposite orientations is **not** one directed illuminating vector.

## Proof
**Facet-normal formula.** Set
\[
 c=\cos(\theta/2),\quad q=\sin(\theta/2),\quad
 k=\frac{1-c}{2h}>0.
\]
At upper vertex \(v_j^+\), let \(e_j=(\cos(j\theta),\sin(j\theta))\) and \(t_j=(-\sin(j\theta),\cos(j\theta))\). Four outward facet normals, with independent positive scalings, are
\[
 (0,0,1),\quad(e_j,-k),\quad(c e_j+q t_j,k),\quad(c e_j-q t_j,k).\tag{1}
\]
At lower vertex \(v_j^-\), replace \(j\theta\) by \((j+1/2)\theta\) and reverse every displayed vertical component. To confirm (1), the top base has outward normal \((0,0,1)\). The side triangle through \(v_j^+\) and its two adjacent lower vertices has horizontal radial normal \(e_j\); equality of supporting values at its vertices forces \(2hk=1-c\). The two other side triangles have horizontal normals at angular offsets \(\pm\theta/2\) from \(e_j\); the same identity forces their displayed vertical components. For each triangle the other vertices have strictly smaller supporting values, by the regular polygons' supporting-edge inequality. Every upper vertex is incident to precisely these three triangular facets and the top base. The lower formula follows by reflection in the midplane followed by the half-step rotation. This gives all active facet inequalities.

**One-direction capacity.** Let \(u=(w,s)\), with \(w\in\mathbb R^2\), illuminate an upper vertex \(v_j^+\). By the base-facet normal, \(s<0\). Put \(\delta=-ks>0\), \(a_j=w\cdot e_j\), and \(b_j=w\cdot t_j\). Strict inward pointing through the other three active facets is equivalent to
\[
 a_j+\delta<0,\qquad c a_j+q|b_j|<\delta.\tag{2}
\]
Thus \(a_j<0\) and
\[
 q|b_j|<(1+c)(-a_j).\tag{3}
\]
For \(w\ne0\), let \(\varphi_j\in(-\pi,\pi]\) be the angle from \(-w\) to \(e_j\). Inequality (3) says
\[
 |\varphi_j|<\arctan\frac{1+c}{q}
 =\frac\pi2-\frac\theta4.
\tag{4}
\]
In particular, the upper vertices lit by any one direction have equispaced radial angles within an *open* arc of length \(\pi-\theta/2\). Such an arc contains at most \(m=\lfloor n/2\rfloor\) of the \(n\) equally spaced points: if it contains \(r\) points, their minimum span is \((r-1)\theta\), which must be strictly below \(\pi-\theta/2\), yielding \(r\le m\). A direction illuminating a lower vertex needs \(s>0\) by the lower base normal. Hence no direction lights any vertices from both layers, and every direction lights at most \(m\) vertices total.

**Realizing every consecutive block.** Fix \(1\le r\le m\) and an upper cyclic block \(v_j^+,v_{j+1}^+,\ldots,v_{j+r-1}^+\). Let \(e\) be the unit horizontal vector pointing at its middle azimuth, and let
\[
 \alpha=\frac{(r-1)\theta}{2},\qquad
 \max\{0,-c\cos\alpha+q\sin\alpha\}<\delta<\cos\alpha.\tag{5}
\]
There is a positive-length interval in (5), since
\[
 \tan\alpha<\frac{1+c}{q}=\cot(\theta/4),
 \qquad \alpha<\frac\pi2-\frac\theta4.
\]
Choose the inward direction \(u=(-e,-\delta/k)\). For each block vertex the horizontal angle from \(e\) has magnitude at most \(\alpha\), so \(a_j\le-\cos\alpha\), while the largest possible \(c a_j+q|b_j|\) on this interval is \(-c\cos\alpha+q\sin\alpha\). Equation (5) makes both inequalities in (2) strict at every block vertex. The same construction, rotating its planar part by \(\theta/2\) and changing the sign of its vertical part, illuminates any lower cyclic block of length at most \(m\).

**Ordinary and fractional optima.** Since each direction lights vertices in only one layer and at most \(m\) vertices there, at least \(\lceil n/m\rceil\) directions per layer are needed. Partition the \(n\) vertices of each layer into \(\lceil n/m\rceil\) consecutive blocks of length at most \(m\) and apply the construction above, attaining the lower bound. Since \(\lceil n/\lfloor n/2\rfloor\rceil=2\) for even \(n\) and \(3\) for odd \(n\), this proves the ordinary formula.

For any fractional illumination with total weight \(W\), sum the unit-demand inequalities at all \(2n\) vertices. Each atom's weight is counted at most \(m\) times, so \(2n\le mW\), hence \(W\ge2n/m\). Conversely, for each layer construct the \(n\) cyclic consecutive blocks of length \(m\) and their illuminating directions. Give each of these \(2n\) directions weight \(1/m\). Each vertex belongs to exactly \(m\) cyclic blocks in its layer, so the weighted illumination is at least one at every vertex, with total weight \(2n/m\). This proves the fractional formula.

Finally, covering vertices also covers the boundary: if a boundary point lies in a face containing vertex \(v\), the facets active at the point form a subset of those active at \(v\); every direction illuminating \(v\) strictly satisfies all facets active at the point. The same observation applies to the weighted construction. This completes both classifications.

## Verification
Run the self-contained Python 3 standard-library checker with `python verify.py`. It derives all candidate facet normals from (1), verifies their support against every one of the \(2n\) vertices, verifies the three-versus-\(n\) facet incidences, constructs and checks every contiguous block of maximal size \(m\) and every block in the ordinary partition, tests the cyclic fractional incidence counts, and samples generic directions to stress-test both one-layer separation and the cap \(m\). It verifies \(3\le n\le80\) and heights \(h=0.1,1,3\), producing `VERIFY_OK` and 143208 regression checks. These floating-point tests are **not** a proof for all \(n,h\); the exact inequalities (1)--(5), integer circular-spacing bound, and cyclic construction above are the complete proof.

## Relationship to prior work
Naszódi introduced fractional illumination for convex bodies and developed its weighted-covering interpretation. Gorodzha's preprint first made public on 20 September 2026 proves the universal bound \(I^*(K)\le2^d\) for every \(d\)-dimensional convex body, with equality exactly for parallelotopes; that bound does not determine an antiprism's exact value, parity dependence, or ordinary optimum.

A closely related same-object public calculation, *Every uniform antiprism has X-ray number three*, proves \(X(A_n)=3\) for uniform antiprisms. X-ray numbers count undirected lines: one line can serve vertices with opposite orientations and therefore only implies the coarse upper bound \(I(A_n)\le6\). It neither establishes the even-case optimum of four, nor the fractional values and gaps, nor covers arbitrary positive heights. Its normal-fan treatment is acknowledged; the present theorem evaluates different invariants and adds sharp parity, height-invariance, and fractional-cover classifications. Other exact fractional-illumination results for planar equiangular polygons evaluate different two-dimensional normal fans and do not imply the three-dimensional antiprism theorem. Results on products of simplices also do not cover antiprisms except unrelated low-dimensional coincidences. Searches of the stated objects, aliases, and parameters did not identify an implication-equivalent source; this is not a guarantee of historical novelty.

## Limitations
The two regular \(n\)-gon layers must be congruent, concentric, half-step rotated, and separated by a positive height. Arbitrary distorted or nonconcentric antiprisms are not addressed. The formula is for *directed* ordinary and finitely supported fractional illumination, not undirected X-ray number or norm-weighted quantitative illumination. The classification of optimal ordinary and fractional weights is not claimed to be unique; the displayed constructions prove optimal values. Although strong matching earlier coverage was not located, historical priority remains subject to independent literature review.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics **4** (2009), 83–88, DOI: 10.55016/ojs/cdm.v4i2.62022.
2. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1, first publicly submitted 20 September 2026, https://arxiv.org/abs/2609.23913.
3. *Every uniform antiprism has X-ray number three*, published mathematical research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-every-uniform-antiprism-has-x-ray-number-three--8163a250996c .
4. *Exact fractional illumination of every equiangular polygon*, published mathematical research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-every-equiangular-polygon--035cb636082a .
