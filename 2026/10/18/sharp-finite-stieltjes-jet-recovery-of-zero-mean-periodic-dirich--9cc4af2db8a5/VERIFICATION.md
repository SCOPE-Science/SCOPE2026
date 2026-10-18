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
# Verification and reproduction

The attached `verify.py` requires Python 3 and `mpmath` (tested at high arbitrary precision). Run `python verify.py` in a directory containing the file. The script checks the exact analytic formula for the Stieltjes-jet entries through evaluations of shifted generalized Stieltjes constants, strict positivity of the determinant in eight parameter cases, orientations of eight real sample-value determinant matrices, reconstruction of known coefficient vectors by linear solves, and one nontrivial sharp three-zero interpolation for period five. The recorded output is `verification_output.txt`.

The universal assertions do not follow from those tests. They follow from the explicit factorization, Mellin integral, Andréief determinant identity, and elementary generalized-Rolle argument presented in `RESULT.md`. No interval-arithmetic rounding enclosure or independent external audit is claimed. Very large periods or extreme shifts may be ill-conditioned; the code tests invertibility only on the displayed finite cases.
