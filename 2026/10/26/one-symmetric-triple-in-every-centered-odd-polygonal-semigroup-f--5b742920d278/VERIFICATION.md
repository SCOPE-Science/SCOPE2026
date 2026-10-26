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

# Reproduction instructions

Run `python verify.py` in Python 3. The program needs only the Python standard library. It independently checks every possible three-generator gluing orientation for all odd orders \(3\le k\le101\) and all \(k\le n\le k+150\), totaling 7,550 exact test cases. It checks the stated exceptional index, verifies the gluing identity, computes Apéry sets with an independent shortest-path algorithm for ten positive and five negative examples, and checks the Frobenius polynomial and genus.

These computations are finite, so they do not establish the theorem for arbitrarily large \(k,n\). The universal classification depends on the modular, inequality and gluing proof recorded in RESULT.md. Independent mathematical auditing has not been performed.
