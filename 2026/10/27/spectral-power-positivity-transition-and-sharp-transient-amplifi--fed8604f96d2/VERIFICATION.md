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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 standard library. The executable reconstructs exact-rational Laplacian eigenspaces, independently computes exponentials of integer powers by Taylor series, checks all kernel entry types and row norms for a grid of fractional and integral powers, and brackets positive recovery roots. A completed execution returned `PASS: 71243 assertions`.

The analytic proof in `RESULT.md` covers all even graph sizes, all positive spectral powers, and the three asymptotic limits; the finite checker cannot establish such quantified statements by enumeration. The code tests matrix size \(4\) through \(16\) for spectral identities and additional orders through \(1000\) for cutoff consistency; numerical accuracy is controlled only for those finite sample cases. No external or independent audit is reported.
