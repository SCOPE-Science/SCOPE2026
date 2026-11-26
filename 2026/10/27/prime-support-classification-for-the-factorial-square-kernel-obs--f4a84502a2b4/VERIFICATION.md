---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For squarefree a, parity gives s(ac!)=a·s(c!)/gcd(a,s(c!))², so nonmembership propagates to squarefree multiples. The unit case follows because kernels are positive. For the singleton witnesses c=2,3,6,7,11 the exact kernels 2,6,5,35,77 each contain the indicated small prime and are less than its square. The large-singleton proof uses s(c!)>c² for all c≥12: this holds at 12–16 by exact computation and thereafter because the three primes in (c/2,c] guaranteed by Sondow's R3=17 occur with exponent one, give a product > (c/2)³, and c≥17. For p<q both at least 13, at c<q only p can divide the gcd, and only if c≥p, handled by the same bound. For c≥q and c≥41, R5=41 gives five such primes and s(c!)>(c/2)^5>c^4≥(pq)². This leaves the 21 pairs from {13,17,19,23,29,31,37} and the finite window q≤c≤40. Independent parity accumulation by factoring each successive multiplier reproduces the kernels and tests all 21 pairs from c=0 to 40; it finds precisely the five cited failures and first witnesses (13,17;17,24310), (13,19;20,46189), (17,19;20,46189), (17,23;26,104006), (19,23;26,104006), with gcd=pq in each. This proves the uniform q≥29 claim and its sharpness among prime cutoffs (failure at q=23), plus nonclosure under multiplication. The finite replay does not by itself prove any statement about unbounded c, and the classified obstruction is not factorial-square representability.

## originality

PASS

The obstruction, gcd criterion, quadratic lower bound and singleton classification have prior coverage. One can also extract individual semiprime failures from some prior factorial identities. Credit is confined to the complete semiprime classification, in particular the exclusion of all other failure pairs and the sharp uniform prime cutoff. Neither the primary density theorem nor the inspected earlier prime-stratum result establishes that semiprime classification.

## value

PASS

Semiprimes are the natural first composite stratum on which the previously defined obstruction can differ from its singleton behavior. The result resolves the competing membership patterns, shows nonclosure under products with exact witnesses, and identifies and proves the least prime cutoff for uniform membership under the smaller-prime condition. The finite residue is derived from an analytic uniform bound, not an arbitrary search, and the exact answer is useful independently of any claim about least factorial counts. The prior singleton result is not credited anew.

The dated certificate retains the supplied scientific assessment, sources and limitations.
