# The two-to-three fibre threshold for equality-only inquisitive team model checking

## Finding
Fix the following single open formula of inquisitive team logic (InqBT), with equality as its only atomic predicate. Define the value question \(\mu(t):=\forall v\,?(v=t)\), where \(v\) is fresh and \(?\alpha\) is inquisitive disjunction of \(\alpha\) and its intuitionistic negation. Let
\[
\Phi(z,x,y):=\bigl((\mu(x)\to\mu(y))\to\exists^{\mathrm{inq}}w\,(w\ne z)\bigr).
\]
Here \(\to\) is inquisitive implication (evaluated on all subteams) and \(\exists^{\mathrm{inq}}\) chooses one domain element uniformly for the team. For any finite nonempty equality structure with domain \(D\) and any team \(X\subseteq D^{\{z,x,y\}}\), put
\[
r(X):=\max_{d\in D}\bigl|\{s\in X:s(z)=d\}\bigr|.
\]
The **fixed-formula model-checking problem for \(\Phi\)** has an exact local-branching complexity threshold:

1. On inputs satisfying \(r(X)\le2\), support \(D\models_X\Phi\) is decidable in deterministic polynomial time, by a uniform reduction to unsatisfiability of a Boolean 2-CNF formula. This includes arbitrary finite domains and arbitrary values in the \(y\)-column.
2. On inputs satisfying \(r(X)\le3\), the same decision problem is coNP-complete. Hardness already holds when every \(z\)-fibre has **exactly three distinct rows** and the \(y\)-column takes only the two values \(0,1\). The underlying structure interprets **no nonlogical predicates, functions or constants**; exactly three free team columns are used.

Thus a third available row per \(z\)-value is sufficient for coNP-completeness, whereas at most two rows always admit a polynomial-time algorithm. This is a complexity-class boundary, not an unconditional proof that the two complexity classes differ.

## Assumptions and scope
The finite domain \(D\) is explicitly given and nonempty. The team is an explicitly listed **set** of assignments, each with exactly the three free variables \(z,x,y\); its duplicate-free triples are regarded as a ternary relation. Equality is interpreted as actual identity. Support uses the standard downward-closed InqBT semantics: implication quantifies over all subteams, inquisitive existential quantification assigns a single common value to the bound variable, and a classical inequality holds if it holds at each assignment. The value-question abbreviation uses the ordinary, non-range-generating universal quantifier of InqBT. The input formula is fixed, so complexity measures the size of \(D\) and \(X\), not a varying formula. The hardness source is three-CNF satisfiability with three different propositional variables in each clause, an NP-complete form of 3SAT.

## Proof
**1. Exact subteam characterization.** For every subteam \(Y\), \(Y\models\mu(t)\) holds exactly if all assignments in \(Y\) give the same value to \(t\). Indeed, for each fixed \(d\in D\), the question \(?(d=t)\) requires either the whole team to have \(t=d\) or the whole team to have \(t\ne d\). Consequently,
\[
Y\models\mu(x)\to\mu(y)
\quad\Longleftrightarrow\quad
\forall s,s'\in Y\;(s(x)=s'(x)\Rightarrow s(y)=s'(y)).
\]
For the forward implication, apply the conditional to the two-element subteam comprising any two assignments with equal \(x\)-values. For the reverse implication, every subteam with constant \(x\) must have constant \(y\). This is the functional dependency \(x\to y\), including on the empty team. Further,
\[
Y\models\exists^{\mathrm{inq}}w(w\ne z)
\quad\Longleftrightarrow\quad
\exists d\in D\;\forall s\in Y\;(s(z)\ne d).
\]
It follows that
\[
D\not\models_X\Phi
\quad\Longleftrightarrow\quad
\exists Y\subseteq X\;\bigl[\,Y\text{ satisfies }x\to y\ \land\ \{s(z):s\in Y\}=D\,\bigr].\tag{1}
\]
If the right-hand side holds, one may retain just one row with each \(z\)-value; the resulting subteam still satisfies the functional dependency and has at most \(|D|\) rows. Checking it is polynomial, proving coNP membership for the support problem on all finite inputs.

**2. Polynomial-time side.** Assume \(r(X)\le2\). Introduce one propositional variable \(P_{a,b}\) for every ordered pair \((a,b)\) appearing as \((s(x),s(y))\) in \(X\). Build a Boolean CNF \(F_X\) as follows. For each \(d\in D\), insert the clause
\[
\bigvee_{\substack{s\in X\\s(z)=d}}P_{s(x),s(y)}.
\]
It has at most two literals; an empty fibre gives an empty clause. For any \(a\in D\) and distinct \(b,c\in D\) for which the corresponding propositional variables occur, add the binary exclusion clause \(\neg P_{a,b}\lor\neg P_{a,c}\). The resulting formula is a 2-CNF of polynomial size (at most quadratic in \(|X|\)). By (1),
\[
F_X\text{ is satisfiable}\quad\Longleftrightarrow\quad D\not\models_X\Phi.
\]
Indeed, any witnessing subteam sets true precisely the pair-variables it uses and satisfies all clauses. Conversely, a satisfying Boolean assignment selects at least one row from each \(z\)-fibre whose pair-variable is true; the binary exclusions ensure that the selected rows obey \(x\to y\). There is no requirement to choose a value for unused \(x\)-values. Ordinary 2-SAT therefore decides support in polynomial time **even when \(y\) has more than two possible values**.

