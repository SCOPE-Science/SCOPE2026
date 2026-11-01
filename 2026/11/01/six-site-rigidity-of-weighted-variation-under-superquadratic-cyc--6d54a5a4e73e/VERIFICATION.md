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
# Reproduction and boundaries
Run `python verification/check_cycle_pheat.py` with a standard Python interpreter. It requires no third-party packages and performs exact-rational checks. It tests 48,530 zero-sum integer gradients for \(p=3\), enumerates all sign chambers for the five-cycle and six-cycle examples, and confirms an explicit six-cycle short-time-growth coefficient. The formal proof for every length and every real \(p>2\) is in `RESULT.md`; finitely many computations do not prove the infinite quantifiers. The five-cycle finite sign enumeration is exhaustive because the optimization within each sign chamber is solved analytically. No external or independent audit has been performed.
