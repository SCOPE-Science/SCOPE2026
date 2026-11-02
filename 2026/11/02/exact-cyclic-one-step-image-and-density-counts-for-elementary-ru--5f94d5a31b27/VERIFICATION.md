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

From the package directory, `python verify.py` checks all indexed binary input rings at each length from 1 through 18 and compares the resulting distinct images against the independent alternating-gap recognition test, weight distribution and a constructive predecessor for every reachable output. It also compares the fixed-weight binomial formula and a separately computed integer logarithmic-derivative series through length 70. The recorded run ended in `VERIFY_OK`.

The checker is a finite cross-check, not a proof for unbounded ring lengths. The all-length proof in RESULT.md is purely combinatorial: pair endpoints of zero runs, reverse the construction, then count the resulting cyclic gap vectors and their intersection. No outside code, network service, or unpublished data are required to replay it.

Independent mathematical audit has not been performed. Historical novelty is assessed against the primary accessible literature and published-claim searches with the stated residual access risk.
