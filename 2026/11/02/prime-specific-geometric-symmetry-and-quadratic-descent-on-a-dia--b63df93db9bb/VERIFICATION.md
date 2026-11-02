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

# Exact computational verification

The accompanying `verify.py` requires only Python 3's standard library; run `python3 verify.py`. Its successful output is retained verbatim in `verification_output.txt` and ends with `VERIFY_OK`.

The program computes the unique primitive integer Möbius interpolation vector for each of the 120 permutations of the five discriminant parameters, using signed maximal minors of a three-row matrix. It checks that only identity and reversal satisfy both remaining interpolation equations integrally and that the support of all nonzero residual gcds is exactly \(\{2,3,5,7,11,13\}\). Accordingly, no untested prime above thirteen can introduce an additional point-stabilizing Möbius map. At the three exceptional primes it evaluates all admissible permutations, their exact finite orders, nonzero denominator residues, and Legendre-symbol lift conditions; it also tests a longer list of ordinary primes. The scalar-square identity for quadratic extensions is separately checked in sample fields and proved algebraically in the accompanying result.

The output confirms the geometric five-point stabilizer sizes \(6,10,6\) at primes \(7,11,13\), and size two elsewhere in scope; exactly two elements in every such stabilizer have a prime-field monomial lift. In particular, sample finite-field checks are a consistency test, not an infinite-domain proof by extrapolation.

The mathematical proof additionally uses the standard theorem that every automorphism of a smooth anticanonically embedded quartic del Pezzo surface acts on its defining pencil of quadrics. The verifier does not enumerate arbitrary projective linear matrices: the independent geometric reduction in the proof makes that unnecessary. No independent scientific review has been performed.
