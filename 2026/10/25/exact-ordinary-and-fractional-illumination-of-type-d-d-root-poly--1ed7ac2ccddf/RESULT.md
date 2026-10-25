# Exact ordinary and fractional illumination of type-\(D_d\) root polytopes

## Finding
For each integer \(d\ge4\), consider the full-dimensional, centrally symmetric convex polytope
\[
P_d=\operatorname{conv}\{\sigma e_i+\tau e_j:\ 1\le i<j\le d,\ \sigma,\tau\in\{-1,1\}\}\subset\mathbb R^d.
\]
Its ordinary and fractional illumination numbers satisfy the **exact simultaneous identities**
\[
\boxed{I(P_d)=I^*(P_d)=2d.}
\]
Every illumination direction reaches at most \(d-1\) of the \(2d(d-1)\) vertices. There is an explicit collection of \(2d\) directions that partitions the vertices into pairwise disjoint illuminated classes of cardinality \(d-1\). For \(d=4\), this gives \(I(P_4)=I^*(P_4)=8\) for the regular \(24\)-cell. The three-dimensional cuboctahedron is exceptional: \(I(P_3)=I^*(P_3)=4\), consistent with its previously published four-source construction.

## Assumptions and scope
Write \(e_1,\ldots,e_d\) for the standard basis. A vector \(u\ne0\) *illuminates* \(x\in\partial P_d\) if some \(\varepsilon>0\) satisfies \(x+\varepsilon u\in\operatorname{int}P_d\). The ordinary illumination number \(I(P_d)\) is the smallest cardinality of a finite set of illuminating vectors covering every boundary point. The fractional illumination number \(I^*(P_d)\) is the infimum of \(\sum_s w_s\) over finite families \((u_s,w_s)\) with \(w_s\ge0\) and \(\sum_{s:\,u_s\text{ illuminates }x}w_s\ge1\) for each \(x\in\partial P_d\). Only real parallel directions are considered; no illumination costs based on distance from an external point are charged. These definitions agree with the standard finite weighted-direction model of fractional illumination.

The polytope is equivalently
\[
P_d=\{x\in[-1,1]^d:\ \textstyle\sum_{k=1}^d|x_k|\le2\}.
\]
Indeed, in each closed orthant the right-hand side is the signed image of \(\{y:0\le y_k\le1,\sum_k y_k\le2\}\), whose vertices are \(0\)-\(1\) vectors supported on at most two coordinates. The zero vector and each signed coordinate vector are convex combinations of the two-coordinate roots. Conversely the roots satisfy all the inequalities. Each root is a vertex: its two nonzero signed coordinate equations force the remaining coordinates to vanish.

## Proof
**1. Exact vertex-illumination criterion.** The complete inequality description comprises the \(2d\) coordinate inequalities \(\pm x_k\le1\) and the \(2^d\) sign inequalities \(\sum_k\epsilon_k x_k\le2\), indexed by \(\epsilon\in\{-1,1\}^d\). At \(v=\sigma e_i+\tau e_j\), the active inequalities are \(\sigma x_i\le1\), \(\tau x_j\le1\), and all sign inequalities with \(\epsilon_i=\sigma\), \(\epsilon_j=\tau\). A direction illuminates a vertex precisely when its scalar product with every active outer normal is strictly negative. Thus, if \(a_k=|u_k|\) and \(S=\sum_k a_k\), illumination of \(v\) is equivalent to
\[
\sigma u_i<0,\quad\tau u_j<0,\quad
-a_i-a_j+\sum_{k\notin\{i,j\}}a_k<0.
\]
The last inequality is \(2(a_i+a_j)>S\). For each unordered coordinate pair \(\{i,j\}\), the first two inequalities uniquely determine the signs \(\sigma,\tau\) of any illuminated root; zero coordinates illuminate none of the corresponding roots. Therefore one direction reaches at most one vertex from each pair, and the pairs reached are exactly those with nonzero coordinate magnitudes satisfying \(2(a_i+a_j)>S\).

**2. Intersecting-edge bound.** Two disjoint coordinate pairs cannot both satisfy the strict inequality: their four magnitudes would have sum exceeding \(S\). Hence the reached pairs form a pairwise-intersecting family of edges of the complete graph on \(d\) vertices. An intersecting family of graph edges is either contained in a star or contained in the three edges of a triangle. To prove the latter elementary fact, choose meeting edges \(ab,ac\). Any edge missing \(a\) must be \(bc\), and then no edge containing \(a\) except \(ab,ac\) can intersect it. Thus a direction illuminates at most \(\max\{d-1,3\}=d-1\) vertices for \(d\ge4\).

**3. Fractional lower bound.** There are \(N=4\binom d2=2d(d-1)\) vertices. In any finite weighted illumination family, sum the vertex constraints over all \(N\) vertices. Each direction contributes its weight at most \(d-1\) times, so
\[
N\le\sum_s w_s\#\{\text{vertices illuminated by }u_s\}
\le(d-1)\sum_s w_s.
\]
Therefore \(I^*(P_d)\ge2d\). The same bound on ordinary illumination follows either directly or because \(I^*(P_d)\le I(P_d)\).

