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

# Reproduction and scope

Run `python3 verify.py` with the Python standard library. The seven binary pollinator types on three plants parametrize every unlabeled-on-pollinator-side finite interaction graph. For each of the one-through-ten-pollinator sizes, the checker enumerates all weak compositions of the pollinator count into these seven types; an exact connectivity predicate retains all connected types. There are 17,017 retained type vectors and 1,529 comparisons between distinct matched-degree union profiles. For each comparison it computes the integer coefficients of \((1+t)^nF(t/(1+t))\); all have one weak sign, which excludes an interior sign reversal without any probability grid or numerical tolerance.

The eleven-pollinator witness is separately verified by expanding all 2,048 possible primary-extinction masks for each of the two networks and checking its full moment and variance polynomials. The program finishes with `VERIFY_OK first_three_plant_reversal_at_eleven_pollinators`. The algebraic crossing is proved independently by strict monotonicity of \(q^3+q^2-1\). Neither the checker nor its finite census tests empirical relevance, unbounded graph sizes, or independent originality.
