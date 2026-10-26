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

The analytic derivation is in `RESULT.md`. Running `python verify_hamming.py` with Python 3, NumPy and SciPy independently builds full two-particle generators and solves the corresponding Poisson systems, rather than only reusing the radial finite-sum formula. Nine configuration-space checks passed at \((q,d)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2),(4,3),(5,2)\); in each case mean rate and Fano ratio agree with exact fractions to better than \(2\times10^{-11}\). Nine asymptotic normalized ratios, at each \(q=2,3,4\) and \(d=20,50,100\), approach the predicted limit one. All these checks were executed successfully. They are numerical corroboration only: infinite-dimensional asymptotics and arbitrary alphabet-size quantifiers rest on the stated proof, not enumeration. Independent audit has not been performed.
