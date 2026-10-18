# A sharp two-point dual separation for relevant topological evidence

## Finding

In the Routley–Meyer up-model semantics of relevant topological evidence logic, consider the base language of propositional variables, conjunction, disjunction, relevant implication, Routley negation, topological interior \(\Box\), and global universal modality \(A\). Two distinct nondefinability phenomena have a *common*, cardinality-minimal witness: there are two models on the same **two-point** Routley–Meyer frame, with the same valuation, that agree pointwise on every base-language formula, but disagree both on (i) the interior of the complement of \(p\), and (ii) the existence of a dense open subset contained in the truth set of \(p\). No such separation is possible with a single world. In particular, the minimum nonempty carrier size for a simultaneous semantic separation of these two operations is exactly \(2\).

## Assumptions and scope

Use the five frame clauses (RM1)–(RM5) in Sedlár (2026), Definition 4.1, and the satisfaction clauses in Definition 4.4. A frame has a nonempty carrier \(X\), preorder \(\preceq\), designated upset \(N\), ternary relation \(R\), and involutive Routley star \(s\). The topology is an up-set topology. For a formula \(\varphi\), write \([\![\varphi]\!]\) for its truth set and \(\operatorname{Int}\) for interior. Consider the added *local* operation \(I_c(p):=\operatorname{Int}(X\setminus [\![p]\!])\) and the *global* condition \(C(p)\) that some dense open \(U\) satisfies \(U\subseteq[\![p]\!]\). The claim is nondefinability over all such models, witnessed simultaneously, not nondefinability in each fixed topology.

## Proof

Let \(X=\{a,b\}\), let \(\preceq\) be equality, let \(N=X\), let \(s(a)=b\) and \(s(b)=a\), and define \(Rxyz\) iff \(y=z\). RM1 holds since \(y=z\); RM2 holds by any choice of \(x\in N\); RM3 is immediate for the equality preorder; RM4 is automatic for equality; and RM5 follows from the involution. Every topology on \(X\) is an up-set topology for this preorder.

Interpret \(p\) as \(P=\{b\}\) and every other atom as the empty set. Model \(M_1\) has topology \(\mathcal T_1=\{\varnothing,P,X\}\). Model \(M_2\) has the discrete topology \(\mathcal T_2=\mathcal P(X)\). Both share every other semantic component.

Put \(\mathcal F=\{\varnothing,P,X\}\). This collection contains the truth sets of all atoms and is closed under intersection and union. For either model, Routley negation sends \(\varnothing\) to \(X\), \(X\) to \(\varnothing\), and \(P\) to itself because the star swaps \(a,b\). Since \(Rxyz\) holds exactly when \(y=z\), implication of truth sets \(S,T\) is \(X\) if \(S\subseteq T\), and \(\varnothing\) otherwise. Global \(A\) sends \(X\) to \(X\) and every other set to \(\varnothing\). Finally, interior in either topology fixes all three members of \(\mathcal F\). Thus these interpretations of **every** connective agree on \(\mathcal F\); structural induction proves that every formula of the full base language has the **same** truth set in both models, and that set is in \(\mathcal F\). This holds regardless of formula depth and the number of atoms (all atoms other than \(p\) are empty).

The complement of \(P\) is \(\{a\}\). It has empty interior in \(M_1\), but interior \(\{a\}\) in \(M_2\). Therefore no base-language formula uniformly expresses \(I_c(p)\). In \(M_1\), \(P\) itself is a dense open set: its only nonempty open competitors are \(P\) and \(X\), both meeting \(P\). In \(M_2\), the only open subsets of \(P\) are \(\varnothing\) and \(P\), neither dense; the nonempty open set \(\{a\}\) is disjoint from each. Therefore \(C(p)\) holds in \(M_1\) and fails in \(M_2\). No formula can uniformly express this global condition either. Both failures are witnessed by the same pair.

Optimality: on any singleton carrier \(X\), the sole topology is \(\{\varnothing,X\}\) and the involution necessarily fixes its sole point. Therefore interior-of-complement equals the truth set of Routley negation \(\neg p\). Moreover, a dense open subset of \([\![p]\!]\) exists iff \(p\) holds at the unique point; the base formula \(p\) expresses this condition. Thus neither phenomenon can separate base-language-indistinguishable singleton models.

## Verification

The independent executable script `check.py` verifies the Routley-star involution, the closure and coincidence of all seven base-language operations over the three truth sets \(\mathcal F\), the two contrasting interior-of-complement values, the opposing dense-open-support conditions, and both singleton truth values. Execute `python3 check.py` in this directory. The infinite family of formulas is covered by the structural-induction proof, not by finite formula enumeration.

## Relationship to prior work

Sedlár (2026, Proposition 4.6) proves both nondefinability statements and exhibits four-point countermodels separately. The present result does not re-claim nondefinability; it identifies the **joint minimal witness size**, obtains both separations with one identical two-point frame and valuation, and proves the one-point lower bound. The base Routley–Meyer semantics and their satisfaction clauses are those of the cited work. Earlier related work on relevant modal logic supplies the semantic background but does not state this two-point simultaneous sharp witness in the material inspected.

## Limitations

The result is a sharp small-model separation, not a general complexity theorem or new nondefinability theorem. It does not determine minimality under additional frame or topology constraints beyond RM1–RM5 and an up-set topology. Full historical priority cannot be guaranteed: logically equivalent two-point examples may exist in unindexed or differently named relevant/topological logic literature. Independent review has not been performed.

## References

- Igor Sedlár, *Non-classical Topological Evidence Logic*, Electronic Proceedings in Theoretical Computer Science 447 (2026), 691–710, DOI: 10.4204/EPTCS.447.39; first arXiv public posting 2026-06-30, arXiv:2606.31888, especially Definitions 4.1, 4.4, Proposition 4.6 and Section 5.
- Shawn Standefer and Rohan French, paper on classicality and relevant logics, available at https://shawn-standefer.github.io/pdfs/classicality.pdf; Routley–Meyer semantic background, not the topological separation.
