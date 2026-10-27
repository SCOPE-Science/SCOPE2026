# Scientific review

## Correctness: PASS

The proof derives all projected ballot types by analyzing equality in the published pointwise harmonic inequality, not by assuming a construction is exhaustive. Equality in the total score comparison forces disjoint committees, equality for every voter, and zero gain in every exchange. The independent integer linear system for those exchanges forces column-constant pair multiplicities and singleton counts \(b_t=S-(k+1)d_t/2\). Integer divisibility and positivity establish the parity-sensitive sharp electorate minimum; explicit constructions attain it. Exact-rational finite tests corroborate the algebra but are not an infinite proof.

## Originality: PASS (subject to historical-priority uncertainty)

The 2026 primary paper proves the harmonic lemma, exhibits one dense tight instance, and derives an asymptotic approximation. These are **prior results**, not new claims here. A full reading of its local-PAV result, proof of Lemma 3.2, and counterexample appendix found no classification of all equality ballots or minimum voter size. The 2024 local-search paper addresses convergence complexity instead of equality rigidity. Published-record searches for exact worst-case electorates and sparse equality profiles produced no implication-equivalent result; such searches cannot prove absolute uniqueness.

## Mathematical value: PASS

This is a complete natural extremizer classification for the canonical single-swap PAV efficiency gap. The smallest certificates exhibit a genuinely arithmetic parity effect: odd sizes admit pair multiplicity one, while even sizes require even pair multiplicities. For three seats the extremal gap requires only eight voters rather than the source's 24, making the pathological case transparent and parsimonious. The exact minimal population provides a structural diagnostic for finite instances and a sharp benchmark for algorithm testing; the known ratio itself is not presented as novel.

## Limitations and literature

Only exact one-swap locality, unit-weight voters and positive optimum scores are covered. The unrestricted necessity statement concerns projection to the two comparison committees; the sufficiency statement requires exactly their union as the candidate set. Absolute historical priority is uncertain. Closest primary source: Peters, Vaish and Yadav, arXiv:2609.07554v1, Theorem 3.1, Lemma 3.2 and Appendix B. Additional source: Kraiczy and Elkind, DOI:10.4230/LIPIcs.ESA.2024.82.

Self-review: passed. Independent audit: not yet performed.
