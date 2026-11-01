---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof reduces each peripheral edge and the center to three initial integer counts, then uses binomial and multinomial probabilities. The finite enumerator is a separate implementation based directly on a labelled graph adjacency list and synchronous neighbor voting.

Execute `python3 verify.py` with Python 3 and no third-party libraries. It exhaustively checks \(174{,}760\) labelled binary configurations across friendship graphs with \(1\le n\le8\). It verifies fixation after at most two steps; the initial-majority and first-center equality; the eventual-majority and terminal-center equality; the reversal/first-fixation-at-two equivalence; the finite fixed, flip and reversal censuses. An additional \(42\) rational-bias cases for \(1\le n\le7\) verify exact weighted formulas independently of the multinomial summation.

Expected final line of the recorded output: `FRIENDSHIP_MAJORITY_CENSUS_OK`. The tests do not certify all infinite graph sizes or the limiting central limit theorem. Those rely on the written proof. No independent audit has been performed.
