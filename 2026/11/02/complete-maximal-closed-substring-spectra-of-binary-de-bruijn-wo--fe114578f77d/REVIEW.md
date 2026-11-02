# Scientific review: complete maximal-closed-substring spectra of binary de Bruijn words through order five

## Correctness — PASS

The domain consists of all binary cyclic de Bruijn words of orders one through five, each cut uniquely at its all-zero order-length window and extended by its initial order-minus-one symbols. The Euler-tour enumeration starts from the uniquely rooted all-zero edge, exhausts every permitted next bit without repeating an edge, and verifies the full cyclic window set at every leaf. Its counts agree with the classical de Bruijn cycle formula and its outputs are deduplicated. The maximal-closed-substring statistic is independently recomputed for every word by (a) direct examination of every possible border of every substring and both one-character extensions, and (b) a record-longest-common-prefix characterization with separate length-one handling. Both methods agree on **every endpoint pair** of every enumerated string. The exact order-five histogram sums to 2048; both extrema and the weighted mean are checked. The standalone program is the finite certificate, not a statistical experiment.

## Originality — PASS, subject to stated priority risk

The closest primary literature is Shibata et al., arXiv:2607.00612, which develops online algorithms for finding maximal closed substrings, and Umezaki et al., arXiv:2607.02838, which develops run-length-encoded enumeration. Kosolobov, arXiv:2410.00209, establishes general \(O(n\log n)\) and expected \(\Omega(n\log n)\) counting bounds for an equivalent closed-repeat representation. These definitions, algorithms and asymptotic theorems do **not** specify the 2048-element de Bruijn histogram. De Bruijn-cycle enumeration fixes the 2048 input objects but does not determine their different maximal-closed-substring counts. Searches under maximal closed substrings, maximal closed repeats, de Bruijn cycles, exact histograms, and the aliases were compared. The closest separate closed-factor census counts *distinct closed factors* of unrestricted short binary words, not *maximal closed substring occurrences* of the canonical de Bruijn family. No covering calculation was found in the inspected literature or available records. Priority remains uncertain if an unindexed dataset or supplementary computation contains the same census.

## Value — PASS

The output count of maximal closed substrings is a natural input-dependent parameter of modern string-enumeration algorithms, and de Bruijn words constitute a canonical maximally factor-diverse input class. The complete first-five-order census, especially its full 2048-word order-five distribution, supplies exact extrema and occurrence multiplicities instead of a single illustrative sequence. Despite identical length and universal five-window coverage, output counts range continuously from 40 to 54, a 35% increase from minimum to maximum. The order-five cutoff is a natural exhaustive one: the standard family has 2048 cycles there but 67,108,864 at the next order. This is a substantive finite classification, not a general theorem for higher orders.

## Limitations and evidence

The statistic depends on the canonical linear cut of each cyclic word. No asymptotic law, larger-order extremum, or cyclic-cut-independent MCS statistic is asserted. Exact finite verification does not supply a formula for all orders. Independent external validation and exhaustive publication-priority confirmation have not occurred.

Self-review: passed. Independent audit: not yet performed.
