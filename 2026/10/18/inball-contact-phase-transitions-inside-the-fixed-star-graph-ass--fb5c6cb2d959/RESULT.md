# Inball-contact phase transitions inside the fixed star graph-associahedron fan

## Finding
Let \(k\ge3\) and let \(e_0,\ldots,e_k\) be the standard basis of \(\mathbb R^{k+1}\). For any nonnegative cardinality weights with \(w_1>0\), put
\[
P_k(w)=\sum_{\varnothing\ne B\subseteq[k]}w_{|B|}\operatorname{conv}\{e_0,e_i:i\in B\},\qquad
T=\sum_{j=1}^k\binom kjw_j.
\]
Distances are intrinsic Euclidean distances in \(\sum_{i=0}^k x_i=T\). With \(d=\sqrt{k/(k+1)}\), define, for \(1\le u\le k\),
\[
A_u=\sum_{j=1}^kw_j\left(\binom kj-\binom{k-u}j\right),\qquad
D_u=ud+\sqrt{\frac{u(k-u+1)}{k+1}},
\]
using \(\binom ab=0\) for \(b>a\). The exact inradius and unique incenter are
\[
\boxed{\rho_k(w)=\min_{1\le u\le k}\frac{A_u}{D_u}},\qquad
\boxed{c=(T-kd\rho_k(w),d\rho_k(w),\ldots,d\rho_k(w))}.
\tag{1}
\]

In the **two-cardinality family** \(w_1=a>0\), \(w_2=b>0\), \(w_j=0\) for \(j\ge3\), every member has **the same normal fan** (that of the star graph associahedron), but its unique inball has a sharp contact transition:
\[
\boxed{\rho_k(a,b)=\min\left\{
\frac{a+(k-1)b}{2}\sqrt{\frac{k+1}{k}},
\frac{ka+\binom{k}{2}b}{\sqrt{k(k+1)}}\right\}.}
\tag{2}
\]
For \(a>b\), exactly \(2k\) facets touch the inball: the \(k\) leaf-coordinate lower facets and the \(k\) leaf-coordinate upper facets. For \(a=b\), precisely these \(2k\) facets plus the hub-coordinate lower facet touch (\(2k+1\) contacts). For \(a<b\), precisely the \(k+1\) coordinate lower facets touch. In all cases every intermediate subset-upper facet lies strictly beyond the inball.

As a consequence, write \(Q_{K_{1,k},m}\) for the canonical Pešović–Stojadinović \(m\)-graph polytope of the \(k\)-leaf star, ignoring its common singleton translation. If \(T_m=\sum_{j=1}^m\binom kj\), then
\[
\boxed{\rho(Q_{K_{1,k},1})=\frac12\sqrt{\frac{k+1}{k}},\qquad
\rho(Q_{K_{1,k},m})=\frac{T_m}{\sqrt{k(k+1)}}\quad(2\le m\le k).}
\tag{3}
\]
The number of contacting facets is \(2k\) at \(m=1\), \(2k+1\) at \(m=2\), and \(k+1\) at **every** \(3\le m\le k\). Crucially, \(Q_{K_{1,k},2}\) and all later members have the same normal fan and the same \(2^k+k-1\) facets: the second contact transition is purely Euclidean, not combinatorial. In (3) the incenter is unique for every \(m\).

## Assumptions and scope
All simplices are unscaled standard coordinate simplices multiplied by the stated real coefficients. The affine hyperplane carries the metric induced from \(\mathbb R^{k+1}\); deleting the hub coordinate without retaining its Gram correction changes the metric. The star has one labeled hub \(0\) and \(k\) labeled leaves. The original \(m\)-graph construction also sums singleton simplices, but these merely translate the polytope and do not affect its radii or tangent-facet counts. The case \(k=2\) has a degenerate five-gon endpoint contact pattern; the phase statement assumes \(k\ge3\).

For \(w_1,w_2>0\), every leaf lower inequality and every nonempty leaf-subset upper inequality below defines a facet. If higher weights are present without positive pair weight, equation (1) still holds but the facet census is not asserted.

## Proof
**1. An exact halfspace description.** Project away the hub coordinate, writing the leaf coordinates as \(y=(x_1,\ldots,x_k)\). The simplex on \(\{0\}\cup B\) projects to \(\operatorname{conv}(0,e_i:i\in B)\), so the projected polytope is the independent-set polymatroid
\[
y_i\ge0\quad(i\in[k]),\qquad
\sum_{i\in U}y_i\le A_{|U|}\quad(\varnothing\ne U\subseteq[k]).
\tag{4}
\]
Indeed its rank is \(f(U)=\sum_{B:B\cap U\ne\varnothing}w_{|B|}=A_{|U|}\). To see that (4) is exhaustive rather than merely necessary, maximize a generic objective: the simplex sum contributes \(w_{|B|}\max(0,\max_{i\in B}\theta_i)\), exactly the greedy support of the nonnegative monotone submodular rank \(f\). Thus the two convex bodies have identical support functions. Recover \(x_0=T-\sum_i y_i\).

