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
# Verification

The proof in `RESULT.md` is based on exact identities: polynomial modulus equality implies conjugate-reflection identities for the rational quotient; the quotient is fixed by a primitive rotation, hence lies in the invariant field \(\mathbb C(z^q)\); conjugation pairs the zeros and poles of its one-variable rational factor; divisibility yields the closed integer intervals. These are arguments for every degree and denominator, not extrapolations from computations.

Use Python 3.10+ with NumPy (`requirements.txt`) and run `python verify.py`. The saved `verification_output.txt` contains a reproducible execution for 16 finite configurations, including exhaustive reflected-zero flips for \(q=2,3,4,5\), orbit multiplicities, and a generic orbit-free polynomial. Numerical thresholds are specified in the code. The checker verifies expected finite counts but neither exhausts all polynomials nor formally certifies the general theorem. The degree bound and its attaining family follow directly from the proof, not from finite tests.

For each claimed sample-equivalence, the polynomial in the real sample parameter has degree at most \(2d\); the finite-sample sufficiency therefore rests on the elementary interpolation zero-count principle. No minimality or robustness theorem is checked or claimed. Independent audit has not been performed.
