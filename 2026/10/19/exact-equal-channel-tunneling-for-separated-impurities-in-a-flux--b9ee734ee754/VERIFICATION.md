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

The self-contained `VERIFY.py` script requires Python 3, NumPy and SymPy and is run with `python VERIFY.py` from this directory. It builds the physical diamond-chain Hermitian hopping matrix from its four link amplitudes rather than from the claimed eigenvalue formula, constructs compact localized states independently, and checks their annihilation and overlap. A symbolic four-coordinate calculation factors the characteristic polynomial exactly. Six finite-section compressed spectra and twelve full physical finite-chain weak-impurity spectra were checked numerically, and the quarter-flux coupling ratio was reproduced as approximately 0.171572875254.

These finite diagnostics test normalization, gauge, index separation and perturbative slopes. The infinite-volume and all-integer-separation claims rest on the algebraic recurrence and rank-four determinant proof in `RESULT.md`; diagnostics are not substituted for a proof. The expansion applies with flux strictly between zero and pi and fixed positive hopping and separation. Source priority is not independently certified; a plausibly relevant 2024 thesis was only indexed, not completely read.
