# Complete real isometry groups and isometric classification of finite quadratic combinatorial Banach spaces

## Finding

Let \(n\ge 1\), let \(\mathcal F\) and \(\mathcal G\) be hereditary families of subsets of \([n]=\{1,\ldots,n\}\) containing all singletons, and define the real finite-dimensional norm
\[
 \|x\|_{\mathcal F,2}=
 \max_{F\in\mathcal F}\Bigl(\sum_{i\in F}x_i^2\Bigr)^{1/2}.
\]
For the set \(\mathcal M_{\mathcal F}\) of inclusion-maximal members (facets), define \(i\sim_{\mathcal F}j\) when \(i\in F\iff j\in F\) for every \(F\in\mathcal M_{\mathcal F}\), and call the equivalence classes *twin blocks*. The complete result is:

1. Every onto real linear isometry \(U:X_{\mathcal F,2}\to X_{\mathcal G,2}\) is orthogonal for the standard Euclidean inner product.
2. Such an isometry exists if and only if there is a coordinate permutation \(\sigma\) carrying \(\mathcal F\) onto \(\mathcal G\) (equivalently carrying facets onto facets). Every isometry factors as \(U=OP_{\sigma}\), where \(O\) is the direct sum of arbitrary orthogonal maps on the twin blocks of \(\mathcal G\). Every such factorization is an isometry.
3. For \(\mathcal F=\mathcal G\), let \(\mathcal H_{\mathcal F}\) be the hypergraph whose vertices are the twin blocks and whose hyperedges are the facets viewed as unions of these blocks, with vertex weights \(|B|\). The full group is
\[
\operatorname{Isom}_{\mathbb R}(X_{\mathcal F,2})
 \cong\Bigl(\prod_{B}O(|B|)\Bigr)
 \rtimes\operatorname{Aut}(\mathcal H_{\mathcal F},|B|),
\]
where the finite automorphism group preserves the displayed vertex weights. Its identity component is \(\prod_{B}SO(|B|)\), of real Lie dimension
\[
\sum_B\frac{|B|(|B|-1)}2.
\]

## Assumptions and scope

All scalars are **real** and dimensions are positive and finite. The family contains every singleton, so each coordinate lies in at least one facet. The maps classified are **surjective linear isometries** (not general into-isometries); metric surjective isometries between these normed spaces are affine by Mazur–Ulam, so the linear classification also handles them after translation. No assertion is made for infinite families or for exponents other than two. Identical facet-incidence, not mere shared membership in some facet, defines a twin block.

## Proof

**(A) Quadratic branches are intrinsic.** Write \(q_F(x)=\sum_{i\in F}x_i^2=x^TD_Fx\), with \(D_F\) the diagonal projection onto \(F\). Since facets form an antichain, for each facet \(F\), the vector \(\mathbf 1_F\) satisfies
\[
q_F(\mathbf 1_F)=|F|>|F\cap H|=q_H(\mathbf 1_F)
\quad(H\in\mathcal M_{\mathcal F},\ H\ne F).
\]
Thus \(q_F\) is the unique active quadratic branch on a nonempty open set. If \(U\) is a linear onto isometry, then throughout this open set \(q_F(x)=\max_{G\in\mathcal M_{\mathcal G}}q_G(Ux)\). Consequently the open set is covered by finitely many zero sets of the polynomials \(q_F-q_G\circ U\). A nonzero polynomial has a zero set with empty interior, hence one equality holds identically. The map from source facets to target facets is injective, since \(U\) is invertible and the target quadratic forms are distinct. Repeating with \(U^{-1}\) makes it a bijection. After indexing matched facets, for every pair \((F,G)\) one has the *matrix identity*
\[
U^TD_GU=D_F.\tag{1}
\]
These identities also show why merely matching the number of facets is insufficient.

**(B) Normalize the canonical incidence form.** Put \(R_{\mathcal F}=\sum_{F\in\mathcal M_{\mathcal F}}D_F=\operatorname{diag}(d_1,\ldots,d_n)\), and define \(R_{\mathcal G}\) similarly. Every \(d_i\ge1\) by singleton coverage, so both matrices are invertible. Summing (1) gives \(U^TR_{\mathcal G}U=R_{\mathcal F}\). Thus
\[
Q=R_{\mathcal G}^{1/2}UR_{\mathcal F}^{-1/2}
\quad\text{satisfies}\quad Q^TQ=I.\tag{2}
\]
Equation (1), conjugated by the two square roots, states that \(Q\) simultaneously orthogonally conjugates the commuting diagonal families \(\{R_{\mathcal F}^{-1/2}D_FR_{\mathcal F}^{-1/2}\}_F\) and \(\{R_{\mathcal G}^{-1/2}D_GR_{\mathcal G}^{-1/2}\}_G\), with their established facet matching.

