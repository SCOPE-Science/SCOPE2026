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

Run `python verify_classification.py` with Python 3. The script uses only the standard library.

It first reconstructs every minimal recovery set for each of the three requests by exact span tests over \(\mathbb F_2\). It checks that each request has exactly eleven minimal recovery sets and that the request-1 list matches the list printed in Example IV.22.

For \(L=2\), every selected service has multiplicity at most two because it intersects every copy of itself. The script therefore exhausts all \(3^{11}\) multiplicity vectors per request. Requiring at least five service occurrences and the same-request exclusion bound leaves exactly \(141\) candidates for each request, with total-size distribution \(82,45,11,3\) at sizes \(5,6,7,8\). Pairwise cross-request exclusion leaves exactly \(306\) compatible candidate pairs for each of the three request pairs. Intersecting those relations yields exactly two global triples, both with totals \((5,5,5)\); the script prints the two claimed multisets and terminates with `VERIFY_OK`.

The computation is finite and exhaustive for the stated claim. It does not inspect structures with other values of \(L\), and it does not quotient the two labeled solutions by automorphisms.