**4. An exact vertex partition using \(2d\) directions.** For each center index \(i\in\{1,\ldots,d\}\), choose a vector \(u^{(i)}\) having coordinate magnitude \(d\) at \(i\), coordinate magnitude \(1\) everywhere else, and signs
\[
\operatorname{sgn}(u^{(i)}_k)=
\begin{cases}+1&k\ge i,\\-1&k<i.\end{cases}
\]
Use the \(2d\) directions \(u^{(i)}\) and \(-u^{(i)}\). For each of them, \(S=2d-1\), and the strict pair condition holds exactly for coordinate pairs incident with \(i\): \(2(d+1)>2d-1\) while \(2(1+1)<2d-1\) for \(d\ge4\). Hence each direction illuminates exactly \(d-1\) roots. For an unordered pair \(i<j\), the directions centered at \(i\) and their negatives illuminate the two roots with equal coordinate signs, while those centered at \(j\) and their negatives illuminate the two roots with opposite coordinate signs. Consequently all four signed roots for \(\{i,j\}\) are illuminated **exactly once**, and the selected directions partition the full vertex set.

**5. Extending to the entire boundary.** Let \(x\) lie in the relative interior of a proper face \(F\) of the polytope, and take any vertex \(v\) of \(F\). Every inequality active at \(x\) is also active at \(v\). Thus any direction strictly decreasing all inequalities active at \(v\) does so for \(x\), hence illuminates \(x\). Lighting every vertex suffices to light every boundary point. The explicit \(2d\) directions therefore give \(I(P_d)\le2d\) and \(I^*(P_d)\le2d\), proving equality.

**6. The excluded three-dimensional endpoint.** When \(d=3\), each direction can illuminate at most three vertices; there are twelve vertices. Four equal-magnitude directions with sign triples \((+,+,+),(+,-,-),(-,+,-),(-,-,+)\) partition the twelve roots into illuminated triples. Hence \(I(P_3)=I^*(P_3)=4\). This case is presented as a consistency and boundary check, not as the new main theorem.

## Verification
The standalone, dependency-free exact-integer program `verify.py` constructs all signed roots, both classes of defining inequalities, and the explicit direction collections. It verifies the direct active-facet test, the derived pair criterion, and exact-once vertex coverage for dimensions \(3\) through \(8\). It separately checks \(5,440\) magnitude profiles in dimensions \(3\) through \(6\), comparing the heavy-pair criterion with the intersecting-edge size bound. The reproducible command is `python3 verify.py`. Its final output is `EXACT_OK dimensions=3..8 incidence_checks=4328 magnitude_profiles=5440`. These finite checks corroborate the displayed formulas; the dimension-free proof is in the preceding five steps. The checker does not enumerate all real illumination directions.

## Relationship to prior work
Gorodzha (September 20, 2026) provides recent motivation by developing sharp universal fractional-illumination bounds; the exact value for the present root-polytope family is not among the stated results. Naszódi established the finite weighted-direction viewpoint earlier. Kiss and Oloff de Wet (2012) provide a four-source upper bound for the cuboctahedron, which explains why the dimension-three endpoint is not offered as a new example.

The closest same-object published mathematical note, *Exact quantitative illumination of type-\(D_d\) root polytopes* (October 2026), proves that the **quantitative** point-source cost is \(2d(d-1)\), and derives a related intersecting-edge restriction using additional source-distance inequalities. That result is credited for the shared heavy-pair geometry. Its optimization objective is \(\inf\sum\|\ell\|_{P_d}\) over external point sources; it neither states nor gives the \(2d\)-direction partition above, and its stated quantitative value does not itself determine ordinary or fractional *directional* illumination. Other nearby published results concern polar root polytopes, Cartesian products, or Euclidean projection brightness rather than these two exact invariants. Database searches and primary-text comparisons are not a proof of historical novelty.

## Limitations
The main formula covers \(d\ge4\); the distinguished \(d=3\) case has its separate value. No rigidity or uniqueness of optimal direction families is asserted, and this result does not evaluate the quantitative point-source-cost invariant. Its mathematical proof is self-contained, but historical priority against unpublished or poorly indexed literature is not guaranteed. The computational checks are finite corroboration only, and no independent expert verification is claimed.

## References
1. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913v1 (public September 20, 2026). https://arxiv.org/abs/2609.23913 .
2. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics 4 (2009), 83–88, DOI: 10.55016/ojs/cdm.v4i2.62022. https://cdm.ucalgary.ca/article/view/62022 .
3. G. Kiss and P. Oloff de Wet, *Notes on the illumination parameters of convex polytopes*, Contributions to Discrete Mathematics 7 (2012), 58–67, DOI: 10.55016/ojs/cdm.v7i1.62108. https://cdm.ucalgary.ca/article/view/62108 .
4. *Exact quantitative illumination of type-\(D_d\) root polytopes*, publicly archived mathematical note (October 11, 2026), record identifier `34479eff57ed` in the 2026 published-finding corpus research collection. Different quantitative objective, same polytope family.
