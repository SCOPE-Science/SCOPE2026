# Moore-family semantic quotient of union-closed team logics

## Finding
Fix a finite set \(N\) of propositional variables with \(|N|=n\), and let
\[
V=2^N
\]
be the \(2^n\)-element set of classical valuations on \(N\). Consider any of the five union-closed propositional team logics treated as expressively complete by Yang: \(\mathbf{CPL}(\veedot)\), \(\mathbf{CPL}(\subseteq_0)\), \(\mathbf{CPL}(\subseteq)\), \(\mathbf{CPL}(\neq(\cdot))\), or \(\mathbf{CPL}(\Upsilon)\), under the paper's lax team semantics.

Then the entailment-ordered semantic quotient of formulas over \(N\) is isomorphic to the inclusion lattice of Moore families on \(V\). Equivalently, semantic formula classes are in bijection with closure systems on the \(2^n\)-element valuation set. Consequently, if \(q_n\) is the number of semantic equivalence classes, then
\[
\boxed{q_n=M_{2^n},}
\]
where \(M_m\) is the number of Moore families, equivalently closure operators, on an \(m\)-element labeled set (OEIS A102896). In particular,
\[
\boxed{q_0=2,\qquad q_1=7,\qquad q_2=2480.}
\]

The classical asymptotic enumeration of Moore families gives
\[
\log_2 M_m\sim \binom{m}{\lfloor m/2\rfloor}.
\]
Substituting \(m=2^n\) yields
\[
\boxed{\log_2 q_n\sim \binom{2^n}{2^{n-1}}}
\]
and hence, by the central-binomial asymptotic,
\[
\log_2 q_n\sim 2^{2^n}\sqrt{\frac{2}{\pi 2^n}},
\qquad
\log_2\log_2 q_n
=2^n-\frac n2-\frac12\log_2(\pi/2)+o(1).
\]
Thus the fixed-variable semantic quotient of these union-closed team logics has triple-exponential scale in \(n\), whereas ordinary classical propositional logic has exactly \(2^{2^n}\) semantic classes.

## Assumptions and scope
Yang's expressive-completeness result is used in its finite propositional, lax-team-semantics setting. For a fixed variable domain \(N\), an \(N\)-team is a subset of \(V=2^N\). The five logics above define exactly the union-closed families of \(N\)-teams that contain the empty team.

The statement counts semantic equivalence classes, not syntactically distinct formulas. It does not apply to Yang's strict semantics, where locality fails, and it does not claim that the original variable-only version of propositional inclusion logic is expressively complete; Yang explicitly distinguishes that weaker variant. The order statement is made for Moore families under inclusion. Although Moore families correspond bijectively to closure operators, their inclusion order should not be confused with the usual pointwise order on closure operators.

## Proof
For a formula \(\varphi\) over \(N\), write
\[
\llbracket\varphi\rrbracket_N
=\{X\subseteq V:X\models\varphi\}.
\]
Yang proves two facts that are decisive here: every such denotation contains \(\varnothing\) and is closed under unions, and conversely every union-closed family of \(N\)-teams containing \(\varnothing\) is the denotation of a formula in each of the five logics. Locality ensures that the fixed-domain denotation is the correct semantic invariant. Therefore semantic equivalence classes over \(N\) are exactly the families
\[
\mathcal F\subseteq\mathcal P(V)
\]
that contain \(\varnothing\) and are closed under arbitrary finite unions. (Since \(V\) is finite, binary-union closure is equivalent to finite-union closure.) Moreover,
\[
\varphi\models\psi
\quad\Longleftrightarrow\quad
\llbracket\varphi\rrbracket_N\subseteq\llbracket\psi\rrbracket_N.
\]

Now apply pointwise set complementation inside \(V\):
\[
D(\mathcal F)=\{V\setminus X:X\in\mathcal F\}.
\]
Because \(\varnothing\in\mathcal F\), one has \(V\in D(\mathcal F)\). De Morgan's law gives
\[
V\setminus(X\cup Y)=(V\setminus X)\cap(V\setminus Y),
\]
so \(D(\mathcal F)\) is intersection-closed. Conversely, complementing an intersection-closed family containing \(V\) gives a union-closed family containing \(\varnothing\). The map \(D\) is involutive and preserves inclusion between families. Hence it is an order isomorphism from the semantic quotient to the inclusion lattice of Moore families on \(V\).

