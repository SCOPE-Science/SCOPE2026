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
# Verification and limits

Use `python3 verify.py` with Python 3 standard library. The verifier defines \(Z_n\) independently by recursive concatenation and by the ruler formula, then checks their equality for levels 1–11. It enumerates **all** cyclic squares by starting positions and all permitted half-lengths for levels 1–11 and compares the exact set of pairs with the theorem. For every such circular square it checks that the following symbol, when available, breaks its period. Independently of the theorem's cyclic-square formula, it constructs and directly scans all 502 distinct rotations through level 8 and compares every rotation's exact linear-square count with the predicted full histogram.

Successful standalone output:

`VERIFY_OK cyclic_square_levels=1..11 cyclic_square_occurrences=55 independently_scanned_conjugates_levels=1..8_count=502 linear_square_histogram_exact=1..8 no_proper_circular_power_above_exponent_2=1..11 recursive_equals_ruler=1..11`

The mathematical proof in `RESULT.md`, rather than this finite enumeration, establishes the theorem for unbounded levels. Computational verification does not prove scientific priority. A directly relevant 2013 preprint was available only via its bibliographic metadata and abstract, so historical originality remains uncertain pending wider literature inspection. No independent audit has occurred.
