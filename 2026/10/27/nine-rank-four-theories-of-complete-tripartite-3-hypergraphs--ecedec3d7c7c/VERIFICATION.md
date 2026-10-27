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

# Verification scope

The file `verify_complete_tripartite.py` implements the exact recursively defined finite first-order rank-type invariant in two independently written forms, with and without orbit compression. Running it over all twenty sorted triples in \(\{1,2,3,4\}^3\) exhausts every possible capped case. Both methods return the identical nine-class partition, checked by equality of full nested signature objects rather than digest collisions. Additional larger-size tests are not used as the infinite proof; the classwise four-round back-and-forth argument supplies that step. The program is self-contained and uses Python's standard library only.

The recorded output in `verification_output.txt` was obtained by executing this script. No formal proof assistant, independent scientific reviewer, external certification, or probabilistic inference is claimed. The only computational assumption is correct execution of the provided transparent finite recursion; its logical correctness is justified in the proof.
