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

# Verification of the exact normal-fan illumination theorem

The mathematical argument is in `RESULT.md`: it proves (i) the exact direction-cell incidence structure from antipodal normal pairs, (ii) sharp vertex-incidence lower bounds, (iii) floor-distributed cyclic-block upper constructions for every positive multiplicity, and (iv) the parity classification of all optimal fractional cell masses by subtracting consecutive vertex saturation equations.

The accompanying finite consistency checker `verify.py` was run from its own file path. It returned `VERIFY_OK` after 1,950 exact cyclic multicover test instances, checking the parity family for 39 tested vertex counts, and validating the closed, strictly convex nonequiangular and noncentrally symmetric six-edge example in exact rational arithmetic. The finite enumeration does not establish the universal theorem; that responsibility belongs to the preceding symbolic proof.

Every optimal fractional measure may redistribute mass freely inside a given illumination cell; the theorem specifies the uniquely determined or alternating *cell totals*. Its assumptions explicitly exclude consecutive collinear edges and polygons lacking a paired normal fan. No external or independent audit has been performed.
