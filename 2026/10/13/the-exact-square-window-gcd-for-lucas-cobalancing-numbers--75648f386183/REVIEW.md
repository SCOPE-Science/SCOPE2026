# Scientific review: the Lucas-cobalancing square-window GCD

## Correctness — PASS
For every positive window length, the proof identifies the exact moving-window sum and computes the GCD of all adjacent differences by Pell strong divisibility. The resulting two-integer GCD has all odd-prime valuations determined by reduction modulo powers of each prime. The prime-three exception is proved from the index parity, and a separate duplication/congruence argument settles all powers of two, including arbitrarily large even window lengths. The proof therefore covers every index without relying on finite enumeration. Exact-arithmetic finite checking independently corroborated the formulas through window length 320.

## Originality — PASS relative to checked sources
The closest source, Mbirika--Schrader--Spilker, arXiv:2301.05758, Section 6.1, Question 30, explicitly lists the Lucas-cobalancing square-window problem as open and reports only computational evidence for a factor-three anomaly. Its Partial Result 29 gives the Pell and associated Pell square-window formulas, which do not supply the odd-index associated-Pell subsequence's GCD. Mbirika--Spilker, arXiv:2204.12626, proves results for recurrence coefficient one, not for Lucas-cobalancing. Prior work identifying squared Lucas-balancing windows does not itself imply the asserted formula for squared Lucas-cobalancing windows without a proved cross-sequence relation. Searches of semantic research records and published literature did not identify an equivalent or dominating theorem. Unindexed equivalents remain possible.

## Value — PASS
This determines a natural, previously posed exact invariant for the entire Lucas-cobalancing family and proves the observed isolated prime-three defect. The determination applies to infinitely many window lengths and turns the published numerical observation into a theorem, with a direct valuation mechanism. It does not solve the separate problem of simplifying the index GCD \(\gcd(B_k,k)\) or the other sequence families of Question 30.

## Limits and evidence
Evidence consists of the unrestricted proof in `RESULT.md` and reproducible integer checks in `verify.py` with the recorded results in `verification_output.txt`. Checked primary papers are identified in the references of `RESULT.md`. Novelty remains conditional on available indexed literature; independent mathematical review has not been carried out.

Self-review: passed. Independent audit: not yet performed.
