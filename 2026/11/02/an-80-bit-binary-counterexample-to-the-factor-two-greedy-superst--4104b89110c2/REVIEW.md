# Review of the binary length-eighty greedy-superstring witness

## Correctness (C): PASS

The mathematical result is a finite existence statement, not a general all-length conjecture. Seventeen binary codewords have a verifiable common leading marker and no later recurrence, giving exact overlap scaling under substitution. The independently replayed verifier generates all 252 eight-symbol source inputs, checks 251 chosen greedy merges against the true maximum over all ordered live pairs, constructs the Eulerian common superstring, verifies all 63,252 ordered binary input-overlap comparisons, and establishes the optimal binary length by a universal start-spacing lower bound. Thus both 5,190 greedy bits and 2,590 optimal bits are supported by explicit reasoning and exact finite checks. A program execution is not offered as a proof for untested inputs.

## Originality (O): PASS, with residual risk

The length-eight large-alphabet source witness, factor-two disproof and binary alphabet-reduction possibility are all prior work. The particular 80-bit bound, length-ten 17-letter synchronized code and complete binary greedy/optimum certificate were not found in the inspected primary literature or the searched accessible indexed claims. Vassilevska's exhibited general reduction yields 288-bit strings for this 17-letter source, so its quantitative conclusion does not imply the 80-bit parameter. The length-ten code is elementary and alternative unpublished short encodings could have been found already; priority is not independently certified.

## Value (V): PASS

Whether a ubiquitous string-assembly heuristic crosses factor two on binary equal-length inputs is a natural specialized benchmark. A concrete 80-bit witness is substantially smaller than applying the cited general-purpose binary substitution to the currently known 17-letter length-eight obstruction (288-bit inputs). A fully constructive instance with exact optimum, every legal merge checked and no solver dependency makes the failure reproducible and useful for testing implementations. No claim is made that this establishes the sharp smallest length.

## Closest literature and scientific limits

Shibata, arXiv:2609.01365, supplies the original general-alphabet refutation. *The greedy superstring ratio at small string lengths* (2026), Theorem 21, supplies the exact 252-word length-eight source case and 519/259 ratio. Vassilevska (2005), binary-alphabet slides, supplies the prior alphabet-preserving overlap idea. These results motivate the question but none states the specific length-eighty binary certificate. This result depends on a worst-case legal tie-breaking and does not settle the minimum failure length over the binary alphabet.

Self-review: passed. Independent audit: not yet performed.
