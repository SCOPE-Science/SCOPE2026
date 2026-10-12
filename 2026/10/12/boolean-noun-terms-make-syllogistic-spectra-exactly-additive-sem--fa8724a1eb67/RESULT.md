# Boolean noun terms make syllogistic spectra exactly additive semigroups
## Finding
Let \(S^{\dagger}_{\mathrm{BoolN}}(card)\) be the finite-model extension of \(S^{\dagger}(card)\) in which noun terms are generated from raw nouns by binary union and complement, while sentences retain exactly the four forms \(\forall(x,y)\), \(\exists(x,y)\), \(\exists^{\geq}(x,y)\), and \(\exists^{>}(x,y)\). For a theory \(\Gamma\), let
\[
\operatorname{Spec}(\Gamma)=\{n\in\mathbb{N}^{+}:\Gamma\text{ has an }n\text{-element model}\}.
\]
Then the spectra of arbitrary \(S^{\dagger}_{\mathrm{BoolN}}(card)\)-theories are exactly \(\varnothing\) and the nonempty additive subsemigroups of \((\mathbb{N}^{+},+)\). Moreover, every nonempty additive subsemigroup is the spectrum of a finite theory.

This completes the noun-level extension direction opened by Jiang's example \(\operatorname{Spec}(\Lambda_3)=\{3k:k\in\mathbb{N}^{+}\}\): noun-level Boolean closure does not merely add higher divisibility tests; it yields precisely all positive additive semigroups as universe-cardinality spectra.

## Assumptions and scope
Models are finite sets equipped with interpretations of raw nouns. Complement is interpreted relative to the universe and union as set union. A Boolean noun term is any finite term obtained from raw nouns by these two operations. Intersections are therefore definable by De Morgan duality. The sentence semantics are those of \(S^{\dagger}(card)\): inclusion, nonempty intersection, non-strict cardinality comparison, and strict cardinality comparison. The spectrum records positive universe cardinalities only.

No propositional connectives are added at sentence level. The theorem concerns theory spectra, where a theory is an arbitrary set of sentences; the realizing theories constructed below are finite.

## Proof
First prove the necessary closure. Let \(\mathfrak M_1\) and \(\mathfrak M_2\) be disjoint finite models of the same theory \(\Gamma\). Form their disjoint union \(\mathfrak M=\mathfrak M_1\sqcup\mathfrak M_2\) by interpreting each raw noun componentwise. By structural induction on Boolean noun terms \(t\),
\[
t^{\mathfrak M}=t^{\mathfrak M_1}\sqcup t^{\mathfrak M_2}.
\]
The union step is immediate. For complement, disjointness gives
\[
(M_1\sqcup M_2)\setminus(A_1\sqcup A_2)
=(M_1\setminus A_1)\sqcup(M_2\setminus A_2).
\]
Hence each of the four sentence forms is preserved. Inclusions and intersections are componentwise. For cardinality comparisons, cardinalities add across the disjoint components; if both summands satisfy \(\geq\), their sums do, and if both satisfy \(>\), their sums do. Therefore \(\mathfrak M\models\Gamma\). Thus, whenever \(m,n\in\operatorname{Spec}(\Gamma)\), also \(m+n\in\operatorname{Spec}(\Gamma)\). Every nonempty spectrum is an additive subsemigroup of \(\mathbb{N}^{+}\); contradictory theories realize \(\varnothing\).

For the converse, let \(S\subseteq\mathbb{N}^{+}\) be a nonempty additive subsemigroup. It is finitely generated. Indeed, let \(a=\min S\). For every residue \(r\pmod a\) occurring in \(S\), choose the least \(m_r\in S\) with that residue. If \(s\in S\) has residue \(r\), then \(s=m_r+qa\) for some \(q\in\mathbb{N}\). Conversely, closure under addition puts every \(m_r+qa\) in \(S\). Hence a finite set of positive generators \(g_1,\ldots,g_k\) exists.

Put \(m=\sum_{i=1}^k g_i\). Choose \(r\geq1\) with \(2^r\geq m\), and take raw nouns \(p_1,\ldots,p_r\). Their \(2^r\) Boolean atoms are the terms obtained by intersecting, for each \(j\), either \(p_j\) or its complement. These atoms are pairwise disjoint and partition every universe. Select exactly \(m\) atoms and split them into blocks \(B_1,\ldots,B_k\) with \(|B_i|=g_i\).

