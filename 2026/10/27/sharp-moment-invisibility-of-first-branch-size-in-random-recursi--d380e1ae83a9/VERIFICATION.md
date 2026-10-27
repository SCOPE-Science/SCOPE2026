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

# Verification record

Executed the exact standalone `verification.py` with `python3 verification.py`; observed `PASS 6586 exact rational assertions; exhaustive trees through n=9`.

The checker independently enumerates every parent array through size nine, comparing conditional branch-size/leaf-count laws with Eulerian convolutions. It then tests exact rational cumulants over further finite sizes and all eligible moment orders, verifies nonzero even-order boundary defects at orders two, four, six and eight, and checks the exact covariance identity.

The all-size, all-even-order conclusion is proved analytically in `RESULT.md` by independent parent-pointer restrictions, Eulerian generating functions and a Laurent-expansion boundary calculation. Computations do not certify untested infinite ranges or publication priority. Independent scientific validation has not been performed.
