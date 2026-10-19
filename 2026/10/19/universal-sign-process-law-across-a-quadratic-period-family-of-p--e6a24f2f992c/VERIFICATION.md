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

# Reproducibility and limits

The analytic proof uses the exact identity \(A_+^n=-I\), the Chebyshev-sine recurrence for the switching ray, and the published rotation number \( (n-1)/n^2 \). Its cyclic-overlap calculation is exact for every integer \(n\ge3\) and every lag. The claim holds for boundary-free invariant Borel probabilities, not for arbitrary noninvariant initial distributions.

From a directory containing the embedded `check.py`, run `python check.py` with Python, SymPy and mpmath installed. Actual execution returned `VERIFY_OK`. It checks algebraic branch matrices at four small parameter values; modular interval overlaps for all \(3\le n<150\) and all lags; and high-precision orbit/sector geometry for \(3\le n\le10\). This finite set of checks is corroboration, not proof of the infinitely quantified theorem.

Earlier work establishes the family and its rotation number; the precise all-time statistical law is proved in the accompanying result. Bibliographic priority and independent mathematical audit remain outstanding. No independent audit evidence is claimed.
