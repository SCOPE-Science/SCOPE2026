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

For n>1, phi(psi(n))/n=P(n)R(n). Bounding P by small-prime products rules out odd supports and all even supports of size <=5. For six supports, any factor >=5 in psi forces R<=4/15 while P<=2304/715<15/4, so psi support is exactly {2,3}; then P>3 forces 2,3,5,7 and two primes u<v with 2,3-smooth successors. Exact product bounds restrict u to 11 or17, v<384 for u11 and v<576/19 for u17, yielding exactly 10+1 prime pairs; exponents >=5 must be one, a,b>=1 arbitrary. Checked rational ratios include q383 147456/147455 and 17,23 13824/13685; catalog eleven rows were inspected and the prime bound exhausts all cases.

## originality

PASS

Best-of-knowledge complete six-support iff classification is not implied by the closest checked 2005 counterexamples or radical reduction, by the exact OEIS defining table, or by a different 2025 composition-order investigation. The sharp 2,3-smoothness restriction and v<384 finite exhaustion add genuine content; bibliographic priority and citation-numbering risks remain.

## value

PASS

Sándor’s counterexample inequality is a natural open structural classification problem. Determining the exact minimum omega=6 support, all eleven possible supports with unrestricted first two exponents, and the sharp q=383 boundary is an exact infinite-family characterization not recoverable from the finite OEIS examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
