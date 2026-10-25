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

Run the included `verify.py` with Python 3. It uses only standard-library integer arithmetic, exact `fractions.Fraction`, and combinatorial enumeration. The checker recomputes utility-improving swaps for every coloring and then independently forms the integration polynomial by compositions. The measured outputs were:

```
PASS: 55 (n,b) parameters; 35103 labeled-vertex colorings independently tested
PASS: exact equilibrium count, complete integration polynomial, contiguous spectrum
```

Coverage is all integer \(n\) from \(3\) through \(15\) and all \(1\le b\le\lfloor n/2\rfloor\). The implementation does **not** establish the infinite family; the structural proof and run bijection in `RESULT.md` do. The proof makes no stochastic or numerical approximation assumptions. Only a self-review has been conducted; independent audit and independent validation remain unperformed.
