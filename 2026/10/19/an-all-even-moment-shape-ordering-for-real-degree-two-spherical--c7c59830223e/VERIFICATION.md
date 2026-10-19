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

Run `python3 checker.py` with Python 3 and no third-party packages. `checker_output.txt` contains the recorded standard output. The code independently evaluates exact sphere monomial expectations using double factorial moments and compares them with the Gaussian generating-function formula for seven real traceless matrix spectra and all orders \(m=1,\ldots,9\). It checks 10 coefficient polynomial orders, both rational sharp sixth-moment endpoints, and the cubic discriminant identity on all 288 nonzero integer pairs in \([-8,8]^2\); 368 assertion groups passed.

The finite checks are not a proof for all matrices or all exponents. The proof uses an identity of analytic germs near the origin, exact formal power series coefficient extraction, the characteristic discriminant of a real cubic, and positivity of all polynomial coefficients. No third-party independent scientific audit has been performed, and older equivalent formulations are a bibliographic risk.
