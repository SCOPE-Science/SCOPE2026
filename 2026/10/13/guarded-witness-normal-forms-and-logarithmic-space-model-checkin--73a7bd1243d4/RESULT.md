# Guarded-witness normal forms and logarithmic-space model checking for nonemptiness teams

## Finding

**Theorem (guarded witnesses and logarithmic space).** In propositional team logic \(\mathrm{PL}(\mathrm{NE})\) with literal negation, Boolean constants, conjunction, and *lax* splitting disjunction, every formula \(\varphi\) admits a uniform polynomial-size representation by one ordinary propositional formula \(C_\varphi\) and at most as many ordinary propositional witness guards as occurrences of \(\mathrm{NE}\) in \(\varphi\). For every team \(T\), including the empty team, the following are equivalent:

\[
T\models\varphi\quad\Longleftrightarrow\quad
(\forall s\in T\;s\models_{\mathrm{cl}}C_\varphi)
\ \land\ (\forall w\in W_\varphi\;\exists s\in T\;s\models_{\mathrm{cl}}w).
\]

For every ambient team \(U\), if some subteam of \(U\) satisfies \(\varphi\), then the uniquely greatest satisfying subteam is exactly \(U\cap\llbracket C_\varphi\rrbracket\). Consequently the *combined* model-checking problem for \(\mathrm{PL}(\mathrm{NE})\), with a finite team listed explicitly as its rows and an input formula, belongs to deterministic logarithmic space \(\mathrm L\). The restriction to classical formulas is already \(\mathrm{NC}^{1}\)-hard; no \(\mathrm L\)-hardness or \(\mathrm{NC}^{1}\)-completeness is claimed.

## Assumptions and scope

Fix a countable propositional variable set. Teams are sets of valuations defined on all variables of the tested formula. A literal \(p\) or \(\neg p\) holds when it holds at every valuation of the team. The constant \(\bot\) holds only on the empty team; \(\top\) holds on every team; and \(\mathrm{NE}\) holds exactly on nonempty teams. Conjunction uses the same team. Disjunction is *lax*: \(T\models\alpha\vee\beta\) precisely when there are \(Y,Z\subseteq T\), potentially intersecting, such that \(T=Y\cup Z\), \(Y\models\alpha\), and \(Z\models\beta\). There is no unrestricted team-level negation or dependence/inclusion atom in this theorem. The mathematical equivalence holds for teams of any cardinality; the complexity claim assumes a conventional finite explicit truth-table-of-rows encoding and well-formed syntax.

Write \(s\models_{\mathrm{cl}}\gamma\) for ordinary Boolean evaluation, and \(\llbracket\gamma\rrbracket\) for the class of valuations verifying \(\gamma\). The flattening \(C_\varphi\) is obtained by replacing every occurrence of \(\mathrm{NE}\) by \(\top\) and interpreting the remaining connectives classically. Define a list of witness guards \(W_\varphi\) recursively by occurrences, preserving repeated guards when they arise:

* For \(\varphi=p,\neg p,\top,\bot\), let \(W_\varphi\) be the empty list.
* For \(\varphi=\mathrm{NE}\), let \(W_\varphi=[\top]\).
* For \(\varphi=\alpha\wedge\beta\), concatenate \(W_\alpha\) and \(W_\beta\).
* For \(\varphi=\alpha\vee\beta\), concatenate the lists \([C_\alpha\wedge w:w\in W_\alpha]\) and \([C_\beta\wedge w:w\in W_\beta]\).

The guards are ordinary propositional formulas, not team formulas. Equivalently, each occurrence of \(\mathrm{NE}\) yields the conjunction of the flattenings of the chosen child at every disjunction ancestor on its path to the root (an empty conjunction is \(\top\)). Thus there are no more than \(\lvert\varphi\rvert_{\mathrm{NE}}\) witnesses. A syntax-DAG retaining pointers to subformula flattenings and the \(\mathrm{NE}\) occurrence/ancestor relation uses at most quadratic reference space in the formula length; expanding every guard separately still takes polynomial space. The algorithm below does not need to construct either representation explicitly.

