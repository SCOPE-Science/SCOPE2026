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

The separate source file `verify_prelinearity.py` may be run with `python verify_prelinearity.py` (Python 3, standard library only). It enumerates each transitive relation on an increasing natural labeling, removes duplicate closures, forms every downset and directly evaluates implications for all ordered pairs. Its structural-form test is implemented independently of the implication calculation. For poset orders one through six it checks respectively 1, 2, 7, 40, 357 and 4,824 increasing-label posets, for a total of 5,231, and checks the unique maximum count within the minimal-failure class for orders three through six. The script also constructs and checks the extremal family with between one and seven upper antichain vertices.

The proof for arbitrary finite poset sizes rests on the singleton separating-ideal argument, the unique-middle-pair normal form, and the forest converse. Exhaustive checks on bounded orders are not an all-size proof. Full mathematical and historical-priority checks by independent researchers remain unperformed.
