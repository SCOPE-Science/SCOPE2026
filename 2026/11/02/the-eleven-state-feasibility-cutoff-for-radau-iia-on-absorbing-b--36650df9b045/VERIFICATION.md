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

# Reproducibility and checks

Run `python3 verify.py` with SymPy available. The verified replay produced `EXACT_VERIFICATION_PASS 1701`. It symbolically checks all rational coefficient and absorbing-column generating-function identities through degree ten, all thirty-six entries of the six-state exact matrix, the six-state quintic bracketing and derivative, and exact full-matrix inversions for selected rational step sizes on chains of lengths two through twelve. At step three, the recurrence's signs were checked exactly using rational numbers. The universal impossibility above eleven states rests on the analytically proved angular inequalities, not on an unbounded computational search. No arbitrary-generator or intermediate-stage positivity has been verified or claimed.
