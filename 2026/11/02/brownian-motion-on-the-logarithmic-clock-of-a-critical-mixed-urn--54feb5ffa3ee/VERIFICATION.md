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

The formal proof is in `RESULT.md`, including the exact domain, martingale bracket, summable correction, and functional-limit argument. Run `python3 checker.py` using Python 3 standard library only, and compare with `checker_output.txt`. The finite checker enumerates exact rational transitions of the specified urn through a bounded number of steps and independently checks the one-step drift, the centred noise bracket, the second moment, and updates. The infinite-time functional conclusion follows from the proof and is **not** certified by finite enumeration.

The limiting theorem is under self-review; no independent audit is asserted. Fang (arXiv:2509.15049) previously established critical logarithmic-clock Brownian limits for an elephant random walk; the mixed random-total urn specialization is addressed here. The historical-priority comparison is also qualified by incomplete access to broad generalized-urn primary text.