## Proof

**1. Inductive semantic invariant.** Prove simultaneously, for each formula \(\psi\), the stated equivalence for all teams. Literal and constant cases follow from flat classical semantics. At \(\mathrm{NE}\), \(C_{\mathrm{NE}}=\top\) and its sole witness is \(\top\): the universal condition is automatic and the witness exists precisely when \(T\ne\varnothing\).

For a conjunction \(\alpha\wedge\beta\), both children are evaluated on the same team. Their respective universal conditions combine to the universal condition for \(C_\alpha\wedge C_\beta\); their existential witness lists concatenate. This is exactly the required invariant.

For a disjunction \(\alpha\vee\beta\), suppose first that \(T=Y\cup Z\) with \(Y\models\alpha\) and \(Z\models\beta\). By the induction hypothesis, every row of \(Y\) satisfies \(C_\alpha\) and every row of \(Z\) satisfies \(C_\beta\). Therefore every row of \(T\) satisfies \(C_\alpha\vee C_\beta\). For any child witness \(w\in W_\alpha\), its valuation in \(Y\) satisfies both \(C_\alpha\) and \(w\), thus supplies the guarded witness \(C_\alpha\wedge w\) in \(T\); similarly for \(\beta\).

Conversely, assume every row of \(T\) satisfies \(C_\alpha\vee C_\beta\), and the guarded witness conditions hold. Choose the *canonical overlapping split*
\[
Y=T\cap\llbracket C_\alpha\rrbracket,
\qquad Z=T\cap\llbracket C_\beta\rrbracket.
\]
The universal hypothesis implies \(T=Y\cup Z\). Every row in \(Y\) satisfies \(C_\alpha\); every witness guard \(C_\alpha\wedge w\) yields a valuation in \(Y\) satisfying \(w\). By the induction hypothesis \(Y\models\alpha\), and likewise \(Z\models\beta\). Consequently \(T\models\alpha\vee\beta\), completing the induction. The use of overlap is essential here: no strict-disjunction assertion is made.

**2. Canonical greatest subteam.** Let \(U\) be any team. If some \(S\subseteq U\) satisfies \(\varphi\), the invariant implies \(S\subseteq U\cap\llbracket C_\varphi\rrbracket=:M\). Each required witness has a valuation in \(S\) and hence in \(M\), while every valuation in \(M\) satisfies \(C_\varphi\). Applying the invariant again gives \(M\models\varphi\). Thus \(M\) contains every satisfying subteam and is itself satisfying. If no satisfying subteam exists, there is no greatest satisfying subteam, and no assertion that \(M\) satisfies \(\varphi\). This distinction covers \(\mathrm{NE}\) on the empty team.

**3. Deterministic logarithmic-space evaluation.** Given an explicitly listed finite team \(T\) and a formula of input length \(n\), sequentially scan rows to test \(C_\varphi\) at each row using the standard logarithmic-space Boolean formula-value algorithm. The flattening is obtained from syntax by replacing atomic \(\mathrm{NE}\) with \(\top\); parenthesized subformulas are addressable by \(O(\log n)\)-bit offsets, so the flattening can be evaluated without a large materialized output (or by logspace composition of the two standard syntax/evaluation procedures).

Then enumerate every occurrence of \(\mathrm{NE}\) using an input-position counter. For each occurrence, scan the team rows and evaluate its witness guard: walk the syntax-ancestor chain of that occurrence, and at each disjunction ancestor check the ordinary Boolean value of the flattened child through which the path descends. Accept that witness exactly if some listed row passes all such tests. The required positional counters and one row index occupy \(O(\log N)\) bits for total input length \(N\); classical Boolean formula value, locating enclosing subexpressions, and any loop iteration can be recomputed in deterministic logarithmic work space. Processing witnesses and rows sequentially needs no saved sets. Accept exactly when all universal and existential tests pass. Hence combined model checking lies in \(\mathrm L\). Since ordinary propositional formula evaluation on a singleton team embeds as the fragment without \(\mathrm{NE}\), Boolean formula evaluation gives the usual \(\mathrm{NC}^{1}\) lower-bound comparison (under standard suitable reductions).