**3. Sharpness at three rows.** Start with a three-CNF instance \(\Theta\) having \(p\ge3\) propositional variables \(p_0,\ldots,p_{p-1}\), \(m\ge1\) clauses, and exactly three distinct underlying variables in every clause. This version is NP-complete: repeated or opposite literals can be simplified, tautological clauses omitted, and remaining one- or two-literal clauses replaced using two or one fresh Boolean variables, respectively; an empty clause has a fixed contradictory three-CNF replacement. Let \(N:=\max\{m,p,2\}\) and \(D:=\{0,\ldots,N-1\}\). If \(m<N\), append \(N-m\) tautological three-literal clauses \(p_0\lor\neg p_0\lor p_1\). For each resulting clause \(c_i\), include in \(X\) exactly its three triples
\[
(i,j,1)\quad\text{for each positive literal }p_j,
\qquad
(i,j,0)\quad\text{for each negative literal }\neg p_j.
\]
The three triples in each fibre are distinct: the original clauses have distinct underlying variables, while each padding clause gives the different pairs \((0,1),(0,0),(1,1)\). Thus \(|X|=3N\), all \(N\) fibres have size three, and only \(0,1\) occur in the third column. The use of the **same universe for all three coordinates** is harmless: a coordinate determines whether a number denotes a clause, a propositional variable or a truth value, and no nonlogical tagging predicates are needed.

If \(\Theta\) is satisfiable, choose for each clause a literal made true by a satisfying assignment, and retain its corresponding row. The resulting subteam covers all \(z\)-values and satisfies \(x\to y\). Conversely, a subteam witnessing (1) supplies at least one literal from every clause; the functional dependency requires every selected literal on a given variable to have the same polarity. Assign each variable that polarity, assigning arbitrary values to variables absent from the subteam. Every clause, including every original clause, is satisfied. Hence
\[
\Theta\text{ satisfiable}\quad\Longleftrightarrow\quad D\not\models_X\Phi.
\]
The reduction is polynomial and maps 3UNSAT to support of the **same fixed equality-only formula** on the promised three-row inputs. Together with coNP membership this completes the claimed dichotomy.

## Verification
The standalone standard-library script `verify.py` expands the actual support clauses for value questions, inquisitive implication and inquisitive existential quantification. Run `python3 verify.py`; the expected success marker is `VERIFY_OK`. It tests both the syntactic team semantics and the witness characterization on all \(258\) teams over domains of sizes one or two and on \(180\) sparse three-element-domain teams. It exhausts all \(46^3=97{,}336\) three-element-domain relations having at most two rows per \(z\)-fibre, compares the Boolean 2-SAT construction with independently enumerated three-valued maps, and checks \(1{,}400\) random four-element-domain cases. It also checks \(5{,}180\) three-CNF instances against an independently enumerated truth-assignment characterization of the padded ternary construction. These finite checks support the implementation; the preceding universally quantified proof, not the tests, establishes arbitrary-domain correctness and coNP hardness.

## Relationship to prior work
Kontinen and Ciardelli, *On the Expressive Power of Inquisitive Team Logic and Inquisitive First-Order Logic*, arXiv:2603.08646 (first version 9 March 2026), Theorem 3.7, prove coNP-completeness for an InqBT fixed formula using a tagged clause set \(C\) and a reduction represented by a four-column team. Their displayed formula already has only the three free variables \(z,x,y\), so the fourth team column can be removed by the standard locality property; **that projection is not claimed as a novelty here**. The added conclusions are (i) a fully predicate-free equality-only formula with a domain-total clause encoding, and (ii) an exact two-versus-three \(z\)-fibre **complexity threshold** for that fixed formula, including the polynomial algorithm at two rows for arbitrary \(y\)-values. General coNP-hardness does not itself imply the at-most-two-fibre algorithm or the equality-only, exactly-three-fibre restriction. The known quantifier-free dependence-logic complexity and coherence literature studies related team constraints, but those formulas use different connectives and do not automatically settle this InqBT subteam-implication problem. The algorithm uses familiar 2-SAT ideas; the contribution is the precise semantic reduction and sharp boundary.

## Limitations
The classification concerns **this fixed formula**, not every InqBT formula, and counts rows by the fibre of the free variable \(z\), not by other coordinate degrees. Polynomial versus coNP-complete does not assert an unconditional complexity-class separation. The construction does not prove minimality of the number of free variables, quantifiers or other syntactic resources. The mathematical correctness follows from the proof; finite computation is not an infinite proof. As with any literature comparison, an equivalent bounded-fibre result may be indexed under database-constraint or generalized constraint-satisfaction terminology.

## References
1. J. Kontinen and I. Ciardelli, *On the Expressive Power of Inquisitive Team Logic and Inquisitive First-Order Logic*, arXiv:2603.08646, first public 9 March 2026, especially Definition 2.1, the value-question derivation, locality, and Theorem 3.7; https://arxiv.org/html/2603.08646.
2. I. Ciardelli and S. Conti, *Connecting state-based and team-based inquisitive logic*, Journal of Logic and Computation 36 (2026), article exag032; https://doi.org/10.1093/logcom/exag032. Its purpose is an entailment-preserving translation between two inquisitive semantic settings, not a bounded-fibre data-complexity classification.
3. J. Kontinen, *Coherence and Computational Complexity of Quantifier-free Dependence Logic Formulas*, Studia Logica 101 (2013), 267–291, https://doi.org/10.1007/s11225-013-9481-8 (related logic/complexity background, not taken as a proof of the present claim).
