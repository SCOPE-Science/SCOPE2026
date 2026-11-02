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
# Verification and limits

Execute `python verify.py` with Python 3 and SymPy 1.13 or later. `verify.out` contains the actual complete stdout of a successful run, including `VERIFY_OK`. The verifier reconstructs the quartic's restriction to a candidate line, its two square-of-quadratic elimination equations, the reduced Gröbner basis, the eliminant's squarefreeness, all irreducible factor degrees using polynomial modular exponentiation and Euclidean gcd, the smoothness contradiction, and the unique rational bitangent identity. The symbolic operations are over \(\mathbf F_5\), not finite samples or floating-point approximations.

General bitangent completeness additionally invokes the standard odd-theta-characteristic theorem for smooth nonhyperelliptic genus-three curves in characteristic different from two. All-extension rational-point formulas follow from degrees of the verified irreducible factors. No independent mathematical certification is claimed. Priority remains provisional because not every possible historical source is indexed or fully available.
