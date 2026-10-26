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

# Verification instructions

The `check_smoothness.py` program checks the complete coefficient domain of 728 nonzero sextuples over \(\mathbf F_3\) by exact Gröbner-basis computations. This checks the Jacobian criterion geometrically on each affine chart, rather than testing finitely many extension-field points. It also compares every outcome with the explicit smoothness criterion in the proof. It requires Python 3 and SymPy.

The independent `check_zeta.py` program uses only Python 3 standard-library finite-field arithmetic to count points over \(\mathbf F_3\), \(\mathbf F_9\), and \(\mathbf F_{27}\) for each of the 32 smooth coefficient vectors. It derives a degree-six Weil polynomial for each by Newton identities plus the genus-three functional equation and compares against the exact expected three-profile census. It does not use the Gröbner-basis package or read the first program's output.

Run:

```sh
python check_smoothness.py
python check_zeta.py
```

`verification_output.txt` records the successful observed output. `smooth_coefficients.json` lists all 16 coefficient vectors modulo scalar. The proof also gives exact linear-algebra and elliptic-quotient derivations; the finite computations are cross-checks, not a replacement for those steps.

No classification of other quartic families or non-split involution structures is claimed. No independent external mathematical audit has been performed.
