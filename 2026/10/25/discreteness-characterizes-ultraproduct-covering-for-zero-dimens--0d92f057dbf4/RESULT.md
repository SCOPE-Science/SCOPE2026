# Discreteness characterizes ultraproduct covering for zero-dimensional sheaf topoi

## Finding

**Theorem.** Let \(X\) be a zero-dimensional Hausdorff space, possibly empty. Give the category of set-valued sheaves \(\mathbf{Sh}(X)\) its cartesian monoidal product and the usual (epimorphism, monomorphism) factorisation system. Then \(\mathbf{Sh}(X)\) has the **ultraproduct covering property** precisely when \(X\) is discrete.

There is a point-local strengthening. For every nonisolated point \(x\in X\), a single family of *constant* two-summand diagrams already violates the second comparison arrow. Specifically, there is an index set \(I\), an ultrafilter \(\mathcal U\) on \(I\), and constant families \(A_i=B_i=1\) for which the canonical arrow
\[
\rho:\left(\prod_{i\in I}1/\mathcal U\right)\amalg\left(\prod_{i\in I}1/\mathcal U\right)
\longrightarrow\prod_{i\in I}(1\amalg1)/\mathcal U
\]
is not surjective on the stalk at \(x\). If \(X\) is discrete, this arrow and the corresponding comparison for all other families are isomorphisms.

## Assumptions and scope

Here **zero-dimensional** means there is a basis of clopen subsets, and **Hausdorff** means distinct points admit disjoint open neighbourhoods. No compactness, countability, metrizability, local compactness or first-countability assumption is imposed. We work in ordinary set-based topology and use the ultrafilter lemma (available in ZFC).

For a set \(I\), ultrafilter \(\mathcal U\) and family of sheaves \((F_i)_{i\in I}\), its categorical ultraproduct is the filtered colimit
\[
\prod_{i\in I}F_i/\mathcal U
:=\mathop{\mathrm{colim}}_{J\in\mathcal U}\ \prod_{i\in J}F_i,
\]
where the transition maps are projections under reverse inclusion. Kamsma--Tendas' property requires, for all such ultrafilters and all sheaf pairs \((A_i),(B_i)\), that both \(0\to\prod_i0/\mathcal U\) and the binary-coproduct comparison above belong to the epimorphism class. Epimorphisms in \(\mathbf{Sh}(X)\) are precisely the maps surjective on every stalk. The notation \(1\amalg1\) denotes the locally constant two-element sheaf, whose sections over \(W\subseteq X\) are locally constant maps \(W\to\{0,1\}\).

## Proof

**1. The discrete direction.** If \(X\) is discrete then \(\mathbf{Sh}(X)\cong\mathbf{Set}^{X}\), and limits, coproducts and filtered colimits are computed at each point. In \(\mathbf{Set}\), an ultrafilter selects exactly one side of a finite partition: any element of \(\prod_i(A_i\amalg B_i)/\mathcal U\) has a representative whose \(A\)-tagged or \(B\)-tagged index set belongs to \(\mathcal U\). Restricting to that set gives an element of the corresponding summand ultraproduct. Different summands have disjoint images, and equality within a summand is exactly equality on an ultrafilter-large index set. Thus the coproduct comparison is bijective for every pair of families. Products of nonempty indexed families of empty sets are empty, so the initial-object comparison is also an isomorphism. Consequently both arrows are isomorphisms pointwise, as claimed.

**2. An ultrafilter following all neighbourhood scales.** Suppose \(x\in X\) is nonisolated. Let \(I\) be the set of all clopen neighbourhoods of \(x\). For each \(V\in I\) set
\[
T_V:=\{U\in I:U\subseteq V\}.
\]
Any finite intersection of such tails contains the intersection of the corresponding clopen neighbourhoods. Hence the tails have the finite-intersection property. Extend the filter they generate to an ultrafilter \(\mathcal U\). For every \(J\in\mathcal U\),
\[
\bigcap_{U\in J}U=\{x\}.\tag{1}
\]
Indeed all \(U\in I\) contain \(x\). For \(y\neq x\), zero-dimensionality and Hausdorff separation supply \(V\in I\) with \(y\notin V\). As \(J\cap T_V\neq\varnothing\), some \(U\in J\) excludes \(y\), proving (1). Because \(x\) is nonisolated, no neighbourhood of \(x\) can be contained in the singleton on the right.

