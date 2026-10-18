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

The standalone `verify.py` uses only Python 3 standard-library features. Run `python3 verify.py` from this directory.

The checker computes inverses of all three pencil matrices over each displayed finite prime field, reconstructs chirp coefficients, sums the Fourier symbol directly, and compares its *exact cyclotomic class* with equation (1) of the proof. The explicit tests cover \((p,d)=(3,2),(3,3),(5,2),(7,2),(11,2)\), for which the computed ranks are respectively \(1,3,25,49,121\). Thus the rank-one ternary example and the invertible prime-five, seven and eleven examples are confirmed without numerical tolerance. A separate exhaustive count of all quadratic-form values checks the stated multiplicity formulas for 52 diagonal forms over the same prime choices, including degenerate forms and even/odd ranks.

The expected output has two `VERIFY_OK` lines, one for the exact Fourier coefficient tests and one for the level-set counts. The script's `assert` statements are the actual checks; there is no external solver or downloaded dependency.

The code tests only the displayed finite instances and diagonal test forms. It does not exhaust arbitrary dimensions, arbitrary symmetric pencils, or all primes; the proof in `RESULT.md` gives the unrestricted result. Complex singular-value assertions use the analytical absolute-value identity rather than a floating-point singular-value decomposition. No independent mathematical audit has been performed.
