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

# Reproduction and limits

Run `python checker.py` using Python 3 and installed NumPy and SciPy. The code checks exact rational identities for four strictly ordered triples, exact normalized-axis reconstruction, the dual symmetry, 20,000 normalized random normal vectors per test triple against both the quadratic-pair formula and its Kantorovich maximum, and deterministic conditional-arcsine quadrature for near-endpoint spherical cap probabilities.

The cap computations at three shrinking deficits are compared with the analytical coefficient for \((a,b,c)=(1,2,3),(2,3,7),(1,4,25)\). Independent numerical integrals corroborate the local-cap normalization, but finite tests do not prove an all-parameter result. The proof in `RESULT.md` provides that argument. No independent audit or external mathematical validation is claimed.
