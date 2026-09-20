# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For the explicit family on \(k[x]\), the filtration axioms reduce to superadditivity of
\[
f_\lambda(n)=n+\lfloor e^{\lambda n}-1\rfloor.
\]
This follows from
\[
(e^{\lambda n}-1)(e^{\lambda m}-1)\ge0
\]
and the elementary floor inequality. The successive quotient dimension is exactly \(f_\lambda(n)-f_\lambda(n-1)\), which is squeezed between \((e^\lambda-1)e^{\lambda(n-1)}\) and that quantity plus \(2\). Its logarithmic rate is therefore exactly \(\lambda\). The \(e^{n^2}\) variant is likewise superadditive and gives infinite entropy. The usual degree filtration gives zero entropy.

These calculations were checked against Definition 2.7 and Definition 2.10 of arXiv:2609.18144v1. Since \(k[x]\) has intrinsic linear growth and GK dimension \(1\), the example directly contradicts the unrestricted statements of Theorem 3.7, Remark 3.8, Theorem 3.9, Theorem 3.14 and Corollary 3.15 as written.

The quantifier repair was checked in both directions. If an affine algebra has exponential intrinsic growth, any finite-dimensional filtration contains a fixed finite generating space at some finite filtration level. Zero entropy would then force all cumulative filtration dimensions to have arbitrarily small exponential rate, contradicting the exponential lower bound on the standard growth function. Conversely, positive entropy for every finite-dimensional filtration includes a standard filtration; submultiplicativity of its cumulative dimensions turns positive limsup layer entropy into a positive exponential rate, yielding exponential growth.

The linear-control repair follows by the same comparison with a standard filtration. No computational experiment is used as evidence for the general statements.

## Originality

PASS, to the best of our knowledge.

The current full text of arXiv:2609.18144v1 was inspected at Definitions 2.7 and 2.10, Theorem 3.7, Remark 3.8, Theorems 3.9, 3.13 and 3.14, Corollary 3.15, and Proposition 3.17. The paper states the unrestricted finite-dimensional-filtration implications corrected here. Its arXiv submission history currently lists only v1, submitted 16 September 2026.

The 2024 Results in Mathematics paper defining this entropy was inspected at Proposition 3.2, Remark 3.3 and Proposition 3.4. It already establishes strong filtration dependence under linear reindexing and explicitly suggests, without proving, that zero entropy for one filtration might imply zero entropy for every filtration. The \(k[x]\) family here disproves that suggestion and realizes the full extended nonnegative entropy spectrum.

Classical filtered-GK theory is prior art. Accessible later sources citing Krause--Lenagan Proposition 6.6 state a finite-generation condition on the associated graded algebra. The primary Krause--Lenagan book statement was not independently inspected, so no novelty is claimed for identifying the general need for filtered-graded hypotheses.

Searches using exact and synonymous formulations for positive filtered entropy on \(k[x]\), arbitrary prescribed entropy of polynomial algebras, nonlinear/superadditive filtration reindexing, and corrections to arXiv:2609.18144 did not locate the spectrum construction or the quantifier theorem. Because the counterexample is elementary once arbitrary filtrations are considered, rediscovery or an older equivalent observation under different filtration terminology remains a material residual risk.

## Value

PASS.

The finding gives a one-variable commutative counterexample to several central growth-detection statements of a current preprint, identifies the omitted associated-graded finiteness issue, and replaces the false one-filtration criterion by a sharp universal-quantifier characterization. The full entropy spectrum \([0,\infty]\) on \(k[x]\) also sharply demonstrates how much information can be introduced solely by accelerating the filtration index.

## Limitations

The correction concerns the specific filtration entropy of Bock et al. and Schwarz--Sebandal. Results for standard or natural filtrations are not contradicted. No claim is made that the later Leavitt-path-algebra PI criterion fails. The primary text of Krause--Lenagan Proposition 6.6 was not independently inspected, although accessible later sources quote it with finite generation of the associated graded algebra. Same-model review is not independent validation, formal verification, or peer review.
