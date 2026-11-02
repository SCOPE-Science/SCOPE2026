# Three-variable field blindness for finite-dimensional subspace lattices

## Finding
For any fields \(F\) and \(K\) (finite or infinite) and any nonnegative integers \(d,e\), let \(\mathcal L_d(F)\) be the structure of **all linear subspaces** of \(F^d\), with **only equality and binary inclusion** \(\subseteq\). Then
\[
\mathcal L_d(F)\equiv_{\mathrm{FO}^3}\mathcal L_e(K)
\quad\Longleftrightarrow\quad d=e.
\]
Here \(\mathrm{FO}^3\) permits only three reusable variable symbols, **without any bound on quantifier rank**, and has no counting quantifiers. Consequently, two variables already recover ambient dimension, while even three cannot detect characteristic, field size, or whether the field is finite at fixed dimension. The field-blindness cutoff is sharp: four variables distinguish \(\mathcal L_2(\mathbb F_2)\) and \(\mathcal L_2(\mathbb F_3)\).

Every fixed dimension therefore has one three-variable theory across all fields. Within the finite-field subfamily the smallest structure representing the dimension-\(d\) theory is \(\mathcal L_d(\mathbb F_2)\), with \(\sum_{j=0}^{d}\binom{d}{j}_2\) elements, where \(\binom{d}{j}_2\) is the Gaussian binomial coefficient.

## Assumptions and scope
The ambient vector spaces have **finite dimension**; the fields themselves need not be finite. Dimensions include zero, whose subspace poset has one element. The language has no scalar sort, vectors, named bounds, lattice meet or join function symbols, rank predicates, or cardinality/counting quantifiers. Order comparison means ordinary subspace inclusion. The result is relative to this class of inclusion posets, not all lattices.

## Proof
**1. Two-subspace classification.** For two subspaces \(U,V\subseteq F^d\), write
\[
a=\dim U,\qquad b=\dim V,\qquad c=\dim(U\cap V).
\]
These three integers, together with ambient dimension \(d\), determine the isomorphism type of the **ordered pair** under the action of \(\mathrm{GL}_d(F)\). Explicitly, choose a basis of \(U\cap V\), extend it separately inside \(U\) and \(V\), and complete the union to a basis of \(F^d\). Such a pair exists if and only if \(0\le c\le\min(a,b)\) and \(a+b-c\le d\), independently of the field. Both equality and inclusion of the pair are determined by these dimensions.

**2. The field-independent three-subspace normal form.** For every ordered triple \(A,B,C\) of subspaces of a finite-dimensional vector space over **any field**, there is a direct-sum decomposition of the ambient space respecting all three subspaces into blocks of the following kinds:

* For every binary triple \(\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)\in\{0,1\}^3\), a one-dimensional block \(E_\epsilon\), on which its \(i\)-th distinguished subspace is \(E_\epsilon\) when \(\epsilon_i=1\) and zero otherwise.
* A two-dimensional block with basis \(u,v\), on which the three distinguished subspaces are \(\langle u\rangle\), \(\langle v\rangle\), and \(\langle u+v\rangle\), respectively.

Repetitions of these nine block types are permitted, including zero repetitions. This is the classical *three-subspaces problem*, or injective-arm part of the \(D_4\)-quiver classification. For clarity, its decomposition argument is elementary and field-independent: first split the triple intersection and, in turn, the remaining pairwise intersections by chosen complements; next split components belonging exclusively to one subspace or to none; in the residual summand the three subspaces meet pairwise in zero, each is contained in the sum of the other two, and the third is the graph of an isomorphism between the first two. Choosing a basis of either of the latter splits the residual triple into the stated two-dimensional diagonal blocks. Etingof et al., Section 5.3, Example 5.10, prove this by complements and linear projections; no algebraic closure, division by a field characteristic, or finiteness of the field is used.

In particular, if an ordered triple \((A,B,C)\) occurs in dimension \(d\) over \(F\), then **the same complete three-subspace incidence and dimension pattern** occurs in dimension \(d\) over any other field \(K\): reconstruct each block with the same multiplicity over \(K\).

**3. The unrestricted three-pebble strategy.** Fix \(d\) and arbitrary fields \(F,K\). Duplicator maintains the following invariant for the at most two pebbled subspaces remaining just before Spoiler moves a third pebble: corresponding subspaces have identical dimensions, and, if two are present, their intersections have equal dimensions. By Step 1, this is a valid matched pair profile, and a pair over \(K\) with those parameters is equivalent under a \(K\)-linear automorphism to any other such pair.

