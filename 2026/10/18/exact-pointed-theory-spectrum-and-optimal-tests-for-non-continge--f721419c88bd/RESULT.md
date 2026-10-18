# Exact pointed-theory spectrum and optimal tests for non-contingency stars

## Finding

For every integer \(n\geq 0\), let \(B_n=\{0,1\}^n\), \(N=2^n\), and consider all classical Kripke models whose frame is a **nonreflexive rooted star**: a root, any set (including the empty set) of terminal successors, and no other arrows. The language has only \(n\) specified propositional letters, Boolean connectives and the non-contingency operator \(\Delta\), where \(\Delta\varphi\) means that all immediate successors agree about \(\varphi\).

Let \(v\in B_n\) be the atomic truth vector at the root and let \(S\subseteq B_n\) be the set of atomic vectors realized among successors. Two pointed stars satisfy exactly the same formulas **if and only if** their root vectors agree and either their successor supports agree or both successor supports have at most one member. Consequently the exact number of complete pointed theories is

\[
T_n=2^n\bigl(2^{2^n}-2^n\bigr).
\]

Every formula over this class has an equivalent formula of modal depth at most one. The bound is sharp for every \(n\geq1\). More strongly, every subset of the \(T_n\) pointed theories is definable; thus the algebra of formula meanings on this class has exactly \(2^{T_n}\) elements.

Fix any root vector and ask for a fixed family of yes/no non-contingency questions sufficient to identify the successor support up to complete-theory equivalence. The optimal family size is \(0\) for \(n=0\), \(1\) for \(n=1\), and \(2^n\) for \(n\geq2\). These bounds apply even when the questions may contain arbitrary nested formulas.

## Assumptions and scope

The root is distinguished. It has zero or more successors. Every successor is terminal, and no successor has an arrow to the root or itself. The successor set may be infinite, but its distinct atomic vectors form a subset of the finite set \(B_n\). The language has classical truth-functional negation, conjunction, the true constant, and \(\Delta\) (other Boolean connectives are abbreviations). For every world \(w\),

