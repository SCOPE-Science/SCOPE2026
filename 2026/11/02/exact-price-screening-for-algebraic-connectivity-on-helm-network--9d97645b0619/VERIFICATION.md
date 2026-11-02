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

# Reproducibility and scope

Run `python VERIFY.py` with Python 3, NumPy, SciPy and SymPy; compare standard output with `VERIFY_OUTPUT.txt`. The verifier was executed on the embedded source before packaging, with all checks passing: two exact symbolic block determinants, two exact rational threshold designs, 84 full-matrix eigenvalue/budget cases and 48 asymmetric random-start nonlinear search comparisons. The finite search is deliberately only a counterexample stress test; the proof of the unrestricted optimum for all sizes comes from concavity, symmetry averaging, Fourier decomposition and the exact normalized-price inequalities in `RESULT.md`.

For the rational boundary case with six rim vertices, both \((x,y,z)=(3,0,2)\) and \((3/19,54/19,2)\) cost exactly 30 and have \(\lambda_2=1\). No independent audit or external formal certification has been performed.
