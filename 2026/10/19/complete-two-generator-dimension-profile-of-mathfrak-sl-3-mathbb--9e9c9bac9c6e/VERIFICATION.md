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

# Exact finite verification

Run `python3 verify.py` in the directory containing the unpacked files. The program uses Python's standard library only. It generates exactly \(256\) trace-zero nine-bit matrices, computes all \(65{,}536\) binary Lie brackets, and for each ordered pair computes the generated dimension using both basis-bracket closure and a differently ordered adjoint-invariance closure. It asserts histogram equality and exactly the nine reported counts, checks a six-dimensional parabolic subalgebra and an explicit generating pair, and enumerates the \(168\) invertible matrices and the centralizer of all off-diagonal matrix units. Successful replay prints `VERIFY_OK`.

Every calculation is exact over \(\mathbb F_2\), and no random seed, external package, network access or partial test subset is involved. The correctness of either closure procedure follows from finite-dimensional stabilization, bilinearity and the Jacobi identity. The certificate proves only the finite stated claim; it does not check analogues for larger fields, nor certify novelty against all literature. Independent auditing has not been performed.
