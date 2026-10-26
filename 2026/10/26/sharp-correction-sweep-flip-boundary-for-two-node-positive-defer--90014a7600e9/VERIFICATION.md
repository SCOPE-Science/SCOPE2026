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

The analytical proof establishes every real parameter and arbitrary correction count. The standalone `verify.py` script uses deterministic pseudorandom test vectors only as finite corroboration. It checks 3,000 parameter points for the fixed-point formula and predictor ordering; checks convergence and the two-cycle equations away from the bifurcation; checks the two sharp step boundaries for five positive initial values; and calculates a critical \(k^{-1/2}\) prefactor at 200,000 iterations. Expected numerical output includes approximately \(x_*=0.9457578532\), \(x_-=0.2478106285\), \(x_+=2.1103854250\) at \(a=1/2,h=2.3\).

The unique two-cycle, strict threshold and critical prefactor follow from the symbolic derivations in `RESULT.md`; the finite sweep tests are not claimed to prove them. No external certification or independent audit has been carried out.
