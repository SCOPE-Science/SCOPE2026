# Review

## Correctness

PASS. The lower-bound construction of Pshenitsyn fixes five agents and five propositions before any arithmetic translation. Its auxiliary formulas use at most \(XX\); set membership uses \(XXp_b\); successor, addition, and multiplication use a single \(X\); and arbitrary second-order formulas are translated only by strategy quantifiers and Boolean composition of those atoms. Prenexing does not create temporal operators, and the injectivizing tautological padding has depth zero. Hence the source's one-one reduction lands in the depth-two fixed-vocabulary fragment.

The source's injective upper translation from Strategy Logic satisfiability to true second-order arithmetic restricts to the fragment. One-one reductions therefore hold in both directions, so Myhill's theorem gives computable isomorphism.

## Originality

PASS. The primary theorem is stated for the full next-time Boolean-goal fragment. The checked source does not state a temporal-depth restriction, and targeted searches did not locate a depth-two or fixed-vocabulary version. Although the proof explicitly fixes the vocabulary and visibly uses only \(X\) and \(XX\), extracting both restrictions and closing the upper-reduction/Myhill argument gives a sharper complexity statement than the published theorem.

## Value

PASS. Strategy Logic has a sharp contrast between decidable one-goal fragments and the fully second-order-hard Boolean-goal fragment. Temporal depth is a standard structural resource in temporal and modal logics. Showing that depth two already suffices, with no growth in agent or proposition vocabulary, isolates strategy quantification rather than temporal reach or vocabulary size as the source of the extreme satisfiability complexity. It also identifies depth one as a natural remaining boundary.

## Closest literature and limitations

Pshenitsyn (2026) is the direct source and contains all semantic ingredients. Mogavero--Murano--Perelli--Vardi (2017) is the principal earlier satisfiability reference, and Laroussinie--Markey (2013) shows that bounding available actions changes the picture.

The theorem does not prove depth-two optimality or a lower agent/proposition bound.

Same-model review: passed. Independent audit: not yet performed.
