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

# Verification record

The standalone script `verification.py` was run using Python with SymPy, NumPy and SciPy: `VERIFY_OK 3343 checks`.

It checks rational transition matrices and their eigenvalues for \(2\le k\le9\), \(2\le m\le12\), independently solves the two-parameter invariant linear program, checks exact samples at both sharp transition regimes, and evaluates 700 non-invariant random kernels against the proposed optimum. The independent-set leaf eigenvalue and core-face results for arbitrary sizes are established analytically in `RESULT.md`, not by these tests.

For a symbolic replay, install the requirements listed in `requirements.txt` and run `python verification.py` from a folder containing both files. The pseudorandom test seed is fixed in the script. Numerical comparisons use explicitly stated small tolerances, while finite exact-rational comparisons use SymPy. The computations are finite checks and not independent mathematical certification.
