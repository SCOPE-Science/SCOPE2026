# Eleven spectra, sixty-seven atomic types, and a sharp seven-element bound in two-noun cardinality syllogistic

## Finding

Fix the language \(S^{\dagger}(\mathrm{card})\) with exactly two raw noun variables \(p,q\), their complements, and the four atomic sentence forms: subset, nonempty intersection, weak cardinality comparison, and strict cardinality comparison. Models have finite **nonempty** universes; a theory is any set of atomic sentences, with no sentence-level Boolean connectives.

For \(j\geq1\), write \(T_j=\{n\geq1:n\geq j\}\) and \(E_j=\{n\geq1:n\geq j\text{ and }2\mid n\}\). Then the possible finite spectra of theories are exactly
\[
\boxed{\{\varnothing\}\ \cup\ \{T_1,T_2,T_3,T_4,T_5,T_6,T_7\}\ \cup\ \{E_2,E_4,E_6\}.}
\]
There are exactly \(67\) realizable complete atomic truth types of finite nonempty two-noun interpretations. Every such type has a representative on at most \(7\) elements, and the bound \(7\) is optimal. In particular every satisfiable two-noun atomic theory has a model of at most seven elements. The same seven-element truth-type reduction also applies to satisfiability of Boolean combinations of the atoms, but the eleven-spectrum classification is asserted only for atomic theories.

## Assumptions and scope

Let \(M\) be a finite nonempty set and interpret \(p,q\) as arbitrary subsets \(P,Q\subseteq M\), with complements relative to \(M\). The nouns are exactly \(p,\bar p,q,\bar q\); no noun-level union/intersection and no additional raw nouns are allowed. For nouns \(x,y\), the permitted atomic sentences assert \(I(x)\subseteq I(y)\), \(I(x)\cap I(y)\neq\varnothing\), \(|I(x)|\geq |I(y)|\), or \(|I(x)|>|I(y)|\). A complete atomic type records the truth values of all \(64\) syntactically ordered atomic tests (four kinds and sixteen ordered noun pairs); the variables remain labeled, with no quotient under swapping or complementing names.

Put
\[
a=|P\cap Q|,\quad b=|P\cap Q^c|,\quad c=|P^c\cap Q|,\quad d=|P^c\cap Q^c|,
\]
so that \(a,b,c,d\in\mathbb N\) and \(a+b+c+d=|M|\geq1\). Define \(s=b-c\) and \(t=a-d\). Here \(\mathbb N\) includes zero.

## Proof

**1. Complete atomic invariants.** The subset and nonempty-intersection tests depend only on which of the four cells \(a,b,c,d\) are zero. The four nontrivial comparisons among noun sizes are controlled, up to sign reversal, by
\[
|P|-|Q|=s,\quad |P|-|Q^c|=t,\quad |P|-|P^c|=s+t,\quad |Q|-|Q^c|=t-s.
\]
All other noun-size differences are zero or their negatives. Conversely the four cell-positivity flags are read by \(\exists(p,q)\), \(\exists(p,\bar q)\), \(\exists(\bar p,q)\), \(\exists(\bar p,\bar q)\), and the four displayed signs are read by strict and weak cardinality comparisons. Thus the exact complete atomic invariant is
\[
\bigl(\mathbf1_{a>0},\mathbf1_{b>0},\mathbf1_{c>0},\mathbf1_{d>0};\operatorname{sgn}(s),\operatorname{sgn}(t),\operatorname{sgn}(s+t),\operatorname{sgn}(t-s)\bigr).
\]

**2. Counting the types.** Consider the pair \((b,c)\), which determines \(s\). Its support has four possibilities: both zero, first alone, second alone, or both positive. Counting support together with the sign of \(s\), there are exactly two ways to have \(s=0\) and four ways to have \(s\neq0\). The same counts apply to \((a,d)\) and \(t\). If both differences are nonzero, three relative magnitude orders \(|s|<|t|\), \(|s|=|t|\), or \(|s|>|t|\) are possible and distinguishable from the signs of \(s+t\) and \(t-s\). If at least one difference is zero there is only one corresponding sign pattern. Every indicated nonzero configuration is realizable by positive integral cell sizes. Excluding the empty universe, the number of atomic types is therefore
\[
2\cdot2+2\cdot4+4\cdot2+3\cdot4\cdot4-1=\boxed{67}.
\]

