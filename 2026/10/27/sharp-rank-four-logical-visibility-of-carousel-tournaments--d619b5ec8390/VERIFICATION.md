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

# Reproduction and verification

Run `python3 verify_carousel.py` in a Python 3 environment, with no third-party packages. It enumerates every tuple extension used by the inductive full first-order quantifier-rank type semantics for each finite carousel tournament of odd size \(1,3,\ldots,19\). Its checks require exactly eight different rank-four types at the representative sizes \(1,3,5,7,9,11,13,15\) and the identical terminal type for sizes \(15,17,19\). An actual run printed `EXACT_SMALL_CASE_CHECK_PASS`.

The program does not and cannot establish the infinite tail from a finite set of tests. That conclusion follows mathematically from the antipodal paired-interval lemma in RESULT.md, using threshold \(T_r=2T_{r-1}+2\). The geometric proof includes all quantifiers, repeated-vertex cases, and alternating-site parity. No independent audit, proof-assistant certification, or external validation has been undertaken.
