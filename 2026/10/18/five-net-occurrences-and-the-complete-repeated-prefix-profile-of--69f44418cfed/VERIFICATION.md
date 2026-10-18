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
The mathematical proof is given in `RESULT.md`, with all quantifiers and finite-word boundaries. The independent program `check_period_net.py` reconstructs the finite period-doubling iterate directly from the binary morphism; for every order \(3\le n\le14\), it computes a suffix array and adjacent longest-common-prefix array, checks all \(2^n\) positions against the exact five-piece profile, and checks all net starts and lengths. For \(3\le n\le7\), it additionally performs independent quadratic suffix comparisons and direct exhaustive repeated-factor enumeration with boundary-aware left and right extensions.

Run `python3 check_period_net.py` in the directory containing that file. The output is saved in `check_period_net.log` and ends with `ALL CHECKS PASSED: finite independent corroboration n=3..14`. The exhaustive small-order checks do not prove the infinite claim; the all-order induction and net-occurrence lemma supply its proof. No independent external review, proof-assistant certification, or authority-based validation is claimed.
