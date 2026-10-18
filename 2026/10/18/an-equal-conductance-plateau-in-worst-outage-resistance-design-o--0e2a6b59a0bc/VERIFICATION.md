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
# Verification of the alternating-price cycle outage theorem

Run the included `verify_robust_cycle.py` with Python 3 and installed NumPy, SciPy, and SymPy:

```sh
python verify_robust_cycle.py
```

Expected output from the checked package: `PASS 2478 independent symbolic/numeric checks`.

The script checks the parity coefficient sums exactly for sizes \(m=2,\ldots,19\), the three closed-form regimes across rational prices, exact budget balance, and the full list of adversarial outage objectives. It separately evaluates Kirchhoff indices through weighted Laplacian eigenvalues on randomly chosen positive conductances, checks many asymmetric feasible competitors, and runs unrestricted numerical optimizers on selected sizes. The reported 2,478 assertions were obtained from the actual program included with this finding.

A separate symbolic check verified the identities \(U_m-V_m=m\), the derivative signs of both branches, the closed forms of both thresholds, and \(\lim_{m\to\infty}m^2(t_+-t_-)=3\).

These finite numerical and symbolic samples do not constitute an exhaustive certification of all sizes, all positive budgets, and all prices. The written analytic proof establishes those quantified statements. Independent external examination has not been performed.
