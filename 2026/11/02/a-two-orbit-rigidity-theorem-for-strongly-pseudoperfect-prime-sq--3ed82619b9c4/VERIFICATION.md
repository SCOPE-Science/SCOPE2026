---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Write A=2^a, B=2A-1, T=σ(n)-2n=B(p+1)-p² odd. Exactly three complement orbits have odd weight: 1+Ap², (A+1)p, A+p²; all other middle/outer orbits have even weight, with even-a square-root singleton counted ONCE. Parity forces one odd orbit in any omission with at most two; 1+Ap²>T and algebra excludes both remaining singleton odds. For two orbits four cases arise (odd w2 or w3 times even middle or outer). The middle cases reduce to p dividing B or A-1 and force respectively no odd prime or the unique A=4,p=3 singleton M=2. Outer cases reduce to integer quadratics with strictly increasing positive-root branches; bounds trap a candidate between consecutive integers or force even quotient k where k must be odd. Boundary a=1,2,3 addressed explicitly. For n=36 omitted weights 13+6=19. Independent exact divisor orbit combination enumeration for a<=14, odd primes up to199 found 36 only. Finite check is not infinite proof.

## originality

PASS

Qualified PASS for the uniform low-OMITTED-COMPLEMENT-ORBIT classification over a whole exponent-two odd-prime family, not the known strongly pseudoperfect example 36 itself. Wang–Zelinsky Sept2026 Table2 gives 36 with omitted divisors {4,9,6}; its main restrictions and 2^a*p Mersenne case do not assert global at-most-two-orbit classification for 2^a*p². Aryan et al classify exactly two omitted INDIVIDUAL divisors, not the three- or four-divisor complement-paired situations. Published SCOPE bitmask result has p^1 rather than p². Stronger sparse-omission literature remains a specific risk.

## value

PASS

Omitted complementary divisor orbits are the natural sparsity parameter under the definition of strong pseudoperfectness. The theorem completely determines 0,1,2-orbit omission phenomena for an infinite two-prime-support family, and the square-root singleton produces one exceptional 36 configuration. This is a structural low-sparsity classification, not rediscovery that 36 belongs to an existing table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