For positive \(w_1,w_2\), each displayed inequality defines a facet. On an upper face for \(U\), pair-simplex summands contained in \(U\) span all differences among coordinates of \(U\), giving \(|U|-1\) affine directions, while positive edge-simplex summands outside \(U\) give \(k-|U|\) independent directions among complementary leaves and the hub (and for \(U=[k]\) only the first group is needed). The total rank is \(k-1\). On \(y_i=0\), the other \(k-1\) leaf-edge summands supply independent face directions. Hence there are exactly \(k+(2^k-1)=2^k+k-1\) facets.

**2. Radius and uniqueness.** The projected intrinsic normal of \(x_i=0\) has length \(d=\sqrt{k/(k+1)}\). The projected normal of \(x(U)=A_u\), \(|U|=u\), has length
\[
\nu_u=\sqrt{\frac{u(k-u+1)}{k+1}}.
\]
A ball of intrinsic radius \(r\) centered at leaf coordinates \(z_i\) therefore satisfies
\[
z_i\ge rd\quad(i\in[k]),\qquad
\sum_{i\in U}z_i+r\nu_u\le A_u\quad(|U|=u).
\tag{5}
\]
Summing the first inequality over any \(U\) yields \(r(ud+\nu_u)\le A_u\), so \(r\le\min_u A_u/D_u\). Conversely, setting every leaf coordinate to \(rd\) for this minimum satisfies (5), proving (1). If another center attained the same radius, take any minimizing cardinality \(u\); for every \(U\) of this size its upper bound in (5) is \(\sum_{i\in U}z_i\le u rd\), while all \(z_i\ge rd\). Every leaf occurs in some such \(U\), forcing every \(z_i=rd\); hence the incenter is unique.

**3. Two-cardinality sharpness.** For weights \((a,b)\),
\[
A_u=ua+\frac{u(2k-u-1)}2 b,\quad
A_1=a+(k-1)b,\quad A_k=ka+\binom k2b.
\tag{6}
\]
The endpoint denominators are \(D_1=2d\) and \(D_k=\sqrt{k(k+1)}\). To prove no intermediate cardinality improves either endpoint, consider three coefficient rays.

For \((a,b)=(1,1)\), put \(z=u(k-u+1)/k\). The bound \(A_u\ge(D_u/D_k)A_k\) simplifies exactly to \(z\ge\sqrt z\). Since
\[
z-1=\frac{(u-1)(k-u)}{k}\ge0,
\]
equality occurs only at \(u=1,k\).

For the pure edge ray \((a,b)=(1,0)\),
\[
\frac{A_u}{D_u}=\frac{1}{d+\sqrt{(k-u+1)/(u(k+1))}},
\]
which increases strictly with \(u\), so the unique minimizing cardinality is \(u=1\).

For the pure pair ray \((a,b)=(0,1)\), normalize \(A_u\) by \(T=\binom k2\). It equals the probability that a uniform two-subset of \([k]\) intersects \(U\). This strictly exceeds the corresponding normalized rank of the \((1,1)\) mixture for every proper nonempty \(U\), since the probability of intersection increases strictly from a uniform singleton to a uniform pair; both probabilities are \(1\) at \(U=[k]\). The established \((1,1)\) inequality therefore implies \(A_u/D_u>A_k/D_k\) for every \(u<k\) on the pure pair ray.

If \(a\ge b\), express \((a,b)=b(1,1)+(a-b)(1,0)\) and combine these linear inequalities to deduce that \(u=1\) minimizes; if \(b\ge a\), express \((a,b)=a(1,1)+(b-a)(0,1)\), deducing that \(u=k\) minimizes. Strictness gives exactly the equality pattern in (2). All leaf-lower facets are always tangent. The upper facets are tangent precisely for the minimizing cardinalities, establishing all three contact counts. The displayed formulas for the unique centers follow from (1).

**4. The canonical cutoff after the fan stabilizes.** For \(m=1\), only edges occur, so the edge-ray calculation gives the first formula in (3), and only the \(2k\) coordinate facets exist. For \(m=2\), \((a,b)=(1,1)\) gives the second formula with \(T_2=k+\binom k2\), together with \(2k+1\) contacts. For \(m\ge3\), let
\[
p_j(u)=1-\frac{\binom{k-u}j}{\binom kj}
\]
be the chance that a uniformly random \(j\)-subset intersects a fixed \(u\)-subset. For \(1\le u<k\), these probabilities are nondecreasing in \(j\), and \(p_2(u)>p_1(u)\). Consequently \(p_j(u)\) for every \(j\ge3\) strictly exceeds the average of \(p_1(u),p_2(u)\), with weights \(\binom k1,\binom k2\). Adding size-\(3\)-and-larger strata therefore strictly increases \(A_u/T_m\) compared with \(A_u^{(2)}/T_2\) for all \(u<k\); at \(u=k\) the normalized value remains \(1\). Since the \(m=2\) candidate at \(u=k\) was already globally minimal, this forces \(u=k\) to be the unique minimizer for every \(m\ge3\), proving (3) and its contacts.

