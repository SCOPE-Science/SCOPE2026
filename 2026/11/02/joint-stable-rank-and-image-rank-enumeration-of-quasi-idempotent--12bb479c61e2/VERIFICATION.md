---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For any order-preserving f with f^3=f^2, the idempotent e=f^2 has contiguous fibers rooted at its fixed points; f preserves each fiber and each root. On a one-sided rooted interval of length a, monotone g with g²=0 and j nonzero image values has exactly C(a,2j) choices by first choosing the maximal image and applying Vandermonde. Rooted intervals contribute uv z[(1-z)/((1-z)^2-vz²)]², and taking the geometric series yields F(z;u,v) as claimed. Extracting coefficients proves C(k+r-1,r-k)C(n+k-1,2r-1), zero off support; r=k means idempotence. A monotone map has no cycles longer than one, so f^4=f² is equivalent to f³=f². Independently enumerated all nondecreasing functions through n=8; totals 1,3,10,33,108,352,1145,3721 and strict n=5=53 confirm low-rank boundaries.

## originality

PASS

The univariate count and generating function already appear in OEIS A060557. Imam et al. (2023) characterized quasi-idempotent order-preserving transformations structurally; Eze et al. (2025) tabulate strict counts, including an apparent 52 versus directly verified 53 at n=5. The specific bivariate stable-image/image-rank count and trivariate generating function are not stated in the inspected primary works and do not follow from the univariate sum without extra joint information. A general older transformation semigroup generating-function identity might subsume it.

## value

PASS

Stable rank and transient image rank are intrinsic independent semigroup invariants. The complete two-rank distribution determines far more than known total counts, while correcting a natural five-point enumerative anomaly. This is a motivated uniform family classification, not merely the single 52→53 correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
