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

# Exact finite verification

Run `python3 verify.py` in an environment providing Python 3 standard-library arithmetic. Successful execution ends with `VERIFY_OK` and prints exact integer dictionaries for the three representative exponents.

The proof-critical coverage invariant is that the generator `all_rref_lines` traverses each reduced-echelon two-dimensional subspace of \(\mathbb F_{13}^4\) exactly once. For each of the \(31110\) generated subspaces the code tests all \(14\) projective points. The independent secant-pair algorithm enumerates all \(14028\) pairs of distinct columns and deduces line sizes from exact triangular-number inversion; its multisets agree with the direct line census.

For each representative the script independently enumerates all \(28561\) four-coordinate messages, confirming the previously published Hamming weight spectrum. It tests projective point distinctness, aggregate incidence identities, and the explicit Frobenius equivalence with the negative-exponent representative. No probabilistic sampling, floating-point arithmetic, external mathematical databases, or conditional unproved search is used.

The completed calculation establishes the three finite \(q=13\) cases and, with the algebraic reductions in the proof, the full parameter classification at this alphabet. It does not establish an asymptotic result for all odd \(q\) or independently certify priority in the literature.
