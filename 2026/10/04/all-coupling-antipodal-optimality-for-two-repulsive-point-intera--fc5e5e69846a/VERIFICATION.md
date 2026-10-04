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

The proof is analytic; the accompanying `verify.py` is a finite consistency check rather than the source of the all-parameter theorem.

It checks four items:

1. for representative positive couplings and asymmetric separations, bisection finds the unique root of the exact scalar secular equation on its positivity branch;
2. the resulting wave number satisfies the periodic two-delta transfer-matrix condition to numerical tolerance;
3. every sampled asymmetric placement has strictly smaller ground-state wave number than the antipodal placement at the same coupling;
4. the antipodal equation and the general scalar equation agree when the complementary arcs are both \(\pi\).

The all-\(\alpha\), all-separation conclusion is proved in `RESULT.md` by monotonicity and strict convexity, not by extrapolating from these samples.
