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

The mathematical derivation is in `RESULT.md`. The contact identities and supporting-halfspace checks there are exact and hold for every integer \(n\ge2\) and every real \(0\le t<1\). To replay the supplementary finite verification, run `python3 verify.py` from the extracted package directory. Expected result: `VERIFY_OK: 258 exact rational parameter checks; 4601 randomly generated feasible symmetric competitors.`

The checker validates exactly computed support margins, frame moments, symmetry constraints, and radii on rational parameter grids; its random test compares only symmetric feasible competitor ellipsoids. Neither finite parameter sampling nor random optimization proves the all-parameter theorem. The proof's global maximality uses John's general contact theorem, not a restriction to symmetric competitors. No independent audit has been performed.
