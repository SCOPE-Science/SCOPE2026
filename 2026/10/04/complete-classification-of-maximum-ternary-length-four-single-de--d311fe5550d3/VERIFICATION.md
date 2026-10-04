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
# Verification

The finite object is the compatibility graph on all \(81\) words in \(\{0,1,2\}^4\), where two words are adjacent exactly when their distinct one-deletion shadows are disjoint. `artifacts/verify.py` reconstructs this graph from the deletion definition rather than loading a precomputed adjacency table.

The target-size enumerator is exhaustive. It maintains candidates in increasing word order; choosing a word removes all earlier choices permanently and intersects the remaining candidates with its compatibility neighborhood. A branch is pruned only if the number of candidates left is smaller than the number of words still required. Therefore every target-size compatible subset is visited exactly once.

Replay with `python3 artifacts/verify.py` produces:

`VERIFY_OK maximum=11 labeled_maxima=6 orbits=1 orbit_size=6 stabilizer=2 nodes11=668442 nodes12=485745`

The verifier checks all six embedded maximum codes, verifies that no size-
\(12\) code exists, confirms the common nine-word core, reconstructs the six-cycle on the remaining six words from deletion-shadow compatibility, and traverses all \(12\) global-symbol/reversal symmetries. It also verifies that every maximum code has deletion-shadow union size \(23\).

Limits: this is a finite exhaustive proof for ternary length four only. It does not establish any asymptotic statement or general classification for odd alphabet sizes. The independent-audit channel has not been performed.
