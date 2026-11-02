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

# Reproducibility and scope
The accompanying `verify.py` is a standalone finite check requiring Python 3 and SymPy. Execute `python verify.py`; its expected terminal line is `VERIFY_OK`. It computes Jacobian and Tjurina quotient lengths by lexicographic Gröbner bases after adjoining sufficiently large powers of both variables, for characteristics 5, 7, 11, 13 and parameters 0, 1, 2; and exact Frobenius quotient powers at exponents 1 and 2.

These checked instances are not exhaustive over primes, parameters or Frobenius levels; the proof's Newton/regular-sequence and induction steps supply the general statements. The local quotient computations explicitly impose powers of both coordinates to avoid counting unrelated critical points. No formal proof assistant or independent audit is claimed.
