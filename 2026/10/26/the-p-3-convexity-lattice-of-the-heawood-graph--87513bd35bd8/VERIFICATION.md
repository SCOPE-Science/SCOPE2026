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

The standalone standard-library Python 3 file `verify_heawood_convex.py` constructs the Fano plane from binary vector triples and checks every one of the \(2^{14}=16,384\) vertex subsets using the definition that each unselected vertex has at most one selected neighbor. A separately implemented join/meet rule is tested on the same universe. All bivariate coefficients, the univariate polynomial, and the 49 maximal proper convex sets are cross-checked against the geometric classification.

Command: `python3 verify_heawood_convex.py`.

Observed output is embedded in `verification_output.txt`; its first line is `VERIFY_OK`. In particular, there are 366 convex sets and the maximal proper counts are \(21\) for the \((3,3)\) point–line type and \(28\) for the \((4,4)\) type.

The checker exhausts this one finite labeled graph only. The general mathematical proof and its classification table appear in `RESULT.md`. No external independent audit or generalization to other projective planes has been performed.
