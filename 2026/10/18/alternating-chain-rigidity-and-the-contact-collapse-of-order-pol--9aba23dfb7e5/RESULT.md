# Alternating-chain rigidity and the contact collapse of order-polytope difference bodies

## Finding
For every nonempty finite poset \(P\), let \(h\) be the maximum cardinality of a chain, and let \(L\) be the number of chains of cardinality \(h\). Its standard-coordinate order polytope and difference body are
\[
\mathcal O(P)=\{x\in[0,1]^P:x_p\le x_q\text{ whenever }p<q\},
\qquad D(P)=\mathcal O(P)-\mathcal O(P).
\]
The difference body has centered Euclidean inradius
\[
\boxed{r(D(P))=h^{-1/2}.}
\]
More precisely, *all* unit normals of support hyperplanes of \(D(P)\) tangent to its largest centered Euclidean ball are
\[
\boxed{u_{C,\pm}=\pm\frac1{\sqrt h}\sum_{j=1}^{h}(-1)^{j-1}e_{c_j},
\quad C=(c_1<\cdots<c_h)\text{ a longest chain}.}
\]
There are exactly \(2L\) such oriented normals, with no additional ones. Equivalently the minimum Euclidean directional width of \(\mathcal O(P)\) is \(h^{-1/2}\), attained only in those directions.

There is an exact strengthened support formula. For any longest chain \(C=(c_1<\cdots<c_h)\) and sign sequence \(\varepsilon_j\in\{-1,1\}\), put
\[
u_{C,\varepsilon}=\frac1{\sqrt h}\sum_{j=1}^h\varepsilon_je_{c_j},
\quad S_k=\sum_{j=k+1}^h\varepsilon_j\quad(0\le k\le h).
\]
Then
\[
\boxed{h_{D(P)}(u_{C,\varepsilon})=
\frac{\max_{0\le k\le h}S_k-\min_{0\le k\le h}S_k}{\sqrt h}.}
\]
This is \(h^{-1/2}\) exactly for alternating signs. Every nonalternating sign sequence gives support at least \(2h^{-1/2}\).

Let \(E(P)\) be the unconditional (enriched) chain polytope, the convex hull of signed characteristic vectors of antichains. The published facet and radius descriptions of \(E(P)\) show that it shares the centered inradius \(h^{-1/2}\) with \(D(P)\), but its centered inball has exactly \(2^hL\) oriented tangent support normals. Thus the order-polytope difference body retains exactly a fraction \(2^{1-h}\) of these contacts, although their optimal radius is unchanged.

## Assumptions and scope
The poset is finite and nonempty, with no purity, grading, connectedness, or labeling hypothesis. A chain \(c_1<\cdots<c_h\) has \(h\) **elements**, not \(h\) edges; each longest chain is automatically inclusion-maximal. The standard Euclidean metric on \(\mathbb R^P\) is essential; a generic affine transformation does not preserve the formula.

For compact convex \(K\), write \(h_K(u)=\max_{x\in K}\langle u,x\rangle\). The width of \(\mathcal O(P)\) in unit direction \(u\) is \(h_{\mathcal O(P)}(u)+h_{\mathcal O(P)}(-u)=h_{D(P)}(u)\). The inradius of a centrally symmetric body is attained at the origin, so its minimum unit support equals its inradius. Distinct normals are oriented: \(u\) and \(-u\) count separately. There is no claim that the origin is the only center of a maximum inscribed ball.

## Proof
**1. Antichain-range inequality.** Vertices of \(\mathcal O(P)\) are incidence vectors of filters (up-sets). Fix any antichain \(A\). Let \(F_A=\{p\in P:\exists a\in A,\ a<p\}\) be its strict upper closure. For each subset \(S\subseteq A\), the set \(F_A\cup S\) is a filter. For any vector \(v\), the values \(\langle v,\mathbf1_{F_A\cup S}\rangle\) have range exactly \(\sum_{a\in A}|v_a|\). Consequently, denoting the width in the unnormalized direction \(v\) by \(W(v)=h_{D(P)}(v)\),
\[
\boxed{W(v)\ge\sum_{a\in A}|v_a|\quad\text{for every antichain }A.}
\]

**2. A universal lower bound.** Give each \(p\in P\) its rank \(r(p)\), the maximum cardinality of a chain ending at \(p\). Strictly comparable elements have strictly different ranks. Hence the rank classes \(A_1,\ldots,A_h\) partition \(P\) into \(h\) antichains. By the preceding inequality,
\[
\|v\|_2^2
=\sum_{j=1}^h\sum_{p\in A_j}v_p^2
\le\sum_{j=1}^h\Big(\sum_{p\in A_j}|v_p|\Big)^2
\le hW(v)^2.
\]
Therefore every unit vector satisfies \(h_{D(P)}(v)\ge h^{-1/2}\), so the centered inradius is at least that value.

**3. An exact longest-chain support formula.** Fix a longest chain \(C=(c_1<\cdots<c_h)\). A filter intersects \(C\) in a terminal segment (a suffix). Conversely every suffix can occur: the upper closure of its least element intersects \(C\) exactly in that suffix; the empty filter realizes the empty suffix. Thus, for any vector supported on \(C\), the range over filter vertices is exactly the range over suffix sums of its chain coordinates. Applied to \(u_{C,\varepsilon}\), this proves the boxed support formula. Alternating signs give suffix sums confined to two consecutive integers, so their range is one. Consequently the inradius is at most \(h^{-1/2}\), giving equality.

