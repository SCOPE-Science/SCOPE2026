# Rigidity and exact census of bounded morphisms between finite layered orders

## Finding
Let
\[
P=A_1\oplus\cdots\oplus A_h,\qquad Q=B_1\oplus\cdots\oplus B_k
\]
be nonempty finite ordinal sums of nonempty antichains, with \(p_i=|A_i|\ge1\) and \(q_j=|B_j|\ge2\). Regard their reflexive partial orders as Kripke accessibility relations. A bounded morphism \(f:P\to Q\) preserves order and satisfies: whenever \(f(x)\le_Q y\), there is \(z\ge_P x\) with \(f(z)=y\).

**Rigidity theorem.** Every *surjective* bounded morphism \(f:P\to Q\) has \(h=k\), maps each source level \(A_i\) *onto* the corresponding target level \(B_i\), and has no other form. Conversely every collection of surjections \(A_i\twoheadrightarrow B_i\), assembled level by level, is a surjective bounded morphism. Thus the complete exact count on individually distinguished underlying sets is
\[
\boxed{N(P,Q)=\begin{cases}\displaystyle\prod_{i=1}^{h}q_i!\,\left\{\!\begin{matrix}p_i\\q_i\end{matrix}\!\right\},&h=k,\\0,&h\ne k.\end{cases}}
\]
Here the braces denote Stirling numbers of the second kind; an empty product is not needed because both orders are nonempty. In particular, a quotient exists exactly when \(h=k\) and \(p_i\ge q_i\) for all \(i\). Consequently, within the family of such finite layered orders, the preorder defined by surjective bounded-morphic images is precisely the disjoint union, by fixed height, of coordinatewise component-size orders.

The requirement \(q_i\ge2\) is sharp as a uniform structural hypothesis: if a target has a singleton level, one may split that singleton into two consecutive singleton source levels, obtaining a source with one extra level and an onto bounded morphism onto the original target.

## Assumptions and scope
An ordinal sum \(A_1\oplus\cdots\oplus A_h\) is the disjoint union of antichains with \(x<y\) for all \(x\in A_i\), \(y\in A_j\) and \(i<j\). Distinct points of one level are incomparable. All points and levels are distinguished; the count is **not** divided by automorphisms. All orders are finite and nonempty, all source levels have at least one point, and every target level has at least two points. The accessibility relation is reflexive \(\le\), and both order preservation and the upward back condition are required. No statement is made about arbitrary posets or about p-morphisms without surjectivity.

## Proof
**Lemma 1 (one source level per target level).** Suppose \(f\) is an onto order-preserving map. Fix a target level \(B_j\), and choose two distinct points \(b,b'\in B_j\). If their preimages lay in different source levels, those preimages would be comparable but their images would be incomparable. Hence they lie in one source level \(A_{\phi(j)}\). Every other preimage of every point of \(B_j\) lies in the same \(A_{\phi(j)}\): compare it with a preimage of \(b\) or \(b'\) whose target value differs. Consequently \(f^{-1}(B_j)\subseteq A_{\phi(j)}\), and \(\phi(j)\) is well defined. Monotonicity gives \(\phi(j)\le\phi(l)\) for \(j<l\); otherwise a source point mapped to the upper target level would lie strictly below one mapped to the lower target level.

**Lemma 2 (strictness forced by the back condition).** In fact \(\phi(j)<\phi(l)\) when \(j<l\). If equality held, choose \(u,v\) in that common source level with \(f(u)=b\in B_j\) and \(f(v)=c\in B_l\). Choose \(c'\in B_l\setminus\{c\}\), possible because \(|B_l|\ge2\). Since \(b<c'\), the back condition for \(u\) produces \(w\ge u\) with \(f(w)=c'\). The point \(w\ne u\) must be in a strictly later source level, because distinct points of \(A_{\phi(j)}\) are incomparable. Thus \(v<w\). But then order preservation would give \(c=f(v)\le f(w)=c'\), impossible for distinct points of the target antichain \(B_l\).

**Level rigidity.** Lemmas 1 and 2 give a strictly increasing injection \(\phi:\{1,\ldots,k\}\to\{1,\ldots,h\}\). Every source level contains an element, which maps into some target level, so every source-level index belongs to the image of \(\phi\). Thus \(\phi\) is also surjective. A strictly increasing bijection of two nonempty finite initial integer intervals has \(h=k\) and \(\phi(j)=j\) for all \(j\). Since \(f\) is onto, its restriction \(A_i\to B_i\) is onto.

**Converse.** Let \(h=k\), and choose arbitrary surjections \(f_i:A_i\twoheadrightarrow B_i\). The resulting map is order preserving. Given \(x\in A_i\) and \(y\ge_Q f(x)\), either \(y=f(x)\) (take \(z=x\)) or \(y\) belongs to some strictly higher level \(B_j\) (choose a preimage \(z\in A_j\), which is above \(x\)). This verifies the back condition and proves the converse.

