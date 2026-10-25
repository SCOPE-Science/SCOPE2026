---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

PASS. If q divides b+1 then b=-1 mod q, giving zero residue for even palindromes, and odd L=2k+1 digit linear form 2 sum_{j<k} (-1)^j d_j +(-1)^k d_k. For Fourier character h=0 the sum is (b-1)b^k. For q even, character h=q/2 has only the center parity phase and gives (b-1)b^(k-1). Each remaining z with z^2 !=1 gives the exact independent-digit product (-1)^(k+1)(z+z^-1), and inversion recovers the printed all-residue law. The residue correction B_q(r) is 0 for q2, either 1-2/q or -2/q for odd q>=3, or 0,1-4/q,-4/q for even q>=4, strictly inside (-1,1). Leading-digit restriction and L=1 addressed separately. Independently enumerated 630 complete exact (b,q,L,r) residue profiles for b=2..12, all q|b+1 and L=1..5; formulas and strict error bound match. Finite tests are not the infinite proof.

## originality

PASS

Best-of-knowledge originality PASS on the exact final claim after new Git-tree proof and computation reconstruction, Resultary semantic searches, checked primary theorem scopes and explicit source risks. Not a claim of comprehensive historical priority, external certification or entire-paper noncoverage where material was inaccessible. All known special-case antecedents are credited.

## value

PASS

PASS. Arithmetic-progression distribution of base-b palindromes is a well-developed natural problem; moduli dividing b+1 are excluded from standard equidistribution hypotheses because digit-pair phases resonate. The exact uniform/biased all-residue formula, strict universal <1 discrepancy and even-modulus persistent parity bias give structural information precisely in that arithmetic obstruction regime. Its value is the all-b all-q family, not the classical even-palindrome divisibility or q=2 special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
