---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Reconstructed the Harris--Tu degree product D_(n,n-c)=prod_(j=0..c-1) [binom(n+j,c)/binom(c+j,c)] for 1<=c<=n-1, and rectangular Schur/Jacobi--Trudi determinant det[binom(n,c-i+j)]_(1<=i,j<=c). If n=p^e, Lucas says binom(n,k)=0 mod p for all 1<=k<=n-1; the determinant has every entry on/below diagonal divisible by p, so det=0 mod p. Also D_(n,n-1)=n, so no other prime can divide all degrees. Conversely when p|n and n/p^e>1, choose c=p^e<n. In F_p, Lucas yields binom(n+j,c) ≡n/p^e (mod p) for 0<=j<c, and binom(c+j,c) ≡1 (mod p); every factor is a p-adic unit, hence the particular degree is nonzero mod p. Thus no p divides all degrees; primes outside n excluded by D_(n,n-1)=n. Rational independent recalculation of all coranks n=2..25 recovered the gcd dichotomy and explicit escaping coranks. The finite data only corroborate the Lucas/determinant universal argument.

## originality

PASS

PASS (best knowledge): Friedland--Krattenthaler 2007, fully accessed through authorized lawful copy, establishes the same product and studies parity of individual rectangular/symmetric/skew determinantal degrees; its Sections 1 and 6 do not state an all-proper-rank common prime support theorem. The 2012 bounded-rank geometry literature gives underlying varieties and singular loci, not their gcd tower. The present simple argument combines classical identities with Lucas to classify a new natural across-ranks invariant. Priority risk exists from older plane-partition/Schur divisibility literature and foundational Harris--Tu material not read in full.

## value

PASS

PASS: The gcd across all nested singular-rank loci is a natural arithmetic invariant distinct from any one degree; its sharp prime-power/composite separation, and an explicit rank avoiding each candidate common prime, are motivated complete classifications. The theorem does not pretend that Lucas, Harris--Tu, or the degree product is new, and explicitly leaves exact common exponents unresolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
