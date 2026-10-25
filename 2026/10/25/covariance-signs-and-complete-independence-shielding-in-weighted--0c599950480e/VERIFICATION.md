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
# Verification and proof limits

The attached `verify_theta.py` is a standalone Python 3 checker using only `fractions` and `itertools`. Execute from the directory containing the script:

```sh
python3 verify_theta.py
```

Observed output: `VERIFIED 2102 exact equalities for 9 finite network cases`.

For each stated finite example, the verifier enumerates all independent edge-indicator assignments with exact rational probability, calculates every vertex degree, retains exactly even-degree configurations, and compares their normalized probabilities to the claimed path laws. It also enumerates every marginal subset and calculates each pair covariance independently of the analytic expression. Cases include five- and six-path networks, mixtures of unequal edge probabilities, the central homogeneous point, both sides of the sign transition, and balancing of an entire path despite having no fair individual edge on that path. All arithmetic and equalities are exact fractions.

The exhaustive check is finite and does **not** establish the theorem for arbitrary graph sizes or irrational probabilities. General validity depends on the explicit even-parity reduction and conditional-odds proof in the result text. No independent external audit, computational proof assistant, or infinite-size certification was performed.
