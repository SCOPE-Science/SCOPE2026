# Three self-homotopy classes on the minimal nine-point weakly contractible finite space
## Finding
Let \\(R\\) be the nine-point finite \\(T_0\\)-space displayed as Figure 1 by Cianci and Ottina. Label its minimal points \\(c_1,c_2,c_3\\), middle points \\(b_1,b_2,b_3\\), and maximal points \\(a_1,a_2,a_3\\). Its cover relations are

\\[
 c_1,c_2<b_1,\qquad c_1,c_2,c_3<b_2,\qquad c_2,c_3<b_3,
\\]
\\[
 b_1<a_1,a_2,\qquad b_2<a_1,a_3,\qquad b_3<a_2,a_3.
\\]

There are exactly \\(12{{,}}575\\) continuous self-maps of \\(R\\). With the pointwise order, the finite mapping space \\(R^R\\) has exactly three connected components, of sizes \\(12{{,}}573\\), \\(1\\), and \\(1\\). The singleton components are the identity and the involution \\(\sigma\\) given by

\\[
 c_1\leftrightarrow c_3,\qquad b_1\leftrightarrow b_3,\qquad a_1\leftrightarrow a_3,
\\]

with \\(c_2,b_2,a_2\\) fixed. These two maps are exactly the homeomorphisms of \\(R\\). Every other self-map is in the component containing all constant maps and is therefore null-homotopic. Hence \\([R,R]\\) has exactly three elements. Under composition, the two nonzero classes form \\(C_2\\), and the null-homotopy class is absorbing. The same statement holds for \\(R^{{\mathrm{{op}}}}\\).

## Assumptions and scope
The order convention is the one used by Cianci--Ottina: finite \\(T_0\\)-spaces are identified with their specialization posets, and continuous maps are exactly order-preserving maps. The claim concerns the specific nine-point space in their Figure 1 and its opposite. Cianci--Ottina prove that these are precisely the homotopically trivial non-contractible spaces of minimum cardinality, up to homeomorphism and order reversal.

No claim is made about the ten-point examples classified later, about arbitrary weakly contractible finite spaces, or about the strong-homotopy type of the whole mapping space beyond its connected-component census.

## Proof
A self-map \\(f:R\to R\\) is continuous exactly when it preserves every cover relation above. Assign the images of the nine domain points in the order \\(c_1,c_2,c_3,b_1,b_2,b_3,a_1,a_2,a_3\\). At each step, the admissible target values are precisely the common upper bounds of the images of already assigned lower covers. Exhaustive backtracking over these finite admissible sets therefore lists every isotone self-map exactly once and lists no non-isotone map. It produces \\(12{{,}}575\\) maps.

For two self-maps \\(f,g\\), write \\(f\leq g\\) when \\(f(x)\leq g(x)\\) for every \\(x\in R\\). Stong's finite-space homotopy criterion, stated explicitly as Corollary 1.2.6 in Barmak's finite-spaces monograph, says that two maps are homotopic exactly when they can be connected by a finite zigzag of pointwise comparable maps. Thus the homotopy classes are exactly the connected components of the undirected comparability graph of \\(R^R\\).

The exhaustive comparison of the \\(12{{,}}575\\) maps yields component sizes \\(12{{,}}573\\), \\(1\\), and \\(1\\). The two isolated maps are the identity and \\(\sigma\\). Exhaustive bijectivity testing shows that these are also the only two order automorphisms. All nine constant maps lie in the large component, so every map in that component is homotopic to a constant. Conversely, neither isolated automorphism is homotopic to a constant because an isolated vertex has no comparability zigzag to another map.

Composition preserves homotopy. Since \\(\sigma^2=\mathrm{id}_R\\), the two non-null classes form \\(C_2\\). Composing any map with a null-homotopic map on either side is again null-homotopic, so the third class is absorbing.

Reversing both the domain and target order does not change which set maps are isotone: \\(f:R\to R\\) is isotone exactly when the same function is isotone \\(R^{\mathrm{{op}}}\to R^{\mathrm{{op}}}\\). The pointwise order on the mapping poset is merely reversed. Therefore the map count, comparability components, homeomorphisms, and homotopy monoid are unchanged for the opposite space.

## Verification
The accompanying verifier reconstructs the poset solely from the listed cover relations, forms its transitive closure, and confirms that it has no beat points. It then enumerates all isotone self-maps, independently checks every enumerated map against the full order relation, identifies all bijective maps, builds the exact pointwise comparability graph by bit-set intersection, and computes its connected components by disjoint-set union.

The final replay reports

`VERIFY_OK maps=12575 components=12573,1,1 automorphisms=2 comparable_pairs=1235007 constants_large=9`.

The finite enumeration is exhaustive for this nine-point poset; it is not used as evidence for any infinite family or for any other finite space.

## Relationship to prior work
Cianci and Ottina identify the nine-point space, show that it has no beat points, prove its order complex is contractible, and prove that it and its opposite are the only homotopically trivial non-contractible spaces with nine points. Their paper also notes that the same poset appeared earlier in Rival's fixed-point work. Those results establish the object and its extremal status but do not state the self-map count or classify its finite-space self-homotopy classes.

Stong supplies the general finite-space homotopy machinery, and Barmak's Corollary 1.2.6 explicitly formulates the criterion that two maps between finite spaces are homotopic exactly when they are joined by a fence of pointwise comparable maps. These general results reduce the present question to an exact component computation but do not determine the three components for this poset.

Das and Mawiong later classify the ten-point weakly contractible non-contractible spaces; their classification is about possible underlying spaces rather than the self-homotopy monoid of the nine-point model. Their 2024 reduction paper also revisits the nine-point example from a different simple-homotopy/Andrews--Curtis perspective. A search of these sources and of the fixed-point literature located no statement of the \\(12{{,}}575\\)-map census or the three-class self-homotopy monoid.

## Limitations
The originality search cannot rule out an older order-theory computation under a different name for the same nine-point poset. Rival's 1976 paper is especially relevant because it contains the poset as an example; accessible bibliographic material and later descriptions were checked, but a full-text comparison of that paper was not available in this run. This residual literature risk is recorded explicitly.

The result is exact for \\(R\\) and \\(R^{\mathrm{{op}}}\\) only. It does not classify self-maps of larger weakly contractible non-contractible spaces, nor does it assert a beat-point core for the large component of \\(R^R\\).

## References
1. N. Cianci and M. Ottina, *Smallest homotopically trivial non-contractible spaces*, arXiv:1608.05307v1, first public 2016-08-18. See Figure 1 and Theorem 3.7. Primary MSC: 55P15 and 06A99.
2. R. E. Stong, *Finite topological spaces*, Transactions of the American Mathematical Society 123 (1966), 325--340.
3. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Springer, 2011, Corollary 1.2.6.
4. J. P. May, *Finite Spaces and Simplicial Complexes*, notes for REU, 2003; revised 2008 and 2010.
5. P. Das and S. M. Mawiong, *On Weakly Contractible Non-Contractible Finite Topological Spaces of Ten Points*, arXiv:2605.06155v1, 2026.
6. P. Das and S. M. Mawiong, *Some Spaces That Satisfy the Andrews-Curtis Conjecture*, Jñānābha 54(2) (2024), 145--157, DOI 10.58250/jnanabha.2024.54214.