**(C) Recover twin blocks from the joint eigenvalues.** The coordinate-\(i\) joint eigenvalue tuple in the source is
\[
\Bigl(\frac{\mathbf1_{\{i\in F\}}}{d_i}\Bigr)_{F\in\mathcal M_{\mathcal F}}.
\]
Two such tuples coincide exactly for twin coordinates: their positive-index supports coincide, forcing equal facet-incidence and then equal positive degrees. The same applies in the target. Since \(Q\) is orthogonal and intertwines these diagonal operators, it bijectively maps each source twin block's coordinate subspace onto a target twin block of the same dimension **and the same degree**. Therefore, for a matched block, the factors \(R_{\mathcal F}^{1/2}\) and \(R_{\mathcal G}^{-1/2}\) in \(U=R_{\mathcal G}^{-1/2}QR_{\mathcal F}^{1/2}\) cancel. Hence \(U=Q\) is itself orthogonal and maps twin blocks orthogonally onto twin blocks.

**(D) Permutation rigidity across families.** Choose a bijection of coordinate labels between each matched pair of equally sized twin blocks. It gives a permutation \(\sigma\) carrying every source facet onto its matched target facet, because facets are unions of complete twin blocks; maximal sets determine the hereditary families. Thus \(P_\sigma\) is an isometry and \(O=UP_\sigma^{-1}\) preserves every target twin block orthogonally. Conversely any such \(OP_\sigma\) preserves each facet's sum of coordinate squares, so it preserves their maximum. This proves statements 1 and 2, including both directions of the isometric-isomorphism criterion.

**(E) Group structure.** An automorphism of the weighted quotient facet hypergraph permutes twin blocks of equal cardinality; after choosing an ordering within each block, this action has a genuine permutation-matrix section. Its kernel is precisely the independent orthogonal group on every twin block. This establishes the semidirect product and the stated identity component and Lie dimension. For singleton blocks, \(O(1)=\{\pm1\}\) and \(SO(1)\) is trivial. The edge case of one facet \([n]\) reduces correctly to \(O(n)\).

## Verification

The proof above is exact and uniform in the number and shape of facets; it does not depend on sampled examples. `check_examples.py` uses only standard-library exact rational arithmetic. It exhausts all \(126\) covering facet antichains in dimensions \(1\) through \(4\), performs \(4{,}545\) exact input-vector checks of \(3/5\)-\(4/5\) rotations within twin blocks, and compares structural coordinate-permutation automorphisms with norm preservation on an integer grid for \(2{,}795\) permutations. Those finite tests support the implementation of definitions but are not proofs for arbitrary dimension or arbitrary real inputs.

For illustration, the two facets \(\{1,2,3\}\) and \(\{1,2,4\}\) give three twin blocks \(\{1,2\},\{3\},\{4\}\): continuous rotations may mix coordinates \(1,2\), while an independent permutation can exchange \(3,4\). Coordinates \(1,3\) cannot be continuously mixed despite lying together in one facet, because their complete facet-incidence signatures differ.

## Relationship to prior work

Fakhoury (2023), arXiv:2305.13125v1, proves signed-permutation rigidity for the \(p\)-convexified setting when \(p\ne2\), gives an explicit rotating example at \(p=2\) (Example 1.2), and in Proposition 4.1 supplies the criterion for when all complex \(p=2\) isometries are signed permutations, acknowledging an earlier real criterion by Brech and Tcaciuc. The present finite **real** result addresses the complementary nonrigid cases by identifying every continuous orthogonal block, classifying all between-family isometries, and determining the full group and connected dimension; these conclusions are not stated in the inspected results. Brech–Ferenczi–Tcaciuc (2019/2020) address the original unconvexified combinatorial norm (rather than quadratic convexification), including between-family isometries. Kalton–Wood (1976) develop general Hilbert-component machinery for **complex** Banach-space isometries, related to the block phenomenon but not an explicit real finite facet-hypergraph classification.

## Limitations

There is no independent external mathematical audit. Existing general theory of Hilbertian components might allow a short alternative derivation, and an unpublished Brech–Tcaciuc manuscript cited by Fakhoury was not available for a full comparison; the originality assessment is relative to inspected public statements, not a guarantee of uniqueness. The statement is restricted to finite **real** quadratic combinatorial norms and onto maps. The finite code does not establish the theorem; the proof is the open-set polynomial argument and the joint-eigenspace calculation.

## References

1. M. Fakhoury, *Isometries of p-convexified combinatorial Banach spaces*, arXiv:2305.13125v1 (first public May 22, 2023), https://arxiv.org/html/2305.13125v1, especially Example 1.2 and Section 4, Proposition 4.1.
2. C. Brech, V. Ferenczi, and A. Tcaciuc, *Isometries of combinatorial Banach spaces*, arXiv:1907.06815 (2019), https://arxiv.org/abs/1907.06815.
3. N. J. Kalton and G. V. Wood, *Orthonormal systems in Banach spaces and their applications*, Math. Proc. Cambridge Philos. Soc. 79 (1976), 493–510.
