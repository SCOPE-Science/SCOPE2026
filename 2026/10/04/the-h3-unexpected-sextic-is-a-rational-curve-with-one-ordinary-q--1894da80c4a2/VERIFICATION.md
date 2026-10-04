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

`artifacts/verify.py` reconstructs the exact interpolation problem over \(\mathbb Q(\sqrt5)\) at \(P_0=[3:5:1]\). It checks rank \(27\), all 15 point incidences, all order-\(<5\) jet conditions, the displayed degree-5 and degree-6 translated pieces, coprimality of those pieces, and squarefreeness of the tangent quintic.

The verifier is finite and exact. It does not enumerate all assigned points. The passage from the witness to a general point uses standard Zariski-openness of irreducibility and nonvanishing of the tangent discriminant on the one-dimensional-kernel locus. The genus-zero and no-other-singularity conclusions use the standard plane-curve genus formula and the delta invariant \(\binom52=10\) of an ordinary quintuple point.
