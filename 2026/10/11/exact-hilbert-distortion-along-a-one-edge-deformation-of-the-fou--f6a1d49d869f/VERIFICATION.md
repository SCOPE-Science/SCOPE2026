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

The analytic proof is in `RESULT.md`. Its nonstandard steps are (i) the four-point dual-coordinate identity, (ii) reduction to diagonal quadratic forms by independent sign symmetry, (iii) the complete first-octant vertex census, and (iv) the two-regime exact minimization, including the outward-normal certificate for the longer-edge regime. Each step is explicitly justified there.

Reproduction: run `python verify_k4.py` with Python 3; only its standard library is required. The script determines the first-octant vertices by all independent triples of active constraints, computes both quadratic extrema exactly, checks sharpness at 48 rational parameters, and checks 2,304 other rational diagonal forms. Its successful final line is `K4_ONE_EDGE_EXACT_OK 2304 ellipsoid tests; 48 rational parameters`.

Computational verification is finite and is not claimed to prove the continuum theorem or nondiagonal optimality. Those conclusions depend on the exact inequalities and symmetry averaging in `RESULT.md`. The proof excludes the degenerate zero-distance limit and complex-linear comparisons. Independent mathematical audit has not been performed.
