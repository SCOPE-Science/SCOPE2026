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

The theorem is proved analytically in `RESULT.md`. The accompanying standalone `CHECK.py` uses Python's standard library, constructs \(B_n\) exactly over rational numbers, and computes \(\operatorname{tr}(B_n^k)\) for every \(1\le n\le10\) and \(1\le k\le6\). Its 60 rational traces satisfy the claimed lower bound and a safe rational relaxation of the upper bound using \(\zeta(2)<2\). It also verifies the exact \(k=2\) trace identity and eight binomial moment-coefficient identities. Execute `python CHECK.py`. No external download, secret, service, or optional dependency is required. The finite calculations do not establish the all-dimensional theorem or global bibliographic novelty. Independent mathematical and bibliographic audit have not been performed.
