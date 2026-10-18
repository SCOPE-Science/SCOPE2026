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

Run `python verify.py` under standard Python 3. The program uses only the Python standard library, builds full directed generators, computes strongly connected components directly, and tests proposed class labels and product-form stationary balance with exact `Fraction` weights. It then compares direct signed transition flux to the coefficient-ratio formula.

Observed output: `PASS: 186 finite generators, 28413 states examined, 3444 class balances and exact current identities`.

The generator checks only finite sizes \(2\le N\le4\), \(N<L\le10\) and \(1\le I\le3\), in right-only, left-only and asymmetric two-sided regimes. The proof in `RESULT.md` establishes the unrestricted finite-ring result independently of these tests. No independent audit has been performed.
