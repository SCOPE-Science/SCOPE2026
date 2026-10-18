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

Run `python3 verify.py` in an ordinary Python 3 environment. The checker uses standard-library `fractions.Fraction` for exact numerical tests. It enumerates all binary words of lengths one through eight in four independently chosen contraction-parameter regimes (strictly disjoint fiber images, overlapping fiber images, touching images and asymmetric overlap), tests exact nondyadic coding, tests all first-symbol-difference pairs and checks the maximum-norm branch-Lipschitz constant. Observed result: `VERIFY_OK`.

The mathematical proof is independent of finite enumeration: the angular doubling identity supplies all words, the first differing fiber-map gap is a minimum of endpoint values of an affine function, and branch contractions yield the symbolic-cell upper bound for all integers \(n\ge2\). The program is finite corroboration, not proof of the all-parameter or asymptotic result. In particular, topological entropy here uses the forward-admissible domain and does not assert dynamical entropy on the attractor.
