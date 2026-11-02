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

# Verification of the locating–dominating coalition theorem

Execute `python3 verify.py` using the accompanying standalone file (Python standard library only). It reconstructs graph edges, directly verifies domination and pairwise open-neighborhood signatures for each candidate LD-set, and then exhaustively tests every unlabelled partition of the labelled vertex set for profiles (2,2), (2,3), (2,4), (3,3), (2,2,2), (3,2,2), (2,2,2,2), (3,3,2), (2,2,2,2,2), (3,2,2,2). It confirms the predicted maximum counts and four-class multiplicities.

A separate 32767-pattern finite check verifies that no loop-allowing simple support graph on five vertices has no one-cover while each vertex belongs to a two-cover. A second enumerator maps each labelled original part onto a pair of the four temporary class labels and obtains exact optimum counts for 2 through 6 parts: 1, 30, 364, 3480, 30256. All tests terminate in `VERIFY_OK`. This is finite corroboration; the main proof supplies the all-parameter theorem.

No independent mathematical assessment has been performed. The r=2 four-cycle case was already in the source's known small-graph classification. The calculation does not include singleton original parts or enumerate three-class maxima for other sizes.
