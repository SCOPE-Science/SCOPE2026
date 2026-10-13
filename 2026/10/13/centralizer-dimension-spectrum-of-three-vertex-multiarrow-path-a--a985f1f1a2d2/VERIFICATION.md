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

# Verification of the centralizer-dimension formula

The standalone `verify.py` uses only Python's standard library. Run `python3 verify.py` from the directory containing this file. It enumerates every algebra element in nine small parameter sets, constructs multiplication independently from the actual path basis, computes the full commutator linear map, and determines its nullity by finite-field Gaussian elimination. It compares the complete observed dimension histogram to the symbolic fourteen-stratum prediction and checks that predicted multiplicities sum to the order of the algebra.

The checked parameters are \((q,r,s)=(2,1,1),(3,1,1),(4,1,1),(2,2,1),(2,1,2),(2,2,2),(3,2,1),(5,1,1),(4,2,1)\). The \(q=4\) cases use \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). The \((2,2,2)\) case is within the theorem's \(r,s\ge2\) domain, while one-arrow-family cases stress-test boundary formulas. A passing run prints `VERIFY_OK` after all exhaustive cases.

The proof of the general formula uses a symbolic case partition and elementary tensor linear algebra; the enumerations alone verify only the listed finite instances. No independent mathematical audit has been performed.
