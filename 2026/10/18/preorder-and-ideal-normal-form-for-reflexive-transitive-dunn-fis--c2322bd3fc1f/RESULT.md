# Preorder-and-ideal normal form for reflexive-transitive Dunn–Fischer–Servi star frames

## Finding

For every integer \(m\geq2\), let \(X_m=\{r\}\sqcup L\), where \(|L|=m\), with the rooted-star order \(r<\ell\) for every \(\ell\in L\) and no distinct comparable leaves. A relation \(R\subseteq X_m^2\) is **admissible** when it is reflexive and transitive and satisfies the three forest-frame inclusions (FS1), (FS2), and (CJ2) defined below.

**Normal-form theorem.** Admissible relations are in bijection with triples \((Q,I,\varepsilon)\) having:

1. a preorder \(Q\) on \(L\);
2. a predecessor-closed subset \(I\subseteq L\), meaning \(xQy\) and \(y\in I\) imply \(x\in I\);
3. a flag \(\varepsilon\in\{0,1\}\), where \(\varepsilon=1\) is permitted exactly when the quotient poset of \(Q\) has a greatest element.

Given a triple, let \(T\subseteq L\) denote that greatest preorder-equivalence class when \(\varepsilon=1\), and let \(T=\varnothing\) otherwise. The complete relation is
\[
R=\{(r,r)\}\cup Q\cup(I\times\{r\})\cup(\{r\}\times T).
\]
Thus the nonempty root-to-leaf target set, when present, is forced to be the *entire* greatest equivalence class of the leaf preorder, not an arbitrary subset.

Write \(p_k\) for the number of partial orders on a specified \(k\)-element set, and \(a_k=\sum_{P\in\mathrm{Pos}(k)}|\operatorname{Id}(P)|\), summing the number of order ideals over all such labeled posets. Set \(p_0=a_0=1\). The exact number \(L_m\) of admissible relations on a fixed labeled rooted star is
\[
L_m=\sum_{k=1}^{m}\left\{\begin{matrix}m\\k\end{matrix}\right\}
\bigl(a_k+k(a_{k-1}+p_{k-1})\bigr),
\]
where braces denote Stirling numbers of the second kind. This finite sum applies for every \(m\geq2\).

There is also an exact ordinary generating function for isomorphism types. Sum over isomorphism classes \([P]\) of finite posets, **including the empty poset**, and write \(\gamma(P)=1\) if \(P\) has a greatest element and \(0\) otherwise. Let \(j_\sigma(P)\) count the order ideals of \(P\) invariant under \(\sigma\in\operatorname{Aut}(P)\). Then the number \(U_m\) of isomorphism types is the coefficient of \(z^m\) in
\[
U(z)=\sum_{[P]}\frac{1+\gamma(P)}{|\operatorname{Aut}(P)|}
\sum_{\sigma\in\operatorname{Aut}(P)}
 j_\sigma(P)\prod_{C\in\operatorname{Cyc}(\sigma)}
 \frac{z^{|C|}}{1-z^{|C|}}.
\]
The series is locally finite: a poset with \(k\) elements only contributes terms of degree at least \(k\).

For \(m=2,3,4,5\), respectively, the exact labeled counts are \(20,189,3084,81536\), and the isomorphism counts are \(13,50,232,1303\). The one-leaf base case, although not genuinely branching, has four relations and four isomorphism classes.

## Assumptions and scope

Relation composition is \((S\circ T)(x,z)\) iff there exists \(y\) with \(xSy\) and \(yTz\). The relevant frame conditions of Flaminio–Godo–Menchón–Rodríguez (Definition 6.11) are
\[
\begin{aligned}
\mathrm{(FS1)}\quad &(\leq\circ R)\subseteq(R\circ\leq),\\
\mathrm{(FS2)}\quad &(R\circ\geq)\subseteq(\geq\circ R),\\
\mathrm{(CJ2)}\quad &(\geq\circ R)\subseteq(R\circ\geq).
\end{aligned}
\]
The original order \(\leq\) is a partial order; the *modal* relation \(R\) is assumed reflexive and transitive, and may have nontrivial equivalence clusters. Each admissible relation is counted separately on labeled leaves, whereas isomorphism preserves the rooted-star order and the relation simultaneously. No symmetry exchanges the distinguished root with a leaf.

