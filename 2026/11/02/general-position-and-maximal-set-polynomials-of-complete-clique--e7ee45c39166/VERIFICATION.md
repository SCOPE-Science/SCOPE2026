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
# Reproduction and proof boundaries

Use Python 3 and its standard library. Save the companion `verify.py` alongside this file and run `python3 verify.py` in that directory. It independently constructs the adjacency lists of \(K_n\square P_L\), obtains every graph distance by breadth-first search, and tests geodesic equality for every selected triple. Every vertex subset is checked, and inclusion-maximality is tested by adjoining every excluded vertex. These tests do not use the classification to determine which subsets are valid.

The eight tested parameter pairs are \((3,3),(3,4),(4,3),(4,4),(3,5),(5,3),(3,6),(4,5)\), totaling \(1,450,496\) subsets. For all eight, the original graph predicates agree exactly with the two symbolic enumerators; the program prints `VERIFICATION_OK` on success. The equalities for arbitrary factor orders are established by the explicit geodesic classification and the separate inclusion-maximality argument in `RESULT.md`. The finite tests are consistency evidence only.

The source-date anchor is the first public arXiv version of the cited general-position-polynomial paper, 2024-01-11 (arXiv:2401.05696); its journal publication on 2024-02-28 is not substituted for that public date. No external independent audit or validation is claimed.
