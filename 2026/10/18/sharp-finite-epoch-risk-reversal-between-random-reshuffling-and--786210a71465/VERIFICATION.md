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

# Mathematical verification

The derivation of the epoch-noise covariance, the scalar recursion, the signed geometric-sum identity, and the factor-two bound and extremizer are written out in `RESULT.md`. Independent rational enumeration in `check.py` verifies six finite cases and does not substitute for proof of the general theorem. Execute `python check.py` using a standard Python 3 interpreter; no third-party dependency is required.

For the \(n=3\), \(K=2\) scalar example with centered component offsets \((1,-2,1)\), the exact RR/SGD terminal gaps switch from \((3649,10929)/32768\) when \(r=1/2\) to \((126369,98289)/32768\) when \(r=-1/2\). For fixed \(H=\mathrm{diag}(1,3)\), \(\eta=1/2\), two offset configurations produce comparisons of opposite signs, illustrating mixed-spectrum weighting.

No infinite result depends solely on a finite enumeration. Source coverage is incomplete for two inaccessible full texts, and independent validation is not performed.
