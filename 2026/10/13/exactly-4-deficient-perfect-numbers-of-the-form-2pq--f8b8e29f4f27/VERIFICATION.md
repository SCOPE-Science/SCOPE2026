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
The symbolic proof leaves only a finite factorization step: the fifteen possible four-subsets of \(\{1,2,p,q,2p,2q\}\). `classification_certificate.json` records every subset and its constant \(K_E\); `verify.py` regenerates the certificate rather than trusting it.

Replay command:

`python3 verify.py`

Expected successful output begins with `VERIFY_OK` and reports exactly fifteen patterns and the solution set \(\{238,310,322\}\). The computation is exhaustive because, after the symbolic reduction, every solution corresponds to a positive divisor of one of the fifteen explicit integers \(K_E\le39\).

The computation does not prove claims outside the stated squarefree \(2pq\) domain, and no inference is drawn from testing bounded values of \(p\) or \(q\).