**Counting and the boundary.** For labelled sets with \(|A_i|=p_i\) and \(|B_i|=q_i\), the number of onto functions is \(q_i!\left\{\!\begin{smallmatrix}p_i\\q_i\end{smallmatrix}\!\right\}\). Multiplying independent level choices proves the census and coordinatewise existence criterion. If a target level \(B_j=\{b\}\) is a singleton, replace it in the source by consecutive singleton levels \(\{u\}\oplus\{v\}\), leave the other levels unchanged, and map \(u,v\) both to \(b\). The resulting quotient is monotone and meets the back condition, while the source height exceeds the target height by one; thus the target-size hypothesis cannot simply be dropped.

## Verification
The standalone standard-library program `artifacts/verify.py` independently constructs both reflexive poset orders, enumerates all functions on small labelled carriers, and tests surjectivity, order preservation, and the upward back condition for every relevant pair of points. It compares the actual count against the Stirling-product theorem in **181 exhaustive source/target-level configurations** with at most six source points and five target points, including cases with unequal heights and some singleton source levels. Its additional tests verify the height-boundary counterexample when a target level is a singleton and check six illustrative count values. The recorded output is in `artifacts/verification_output.txt`, ending with `ALL_TESTS_PASS`. This finite evidence tests the proof but does not replace the two general lemmas.

Run with `python3 artifacts/verify.py` from the root of the extracted package. The verifier has no third-party dependencies.

## Relationship to prior work
Pouzet and Zaguia (2007) characterize weak orders as lexicographic sums of antichains and study perpendicular linear orders and monotone endomorphisms. That structural starting point does not give the onto bounded-morphism classification. Rzążewski and Stronkowski (2025) define the exact forward and backward conditions and study the general surjective p-morphism decision problem, including hardness results, but their stated restricted tractable case concerns tree inputs rather than layered orders. Alberto (2024) identifies these layered orders as the posets underlying pseudospheres, but studies their simplicial/topological properties rather than bounded-morphic quotients.

Related public results titled *Exact cardinality recurrence for mapping spaces between finite weak orders*, *Off-diagonal homotopy rigidity for finite weak-order pseudospheres*, and *Cross-height nullity for finite weak-order pseudospheres* concern **all monotone maps**, their homotopy classes, and mapping-space components, respectively. They do not state an onto bounded-morphism census or show that the back condition forces strict level correspondence. In particular, a null-homotopic monotone map is not automatically disqualified from being a surjective bounded morphism without an additional argument. The present theorem identifies an exactly soluble subclass of the general surjective p-morphism problem, rather than re-counting all continuous maps.

## Limitations
All target levels must have at least two points. Singleton target levels permit genuine height collapse, as exhibited in the proof. The exact count concerns global surjectivity and the **upward** back condition on reflexive orders, not downwards back conditions, embeddings, finite-space homotopy equivalence, or quotient maps in an unrelated algebraic sense. Arithmetic complexity is not asserted beyond evaluating the explicit finite product. A literature search cannot establish absolute historical uniqueness; an equivalent characterization could appear in specialized modal-logic or finite-poset work under different terminology. Independent external validation is not claimed.

## References
1. M. Pouzet and I. Zaguia, *Weak orders admitting a perpendicular linear order*, Discrete Mathematics **307** (2007), 97–107, DOI: `10.1016/j.disc.2006.05.038`; dated public publisher record 2007-01-06.
2. P. Rzążewski and M. Stronkowski, *Tabular intermediate logics comparison*, arXiv:`2509.06841` (2025), especially Definition of p-morphism and Theorem 1.4.
3. L. Alberto, *Pseudospheres: combinatorics, topology and distributed systems*, Journal of Applied and Computational Topology **8** (2024), 1023–1052, DOI: `10.1007/s41468-023-00162-5`.
4. *Exact cardinality recurrence for mapping spaces between finite weak orders*, publicly available mathematical result (2026), identifier `2026/10/4/SCOPE-exact-cardinality-recurrence-for-mapping-spaces-between-finite-w--1cee64311a06`.
5. *Off-diagonal homotopy rigidity for finite weak-order pseudospheres*, publicly available mathematical result (2026), identifier `2026/10/4/SCOPE-off-diagonal-homotopy-rigidity-for-finite-weak-order-pseudospher--b0d3c63112c5`.
6. *Cross-height nullity for finite weak-order pseudospheres*, publicly available mathematical result (2026), identifier `2026/10/4/SCOPE-cross-height-nullity-for-finite-weak-order-pseudospheres--3a228577217e`.
