# A Frankl majority-literal theorem for shallow exact-equivalence normal forms
## Finding
Fix a finite propositional vocabulary with \(q\ge 1\) variables in Berardi Gili's modal logic of exact equivalence, and let \(C_n\) be the set of canonical representatives of literals of modal degree at most \(n\), with \(R_n=|C_n|\). Then \(R_0=2q\), \(R_1=R_0+2(2^{R_0}-1)\), and for \(n\ge1\), \(R_{n+1}=R_n+2(2^{R_n}-2^{R_{n-1}})\). Every exact-equivalence class of formulas of modal degree at most \(n\) is represented uniquely by a nonempty union-closed family \(\mathcal F\) of nonempty subsets of \(C_n\): for a normal form \(D\), \(\mathcal F\) is the set of distinct canonical representations of the state-description disjuncts in \(cl(D)\), and every such union-closed family occurs. Consequently, using the published theorem that Frankl's union-closed sets conjecture holds on universes of size at most \(12\), every formula in either fragment \(n=0, q\le6\) or \(n=1, q=1\) has an exactly equivalent closed normal form for which some canonical literal representative occurs in at least half of its distinct canonical state-description disjunct classes. These are exactly the positive-\(q\) parameter pairs for which the ambient bound \(R_n\le12\) gives this uniform conclusion from the published 12-element theorem; no failure of the majority property is claimed outside those pairs.

## Assumptions and scope
Work in the inclusive exact truthmaker semantics and proof system \(\mathbf{E}_\lozenge\) of Berardi Gili. Fix a finite set \(P\) of \(q\ge1\) propositional variables. A degree-\(0\) literal is \(p\) or \(\neg p\); a degree-\(n+1\) literal is \(\lozenge\pi\) or \(\neg\lozenge\pi\) for a state description \(\pi\) of degree \(n\); and a state description is a nonempty finite conjunction of literals of allowed degrees. For a literal \(\lambda\), write \(cr(\lambda)\) for its canonical representative, and for a state description \(\pi\), write \(|\pi|\) for the set of canonical representatives of its conjuncts.

Let \(C_n\) be the set of canonical representatives of literals whose least modal degree is at most \(n\), and set \(R_n=|C_n|\). For a normal form \(D\), let \(cl(D)\) be Berardi Gili's closure, obtained by adjoining the conjunction of every nonempty set of disjuncts of \(D\). Define
\[
\mathcal F_D=\{\,|\pi|: \pi\text{ is a disjunct of }cl(D)\,\}.
\]
Repeated syntactic disjuncts with the same canonical representation contribute only one member to \(\mathcal F_D\).

## Proof
There are exactly \(2q\) degree-\(0\) canonical literal representatives, so \(R_0=2q\). Every state-description representation using literals of degree at most \(n\) is a nonempty subset of \(C_n\), and every nonempty subset is realized by conjoining one literal for each representative. Distinct representations are distinct exact-equivalence classes of state descriptions: Berardi Gili's canonical-model Lemma 4 separates unequal representations, while the proof sketch following Lemma 5 shows that equal representations are provably equivalent.

A new canonical representative of modal degree \(1\) is either \((\lozenge,A)\) or \((\neg\lozenge,A)\), where \(A\) is a nonempty subset of \(C_0\). Hence
\[
R_1=R_0+2(2^{R_0}-1).
\]
For \(n\ge1\), the state descriptions of least modal degree exactly \(n\) are represented by the nonempty subsets of \(C_n\) that are not contained in \(C_{n-1}\). Their number is \(2^{R_n}-2^{R_{n-1}}\). Each yields two new signed modal representatives, so
\[
R_{n+1}=R_n+2(2^{R_n}-2^{R_{n-1}}).
\]

