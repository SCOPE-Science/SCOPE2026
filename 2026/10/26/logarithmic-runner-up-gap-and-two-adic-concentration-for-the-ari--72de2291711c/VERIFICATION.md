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

# Verification

The exact proof and explicit constants are in `RESULT.md`. The following scientific checks were completed:

1. Reconstructed the arithmetic derivative from its defining Leibniz rule and prime values. Checked the \(m=1\) and \(t=k\) boundary cases explicitly.
2. Checked the key odd-prime bound by monotonicity of \(p\log p\), the affine minimization using \(m\le2^t-1\), and the convex minimum of \(ct+bk2^{-t}\), including the factor \(b=1/2-c\).
3. Independently enumerated the entire sets \(1\le n<2^k\) for \(2\le k\le20\), computing arithmetic derivatives via prime-factor recurrence; the numerical bounds and maximizing-argument localization were satisfied. The verifier is included as `verify_gap.py`.
4. Compared the claimed second-best gap and two-adic localization with the 2011 dyadic record theorem, the 2003 factorization and equation results, published record tables, and semantic research searches. No exact implication was found among inspected materials.

**Limits.** Tests through \(2^{20}\) are finite corroboration and do not prove the universal result. The proof does not determine the sharp leading constant or exact runner-up for all \(k\). A prior literature result outside inspected sources remains possible. Independent audit has not been performed.
