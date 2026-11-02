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

# Verification summary

The independent validation channel has not been used. Run `python3 verify.py` with the Python standard library.

The included verifier uses an exact smallest-prime-factor sieve through \(200000\) and computes first forbidden mosaic depth by valuation recurrence, comparing small instances with an independently recursive definition. For nine forbidden-prime sets it checks all tower minima that lie within the bound and, where applicable, verifies the depth-three second-witness gap. It separately compares truncated Euler products via exact rational sums and a tabulation of depths. The execution completed with `VERIFY_OK`; the detailed printed rows are reproducible by running the file. No computation claims to establish an infinite limit. The proof uses convergence of multiplicative Euler products and upper densities of prime-power divisibility events, not experiments.
