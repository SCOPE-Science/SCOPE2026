# Fixed-vocabulary monotonicity in monadic logic with the infinity quantifier is \(\mathrm{PSPACE}\)-complete

## Finding

For every fixed integer \(k\ge 1\), deciding whether a sentence \(\varphi\) of monadic first-order logic with equality and the infinity quantifiers is monotone in a designated unary predicate \(P\), over possibly empty domains and with exactly \(k\) unary predicates in the input signature, is \(\mathrm{PSPACE}\)-complete under polynomial-time many-one reductions. Hardness already holds for \(k=1\) in the first-order sublanguage without infinity quantifiers.

## Assumptions and scope

The signature contains a fixed number \(k\) of unary predicate symbols, independent of the input length; \(P\) is one of them. The language includes equality and may include \(\exists^\infty x\,\psi\) (infinitely many witnesses) and its dual \(\forall^\infty x\,\psi\) (all but finitely many witnesses). Domains may be empty. Monotonicity in \(P\) means that on every fixed domain, for every pair of valuations that agree on all other predicates and satisfy \(P\subseteq P'\), truth under the first valuation implies truth under the second. The polynomial-space bound is for each fixed \(k\); no uniform polynomial exponent as \(k\) varies is claimed.

## Proof

### Membership in \(\mathrm{PSPACE}\)

Given \(\varphi\), introduce a fresh unary predicate \(Q\) and form

\[
\eta_\varphi := \forall x\,(P(x)\to Q(x))\;\land\;\varphi[P]\;\land\;\neg\varphi[Q],
\]

where \(\varphi[Q]\) is obtained by replacing the designated predicate \(P\) by \(Q\). The sentence \(\eta_\varphi\) is satisfiable exactly when \(\varphi\) is not monotone in \(P\). Its signature has \(k+1\) unary predicates, still a fixed number.

Let \(q\) be the quantifier rank of \(\eta_\varphi\). With \(k+1\) unary predicates there are \(m=2^{k+1}\) exact unary types. The standard rank-\(q\) type characterization for monadic logic with the infinity quantifier says that, for each type, two structures of the same rank-\(q\) theory have either the same cardinality below \(q\), both have finite cardinality at least \(q\), or both have infinite cardinality. Thus there are at most \((q+2)^m\) rank-\(q\) type-count vectors. For fixed \(k\), this is polynomial in the input length.

Enumerate these vectors and evaluate \(\eta_\varphi\) on a canonical representative of each. This evaluation uses polynomial space: at any point a depth-first evaluation stores at most \(q\) active variable assignments, their unary types and equality pattern, and the type-cell counts truncated at \(q\). Ordinary quantifiers need only consider previously assigned elements and one fresh representative of each type with an available element. For \(\exists^\infty\), it suffices to test a fresh representative of each infinite type cell, because all fresh elements of a fixed type are interchangeable by permutations fixing the assigned elements; \(\forall^\infty\) is handled dually. Finite type cells contribute only finitely many exceptions. The recursion and the vector counter therefore require polynomial space. Satisfiability of \(\eta_\varphi\), and hence monotonicity of \(\varphi\), is in \(\mathrm{PSPACE}\).

### \(\mathrm{PSPACE}\)-hardness with one predicate

Reduce from true quantified Boolean formula (TQBF), which is \(\mathrm{PSPACE}\)-complete. Let

\[
F=Q_1p_1\cdots Q_np_n\,\theta(p_1,\ldots,p_n)
\]

be a closed quantified Boolean formula. Use a single unary predicate \(P\), and let

\[
\chi_P:=\exists a\exists b\bigl(a\ne b\land P(a)\land\neg P(b)\land\forall z\,(z=a\lor z=b)\bigr).
\]

This forces the domain to have exactly two elements, exactly one of which satisfies \(P\). Replace each Boolean variable \(p_i\) in \(\theta\) by \(P(x_i)\), and replace each Boolean quantifier \(Q_i\) by the corresponding first-order quantifier over \(x_i\); call the resulting sentence \(F_P\). Put \(\psi_F:=\chi_P\land F_P\). On any model of \(\chi_P\), the two domain elements encode the Boolean values, so \(\psi_F\) is satisfiable exactly when \(F\) is true. If \(F\) is true, expanding \(P\) to the whole two-element domain makes \(\chi_P\) false, witnessing non-monotonicity. If \(F\) is false, \(\psi_F\) is unsatisfiable and therefore monotone. Applying this construction to the Boolean negation of the input QBF gives a polynomial-time reduction from TQBF to monotonicity. The construction has polynomial size and uses no infinity quantifier. Hardness follows for one predicate, and therefore for every fixed \(k\ge1\).

## Verification

The membership reduction preserves the exact semantics of monotonicity: \(\eta_\varphi\) asserts an inclusion between two interpretations on the same domain and a truth-value change from true to false. The type-count argument separates finite counts below rank \(q\), larger finite counts, and infinite counts; these are precisely the distinctions required by the rank-\(q\) equivalence theorem for this language. The symbolic evaluator treats infinitely many witnesses separately from arbitrarily large finite witness sets. The lower-bound construction forces a two-element domain and translates Boolean quantifiers directly, so it does not rely on finite experiments or an enumeration as proof.

## Relationship to prior work

Carreiro, Facchini, Venema and Zanasi establish effective normal forms and decidability of monotonicity for monadic first-order logic with the infinity quantifier. Their rank-\(q\) characterization distinguishes exact type counts below \(q\), finite counts at least \(q\), and infinite type cells. The published paper explicitly leaves computational-complexity questions unexplored. The result here adds a fixed-vocabulary complexity classification: polynomially many rank-\(q\) type-count vectors give the polynomial-space upper bound, while the two-element encoding gives the lower bound. Results for an input-unbounded vocabulary concern a different complexity regime and do not supply this fixed-vocabulary classification.

## Limitations

The result fixes \(k\) before the input is supplied. It gives no uniform polynomial exponent in \(k\), no exact running-time bound within \(\mathrm{PSPACE}\), and no classification for languages with binary predicates, function symbols, or other generalized quantifiers. The literature search did not exhaust every possible synonym or unpublished source; the closest inspected source establishes decidability, not the stated complexity classification.

## References

1. F. Carreiro, A. Facchini, Y. Venema and F. Zanasi, “Model Theory of Monadic Predicate Logic with the Infinity Quantifier,” arXiv:1809.03262 (first public version 2018-09-10); later published in *Archive for Mathematical Logic* 61 (2022), 465–502, DOI: 10.1007/s00153-021-00797-0.
2. C. H. Papadimitriou, *Computational Complexity*, Addison-Wesley, 1994, Theorem 4.11 (TQBF is \(\mathrm{PSPACE}\)-complete).
