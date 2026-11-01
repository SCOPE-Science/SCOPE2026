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

# Reproducibility and scope

Run `python verify_matching_effects.py` in an environment containing NumPy. The actual run returned `VERIFICATION_OK`. For each even \(n\in\{4,6,8,10\}\), the checker exhaustively enumerated all perfect matchings relative to a fixed matching, checked exact integer commutator equality and the alternating-cycle commuting criterion, and compared all complex eigenvalues from independent numerical Hermitian diagonalization with the claimed sine multiset. At \(n=12\), it exhaustively checked exact integer commutators and matching-class counts without numeric diagonalization. The enumeration totals are \(3,15,105,945,10395\); commuting-partner counts are \(3,7,25,81,331\), and sharp-maximizer counts are \(0,0,48,240,2160\). For each dimension, direct numerical frame sums also matched the orthogonal projection onto the mean-zero subspace.

The proof of arbitrary-even-dimensional correctness is in `RESULT.md`: the Parseval second-moment identity, matching involution compression, unitary product cycle decomposition, and exponential generating function are independent analytic arguments. Finite tests do not constitute an exhaustive test of infinitely many dimensions, and tolerance-based eigenvalue comparisons do not constitute exact algebraic proofs. The eigenvalue formula has not been externally certified.
