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

# Verification of the finite-horizon diagonal RK–RK result

Run `python3 verify.py` in the same directory. The file uses only the Python standard library and reads no external data. It directly constructs both row updates in exact `Fraction` arithmetic, enumerates every row-pair sequence for small diagonal systems, and checks the exact componentwise error formula. It checks all pair-law marginal sums, the extremal diagonal coupling, and strict independent-versus-maximal risk comparisons. The balanced identity is checked as a rational equality over multiple dimensions, horizons, and synchronization mixtures. Lastly, numerical evaluations test the exact transition root and the finite-size correction predicted by the analytic expansion.

All infinite-dimensional-in-the-parameter assertions—every integer dimension, every nonnegative horizon, all admissible real sampling marginals and coupling weights, and the uniform asymptotic scaling—are established by the proof in `RESULT.md`, not by the finite tests. There is no claim of independent external verification.
