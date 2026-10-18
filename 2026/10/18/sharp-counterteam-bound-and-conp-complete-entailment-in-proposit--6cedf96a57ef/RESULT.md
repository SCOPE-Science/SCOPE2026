# Sharp counterteam bound and coNP-complete entailment in propositional nonemptiness logic

## Finding

Let \(\Gamma\) be any finite collection of formulas of \(\mathrm{PL}(\mathrm{NE})\), and let \(\psi\) be another formula. Write \(m\) for the **total number of occurrences** of the nonemptiness atom in all formulas of \(\Gamma\), counted with multiplicity. Then:

**Sharp counterteam theorem.** If \(\Gamma\not\models\psi\), there exists a team \(T\) satisfying every formula in \(\Gamma\) but not \(\psi\), with

\[
|T|\leq m+1.
\]

For every integer \(m\geq0\), there is an instance with precisely \(m\) antecedent nonemptiness occurrences for which the smallest counterteam has exactly \(m+1\) valuations. Consequently the semantic entailment problem, with a finite set of premises or one conjunctive premise and one conclusion, is \(\mathrm{coNP}\)-complete under polynomial-time many-one reductions.

## Assumptions and scope

Fix a finite set \(X\) of propositional variables, the union of the variables occurring in the input formulas. A valuation is a function \(v:X\to\{0,1\}\), and a **team** is a set \(T\subseteq2^X\). The logic has literals \(p\) and \(\neg p\), constants \(\top\) and \(\bot\), nonemptiness \(\mathrm{NE}\), conjunction, and lax split disjunction. Satisfaction is defined by

- \(T\models p\) exactly when every valuation in \(T\) gives \(p\) value one, and analogously for \(\neg p\);
- \(T\models\top\) always, while \(T\models\bot\) exactly when \(T=\varnothing\);
- \(T\models\mathrm{NE}\) exactly when \(T\ne\varnothing\);
- \(T\models\alpha\wedge\beta\) exactly when both conjuncts hold;
- \(T\models\alpha\vee\beta\) exactly when \(T=S\cup U\) for possibly overlapping subteams \(S,U\) satisfying \(\alpha,\beta\), respectively.

For finite premises, \(T\models\Gamma\) means satisfaction of each formula. The empty set of premises corresponds to \(\top\). Satisfaction has **locality**: restricting valuations to the variables of the formula preserves truth. Therefore a counterteam over an arbitrary larger variable domain projects to one over finite \(X\), and conversely a team over \(X\) is a legitimate witness. Throughout, consequence quantifies over **all** teams, including the empty team.

Two elementary properties of every formula \(\theta\) in this language are used: **union closure**, meaning the union of any nonempty family of satisfying teams satisfies \(\theta\), and **convexity**, meaning that if \(A\subseteq B\subseteq C\) with \(A,C\models\theta\), then \(B\models\theta\). Both hold for this precise lax semantics; they are proved in the literature referenced below.

## Proof

**1. A small antecedent witness.** Write \(\varphi=\bigwedge\Gamma\), with \(\varphi=\top\) for empty premises. Thus the number of \(\mathrm{NE}\) occurrences in \(\varphi\) is \(m\). We first verify the small-subteam principle: if \(T\models\theta\) and \(r\) counts nonemptiness occurrences in \(\theta\), then some \(A\subseteq T\) satisfies \(\theta\) with \(|A|\leq r\).

Proceed by structural induction on \(\theta\). Classical literals and constants are true of the empty team whenever they are true of any team, giving an empty witness; for \(\mathrm{NE}\), select a valuation. If \(\theta=\alpha\vee\beta\), take a witnessing lax split \(T=S\cup U\), choose by induction small satisfying subteams \(A\subseteq S\) and \(B\subseteq U\), and note that \(A\cup B\) satisfies the same split and has size at most the sum of the two occurrence counts. If \(\theta=\alpha\wedge\beta\), obtain satisfying \(A,B\subseteq T\) separately and use convexity of the two conjuncts to infer that \(A\cup B\) satisfies both; again its size is at most the sum of the occurrence counts. This proves the principle, including the zero-occurrence case, and reconstructs the small-team lemma in Anttila–Kontinen–Yang.

**2. Compressing a failed entailment.** Suppose \(T\models\varphi\) but \(T\not\models\psi\). By Step 1, choose \(A\subseteq T\) with \(A\models\varphi\) and \(|A|\leq m\). Let \(V=2^X\), and let \(\mathcal F_\psi=\{S\subseteq V:S\models\psi\}\).

If \(\mathcal F_\psi\) is empty, \(A\) already fails \(\psi\), so \(A\) is a counterteam of at most \(m\) valuations. Otherwise put

\[
U_\psi=\bigcup_{S\in\mathcal F_\psi}S.
\]

There are finitely many teams over \(X\), and \(\mathcal F_\psi\) is nonempty. Union closure yields \(U_\psi\models\psi\); every team satisfying \(\psi\) is a subset of \(U_\psi\).

If \(T\subseteq U_\psi\), then \(A\) **cannot** satisfy \(\psi\): otherwise convexity of \(\psi\) applied to \(A\subseteq T\subseteq U_\psi\) would imply \(T\models\psi\), contrary to assumption. Hence \(A\) is already the desired counterteam.

If \(T\not\subseteq U_\psi\), choose \(v\in T\setminus U_\psi\) and let \(B=A\cup\{v\}\). Because \(A\subseteq B\subseteq T\) and both outer teams satisfy \(\varphi\), convexity gives \(B\models\varphi\). But \(B\not\models\psi\), since \(B\) contains a valuation outside the union of **all** \(\psi\)-satisfying teams. Finally \(|B|\leq m+1\). These cases are exhaustive, proving the upper bound even when \(m=0\), \(T=\varnothing\), \(\Gamma=\varnothing\), or \(\psi\) has no satisfying team.

