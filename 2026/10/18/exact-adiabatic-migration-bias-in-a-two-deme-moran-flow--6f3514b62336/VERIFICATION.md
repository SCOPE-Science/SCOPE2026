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

# Verification and reproducibility

The `verify.py` program operates on the equations displayed in `RESULT.md`. Run with Python and installed `sympy`, `numpy`, and `scipy`:

```sh
python verify.py
```

The run performed for this package passed exact symbolic checks of the two stationary polynomial numerators, their factorized sum, the Jacobian at the isolated-deme equilibrium, the analytic interior equilibrium branch, and the small-amplitude bias coefficient. Direct constant-migration equilibria and two finite-period forced simulations were also checked. The numerical examples use \(q=0.05\), periods \(T=100\) and \(T=400\), and report period means approximately \(0.513031239651\) and \(0.512992746477\), converging toward the proved adiabatic target \(0.512989176043\). The equal-mean constant-flow comparison is approximately \(0.512820512821\).

The script does **not** certify all parameter ranges, convergence for every initial state, or the infinite-time/adiabatic assertion by sampling. Those assertions follow from the invariant-rectangle contraction and tracking argument in the proof. No external independent audit has been performed.
