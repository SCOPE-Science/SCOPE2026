---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For n>=2 and ordinary multiplicity S(n)=sum p nu_p(n), the four possibilities prime/prime, prime/semiprime, semiprime/prime and semiprime/semiprime exhaust Omega(n),Omega(n+1)<=2. Adjacent primes 2,3 have unequal S. In prime/semiprime case p=ab-1=a+b gives (a-1)(b-1)=2 and uniquely a,b=2,3 so n=5. In reverse case a+b=ab+1 forces (a-1)(b-1)=0, impossible for primes. Two semiprimes ab,cd with cd-ab=1 and c+d=a+b yield the exact factorization 1=(c-a)(b-c). The two sign choices force three consecutive integers to be prime, necessarily 2,3,4, impossible. Repetition a=b and c=d is included; independent direct factorization scan through n=20000 found only n=5. Universal proof is symbolic, not finite.

## originality

PASS

PASS best-of-knowledge: the known published unique prime-containing Ruth-Aaron theorem already settles three of the four patterns, but does not settle the semiprime/semiprime pattern. The new exact factorization supplies that missing case; Jiang–Miller and the OEIS list the general object and examples without an inspected such complete two-almost-prime theorem.

## value

PASS

This is the complete first nontrivial factor-complexity boundary for the classical Ruth–Aaron invariant when multiplicities count. It closes an ordinary natural prime/semiprime comparison, explicitly including squares, by a sharp obstruction to two neighboring semiprimes. It is elementary and narrow, but a genuine natural exact classification rather than a generic rephrasing or an arbitrary numerical slice; no claims beyond Omega<=2 are made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