**4. Rigidity of equality.** Suppose \(v\) is a unit vector with \(W(v)=h^{-1/2}\). Equality must hold throughout the two inequalities in Step 2. Every rank layer has total absolute coefficient \(W(v)\), and equality between \(\ell_1\) and \(\ell_2\) squares on that layer forces *exactly one* nonzero coefficient. Thus the support consists of \(h\) elements, each with absolute coefficient \(h^{-1/2}\). Any two incomparable support elements would form an antichain \(\{p,q\}\) with \(W(v)\ge |v_p|+|v_q|=2h^{-1/2}\), a contradiction. The support therefore is a chain of cardinality \(h\).

On this chain, if two consecutive coefficient signs agreed, the suffix-sum walk would contain two consecutive unit steps in the same direction. Its range would be at least two, contradicting \(W(v)=h^{-1/2}\). Hence signs alternate. Conversely every such alternating longest-chain vector attains equality by Step 3. Different longest chains have different supports, and each admits exactly two alternating orientations, giving \(2L\) unit normal directions.

**5. Comparison with the enriched chain polytope.** Existing facet theory writes \(E(P)\) as the intersection of inequalities \(\sum_{p\in C}\varepsilon_px_p\le1\) over inclusion-maximal chains and all sign patterns. The centered inradius is \(h^{-1/2}\); the active supporting hyperplanes are exactly the \(2^h\) sign patterns on each of the \(L\) longest chains. The normals in Step 4 select only the two alternating patterns on each longest chain. The contact-count ratio is therefore \((2L)/(2^hL)=2^{1-h}\). No equality of the two bodies is asserted.

## Verification
The independent, standard-library-only `verify.py` uses exact integer arithmetic. It generates every transitively closed relation compatible with a natural labeling on at most five elements (407 distinct such representations). Every finite poset on at most five elements admits a natural labeling, so all isomorphism types of those sizes are represented. It independently enumerates filter vertices, longest chains, and all nonzero ternary directions, testing the quadratic width lower bound and the exact equality-normal set. It separately verifies the suffix-walk support formula for every signed longest chain. The run passed on 407 representations, with 89,794 finite-grid directional comparisons and 1,760 counted equality witnesses. Finite tests are corroboration only; Steps 1--5 prove the theorem in every dimension.

To reproduce: run `python3 verify.py` (Python 3.9 or later; no external packages). The output must end with `PASS: 407 posets, 89794 directional checks, 1760 shortest-unit-direction witnesses`.

## Relationship to prior work
The order-polytope filter-vertex description goes back to Stanley and appears in von Bell et al., *Triangulations, Order Polytopes, and Generalized Snake Posets* (arXiv:2102.11306, first posted 2021-02-22; primary geometric classification in its published version). That work concerns triangulations, volumes, and circuits rather than Euclidean difference-body contact normals.

Ohsugi--Tsuchiya (arXiv:1903.00909) and Okada--Tsuchiya (arXiv:2003.12271) give the signed-antichain and signed-chain descriptions for enriched poset polytopes. A later published mathematical note, *Height and width are the exact Euclidean radii of enriched chain polytopes* (2026), establishes the enriched-chain inradius and all its tangent signed-chain normals. These inputs already give a route to the **numerical lower bound** for the difference-body inradius, since \(E(P)\subseteq D(P)\). No novelty is claimed for that inequality alone. The contribution here is the **complete alternating rigidity of the different body's equality normals, its exact signed-chain support profile, and the exponential contact collapse**; the all-sign enriched-chain contact theorem does not establish those statements for \(D(P)\).

A recent work by J. Lee, *A refinement of the edge theorem for order and chain polytopes* (arXiv:2610.07413, 2026), compares edges and graph diameters of the ordinary polytopes, not these Euclidean inball contacts. The original numerical radius equality is not presented as independent of the enriched-chain theorem.

## Limitations
The analysis is for the **difference body** of the canonical order polytope, not for the original order polytope's inball. Its canonical Euclidean metric is required. The proof classifies tangent **normal directions of the centered maximal ball**, not all centers of maximal balls or all faces of the difference body. The equality-normal count concerns oriented normals; antipodal pairs count twice.

Because the lower radius bound follows quickly from earlier enriched-chain work and the embedding \(E(P)\subseteq D(P)\), only the narrower geometric equality/contact classification is assessed as a potential new result. An equivalent older observation under distributive-lattice or isotone-function terminology cannot be excluded solely by current literature searches; independent audit has not been performed.

## References
1. M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. R. Vindas-Meléndez, and M. Yip, *Triangulations, Order Polytopes, and Generalized Snake Posets*, arXiv:2102.11306 (2021), *Combinatorial Theory* **2** (2022), no. 3, DOI 10.5070/C62359166.
2. H. Ohsugi and A. Tsuchiya, *Enriched order polytopes and Enriched Hibi rings*, arXiv:1903.00909 (2019), *European Journal of Mathematics* **7** (2021), 48--68.
3. S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271 (2020), *Annals of Combinatorics* **28** (2024), 257--282.
4. *Height and width are the exact Euclidean radii of enriched chain polytopes*, published mathematical note (2026), published-finding corpus public mathematical research collection, record `db93f92ff100`.
5. J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413 (2026).
6. R. P. Stanley, *Two poset polytopes*, *Discrete & Computational Geometry* **1** (1986), 9--23.
