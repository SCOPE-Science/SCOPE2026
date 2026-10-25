# Illumination phase transition under nonzero rotations of regular prisms

## Finding
For integers \(n\ge3\), let \(\theta=2\pi/n\), \(h>0\), and \(0\le t<\theta\). Consider the three-dimensional convex hull
\[
K_{n,t,h}=\operatorname{conv}\left(\{(\cos(j\theta),\sin(j\theta),h):0\le j<n\}\cup\{(\cos(j\theta+t),\sin(j\theta+t),-h):0\le j<n\}\right).
\]
Its two parallel bases are congruent regular \(n\)-gons. Write \(I(K)\) for ordinary illumination by parallel directions and \(I^*(K)\) for finite fractional illumination. Put \(m=\lfloor n/2\rfloor\), \(q=\lfloor(n-1)/2\rfloor\). For every \(0<t<\theta\),
\[
\boxed{I(K_{n,t,h})=2\left\lceil\frac{n}{m}\right\rceil,\qquad I^*(K_{n,t,h})=\frac{2n}{m}.}
\]
At the aligned endpoint \(t=0\),
\[
\boxed{I(K_{n,0,h})=2\left\lceil\frac{n}{q}\right\rceil,\qquad I^*(K_{n,0,h})=\frac{2n}{q}.}
\]
Both values are independent of \(h\) and, in the open interval, independent of the rotation angle \(t\). In particular, every nonzero rotation of a right regular prism with even \(n\) reduces its ordinary illumination number to \(4\) and its fractional illumination number to \(4\). The aligned values are \(8\) for \(n=4\), respectively \(6\) for even \(n\ge6\), in ordinary illumination, and \(2n/(n/2-1)\) in fractional illumination. For odd \(n\), the values do not change at alignment: \(I=6\) and \(I^*=2n/m\).

## Assumptions and scope
A direction \(u\ne0\) illuminates a boundary point \(x\) if \(x+\varepsilon u\) lies in the interior for some \(\varepsilon>0\). A finite collection of pairs of directions and nonnegative weights fractionally illuminates \(K\) if the weights of directions illuminating every boundary point sum to at least one; \(I^*(K)\) is the infimum of total weights. Unit normalization does not alter illuminated points. All inequalities at facets are strict; the excluded aligned angles \(t\equiv0\pmod\theta\) have different facets and are evaluated separately. For a polytope, vertex illumination suffices: a direction illuminating a vertex illuminates every boundary point in the relative interior of a face containing that vertex.

## Proof
**1. Facets.** Write \(e_a=(\cos a,\sin a)\). For \(0<t<\theta\), set
\[
\delta=\cos(t-\theta/2)-\cos(\theta/2)>0,\qquad c=\delta/(2h)>0.
\]
The two horizontal bases have outward normals \((0,0,1)\) and \((0,0,-1)\). For each \(j\) modulo \(n\), the triangular facet through the adjacent upper vertices at angles \(j\theta\), \((j+1)\theta\) and the lower vertex at angle \(j\theta+t\) has outward normal
\[
F_j^+=(e_{(j+1/2)\theta},c).
\]
The triangular facet through adjacent lower vertices at angles \(j\theta+t\), \((j+1)\theta+t\) and the upper vertex at angle \((j+1)\theta\) has outward normal
\[
F_j^-=(e_{(j+1/2)\theta+t},-c).
\]
The supporting value of each listed side inequality is \(\cos(\theta/2)+ch\); direct angular comparison shows all other vertices lie strictly below it. These are precisely the \(2n\) lateral facets: together with the bases they form the complete closed supporting triangulation of the boundary, with \(2n\) vertices and \(4n\) edges.

At the upper vertex \(T_j\), the active side facets are \(F_{j-1}^+,F_j^+,F_{j-1}^-\). Thus a direction \(u=(v,z)\in\mathbb R^2\times\mathbb R\) illuminates \(T_j\) exactly if
\[
z<0,\quad e_{(j-1/2)\theta}\cdot v+cz<0,\quad e_{(j+1/2)\theta}\cdot v+cz<0,\quad e_{(j-1/2)\theta+t}\cdot v-cz<0.\tag{1}
\]
The lower vertices require \(z>0\). Hence no direction illuminates vertices from both horizontal layers.

**2. Sharp capacity of one layer.** For even \(n=2m\), condition (1) implies \(e_{(j-1/2)\theta+t}\cdot v<0\) whenever \(T_j\) is illuminated. These \(n\) planar normals occur in \(m\) opposite pairs, so at most \(m\) upper vertices can be illuminated.

For odd \(n=2m+1\), add the inequalities for \(F_{j-1}^+\) and \(F_{j-1}^-\) at \(T_j\), cancelling their opposite vertical coefficients. The result says
\[
2\cos(t/2)e_{(j-1/2)\theta+t/2}\cdot v<0.\tag{2}
\]
Likewise, adding the inequalities for \(F_{j+m}^+\) and \(F_{j+m-1}^-\) at \(T_{j+m}\) gives
\[
2\cos((\theta-t)/2)e_{(j+m)\theta+t/2}\cdot v<0.\tag{3}
\]
The two planar vectors are antiparallel, since \((m+1/2)\theta=\pi\), and both scalar cosines are positive. Thus \(T_j\) and \(T_{j+m}\) cannot be simultaneously illuminated. These conflicts form a single odd cycle on the \(n\) upper indices, because \(\gcd(m,2m+1)=1\); its largest independent set has \(m\) vertices. Again at most \(m\) upper vertices are illuminated.

