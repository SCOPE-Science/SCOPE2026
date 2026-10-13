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

# Computational verification and proof boundary

Run the standalone standard-library program `python verify.py` to enumerate the nonzero maximal-ideal vectors and verify the complete degree multiset, as well as the count of self-orthogonal vectors. The final line of a successful execution is `VERIFY_OK`. The enumerated cases comprise \(13\) combinations of prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), form dimensions \(2,3,4\), and diagonal or hyperbolic representatives; both similarity types for the even-dimensional cases are covered. All cases passed when executed from the packaged code.

The script uses exact modular arithmetic without external dependencies. It enumerates finite examples only; it does not establish the infinitely many finite-field or dimension cases. The general classification follows from the proof in RESULT.md: maximal-ideal multiplication, symplectic/orthogonal similarity classification of nondegenerate symmetric forms over finite fields, and the explicit finite-field quadratic-form zero counts.

Independent audit: not performed.