**3. Uniform small representatives.** Given a realizable type, retain the signs of \(s,t\) and their relative absolute sizes, but replace their magnitudes as follows: choose both zero if both were zero; choose magnitude \(1\) for the sole nonzero difference; if both are nonzero choose \((|s|,|t|)=(1,1),(1,2),(2,1)\) according as the original magnitudes were equal, the first smaller, or the first larger. This preserves the signs of \(s,t,s+t,t-s\), with \(|s|+|t|\leq3\).

Realize each reduced difference with the same zero/nonzero flags. For instance, when \(b,c>0\), take \((b,c)=(1+\max(s,0),1+\max(-s,0))\); if only one cell is positive, give it size \(|s|\); if neither is positive use \((0,0)\). Do the same for \((a,d)\) and \(t\). Each positive cell costs a baseline of at most one, plus at most the absolute difference for its pair. Consequently
\[
1\leq a+b+c+d\leq \#\{\text{positive cells}\}+|s|+|t|\leq4+3=7.
\]
Every atomic statement, including all negated statements in a Boolean sentence-level extension, is preserved. Hence every satisfiable atomic theory has a model of size at most seven.

**4. Optimality.** Require each of the four intersections determined by \(p,q\) and their complements to be nonempty, and add \(\exists^{>}(p,q)\) and \(\exists^{>}(q,\bar q)\). In the cell notation these assert \(a,b,c,d\geq1\), \(s>0\), and \(t-s>0\). Thus \(s\geq1\), \(t\geq s+1\geq2\), and
\[
|M|=a+b+c+d\geq4+s+t\geq7.
\]
The four-cell vector \((a,b,c,d)=(3,2,1,1)\) realizes this theory on seven elements. This also exhibits a complete atomic type whose smallest model has size seven.

**5. Spectral upper classification.** Jiang's spectrum theorem for the unrestricted vocabulary says that every finite spectrum of an atomic \(S^{\dagger}(\mathrm{card})\)-theory is either empty, an ordinary tail \(T_j\), or an even tail \(E_j\) [1, Theorem 3.16]. Applied to the two-noun sublanguage, our seven-element bound forces the least spectrum element to be at most seven. Hence the only possible nonempty spectra are \(T_1,\ldots,T_7\) and \(E_2,E_4,E_6\).

**6. Every candidate spectrum is realized.** For succinctness write \(F\) for the conjunction, as an atomic theory, of the four nonempty-intersection sentences in Step 4. Write \(x\sim y\) for the pair of weak comparisons \(\exists^{\geq}(x,y),\exists^{\geq}(y,x)\); thus \(x\sim y\) asserts equal sizes. The following table gives theories whose models realize precisely the indicated spectrum. All entries are sets of permitted atomic sentences, not use of a conjunction connective in the original language.

| Spectrum | Requirements beyond tautologies |
|---|---|
| \(T_1\) | none |
| \(T_2\) | \(\exists(p,p),\ \exists(\bar p,\bar p)\) |
| \(T_3\) | \(T_2\) requirements and \(\exists^{>}(p,\bar p)\) |
| \(T_4\) | \(F\) |
| \(T_5\) | \(F\) and \(\exists^{>}(p,q)\) |
| \(T_6\) | \(F\), \(\exists^{>}(p,q)\), \(\exists^{>}(p,\bar q)\) |
| \(T_7\) | \(F\), \(\exists^{>}(p,q)\), \(\exists^{>}(q,\bar q)\) |
| \(E_2\) | \(p\sim\bar p\) |
| \(E_4\) | \(F\) and \(p\sim\bar p\) |
| \(E_6\) | \(F\), \(\exists^{>}(p,q)\), and \(q\sim\bar q\) |