**3. Sharpness for every occurrence count.** For \(m=0\), take \(\varphi=\top\) and \(\psi=p\) over one variable. The empty team satisfies both, whereas a singleton assigning zero to \(p\) satisfies only \(\varphi\). Thus the minimum size of a counterteam is one.

For \(m\geq1\), choose a finite set of variables with at least \(m+1\) distinct valuations, select distinct valuations \(v_1,\dots,v_m,v_*\), and let \(\chi_i\) be the full classical conjunction characterizing \(v_i\). Define

\[
\varphi=\bigl((\chi_1\wedge\mathrm{NE})\vee\cdots\vee(\chi_m\wedge\mathrm{NE})\bigr)\vee\top,
\qquad
\psi=\chi_1\vee\cdots\vee\chi_m.
\]

The antecedent has exactly \(m\) nonemptiness occurrences. Lax splitting shows that a team satisfies \(\varphi\) if and only if it contains **every** \(v_i\), for \(1\leq i\leq m\). The classical formula \(\psi\) holds precisely when every member of the team is among these \(m\) valuations. Therefore a counterteam must contain all \(m\) selected valuations and at least one outsider. The team \(\{v_1,\ldots,v_m,v_*\}\) is such a counterteam, of size exactly \(m+1\). This proves sharpness simultaneously for all positive \(m\).

**4. Complexity.** The complement of entailment can be decided nondeterministically by guessing at most \(m+1\) valuations over \(X\), each encoded in \(|X|\) bits, then checking that the guessed team satisfies every member of \(\Gamma\) and fails \(\psi\). Because \(m\) and \(|X|\) are at most the input length and \(\mathrm{PL}(\mathrm{NE})\) model checking is deterministic polynomial time (Anttila–Kontinen–Yang, Proposition 4), this is an NP verification procedure. Hence entailment is in \(\mathrm{coNP}\).

For hardness, map an ordinary classical propositional formula \(\alpha\) to \(\top\models\alpha\). Classical formulas are **flat** in this team semantics, and the empty team supports every classical formula. Thus the displayed entailment holds exactly when \(\alpha\) is a classical tautology. The mapping is linear-time, and classical tautology is \(\mathrm{coNP}\)-complete. The instance has one premise and no nonemptiness occurrences. The upper and lower bounds establish \(\mathrm{coNP}\)-completeness.

## Verification

The bundled `verify_entailment.py` implements the original inductive semantics using exhaustive lax splits (including overlapping subteams), not the small-counterteam theorem as an assumption. Run `python3 verify_entailment.py` from the directory containing this file. It checks 1,605 and 1,607 generated formulas on one and two propositional variables, respectively, consolidating them into 11 and 51 distinct team truth tables. It tests 121 and 2,601 semantic entailment pairs against the proposed \(m+1\) witness bound, and tests union closure, convexity, and the antecedent small-subteam property directly. Constructed sharpness examples are verified for \(m=1,2,3\), with least counterteam sizes two, three, and four. Expected final output: `VERIFY_OK`.

These experiments check only small finite domains; the unrestricted finite-input theorem follows from Steps 1–4, not from extrapolating the checker.

## Relationship to prior work

Anttila, Kontinen and Yang, *Complexity Results in Team Semantics: Nonemptiness Is Not So Complex* (first released 9 October 2025), establish the convexity and union closure of \(\mathrm{PL}(\mathrm{NE})\), the small satisfying-subteam lemma, polynomial-time model checking, NP-complete satisfiability, and coNP-complete validity. Their conclusion explicitly identifies **the entailment problem** as a direction for future work. These facts supply the starting point, but **none of their SAT, VAL or MC classifications alone gives the sharp counterteam theorem or the entailment upper bound**: implication needs a team that satisfies its antecedent while violating its conclusion. Step 2 supplies the missing geometric argument using the union of all conclusion-models.

Anttila and Knudstorp, *Convex Team Logics* (first released 27 March 2025), characterize expressive completeness for convex union-closed team properties. Expressive completeness does not itself give a polynomial-size counterexample certificate or a computational complexity classification for semantic entailment. A separately indexed result on **material-implication closure** characterizes when uniform union and intersection closure are preserved by an implication-like connective; that statement neither decides semantic entailment nor bounds counterteams for nonemptiness logic.

## Limitations

The result applies to the finitary propositional language with lax split disjunction and a nonemptiness atom, over ordinary sets of Boolean valuations. It does not establish polynomial-time model checking for richer team atoms, modal extensions, strict splitting, arbitrary non-convex team logics, or infinite premise sets. The theorem bounds the *number of valuations* in a counterteam, not the size of a full truth table. Finite experiments are corroborating checks, not a proof of unbounded cases. The originality assessment is based on inspected literature and indexed records; equivalent unindexed work cannot be ruled out. Independent audit has not been performed.

## References

1. A. Anttila, J. Kontinen, and F. Yang, *Complexity Results in Team Semantics: Nonemptiness Is Not So Complex*, arXiv:2510.08122 (first public version 9 October 2025; accessible manuscript version 2, 26 February 2026), Sections 2–6, especially Proposition 1, Lemma 3, Proposition 4 and the conclusion. https://arxiv.org/html/2510.08122
2. A. Anttila and S. Brinck Knudstorp, *Convex Team Logics*, arXiv:2503.21850 (first public version 27 March 2025), introduction and the propositional expressive-completeness results. https://arxiv.org/abs/2503.21850
