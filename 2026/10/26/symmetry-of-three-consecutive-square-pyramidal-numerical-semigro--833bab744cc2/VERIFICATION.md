---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The generator identity (n+1)c=(n+2)a+5b and exact adjacent gcd(a,b)=(n+1)/gcd(n+1,6), gcd(b,c)=(n+2)/gcd(n+2,6) imply gcd(a,b,c)=1; also gcd(a,c)|5. For n>=3 all three generators minimal, using c<2a for n>=8 and checks n=3..7. The classical symmetric three-generator gluing criterion applies. For pair (a,b), a nonnegative representation of c after dividing by gcd forces t=0 in the 2-generated Diophantine general solution and hence gcd(n+1,6)=1; conversely it constructs gluing when n≡0,4 mod6. Pairs (b,c) and (a,c) are ruled out by divisibility and size inequalities. The gluing Frobenius formula yields [4n^5+32n^4+101n^3+175n²+102n−36]/36 and g=(F+1)/2. At n=1 S=N0, F=-1; at n=2 S=<5,14>, F=51. Independent Apéry shortest-path checks all 100 indices n<=100 agree, but all-n follows from gluing proof not enumeration.

## originality

PASS

PASS, qualified: Fel's related 2016 primary paper studies generators (n-1)^k,n^k,(n+1)^k for k=2,3,4, not consecutive values of the cubic square-pyramidal partial sum Q(n). Robles-Perez and Rosales study consecutive triangular/tetrahedral rather than these triples. OEIS A000330 and A322479 tabulate raw pyramidal numbers and consecutive sums, not three-generator semigroup symmetry or Frobenius polynomials. An earlier equivalent general polynomial-sequence gluing result remains possible; no database search establishes absolute novelty.

## value

PASS

PASS: Classifying a natural family of minimally three-generated numerical semigroups into exact mod-six symmetry classes and deriving the degree-five Frobenius polynomial is a precise infinite arithmetic classification. The density 1/3 and two exceptional small semigroups are structurally motivated by the gcd/gluing mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
