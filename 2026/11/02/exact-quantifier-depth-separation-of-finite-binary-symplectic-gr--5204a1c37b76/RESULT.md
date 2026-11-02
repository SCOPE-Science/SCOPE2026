# Exact quantifier-depth separation of finite binary symplectic graphs

## Finding

For every integer \(d\ge 1\), let \(S_d\) be the graph with vertex set \(V_d\setminus\{0\}\), where \(V_d=\mathbb F_2^{2d}\) carries a nondegenerate alternating bilinear form \(B_d\). Distinct vertices \(x,y\) are adjacent exactly when \(B_d(x,y)=1\). This is the graph customarily denoted \(\operatorname{Sp}(2d,2)\); its order is \(2^{2d}-1\).

Write \(S_d\equiv_q S_e\) if the graphs satisfy the same first-order sentences of quantifier rank at most \(q\), in the language of equality and a single undirected adjacency relation. Then:

1. All \(S_d\) are equivalent at rank one.
2. At rank two, \(S_1\) forms one class and all \(S_d\) with \(d\ge2\) form the other.
3. For every integer \(q\ge3\),
   \[
   S_d\equiv_q S_e \quad\Longleftrightarrow\quad
   \bigl(d=e<q-1\bigr)\ \lor\ \bigl(d,e\ge q-1\bigr).
   \]
   In particular, there are exactly \(q-1\) rank-\(q\) classes, represented by \(S_1,\ldots,S_{q-1}\). Every graph in the family has a rank-\(q\) equivalent representative on at most \(2^{2(q-1)}-1\) vertices, and this bound is sharp within the family.

Equivalently, for \(1\le d<e\), the minimum quantifier rank of a sentence distinguishing \(S_d\) and \(S_e\) is \(2\) if \(d=1\), and \(d+2\) if \(d\ge2\). The three rank-four classes have smallest representatives of orders \(3,15,63\).

## Assumptions and scope

The field is precisely \(\mathbb F_2\); the ambient space is even-dimensional with a nondegenerate alternating form. Nonzero vectors, not one-dimensional subspaces, are vertices (these coincide over \(\mathbb F_2\)). Adjacency means *nonorthogonality* \(B_d(x,y)=1\); for distinct vertices orthogonality means nonadjacency. The only predicates named are graph adjacency and equality. Quantifier rank counts nested first-order quantifiers, without counting quantifiers or additional symbols. All ranks \(q\) and dimensions \(d,e\) in the statement are positive integers. No claim is made for other fields or for graph languages enriched by algebraic operations.

Fix a symplectic basis \(e_1,f_1,\ldots,e_d,f_d\) so that \(B_d(e_i,f_j)=\delta_{ij}\), and all other pairings between basis vectors vanish. Any two nondegenerate alternating forms of this dimension are isometric, so \(S_d\) is well defined up to graph isomorphism.

## Proof

**Linear extension lemma.** Let \(U\) be any \(t\)-dimensional subspace of \(V_d\), and let \(\lambda:U\to\mathbb F_2\) be a linear functional. The vectors \(w\in V_d\) satisfying \(B_d(w,u)=\lambda(u)\) for every \(u\in U\) form an affine subspace with exactly \(2^{2d-t}\) elements. Indeed, the nondegenerate form identifies \(V_d\) with its full dual, and restriction of dual functionals to \(U\) is surjective. Hence the restriction map has rank \(t\), and each fiber has the asserted size. In particular, if \(d>t\), a fiber has more than \(2^t\) members, so it contains an element outside \(U\).

**Upper bound for rank \(q\ge3\).** Suppose \(d,e\ge q-1\). Duplicator has a winning strategy in the \(q\)-round Ehrenfeucht--Fraïssé game on \(S_d,S_e\). For the first \(q-1\) selections, strengthen the usual graph-partial-isomorphism condition: the correspondence between selected nonzero vectors extends to a linear isomorphism of their spans preserving the alternating form.

