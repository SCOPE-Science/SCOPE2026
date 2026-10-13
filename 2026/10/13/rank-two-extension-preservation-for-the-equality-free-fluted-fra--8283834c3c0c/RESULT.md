# Rank-two extension preservation for the equality-free fluted fragment

## Finding

**Theorem (rank-two extension preservation, separately in ordinary and finite semantics).** Let \(\sigma\) be any finite relational signature with all predicate arities positive, without equality, constants or function symbols; structures have nonempty domains. For every fluted sentence \(\varphi\in\mathrm{FL}[0](\sigma)\) of quantifier rank at most two, the following are equivalent, with the same choice of either *all* \(\sigma\)-structures or *finite* \(\sigma\)-structures throughout:

1. \(\varphi\) is preserved under induced-substructure extensions (if \(A\subseteq B\) are in the chosen class and \(A\models\varphi\), then \(B\models\varphi\)).
2. There is an existential fluted sentence \(\psi\in\exists\mathrm{FL}[0](\sigma)\), in negation normal form with negated atomic formulas permitted and **quantifier rank at most two**, equivalent to \(\varphi\) in the chosen class.

Moreover, the positive translation is a finite disjunction of explicit two-quantifier row-witness requirements; the crucial extension-amalgamation lemma holds for infinite as well as finite structures. The rank bound is sharp as a preservation **threshold**: Ding's rank-three counterexample [1] is extension-preserved yet has no existential fluted equivalent, even on finite structures. The rank-three counterexample is *prior work*, not a new assertion of its proof here.

## Assumptions and scope

We use the formation convention of [1]: \(\mathrm{FL}[m](\sigma)\) admits truth constants, Boolean connectives, the suffix atom \(R(x_{m-r+1},\ldots,x_m)\) for an \(r\)-ary predicate with \(r\le m\), and quantification of \(x_{m+1}\) in an \(\mathrm{FL}[m+1]\) formula to return to level \(m\). A sentence is at level zero. Quantifier rank counts the largest number of nested quantifiers. The existential fragment allows positive/negative atoms, finite conjunctions/disjunctions and existential quantification only. An extension has its predecessor as an *induced* substructure, including all higher-arity relations. Unused relation symbols of arity at least three do not occur in rank-two sentences.

For any structure \(A\), let \(u_A(a)\) denote the complete truth-value assignment to unary predicates at \(a\). Let \(t_A(a,b)\) denote the pair comprising \(u_A(b)\) and the complete truth-value assignment to binary predicates on ordered pair \((a,b)\); thus \(t_A(a,b)\) is a complete atomic **level-two suffix type**. Define the nonempty row support \(S_A(a)=\{t_A(a,b):b\in A\}\), descriptor \(d_A(a)=(u_A(a),S_A(a))\), and descriptor set \(D(A)=\{d_A(a):a\in A\}\). All sets of possible type values and descriptor values are finite, depending only on the finite signature, even when \(A\) is infinite.

Write \(\alpha_u(x_1)\) for the complete conjunction of unary literals specifying \(u\), and \(\beta_t(x_1,x_2)\) for the complete conjunction specifying unary literals at \(x_2\) and all binary literals at \((x_1,x_2)\). Empty conjunctions mean \(\top\). These formulas are permitted respectively at levels one and two. For each structure \(A\), define the finite existential fluted sentence

\[
\chi_A=\bigwedge_{(u,S)\in D(A)}\exists x_1\left(\alpha_u(x_1)\land\bigwedge_{t\in S}\exists x_2\,\beta_t(x_1,x_2)\right).
\]

Each \(\chi_A\) has quantifier rank at most two; \(A\models\chi_A\).

## Proof

**1. Rank-two truth depends only on descriptors.** A quantifier-free level-two formula depends only on \(t_A(a,b)\); a quantifier-free level-one formula depends only on \(u_A(a)\). Structural induction, including universal and existential quantifiers, shows that the truth value at \(a\) of any level-one formula of rank at most one depends only on \((u_A(a),S_A(a))\). Quantification over \(x_2\) computes respectively the presence of or universality over a Boolean property of support types, and Boolean connectives preserve this dependence. Finally, every level-zero sentence of rank at most two is a Boolean combination of quantified level-one formulas of rank at most one, so its truth depends only on \(D(A)\). In particular,

\[
D(B)=D(C)\quad\Longrightarrow\quad (B\models\varphi\iff C\models\varphi)
\]

for *every* rank-two fluted sentence, independently of extension preservation.

**2. Characteristic witnesses.** Directly from the definitions,

\[
B\models\chi_A\quad\Longleftrightarrow\quad
\forall a\in A\ \exists b\in B:\quad u_A(a)=u_B(b)\quad\text{and}\quad S_A(a)\subseteq S_B(b).
\]

The forward implication assigns to each descriptor of \(A\) the \(x_1\)-witness in \(B\); the reverse implication supplies all \(x_2\)-witnesses for every required type.

**3. Extension-amalgamation lemma.** Suppose \(B\models\chi_A\). Then there exists a structure \(C\) in the same finite-or-arbitrary class containing \(A\) as an induced substructure and satisfying \(D(C)=D(B)\).