The underlying order is a finite forest in the convention that principal downsets are chains. The 2021 representation theorem (Proposition 6.12) supplies the connection with Dunn–Fischer–Servi Gödel algebras with operators; its general theorem and modal frame conditions are prior work, not part of the claimed contribution. The new claim is the reflexive-transitive star-specific normal form, the exact Stirling-transform count, and the isomorphism generating function.

## Proof

**Step 1: reduce three relational conditions to one star condition.** Reflexivity ensures \(rRr\) and \(xRx\) for every leaf. On a rooted star, (FS1) is then automatic: whenever \(r\leq xRy\), the root loop \(rRr\), followed by \(r\leq y\), provides the required witness; all other instances are tautological. Likewise (FS2) is automatic: the only nontrivial lowering of a target leaf is to \(r\); if the source is a leaf, the root loop gives a witness at a predecessor of that source, and if the source is \(r\), its own loop is a witness. Thus (CJ2) is the only remaining condition. Put \(T=\{t\in L:rRt\}\). The only nontrivial instances of (CJ2) have source a leaf \(x\), intermediate source \(r\), and target \(t\in T\). Since a leaf has no strict successor, (CJ2) is equivalent to
\[
\forall x\in L\;\forall t\in T:\quad xRt.
\]
Its requirement for target \(r\) follows from reflexivity of each leaf.

**Step 2: extract the triple.** Restrict \(R\) to \(L\times L\), calling the result \(Q\). Reflexivity and transitivity of \(R\) imply that \(Q\) is a preorder. Let \(I=\{x\in L:xRr\}\). If \(xQy\) and \(y\in I\), transitivity gives \(xRr\), proving that \(I\) is predecessor-closed. If \(T\ne\varnothing\), Step 1 makes every \(x\in L\) relate to every member of \(T\). If \(t\in T\), \(tQy\), and \(y\in L\), the arrows \(rRt\) and \(tRy\) imply \(rRy\), so \(y\in T\). Hence all elements of \(T\) are mutually \(Q\)-equivalent, and nothing in \(T\) accesses a leaf outside \(T\); they form the unique greatest equivalence class of \(Q\). Thus \(T\) is either empty or precisely that class. This determines \(\varepsilon\) uniquely.

**Step 3: reconstruct the relation.** Conversely, start with a triple as stated and use the displayed definition of \(R\). Reflexivity is immediate. Transitivity wholly inside \(L\) follows from \(Q\); two-step paths ending at the root use predecessor closure of \(I\). Paths beginning at the root and continuing through a leaf in \(T\) stay inside \(T\), by maximality of the greatest preorder class. Paths passing from a leaf through the root and then to \(T\) close because every leaf already accesses that greatest class. All remaining two-step paths contain only loops or an immediate edge. Hence \(R\) is transitive. Step 1 now proves (FS1), (FS2), and (CJ2). The construction recovers the extracted \((Q,I,\varepsilon)\), so the correspondence is bijective.

**Step 4: count labeled relations.** Partition \(L\) into its \(k\) equivalence classes under \(Q\). There are \(\left\{\begin{smallmatrix}m\\k\end{smallmatrix}\right\}\) such partitions, and, for each, choosing \(Q\) amounts exactly to choosing a partial order \(P\) on those \(k\) distinct blocks. Predecessor-closed choices of \(I\) correspond to order ideals of \(P\). The flag has one possible value without a greatest block, and two with one. The contribution of the unflagged choice is therefore \(a_k\). To count the extra flagged choice, pick its greatest block (\(k\) choices), delete it, and select an arbitrary poset \(P'\) on the remaining blocks. Its ideals are exactly the ideals of \(P'\) plus the full set of \(k\) blocks, since any ideal containing the greatest block contains everything. Summing gives \(k(a_{k-1}+p_{k-1})\). Summing over \(k\) proves the labeled formula.

