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
# Exact reproducibility

Execute `python3 verification/verify.py` from the root of this package; it uses only the Python standard library and prints `VERIFY_OK` on success. It reconstructs the two Gray halves directly from the complement-product defining set, normalizes every surviving column, and computes multiplicity classes. For seven field/parameter combinations it tests the missing-flat condition and exact dual weight-two count; a reduced-echelon enumeration checks every dimension of the projective-core generalized weight hierarchy. All arithmetic, including the four-element field, is exact.

Representative independently reproduced outputs: at \(q=2,m=3,A=\{1,2\},B=\{2,3\}\), length \(96\), heavy \(40\), light \(16\), projective core length \(56\), core generalized weights \((28,42,49,53,55,56)\); at \(q=3,m=2,A=\{1\},B=\{2\}\), length \(144\), heavy \(33\), light \(6\), core generalized weights \((26,35,38,39)\), dual weight-two count \(408\).

These checks are exhaustive only for the seven enumerated cases. The mathematical proof, not the checker, establishes the quantifiers for arbitrary prime powers and all admissible \(A,B\). No independent review is asserted.
