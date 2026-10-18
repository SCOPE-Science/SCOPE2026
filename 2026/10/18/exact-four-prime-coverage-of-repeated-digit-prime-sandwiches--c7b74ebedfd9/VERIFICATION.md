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

# Verification instructions and limits

The attached `check.py` requires only Python 3 and the standard library. Execute `python3 check.py` from a directory containing the extracted file. It tests all \(6\cdot3003\cdot24\) local residue/position combinations and separately builds a Chinese-remainder/bitmask enumeration. It asserts the complete residue table with cardinalities \(273,1,273,3,273,1\), the three non-\(11\) odd-length classes, and the necessity of each of the four primes for the \(231\) certificate. Assertions are decisive and no randomization or floating-point calculations occur.

The general proof relies on periodicity modulo the four primes; the check alone does not prove this symbolic step. Likewise, the density formulas are proved by geometric-series counting, not by a finite numerical sample. No implication is claimed for cores that fail the specified covering test. An independent audit has not been performed.
