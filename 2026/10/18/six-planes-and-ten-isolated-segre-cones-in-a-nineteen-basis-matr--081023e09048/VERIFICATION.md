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

The standalone `verify_matroid19.py` script performs exhaustive exact arithmetic for the finite polytope in the theorem. It does not need third-party packages. `python verify_matroid19.py` must emit `VERIFY_OK`, enumerate \(285\) nonempty faces with face vector \((19,81,111,60,13,1)\), locate \(43\) singular torus orbits by exact primitive-ray and maximal-minor tests, and identify their \(16\) maximal singular faces. Cone relations are checked for all six triangular and all ten isolated-vertex candidates. The ambient toric normality, local analytic chart identifications and Hilbert--Samuel multiplicities also use the arguments given in the proof. The checker is an independent computational route to enumerating the finite cone data, not an independent review or certification of the entire theorem.
