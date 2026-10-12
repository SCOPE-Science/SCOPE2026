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

# Verification record

The complete local-ring argument consists of a finite birational normalization morphism, a coprimality differential test, explicit monomial tangent-space ranks, dimension-versus-embedding-dimension regularity for the pairwise intersections, and the simultaneous formal-straightening lemma. These steps establish the infinite statement in characteristic zero.

An independent exact-arithmetic SymPy script is embedded as `cubic_factorization_checker.py`. Running it checks the branch, pairwise sum, and total tangent ranks for a coordinate triangle and for another linearly independent triple. It also checks a concurrent-triple boundary (total rank falls to 9) and verifies the quotient Hilbert-series identity. The recorded output corresponds to execution of the actual embedded script. There is no computer proof covering all triples; the all-triple statement follows from the algebraic argument and coordinate-change invariance.

The ring's normalization is a threefold product of formal power-series rings, and the difference from the singular ring is two copies of the regular six-dimensional stratum ring; this follows by comparing branch restrictions. The computed Hilbert--Samuel series, multiplicity, conductor, and Cohen--Macaulay type are consequences of the explicit ring presentation. Nonconcurrent triangles are essential: concurrent triples are expressly outside the theorem. An independently conducted audit has not occurred.
