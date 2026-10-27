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

# Reproducibility

Run `python3 check_alltop.py` with a Python 3 standard library. It independently evaluates 23,570 finite self-ambiguity sums and the predicted exact Gauss-sum expression, checks all arithmetic candidate cancellation conditions for ten primes, and checks a genuine resonance at the positive real amplitude in length 17. Tolerance in complex floating comparisons is `2e-9`. This is not an infinite proof or an independent audit.

The complete prime-uniform argument is the quadratic Gauss-sum identity and modular phase cancellation in RESULT.md. The finite search for the length-5 and length-13 exceptions is exhaustive only for those finite primes. No outside packages, downloaded source papers, remote services, or existing files are needed to rerun the checker.
