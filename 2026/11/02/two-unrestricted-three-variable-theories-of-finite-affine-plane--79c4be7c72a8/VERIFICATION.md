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
# Verification

The logical theorem has a mathematical all-plane proof: the noncounting three-pebble strategy preserves ranks, containment, and parallel/intersecting two-line pair profiles, whose one-point extension **supports** are uniform for every affine plane of order at least three. No enumeration is used to infer an infinite family from finitely many cases.

`checks/verify_incidence_profiles.py` enumerates actual finite-field affine planes of orders 2, 3, 4, 5, 7, and 9, including two extension fields. It confirms 21 pair profiles, 144 total distinct ordered support patterns for order two and 148 for each larger order, and it compares each profile's full set of supported pair-profile transitions. The exact recorded output is `checks/incidence_profiles.out`.

`checks/verify_fo3_types.py` independently builds the order-two and order-three planes and computes complete \(\mathrm{FO}^3\) Hintikka-type refinement (including unassigned-variable states) through quantifier rank seven. A quantifier substitutes one variable and records the set of earlier types; therefore it models ordinary existential quantifiers, not counting. It verifies agreement at ranks zero through three and first separation at rank four. Exact recorded output is `checks/fo3_types.out`.

To replay, use Python 3: `python3 checks/verify_incidence_profiles.py` and `python3 checks/verify_fo3_types.py`. Both programs use standard-library imports only. They do not check non-Desarguesian finite coordinates, because that universal case is proved by incidence axioms. An independent audit has not been performed.
