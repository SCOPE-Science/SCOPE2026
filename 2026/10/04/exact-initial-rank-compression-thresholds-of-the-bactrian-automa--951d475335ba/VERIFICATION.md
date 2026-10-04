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

The proof is symbolic and does not depend on finite enumeration. The included `verify.py` provides two independent stress tests of the stated formulas: exact power-automaton breadth-first search for every odd \(n\) from \(5\) through \(17\), and direct replay of the explicit witnesses for every odd \(n\) from \(5\) through \(101\) whenever the target lies in the proved half-range.

The BFS computes shortest distances from the full state set to every reachable subset and then minimizes over all subsets of size at most the target rank. It checks every claimed \(\lambda_n(s)\) in the theorem's domain. The witness replay checks exact achieved deficiency and word length. Successful execution prints `VERIFY_OK`.

Limit: finite verification cannot establish the infinite theorem and is not used as a substitute for the proof in `RESULT.md`.
