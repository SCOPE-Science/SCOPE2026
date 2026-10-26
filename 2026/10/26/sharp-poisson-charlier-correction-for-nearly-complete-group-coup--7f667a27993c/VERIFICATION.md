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

# Reproducible checks and limits

Run `python verify.py` with Python 3's standard library. Exact rational factorial-moment inversion reproduces exhaustive uniform-group enumeration for the tuples \((n,r,t)=(5,2,3)\) and \((6,3,2)\). Numerical comparisons at \((100,10,2)\), \((400,20,2)\), \((1600,40,2)\), \((64,16,3)\) and \((216,36,3)\) verify the stated explicit \(\ell^1\) bound; for the first three, \(r\,d_{\mathrm{TV}}\) decreases from approximately \(0.576860\) to \(0.558592\), toward the analytically established value \(0.551819\) at \(\lambda=1\). The all-parameter inequality follows from the written analytical proof and is not established by these finite checks.

An independent audit and independent validation have not been performed. Historical priority, as opposed to the internal proof, remains subject to external literature evaluation.