Initially the spans are zero and the condition holds. When Spoiler repeats a selected vertex, Duplicator repeats its mate. If Spoiler selects a new vector lying in the current span, Duplicator applies the span isomorphism: the image remains nonzero and new, and the span isomorphism persists. If Spoiler instead selects a vector linearly independent of previously chosen vectors, the form prescribes a consistent functional on their span. Let that span have dimension \(t\). Before the last move, \(t\le q-2\). In the other graph the linear extension lemma provides \(2^{2e-t}>2^t\) vectors with those pairings, so at least one lies outside the old span. Choosing it extends the span isometry. The argument is symmetric if Spoiler plays in either graph.

At the final, \(q\)th, move it is unnecessary to preserve linear dependence: only equality and adjacency of the selected vertices must match. If Spoiler chooses a previously selected vertex, respond with its mate. Otherwise, if the old span has dimension \(t\le q-1\), its pairing prescription is a consistent linear functional on the other old span. The solution fiber has at least \(2^{2(q-1)-(q-1)}=2^{q-1}>q\) vectors, since \(q\ge3\). Excluding zero and at most \(q-1\) previously selected vertices leaves an admissible fresh nonzero vector. The resulting correspondence preserves adjacency and equality on all \(q\) selections. Hence \(S_d\equiv_q S_e\) whenever \(d,e\ge q-1\).

**Lower bound for different small dimensions.** Let \(1\le d<e\). If \(d=1\), then \(S_1\) is the complete graph on three vertices. Every \(S_e\), \(e\ge2\), has distinct orthogonal nonzero vectors, hence a pair of nonadjacent vertices. The latter property is expressed by two existential quantifiers, and the two graphs are distinguishable at rank two.

Now let \(d\ge2\). In \(S_e\), Spoiler selects \(d+1\) independent mutually orthogonal nonzero vectors \(x_1,\ldots,x_{d+1}\). These exist because the span of \(e_1,\ldots,e_e\) is totally isotropic and \(e\ge d+1\). Their mates \(y_1,\ldots,y_{d+1}\) in \(S_d\), unless Duplicator has already lost, must be distinct, nonzero, and pairwise orthogonal. Their span is totally isotropic; any such subspace of the \(2d\)-dimensional nondegenerate symplectic space has dimension at most \(d\), since \(U\subseteq U^\perp\) gives \(\dim U\le d\). Thus the mates are linearly dependent: \(\sum_{i\in I}y_i=0\) for some nonempty index set \(I\).

Choose bits \(b_1,\ldots,b_{d+1}\in\mathbb F_2\) with \(\sum_{i\in I}b_i=1\). Because the \(x_i\) are independent and the alternating form is nondegenerate, the extension lemma supplies \(w\in V_e\) with \(B_e(w,x_i)=b_i\) for all \(i\). This vector is nonzero and different from every \(x_i\), since at least one \(b_i\) is one while all \(x_j\) pair to zero with all the \(x_i\). Spoiler selects \(w\) as the next vertex. Any response \(z\in V_d\) would have to satisfy \(B_d(z,y_i)=b_i\) for all \(i\), contradicting \(0=B_d(z,\sum_{i\in I}y_i)=\sum_{i\in I}b_i=1\). Therefore Spoiler wins in at most \(d+2\) moves.

For ranks \(q\le d+1\), the upper-bound strategy applies to \(S_d,S_e\) when \(q\ge3\), because \(d,e\ge q-1\). At rank two both graphs have edges and nonedges, and the two-round adjacency patterns can all be matched; rank one is trivial for nonempty loopless graphs. Thus, for \(d\ge2\), the *first* distinguishing rank is exactly \(d+2\), not merely at most that rank.

**Ranks one and two.** All graphs here are nonempty and irreflexive, so all rank-one sentences have the same truth value. For \(d\ge2\), every nonzero vector has distinct adjacent and nonadjacent nonzero partners: the functional \(B_d(x,-)\) is nonzero, and its kernel has \(2^{2d-1}\) members including \(0,x\), leaving at least six other nonzero partners. In a two-round game Duplicator can therefore match a repetition, an edge, or a nonedge. In \(S_1\), every pair of distinct vertices is an edge. This establishes the rank-two dichotomy.

