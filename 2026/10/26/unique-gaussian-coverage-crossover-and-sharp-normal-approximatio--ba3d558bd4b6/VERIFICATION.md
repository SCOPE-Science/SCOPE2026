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

The analytical proof in `RESULT.md` controls infinite products, the mixture density ratio for all positive arguments, and the uniform \(L^1\) Gaussian expansion. The calculations below provide additional finite checks; they are not independent mathematical certification.

Execute `python VERIFY.py` with Python 3, NumPy and SciPy. The script checks geometric variance weights and exact fourth moments for four reset parameters; verifies the quartic Hermite roots and integrated Gaussian leading constants; evaluates the finite geometric-product characteristic function; and locates interval-coverage sign changes by numerical Fourier inversion. The recorded run printed `PASS: 62 numerical and algebraic checks` and the exact leading constants to twelve decimal places. Its results are archived verbatim in `VERIFY_OUTPUT.txt`.

The truncation error in the numerical characteristic product is small but the numerical integrals are not rigorous interval arithmetic. These checks do not establish the unique crossing on a continuum or the limiting \(O(s_a^{3/2})\) bound; those statements rely on the complete analytical derivation. The theorem is stationary and one-dimensional; external independent audit has not been performed.