*Construction and verification.* For every \(a\in A\), choose \(b_a\in B\) as in Step 2. Let \(K\) be the total number of possible level-two suffix types (at least one). Form \(C\) from \(A\) together with \(K\) disjoint copies of \(B\), preserving all relations inside \(A\) and inside each copy. Unary types in the new copies match \(B\). For an old source \(a\) and new target \(z\) of unary type \(u_B(y)\), choose the binary-predicate values so that \(t_C(a,z)\) belongs to \(S_B(b_a)\) and has that target unary type. Such a choice exists because \(b_a\) has an outgoing pair of each unary target type realized by \(B\). Furthermore, for every \(t\in S_B(b_a)\), reserve a distinct \(B\)-copy and in that copy choose a target of the unary type specified by \(t\), forcing exactly type \(t\) from \(a\) to that target. This is possible since \(K\ge|S_B(b_a)|\) and different ordered pairs have independent relation values. The old--old pairs already realize precisely \(S_A(a)\subseteq S_B(b_a)\); hence \(S_C(a)=S_B(b_a)\).

For a new source \(z\) in a copy of \(B\), its outgoing pairs within that same copy realize the complete original support \(S_B(z_0)\), where \(z_0\in B\) is the copied point. For every target outside its own copy, prescribe any outgoing binary type in \(S_B(z_0)\) with the target's unary type. This is always possible: every unary type in \(B\) is seen from \(z_0\) at some pair, and each unary type in \(A\) is realized in \(B\) by Step 2. Therefore \(S_C(z)=S_B(z_0)\). Ordered pairs with opposite orientation are independent; assigning one does not change the other. For relation symbols of arity three or higher, fix values on all-old and same-copy tuples and assign arbitrary values to mixed tuples; none affect the calculated rank-two descriptors. Thus \(D(C)=D(B)\) and \(A\subseteq C\). If \(A,B\) are finite, then \(C\) is finite (indeed its size is \(|A|+K|B|\)). For infinite inputs, ordinary set-theoretic choices suffice and there is no finiteness claim.

**4. Entailment and finite disjunction.** If \(\varphi\) is preserved under extensions in the selected class and \(A\models\varphi\), then any \(B\models\chi_A\) in the same class yields \(A\subseteq C\) from Step 3, hence \(C\models\varphi\), hence \(B\models\varphi\) by Step 1. Consequently \(\chi_A\) entails \(\varphi\) in that class. There are only finitely many possible descriptor sets \(D(A)\) for a fixed finite signature. Select one model \(A\) of \(\varphi\) per realized descriptor set, restricted to the chosen class, and take the finite disjunction of the corresponding \(\chi_A\). If there are no such models, take \(\bot\). Every model \(B\models\varphi\) satisfies its own characteristic sentence, while characteristic entailment gives the converse. This yields the required \(\psi\), in existential fluted syntax with rank at most two. Conversely, an existential fluted sentence with atomic negation is preserved under induced extensions: witnesses and the entire induced atomic diagram on old elements remain unchanged. Thus (1) and (2) are equivalent.

## Verification

The companion standalone `verify.py` reconstructs row descriptors for the mixed signature of one unary and one binary predicate. It checks the amalgamation algorithm for every ordered compatible pair of structures with domain size one or two, and for 6,000 reproducible randomly chosen pairs on three-element domains. The program asserts that the old substructure is induced and the new descriptor set is exactly that of the target. It also tests an independently evaluated nontrivial rank-two fluted formula on corresponding descriptor-equivalent structures. Running `python3 verify.py` gives 1,472 checked compatible ordered pairs and no failed assertions. The program does **not** enumerate all three-element pairs, check every signature, or prove the infinite theorem; the four-step argument above supplies the general proof.

## Relationship to prior work

Ding's 2026 paper [1] establishes equirank **homomorphism** preservation for fluted sentences and separately supplies an extension-preserved **rank-three** sentence not definable in existential fluted logic, even finitely. Those statements neither assert nor imply the above rank-two **extension** preservation theorem: preservation under induced embeddings is weaker than preservation under homomorphisms, particularly when the putative existential formula uses negated atoms. The present threshold result closes this low-rank gap and uses Ding's rank-three obstruction only to identify sharpness.

Yin's preservation theorem for the **ordered** fragment [2] applies to its prefix-variable syntax, whereas fluted atoms are suffixes. For example, the combination of \(P(x_2)\) and \(R(x_1,x_2)\) at fluted level two need not be in that ordered syntax; overlap in purely binary sublanguages is acknowledged. The guarded-fluted preservation theorem mentioned in [1] concerns a proper restricted fragment. Grädel and Rosen [3] address two-variable logic and do not establish an equivalent rank-two theorem for the unrestricted fluted syntax; the two-variable and fluted constraints differ. No universal uniqueness claim is inferred from literature or database searches.

## Limitations

The theorem applies only to positive-arity finite relational signatures, nonempty domains, no identity predicate, and quantifier rank at most two. It does **not** claim an effective decision procedure for finding the disjunction from an arbitrary sentence, a polynomial formula-size bound, preservation at rank three, or a result for equality or functions. Other formulations of a rank-two preservation principle may predate this proof; the literature comparison is not exhaustive, particularly where full texts are inaccessible. The general theorem is mathematical proof, not an independently audited or machine-certified statement; finite checks are supplementary.

## References

[1] Yiwen Ding, *Preservation and definability for the fluted fragment*, arXiv:2607.12970v2 (2026), first public version July 14, 2026 under the title *Failure of the Los-Tarski preservation theorem for the fluted fragment*. Sections 2, 3, 4; especially Theorem 4.8 and Corollary 4.9. `https://arxiv.org/abs/2607.12970` and `https://pdfs.assets.alphaxiv.org/2607.12970v2.pdf`.

[2] Hongkai Yin, *The Niceness of the Ordered Fragment of First-Order Logic*, Journal of Philosophical Logic 55 (2026), 617–635. DOI `10.1007/s10992-026-09845-7`.

[3] Erich Grädel and Eric Rosen, *On Preservation Theorems for Two-Variable Logic*, Mathematical Logic Quarterly 45 (1999). DOI `10.1002/malq.19990450304`.
