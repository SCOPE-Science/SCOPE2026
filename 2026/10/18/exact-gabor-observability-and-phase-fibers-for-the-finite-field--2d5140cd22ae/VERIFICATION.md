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

# Verification and evidence

The packaged Python program `checks/verify.py` uses only the standard library. It computes all Gabor ambiguity entries with exact cyclotomic multiplicity arithmetic and independently enumerates hyperbola differences and Cayley-graph components at seven odd prime-power field sizes. The output in `checks/verification_output.txt` is reproduced from this program. It is a finite independent algorithmic check of the overlap and character criteria, not an infinite theorem proof.

An additional direct numerical rank computation of the full 81-by-81 Gabor lifting matrix at field order 3 returned 27, consistent with the exact rank formula. Numerical tolerances play no role in the packaged cyclotomic zero tests. The unrestricted statements are established by discriminant arithmetic, cyclotomic divisibility, Fourier diagonalization, and an explicit additive-generation argument.

No independent mathematical audit has been performed.
