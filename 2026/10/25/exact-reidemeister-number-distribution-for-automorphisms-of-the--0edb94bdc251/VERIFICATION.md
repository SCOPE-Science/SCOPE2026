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

# Verification details

The proof relies on the classification of all automorphisms by a quotient matrix and a central linear shift, a fixed-ordinary-class formula for twisted conjugacy, and an exhaustive four-case classification of invertible two-dimensional matrices. These are proved in `RESULT.md`; computations are independent consistency checks only.

The standalone `check_reidemeister.py` (Python 3, no third-party dependencies) enumerates all invertible matrices for the four odd primes \(3,5,7,11\), tallies the exact automorphism multiplicities, and checks the total. In addition, for \(p=3\), the checker constructs the actual order-\(27\) group multiplication, all \(432\) automorphisms, and all action orbits \(x\mapsto gx\varphi(g)^{-1}\). This tests the defining relation directly rather than relying on the fixed-conjugacy-class formula. Output: `VERIFY_OK`.

No computational enumeration is used to infer the universal quantifier over all odd primes. The statement does not apply to characteristic two or to all extraspecial groups of higher order. No independent mathematical audit has been performed.
