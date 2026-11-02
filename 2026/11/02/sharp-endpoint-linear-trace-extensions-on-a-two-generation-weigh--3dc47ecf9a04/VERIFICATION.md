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

# Reproduction and proof boundaries

The theorem concerns real vertex functions modulo constants on the stated seven-vertex tree. Every positive root-edge weight is included. The proof identifies gradients with weighted \(\ell_1^6\), then symmetrizes all right inverses, determines the only free parameter, evaluates all six weighted columns, and minimizes their maximum over every real parameter. The sharp interior peak is established by direct differentiation. These are exhaustive analytic arguments, unlike finite tests.

Run `python verify_tv_h2.py` in Python 3 with no additional packages. Expected result: `PASS 2200 exact rational column/optimization comparisons`, including the endpoint tests shown in its output. The script constructs six extended gradient columns from the explicit extension and checks their weighted \(\ell_1\) norm against the theorem for rational weights and candidates.

For an additional nonsymmetric consistency check, install NumPy and SciPy, then run `python verify_tv_h2_lp.py`. The separate linear program minimizes the operator norm over twelve arbitrary internal linear coefficients and tests ten selected positive weight ratios. The solver's numerical agreement is not a certificate for all real parameters and is not a replacement for symmetrization.

The archived source evidence compares the endpoint claim with a known \(1<p<\infty\) theorem and other kinds of trace right inverses; it cannot rule out every unindexed equivalent weighted-projection calculation. No independent audit has been performed.
