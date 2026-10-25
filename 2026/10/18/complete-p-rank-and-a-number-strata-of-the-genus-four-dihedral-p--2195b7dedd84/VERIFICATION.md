---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

From actual RESULT.md blob 262717f88e039b7186c075a5072d2232dea90dc1: polynomial squarefreeness iff s²!=4 follows from derivative. Cartier-Manin coefficients gamma_(41i-j) only exponents divisible by 5; 41 ≡1 (mod5) forces diagonal matrix (A(v),B(v),B(v),A(v)). Fresh independent exact F41 trinomial coefficient expansion matched A=18(v+15)(v³−17v²+v+2), B=7(v+13)(v+15)(v⁶+20v⁵+14v⁴−3v³+15v²−14v−19), gcd v+15; Rabin finite-field irreducibility checks certified degree 3 and 6 factors; v=4 gives nonzero coefficients. Frobenius semilinear diagonal iterates keep precisely nonzero positions: stable rank is 2 for single vanishing A or B and 0 for both; a=4−rank. Geometry of moduli uses published s↔−s isomorphism criterion, not just polynomial root counting. Computations exact over a finite field, not sampled geometric instances.

## originality

PASS

Known characteristic-41 superspecial point and isomorphism criterion, as well as general Cartier/mass machinery, are credited. The exact ten intermediate p-rank-two geometric points, irreducible orbit degrees 1,3,6, and complete stratification are not displayed in the directly checked primary superspecial census or broader nonordinary mass paper. Best-knowledge with explicit possibility of implicit mass-based equivalence.

## value

PASS

The natural genus-four dihedral pencil has a sharply resolved nonordinary stratum and field-of-moduli Frobenius orbit structure at characteristic 41. This answers a concrete parameter-wise geometric classification beyond superspecial existence, with explicit Cartier factors that can be reused for arithmetic geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