**Step 5: count isomorphism classes.** Up to relabeling of leaves, a preorder is a finite poset \(P\) of equivalence classes with positive integer multiplicity \(w(v)\) at each vertex. The predecessor-closed set is an order ideal of \(P\), and the root-target flag is optional exactly when \(P\) has a greatest vertex. The remaining symmetry group is \(\operatorname{Aut}(P)\). For an automorphism \(\sigma\), the fixed ideals number \(j_\sigma(P)\). Fixed multiplicity functions are constant on each cycle \(C\) and have generating series \(z^{|C|}/(1-z^{|C|})\) for that cycle. Burnside's lemma, together with the optional top flag, gives the displayed formula. Every isomorphism class has exactly one such orbit description, so there is no overcounting.

## Verification

The companion `verify.py` executes two separate enumerations. First it enumerates **all reflexive relations** on rooted stars with \(1\) through \(4\) leaves, tests transitivity and all three displayed relational inclusions directly, and compares their truth value with the triple criterion. It also evaluates permutation-fixed relations to obtain direct isomorphism counts. Second, it enumerates partial orders by unordered-pair orientation choices through five vertices; counts their ideals; applies the Stirling formula; and independently computes the unlabelled generating-function coefficients through five leaves using canonical posets and automorphism cycles. Both methods agree wherever their ranges overlap. The recorded output terminates with `VERIFY_OK`.

The finite enumerations independently check examples and the equivalence for small sizes; the unrestricted theorem follows from Steps 1–5, not from finite experimentation.

## Relationship to prior work

Flaminio, Godo, Menchón and Rodríguez (2021), Sections 5–6, define the Dunn and Fischer–Servi modal forest conditions and their representation. In particular their Definition 6.11 identifies exactly the three relational inclusions used here, and their Proposition 6.12 reconstructs the associated algebra from such a frame. The present result adds modal reflexivity and transitivity, specializes to the first genuinely branching rooted forest, and gives a preorder/ideal classification and exact labeled and unlabeled counts; those specialized results are not stated in the inspected material.

Balbiani, Diéguez, Fernández-Duque and McLean (2024 initial version; 2026 revision) study several constructive and Gödel \(\mathsf{S4}\) logics through general birelational confluence and finite-frame properties. Their frame semantics motivate the S4-style preorder restriction, but their completeness and finite-model results do not themselves enumerate Dunn–Fischer–Servi rooted stars or imply the displayed coefficients without a separate classification. Earlier enumerations of modal chain frames are over total intuitionistic orders rather than a branching rooted star, and are not an instance of this classification.

## Limitations

The theorem treats only a fixed rooted star with at least two leaves, plus the one-leaf consistency check. It does not classify arbitrary finite forests, all Gödel modal expansions, or all constructive S4 frames. Its modal relation may have nontrivial clusters. The equations in the underlying algebra are used through a published representation rather than re-proved here. Only the sample coefficients are computationally verified, while the general formulas are proved abstractly. Independent external evaluation has not been performed. An earlier equivalent result under different terminology or in an unindexed source cannot be excluded solely by the literature searches.

## References

1. T. Flaminio, L. Godo, P. Menchón, and R. O. Rodríguez, *Algebras and relational frames for Gödel modal logic and some of its extensions*, arXiv:2110.02528v1 (2021), especially Definitions 6.1, 6.6, 6.11 and Proposition 6.12; https://arxiv.org/abs/2110.02528.
2. P. Balbiani, M. Diéguez, D. Fernández-Duque, and B. McLean, *Constructive S4 modal logics with the finite birelational frame property*, arXiv:2403.00201v1 (2024), including later public revision; https://arxiv.org/abs/2403.00201.
