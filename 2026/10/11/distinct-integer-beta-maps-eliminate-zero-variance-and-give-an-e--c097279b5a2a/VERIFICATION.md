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

# Reproducibility and proof verification

The analytical argument in `RESULT.md` supplies the quantified proof; finite computation is not treated as proof of a universal dynamical statement. In particular, the transfer-operator variation bound and the Fourier common-composition lemma are the two nonstandard steps needed for strict positivity. The one-sided derivative is obtained by differentiating a uniformly convergent operator resolvent, and all boundary restrictions appear in the theorem.

The embedded file `checks/variance_fourier.py` requires only Python 3 standard-library `fractions`. Invoke `python3 checks/variance_fourier.py`. It evaluates exactly (with rational arithmetic) finitely supported cosine coefficients under inverse transfer operators and compares stationary norm-difference variance with independent arithmetic formulas. It tests positive-noise probabilities, pure-map endpoints, divisible slopes, resonant powers and the first-order coefficient for additional trigonometric coboundaries. The expected final marker is `CHECK_OK`; it does not validate the entire infinite-dimensional proof or priority claim.

Independent audit has not been performed. No external certification, formal proof assistant, or nonpublic source is asserted.
