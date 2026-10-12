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

# Reproducible finite checks

Run `python3 verify.py` with standard Python 3; no nonstandard modules are required. The final package contains the exact script used. It enumerates every map on sets of sizes \(1\) through \(6\), computes eventual idempotents by a common multiple of their possible cycle lengths, verifies the closed formula for **each** idempotent separately, and checks the full \(n=5\) fiber-profile split. It separately builds edges from actual powers and compares graph connected components to eventual-idempotent fibers for \(n\le5\). Successful output ends `VERIFY_OK`; no subsampling or timeout is treated as evidence.

The independent mathematical argument is the rooted-forest determinant evaluation in `RESULT.md`. Exhaustive finite tests cannot prove the unrestricted \(n\)-quantified statement. The report records only the review stated above; no external or independent audit has been carried out.
