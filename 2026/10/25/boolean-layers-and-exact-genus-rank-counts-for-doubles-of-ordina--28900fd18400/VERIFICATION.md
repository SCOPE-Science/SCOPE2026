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

# Reproduction and limits

Run `python3 verify.py` using Python 3 without third-party packages, in the directory with the proof. The verifier independently reconstructs additive closure and gap statistics, checks membership through 300 or beyond in 2,794 triples for integer \(m=2,\ldots,8\), tests 216 cofinite odd masks directly for \(m=2,3,4,5\), and independently counts genus–relative-rank layers. Observed terminal markers: `PARAMETER_CASES_OK 2794`, `BRUTE_CASES_OK 216`, `JOINT_CENSUS_OK`, and `VERIFY_OK`.

The universal claim is proved symbolically in `RESULT.md`: parity fixes the even part, one odd element forces a tail, and closure places no constraints on intermediate odd positions; their indispensability and gap count yield every displayed formula. Bounded masks are not an exhaustive infinite proof, nor do they establish originality. General all-divisor/all-target fixed-quotient generation, rank-one results, the maximum-member framework, and the minimum genus alone are prior known and explicitly credited. No independent audit or independent certification has been performed.
