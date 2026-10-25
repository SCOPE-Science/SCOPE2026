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
# Verification and scientific limits

The proof is analytic and combinatorial. Its crucial infinite-family steps are: (i) continuity, equivariance and fixed-image property of the explicit deformation on radial coordinate charts; (ii) connectedness and integral incidence exactness of the resulting crown graph; (iii) signed trace on the oriented edge chain group; and (iv) the standard rational two-subset-module and exterior-square character identities. The manuscript states these steps in full and distinguishes \(n=3\) from \(n\ge4\).

Reproducibility: run `python3 check.py` (Python standard library only) alongside this file. The checker constructs a spanning tree, computes an explicit integral basis of fundamental cycles, and evaluates signed actions directly on those cycles for every group element of \(S_n\times C_2\) for \(n=3,4,5,6,7\). The actual recorded output reports group-element totals \(12,48,240,1440,10080\) and overall `PASS group actions checked: 11820`. It also verifies the basis' integral boundary vanishes. This is a finite consistency check, not an exhaustive verification of all \(n\).

No independent audit has been performed. Unindexed prior character calculations and modular representation behavior are outside this verification.