Lastly, the normal fan does not change for any positive \(a,b\), nor when nonnegative higher-cardinality simplex summands are added. In a generic objective, the summands on \(\{0,i\}\) determine whether leaf \(i\) ranks above the hub; those on \(\{0,i,j\}\) determine the relative order of all leaves ranked above the hub. Together they determine the maximizing vertex of **every** \(\Delta_{\{0\}\cup B}\). Thus the common refinement of the edge and pair simplex fans already refines all higher simplex fans. Changing their positive coefficients cannot alter this common refinement, so the normal fan of every \(m\ge2\) member is identical, while the inball contact count changes between \(m=2\) and \(m=3\).

## Verification
The accompanying `verify_star_inballs.py` independently constructs vertices by summing individual simplex maximizers over all strict coordinate orders, rather than evaluating the asserted inradius formula. It then checks upper support values against these vertices, computes affine ranks of the equality faces, and checks all intrinsic facet distances and contact counts. It passes 35 exact-integer support/facet scenarios: all cutoffs for star orders \(k=2,\ldots,6\) and five distinct positive integer weight pairs in each of \(k=3,4,5\). Integer support and affine rank are checked before floating-point intrinsic-distance comparisons. Run `python3 verify_star_inballs.py` with Python 3 and NumPy installed; success prints `VERIFY_OK`.

The arbitrary-\(k\) proof is analytical. These finite checks do not establish any unrestricted statement by enumeration and do not address cases outside the explicit hypotheses.

## Relationship to prior work
Pešović and Stojadinović define the \(m\)-graph polytopes as simplex sums over connected induced vertex subsets of bounded size, and analyze enumerators, normal fans and graph-associahedral interpolation (arXiv:2209.12053v1, Definition 2.1 and Example 3.6). Their graph-combinatorial stabilization for the star at the second step is a starting point, not the metric contact transition established here.

For the final unweighted stellohedron endpoint, an earlier published record gives the Euclidean inradius \((2^k-1)/\sqrt{k(k+1)}\), unique uniform center, and \(k+1\) contacting singleton facets. That endpoint is **already known**, and is not asserted to be a novel special case. A second published record gives the ambient Euclidean **diameter** and diametral endpoints of the same cardinality-weighted star simplex-sum family; diameter extremizers do not determine the largest inscribed ball or the contact-facet transition. A third published record gives the Euclidean inradius of projected partial permutohedra in the **leaf-coordinate metric**, which is not the intrinsic lifted metric here: after eliminating the hub the metric tensor is \(I+\mathbf1\mathbf1^{\mathsf T}\), so projection is not an isometry. The weighted transition at \(a=b\) and the exact contact jump between the fan-identical \(m=2\) and \(m=3\) objects are not derived from these results.

Behrend's full text (arXiv:2403.06975v1, Section 2(v) and Section 3) supplies the partial-permutohedron simplex decomposition and establishes the relevant lifted-versus-projected distinction, but studies Ehrhart theory and combinatorics, not these intrinsic inspheres. The possibility of an equivalent general polymatroid or Chebyshev-center theorem under different terminology remains a bibliographic risk.

## Limitations
The weight-phase statement assumes \(k\ge3\), positive edge and pair coefficients, and the canonical intrinsic Euclidean metric. It does not claim a phase diagram for arbitrary unrelated simplex coefficients or for all graphs. Formula (1) holds for cardinality weights with positive edge weight and nonnegative remaining weights; the full facet count is asserted only when pair weights are positive. For \(m=k\), the scalar inradius and its contacts are already known; novelty is restricted to the parameterized interpolation and sharp contact transition inside the unchanged normal fan. Originality is assessed against available primary literature and published records, not proved by the absence of a search result.

## References
1. Marko Pešović and Tanja Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053v1, first public 2022-09-24, especially Definition 2.1 and Example 3.6. https://arxiv.org/abs/2209.12053.
2. Roger E. Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975v1, first public 2024-03-11, especially Section 2(v). https://arxiv.org/abs/2403.06975.
3. *Exact Euclidean inradius and unique uniform incenter of the standard stellohedron*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-euclidean-inradius-and-unique-uniform-incenter-of-the-stan--725a5078e7c3.
4. *Diametral rigidity of cardinality-weighted star hypergraphic polytopes*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-diametral-rigidity-of-cardinality-weighted-star-hypergraphic-pol--fc74a3f40add.
5. *Exact Euclidean inradius of partial permutohedra*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-euclidean-inradius-of-partial-permutohedra--df8bf5a2a297.
