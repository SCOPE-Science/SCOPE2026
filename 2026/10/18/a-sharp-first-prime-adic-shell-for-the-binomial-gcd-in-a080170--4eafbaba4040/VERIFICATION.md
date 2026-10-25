---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For p^a=A and A/p<m<A with p∤m, Lucas digit conditions force q≡1 mod A for any p-nondivisible binomial in the defining family. Writing q=1+At with 1<=t<=m−1 then the high digit segments (m−1)+(t k) have a base-p carry because their residues modulo A sum to at least A, proving p divides every binomial. For s=A/p−1, q*=1+As is admissible, and sk=A(sm−1)+(A−s). The low a digits A−s have a 1 in units and p−1 at position a−1; since p∤m, no unit carry, exactly one carry from position a−1, and no propagated carry because (sm−1) mod p<=p−2. Kummer therefore gives exact valuation1. Separately, polynomial forward differences show any prime r|D(k) divides k+1=n, and Guo et al Lemma 9 asserts r|D(n−1) iff n/r^e<=r^e for r^e||n. For r!=p one has r^e<=m<A<=n/r^e so r cannot divide D. Independent factorial valuation computations for 91 admissible small shell cases reproduce valuation1; they are corroboration, not universal proof.

## originality

PASS

Published Guo et al 2026 establishes whether a prime divides the gcd, not the positive exponent. The explicit Kummer single-carry multiplier shows valuation exactly1 in a natural first p-adic shell; OEIS A080170 records unit-gcd indices only. Source relation is a genuine quantitative strengthening not identical to a rephrased support theorem, subject to a residual risk of older valuation formulae.

## value

PASS

Exact prime-adic exponent in a natural first-shell family of the archival binomial gcd invariant fills a genuine gap between known prime support and numerical gcd. An explicit uniform one-carry multiplier is a structural witness, not a table recomputation or arbitrary substituted parameter. The restricted family is motivated by the published prime-support boundary and deliberately avoids extrapolating to all k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
