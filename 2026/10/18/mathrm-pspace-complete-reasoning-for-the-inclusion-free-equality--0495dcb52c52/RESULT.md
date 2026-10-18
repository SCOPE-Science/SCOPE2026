# \(\mathrm{PSPACE}\)-complete reasoning for the inclusion-free equality team logic

## Finding
In the empty relational signature, the inclusion-atom-free fragment \(\mathsf{FOT}^{-}\) of elementary first-order team logic has \(\mathrm{PSPACE}\)-complete **nonempty-team satisfiability**, **validity** and **semantic equivalence** problems, under ordinary formula-size encodings and polynomial-time many-one reductions. Validity and equivalence range over all structures of nonempty domain and all teams, including the empty team; satisfiability explicitly requires a nonempty team.

There is also a polynomial cardinality cutoff for each of the three tasks. If the total syntactic size of the input formula or formula pair is \(L\geq1\), then all pertinent truth patterns can be tested on universes of cardinality at most \(2L+2\). This cutoff concerns the size of the underlying **universe**, not the cardinality of an explicitly represented team. It does not assert a polynomial-size explicit-team certificate.

## Assumptions and scope
The signature is pure equality, with no predicate symbols, nonlogical constants or functions. The syntax has equality atoms \(x=y\), weak/Boolean conjunction and disjunction \(\land,\mathbin{\mathsf{V}}\), contradictory weak negation \(\dot\sim\), and the **single-value** team quantifiers \(\exists^{1}x,\forall^{1}x\). In a nonempty team \(X\), the weak connectives act as ordinary Boolean operations on the proposition \(M,X\models\varphi\); for a variable \(z\),
\[
M,X\models\exists^{1}z\,\varphi\iff (\exists a\in M)\,M,X[a/z]\models\varphi,
\]
with the dual condition for \(\forall^{1}z\), where \(X[a/z]\) assigns the **same** element \(a\) to \(z\) in every row. All these formulas have the empty-team property. Variable capture is avoided by renaming bound variables apart.

The three decision problems use combined input complexity and permit arbitrary nesting of the displayed connectives and quantifiers. A closed formula is evaluated on its unique nonempty team of empty assignments.

## Proof
**1. Equality–constancy profiles and their realizability.** Fix a nonempty team \(X\) over a finite list \(\bar x=(x_1,\ldots,x_k)\). Define \(i\equiv_X j\) when \(x_i=x_j\) holds throughout \(X\). This is an equivalence relation. Mark an equivalence class **constant** if its variables assume only one value across the team. Let \(c(X)\) be the number of constant classes. Distinct constant classes have distinct values. These data form a profile \(\pi(X)\). This is the equality–constancy information underlying the quantifier-elimination theorem of Engström and Kontinen.

If the universe has cardinality \(q\geq2\), a partition of the \(k\) variables with an arbitrary choice of constant classes is realizable by a nonempty team exactly when the number \(c\) of chosen constant classes satisfies \(c\leq q\). Necessity is immediate. For sufficiency assign the \(c\) constant classes distinct fixed values, and independently let all other classes range over the entire \(q\)-element universe. The team of all these rows makes every unmarked class nonconstant and separates every distinct pair of classes. For \(q=1\), every variable is constant and all variables are equal; for \(k=0\), the unique nonempty team consists of the empty assignment.

**2. Exact symbolic evaluation.** A nonempty team's truth of every \(\mathsf{FOT}^{-}\) formula depends only on its equality–constancy profile and on \(q\), the universe cardinality. Prove this directly by induction. Equality tests ask whether two variables belong to the same block; the Boolean cases are immediate. For a weak quantifier on \(z\), every possible witness value \(a\in M\) has exactly one of the following effects on the profile: it matches one of the \(c\) existing constant blocks, or it matches none. In the latter case it creates a new constant block, possible exactly when \(c<q\). It cannot make \(z\) equal throughout the team to a nonconstant variable. Witnesses in the same case produce identical extended profiles, so an existential quantifier takes the Boolean OR over at most \(c+1\) cases and a universal quantifier the Boolean AND over the same cases. This argument also handles singleton teams and all boundary cardinalities. The inductive assertion remains valid for infinite universes by treating the fresh-value case as always available.

**3. Polynomial universe cutoff and polynomial space.** Let \(L\) be the combined syntax size of the input formula(s). At most \(L\) distinct free variables occur, and along a branch of the syntax tree at most \(L\) quantifier-bound variables can be simultaneously active. Thus an evaluation profile contains at most \(2L\) constant blocks. If \(q\geq2L+2\), the fresh-value option is available at every quantifier step, and its truth calculation is exactly the same for all such finite \(q\) and for infinite domains. Every profile with at most \(L\) free-variable classes is realizable in all these domains by Step 1. Therefore satisfiability, validity and equivalence have the same answers if only \(q=1,\ldots,2L+2\) are considered.

