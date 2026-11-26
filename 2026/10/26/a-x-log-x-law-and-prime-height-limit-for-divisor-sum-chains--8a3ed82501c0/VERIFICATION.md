---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For distinct primes p<q, only the two middle divisor sums p+1 and q+1 need testing for comparability. The chain condition is q=-1 modulo p+1; the only positive integer in that class at most p is p itself. The fixed-modulus prime number theorem therefore gives the displayed fixed-p main term, also at tX for each fixed t>0. For p<=X^(1/3), the Brun–Titchmarsh logarithm is at least (log X)/3-log(1+X^(-1/3)), giving the stated bound with 7 eventually. Above the split, counting q=p+j(p+1), j>=1, gives at most X/[p(p+1)] per p, hence O(X^(2/3)) even summing over all integer p in the upper range. The elementary bound phi(m)>=sqrt(m/2) follows from the prime-power formula (the factor phi(l^e)^2/l^e is at least 1 except at l^e=2), giving a summable dominating prime series in the lower range. This justifies the total asymptotic, not just its finite truncations. The fixed-p counts at tX give the limiting rectangles, with t=0 automatic and tightness supplied by the same tail bound. Landau's two-factor asymptotic gives the proportion since squares are negligible and a fixed finite list of least primes contributes only O(X/log X) in the unrestricted set. The supporting numerical checks were inspected, not run, and do not establish any asymptotic.

## originality

PASS

The chain criterion is exactly Huber's; the result being credited is the aggregate asymptotic and the limiting least-prime mass for that criterion. The height law is a useful consequence of these asymptotics, not a separate prime-distribution breakthrough. The strongest indexed analogues count different congruences and do not supply this law, although the summation method is closely analogous.

## value

PASS

This is a quantitative law for a natural poset condition already singled out in prior work. It identifies the rarity scale among semiprimes and an explicit tight least-prime population, in contrast to the diverging least prime under uniform unrestricted sampling. The aggregate requires controlling primes beyond every fixed cutoff; the value is in that law and its concrete conditional mass, not in the known congruence test or an arbitrarily selected case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
