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

# Reproducibility and proof checks

Execute `python3 verify_two_car.py` in the same directory as the other files. The script requires only the Python standard library and independently simulates the labeled horizontal and vertical positions with ordered half-steps. It does **not** implement the reduced arithmetic orbit map as its step function.

The executed run passed \(225\) pairs of grid dimensions \((m,n)\) with \(2\le m,n\le16\) and all \(18{,}000\) nonoverlapping relative placements on those grids. It checked the exact primitive eventual full-configuration period, number of failed attempts by each species per period, at-most-once blocking for gcd at least three, and the exact number \(2\operatorname{lcm}(m,n)-1\) of placements suffering one block in that regime. Representative larger dimension predictions are also printed; those are formula evaluations, not a proof for large sizes.

Independent mathematical reconstruction should verify the relative map at each of the two exceptional states; the \(\gcd\)-class action; the two congruence systems determining intervals between event types; and the closure of full physical positions rather than only relative displacement. These steps are written in `RESULT.md` and establish the arbitrary-dimension result analytically. Finitely many exact simulations cannot establish universality or absence of unindexed historical literature. Independent audit remains unperformed.
