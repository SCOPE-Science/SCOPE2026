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

The accompanying `verify.py` uses Python's `Fraction` and integer arithmetic only; no nonstandard packages or data files are necessary. Run `python verify.py` alongside this document. The verifier compares two independent calculations of the interleaving-cost law for all 64 ordered block-size pairs from 1 to 8, checks the five exceptional cases exactly, and verifies the mixed-block inequality on 300 pairs of sizes 2 through 25.

It also enumerates every unlabeled full rooted binary shape for 2 through 14 leaves (2,179 shapes at 14 leaves), checks the precise caterpillar optimum and second-ranked tree shape and \(1/6\) gap, and for up to six leaves independently enumerates all full rankings and admissible domain rankings to check the expected minimum Kendall distance directly. Every one of these tests passed. The analytic proof, rather than finite enumeration, certifies the claim for unbounded numbers of leaves. It does not establish an independent audit or priority outside the inspected sources.
