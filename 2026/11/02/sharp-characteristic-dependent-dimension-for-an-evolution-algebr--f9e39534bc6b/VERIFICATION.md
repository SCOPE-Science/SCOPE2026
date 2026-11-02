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

The symbolic proof treats every infinite field, including non-algebraically closed fields. The standalone checker uses exact arithmetic and no external dependencies. It exhaustively tests invertible matrices over two small prime fields against the given multiplication tables, tests rational rotation bases, and checks the characteristic-two basis-polynomial identities coefficientwise. Recorded counts are \(6\) matrices and \(1\) automorphism in dimension two over \(\mathbb F_2\), \(168\) and \(1\) in dimension three over \(\mathbb F_2\), and \(11{,}232\) and \(1\) in dimension three over \(\mathbb F_3\). See `verify_natural_basis.py` and `verification_output.txt`.

Finite-field enumeration does not prove the theorem over infinite fields and cannot certify originality. The all-field automorphism calculations, natural-family construction, and minimality follow from the explicit algebraic argument in `RESULT.md`. An independent mathematical audit has not been carried out.