\[
M,w\models\Delta\psi \quad\Longleftrightarrow\quad
\text{for all }u,u'\text{ with }wRu,wRu',\ 
(M,u\models\psi\Longleftrightarrow M,u'\models\psi).
\]

The empty- and singleton-successor cases satisfy every \(\Delta\psi\), by vacuity. Models are compared at the root and only for the specified finite language; no frame-definability assertion for unrestricted graphs is made. The symbol \(S\) denotes distinct valuation types, not individual leaves or their multiplicities.

## Proof

**Terminal flattening.** Define the Boolean flattening \(f(\psi)\) by replacing each modal subformula \(\Delta\eta\) by the truth constant, recursively respecting the Boolean operations. At a terminal world every \(\Delta\eta\) is true. Structural induction therefore gives \(M,u\models\psi\iff f(\psi)(\operatorname{val}(u))=1\) for every terminal world \(u\). Thus at the root \(\Delta\psi\) holds precisely when the Boolean function \(f(\psi)\) is constant on \(S\). The root truth of every formula is determined by \(v\) and \(S\), with all \(|S|\leq1\) cases indistinguishable.

**Exact separation.** For each \(a\in B_n\), let \(\chi_a\) be the conjunction of the \(n\) literals specifying exactly the valuation \(a\); when \(n=0\), put \(\chi_a=\top\). If \(|S|\geq2\), then \(\chi_a\) takes both Boolean values on \(S\) exactly when \(a\in S\). Therefore

\[
M,r\models\neg\Delta\chi_a \quad\Longleftrightarrow\quad a\in S\qquad(|S|\geq2).
\]

If \(|S|\leq1\), every \(\Delta\chi_a\) is true. The vector of the \(N\) modal answers is therefore injective on the family consisting of the single collapsed small-support class and all \(S\subseteq B_n\) of size at least two. Root literals recover \(v\). This proves both directions of the claimed exact pointed equivalence. The number of successor classes is \(1+(2^N-1-N)=2^N-N\). Multiplying by the \(N\) freely chosen root vectors gives \(T_n=N(2^N-N)\).

**Constructive normal form and semantic algebra.** For a root vector \(v\), write \(\chi_v\) for its propositional minterm. Define

\[
\Theta_{v,*}=\chi_v\land\bigwedge_{a\in B_n}\Delta\chi_a,
\]

and for each \(S\subseteq B_n\) with \(|S|\geq2\) define

\[
\Theta_{v,S}=\chi_v\land
\bigwedge_{a\in S}\neg\Delta\chi_a\land
\bigwedge_{a\in B_n\setminus S}\Delta\chi_a.
\]

These depth-one formulas isolate precisely the \(T_n\) mutually exclusive complete theories. Their finite disjunctions realize every subset of those theories. Every original formula is equivalent, on this class, to the disjunction of exactly those isolation formulas whose pointed types satisfy it. There are therefore exactly \(2^{T_n}\) formula meanings, all attained at depth at most one. For \(n\geq1\), \(\Delta p_1\) has different truth values on stars with the same root valuation (compare a single successor to two successors disagreeing about \(p_1\)); a modal-depth-zero formula cannot do this. Thus the modal-depth bound is sharp.

**Optimal questions.** The \(N\) questions \(\Delta\chi_a\) reconstruct the successor class. For \(n=0\), only one class exists and no question is needed. For \(n=1\), precisely two classes exist and \(\Delta p_1\) is sufficient. For \(n\geq2\), \(N\geq4\), and the number of successor classes is \(2^N-N>2^{N-1}\). Any collection of \(N-1\) yes/no formulas produces at most \(2^{N-1}\) distinct answer strings (even permitting adaptive choice), so it cannot separate every class. This information bound is attained by the \(N\) explicit questions.

## Verification

The included standalone Python checker enumerates every support for \(n=0,1,2,3\) and checks the exact quotient sizes \(1,2,12,248\) and total pointed-theory counts \(1,4,48,1984\). It independently evaluates thousands of root/terminal truth tables of mixed nested formulas and compares them with the flattening recursion. These finite checks are consistency tests, not substitutes for the all-\(n\) structural induction and elementary counting arguments above. Run with `python3 verify.py`.

## Relationship to prior work

Sierra Miranda, Wang and Zenger (2026) develop labelled sequent calculi for non-contingency logic and fix the standard semantics. Fan, Wang and van Ditmarsch (2014), especially their Section 3, establish a general \(\Delta\)-bisimulation theory that already explains why observationally homogeneous successor configurations may collapse. **The qualitative fact that this language cannot always see successor multiplicity is not new.** The present statement is a quantitative, class-specific complete pointed-theory and formula-algebra enumeration with explicit depth-one isolators and the exact optimal number of detecting questions. The 2014 bisimulation invariance theorem does not give these counts or an optimal family of questions as stated. Bradley and Swartz (1979, chapter on S5, counting section) count equivalence classes in the full normal-modal S5 semantics; that count concerns reflexive equivalence frames with necessity, rather than nonreflexive stars with non-contingency as the only modality.

## Limitations

The frame restriction is essential; nesting need not collapse on general Kripke frames. The theorem counts indistinguishable pointed theories and formula meanings, not syntactic formulas or graph isomorphism classes. It assumes all valuations of the specified atoms are permitted at each world. The contribution is a finite-variable structural classification, not a new general characterization of non-contingency or a claim of absolute historical priority. Generic bisimulation and modal-normal-form machinery may facilitate alternate derivations. Independent review of originality and correctness has not been performed.

## References

1. Borja Sierra Miranda, Yunsong Wang, and Lukas Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975v1, first posted 2026-09-30. https://arxiv.org/html/2609.38975v1
2. Jie Fan, Yanjing Wang, and Hans van Ditmarsch, *Almost Necessary*, Advances in Modal Logic 10 (2014), 178–196. Author-uploaded accessible text: https://www.researchgate.net/publication/278156587_Almost_Necessary
3. Raymond Bradley and Norman Swartz, *Possible Worlds: An Introduction to Logic and Its Philosophy*, Hackett (1979), chapter on modal propositional logic, section 10. https://studylib.net/doc/13901139/
