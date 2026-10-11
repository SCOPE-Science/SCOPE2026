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

The proof in `RESULT.md` gives the exact event equivalence, the generating rays of the spherical triangle, the use of the established solid-angle formula, and the sharp inequalities. The symbolic determinant computation for the rays yielded \(-2abc\); their pairwise scalar products were verified as \(bc\), \(ab\), and \(ac\), and their squared norms as \(a^2+b^2\), \(a^2+c^2\), and \(b^2+c^2\).

The accompanying executable `verify_probability.py` was run under Python 3 with deterministic pseudorandom seed `20261009` and concluded `VERIFY_OK`. It compared 400 numerical evaluations against independently calculated Girard spherical excess; checked 720,000 Gaussian-distributed directions for four box shapes; checked the cube equality against its existing trigonometric form; and tested the denominator bound and scale invariance for 200 additional triples. Numerical checks are finite and do not certify all real input triples, the novelty assertion, or publication precedence.

Reproduce using `python3 verify_probability.py`. The precise model is uniform orientation of the central plane, not uniform intercept distance. Boundaries corresponding to planes through box vertices have spherical measure zero. Only same-model mathematical review is recorded here; independent audit has not been performed.
