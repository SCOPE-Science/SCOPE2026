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

# Mathematical verification and reproducibility

Run `python verify.py` from the directory containing that standalone file, using Python 3 with only its standard library. The packaged program computes the finite subset expansion using exact rational arithmetic and checks it against a separately assembled exponential-race mixture for 144 positive two-rate pairs. It verifies rate-scale and label-permutation invariances, the identity \(\tau=1/(2n-1)\) for five homogeneous sample sizes, and 51 additional heterogeneous rate vectors. Three fixed exact heterogeneous reference fractions and three fixed-seed stochastic diagnostics supply additional cross-checks. Expected output: `VERIFY_OK two_rate=144 symmetric=5 multirate=51 known_values=3 mc=3`.

The infinite-dimensional quantifiers over every integer \(n\ge2\), every positive real rate vector, and every admissible baseline are justified by the finite algebraic derivation in RESULT.md, not the finite scripts. The optimal sensitivity inequalities and the inverse formula are derived from explicit scalar calculus. The Monte Carlo tests use a fixed seed and tolerance; statistical agreement is not proof. Floating-point numerical stability for large rate lists, sensitivity to censoring, statistical estimation, and independence of scientific review have not been established.
