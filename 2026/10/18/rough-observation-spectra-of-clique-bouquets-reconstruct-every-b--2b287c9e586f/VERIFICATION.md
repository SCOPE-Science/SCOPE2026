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

Run `python3 verify_clique_bouquet.py` using Python 3 standard library. The program creates each clique bouquet, independently enumerates all vertex subsets, computes both exact rough approximations, and constructs the multiplicity multiset. It compares with the closed formula and checks the unique central fiber, runner-up multiplicity and number of runner-up outputs, plus multiplicity-aware reconstruction of clique factors.

Actual result: `VERIFY_OK profiles= 141 vertex_subsets= 551328 fiber_spectrum=PASS central_uniqueness=PASS runnerup=PASS size_reconstruction=PASS`.

The checks are exhaustive for the specified 141 finite profiles, not for the infinite family. The written proof covers all integer parameters in scope. Bibliographic uniqueness and independent review remain unverified.
