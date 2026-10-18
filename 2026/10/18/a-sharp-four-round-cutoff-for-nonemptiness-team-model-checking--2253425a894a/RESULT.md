# A sharp four-round cutoff for nonemptiness-team model checking

## Finding
For the published alternating greatest-subteam algorithm on propositional team logic with the nonemptiness atom, the labelling sequence satisfies
\[
f_4=f_5=f_6=\cdots
\]
for every formula and finite input team. This is **sharp**: \(f_3\ne f_4\) for \(\mathrm{NE}\wedge\bot\) on a one-valuation team. A flat-support/witness characterization additionally gives a direct \(O(|\varphi|\,|T|)\) model-checking algorithm on explicit teams. The quantitative four-round claim concerns the exact algorithm of Anttila, Kontinen and Yang (2025), not an arbitrary fixpoint algorithm.

## Assumptions and scope
Fix a finite set \(P\) of propositional variables and let \(U=2^P\). The input is any team \(T\subseteq U\). Formulas use classical literals \(p\), \(\neg p\), constants \(\top,\bot\), conjunction, lax split disjunction \(\vee\), and \(\mathrm{NE}\). Team clauses: \(S\models p\) iff every valuation in \(S\) satisfies \(p\); \(S\models\bot\) iff \(S=\varnothing\); \(S\models\mathrm{NE}\) iff \(S\ne\varnothing\); \(S\models a\wedge b\) iff both hold on \(S\); \(S\models a\vee b\) iff \(S=S_a\cup S_b\) for subteams supporting the respective operands (overlap permitted). Classical negation is only on variables.

The published labelling starts with \(f_0(u)=T\) for every *occurrence* \(u\). On odd updates, each literal occurrence receives its maximum satisfying subteam of its preceding label, or a distinguished null \(\mathbf0\) if none exists; conjunction combines children by intersection, and split disjunction by union, with \(\mathbf0\) absorbing in either operation. On even updates, the root retains its preceding label; a conjunction gives each child its parent label; a disjunction gives child \(u\) the intersection of its preceding label and its parent's current label, with null absorbing. The null symbol differs from the actual empty team.

## Proof
**1. Flat supports and existential obligations.** To each occurrence \(u\), associate a flat valuation set \(F_u\subseteq U\) and a finite family \(\mathcal W_u\) of sets of valuations, recursively. A classical literal has its ordinary truth set as \(F_u\) and no obligations. The nonemptiness atom has \(F_u=U\) and \(\mathcal W_u=\{U\}\). At a conjunction \(u=a\wedge b\), put
\[
F_u=F_a\cap F_b,\qquad
\mathcal W_u=\{W\cap F_b:W\in\mathcal W_a\}\cup\{W\cap F_a:W\in\mathcal W_b\}.
\]
At a split disjunction \(u=a\vee b\), put \(F_u=F_a\cup F_b\) and \(\mathcal W_u=\mathcal W_a\cup\mathcal W_b\). For \(\top\) and \(\bot\) use \(F=U\) and \(F=\varnothing\), respectively, with no obligations. Every \(W\in\mathcal W_u\) lies inside \(F_u\).

For every team \(S\subseteq U\), structural induction proves the exact criterion
\[
S\models u\quad\Longleftrightarrow\quad S\subseteq F_u\quad\hbox{and}\quad (\forall W\in\mathcal W_u)\ S\cap W\ne\varnothing.\tag{1}
\]
For conjunction, the containment \(S\subseteq F_a\cap F_b\) makes the added intersections with the other conjunct redundant when testing the obligations. For disjunction, the forward implication uses the supporting split; conversely, choose \(S_a=S\cap F_a\) and \(S_b=S\cap F_b\). They cover \(S\), and each obligation for the respective subformula is met because it lies in that subformula's flat support. This proves the induction without treating finite experiments as proof.

**2. Labels after two updates.** First take \(T\ne\varnothing\). No leaf yields null at stage one. Bottom-up induction gives \(f_1(u)=T\cap F_u\). Define a context \(C_u\subseteq U\) by \(C_{\rm root}=U\); across a conjunction give the left child \(C_u\cap F_b\) and the right child \(C_u\cap F_a\); across a disjunction give both children \(C_u\). Direct top-down induction yields
\[
f_2(u)=T\cap F_u\cap C_u.\tag{2}
\]
For a nonemptiness leaf \(\lambda\), this is \(T\cap C_\lambda\). The context \(C_\lambda\) is exactly the obligation set contributed by that leaf in \(\mathcal W_{\rm root}\): it is the intersection of the flattened siblings at all conjunction ancestors on the leaf-to-root path. This is also seen directly from the recursion for \(\mathcal W\).

