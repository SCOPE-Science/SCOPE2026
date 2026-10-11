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

# Reproduction and proof boundaries

The bundled `verify_zak_endpoint.py` uses only the Python standard library. Execute `python3 verify_zak_endpoint.py`. It checks the exact rational alternating-phase Zak identity for 19 integer oversampling factors, four rational offsets, and 31 rational sample positions, plus two-edge energy and transverse-derivative identities. These are 2,622 exact rational checks. It also performs 1,740 supplementary floating-point local samples for six oversampling factors. The checks were run successfully from the supplied script.

The verified full claim is not a finite-computation statement. The proof needs the published global Zak-zero classification for the precise critical zero set and Zibulski–Zeevi's exact fiber representation. The new analysis provides the exact alternating identity, uniform nonzero phase derivative, compactness localization, and sharp scalar hinge minimum. Finite meshes do not prove a global frame bound, and the output asserts no results for other lattice products. The complete text of arXiv:2609.13116 was unavailable and remains an independent literature risk.