Now let \(D\) be a normal form. If its original disjunct representations are \(A_1,\ldots,A_k\), then a closure disjunct is a conjunction of a nonempty selection of original disjuncts, and its canonical representation is the union of the corresponding \(A_i\). Therefore
\[
\mathcal F_D=\left\{\bigcup_{i\in I}A_i: \varnothing\ne I\subseteq\{1,\ldots,k\}\right\},
\]
so \(\mathcal F_D\) is a nonempty union-closed family of nonempty subsets of \(C_n\). Conversely, if \(\mathcal F\) is any nonempty union-closed family of nonempty subsets of \(C_n\), choose a state description \(\pi_A\) with \(|\pi_A|=A\) for each \(A\in\mathcal F\), and let \(D=\bigvee_{A\in\mathcal F}\pi_A\). Since \(\mathcal F\) is already union closed, \(\mathcal F_D=\mathcal F\).

Berardi Gili proves \(D\approx cl(D)\) and, in the canonical model, that the exact verifiers of \(D\) are precisely the canonical representations of closure disjuncts. Thus two normal forms are exactly equivalent exactly when their families \(\mathcal F_D\) agree. Together with the normal-form theorem, this gives the stated bijection for formulas of modal degree at most \(n\).

Vučković and Živković proved that every finite union-closed family whose universe has at most \(12\) elements has an element belonging to at least half of its members. Since the universe of \(\mathcal F_D\) is contained in \(C_n\), this theorem applies uniformly whenever \(R_n\le12\). The recurrence gives \(R_0=2q\), so at degree \(0\) this is exactly \(q\le6\). At degree \(1\), \(R_1=2q+2(2^{2q}-1)\), which is \(8\) for \(q=1\) and already \(34\) for \(q=2\). For \(q=1\), the next value is \(R_2=8+2(2^8-2^2)=512\), and the sequence is increasing. Hence the positive-\(q\) pairs with \(R_n\le12\) are exactly \(n=0,q\le6\) and \(n=1,q=1\). Frankl's conclusion for \(\mathcal F_D\) is exactly the claimed majority occurrence of one canonical literal representative among the distinct canonical state-description classes.

## Verification
The proof was reconstructed from Berardi Gili's Definitions 7--10, closure Lemmas 2--3, canonical-model Lemmas 4--5, and completeness theorem. The counting recurrence was checked directly from the distinction between least modal degree and cumulative allowed degree; in particular, the degree-\(2\) count for one variable is \(512\), not the overcount obtained by re-adding lower-degree modal representatives. The published 12-element Frankl theorem was checked in its primary article statement.

## Relationship to prior work
Berardi Gili proves soundness, normal forms, closure, completeness and decidability for modal exact equivalence, but does not identify the canonical closure families as arbitrary finite union-closed set systems or connect them to Frankl's conjecture. Earlier inclusive truthmaker semantics explicitly uses closure under fusion, and Correia/Fine--Jago supply the propositional closure machinery used by Berardi Gili; this explains why union closure is structurally natural but does not state the classification or majority-literal consequence here. Vučković and Živković prove the independent combinatorial theorem for universes of size at most \(12\), without a truthmaker or modal application. Searches for the direct combination, aliases, and the parameter boundary did not locate a published statement implying this result.

## Limitations
The Frankl step imports a published computer-assisted theorem; its underlying exhaustive computation was not independently replayed here. The logical transfer and all finite representative counts were checked directly. The parameter statement is only the exact boundary for a uniform application of the published \(12\)-element theorem through the ambient size \(R_n\); formulas outside these fragments can still have smaller closure universes and may satisfy the same majority conclusion, and no counterexample outside the displayed pairs is asserted. The result concerns positive exact content in the inclusive semantics used by the source and does not claim an analogue for bilateral exact equivalence, exact consequence, quantified languages, or non-inclusive semantics.

## References
1. Pietro Berardi Gili, *The Modal Logic of Exact Equivalence*, *The Review of Symbolic Logic* 19 (2026), 519--535. DOI: 10.1017/S1755020326101154. Published online 06 May 2026.
2. Bojan Vučković and Miodrag Živković, *The 12-Element Case of Frankl's Conjecture*, *IPSI BGD Transactions on Internet Research* 13(1) (2017), 65--71.
3. Julia Korbmacher, *Proof Systems for Exact Entailment*, *The Review of Symbolic Logic* 16(4) (2023), 1260--1295. DOI: 10.1017/S175502032200020X.