A deterministic depth-first procedure enumerates these \(q\), then every partition and legal choice of constant classes on the free variables. For a chosen profile it evaluates the formula recursively according to Step 2. Represent a partition by at most \(L\) block labels and one constancy bit per block; each depth-first recursive frame and each quantifier choice needs polynomially many bits, and recursion depth is at most \(L\). Time may be exponential, but space is polynomial. For satisfiability, accept if any nonempty-team profile satisfies the input. For validity, accept if all profiles satisfy it (the empty team is automatic). For equivalence, compare the truth of both formulas on all common profiles. Hence all three problems belong to \(\mathrm{PSPACE}\).

**4. The lower bounds.** Let \(Q\) be an arbitrary closed quantified Boolean formula. Define a closed equality-only formula \(\mathsf{Two}\) by
\[
\exists^{1}a\,\exists^{1}b\bigl(\dot\sim(a=b)\land\forall^{1}c\,((c=a)\mathbin{\mathsf V}(c=b))\bigr).
\]
On every nonempty team, \(\mathsf{Two}\) is true precisely when the underlying universe has two elements. In a two-element universe, choose distinct elements \(a,b\). Translate each quantified Boolean variable \(p_i\) to a weakly quantified first-order variable \(u_i\), each Boolean occurrence of \(p_i\) to \(u_i=a\), and Boolean connectives to the corresponding weak connectives. Call the resulting formula \(Q^{a,b}\). By induction on the quantified Boolean formula, on the singleton closed team and its constant extensions \(Q^{a,b}\) has exactly the truth value of \(Q\), with \(u_i=a\) meaning true and \(u_i=b\) meaning false.

Set
\[
S_Q:=\mathsf{Two}\land\exists^{1}a\,\exists^{1}b\bigl(\dot\sim(a=b)\land Q^{a,b}\bigr),
\qquad
V_Q:=(\dot\sim\mathsf{Two})\mathbin{\mathsf V} S_Q.
\]
Bound variables in the two occurrences are renamed apart. On nonempty closed teams, \(S_Q\) has a model exactly when \(Q\) is true: a model must have exactly two elements. Meanwhile \(V_Q\) is valid in every nonempty domain and on every team exactly when \(Q\) is true: outside size two its first disjunct holds; at size two the second disjunct has value \(Q\); on the empty team both formulas hold. Thus nonempty-team satisfiability and validity are \(\mathrm{PSPACE}\)-hard by polynomial reductions from true quantified Boolean formulas. Equivalence is \(\mathrm{PSPACE}\)-hard by asking whether \(V_Q\) is equivalent to the always-true closed sentence \(\forall^{1}z(z=z)\). Together with Step 3, this proves all three completeness claims.

## Verification
The standalone script `checker.py` implements the original finite team clauses and the symbolic equality–constancy evaluator separately. Running `python checker.py` reports `VERIFY_OK finite_team_symbolic_comparisons 18830 formulas 210` and `VERIFY_OK qbf_translation_cases 400`. The first comparison covers all nonempty teams on universes of sizes one through three with one or two free variables against generated formulas with weak quantifiers. The second compares 400 generated quantified Boolean formulas against their two-element team translations, also checking the universe-size guard at sizes one, two and three. Additional randomly generated profile evaluations compare large-cardinality cutoffs. These finite checks are regression tests, not substitutes for the structural induction and polynomial-space argument above.

## Relationship to prior work
Engström and Kontinen, *Intuitionistic Implication in Elementary Team Logics* (first arXiv posting 2026-09-14, arXiv:2609.15216), prove quantifier elimination for this inclusion-free empty-signature fragment and conclude in Corollary 3.7 that nonempty-team satisfiability, validity and equivalence are decidable. Their constructive elimination does not state a polynomial-space procedure or the three \(\mathrm{PSPACE}\)-completeness classifications. The direct profile transition in Step 2 supplies that resource bound. Kontinen and Yang, *Complete Logics for Elementary Team Properties* (arXiv:1904.08695), establish the larger elementary team logic and its expressive characterization; those results do not directly give the present sharp complexity result for the inclusion-free fragment. Standard \(\mathrm{PSPACE}\)-hardness of true quantified Boolean formulas is used in the lower bound, not claimed as novel.

## Limitations
The theorem concerns only pure equality and the specific inclusion-free weak-quantifier language. Adding inclusion atoms or stronger team quantifiers is outside its scope. The cardinality cutoff is for universes, not explicit teams, and the algorithm is polynomial **space**, not polynomial time. Exhaustive priority relative to all unpublished or unindexed literature is not established. No independently conducted mathematical audit has been performed.

## References
1. Fredrik Engström and Juha Kontinen, *Intuitionistic Implication in Elementary Team Logics*, arXiv:2609.15216 (initial posting 2026-09-14), Sections 2–3 and Corollary 3.7; https://arxiv.org/abs/2609.15216 .
2. Juha Kontinen and Fan Yang, *Complete Logics for Elementary Team Properties*, *Journal of Symbolic Logic* 88 (2023), 579–619, arXiv:1904.08695; https://arxiv.org/abs/1904.08695 .
3. True quantified Boolean formula, the classical \(\mathrm{PSPACE}\)-complete decision problem (standard complexity background).