**3. Every \(m\)-vertex consecutive block is illuminated.** Choose indices \(a,a+1,\ldots,a+m-1\) and let
\[
\beta=\bigl(a+(m-2)/2\bigr)\theta+t,\quad L=(m-1)\theta/2,\quad C=\cos L,\quad U=\max\{0,-\cos(L+t),-\cos(L+\theta-t)\}.
\]
Since \(2L+t<\pi\) and \(2L+\theta-t<\pi\) for \(m=\lfloor n/2\rfloor\) and \(0<t<\theta\), we have \(0\le U<C\). Put \(w=(U+C)/2\) and take the explicit direction
\[
u=(-e_\beta,-w/c).\tag{4}
\]
All active lower-edge normals \(e_{(j-1/2)\theta+t}\) for the chosen upper vertices have dot product with \(-e_\beta\) at most \(-C\). All active upper-edge normals have dot product at most \(U\). Substitution in (1) therefore gives strict negativity at all incident facets. The direction illuminates the entire block. By the symmetry \((x,z)\mapsto(R_{-t}x,-z)\), which transforms this family into the same family with angle \(\theta-t\), the identical capacity and block constructions hold for the lower layer.

**4. Ordinary and fractional optima for nonzero twist.** Every direction covers at most \(m\) vertices, all in one layer. Each layer therefore requires at least \(\lceil n/m\rceil\) ordinary directions and total fractional weight at least \(n/m\). A partition of each cyclic layer into \(\lceil n/m\rceil\) consecutive blocks of at most \(m\) vertices, using (4), gives the matching ordinary upper bound. For the fractional upper bound, take all \(n\) cyclic shifts of an \(m\)-vertex block direction in each layer, each with weight \(1/m\). Every vertex belongs to exactly \(m\) of the blocks in its layer; the total weight is \(2n/m\). These covers illuminate all boundary faces because vertex coverage suffices.

**5. Aligned endpoint.** At \(t=0\), the body is the Cartesian product of a regular \(n\)-gon and a segment. A direction illuminating a top or bottom vertex has a fixed sign of its vertical component and must illuminate that vertex in the planar polygon under its horizontal projection. Consecutive polygon vertices have an illumination direction if and only if their incident edge-normal angular span is strictly smaller than \(\pi\). An illuminated set therefore has at most \(q=\lfloor(n-1)/2\rfloor\) vertices, and each consecutive \(q\)-vertex block can be illuminated. The same capacity, partition and cyclic-weight arguments as in Step 4, independently in the two layers, give the claimed endpoint formulas. Rotations by integer multiples of \(\theta\) simply relabel vertices, completing the classification.

## Verification
The standalone standard-library script `verify.py` reconstructs the listed side and base planes, checks their supporting incidences against every vertex, evaluates the explicit block directions at all active facets, verifies that cyclic block weights cover every vertex exactly, and checks the odd-index antiparallel obstruction. Its tested range is \(3\le n\le32\), three interior twist ratios, and two positive heights. A successful run outputs `VERIFY_OK cases=180 checked_planes=6660 vertices=6300 ordinary_directions=900`. The proof above, not this finite test, supplies the all-integer and all-real-parameter conclusions.

## Relationship to prior work
Naszódi introduced fractional illumination and its weighted definition in 2009. Gorodzha established a general upper bound with its equality characterization in a preprint first submitted 20 September 2026; neither general statement supplies the present exact incidence and parity formulas. Arman, Kaire and Prymak established a six-direction upper bound for three-dimensional cap bodies in a 2025 preprint, a different class. Known results for uniform antiprisms or the half-step rotation do not give the full open twist interval or its discontinuity at alignment. An X-ray number is an undirected-line invariant and does not determine these directed ordinary and fractional illumination numbers.

## Limitations
The claim concerns congruent, coaxial regular polygon bases with a common circumradius; different radii, translations, nonregular bases, or higher-dimensional analogues are not considered. It does not classify optimizer rigidity or quantitative illumination. Novelty is assessed against inspected sources and searchable records, not certified by an exhaustive historical literature census. An inaccessible study phrased in terms of generic antiprism realization spaces could potentially overlap and warrants later independent priority review. Independent scientific audit has not been performed.

## References
- M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4(2) (2009), 83–88, https://doi.org/10.55016/ojs/cdm.v4i2.62022.
- Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913, first submitted 20 September 2026, https://arxiv.org/abs/2609.23913.
- A. Arman, J. S. Kaire and A. Prymak, *Illumination number of 3-dimensional cap bodies*, arXiv:2507.08712, first submitted 11 July 2025, https://arxiv.org/abs/2507.08712.
