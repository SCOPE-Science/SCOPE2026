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

# Verification of the rectangular nilpotent-product law

The standalone `verify_rectangular_npp.py` enumerates all matrices and matrix pairs over the prime fields of orders \(2,3,5\) in all fifteen indicated size choices: all \(1\times1\), \(1\times2\), \(2\times1\), \(2\times2\) dimensions over those fields, plus \((m,n)=(2,3),(3,2),(3,3)\) over \(\mathbb F_2\). It computes products entry by entry and determines nilpotence by successive powers up to the matrix dimension. For each fixed left matrix it independently calculates rank via Gaussian elimination and compares the number of successful right matrices with \(q^{mn-r}\). It checks the aggregate exact count and the separate nilpotent-matrix census; successful execution prints `VERIFY_OK`.

Reproduction command: `python3 verify_rectangular_npp.py` using only the Python standard library. The program treats its modulus as prime; the theorem extends to all prime-power fields by the noncomputational finite-field proof. These enumerations are not an exhaustive test of all field orders or dimensions. No external independent audit has been performed.
