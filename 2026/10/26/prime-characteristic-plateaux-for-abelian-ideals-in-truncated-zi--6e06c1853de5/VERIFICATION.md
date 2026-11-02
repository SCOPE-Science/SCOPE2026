---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The finite algebra has e_i∘e_j=binom(i+j-1,j)e_{i+j} modulo p for i+j<=n; the integer half-shuffle identity verifies the Zinbiel axiom even after modular reduction. Left multiplication by e_1 sends e_j to e_{j+1}, a single Jordan shift. Hence every nonzero two-sided ideal is a terminal span I_r=(e_r,...,e_n). Let P=p^k and (p+ceil(p/2))P<=n<=(2p-1)P, set r=n-pP+1. For any product e_i∘e_j with i,j>=r and i+j<=n, both i-1 and j have P-digit at least ceil(p/2), so their base-p addition has a carry. Lucas's theorem makes binom(i+j-1,j)=0 mod p; I_r is abelian. I_{r-1} contains e_{n-pP},e_{pP}, whose product is binom(n-1,pP)e_n=e_n mod p because the base-p P-digit of n-1 equals p. Thus I_{r-1} is not abelian, and every larger ideal is also not. Since every ideal is a suffix, I_r is the unique maximizing abelian ideal, of dimension pP. An independently implemented exhaustive modular-coefficient test checked 32 (p,k,n) triples over primes p=2,3,5,7, all claimed bounds, with no exceptions. The proof relies on Lucas and the Jordan shift, not numerical evidence.

## originality

PASS

PASS on the explicit modular plateau intervals, sharp boundary and unique maximal ideal, with the complex-field null-filiform result credited; a characteristic-zero beta formula cannot be transported through the vanishing of binomial coefficients modulo p.

## value

PASS

The maximal dimension of an abelian ideal is a natural structural invariant of nilpotent nonassociative algebras. Prime characteristic changes the invariant discontinuously via Lucas carrying, generating exact infinite-dimensional plateaux with a sharp first-failing boundary and unique maximizer. This isolates a genuine modular phenomenon absent in the known complex theory, not a formal substitution of p into the complex answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
