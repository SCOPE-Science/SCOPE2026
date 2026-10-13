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

# Reproducibility and scope

Use the exact CSV codeword list `code_triples.csv`, and run `python3 verify.py` in the same directory. The verifier uses the standard library only. It checks:

1. Exactly \(37\) valid distinct triples in the CSV, corresponding to length-\(15\), weight-\(3\) binary words.
2. Both deletion-output implementations agree for all \(\binom{15}{3}=455\) possible input words.
3. The \(37\) codewords have pairwise disjoint sets of one-deletion outputs.
4. The assigned nonnegative output weights sum to \(37\); every one of the \(455\) candidate inputs is covered to weight at least \(1\).
5. Each of the \(13\) modified-VT checksum cells of this layer has exactly \(35\) words.

The expected terminal result begins `VERIFY_OK N=15 W=3 candidates=455 selected=37 dual_weight=37`. The upper bound is also proved structurally by run cases in `RESULT.md`; the finite verifier is additional exact redundancy. No infinite domain is claimed; the exhaustive check covers all \(455\) candidates. No independent validation or audit is claimed.
