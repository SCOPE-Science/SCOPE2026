# Scientific review

## Correctness — PASS
For each original constant run, the number of symbols sent to one track completely determines the two scattered subsequences. Fixing one of three allocation states per run determines both output run-symbol sequences. If they match, equality of corresponding lengths gives one equation per output run, with each undecided quantity present in exactly two incidences (a loop if both occur in the same equation). This is precisely an integer capacitated exact-degree matching system. Both directions of the equivalence and the \(3^r\) bound are proved. The public checker verifies 5,327 independent finite words and a large-compressed example; known polynomial b-matching algorithms provide the infinite running-time guarantee.

## Originality — PASS, with residual risk
The focal 2023 shuffle-square paper and the 2025 graph characterization are inspected primary sources. The latter may already imply FPT in run count by a more general, larger graph encoding, so unqualified FPT alone is not presented as new. The precise contribution is a simple per-run three-state decomposition into *at most* \(3^r\) exact-degree instances with at most \(r\) edges, including bit-compressed lengths. Literature and published-record comparisons did not identify an equivalent single-exponential compact formulation. The principal residual risk is an unindexed parameterized recognition algorithm or an implicit reduction hidden in other graph formulations; novelty is therefore not absolute.

## Mathematical value — PASS
Binary shuffle-square recognition is NP-complete in general, whereas few-run inputs arise naturally from run-length compression. This explicit single-exponential algorithm and small exact-degree formulation establish structural tractability for *arbitrarily large* runs without expanding the word, strengthen what a mere list of low-run classifications can provide, and extend to arbitrary finite alphabets. The result is an algorithmic upper bound, not an optimality theorem.

## Limits and nearest sources
Grytczuk–Pawlik–Pleszczyński (2023, arXiv:2308.13882) supplies the core problem and MSC. Grytczuk–Pawlik–Ruciński (2025, arXiv:2503.22043) supplies a general nest-free graph characterization and classifies short-run families. Letchford–Reinelt–Theis (2008) and Gabow–Sankowski (2021) supply polynomial b-matching methods. No new matching solver is claimed. The certificate tests the reduction but does not itself implement a polynomial blossom algorithm.

Self-review: passed. Independent audit: not yet performed.
