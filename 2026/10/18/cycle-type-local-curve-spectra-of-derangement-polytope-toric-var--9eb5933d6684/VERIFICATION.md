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
# Verification details

The standalone standard-library program `checker.py` implements the run-polynomial coefficient formula and two independent finite tests. First, every directed cyclic permutation on every support for each derangement cycle type is enumerated directly through \(n=8\), with a forbidden-arc condition not using inclusion-exclusion. Second, actual derangement permutation pairs are enumerated through \(n=6\), and adjacency is recognized by the one-cycle condition. All coefficient distributions and all global edge counts agree; the output ends with `VERIFY_OK`.

These exhaustive finite tests do not prove the theorem for arbitrary \(n\). The all-parameter proof, including the subtle entire-forbidden-cycle correction, is given in RESULT.md. The smoothness conclusion uses a strict degree-versus-dimension lower bound, not an unverified smoothness converse. Independent audit is not performed.
