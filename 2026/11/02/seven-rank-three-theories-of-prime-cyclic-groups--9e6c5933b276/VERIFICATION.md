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

# Verification of the seven-class rank-three classification

The accompanying `verify.py` is a standalone Python 3 program using only the standard library. Run `python3 verify.py` to reproduce the checks. The accompanying `verify.log` was obtained by running it on these supplied bytes.

The executable checks derive the set of thirteen exceptional ratios from all \(66\) pairwise comparisons of twelve affine third-move values, using exact rational arithmetic. They check that the cross-difference numerators of two distinct ratios never exceed \(15\) in absolute value. This supports the symbolic assertion that the exceptional ratios are distinct in every prime characteristic at least \(17\).

The program tests the defined generic-pair sentence on each prime from \(2\) through \(31\), the five explicit characteristic sentences, and independent complete recursive atomic-type signatures on primes \(2,3,5,7,11,13,17,19,23\). The final three signatures agree; the first seven are all different.

These finite computations are not the proof of equivalence for unbounded prime orders. That proof is the structural twelve-affine-candidate argument in `RESULT.md`: for every prime at least \(17\), the same thirteen exceptional ratios and generic ratio class give exactly the same one-move extension profiles; the named-zero case is handled separately. Distinctness follows from explicit rank-at-most-three sentences, not from merely inspecting finite signatures.

No independent scientific audit, external certification, or full survey of inaccessible mathematical literature has been performed.
