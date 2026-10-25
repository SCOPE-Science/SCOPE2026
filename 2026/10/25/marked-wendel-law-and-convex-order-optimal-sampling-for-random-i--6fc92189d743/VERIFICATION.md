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

# Computational corroboration and limits

The self-contained script `check_marked_wendel.py` uses NumPy and SciPy. Run it from this directory with `python check_marked_wendel.py`.

It tests the exact finite-sample circle tail by direct unconditional random angle spacings; independently compares the closing-chord distance with the minimum distance over every edge in a SciPy Cartesian convex hull; samples the exact rare failure event using inverse-CDF angular conditioning for circular and elliptic curves; and checks the limiting mean, second moment, survival function and minimizing second moment. Its numerical simulations are finite and tolerance-based, not a proof of convergence or historical priority.

The accompanying analytical proof in `RESULT.md` supplies exact conditional survival probabilities, uniform asymptotic expansions, exponential tail bounds and a convex-order minimization argument. Mathematical independence or external certification is not claimed.