The numerical identity \(q_n=M_{2^n}\) follows immediately. OEIS A102896 records \(M_1=2\), \(M_2=7\), and \(M_4=2480\), giving the displayed small-variable values. OEIS A102897 records \(A102897(m)=2M_m\) and cites the classical asymptotic
\[
\log_2 M_m\sim\binom{m}{\lfloor m/2\rfloor}.
\]
The final asymptotic formulas are obtained by setting \(m=2^n\) and applying Stirling's formula to the central binomial coefficient.

## Verification
A standalone C++ replay exhausts every family of subsets of a labeled set of size \(m\le4\). For each family it independently checks union closure, intersection closure, the complement involution, and the requirement that a union-closed family contain \(\varnothing\) exactly when its complement family is a Moore family containing the universe. It obtains

```text
m=1: union_closed_with_empty=2, Moore=2, intersection_closed=4
m=2: union_closed_with_empty=7, Moore=7, intersection_closed=14
m=3: union_closed_with_empty=61, Moore=61, intersection_closed=122
m=4: union_closed_with_empty=2480, Moore=2480, intersection_closed=4960
n=0: q_n=M_(2^n)=2
n=1: q_n=M_(2^n)=7
n=2: q_n=M_(2^n)=2480
VERIFY_OK 2281512 exact assertions/comparisons
```

The replay verifies the finite combinatorial bridge and the first three logical class counts. The general semantic identification uses Yang's expressive-completeness theorem, and the asymptotic uses the classical Moore-family enumeration theorem; neither is replaced by finite computation. Independent audit has not been performed.

## Relationship to prior work
Fan Yang, *Propositional union closed team logics* (arXiv:2008.10324; Annals of Pure and Applied Logic 173(6), 103102, 2022), proves that the five displayed propositional team logics are expressively complete for union-closed team properties containing the empty team. The paper's inspected text does not use the terms “Moore family” or “closure operator” and does not give the resulting finite semantic-class census.

The combinatorics of Moore families is classical. OEIS A102896 identifies the same numbers with Moore families and closure operators, while A102897 records the asymptotic logarithmic enumeration and the relation \(A102897(m)=2A102896(m)\). Those sources do not connect the sequence to the semantic quotient of propositional team logics.

Targeted semantic-index searches for propositional union-closed team logic together with Moore families, closure systems, closure operators, semantic quotients, and exact class counts returned no equivalent result. Exact web searches under the same formulations likewise found no such bridge. The current and preceding cumulative middle-cohort ledgers contain no Moore-family or union-closed-team semantic-quotient finding. A nearby paper, *Counting of Teams in First-Order Team Logics* (MFCS 2019), studies counts of teams in first-order team logics rather than the number of semantic formula classes on a fixed propositional variable set.

The retained originality claim is therefore the explicit order-theoretic bridge and its exact/asymptotic semantic-class consequences, not Yang's expressive-completeness theorem and not the classical enumeration of Moore families.

## Limitations
The result is a short synthesis of two established ingredients, so an equivalent observation may exist as uncatalogued folklore, lecture material, or under closure-system terminology not found by the searches. Exact values of \(M_m\) are known only for small \(m\); in particular the theorem does not provide a new algorithm for computing large Moore-family numbers. The asymptotic is inherited from the classical enumeration literature and is not reproved here. The statement is finite-variable and uses lax team semantics.

## References
1. Fan Yang, *Propositional union closed team logics*, arXiv:2008.10324 (first public version 2020-08-24); Annals of Pure and Applied Logic 173(6), 103102 (2022), DOI 10.1016/j.apal.2022.103102.
2. OEIS A102896, *Number of ACI algebras (or semilattices) on n generators with no annihilator*; comments identify the sequence with Moore families and closure operators.
3. OEIS A102897, *Number of ACI algebras (or semilattices) on n generators*; comments identify intersection-closed families/Horn functions and record the logarithmic asymptotic, citing Alekseev and Burosch--Demetrovics--Katona--Kleitman--Sapozhenko.
4. G. Brinkmann and J. Deklerck, *Generation of Union-Closed Sets and Moore Families*, Journal of Integer Sequences 21 (2018), Article 18.7.4.
