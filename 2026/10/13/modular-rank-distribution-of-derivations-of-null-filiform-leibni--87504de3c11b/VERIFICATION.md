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

# Finite-field verification and proof dependencies

Run `python verify_derivation_nullfiliform.py` in the directory containing the included script. It uses Python 3 and only its standard library. The script exhausts every parameter vector for dimensions \(1\leq n\leq8\) over \(\mathbf F_2\), \(1\leq n\leq6\) over \(\mathbf F_3\), and \(1\leq n\leq5\) over each of \(\mathbf F_4\) and \(\mathbf F_5\). It constructs matrices and computes ranks without using the counting formula, verifies the gauge identity coefficientwise, and checks the resulting nullity counts against the claimed closed forms. Successful output terminates with `VERIFY_OK`.

A direct derivation of the closed formula, valid beyond these finite tests, is given in `RESULT.md`, Proof, Steps 1–5. The critical arguments are the derivation recurrence, triangular invertibility on an incomplete characteristic block, the coefficientwise gauge recursion, its decomposition into residue classes modulo \(p\), and uniform triangular fibers. There are no external computational packages or precomputed data dependencies.

Finite exhaustive agreement cannot certify originality, independence, or every infinite-dimensional parameter case. No independent mathematical audit has been performed.
