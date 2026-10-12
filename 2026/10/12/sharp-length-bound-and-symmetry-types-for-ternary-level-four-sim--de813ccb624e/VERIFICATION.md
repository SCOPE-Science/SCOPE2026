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

# Reproducibility and limits

Run `python3 verify.py` (standard Python 3, no third-party dependencies). The checker constructs all \(120\) allowable nonempty subsequences, traverses every reachable append-signature state, and confirms the complete depth census, \(334202\) reachable signatures, and exactly \(1002606\) examined transitions. The enumeration queue empties, so these are exhaustive transition-closed states, not observations from a finite prefix. Three extremal symmetry orbits are calculated from all alphabet permutations and reversal, with exact coverage of the eighteen farthest signatures.

The checker also enumerates actual index combinations to reconstruct subsequence sets of every extremal word independently of the transition recurrence, and computes forward/backward shortest-ranker attributes. All extremal words satisfy the published minimality condition.

Expected first output line:

`VERIFY_OK alphabet=3 level=4 classes=334202 max_minimal_length=18 extremal_classes=18 symmetry_orbits=3`

The scientific claim does not extend to other levels or alphabets; the finite checks do not by themselves imply such an extension. The literature comparison cannot exclude an unindexed or inaccessible prior enumeration. Independent external audit has not been performed.
