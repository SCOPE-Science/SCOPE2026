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
# Verification and reproducibility

The proof in `RESULT.md` applies to every integer \(N\ge5\) and every strictly positive prescribed normalized three-tap magnitude triple. All required analytic ingredients are stated and proved there, including the boundary gap case and the unit-circle-root argument.

Run `python3 CHECK.py` from the same directory; no third-party dependencies are required. It independently builds finite cyclic Gabor atoms and their frame operators, compares direct Hilbert–Schmidt and Fourier-spectral calculations, enumerates sampled gap optimizers, and checks explicit tight examples. The supplied deterministic run passed with `CHECK_OK assertions=43821`.

Floating-point agreement does not establish universal mathematical correctness or originality. The exact all-order conclusions follow from the analytic proof. No independent mathematical audit has been performed.
