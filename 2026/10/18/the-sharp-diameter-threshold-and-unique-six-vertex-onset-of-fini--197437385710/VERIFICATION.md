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

`python3 verifier.py` runs entirely on the Python standard library. The attached `verification_output.txt` is the program output from the current package source. Checks are exhaustive for all labelled simple graphs at orders four, five and six; connectivity and exact diameter are computed for every edge mask, and each qualifying graph is tested against every set partition generated as a restricted-growth word. The finite census returns \(12,300,12540\) diameter-three labelled graphs and \(0,0,720\) graph masks with some resolving multiset partition. All \(720\) positive masks pass an explicit isomorphism check to the stated six-vertex graph. Its 203 partitions contain only two resolving partitions, both with five blocks. The independent graph-atlas enumeration used during exploration agreed on the single isomorphism class; the standalone program is the necessary complete finite certificate.

**Unbounded part.** The diameter-two statement uses an elementary argument about the number of possible codes and is proved in `RESULT.md`; the finite program does not attempt to certify infinitely many graphs.

**Limits.** No classification is proved for larger diameter-three graphs. Independent audit has not been performed; bibliographic priority has not been independently certified.
