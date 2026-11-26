---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the exact moments from disk orthogonality, applying it to f and f². The only phase interaction is |b²+2ac|², so when all coefficients are nonzero the stated congruence is necessary. For nonzero a, fixing s=|c/a| and parametrizing by the linear-mode fraction of L² energy makes the phase-aligned ratio a quadratic with positive slope at fraction 0 and negative slope at 1. Its sole maximum reproduces the stated rational envelope; its derivative changes sign exactly once by the factored cubic and Descartes' rule. Substitution at the root gives |b/a|²=s+3. Independently reoptimized every two-mode face, yielding 8/5, 11/6 and 99/43. These are strictly below the interior envelope maximum. The resultant gives the claimed polynomial for K; its derivative has strictly positive coefficients after shifting K by 5/2, and the envelope at s=3 is already greater than 5/2, so the value is the largest real root. This proves the sharp constant and all equality cases rather than inferring them from samples.

## originality

PASS

Pass applies to the exact finite unweighted norm, the uniquely determined magnitudes with a complete equality family, and the exact two-mode benchmark. Generic three-mode support and phase alignment are not distinct contributions: stronger weighted results already imply them. The strongest retrieved weighted record provides the exact unoptimized quartic and face exclusion but does not solve the finite unweighted maximization or give the sharp two-mode constant. Its unsupported reference to a previously known unweighted calculation is a real residual risk, not demonstrated equivalent coverage.

## value

PASS

A natural first disk-area Bergman space with phase interference gets an exact sharp embedding norm and a complete optimizer classification. The quantified best two-mode value distinguishes how much is gained by the third mode, beyond qualitative support persistence. These precise quantities are useful benchmarks for weighted extensions and for testing candidate extremizers, not just a recomputation of a general upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
