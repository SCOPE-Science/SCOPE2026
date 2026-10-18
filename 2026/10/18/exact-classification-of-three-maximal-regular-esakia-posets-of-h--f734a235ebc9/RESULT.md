# Exact classification of three-maximal regular Esakia posets of height four

## Finding
A finite rooted poset has **height four** when its longest chain has four vertices. Call such a poset *regular* if every nonmaximal point has at least two immediate successors and two distinct nonmaximal points never have the same immediate-successor set. There are exactly **\(3344\) isomorphism classes** of regular rooted height-four posets with exactly three maximal points. This is a complete normal form, not only a finite partial census.

The corresponding objects under finite Esakia duality are exactly \(3344\) isomorphism types of finite **subdirectly irreducible regularly generated Heyting algebras** with dual height four and exactly eight double-negation-fixed elements. The eight regular elements count the Boolean core; they are not a bound on the total algebra cardinality.

## Assumptions and scope
All posets are finite and antisymmetric. Their maximal elements are initially labelled \(a,b,c\) and considered indistinguishable only at the final orbit step. For a nonmaximal point \(x\), its *immediate-successor set* \(S(x)\) consists of elements covering \(x\). This is different from the set of maximal points above \(x\).

Write \(M=\{a,b,c\}\) and \(\mathcal{T}=\{\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}\}\). For every \(T\subseteq\mathcal{T}\) form an auxiliary poset \(Q_T\) with vertices \(M\) and one further vertex \(m_t\) for each \(t\in T\). Its only strict order relations are \(m_t<z\) when \(z\in t\), so its elements \(m_t\) are pairwise incomparable.

Let \(\mathcal{A}(T)\) be the family of antichains \(A\subseteq Q_T\) of size at least two which contain at least one vertex \(m_t\). For \(T\) with \(\mathcal{A}(T)\ne\varnothing\), let \(U\subseteq\mathcal{A}(T)\) be nonempty and not equal to the singleton \(\{\operatorname{Min}(Q_T)\}\). The set \(\operatorname{Min}(Q_T)\) is itself a member of \(\mathcal{A}(T)\) in every such case.

Construct \(P(T,U)\) by adding to \(Q_T\) a point \(u_A\) directly below exactly the vertices of \(A\), for every \(A\in U\), and one new least point \(r\) immediately below every minimal point of the resulting poset. Take the transitive closure. The classification asserts that \(P(T,U)\) gives all and only the required rooted regular posets, with no repetitions when \(T,U\) are fixed and the maxima are distinguished; two such posets are isomorphic precisely when their data differ by an element of \(S_3\) permuting \(a,b,c\).

## Proof
**1. The first upper layer.** The root is the only point of depth three: any other such point would yield a chain of at least five vertices starting at the root. Every nonroot point therefore has depth at most two. A point of depth one covers only maximal points. It covers at least two of the three maxima and, by regularity, there is at most one such point for each of the four support sets in \(\mathcal T\). Thus all depth-one points and their order relations are exactly \(Q_T\), for some \(T\subseteq\mathcal T\).

**2. The second upper layer.** Every depth-two point has immediate successors that form an antichain of size at least two. This antichain must include a depth-one point, or the original point would have depth one instead. Hence it belongs to \(\mathcal A(T)\). Uniqueness of successor sets implies at most one depth-two point for each possible antichain. Conversely, adding one depth-two point with immediate-successor set \(A\) for each \(A\in U\subseteq\mathcal A(T)\) creates no conflicting cover sets, because the sets for depth-two points contain depth-one vertices and are distinct, whereas those for depth-one points contain only maxima.

**3. The root and admissibility.** The height is four exactly when \(U\ne\varnothing\). The root covers the minimal elements of the assembled upper poset. If \(U\) has at least two members, those distinct depth-two points are distinct minimal vertices; thus the root has at least two covers. If \(U=\{A\}\), the root has only one cover exactly when \(A\) contains every minimal vertex of \(Q_T\). Because \(A\) is an antichain, this is equivalent to \(A=\operatorname{Min}(Q_T)\): every antichain containing all minimal vertices cannot contain any other vertex. Therefore the sole excluded nonempty selection is \(U=\{\operatorname{Min}(Q_T)\}\). For all allowed \(U\), the root has at least two covers, and its cover set contains a depth-two vertex, unlike every other nonmaximal point's cover set; hence all required conditions hold. This also proves the construction is exhaustive.

