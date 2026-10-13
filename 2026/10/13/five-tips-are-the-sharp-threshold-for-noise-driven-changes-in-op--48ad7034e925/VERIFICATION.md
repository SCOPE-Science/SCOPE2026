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

# Reproducible verification and proof limits

The companion `verify.py` is a standalone Python 3 program requiring SymPy. Run `python verify.py`. Its successful completion prints:

```text
VERIFY_OK five_tip_subsets=5 exact_rational_noise_checks=35 fixed_four_tip_weight_identity=3 cubic_positive_root_interval=(29,30)
```

The checker constructs the exact integer-valued five-tip Brownian covariance matrix \(K\) from the stated branch lengths, then symbolically inverts every \(4\times4\) matrix \(K_S+xI\) for the five ways of omitting one tip. It confirms the formulas for \(L(x)\), \(R(x)\), and \(M(x)\) and factors \(L-R\) and \(R-M\) exactly. It evaluates all five exact-rational information functions at seven nonnegative integer noise variances and checks the predicted strict ordering. It independently verifies the unnormalized GLS weight formula for the general four-tip obstruction.

The result for **all** positive noise strengths follows instead from the analytic polynomial sign argument, the strictly positive denominators, and Descartes' one-positive-root conclusion. The impossibility for every rooted binary ultrametric tree on at most four tips follows from exhaustive root-split case analysis and the positivity argument for three-tip GLS weights; the program does not enumerate an uncountable set of possible branch lengths. Symbolic computations are supporting reproducible evidence, not a replacement for those universal proofs. This file contains no independent-audit result.
