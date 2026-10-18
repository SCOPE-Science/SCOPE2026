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

Set B(n)=n s(n), s(n)=sigma(n)−n; B(p²)=p²(p+1). Any solution n divides p²(p+1), split e=v_p(n)∈{0,1,2}. For e=2 n=p²d, d|p+1, d>1 makes proper divisor p² contradict s(n)=(p+1)/d; hence n=p². For e=0 n=d|p+1 and p²|s(d), impossible as s(d)≤d(d−1)/2≤p(p+1)/2<p². For e=1 n=pd, d|p+1, gcd(p,d)=1 and sigma multiplicativity yield d(d+(p+1)s(d))=p(p+1). Put p+1=dk: d(1+k s(d))=pk, hence d|k, k=dh, and modulo h forces h=1; p+1=d², primality gives d=2,p=3,n=6. Both B(6)=B(9)=36. All primes covered, including p=2; independent exact divisor enumeration corroborates first 62 primes, not a proof of all primes.

## originality

PASS

Best-of-knowledge PASS for the exact INFINITE family fiber theorem. Noppakaew–Pongsriiam 2023 Example 8 already lists B(6)=B(9)=36 and Question 29 asks whether infinitely many collisions exist; a finite example does NOT imply all other prime squares cannot collide. OEIS A212327 lists collision values but no universal prime-square exclusion. The known collision 36 gets no novelty credit.

## value

PASS

Determining all fibers containing prime squares is a natural complete first subfamily of the open ns(n) collision problem, establishes 9 as unique prime-square participant, and gives a reusable obstacle for attempts to construct infinitely many collisions. It is a genuine infinite classification, not a restatement of the sample value 36.

The dated certificate retains the supplied scientific assessment, sources and limitations.
