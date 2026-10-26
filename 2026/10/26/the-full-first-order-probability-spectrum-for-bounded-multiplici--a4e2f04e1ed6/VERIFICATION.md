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

# Finite exact checks and analytic limits
Run `python3 bounded_cycles_check.py`. The checker enumerates integer partitions at small sizes; evaluates truncated Euler factors exactly; verifies every finite-block conditioning identity for caps 1, 2, 3 and window sizes 1, 2, 3 through order 120; and computes the rational probability errors for the first two coordinates at order 480. The exact success line is:

`BOUNDED_CYCLE_PARTITIONS_EXACT_OK 1134 finite_checks [(1, 49, 0.0151278302148033), (2, 57, 0.016065698823015284), (3, 61, 0.014859501214983098)]`

The decimal errors are display values computed from exact rational probabilities. The checker does **not** establish the limiting distribution, the Fourier bounds, Hanf locality, or historical priority. The mathematical proof in `RESULT.md` supplies the infinite statements. No independent audit or external formal certification has occurred.
