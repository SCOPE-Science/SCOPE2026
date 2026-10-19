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

# Reproducibility and verification limits

The companion `verify.py` implements explicit ring multiplication with a symmetric bilinear form, computes annihilators by scanning all ring elements, and checks every unordered pair of nonzero zero-divisors against the theorem's adjacency criterion. It independently computes radical dimension, projective-class multiplicities and vertex degrees. The tests include nine split examples over prime fields and two mixed-characteristic examples.

Run from the directory containing `verify.py` with `python3 verify.py`. Expected terminal marker: `ALL_TESTS_PASS: 11 exact ring configurations`.

A separate mathematical argument establishes the general theorem for all residue prime powers, all allowed dimensions, and rings without a coefficient field. Finite tests do not certify infinitely many rings, prove ring nonisomorphism, or establish novelty. The two example rings are distinguished in the proof by the existence of a nonsocle square-zero element.

Independent mathematical audit: not performed.
