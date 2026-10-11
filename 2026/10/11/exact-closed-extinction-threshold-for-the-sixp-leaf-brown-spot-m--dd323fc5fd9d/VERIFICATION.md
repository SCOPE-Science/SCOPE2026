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
The packaged checker `verify.py` was executed after serialization and re-extraction of the new row. It symbolically verifies the exact identity
\[
\dot V=-\frac{(R_xX+R_cI)I}{S+I}-c(1-R_0)I,
\]
under \(cR_0=R_c+R_x\sigma/\varepsilon\), the infected-block determinant \(\varepsilon c(1-R_0)\), and the plant-block determinant \(\mu(\delta+\mu+\pi)\) with negative trace.

The checker does not prove LaSalle's invariance principle or variation-of-constants estimates; those are supplied analytically in `RESULT.md`. No numerical trajectory experiment is used as an infinite-time proof. The result does not assess endemic-equilibrium stability or the optimal-control subsystem.
