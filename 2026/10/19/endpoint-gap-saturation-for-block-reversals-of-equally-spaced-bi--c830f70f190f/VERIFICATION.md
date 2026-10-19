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

# Finite verification of a structural block-reversal theorem

Run `python3 check.py` in the directory containing the packaged files. The checker independently builds block-reversal sets by enumerating every possible cut mask and constructs the predicted sets directly from zero-gap quadruples. It compares exact **sets**, not just their sizes, for \(0\le m\le7\), and checks \(|\operatorname{BR}(w_m)|=(m+1)^3\).

A successful run reports `PASS 8 source words (a=b=m, 0<=m<=7), exact image equality, cardinality`.

These tests are finite. The general result for arbitrary \(m\ge0\) follows solely from the necessity, explicit five-piece sufficiency construction, and counting proof in `RESULT.md`. No independent audit or external validation is claimed.