**3. A binary-sheaf germ outside the comparison image.** Put \(C:=1\amalg1\). Every clopen \(U\in I\) defines a global section \(s_U:X\to\{0,1\}\) of \(C\): value \(1\) on \(U\), value \(0\) off \(U\). These sections form a global section of the product sheaf \(\prod_{U\in I}C\), hence a section \(s\) of its ultraproduct. Since all terminal-object products and their filtered colimits remain terminal, the source of the comparison is just \(C\), and its image consists of the two constant sections, labelled \(0\) and \(1\).

We show the germ \(s_x\) equals neither constant germ. Stalk functors preserve filtered colimits, so equality of \(s_x\) with either constant germ would hold at some stage \(\prod_{U\in J}C\) for \(J\in\mathcal U\). At that stage, equality of germs of product-sheaf sections means there is **one common** open neighbourhood \(W\ni x\) on which every coordinate section \(s_U\), for \(U\in J\), equals the same constant value. Equality with \(0\) is impossible since \(s_U(x)=1\) for every \(U\). Equality with \(1\) would imply
\[
W\subseteq\bigcap_{U\in J}U=\{x\},
\]
contradicting nonisolation. Thus \(s_x\) lies outside the image of \(\rho_x\), so \(\rho\) is not epi. A nondiscrete space has at least one nonisolated point, completing the equivalence.

**4. Boundary cases.** An infinite discrete space satisfies the property, just as a finite discrete space does. Any nondiscrete zero-dimensional Hausdorff space fails it, whether compact (such as Cantor space) or noncompact (such as the rationals with their usual topology). For the empty space, the sheaf category has one object and all indicated comparisons are isomorphisms.

## Verification

The critical steps are categorical rather than numerical. The tail-family intersection is checked by clopen separation and the ultrafilter finite-intersection property. The comparison source reduces to \(C\) because ultraproducts of terminal sheaves are terminal. The target has a global section from the family of characteristic maps \((s_U)\). The key obstruction uses the order of operations: **a stalk of a product sheaf requires one neighbourhood for all coordinates**, not independently chosen neighbourhoods. Filtered-colimit equality then supplies a single ultrafilter-large coordinate set \(J\), giving the contradiction (1). These calculations are valid for arbitrary, including uncountable, neighbourhood bases. No finite experiment is offered as an infinite proof.

## Relationship to prior work

Kamsma and Tendas, *The Compactness Theorem for Enriched Logic*, Definition 4.2, define the ultraproduct covering property. Their Example 9.9 proves failure for sheaves over Cantor space using two varying subterminal families, while Theorem 8.2 gives a separate sufficient criterion. Kanalas' 2026 lecture slides discuss failure over \(\mathbb R\) and, in Example 2, use the global sections of \(1\amalg1\) on Stone spaces associated with **arbitrary infinite Boolean algebras**. Thus the negative Stone-space case is **not** claimed as new. The present result gives a single iff criterion for all zero-dimensional Hausdorff spaces, including noncompact/nonmetrizable bases and arbitrary isolated-point patterns, and a pointwise, constant-two-sheaf witness at each nonisolated point. This is an extension of the known obstruction, not a claim that the obstruction was first discovered here.

## Limitations

This is a theorem about the ultraproduct covering property for the specified factorisation system, not a proof or disproof of enriched compactness on each such sheaf topos. Other structural assumptions of enriched logic may fail in noncoherent or noncompact settings. Zero-dimensional Hausdorff is essential to this particular characteristic-section argument; no classification for all topological spaces or for alternative factorisation systems is asserted. Prior generalizations formulated using localic or topos-theoretic language may subsume parts of the result; historical completeness is not independently certified.

## References

1. M. Kamsma and G. Tendas, *The Compactness Theorem for Enriched Logic*, arXiv:2610.23278v1 (first public 16 October 2026), especially Definition 4.2, Theorem 8.2, and Example 9.9. https://arxiv.org/html/2610.23278v1
2. K. Kanalas, *Realizing types in topos-valued models*, Making Categorical Model Theory Accessible, Masaryk University (2026), examples on slide pages 12–13 of 24 (PDF pages 23–25). https://www.markkamsma.nl/making-categorical-model-theory-accessible/slides/kanalas.pdf
