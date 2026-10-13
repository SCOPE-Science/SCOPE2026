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

# Verification record

Reproducibility: run `python3 verify.py` from the directory containing `verify.py`, using the Python 3 standard library only. The script uses explicit Kripke semantics rather than any external modal-logic package. The observed terminating line was `VERIFY_OK`.

Checks performed: enumeration of all directed binary relations on labeled sets of one through four worlds (including those with no successors), filtering by the Euclidean first-order condition; \(354\) frames satisfy it. Across these frames the script inspected \(5240\) valuation instances and checked the twelve proposed formulas for empty-set preservation and binary union preservation for every pair of subsets of each frame. It also verified that all five serial signatures plus a freely chosen root truth bit and two dead-end signatures are realizable and distinguishable, that the twelve representatives are pairwise distinguishable, and that exactly twelve of the \(4096\) Boolean functions on the twelve point types satisfy normality and binary additivity on the canonical five-world frame together with the dead-end frame.

Proof obligations beyond computation: the cluster lemma for arbitrary cardinalities; both formula-structural inductions; correspondence between the canonical frame's union-preserving root operators and all globally definable operations; full exclusion of an additional infinitary case. These are established in `RESULT.md` and are not claims of exhaustive computer verification over infinite structures. There has been no independent audit.
