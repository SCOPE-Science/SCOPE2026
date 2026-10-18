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

At n<=3 there is no solution, n=4 and n=7 are the exceptional solutions. For even n, an odd prime factor of n=2u forces Omega(n+2)>=3, except n=4. For odd n with both endpoint Omega<=2, systematically eliminate prime/prime, prime/square, square/prime, semiprime/prime, prime/semiprime, both squares, square/semiprime and semiprime/square by the totient and product/sum identities or AM-GM. In the remaining distinct-odd-semiprime case n=pq, n+2=rs, equality of totients and product difference give r+s=p+q+2; ordered prime gaps e=s-r,d=q-p satisfy e^2-d^2=4(p+q-1). Therefore A=(e-d)/2, B=(e+d)/2 are uniquely determined odd integers 3<=A<B, with the four prime formulas in pinned RESULT.md. Direct expansion gives rs=pq+2 and equal totients in the converse. The result is genuinely unbounded in n; enumeration only cross-checks. Independent Euler totient/sieve through n=250000 found precisely 4,7,6497,12317,133787,181427 with nontrivial pairs (A,B)=(7,23),(13,17),(17,43),(23,37).

## originality

PASS

The exact biconditional covers ALL separately low-Omega endpoint types and uniquely inverts a two-parameter prime quadruple. Graham–Holt–Pomerance 1999 already gives a four-prime family, and for gap two its construction is precisely A=3, so that special case receives no novelty credit. Their Theorem 1 yields another class and is not a complete classification of the low-Omega layer. Ford studies the fixed-gap problem generally. An OEIS solution list is not a symbolic exhaustive classifier. Best-of-knowledge no source inspected dominates the full result; a hidden elementary classification remains possible.

## value

PASS

A sharp, unconditional, infinite-domain arithmetic classification of the first nontrivial prime-factor complexity layer in a long-studied fixed-gap totient equation is an independently useful structural result. The unique inverse parameters and converse give an exact practical recognizer without pretending to prove infinitely many prime quadruples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
