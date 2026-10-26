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
# Reproduction and scope
Run `python verify.py` with NumPy, SciPy and mpmath. The self-review reproducibility run returned `PASS: 104 independently evaluated numerical assertions`. Specifically, numerical Fourier inversion was compared against exact even derivatives, the independently derived partial-fraction density was checked against Fourier inversion, the period-half contrast was compared to the Poisson-summed Fourier series, and the exact positive asymptotic remainder was compared to a geometric tail bound. Parameter choices include \(q=0.2,0.4,0.5,0.7\). These finite checks do not prove the all-parameter regularity statement, the strict nonzero harmonic, or any originality claim. The exact proof is in RESULT.md. No external independent audit has been performed.
