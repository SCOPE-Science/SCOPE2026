# Eight four-round theories of antipodally folded binary cubes

## Finding
For each integer \(n\ge2\), let \(F_n\) be the simple graph with vertex set \(\mathbb F_2^n/\langle\mathbf1\rangle\), where \(\mathbf1\) is the all-one vector, and join two distinct cosets when some representatives differ in exactly one coordinate. Work in first-order logic with equality and adjacency as the only relation symbols, without constants, order, colours, or counting quantifiers. Then
\[
F_n\equiv_4 F_m
\quad\Longleftrightarrow\quad
(n=m\in\{2,3,4,5,6,7\})\ \lor\ (n,m\in\{8,9\})\ \lor\ (n,m\ge10).
\]
Consequently there are exactly eight rank-four equivalence classes, with smallest-dimension representatives \(F_2,F_3,F_4,F_5,F_6,F_7,F_8,F_{10}\). Every member has a rank-four-equivalent member of this family on at most \(2^9=512\) vertices; this bound is attained and is optimal among representatives drawn from the family.

A second conclusion, proved independently of the finite enumeration, is that \(F_n\equiv_4 F_m\) whenever \(n,m\ge16\). The exhaustive finite exact-type calculation is needed only for \(2\le n\le16\). The class of \(F_8\) also contains \(F_9\); the remaining nonsingleton class contains all \(F_n\) with \(n\ge10\). This collision crosses a genuine global graph boundary: \(F_8\) is bipartite, because even-dimensional complementation preserves coordinate parity, whereas \(F_9\) has an odd nine-cycle obtained by flipping the nine coordinates successively and returning to the initial antipodal class.

## Assumptions and scope
The graph \(F_n\) is the antipodal quotient of the \(n\)-cube, equivalently the graph obtained from the ordinary \((n-1)\)-cube by adding edges between complements. It has \(2^{n-1}\) vertices. Our dimension parameter is therefore one greater than that used in literature defining a folded cube as a cube with extra antipodal edges rather than as a quotient.

For representatives \(x,y\in\mathbb F_2^n\), let \(h(x,y)\) denote Hamming distance. Equality of their quotient vertices holds exactly when \(h(x,y)\in\{0,n\}\); adjacency holds exactly when \(h(x,y)\in\{1,n-1\}\). The latter remains well-defined after complementing either representative. We only use \(n\ge2\), so equality and adjacency do not overlap. Translation makes every \(F_n\) vertex-transitive.

The notation \(G\equiv_4H\) means that every first-order sentence of quantifier rank at most four has the same truth value in both finite graphs. This is equivalent to Duplicator winning the unrestricted four-round Ehrenfeucht–Fraïssé game.

## Proof
**1. Coordinate profiles of ordered tuples.** After any first vertex is selected, use translation to choose its lift as the zero vector. For an ordered tuple of \(t\) quotient vertices, choose arbitrary lifts of the other \(t-1\) vertices. Each of the \(n\) coordinate positions then has a bit pattern \(p\in\{0,1\}^{t-1}\). Let \(c_p\) be the nonnegative number of coordinates with pattern \(p\); the \(2^{t-1}\) counts sum to \(n\). Every such nonnegative count vector is realized by a tuple, including tuples with repetitions. The arbitrary choice of representatives does not affect this exhaustive enumeration.

When a new quotient vertex is chosen, lift it as a bit vector and assign its bit independently within the coordinates of each existing pattern. Thus the exact set of possible extended count vectors consists of all vectors \((c_p-a_p,a_p)_p\) with integral \(0\le a_p\le c_p\); the concatenation follows the order of patterns with new bit zero then one. This enumerates **all** extensions, not just orbit representatives subject to an unproved completeness assumption.

**2. Atomic diagrams.** For a four-tuple, its profile has eight counts. Write \(b_1(p)=0\) and let \(b_i(p)\), for \(i=2,3,4\), be the appropriate bits of \(p\). For every \(1\le i<j\le4\), put
\[
\delta_{ij}=\sum_{p:b_i(p)\ne b_j(p)}c_p.
\]
The complete atomic diagram in the pure graph language is determined by declaring equality precisely when \(\delta_{ij}\in\{0,n\}\), adjacency precisely when \(\delta_{ij}\in\{1,n-1\}\), and neither otherwise. This includes all six vertex pairs and handles repeated selections.

**3. Exact Hintikka recursion.** Let \(T_4(c)\) be this complete atomic diagram. For \(t=3,2,1\), define \(T_t(c)\) recursively as the finite set of \(T_{t+1}(c')\) over every allowed split extension \(c'\). These sets are nested finite mathematical objects, not hashes. The standard back-and-forth induction says two states at level \(t\) support the same \(4-t\) remaining rounds exactly when their \(T_t\) objects agree. The base case is equality of all atomic formulas, and the induction step is equality of the complete sets of possible opponent choices in either structure. Because the graphs are vertex-transitive, their unpointed four-round theories agree exactly when \(T_1((n))=T_1((m))\).

**4. Uniform stabilization.** Define \(c\sim_hc'\) for two same-length count vectors by \(\min(c_p,h)=\min(c'_p,h)\) for every pattern. The *splitting lemma* states that if \(c\sim_{2h}c'\), then every split \(c=a+b\) can be matched by a split \(c'=a'+b'\) such that the two concatenated child vectors are related by \(\sim_h\), and conversely. For each coordinate-pattern count smaller than \(2h\), the numbers are equal, so copy the split. If both counts are at least \(2h\), then each requested child part below \(h\) can be copied exactly and any requested part at least \(h\) can be matched by an available part at least \(h\). Two requested large parts are feasible because both parent counts are at least \(2h\). The construction works independently in every profile cell and in both directions.

