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

The source `verify_hamming_fixed.py` uses Python 3 standard library and reconstructs the Hamming graph and its actual total two-cut faces from pairs of words at Hamming distance at least two. The directly enumerated fixed-orbit complex is compared to the exact histogram criterion and to the combinatorial Alexander dual consisting of the \(q\) constant histograms. Test dimensions and alphabet sizes: \((2,2),(3,2),(4,2),(5,2),(6,2),(2,3),(3,3),(4,3),(2,4),(3,4),(2,5)\). There are **1,116,429** face comparisons, plus mod-two boundary-rank checks for the tractable examples and **46** signed Lefschetz trace comparisons across alphabet permutations. All passed, ending with `ALL_OK`.

Run `python3 verify_hamming_fixed.py` from the unpacked package to replay. The infinite-parameter claim rests on the orbit/nonedge equivalence, simplicial join model, suspension argument, and the signed **integral** Alexander-dual cochain isomorphism in `RESULT.md`; finite verification cannot certify an infinite theorem. Integral module correctness is proved by natural integral duality, not by the finite mod-two computations. Independent audit has not been performed.
