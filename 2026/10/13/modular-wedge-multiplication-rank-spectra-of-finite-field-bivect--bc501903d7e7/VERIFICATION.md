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

# Verification of the finite-field wedge-multiplication rank formula

Run `python3 verify.py` using Python 3.8 or later. The code computes the claimed binomial modular ranks and independently constructs exterior-multiplication matrices with signed wedge products and alternating coefficient matrices for each tested bivector. It checks exhaustion for small fields, coefficient totals, rank monotonicity, and the characteristic-two simplification. A successful run prints `VERIFY_OK_EXTERIOR_WEDGE`.

The verifier makes no claim to prove the all-dimensions statement by enumeration; the proof uses Wilson's integral inclusion-matrix diagonalization, the alternating-form classification, and the paired-generator decomposition.
