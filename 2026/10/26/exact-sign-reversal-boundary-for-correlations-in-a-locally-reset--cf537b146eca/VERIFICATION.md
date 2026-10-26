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

# Reproducibility and verification

The analytic proof appears in `RESULT.md`; `check.py` is an independent executable check of its displayed rational identities and geometric convolution. Run `python check.py` using Python 3 and SymPy. The resulting stdout is embedded as `check_output.txt`.

The checker symbolically verifies the rational expression for \(G_1\), the two partial-derivative factorizations, and the \(c=-1\), \(c=0\), and \(c=1\) specializations. It also independently sums rapidly convergent Green-kernel convolutions, compares both calculations on a parameter grid, and verifies the cubic threshold and two exact opposite-sign witnesses. It reported 1,335 subsidiary numeric/rational comparisons and exact symbolic passes.

The positivity arguments for the derivative polynomials, uniqueness of the stationary process, and strict global sign classifications are fully analytic; no finite grid or printed log is used as a proof of those infinitely quantified claims. The file `check_output.txt` is the actual output of the included checker. No independent audit or external certification has been performed.
