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

For finite-dimensional \(\ell_\infty^n\) and finite \(t\ge1\), the proof reduces the defining supremum to cube vertices using the published Proposition 4.4. After signed-permutation normalization of \(x\), the proof checks both possible signs of the first coordinate of every vertex, so no vertex class is omitted. The explicit vertex \((1,-1,1,\ldots,1)\) attains the upper bound.

The companion `verify.py` enumerates all cube vertices for several representative rational sphere points in dimensions \(2\) through \(4\) and compares the direct maximum with the closed formula for several finite parameters. It prints `VERIFY_OK` on success. These finite computations are sanity checks only; the quantified theorem is established by the analytic argument in `RESULT.md`.

Unproved limits: no assertion is made for \(t<1\), the non-power-mean endpoints, or infinite-dimensional \(\ell_\infty\).