For every unused atom \(U\), include \(\forall(U,\bar U)\), which forces \(U=\varnothing\). For every block \(B_i\), choose a representative atom \(R_i\), and for each \(A\in B_i\) include both
\[
\exists^{\geq}(A,R_i)\quad\text{and}\quad\exists^{\geq}(R_i,A).
\]
Thus all atoms in \(B_i\) have a common size \(t_i\in\mathbb{N}\). Since the atoms partition the universe and all unused atoms are empty, every positive-cardinality model has
\[
|M|=\sum_{i=1}^k g_i t_i,
\]
with not all \(t_i\) equal to zero. Therefore every model size belongs to \(S\).

Conversely, for \(n\in S\), choose \(t_1,\ldots,t_k\in\mathbb{N}\), not all zero, such that \(n=\sum_i g_i t_i\). Partition an \(n\)-element universe into the selected Boolean atoms so that every atom of \(B_i\) has size \(t_i\), leaving unused atoms empty. Interpret each raw noun \(p_j\) as the union of the atom-parts whose \(j\)-th bit is one. The resulting Boolean atoms are exactly the prescribed parts, so the finite theory is satisfied. Hence its spectrum is exactly \(S\).

## Verification
The proof was replayed at the level of definitions. The only algebraic input is the elementary finite-generation lemma for additive subsemigroups of \(\mathbb{N}^{+}\), proved above by least representatives modulo the least positive element. The model construction uses only finite Boolean partitions and mutual non-strict cardinality comparisons. No finite experiment is used as a substitute for the general proof.

Boundary checks include: empty spectra are allowed separately; zero is not a spectrum element because spectra are subsets of \(\mathbb{N}^{+}\); block sizes \(t_i\) may be zero, which is necessary for arbitrary nonnegative generator combinations; and the all-zero choice cannot occur in a positive-cardinality model because the Boolean atoms partition the universe.

## Relationship to prior work
Jiang proves that the base language has only empty spectra, tails, and even tails, and observes that noun-level union together with complement can express divisibility by three via a concrete theory \(\Lambda_3\). Section 5.1 explicitly identifies noun-level union/intersection as an expressive extension, but it does not classify its spectra. The theorem above supplies that classification.

Kisby, Blanco, Kruckman, and Moss study syllogistic size logics with union or intersection terms and prove soundness, completeness, and polynomial-time decidability for those fragments. Their terms do not combine union/intersection with term complement, and their paper does not study finite-model spectra; its concluding discussion identifies integrating these resources as a further step.

Manière and Przybyłko prove an analogous additive-semigroup phenomenon for spectra of concept-cardinality query answers over \(\mathcal{ALCIF}\) knowledge bases. That result concerns the possible cardinalities of a designated concept across models in a substantially different description-logic formalism, including infinite answer value \(\infty\); it does not imply a classification of universe sizes realizable by the much smaller syllogistic theory language considered here. Its presence is nevertheless an important comparison: additive closure is a recurring structural signature of disjoint-union constructions, while the realization argument here is specific to finite Boolean noun atoms.

## Limitations
The theorem classifies theory spectra only for finite models and only when sentence syntax remains the four atomic syllogistic forms. Adding sentence-level Boolean connectives can destroy simple additive closure. The construction is existential and can use exponentially many Boolean atoms relative to the number of raw nouns; no claim of optimal formula size or decision complexity is made. The result does not classify spectra over infinite cardinalities.

## References
1. R. Jiang, “Finite Spectra of Syllogistic Logic with Cardinality Comparisons,” arXiv:2609.24902v1, 2026. In particular, Theorem 1.3, Lemmas 3.7–3.8, and Section 5.1.
2. C. Kisby, S. A. Blanco, A. Kruckman, and L. S. Moss, “Logics for Sizes with Union or Intersection,” Proceedings of the AAAI Conference on Artificial Intelligence 34(03), 2870–2876, 2020. DOI: 10.1609/aaai.v34i03.5677.
3. Q. Manière and M. Przybyłko, “Spectra of Cardinality Queries over Description Logic Knowledge Bases,” arXiv:2412.12929v1; Proceedings of AAAI 39(14), 15067–15074, 2025. DOI: 10.1609/aaai.v39i14.33652.
4. L. S. Moss and S. Topal, “Syllogistic Logic with Cardinality Comparisons, on Infinite Sets,” Review of Symbolic Logic 13(1), 1–22, 2020. DOI: 10.1017/S1755020318000126.
