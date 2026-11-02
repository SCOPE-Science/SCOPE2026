# Self-review

## Correctness — PASS

The statement has global quantifiers: all integer weights, all moduli at least two, all indices, and exact **least** eventual periods. The proof derives the binomial identity, calculates prime-power shift divisibility, proves odd-prime minimality from the recurrence, isolates the unique lowest dyadic term for weights divisible by four, and accounts for the two-term cancellation at weights congruent to two modulo four. The odd-weight induction identifies the exact last nonzero binary residue. Chinese remaindering preserves exact minima. The standard-library verifier checks 12,691 weight/modulus pairs, 28,800 shift comparisons and 252 dyadic layers. The computation is corroboration, not an infinite proof.

## Originality — PASS with historical-priority risk

Kim and Kim's Theorems 6.2–6.3 **already contain the entire unweighted eventual-period result**. Bednarz and Wołowiec-Musiał's Theorems 8 and 10 already contain broad weighted congruences and cover the basic odd-shift upper-bound mechanism. Kallat's universal shift theorem is still more general but not an explicit least-period classification. The assessed new content is the **parameter-dependent exact dyadic least periods for even weights**, notably the change at \(\nu_2(c)=1\) versus \(\nu_2(c)\ge2\), together with its exact shift valuation and assembly at composite moduli. No inspected prior result was found to state or imply those exact minima solely from its published assertions. Historical coverage may be incomplete, particularly for specialized Hermite/matching polynomial congruences.

## Mathematical value — PASS

Least periods and sharp preperiods of combinatorially defined integer sequences are natural arithmetic invariants, and this parameter phase diagram settles the modular dynamics for an infinite family. The cancellation at \(c\equiv2\pmod4\) forces different growth of the minimal dyadic period from the \(4\mid c\) case, not merely a reparameterized unweighted result. The exact shift valuation also gives uniform divisibility information at every index, independently of the period formula. No paper-scale or downstream theorem is claimed.

## Scientific and historical limitations

The self-review does not certify absolute literature priority or independent validity. Known \(c=1\) conclusions and established general shift congruences are explicitly excluded from the asserted new contribution. It does not classify unrelated recurrences or residue frequencies.

Self-review: passed. Independent audit: not yet performed.
