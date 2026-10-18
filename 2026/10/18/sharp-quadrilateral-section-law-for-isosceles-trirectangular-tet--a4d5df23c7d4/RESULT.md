# Sharp quadrilateral-section law for isosceles trirectangular tetrahedra

## Finding

Let \(T_t=\operatorname{conv}\{(0,0,0),(1,0,0),(0,1,0),(0,0,t)\}\) for \(t>0\). Sample an unoriented affine plane with the Euclidean-motion-invariant measure, conditioned on meeting the interior of \(T_t\). Let \(N_t\) count the vertices of its intersection polygon. Almost surely \(N_t\in\{3,4\}\).

Set
\[
 z=\sqrt{1+t^2},\qquad A=\arctan\frac{t}{z},\qquad B=\arctan\frac{1}{\sqrt2\,t},
 \qquad L=2+t+2z+\sqrt2,\qquad D=2zA+\sqrt2 B.
\]
Then the *complete* probability law is
\[
 \Pr(N_t=4)=P(t)=\frac{4}{1+2D/(\pi L)}-3,
 \qquad \Pr(N_t=3)=1-P(t).
\]
The function \(P\) is strictly increasing on \((0,1)\), strictly decreasing on \((1,\infty)\), and has its unique maximum at the equal-leg cube-corner tetrahedron \(t=1\):
\[
 P(1)=\frac{4}{1+\frac{2(2-\sqrt2)}{\pi}\arctan(1/\sqrt2)}-3
 =0.25328442627564\ldots.
\]
The limiting probabilities are
\[
 \lim_{t\downarrow0}P(t)=3-2\sqrt2,
 \qquad \lim_{t\to\infty}P(t)=0.
\]
Consequently \(P((0,\infty))=(0,P(1)]\). For each probability \(q\in(3-2\sqrt2,P(1))\), there are *exactly two* non-similar members of this family whose random affine-plane sections are quadrilateral with probability \(q\); for \(0<q\le3-2\sqrt2\) there is exactly one, and at \(q=P(1)\) there is exactly one.

## Assumptions and scope

This is a nondegenerate Euclidean tetrahedron for every \(t>0\); two of its mutually perpendicular edges at the origin have equal length one, and the third has length \(t\). Similarity allows fixing the equal pair to one. Planes are sampled by the invariant measure \(d\sigma(u)\,ds\) on unit normals \(u\in S^2\) and offsets \(s\in\mathbb R\), with the two opposite orientations identified; the overall constant cancels on conditioning. In particular, the normal is **not** Haar-uniform after conditioning: its conditional density is proportional to the directional width. Exceptional supporting planes and planes through vertices have zero probability. This is not the distribution of a uniformly oriented central section or a random orthogonal shadow.

## Proof

**1. Crofton counting identity.** Let \(Q\subset\mathbb R^3\) be an arbitrary nondegenerate convex tetrahedron. Write \(\ell_e\) for its six edge lengths, \(\theta_e\in(0,\pi)\) for the *exterior* dihedral angles (angles between outward unit facet normals), and \(w_Q(u)\) for its directional width. A generic intersecting plane cuts either three or four edges, and these crossings are exactly the vertices of the section polygon. For each fixed normal \(u\), integration over offsets gives
\[
 \int_{\mathbb R}N_Q(u,s)\,ds
 =\sum_{e=[v,w]}|u\cdot(v-w)|.
\]
Because \(\int_{S^2}|u\cdot v|\,d\sigma(u)=2\pi\|v\|\), the integrated vertex count is \(2\pi\sum_e\ell_e\). The integrated mass of all intersecting planes is \(\int_{S^2}w_Q(u)d\sigma(u)=\sum_e\ell_e\theta_e\), the standard polyhedral mean-width identity (equivalently the edge term in the Steiner parallel-volume formula). Thus
\[
 \mathbb E[N_Q]
 =\frac{2\pi\sum_e\ell_e}{\sum_e\ell_e\theta_e},
 \qquad
 \Pr(N_Q=4)=\mathbb E[N_Q]-3.
\]
The exterior, rather than interior, dihedral angle is required; this normalization is also checked by a unit cube, whose integrated mean width is \(6\pi\).

**2. The six edges of the cube-corner tetrahedron.** Three edges from the origin have lengths \(1,1,t\) and exterior dihedral angle \(\pi/2\). The other three have lengths \(z,z,\sqrt2\). The sloped face has outward normal parallel to \((1,1,1/t)\). Its exterior angles with the adjacent coordinate faces are \(\pi/2+A\), \(\pi/2+A\), and \(\pi/2+B\), respectively, since
\[
 A=\arcsin\frac{t}{\sqrt{1+2t^2}}=\arctan\frac{t}{\sqrt{1+t^2}},
 \qquad B=\arcsin\frac1{\sqrt{1+2t^2}}=\arctan\frac1{\sqrt2 t}.
\]
Therefore \(\sum_e\ell_e=L\) and \(\sum_e\ell_e\theta_e=(\pi/2)L+D\). The formula for \(P(t)\) follows from step 1.

