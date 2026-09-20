# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The construction was checked at the level of the exact structure,
extension bifunctor, ideal orthogonality, object-ideal factorization, ideal
approximations, and object-level obstruction.

The key structural point is that the finite quotient \(G=K_0(\mathcal S)/H\)
supplies exactly the finite multiplicities needed in the Ren--Wang doubling
argument. If a truncation has quotient class of order \(m\), taking \(m\) copies
moves it into \(\mathcal A_H\). This proves both the object-ideal factorizations
and the explicit special ideal approximations. The Ext formula over a semisimple
category gives the orthogonality equalities, with simple stalk complexes of
multiplicity equal to the order of a simple class in \(G\) detecting any
forbidden nonzero cohomology map.

For object approximations, the long exact cohomology sequence forces the middle
object to have precisely the relevant lower or upper truncated cohomology. This
gives necessity of \(\delta_-=0\) and \(\delta_+=0\); the ordinary cone
constructions with multiplicity one prove sufficiency. The three-degree
realization
\[
S^0(L)\oplus S^1(M)\oplus S^2(W)
\]
was checked to have total Euler class zero modulo \(H\) and arbitrary prescribed
defect pair \((g,h)\). The idempotent-completion statement follows because every
quotient class has finite order, so every complex is a summand of a finite direct
sum belonging to \(\mathcal A_H\).

No computational verification is needed for these symbolic arguments.

## Originality

**PASS, to the best of our knowledge.** The result is a genuine strengthening
and conceptual reorganization of a very recent construction, but several major
ingredients are prior art and are not claimed as new.

Ren--Wang (arXiv:2609.18681v1) proves the parity case \(K_0\cong\mathbb Z\),
\(H=2\mathbb Z\), including the Frobenius structure, Ext calculation, complete
ideal cotorsion pair, and parity obstruction to special object approximations.
Their full text was inspected. Searches of that text for Grothendieck-group,
finite-index, and general quotient formulations did not locate such a statement.

Thomason's dense-subcategory theorem and Matsui's exact-category extension make
the \(K_0\)-subgroup/density viewpoint standard prior art. Matsui's Theorem 2.8
was inspected and explicitly identifies dense resolving/coresolving
subcategories with suitable subgroups of \(K_0\). Accordingly, no novelty is
claimed for the bare fact that subgroup conditions on Grothendieck classes define
dense subcategories or for the resulting idempotent-completion phenomenon.

Targeted searches using combinations of “ideal cotorsion pair”, “Grothendieck
group”, “finite-index subgroup”, “Euler characteristic”, “dense subcategory”,
“object cotorsion”, “finite abelian group”, and quotient/congruence terminology
did not locate a prior theorem giving the quotient-valued obstruction,
the exact special-approximation criteria, the full \(G\times G\) defect spectrum,
or realization of arbitrary finite abelian defect groups.

The principal residual originality risk is the foundational paper Fu--Guil
Asensio--Herzog--Torrecillas, *Ideal approximation theory* (Adv. Math. 244
(2013), 750--790, DOI 10.1016/j.aim.2013.05.020). Its abstract and the
Theorem 28 / Question 29 statements as quoted in later literature were inspected,
but the full article text was not independently inspected. This matters because
it is the most plausible older source for a general ideal-theoretic formulation.
The much more recent Frobenius ideal-approximation papers were also searched at
the title/abstract and theorem-context level; no Grothendieck-quotient mechanism
was found. Because the Ren--Wang source is itself very recent, independent
concurrent observation or a later revision remains a further residual risk.

## Value

**PASS.** The result turns a binary parity counterexample into a classification
mechanism. It identifies a finite abelian group that measures the failure of
object completeness, gives necessary and sufficient criteria for each individual
special object approximation, realizes every possible pair of defects, and shows
that arbitrary finite abelian groups occur. This separates the established
\(K_0\)-density phenomenon from a new approximation-theoretic consequence and
provides a reusable family of controlled counterexamples to object completeness.

## Scope and limitations

The proof depends essentially on semisimplicity and on finiteness of
\(K_0(\mathcal S)/H\). No claim is made for nonsemisimple hearts, infinite-index
subgroups, arbitrary dense exact subcategories, or ordinary nonspecial
precover/preenvelope existence. The review is not independent validation, formal
verification, or peer review.
