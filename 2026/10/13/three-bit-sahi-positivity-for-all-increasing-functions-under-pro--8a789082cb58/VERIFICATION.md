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

The companion `verify.py` is a standalone standard-library Python 3 program. It tests the integer polarization-coefficient identity for every unordered triple drawn from all 20 upper sets of the Boolean three-cube. Its exact exhaustive computation yields 1,540 event triples and 98,560 nonnegative coefficients; 33,057 coefficients are strictly positive, 65,503 are zero, and the maximum is 18. It simultaneously verifies the same functional using direct integer event masses for parameters \((1/3,2/5,3/7)\) and independently at uniform parameters.

To reproduce, save the companion file next to this document and run `python3 verify.py`; the program terminates with `EXACT_VERIFICATION PASS` if every assertion holds. No statistical sampling, floating-point tolerance, or unverified numerical solver is used. The universal parameter claim follows from the exact positive-coefficient polynomial identity, so enumerating parameters is unnecessary. The method is a self-reviewed computation and proof, not an independent audit, and its conclusions are restricted to three product Bernoulli coordinates.