The lower-bound argument separates every pair \(d<e\) with \(d<q-1\) using at most \(q\) moves. The upper-bound argument merges all \(d,e\ge q-1\). This proves the displayed exact classification and class count. Since \(S_d\) has \(2^{2d}-1\) vertices, the largest smallest representative, \(S_{q-1}\), gives the asserted optimal cardinality bound.

**Concrete rank-four boundary.** The graph \(S_2\) has no induced \(K_{1,3}\): any three pairwise orthogonal leaves in a nondegenerate four-dimensional space are dependent (the maximum isotropic dimension is two), so no vertex can pair to one with all three if their dependence has odd parity. More explicitly, any three *distinct* nonzero elements of a two-dimensional isotropic subspace sum to zero. Conversely, in \(S_3\), \(e_1,e_2,e_3\) are pairwise orthogonal independent vertices and \(f_1+f_2+f_3\) is adjacent to each, giving an induced claw. The graph-only existential induced-claw sentence has rank four, confirming the first separation between \(S_2\) and \(S_3\).

## Verification

A standalone Python 3 verifier, `verify.py`, constructs \(S_1,S_2,S_3\) directly from the alternating form. Separately from the symbolic game proof, it computes their exact root first-order types through rank four by recursively collecting all possible one-vertex extension types. Extension supports are computed by bitsets, and the program checks the induced-claw condition. Run `python3 verify.py` in a directory containing this file. The accompanying `verify_output.txt` records the reproduced output.

The finite calculation checks rank-two equivalence of \(S_2,S_3\), rank-three equivalence of \(S_2,S_3\), and their rank-four inequivalence. It also checks that \(S_1\) is separated from \(S_2\) by rank two and that \(S_2\) is claw-free whereas \(S_3\) contains a claw. The all-rank theorem is justified by the linear extension and game arguments, not by finite extrapolation.

## Relationship to prior work

Abiad and Haemers' *Switched symplectic graphs and their 2-ranks* (first made public 9 December 2014) defines precisely the binary symplectic graph used here and studies Godsil--McKay switching and binary matrix ranks; it also identifies the small \(3\)-, \(15\)-, and \(63\)-vertex examples. Its statements concern spectrum, switching, and graph isomorphism, not an exact first-order quantifier-rank classification across dimensions. Pikhurko and Verbitsky's *Logical complexity of graphs: a survey* (first public 25 March 2010) develops graph quantifier depth and Ehrenfeucht games in general. The present claim is a specialized exact all-depth comparison rather than a general definition of those methods.

The source comparisons do not establish absolute historical priority. In particular, a finite-model-theoretic treatment of binary symplectic form reducts or an unindexed equivalent game argument could imply the same theorem without mentioning the graph name. The literature comparisons identified no such covering statement in the sources inspected.

## Limitations

The proof is restricted to binary vector spaces and to pure undirected adjacency. The equivalence can fail at lower depth if a richer language explicitly names vector addition, the zero vector, the bilinear form, colors, or counting. No assertion is made about other characteristics or switched symplectic graphs. The finite verifier is supplementary, and neither it nor this manuscript constitutes independent formal proof certification or independent audit. Historical-priority coverage is necessarily incomplete.

## References

1. A. Abiad and W. H. Haemers, *Switched symplectic graphs and their 2-ranks*, arXiv:1412.2945, version 1 submitted 2014-12-09, https://arxiv.org/abs/1412.2945; *Designs, Codes and Cryptography* 81 (2016), 35–41, DOI:10.1007/s10623-015-0127-x. Particularly the introductory definition of \(\operatorname{Sp}(2d,2)\) and Section 2.
2. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, initially submitted 2010-03-25, https://arxiv.org/abs/1003.4865. Particularly Sections 1–3 on graph quantifier depth and Ehrenfeucht games.