**4. Distinguishing and forgetting labels.** For fixed maximal labels, \(T\) and \(U\) are determined by the order, yielding
\[
N_{\mathrm{marked}}=\sum_{T:\,\mathcal A(T)\ne\varnothing}\bigl(2^{|\mathcal A(T)|}-2\bigr)=16718.
\]
The cardinalities \(|\mathcal A(T)|\), grouped by types of \(T\), follow directly from its antichain definition: three two-pair selections contribute \(3\) each, the all-three-pairs selection contributes \(7\), three pair-plus-triple selections contribute \(2\) each, three two-pairs-plus-triple selections contribute \(6\) each, and the full selection contributes \(14\). Every other \(T\) contributes zero. Thus the total is
\[
3(2^3-2)+(2^7-2)+3(2^2-2)+3(2^6-2)+(2^{14}-2)=16718.
\]
The group \(S_3\) acts on the distinguished maximal points and thereby on \((T,U)\). For a permutation \(\sigma\), a \(T\) invariant under \(\sigma\) has \(\sigma\)-invariant admissible selections in bijection with subsets of the cycles of \(\sigma\) on \(\mathcal A(T)\), excluding empty and the singleton of all minima. Consequently the number fixed by \(\sigma\) is the sum of \(2^{c_\sigma(T)}-2\) over the relevant invariant \(T\), where \(c_\sigma(T)\) is the number of these cycles. Direct finite evaluation gives the identity count \(16718\), each transposition \(1070\), and each 3-cycle \(68\). Burnside's lemma yields
\[
N_{\mathrm{unmarked}}=\frac{16718+3\cdot1070+2\cdot68}{6}=\boxed{3344}.
\]
No other order isomorphisms occur: every isomorphism permutes maximal elements and its action on all other points is forced by their ranks and immediate-successor antichains.

**5. Algebraic translation.** By Grilletti and Quadrellaro, Theorem 4.7, finite regular posets in this sense are precisely the finite Esakia duals of regularly generated Heyting algebras; rootedness corresponds to subdirect irreducibility. By their Corollary 3.5, the Boolean algebra of double-negation-fixed elements is the power-set Boolean algebra on the maximal points. The three maxima therefore give exactly \(2^3=8\) regular elements. Esakia duality preserves and reflects isomorphism, so the poset and algebra counts agree.

## Verification
The accompanying Python 3 standard-library program `verify.py` checks all \(16718\) admissible marked constructions. It reconstructs transitive closure, recalculates cover sets, checks uniqueness and cover multiplicity at every nonmaximal point, checks height four, rootedness, and precisely three maxima. It independently canonicalises data under all six permutations and finds \(3344\) orbits. A separate cycle-count evaluation of Burnside's lemma obtains fixed-point multiset \(\{16718,1070,1070,1070,68,68\}\). The posets have from \(7\) through \(22\) points; the last bound is attained when all four middle supports and all fourteen eligible second-layer antichains are selected.

Reproduce with `python3 verify.py` from the directory containing the embedded standalone file. The program prints `VERIFIED` only if all assertions succeed. The infinite mathematical assertion is the finite-parameter normal-form argument above; the computation is an exhaustive independent check of that finite normal-form census, not a substitute for the proof of completeness.

## Relationship to prior work
Grilletti and Quadrellaro's *Esakia Duals of Regular Heyting Algebras*, Theorem 4.7, establishes the regularity criterion used in Step 5, and its concluding section explicitly proposes classification by depth and number of maximal elements as a problem. Their paper does not provide this height-four/three-maximal normal form or isomorphism count. Its Corollary 3.5 supplies the relation between maximal points and regular algebra elements. Related results about finite Kripke frames, modal relations and general poset orbit counts do not yield the specific regular-Heyting constrained census without the stated antichain decomposition.

## Limitations
The result counts **isomorphism classes of algebras/posets**, not distinct logics, distinct varieties, or numbers of elements in the Heyting carriers. Height is measured in **vertices of a longest chain**, not edges. Marked maxima yield \(16718\) objects; unmarked objects yield \(3344\). An independently performed external mathematical audit has not been conducted. Exhaustive literature searching cannot prove that an earlier equivalent enumeration does not exist under another terminology.

## References
1. G. Grilletti and D. E. Quadrellaro, *Esakia Duals of Regular Heyting Algebras*, arXiv:2303.11246, first public version 20 March 2023; *Algebra Universalis* 85, article 5 (2024), doi:10.1007/s00012-023-00833-5. Especially Corollary 3.5, Theorem 4.7 and Section 7.
2. W. Burnside, standard orbit-counting lemma (used only in its elementary finite permutation-group form).
