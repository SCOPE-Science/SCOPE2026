---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The full RESULT and exact verifier were read and freshly replayed. Positive rational rescaling of each Sturm remainder to a primitive integer polynomial preserves every sign variation while avoiding fraction blowup; caching does not change any polynomial. Exact factorization, zero real roots of S and S-3/200, exactly two distinct real roots of R, interpolation constraints and all 49 rebuilt coefficients pass. Additionally every individual critical box was recounted and checked disjoint/in-range, not merely its claimed count sum. Machin alternating-series rational pi bounds and rational sine/cosine Taylor remainders verify the tan cover; the exact Fourier triangle bound verifies F(1/2)-L*0.001>0.2355. All critical and endpoint values exceed 3/1000. Positivity and the exact two zeros force every maximizing invariant measure onto the two-cycle, whose invariant measure is unique.

## originality

PASS

No inspected prior theorem or table determines this exact two-harmonic maximizing-measure problem.

## value

PASS

An exact, certified maximizing measure for a natural low-degree trigonometric potential outside the translated-cosine one-parameter family is a motivated finite exact result in ergodic optimization and supplies a reusable explicit calibrated-subaction example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