Suppose Spoiler selects a subspace \(W\) over \(F\), with remaining pebbled subspaces \(U,V\). Apply Step 2 to \((U,V,W)\), and transfer its block decomposition to dimension \(d\) over \(K\), obtaining \((U_*,V_*,W_*)\). Step 1 provides an automorphism sending \((U_*,V_*)\) to the two actual paired subspaces \((U',V')\) already pebbled over \(K\). Respond with the image \(W'\) of \(W_*\). Every pair among the three pebbled subspaces now has equal individual dimensions and equal intersection dimension on both sides. In particular, their equality and inclusion atomic diagrams agree. When one pebble is removed on the next move, the same invariant remains true. The one- or zero-pebble cases are obtained by omitting unused subspaces and use the same construction. Since there is **no decrease in an auxiliary parameter**, this strategy works through arbitrarily many moves, proving \(\mathcal L_d(F)\equiv_{\mathrm{FO}^3}\mathcal L_d(K)\). The strategy is symmetric when Spoiler selects from either structure.

**4. Necessity of equal dimensions using only two variables.** Write \(X\subsetneq Y\) for strict inclusion. With alternating variable symbols \(x,y\), define recursively \(\theta_0(x):=(x=x)\) and \(\theta_{r+1}(x):=\exists y\,(x\subsetneq y\land\theta_r(y))\); in the recursive occurrence, the variable symbols alternate by capture-avoiding renaming. This uses only two variables. The sentence \(\exists x\,\theta_{d+1}(x)\) holds in \(\mathcal L_e(K)\) exactly when \(e\ge d+1\), since the maximum strict chain has \(e+1\) subspaces. Thus unequal ambient dimensions are already distinguishable in \(\mathrm{FO}^2\). For dimensions equal to zero, the argument remains valid.

**5. Sharp four-variable boundary.** Over \(\mathbb F_2^2\), the three one-dimensional subspaces are the only members of an antichain of size three; no antichain has size four. Over \(\mathbb F_3^2\), the four distinct one-dimensional subspaces form a four-element antichain. The four-variable sentence \(\exists x\exists y\exists z\exists w\) asserting all six pairs are incomparable therefore distinguishes the two inclusion structures. Conversely, three-variable field blindness has just been established. This completes the theorem and the sharp variable bound.

## Verification
Two standalone standard-library Python programs implement complementary finite checks. `verify_extension_support.py` enumerates subspaces by reduced-row-echelon bases and records, for every two-subspace orbit, all possible third-subspace intersection-dimension triples. It compares supports over fields of orders \(2,3,5\) in dimensions \(1,2,3\), and orders \(2,3\) in dimension \(4\). `verify_three_pebble.py` independently enumerates subspaces by span closure and computes stable three-variable atomic-type refinements **using sets of reachable colours rather than counts** for dimensions \(1,2,3\) and multiple prime fields. It also verifies dimension-separating controls. Both returned `PASS`; exact outputs are embedded in the package as `extension_support_output.json` and `three_pebble_output.json`. Execute `python3 verify_extension_support.py` and `python3 verify_three_pebble.py` in a Python 3 standard-library environment. The finite tests check the pivotal local patterns but **do not establish the all-field, all-dimension theorem**; that is supplied by the proof above.

## Relationship to prior work
The classical \(D_4\)-quiver decomposition in Etingof et al., Section 5.3, supplies the triple-subspace normal form, but does **not** state an unrestricted-depth logical equivalence or a sharp variable-width boundary. Grohe and Otto develop plain pebble games and logic equivalence in general; their application concerns graph-isomorphism relaxations rather than subspace-inclusion lattices. Herrmann, Tsukamoto and Ziegler study coordinatization and consistency questions for modular lattices; their Section 3 uses full lattice operations and many-element frames, and does not imply the bounded-three-variable pure-inclusion result as stated. In particular, existence of definable field coordinatizations with many named parameters does not contradict field blindness with only three variable names.

A **bounded quantifier-rank-three** classification of these same inclusion structures cannot, merely from its conclusion, imply this theorem: the present statement covers every finite quantifier rank with three reusable variables, and differentiates every pair of ambient dimensions, not just a bounded cutoff. The implication comparison concerns the mathematical strength of the statements, not their titles. The novelty comparison is qualified: a general unlocated theorem about three-pebble equivalence of modular geometries could subsume the result.

## Limitations
Only finite **ambient dimension**, pure inclusion and noncounting first-order logic are claimed. No assertion is made for join/meet function symbols, named scalars, counting logic, or four-variable field blindness. No finite computational test proves the infinite statement. Historical-priority comparisons are necessarily non-exhaustive.

## References
1. P. Etingof, O. Golberg, S. Hensel, T. Liu, A. Schwendner, D. Vaintrob, E. Yudovina, *Introduction to Representation Theory*, arXiv:0901.0827, first public version 2009-01-07, Section 5.3, Example 5.10. https://arxiv.org/abs/0901.0827
2. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, CSL 2012, DOI:10.4230/LIPIcs.CSL.2012.289, 2012-09-03. https://doi.org/10.4230/LIPIcs.CSL.2012.289
3. C. Herrmann, Y. Tsukamoto, and M. Ziegler, *On the Consistency Problem for Modular Lattices and Related Structures*, arXiv:1607.03315, first posted 2016-07-12, especially Section 3. https://arxiv.org/abs/1607.03315
