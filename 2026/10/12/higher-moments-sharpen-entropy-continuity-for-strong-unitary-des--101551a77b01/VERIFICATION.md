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

The mathematical proof is analytic. The executable check in `artifacts/verify.py` verifies only finite algebraic and numerical consequences:

- the optimized cutoff reproduces the closed-form bound;
- the case \(q=2\) reduces to the source square-root bound with the exact finite-dimension factor \(R_{N,2}=N/(N+1)\);
- \(0<R_{N,q}\le1\) for representative dimensions and even moments;
- the constant used to simplify the logarithmic-moment choice is strictly below \(15\).

The checker does not establish the infinite family, novelty, or asymptotic big-O statement. Those depend on the written proof and the cited source theorem. The full proof also records the restrictions to strong relative-error designs, even moments \(q\le2k\), ensemble-averaged Shannon entropy, and the generic regime \(k\ll2^n\) for the resource corollary.
