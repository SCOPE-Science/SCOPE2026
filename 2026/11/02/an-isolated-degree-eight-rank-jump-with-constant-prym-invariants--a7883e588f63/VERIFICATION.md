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

Two executable checks were completed on the embedded original scripts: `python verify_symbolic.py` returned `SYMBOLIC_GENUS7_PRYM_OK`; `python verify_field.py` returned `INDEPENDENT_FINITE_FIELD_OK`. The symbolic script evaluates Cartier coefficient identities, nonzero minors, and finite-field polynomial separability/irreducibility. The second script constructs \(\mathbb F_{5^8}\) explicitly and checks semilinear ranks on smooth ordinary-maximum and exceptional parameters for both curves. The proof in RESULT.md supplies the infinite-field reasoning; no finite run is treated as an exhaustive enumeration of algebraically closed parameters. Independent external audit and validation have not been performed.
