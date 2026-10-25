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

# Verification of the finite shellings

The package includes the complete ordered facet masks in `shellings.json`, a deterministic generator `generate_certificate.py`, and two independent finite verifiers. The first reads each mask, reconstructs every disconnected triple by disjoint-set connectivity, checks completeness and uniqueness of facets and verifies the pure shelling ridge condition against every preceding facet. The second reconstructs the graph with adjacency lists, computes connectivity by depth-first traversal, and checks direct coverage of each pairwise facet intersection by previously present ridges; it also enumerates all nonempty faces.

The observed counts are 169 facets, 7,904 nonempty simplices, and one spanning facet for thirteen vertices; and 238 facets, 16,067 nonempty simplices, and eight spanning facets for fourteen vertices. The `verification_output.txt` file records the exact console output reproduced by `python3 check_shelling.py` and `python3 check_shelling_independent.py` from this package. Only standard Python is required. The all-larger-order conclusion separately uses an explicitly identified earlier theorem, rather than finite numerical induction.

The finite checks are exhaustive within their specified graph orders but establish nothing independently for other graph orders or powers. Bibliographic completeness and independent scientific audit are not certified.
