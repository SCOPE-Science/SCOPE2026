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

# Verification of the mathematical finding

Run `python3 verify_moran.py`. The program uses Python 3 standard-library integer arithmetic and enumerates all connected labeled simple undirected graphs on two, three or four vertices and every nonconstant binary source profile. It calculates adjugate-polynomial representations of equilibria and exact integer coefficients of the Moran derivative numerator; all nonexception coefficients are nonnegative. Exactly 24 exceptional labeled instances are identified, representing the path with a contiguous two-site source block at one endpoint or its complement.

The program's exact checks also cross-multiply the closed formulas for Moran and Geary indices on the canonical path and assert them as polynomial identities, avoiding floating-point evaluation and numerical root approximation. The proof separately factors the Moran derivative for all real dispersal ratios and identifies its sole positive zero. The statement has no claims about larger graphs, irregular dispersal weights, nonlinear dynamics or empirical causal effects. No external independent audit has been conducted.
