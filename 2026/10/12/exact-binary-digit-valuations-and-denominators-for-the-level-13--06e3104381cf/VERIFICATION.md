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

# Exact arithmetic verification

The included `verify.py` is standalone and uses only Python's standard library. It generates the level-13 four-term sequence from the published recurrence using integer arithmetic and enforces exact division at each step. It compares the first eleven terms with Cooper's displayed sequence. It independently forms the first seven coefficients of the square of the rational power series \(\sum_{n\ge0}S_nX^n/4^n\) and verifies the published integral coefficients \(1,3,25,195,1729,16107,156481\) using exact fractions. For every index \(1\le n\le350\), it checks the valuation identity, the two-extra-powers Catalan congruence, and the valuation of the Catalan-leading term.

Run with `python3 verify.py`; the captured reproducible output is `verification_output.txt`. A successful run is finite corroboration only; the all-index result relies on the proved binomial valuation comparison and the original level-13 square identity. No independent scientific audit is claimed.
