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

# Verification record

The package contains `point_trap_verify.py`, a standalone reproducibility script requiring Python, NumPy and SciPy. It uses the exact piecewise-harmonic transfer matrix for the operator, and independently locates the lowest positive spectral root for trial and optimized trap placements. Running `python3 point_trap_verify.py` yielded `PASS: 1260 assertion groups including exact transfer roots and randomized competitors`.

The script samples 120 parameter sets with one through six fixed, generally unequal trap strengths and tests three independently randomized alternative placements per set. Checks include strict interior ordering, the independently computed spectral residual, equality of the predicted wavenumber and the transfer-matrix ground root, and absence of a randomly sampled competing larger root. The all-parameter uniqueness and sharp bound rely on the four-step analytical Prüfer-phase proof, not sampling, finite-grid approximations, or numerical timeout. The scheme does not establish historical priority or cover zero-strength trap non-identifiability.
