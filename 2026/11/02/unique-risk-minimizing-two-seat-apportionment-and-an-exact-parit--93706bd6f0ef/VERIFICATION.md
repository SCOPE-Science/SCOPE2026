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

Run `python verify.py` with Python 3 and its standard library. For \(3\le n\le100\) the verifier uses exact fractions to reconstruct the proposed lotteries and checks normalization, each \(2/n\) marginal, the pairwise inversion formula, the exact optimum-variance and three-point risk distribution, the sharp central-party lower-bound inequality, and the uniform anonymous variance.

If NumPy and SciPy are installed, run `python verify.py --lp` to add an independently formulated finite linear-programming benchmark for \(3\le n\le18\). The tested LP constrains each party's marginal to \(2/n\) and minimizes the exact pair cost \((i+j-(n+1))^2\) using SciPy/HiGHS; numerical objective comparisons use tolerance \(10^{-8}\). Both commands executed successfully in the reported environment. The executable file `verify.py` is included alongside this text in the package.

The analytic proof in RESULT.md proves global correctness for every integer \(n\ge3\), including uniqueness, without relying on finite enumeration or floating-point optimization. A feasibility check and a numerical solver output alone would not prove uniqueness or an all-population optimum. The proof assumes the fixed arbitrary label convention at equal quotas; there is no assertion about alternate tie conventions or other residual-seat counts.