At the four-vertex stage, \(c\sim_2c'\) preserves every atomic diagram: a sum over a subset of cells is zero or one exactly when its truncated-at-two cell counts force that result; the complementary subset similarly determines whether the sum is \(n\) or \(n-1\). Applying the splitting lemma backward gives equality of \(T_3\) under \(\sim_4\), equality of \(T_2\) under \(\sim_8\), and equality of \(T_1\) under \(\sim_{16}\). For any \(n,m\ge16\), the initial one-cell profiles \((n)\) and \((m)\) are \(\sim_{16}\), proving \(F_n\equiv_4F_m\) uniformly.

**5. Sharp finite boundary.** Evaluate the exact recursion from step 3 for each integer \(2\le n\le16\), with all four-tuple atomic diagrams computed by step 2. The exhaustive standalone Python program supplied with this result uses integer profile splits only; every dimension has finitely many profiles, and it makes no graph-size extrapolation. Its exact outcomes are:
\[
\{2\},\ \{3\},\ \{4\},\ \{5\},\ \{6\},\ \{7\},\ \{8,9\},\ \{10,11,12,13,14,15,16\}.
\]
The last class extends to all greater dimensions by step 4. The first seven distinct profiles and the final distinct profile give exactly eight classes. Their largest smallest representative is \(F_{10}\), which has \(512\) vertices; no graph \(F_n\) with \(n<10\) has its four-round theory, proving the sharp family-relative representative bound. A particularly transparent separator of the last two classes is diameter. The graph distance on quotient vertices is \(\min(h,n-h)\), hence \(\operatorname{diam}(F_n)=\lfloor n/2\rfloor\). Define \(\delta_0(x,y)\) to mean \(x=y\lor E(x,y)\), and recursively \(\delta_{j+1}(x,y):=\exists z(\delta_j(x,z)\land\delta_j(z,y))\). The sentence \(\forall x\,\forall y\,\delta_2(x,y)\) has quantifier rank four and expresses diameter at most four; it holds for \(F_8,F_9\) and fails for every \(F_n\) with \(n\ge10\). The other boundaries are certified by the complete exact-type recursion.

## Verification
Run `python3 folded_rank4_verify.py` in a directory containing the supplied script; it uses only the Python standard library. The script enumerates every nonnegative coordinate-profile split, computes all six atomic pair relations, and builds nested immutable sets of extension types. Its printed representative sequence for dimensions \(2\) through \(16\) is
\[
2,3,4,5,6,7,8,8,10,10,10,10,10,10,10.
\]
An independent path through direct graph vertices, rather than coordinate profiles, recomputes the complete four-round type for dimensions \(2\) through \(7\) and asserts equality with the profile implementation. The complete saved output ends with `EIGHT_CLASSES_AND_FINITE_BOUNDARY_OK` and `VERIFY_OK`.

The infinite-dimension conclusion is a proof from the splitting lemma and does not use a computer. The finite verifier is exhaustive only for the explicitly stated integer range; the direct second computation is restricted to dimensions at most seven.

## Relationship to prior work
Pikhurko and Verbitsky (2010) survey first-order graph definability, quantifier rank and Ehrenfeucht games, including the relevant logical equivalence principle. Mirafzal (2011) gives the Cayley realization and automorphism group of folded hypercubes and proves their arc-transitivity, but does not classify bounded-rank first-order theories. Existing graph-theoretic data, including distance-transitivity and chromatic behavior, do not themselves imply the displayed four-round partition.

The corresponding rank-four classification of ordinary binary hypercubes does not directly apply: forming the antipodal quotient changes the vertex domain and edge relation, and the antipodal pairing of the original cube is not given as a primitive relation in the graph language. Folded-cube occurrences in other constructions also do not imply a bounded-rank equivalence classification. Searches found no prior statement that covers this exact eight-class result; this is a bounded search conclusion, not proof of priority.

## Limitations
Only ordinary first-order logic in the equality/adjacency language and quantifier rank four is treated. No claim is made for counting quantifiers, named coordinates, ordered graphs, arbitrary graph covers or higher rank. The bound of \(512\) vertices is optimal among folded cubes, not among arbitrary finite graphs. Historical originality remains subject to further literature review; no independent mathematical audit has been performed.

## References
- O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first public 2010-03-25, https://arxiv.org/abs/1003.4865.
- S. M. Mirafzal, *Some other algebraic properties of folded hypercubes*, arXiv:1103.4351, first public 2011-03-22, https://arxiv.org/abs/1103.4351.
