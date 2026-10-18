# Scientific review

## Correctness — PASS
The gap decomposition is bijective and yields the occurrence count \(\sum_i\binom{i}{s}\binom{A-i}{t}b_i\) exactly. The inequality \(w_{A,s+j}\ge(j+1)(u-j)\ge u\) proves the finite range of zero counts and the support cutoff, with no unproven combinatorial sublemmas. The maximum support equality cases are exhausted, including the \(k=1\) coincidence and the distinct endpoint cases for \(k\ge2\). The binomial polynomial is handled carefully for negative arguments. Exact enumeration cross-checks 702 small instances; the proof is valid for all positive parameters. Risk: accidental alternative conventions for generalized binomial coefficients; these are explicitly defined in the result.

## Originality — PASS within inspected evidence
The result uses the same underlying frequency statistic as the 2023 Menon–Singh paper and the 2026 Bruda paper. Earlier explicit counts for \(k\le4\) and the general eventual polynomial degree are acknowledged as covered. The new content is a finite coefficient expression for arbitrary positive frequency and, more decisively, the **sharp, uniform stabilization index** \(k+1\) and exact preceding discrepancy. Neither inspected primary text states this theorem, and no covering published statement was found in the searched research index. A differently phrased gap decomposition in unindexed work remains possible; independently verify novelty before external publication.

## Value — PASS
An unspecified 'sufficiently large' in a general polynomiality theorem is sharpened to a minimal universal cutoff depending only on target frequency, not on the potentially much larger outer runs. The exact small-length jump is a structural boundary, and the rational enumerator provides direct exact coefficients for every length and fixed frequency. The natural three-run pattern family is prominent in subsequence-frequency work; this is a substantial uniform refinement rather than a one-off numerical improvement.

## Limitations and closest sources
Menon–Singh, arXiv:2306.07870, gives counts through frequency four. Bruda, arXiv:2607.02578, gives arbitrary-frequency eventual polynomiality and degree bounds. Neither inspects the exact universal onset for this three-run subfamily in its stated results; primary text and available proof sections were compared, not just abstracts. General degree equality for patterns with singleton internal runs is pre-existing and not presented as a novelty. Verification for all parameters remains mathematical, not computational; outside literature may contain an equivalent identity.

Self-review: passed. Independent audit: not yet performed.
