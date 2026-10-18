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

# Verification instructions and boundaries

Execute `python3 verify.py` in the directory containing the files. The program uses only Python standard-library integer arithmetic and asserts the exact factorial squarefree-kernel collision structure for every pair of indices in the range \(1\le c<d\le260\), checks each of the ordered three-factor square conditions up to largest index \(260\), verifies that at most two consecutive-largest representations occur, and matches the exact doubled-endpoint count at four cutoffs. It computes the first eight distinct duplicate kernels without floating-point factorization.

The underlying infinite proof is the argument in `RESULT.md`, depending on the Erdős--Selfridge perfect-power exclusion, the squarefree-factorial growth bound, Yudin's exceptional-endpoint theorem, and the uniform small-parameter estimate. The finite program neither proves those theorems nor supplies a rigorous numerical tail bound for the infinite constant. No independent examination has been performed.
