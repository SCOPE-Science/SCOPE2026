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

The theorem is proved using only explicit Weierstrass division, parameter regularity, and Koszul syzygies. The full ring-theoretic argument is given in `RESULT.md`.

Run `python3 verify.py` to recompute the lengths of truncated Koszul images by exact row reduction over the prime field of order \(32003\). It evaluates parameter pairs \((3,7),(3,8),(4,9),(4,10),(5,11)\) and checks the predicted one-unit difference. It prints `VERIFY_OK` on success. These are five finite sanity checks; the independent infinite-family proof is symbolic.

The code has no third-party dependencies. Historical literature priority remains subject to independent verification; an independent mathematical audit is not performed.
