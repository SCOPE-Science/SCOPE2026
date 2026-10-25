# Monotonicity in monadic logic with the infinity quantifier is \(\mathrm{coNEXPTIME}\)-complete

## Finding

In combined complexity, for \(\mathrm{ME}^{\infty}\) sentences over an input-specified finite but unbounded unary vocabulary, deciding whether a sentence is monotone in a designated unary predicate is \(\mathrm{coNEXPTIME}\)-complete under polynomial-time many-one reductions. The hardness already holds when the designated predicate occurs only negatively.

Here \(\mathrm{ME}^{\infty}\) is monadic first-order logic with equality, unary predicate symbols, the ordinary quantifiers \(\exists,\forall\), and the generalized quantifiers \(\exists^{\infty},\forall^{\infty}\), interpreted as “infinitely many” and “all but finitely many.” A sentence \(\varphi\) is monotone in \(P\) when, for every domain \(D\), fixed interpretations of the other predicates, and subsets \(X\subseteq Y\subseteq D\), truth of \(\varphi\) with \(P=X\) implies truth with \(P=Y\). The statement includes the empty-domain convention; the lower-bound reduction uses nonempty models.

## Assumptions and scope

The vocabulary is part of the input, so the number of unary predicates is not fixed. Input length is the ordinary finite encoding length of the sentence and designated predicate. Reductions are polynomial-time many-one reductions. The result does not assert a complexity classification for any fixed-vocabulary restriction.

## Proof

Let \(P'\) be a fresh unary predicate and let \(\varphi[P'/P]\) denote replacement of every occurrence of \(P\) by \(P'\), leaving all other predicates unchanged. Form the sentence
\[
\chi_{\varphi,P}:=\varphi\wedge\neg\varphi[P'/P]\wedge\forall x\,(P(x)\to P'(x)).
\]
A model of \(\chi_{\varphi,P}\) is exactly a same-domain counterexample to monotonicity: the two interpretations of the designated predicate are nested, the other predicates are shared, and truth changes from true to false. Thus nonmonotonicity is equivalent to satisfiability of \(\chi_{\varphi,P}\), whose length is linear in the input length.

For the upper bound, let \(n\) be the input length and set \(r=\max(1,\operatorname{qr}(\chi_{\varphi,P}))\). If the combined vocabulary has \(m\) unary predicates, each element has one of \(2^m\) unary types. For each type, guess one of the following cardinality states: exact size \(c<r\), finite size at least \(r\), or infinite size. The quantifier-rank profile theorem for \(\mathrm{ME}^{\infty}\) says that two models with the same profile satisfy the same sentences of quantifier rank at most \(r\): for every type, their counts either agree exactly below \(r\), are both finite and at least \(r\), or are both infinite. Hence every satisfiable input has a canonical profile model with exactly \(c\) elements for a state \(c<r\), exactly \(r\) elements for a finite-large state, and countably infinitely many elements for an infinite state.

The guessed profile has size \(O(2^m\log(r+2))\), exponential in \(n\). To evaluate the sentence on its canonical model, symbolic recursion need consider only the elements already assigned to variables and one fresh representative of each unary type. For \(\exists^{\infty}\), infinitely many witnesses exist exactly when a fresh representative of some infinite type satisfies the subformula; for \(\forall^{\infty}\), every infinite type must satisfy the subformula on its fresh representatives. Since at most \(r\) variables are simultaneously assigned, a direct recursive evaluator has at most \((2^m+r)^r=2^{O(n^2)}\) branches. Guessing a profile and running this evaluator is nondeterministic exponential time. Therefore satisfiability for \(\mathrm{ME}^{\infty}\) is in \(\mathrm{NEXPTIME}\), so nonmonotonicity is in \(\mathrm{NEXPTIME}\) and monotonicity is in \(\mathrm{coNEXPTIME}\).

For hardness, take a sentence \(\theta\) of ordinary equality-free monadic first-order logic, with standard nonempty-domain semantics, and introduce a fresh predicate \(P\). Set
\[
\psi(P):=\theta\wedge\forall x\,\neg P(x).
\]
If \(\theta\) has a nonempty model with domain \(D\), then \(\psi\) is true at \(P=\varnothing\) and false at \(P=D\), so \(\psi\) is not monotone in \(P\). If \(\theta\) has no nonempty model, \(\psi\) is false on every nonempty domain; on the empty domain there is no proper enlargement of \(P\), so \(\psi\) is monotone. Thus \(\theta\) is satisfiable exactly when \(\psi\) is nonmonotone. Lewis proved NEXPTIME-hardness for monadic satisfiability, already for a monadic prefix fragment without equality. The reduction is polynomial-time and uses \(P\) only negatively. Hence nonmonotonicity is \(\mathrm{NEXPTIME}\)-hard, and monotonicity is \(\mathrm{coNEXPTIME}\)-hard even under that polarity restriction. Combining the bounds proves the claim.

## Verification

The upper bound uses the published quantifier-rank profile characterization together with an explicit symbolic evaluation argument; the lower bound uses the monadic-satisfiability reduction above. The empty-domain case is handled separately in the hardness argument. No fixed-vocabulary or finer-grained time bound is claimed, and no mechanized checker is supplied.

## Relationship to prior work

Carreiro, Facchini, Venema, and Zanasi characterize monotonicity in \(\mathrm{ME}^{\infty}\) by equivalence to a positive fragment and prove decidability. Their introduction explicitly leaves computational-complexity questions unexplored; their quantifier-rank profile result supplies the structural input for the upper bound here. Lewis establishes the monadic satisfiability lower bound, but does not study this semantic monotonicity problem. The exact \(\mathrm{coNEXPTIME}\)-completeness classification follows from the profile-based upper bound and the counterexample reduction, not from a matching complexity statement in either source.

## Limitations

The classification is for combined complexity with an unbounded finite unary vocabulary. It does not classify the fixed-vocabulary case, provide a finer time bound, or include an executable implementation. The lower bound depends only on ordinary monadic first-order logic, so the infinity quantifiers are not needed for hardness.

## References

1. F. Carreiro, A. Facchini, Y. Venema, and F. Zanasi, “Model theory of monadic predicate logic with the infinity quantifier,” *Archive for Mathematical Logic* 61 (2022), 465–502; first published online 27 October 2021. DOI: 10.1007/s00153-021-00797-0. Relevant material: introduction’s complexity discussion; Definition 14 and Proposition 5; Theorem 3.
2. H. R. Lewis, “Complexity results for classes of quantificational formulas,” *Journal of Computer and System Sciences* 21(3) (1980), 317–353. DOI: 10.1016/0022-0000(80)90027-6. Relevant material: Theorem 4.1 and Corollary 4.2 on the monadic satisfiability lower bound.