**3. Closure by update four.** If every nonemptiness leaf has nonempty \(f_2\), then the odd literal update preserves every stage-two label. The stage-two child labels already have parent intersection identities at conjunctions and parent union identities at split disjunctions (by (2)); bottom-up induction therefore gives \(f_3=f_2\). Consequently every later update is unchanged.

Otherwise at least one nonemptiness leaf has empty stage-two label. At stage three its maximum satisfying subteam is null, and null is absorbing up every ancestor to the root; hence \(f_3({\rm root})=\mathbf0\). The fourth top-down update propagates null to **all** occurrences. Subsequent bottom-up/top-down updates preserve the all-null labelling. The case \(T=\varnothing\) is immediate: if a nonemptiness leaf occurs, stage one makes the root null and stage two propagates null everywhere; without such a leaf all classical formulas hold on the empty team and the empty labels are stationary. Thus \(f_4=f_5=f_6=\cdots\) in every case.

For sharpness take \(\varphi=\mathrm{NE}\wedge\bot\) and singleton \(T\). At update two the root and the nonemptiness child have empty actual-team labels, while the bottom child also has the empty team. At update three the nonemptiness child and root become null, but the bottom child remains the actual empty team. At update four the bottom child becomes null; therefore \(f_3\ne f_4\).

**4. Direct checker.** Compute all \(F_u\cap T\) bottom-up and all \(C_u\cap T\) top-down. Accept exactly if \(T\subseteq F_{\rm root}\) and each nonemptiness leaf \(\lambda\) has \(T\cap C_\lambda\ne\varnothing\), by (1). Each tree edge requires a constant number of team-mask intersections/unions. Explicitly scanning the \(|T|\) valuations gives \(O(|\varphi|\,|T|)\) elementary operations. This is a direct bound, not an assertion about bit-complexity of arbitrary encodings.

## Verification
The bundled standalone Python program independently implements original lax split semantics, the flat-obligation criterion, its top-down contextual version, and the alternating published updates. It checks 14,400 formula/team instances with semantic cross-comparison and 21,600 input instances for fourth-round stabilization, and verifies the sharp singleton example. Run \(\texttt{python3 verify_ne_obligations.py}\). The emitted markers are `CONVEX_NE_FLAT_OBLIGATIONS_OK 14400`, `FOUR_ROUND_FIXED_POINT_BOUND_OK 21600`, and `FOUR_ROUND_SHARPNESS_OK`. The universal proof is the structural argument above, not finite sampling.

## Relationship to prior work
Anttila, Kontinen and Yang (arXiv:2510.08122, §3) give the alternating procedure with a polynomial upper bound on the number of updates. Their final discussion of the procedure observes apparent convergence by the fourth update but explicitly leaves a proof and algorithmic improvement for future investigation. Their §4 already establishes the small satisfying-subteam lemma, and none of that existing result is claimed anew here. Anttila and Knudstorp (arXiv:2503.21850) prove expressive completeness for convex, union-closed team properties, not the exact update count of this particular algorithm. The existing coNP-complete entailment and sharp counterteam bound are likewise distinct, previously established results and are **not** part of this finding.

## Limitations
The four-round cutoff is for the specified lax-split propositional nonemptiness algorithm; no claim is made for strict-split semantics, inclusion/dependence atoms, non-flat negation, other fixed-point procedures, or the complexity of arbitrary succinctly represented teams. No independent audit has been performed. Older or differently named algorithmic analyses might contain the same convergence observation; the checked literature and records did not establish one.

## References
Anttila, A., Kontinen, J., and Yang, F., *Complexity Results in Team Semantics: Nonemptiness Is Not So Complex*, arXiv:2510.08122, first publicly submitted 2025-10-09; especially §§2–4 and §6, https://arxiv.org/html/2510.08122.

Anttila, A., and Knudstorp, S. B., *Convex Team Logics*, arXiv:2503.21850, first publicly submitted 2025-03-27; see its convex/union-closed expressive completeness results, https://arxiv.org/html/2503.21850.
