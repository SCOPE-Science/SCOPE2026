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

# Verification and limits

The symbolic proof is complete under the cited Ren–Chen and Ljunggren results. The standalone `verify.py` uses Python standard-library exact arithmetic and performs finite regression checks: 60 parameterized known two-prime near-perfect cases for \(p\le16\), \(t\le18\); it finds the single long-repdigit representation \((3,1,4,40)\), checks \(\sigma(40)=90\), and checks the inequalities for \(2\le s\le19\). Exhaustion is only over these parameter ranges. The unbounded conclusion follows from the written parity, factorization, valuation and size proof, not from computation. Independent audit has not been performed.
