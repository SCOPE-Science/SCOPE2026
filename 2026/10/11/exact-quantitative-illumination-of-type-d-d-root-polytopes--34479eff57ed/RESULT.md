# Exact quantitative illumination of type-\(D_d\) root polytopes

## Finding
For every integer \(d\ge 3\), let
\[
P_d=\operatorname{conv}\{\sigma e_i+\tau e_j:\ 1\le i<j\le d,\ \sigma,\tau\in\{-1,1\}\}\subset\mathbb R^d,
\]
where \(e_i\) are the standard coordinate vectors. The **quantitative illumination parameter** of this centrally symmetric polytope is exactly
\[
\boxed{\mathcal I(P_d)=2d(d-1)=\#\operatorname{vert}(P_d).}
\]
More strongly, every exterior point source \(\ell\) which illuminates exactly \(k\ge 1\) vertices satisfies the sharp efficiency obstruction
\[
\boxed{\|\ell\|_{P_d}>k.}
\]
Here \(\|\cdot\|_{P_d}\) is the Minkowski gauge of \(P_d\). In particular, the regular cuboctahedron has quantitative illumination parameter \(12\), completing the lower bound missing from the published \(12\)-upper estimate, and the regular four-dimensional \(24\)-cell has parameter \(24\). The value is unchanged under invertible linear transformations.

## Assumptions and scope
A source \(\ell\in\mathbb R^d\setminus P_d\) **illuminates** a boundary point \(v\in\partial P_d\) when \(v+t(v-\ell)\in\operatorname{int}P_d\) for some \(t>0\). A finite set of sources illuminates the body if every boundary point is illuminated by at least one source. The quantitative parameter is
\[
\mathcal I(P_d)=\inf_{\substack{L\subset\mathbb R^d\setminus P_d\\L\text{ finite, illuminating}}}\sum_{\ell\in L}\|\ell\|_{P_d}.
\]
For this specific polytope,
\[
P_d=\{x\in\mathbb R^d:\|x\|_\infty\le1,\ \|x\|_1\le2\},\qquad
\|x\|_{P_d}=\max\{\|x\|_\infty,\tfrac12\|x\|_1\}.
\]
The endpoint \(d=2\) is excluded from the root-system formulation; the theorem covers all dimensions \(d\ge3\) without regularity, smoothness, or genericity assumptions on sources.

## Proof
**1. Polytope and facets.** Every displayed root has infinity norm \(1\) and \(\ell_1\)-norm \(2\), hence the convex hull is contained in the intersection above. In a fixed orthant, the latter intersection is the signed image of \(\{y:\ 0\le y_i\le1,\ \sum_i y_i\le2\}\). Its vertices are precisely the \(0\)-\(1\) vectors with at most two nonzero coordinates: if two coordinates are fractional they admit an opposite perturbation when the sum constraint is active, while a single fractional coordinate is incompatible with an active *integer* sum; if the sum constraint is slack, any fractional coordinate can be perturbed. The origin and the signed coordinate vectors are convex combinations of the displayed roots. This proves the intersection description. Each root is an exposed vertex: imposing the two corresponding signed coordinate equalities forces all other coordinates to vanish. Therefore there are \(4\binom d2=2d(d-1)\) vertices.

The full halfspace description uses \(\pm x_i\le1\) and \(\sum_i\varepsilon_i x_i\le2\) for all sign vectors \(\varepsilon\in\{-1,1\}^d\). At a vertex \(v=\sigma e_i+\tau e_j\), exactly the two coordinate inequalities with signs \(\sigma,\tau\) and the sign-sum inequalities with \(\varepsilon_i=\sigma,\varepsilon_j=\tau\) are active. An exterior source illuminates a polyhedral vertex if and only if it lies strictly beyond *every* supporting hyperplane active there: this is exactly the condition that the ray beyond the vertex immediately enters the interior. Hence \(\ell\) illuminates \(v\) precisely when
\[
\sigma\ell_i>1,\quad\tau\ell_j>1,\quad
\sigma\ell_i+\tau\ell_j-\sum_{h\notin\{i,j\}}|\ell_h|>2.\tag{1}
\]

**2. Intersecting-edge reduction.** Put \(a_i=|\ell_i|\) and \(S=\sum_i a_i\). The signs of an illuminated root are forced to agree with the corresponding coordinates of \(\ell\), so at most one root from each unordered coordinate pair can be illuminated. By (1), a pair \(\{i,j\}\) can be illuminated only if
\[
a_i>1,\qquad a_j>1,\qquad 2(a_i+a_j)>S+2.\tag{2}
\]
If two such pairs were disjoint, adding their last inequalities would give \(a_i+a_j+a_k+a_h>S+2\), impossible because their sum is at most \(S\). Thus the illuminated pairs form a pairwise-intersecting family of edges of a complete graph. Every such nonempty family is either a star or the three edges of a triangle (the one-edge case is a star).

**3. Strict source-cost obstruction.** Suppose the illuminated edges are a star of size \(m\), with center \(c\) and neighbor set \(J\). For \(m=1\), (2) already gives \(\|\ell\|_{P_d}\ge a_c>1\). For \(m\ge2\), set \(B=\sum_{j\in J}a_j>m\) and \(T=\sum_{h\notin\{c\}\cup J}a_h\ge0\), so \(S=a_c+B+T\). Summing (2) over the star edges gives
\[
ma_c>(m-2)B+mT+2m,
\]
and therefore \(a_c>m\): this is immediate for \(m=2\), and for \(m>2\) follows from \(B>m\). Thus \(\|\ell\|_{P_d}\ge a_c>m\).

If instead the illuminated edges are the three edges of a triangle on \(i,j,k\), put \(B=a_i+a_j+a_k\) and \(T=S-B\ge0\). Summing the three inequalities (2) yields
\[
4B>3(B+T)+6,\quad\text{hence}\quad B>3T+6.
\]
Consequently \(\|\ell\|_{P_d}\ge S/2=(B+T)/2>3\). These cases exhaust all possible illuminated-vertex sets and establish \(\|\ell\|_{P_d}>k\) for every source illuminating \(k\ge1\) vertices. For \(k=0\), its positive gauge also exceeds \(k\).

**4. Global lower and upper bounds.** If \(L\) is a finite illuminating set, every vertex must be illuminated; therefore, writing \(k(\ell)\) for the number of vertices reached by \(\ell\),
\[
\sum_{\ell\in L}\|\ell\|_{P_d}>
\sum_{\ell\in L}k(\ell)\ge 2d(d-1).
\]
Conversely, for each vertex \(v\) choose \(\ell_v=(1+\epsilon)v\). This source illuminates \(v\), since \((1-\delta)v\) is interior for every sufficiently small \(\delta>0\). Lighting all vertices lights every face: a source illuminating a vertex of a face illuminates its relative interior because all supporting inequalities active on the face are active at the vertex. Thus the \(2d(d-1)\) sources illuminate the entire boundary and each has gauge \(1+\epsilon\). Let \(\epsilon\downarrow0\) to obtain \(\mathcal I(P_d)\le2d(d-1)\), completing the proof.

## Verification
The supplied standalone program `verify_root_illumination.py` independently enumerates all incident signed facet inequalities and checks their equivalence with (2). It exhaustively tests scaled rational source magnitudes from \(\{0,\tfrac12,1,\tfrac32,2,3,4\}\) in dimensions \(3\) through \(6\). Its reproducible command is `python3 verify_root_illumination.py`; the exact-arithmetic output is `EXACT_DIAGNOSTIC_OK cases=137200 illuminated_pairs=68296 max_single_source_count=3`. These finite cases are consistency checks, **not** the proof of the universal statement. The dimension-free deductions in Sections 1–4 provide that proof.

## Relationship to prior work
Kiss and de Wet's 2012 paper defines this quantitative parameter and gives \(12\) as an **upper estimate** for the cuboctahedron in Theorem 3.4; the authors explicitly state that they do not determine exact values for their listed Archimedean solids. The present result proves the corresponding lower bound and extends it to all type-\(D_d\) root polytopes. Bezdek and Khan's 2016 survey, Section 4.1, distinguishes quantitative illumination from the ordinary illumination number and describes the related three-dimensional upper-bound conjecture. The 2006 paper of Bezdek, Böröczky and Kiss concerns successive parameters and gives exact cases for cubes and cross-polytopes according to its accessible abstract. Those different polytopes and the ordinary-illumination results for the cube–octahedron intersection family do not imply the quantitative cost formula above. The complete 2006 text was not accessible during comparison, so a residual historical overlap risk remains.

## Limitations
The theorem does not resolve the universal quantitative illumination conjecture or determine parameters of other Archimedean solids. Its source-cost bound is strict for each fixed finite illuminating set but the infimum is approached, not attained, by the near-vertex construction. The certificate establishes correctness conditional only on the explicitly proved polytope description and vertex illumination criterion; it is not an independent expert audit. Originality against all unindexed literature cannot be guaranteed.

## References
1. G. Kiss and P. O. de Wet, *Notes on the illumination parameters of convex polytopes*, Contributions to Discrete Mathematics 7 (2012), 58–67, DOI: 10.55016/ojs/cdm.v7i1.62108, especially Theorem 3.4. Public article page: https://cdm.ucalgary.ca/article/view/62108 .
2. K. Bezdek and M. A. Khan, *The geometry of homothetic covering and illumination*, arXiv:1602.06040 (2016), Section 4.1. https://arxiv.org/html/1602.06040v2 .
3. K. Bezdek, K. Böröczky and G. Kiss, *On the successive illumination parameters of convex bodies*, Periodica Mathematica Hungarica 53 (2006), 71–82, DOI: 10.1007/s10998-006-0022-3 (abstract and bibliographic details reviewed; complete text not accessible).
