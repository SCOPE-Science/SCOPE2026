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

# Verification notes

The main proof is fully analytic. The replay program `verify.py` requires NumPy, as stated in `requirements.txt`. Invoke `python3 verify.py` from the extracted file directory.

The reference program computes the amplitude-damped density matrix using a *different* route from the closed-form block formula: it applies each qubit's two Kraus matrices to the full GHZ density matrix, diagonalizes the result, and evaluates the spectral symmetric-logarithmic-derivative QFI. The program tested 48 random instances for register sizes two through five, checked 1,200 random two-coordinate averaging inequalities for register sizes two through thirteen, compared 2,750 vectors against both exact envelopes, tested uniqueness/bracketing of the ideal-SQL threshold for 38 system sizes, and tested the asymptotic expansion at six sizes. The actual successful replay printed:

`VERIFY_OK 4042 direct_density_QFI 48 majorization 1200 extrema 2750 threshold 38 asymptotics 6`

The experiments are numerical consistency checks with finite precision; they do not certify the all-size proof, global literature priority, realistic measurement achievability, or physical optimization under a different resource constraint. In particular, the \(F=n\) benchmark is the ideal product-probe standard quantum limit, not the optimum of a noisy local-sensor protocol. Independent external audit was not performed.