## Verification

A dependency-free Python checker `verify.py` independently implements the inductive normal form and the original recursive team semantics, enumerating every possible pair of subteams for each lax disjunction. It also enumerates subteams to test the maximal-subteam criterion. Running `python verify.py` produces:

```
EXHAUSTIVE_2_VARIABLES_NODES_LE_2 2849 FORMULAS 45584 FORMULA_TEAM_PAIRS
RANDOM_THREE_VARIABLE_CHECKS 4800
VERIFY_OK
```

The first set includes every enumerated syntax tree with at most two binary connectives over two variables, four literals, \(\top\), \(\bot\), and \(\mathrm{NE}\), tested on all 16 teams over the two-variable assignment space. The second set uses a fixed pseudorandom seed, 100 formulas of depth at most four, and 48 three-variable teams per formula. This is finite regression evidence only; the theorem for arbitrary formulas and arbitrary teams follows from the structural induction above. The logarithmic-space complexity is an algorithmic proof, not a performance measurement of the Python checker.

## Relationship to prior work

Anttila, Kontinen, and Yang (arXiv:2510.08122, first public 2025-10-09) prove polynomial-time combined model checking for \(\mathrm{PL}(\mathrm{NE})\), by a sequence of shrinking team labels and a fixed-point procedure (their Proposition 4). Their discussion immediately after Proposition 4 observes empirically that the fixed-point sequence appears to stabilize by its fourth step, but leaves proof of this and improvement to future work; Section 6 explicitly raises the problem of improving the complexity upper bound. Their flattening construction and union-closure lemmas are used as a conceptual point of departure. The present proof supplies an explicit guarded-existential invariant that permits a direct deterministic logarithmic-space algorithm. The existing \(\mathrm P\) inclusion alone does not imply this improved upper bound.

Anttila and Knudstorp (arXiv:2503.21850) study expressive completeness and convex team properties, providing closely relevant background; any expressive normal form established there should not be mistaken without analysis for a logspace-uniform translation with this witness structure. An equivalent construction in its sections not examined in full remains a genuine literature risk. The classical Boolean formula-value upper bound is standard (Buss 1987); neither propositional \(\mathrm{NC}^{1}\) completeness nor the general flattening operation is claimed new. The claim concerns their uniform guarded composition and the resulting \(\mathrm L\) bound.

## Limitations

Only positive \(\mathrm{PL}(\mathrm{NE})\) syntax with lax splitting is covered. Strict disjunction, contradictory negation, inclusion/dependence atoms, and modal extensions are not handled. The logarithmic-space bound assumes an explicit encoding of rows rather than a succinct circuit-defined team. The exact lower-bound complexity between \(\mathrm{NC}^{1}\) and \(\mathrm L\) is not resolved. The full text of one plausible related source could not be examined; originality is a literature-informed assessment and not a priority or independence guarantee. All computations are finite tests, not replacements for the unbounded proof.

## References

1. A. Anttila, J. Kontinen, and F. Yang, *Complexity Results in Team Semantics: Nonemptiness Is Not So Complex*, arXiv:2510.08122, publicly posted 2025-10-09, https://arxiv.org/html/2510.08122 (especially definitions, Proposition 4, and Section 6).
2. A. Anttila and S. B. Knudstorp, *Convex Team Logics*, arXiv:2503.21850, https://arxiv.org/abs/2503.21850 (abstract and bibliographic record examined; full text not examined).
3. S. R. Buss, *The Boolean Formula Value Problem Is in ALOGTIME*, STOC 1987. This standard classical complexity upper bound is background, not a claimed contribution.
