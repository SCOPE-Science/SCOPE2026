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

# Reproducibility and scientific limits

Execute `python3 verify_spiral.py` in a directory containing the accompanying file. The script uses only the Python standard library and prints `SPIRAL_INRADIUS_PHASE_ASYMPTOTIC_CHECKS_OK` if its checks succeed.

The test examines finite sets of moduli, arguments and fractional phases, discrete leading-term maximizers, exact illustrative phase values, positive edge orientations of three-eigenvalue triangles, and their lower and upper distance bounds. The written proof independently establishes the infinite-dimensional and uniform-in-phase theorem. This finite test is neither exhaustive over continuum parameters nor a substitute for the analytical argument.

The comparison with the published literature has residual risk because full text for Matache (2001) and Fatehi (2019) was unavailable. No external independent mathematical validation has been performed. There is no claim to an exact numerical range polygon at arbitrary fixed angle.
