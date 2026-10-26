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

# Reproduction and verification

Run `python3 verify.py` using a standard Python 3 interpreter, without external packages. The program builds the degree-eight polynomial, computes the Cartier–Manin coefficient matrix and finite-field ranks using direct arithmetic, and tests three Frobenius twists. It enumerates all eligible ordered \((a,b)\) over the irreducible-polynomial presentations of \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), checking separately all three exceptional loci. Its successful output ends `VERIFY_OK`.

The checks gave \(q=3\): zero smooth ordered models; \(q=9\): 42 smooth models, 18 rank-two and 24 rank-three; \(q=27\): 600 smooth models, 72 rank-two and 528 rank-three. Each of the three exceptional curves has respectively 0, 6 and 24 rational ordered parameter pairs over those fields. The verification also compares independently calculated elliptic quotient Hasse invariants. The complete characteristic-three statement is supported by the algebraic proof in `RESULT.md`, not merely by this finite enumeration.

No independent audit or independent validation has been performed. No certification of a broad novelty search is claimed.
