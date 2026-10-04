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

The arbitrary-\(n\) theorem is proved symbolically in `RESULT.md`. The proof does not infer an infinite statement from finite experiments.

The packaged `artifacts/verify.py` independently enumerates every order-preserving self-map for the cases \(n=1,2,3\). For each model it checks the exact number of maps and homeomorphisms, verifies that every proper image has a singleton occupied level, beat-reduces every distinct proper image to one point, and confirms directly that each homeomorphism is incomparable with every other self-map in the finite function poset.

The replay output is stored in `artifacts/verification_output.txt`. It reports \(36\), \(446\), and \(6080\) self-maps and \(5\), \(9\), and \(17\) homotopy classes for \(n=1,2,3\), followed by `VERIFY_OK`.

The computation does not test all \(n\), does not classify higher homotopy groups of the mapping spaces, and does not establish bibliographic novelty.
