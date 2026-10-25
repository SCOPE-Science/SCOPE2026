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

# Analytical and reproducibility verification

The general proof is in `RESULT.md`. Its decisive steps are the normalized outer \(H^2\) root, the Schwarz–Pick and Parseval inequalities, strict unimodality of the scalar quotient for every \(q>2\), and the equality cases in Schwarz–Pick, Parseval, and the triangle inequality. These are analytical arguments for all admissible parameters, not deductions from sampled inputs.

The standalone artifact `verify.py` uses Python's standard library. Execute `python verify.py` from the directory containing the embedded files. An actual execution returned `CHECK_OK: 80 analytic-parameter grids, 25 exact rational monotonicity certificates, endpoint tests`. It checked the stationarity equation, nonnegative optimizer and range, exhibited first derivative, parameter monotonicity on grids, exact \(\mathbb Q\)-arithmetic evaluation of the polynomial identity at twenty-five parameter pairs, and endpoint asymptotic coefficients. No external package, file, network data, or previously generated logs are required.

The rational identities do not by themselves prove completeness of any parameter domain. The global conclusions instead follow from the strict polynomial derivative sign and equality conditions as documented in the proof. Historical priority and independent scientific validation are not certified by the checker.
