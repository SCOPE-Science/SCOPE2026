# Review: One comparability can increase one-point type counts

## Correctness — PASS

The ideal/filter representation follows from transitivity and exactly encodes extensions over fixed parameters. The three-case classification of a complete two-level poset yields \(2^{a+b}+2^a+2^b-2\). The comparison with one deleted incidence is exact: restoring the incidence admits \(2^{a+b-2}\) new ternary assignments and forbids exactly two old ones, proving the all-size jump. An independent transitive-closure implementation exhausts all partial orders and feasible relation additions on at most four old points, yielding no increases through three and six comparison orbits at four. The separate finite checks of the closed forms are supporting evidence, not substitutes for the symbolic proof.

## Originality — PASS, with explicit risks

Dolinka–Mašulović (2010 preprint / 2012 journal), Lemma 4.3, already describes inserted points by sets of parameters below and above them. The accessible full `RESULT.md` of *Finite-parameter 1-type counting in the random poset is #P-complete* already gives the counting invariant, the model-theoretic identification, and a complexity classification. Neither inspected result provides the change under adjoining one comparability. The claim is the exact nonmonotone jump, its sharp four-point threshold, and the first failure census—not the pre-existing extension encoding, count-complexity result, or characterization of the random poset. Oliver Pretzel (1980) studies insertion positions and is a particularly relevant priority risk; only its abstract concerning their **dimension** was accessible. Its full text was not checked, so originality is conditional on this specific unresolved source comparison, though no available evidence gives a dominating result. Searches and full-text comparisons cannot prove first discovery.

## Value — PASS

Adding order relations might be expected to restrict available one-point extensions. The result shows the opposite behavior, and the gain \(2^{n-2}-2\) is unbounded and exponential while changing only one relation in a natural height-two family. The first size and complete first failure layer make this a motivated sharp boundary for orbit/type counting, not an isolated arbitrary numerical curiosity. The exact formula identifies the competing mechanisms behind the jump (new interval placements versus lost boundary placements), useful for analyzing parameter changes in Fraïssé limits and for testing counting algorithms.

## Scope and limitations

The infinite formula concerns near-complete height-two orders. The complete classification of increases concerns four old points only. It does not classify arbitrary large-poset edge additions. Pretzel's uninspected full text and unindexed older insertion-position calculations remain originality risks. Source evidence is not an independent review.

Self-review: passed. Independent audit: not yet performed.
