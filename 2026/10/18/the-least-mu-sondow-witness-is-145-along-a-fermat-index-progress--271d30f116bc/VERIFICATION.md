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

## Direct verification
The standalone standard-library program `verify.py` was executed from the extracted package and returned `CERTIFICATE_PASS` with exactly 58 odd-squarefree candidates, 33 selected prime blockers, and maximum prime orbit length 52. For each candidate, it trial-factors the integer and checks all forward states of the modular recurrence `x -> x**8 mod p` until the first repeated state; no target `-m/p mod p` is present for its selected prime. The program also checks the exact uniform fixed point at 145 and separately performs diagnostic direct prime-power tests for indices 3 through 24 in steps of three.

## Mathematical boundaries
An infinite family cannot be validated by finitely many tested indices. The infinite quantifier is proved symbolically: for j=3r, the parameter residue modulo p equals the r-th recurrence state, so each complete finite orbit rules out every r. The finite bound 144 is exhaustive because every smaller candidate is checked or excluded by a valuation argument. No claims about absolute originality or independent mathematical certification are made.
