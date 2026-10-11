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
# Verification and limits

The main proof is analytic. Explicitly expand the cubic vector kernel of the quartic interaction; the antipodal first and cubic odd moments vanish. Verify the equality between the resulting force field and the stated covariance-operator expression. Spectrally decompose the positive-definite symmetric covariance operator and trace every eigenspace identity to recover each radial and weighted-frame equality. Substitute the candidate blocks back into the exact force, then integrate the scalar quartic oscillator using its conserved energy. A square Parseval matrix establishes rigidity at the minimal pair count.

A reproducible standalone computation is provided in `checker.py`. With Python 3 and installed `sympy`, `numpy`, `scipy`, and `mpmath`, run `python checker.py` in the directory containing the file. The script explicitly evaluates full-force sums with exact radicals for 201 finite cross-polytope configurations and one non-cospherical tight-frame assembly, then compares the analytic beta quarter-period with numerical integration to the first zero. These are finite consistency checks, not exhaustive proofs for arbitrary dimension, arbitrary positive masses, or every frame. The analytic proof supplies those quantifiers.

No computer algebra package is required to follow the theoretical proof. Source access and novelty limitations are described in the associated relationship and review sections; independent scientific validation has not been performed.
