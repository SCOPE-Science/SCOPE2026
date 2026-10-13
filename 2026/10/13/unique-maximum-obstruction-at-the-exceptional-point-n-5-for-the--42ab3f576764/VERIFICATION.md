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

The symbolic proof has two finite components and one cited infinite component.

For the uniqueness statement, every nine-element subset of \(\{1,\ldots,10\}\) is the complement of one value. The proof shows directly that deleting \(5\) blocks every witness and gives an explicit witness for each of the other nine deletions.

`verify_h4_n5.py` independently enumerates every four-element positive-integer candidate that can have all pairwise sums in \(\{1,\ldots,10\}\). It confirms that deleting \(5\) is the unique obstruction, checks all explicit witnesses, and exhaustively recomputes the finite thresholds \(h_4(1),\ldots,h_4(5)\). The expected replay line is:

`VERIFY_OK complements=10 unique_obstruction_missing=5 small_h4=2,3,4,4,5`

The computation uses exact integers and set containment only. It does not establish the infinite stable-range statement. The assertion \(h_4(n)=4\) for every \(n\ge6\) is cited from arXiv:2609.39314v1 and is not re-certified here.
