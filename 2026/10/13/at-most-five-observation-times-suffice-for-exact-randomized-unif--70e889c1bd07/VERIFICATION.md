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

# Reproduction of exact quantum-walk calculations

Run `python3 verify.py` in the directory containing the standalone source file. No external Python package or network access is required. The successful output is:

```
VERIFY_OK spectral_projectors=5 exact_projector_entries=320 exact_mixing_classes=5 exact_cesaro=3/32 independent_taylor_entries=256
```

The checker constructs the complete eight-cycle adjacency matrix and five spectral projectors in the exact field \(\mathbb Q(\sqrt2)\); it checks the projector identities and the exact weighted moments producing the five probabilities \(1/8\). It verifies the ordinary Cesàro distance-two probability \(3/32\). Four time values provide independent direct Taylor-series-vs-spectral matrix-exponential comparisons; these finite numerical tests corroborate but do not prove the theorem for all times.

The unrestricted existence of positive-weight physical observation times follows from the analytic full-support barycenter argument, irrational flow density, and Carathéodory's theorem in `RESULT.md`. No finite numerical phase approximation substitutes for that argument. No explicit exact time list, minimum support size, or external independent validation is asserted.
