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
The package checks the exact additive SM3-I and SM3-II recurrences on finite covers.

`verify.py` reproduces the two-round poisoning construction, compares the target update with singleton-cover AdaGrad, exhaustively proves the one-spike impossibility for a matrix row-column cover, and checks two-spike transversals for tensor slice covers through rank five.

The finite checks are implementation and transcription guards. The arbitrary-cover necessity and sufficiency are proved symbolically by the transversal argument in `RESULT.md`.
