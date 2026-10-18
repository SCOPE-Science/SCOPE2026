---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For c=8beta+r, if p∤c then CRT coprimality of c to 8p² and Dirichlet prime q≡c mod8p² produce tau(q)=2. If p²|c, the unique possible c in [r,8p²-8+r] with c≡r mod8 is c=rp²; when p!=r tau(rp²)=6, and for p=r choose prime q≡p mod8 to get p²q with tau=6. For p||c, write t=c/p and multiplicativity tau(p(8pn+t))=2tau(8pn+t); modulo4 congruence holds iff the progression avoids squares. Such a square occurs iff x²≡t mod8p has a solution (lift x to large positive representative); for odd unit t CRT gives t≡1 mod8 and Legendre(t/p)=+1. As beta cycles mod p², nonzero t values run through all nonzero residues mod p, while t≡rp mod8, so count is (p-1)/2 if p≡r mod8 else p-1. Boundary p=r and p=3 included. Independently brute-checked p=3,5,7,11 all r and initial 300 n, in addition to reading finite source verifier; all-prime proof is symbolic.

## originality

PASS

Merca 2022 Axioms 11(342) explicitly poses exactly the cardinality formula as Conjecture 3, while proving p=3,5. The general Craig–Merca framework concerns valuations/congruences but does not state this exact quadratic-obstruction classification. The theorem supplies a full character criterion and proves conjecture. Searches on exact notation, Legendre/square-progression aliases and Resultary yielded no dominating matching result; recent unrelated paper with similar title about Merca number-of-divisors problems has unresolved topic and is retained as bibliographic risk rather than claimed excluded.

## value

PASS

Proves an exact published conjecture across all odd primes and three residue classes, with an illuminating necessary-and-sufficient membership test explaining the two possible counts. It resolves the previously noted difficulty of deciding square membership of a progression, rather than merely extending a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