The minimum cell vectors, in table order, are \((1,0,0,0)\), \((1,0,1,0)\), \((1,1,0,1)\), \((1,1,1,1)\), \((1,2,1,1)\), \((2,2,1,1)\), \((3,2,1,1)\), \((1,0,1,0)\), \((1,1,1,1)\), \((2,2,1,1)\). For \(T_1,T_2,T_3,T_4,T_6,T_7\), all larger cardinalities are obtained by adding elements to cell \(a\); for \(T_5\), add them to cell \(b\). For \(E_2,E_4\), add equally many elements to cells \(a,c\); for \(E_6\), add equally many to cells \(a,d\). Each operation preserves all displayed requirements. The given lower bounds follow directly from cell positivity, strict integer inequalities, and (for the last three entries) even parity. An inconsistent theory gives the empty spectrum. This proves the eleven-spectrum classification.

## Verification

The standalone Python 3 file `verify_two_noun.py` exhaustively evaluates all \(64\) actual atomic sentence truth values on four-cell count vectors up to universe size \(18\), independently constructs their proposed support/sign invariants, checks the exact one-to-one match, obtains the \(67\) types and their minimum-size distribution, and tests every displayed spectral construction for all universe sizes \(1\) through \(18\). It outputs `TWO_NOUN_CARDINALITY_VERIFY_OK`. The all-size theorem follows from the proofs above, not from the finite enumeration.

The observed minimum representative sizes are distributed as follows: \(4\) types at size \(1\), \(6\) at size \(2\), \(16\) at size \(3\), \(9\) at size \(4\), \(20\) at size \(5\), \(4\) at size \(6\), and \(8\) at size \(7\).

## Relationship to prior work

Jiang [1] proves the unrestricted-vocabulary classification into ordinary and even tails. That stronger-in-vocabulary theorem is used here for the **shape** of spectra; it does not state the sharp two-noun cutoff, enumerate the two-noun possibilities, or count their complete atomic types. Moss [2] introduced the finite-model cardinality syllogistic, with completeness and algorithms. The infinite-universe version is studied by Moss and Topal [3]. A prior published one-noun classification [4] identifies five spectra; it treats a strictly smaller vocabulary and does not establish the two-independent-difference geometry used here. The new conclusions require keeping both correlated noun margins \(s,t\) and the hyperplanes \(s=0,t=0,s=t,s=-t\).

## Limitations

The eleven-spectrum result applies to atomic theories over exactly two raw nouns and their complements, on finite nonempty universes. It does not classify spectra for larger vocabularies or for arbitrary sentence-level disjunctions. The \(67\)-type quotient and seven-element bound **do** extend to finite Boolean combinations of the same atoms, because their complete atomic truth vectors are preserved. The 2016 foundational book chapter [2] was identified through its abstract and bibliographic record, but its full text was not available for comparison; historical priority therefore retains uncertainty.

## References

[1] Ruiting Jiang, *Finite Spectra of Syllogistic Logic with Cardinality Comparisons*, arXiv:2609.24902, first public 2026-09-21, especially Definitions 2.2–2.4 and Theorem 3.16. https://arxiv.org/abs/2609.24902

[2] Lawrence S. Moss, *Syllogistic Logic with Cardinality Comparisons*, in *J. Michael Dunn on Information Based Logics*, 2016, pp. 391–415, DOI 10.1007/978-3-319-29300-4_18. The available abstract describes finite-model proof search and construction, not the two-noun type enumeration. https://doi.org/10.1007/978-3-319-29300-4_18

[3] Lawrence S. Moss and Selçuk Topal, *Syllogistic Logic with Cardinality Comparisons, On Infinite Sets*, arXiv:1705.03037, first public 2017-05-08. https://arxiv.org/abs/1705.03037

[4] *The one-variable cardinality syllogistic has exactly five finite spectra*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-one-variable-cardinality-syllogistic-has-exactly-five-finite--115eacbc2bad
