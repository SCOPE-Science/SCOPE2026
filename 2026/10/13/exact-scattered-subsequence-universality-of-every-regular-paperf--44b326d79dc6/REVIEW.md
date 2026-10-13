# Scientific review: exact paperfolding-prefix subsequence universality

## Correctness — PASS

The alphabet, index convention, and subsequence quantifier are fixed explicitly. Greedy arch count equals finite-word subsequence universality by the standard earliest-embedding argument. The odd-part definition proves the eight-symbol block identity for every block index. All eight combinations of incoming one-letter rest flag, block parity, and final bit give the symbolic increment \(3+q-z\) and outgoing flag \(z\). All sixty-four initial-fragment cases give the claimed residue formula. The resulting telescoping sum proves the all-prefix identity, and a recurrence for paperfolding-one counts proves the limiting frequencies. The standalone checker confirms symbolic transition tables and independent finite instances, but the all-prefix proof does not rely on extrapolating them. The exact independent-subsequence predicate was checked for lengths through \(29\).

## Originality — PASS

The full primary text of Schnoebelen and Veron (arXiv:2304.11932v1) was examined in relevant sections for arch factorization, finite-word signatures, and compressed-word algorithms; its paperfolding scope was also checked. It establishes general arch techniques rather than the explicit regular-paperfolding index. Adamson et al. (arXiv:2311.10658v1) treat universality of regular languages, not the all-prefix numerical invariant for one infinite word. The earlier Barker et al. source (arXiv:2003.04629v1) supplies the universal-arch characterization and receives credit for it. Published-source searches included paperfolding, fold sequence, scattered subword/subsequence, greedy arches, exact residue formulas, and the specific \(3/8\) density; no equivalent formula was found. Related results concerning other automatic words or the distribution over all binary finite words do not imply the paperfolding-specific formula. A previously published unindexed paperfolding derivation remains possible and is the principal residual risk; search failure is not a proof of uniqueness.

## Mathematical value — PASS

The result is a complete, explicit evaluation of a natural formal-language invariant on **every prefix** of the canonical regular paperfolding sequence, not an arbitrary finite slice. It supplies a sharp global discrepancy bound, an exact dyadic law, and an unusually rigid limiting ten-value deviation distribution. Existing arch algorithms compute the index from finite words or their compressed representations but do not deliver these structural constants and closed forms. The problem and result are self-contained in combinatorics on words and formal-language theory. No claim of independent certification, a general theorem for other paperfolding codings, or a classification of arbitrary factors is made.

## Limits and relevant evidence

The computation in `verify.py` is finite and supports, rather than replaces, the universal block argument. Source comparisons are restricted to the inspected primary texts and actual published-result searches. A potentially equivalent unindexed special-sequence calculation cannot be categorically excluded. The verified source date used for this work is the first arXiv posting of the main 2023 arch-algorithm source (2023-04-24); the older 2020 arch-characterization paper is credited as background.

Self-review: passed. Independent audit: not yet performed.
