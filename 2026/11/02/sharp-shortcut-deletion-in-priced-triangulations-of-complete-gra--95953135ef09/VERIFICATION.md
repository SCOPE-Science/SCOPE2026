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

The proof is analytic and covers every integer \(n\ge3\) and all positive prices and budget. The embedded `verify.py` is dependency-free and reconstructs weighted Laplacians, rather than merely substituting into the proposed closed formula.

Run `python3 verify.py` in the directory containing this document. The resulting exact-rational checks include 12 full-matrix pseudoinverse traces on orders \(n=3,4,5,6\), 196 coefficient and threshold identities over \(3\le n\le100\), two checks of the equal-price support cutoff, and 98 vanishing boundary-derivative identities. The supplied execution reported 308 passing checks.

The arbitrary-dimensional spectral block decomposition, strict convexity of the unrestricted edge allocation, and the absence of other minimizers at the boundary are justified in `RESULT.md`; no claim of exhaustive numerical enumeration or independent validation is made. The checker does not establish publication priority.
