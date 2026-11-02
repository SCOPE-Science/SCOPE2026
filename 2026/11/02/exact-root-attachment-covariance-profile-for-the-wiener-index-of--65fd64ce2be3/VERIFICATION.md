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

# Verification record

Run `python3 verify.py` from the folder containing the extracted artifacts. No nonstandard packages or network access are required.

The checker enumerates all \((n-1)!\) recursive trees for each size \(n=2,\ldots,8\): exactly \(5913\) trees. It constructs each undirected tree and computes graph distances without relying on the proposed Wiener recurrence, then checks the local covariance for all \(28\) admissible \((n,j)\) pairs with exact fractions. It separately checks the finite-sum formula against the closed covariance formula for every \(n=2,\ldots,150\), also using exact fractions. Observed result: `PASS: 5913 recursive trees exhaustively enumerated (sizes 2..8), 28 exact local covariance checks; 149 exact symbolic-sum comparisons (sizes 2..150).`

The proof for all \(n\) is the conditional-growth argument and elementary strict harmonic-ratio inequality in `RESULT.md`. Enumeration beyond \(n=8\) was not performed and is not claimed. External independent audit remains unperformed.