**3. Exact one-crossing derivative proof.** We must minimize \(R(t)=D/L\), because \(P\) is strictly decreasing as a function of \(R\). Differentiation yields the cancellation
\[
 A'=\frac1{z(1+2t^2)},\quad
 B'=-\frac{\sqrt2}{1+2t^2},\quad
 D'=\frac{2t}{z}A,\quad L'=1+\frac{2t}{z}.
\]
A direct rearrangement gives
\[
 zL^2R'(t)
 =2\bigl((2+\sqrt2)t-1\bigr)A
 -\sqrt2(z+2t)B.
\]
When \(0<t\le(2+\sqrt2)^{-1}\), this is negative. For larger \(t\), its sign is that of \(A/B-G(t)\), where
\[
 G(t)=\frac{\sqrt2(z+2t)}{2((2+\sqrt2)t-1)}.
\]
Here \(A/B\) is strictly increasing because \(A'>0\) and \(B'<0\), whereas \(G\) is strictly decreasing: its derivative has the sign of
\[
 (t/z+2)((2+\sqrt2)t-1)-(2+\sqrt2)(z+2t)
 =-\frac{2+\sqrt2+t}{z}-2<0.
\]
At \(t=1\), \(A=B=\arctan(1/\sqrt2)\) and \(G(1)=1\). Hence \(R'(t)<0\) for all \(t<1\), and \(R'(t)>0\) for all \(t>1\). The desired strict increase/decrease of \(P\), and its unique global maximizer, follow.

**4. Boundaries and inverse multiplicities.** As \(t\downarrow0\), \(z\to1\), \(A\to0\), \(B\to\pi/2\), so \(D/L\to\pi/(4\sqrt2+2)\), giving \(P\to3-2\sqrt2\). As \(t\to\infty\), \(z/t\to1\), \(A\to\pi/4\), \(B\to0\), and \(D/L\to\pi/6\), so \(P\to0\). Monotonicity and continuity give the range and exact numbers of preimages for each probability. Distinct positive parameters \(t\) give non-similar tetrahedra: the unique triple-right vertex has leg-length multiset \(\{1,1,t\}\), determining \(t\) up to common scale and permutation.

## Verification

The accompanying independent numerical quadrature program `check_profile.py` integrates edge crossings and widths directly over \(30{,}000\) evenly spread directions per shape for five aspect ratios, without using the dihedral-angle formula inside the quadrature. It additionally compares finite-difference derivatives with the proved monotonicity and checks both degenerate limits. Expected successful terminator: `TETRA_CROFTON_PROFILE_CHECK_OK`. The continuum assertion rests on the proof above, not on the finite checks.

## Relationship to prior work

Korotov and Křížek establish sharp bounds on the **unweighted sum of interior dihedral angles** of various tetrahedra and specifically note that this sum for a trirectangular cube-corner tetrahedron is minimized at equal legs [1, Section 3, Remark 3]. That does not give the length-weighted *exterior* angle ratio governing invariant-plane section probabilities; the present theorem determines that ratio on a natural one-parameter family and its strict optimum.

Birkemeyer, Brose, Brandenburg and Prün classify possible combinatorial slices of pyramids and study reconstruction from directional section counts [2, Sections 3–4]. They do not compute or optimize this invariant-plane quadrilateral probability. Feldman and Klain [3] compute probabilities for **orthogonal projections**, not affine sections, so their angle measure is not the measure used here. Finch [4] treats widths of **regular** polyhedra, rather than the aspect-ratio dependence of random sections of right-angled tetrahedra.

## Limitations

This covers the one-parameter family having two equal perpendicular legs, not all trirectangular tetrahedra or all tetrahedra. The extension to three independently varying legs is not proved. Similarity-class nonidentifiability is only for the scalar polygon-type probability, not for the full direction-and-offset section-count function. The mean-width identity and the tetrahedral three-or-four section dichotomy are prior geometric facts. No assertion of independent audit or exhaustiveness of historical priority is made; older stereological literature may contain equivalent special cases.

## References

[1] S. Korotov and M. Křížek, *Two-sided bounds for dihedral angle sums of path and 4-ball tetrahedra*, arXiv:2601.08304, first public version January 13, 2026, especially Section 3, Remark 3. https://arxiv.org/abs/2601.08304

[2] A. Birkemeyer, A. E. Brose, M.-C. Brandenburg and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, first public version September 14, 2026, Sections 3–4. https://arxiv.org/abs/2609.16195

[3] D. V. Feldman and D. A. Klain, *Angles as probabilities*, arXiv:0809.3459, 2008, Theorem 1. https://arxiv.org/abs/0809.3459

[4] S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, 2011, Section 3. https://arxiv.org/abs/1110.0671
