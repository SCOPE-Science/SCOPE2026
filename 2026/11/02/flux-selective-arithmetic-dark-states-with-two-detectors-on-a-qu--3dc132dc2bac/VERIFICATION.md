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

# Reproducibility record

The full exact finite-ring checker is embedded alongside this file as `quantum_ring_dark_check.py`. Run `python quantum_ring_dark_check.py` using Python 3 with NumPy and SciPy. The checker was executed from its actual package source and returned:

`PASS 32975 exact-arithmetic/Fourier, absorbing and projective evolution checks`

All ring lengths from \(3\) through \(36\), all distinct monitor spacings and localized starts, and both special fluxes are covered by direct arithmetic/Fourier assertions. Selected cases were also tested by independently exponentiating the non-Hermitian absorption generator and by projecting a discrete unitary evolution for 4,000 steps. This is not exhaustive for unbounded ring sizes and does not establish statements about sampling resonances. The mathematical proof is contained in `RESULT.md`; no independent scientific audit has been performed.
