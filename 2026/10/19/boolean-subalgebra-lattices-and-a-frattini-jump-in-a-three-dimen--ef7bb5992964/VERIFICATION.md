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

# Verification record

The proof derives the full list of one-dimensional subalgebras from square-zero lines and normalized idempotents, then reduces two-dimensional subalgebra closure to total isotropy of an explicit symmetric bilinear form. Rank and radical arguments exclude all additional planes. Direct intersections give the Frattini and dual-atomistic results.

The included `verify.py` independently enumerates every projective line and hyperplane in dimension three, tests multiplication closure for each, and compares the entire resulting lists to the claimed formulas over all nonzero parameters in the prime fields of orders 3, 5, 7 and 11. It also checks maximal-subalgebra intersections and whether every subalgebra is an intersection of maximal ones. Running `python3 verify.py` returned `VERIFY_OK 22 complete finite-field configurations`.

These exhaustive **finite-field** checks are not a proof for infinite fields or larger finite fields; the symbolic bilinear-form argument supplies that proof. No independent audit or external certification was undertaken.
