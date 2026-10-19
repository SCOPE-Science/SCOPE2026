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

# Verification and limits

The explicit four-case ray-entrance proof and the exact two-/three-step scalar return formula establish the all-state and all-parameter assertions. The inequality \(ab-1<d<ab+1/a\) follows by checking when the relevant return factor is below one; at equality, a continuum of primitive periodic rays witnesses failure of asymptotic stability.

For \(d=ab\), the third iterate of every \(x>0\), \(s=y-bx>0\) input is \((ad x,0)\), sharpening the global entrance time to three steps. Thus \(F^5\equiv0\), while \(F^4(1,b/2)=(-a^2b^2/2,-a^3b/2)\ne0\) shows sharpness.

Execute `python verify.py` using the Python standard library. It checks 229 exact rational parameter triples and 361 rational initial points for each triple, along with exact return and critical cases; all checks passed. This finite computation is supplementary, not an infinite certificate. No independent mathematical verification has been performed.
