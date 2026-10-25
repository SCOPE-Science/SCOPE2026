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

# Exact verification
Run `python3 verification/schur_verify.py`. The only dependency is Python's standard library. The verifier uses \(\mathbf F_{25}=\mathbf F_5[e]/(e^2-2)\), enumerates every one of the \(25^4\) ordered matrices, checks all five coefficients of the binary quartic identity with exact field arithmetic, enumerates the full 64-line list, and detects every plane containing at least two lines by exact row elimination. It verifies the 72 four-line planes, 12 rational four-line planes, rational-line intersection graph, and every Frobenius orbit count. The expected success sentinel is `VERIFY_OK`.

These finite exhaustive computations are certificates for algebraic identities over the specified field, not general proof of all geometric lines without [1]. Completeness is supplied by the independently established geometric bound. The reduced four-line-plane set is treated set-theoretically; no claim of scheme-theoretic smoothness or etaleness is made for that auxiliary locus. No independent audit has been performed.
