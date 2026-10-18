---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

When q<B≤pq the prime factors are single-digit and product has exactly two digits pq=aB+c, 1≤a<B, 0≤c<B. The Smith identity a+c=p+q gives pq-p-q=a(B-1). For p=2 this forces B=q-1 and violates B>q. For odd p,q, put K=pq-p-q>0 and m=B-1=K/a. With m≥q, a≤p-2, so c=p+q-a>0 automatically; the remaining bound c≤m is f(m)=m²-(p+q)m+K≥0. Since f(q)=-(p+q)<0 and roots positive, equivalent to m≥rho_+, or a≤rho_-=K/rho_+. This proves all divisors and no extras. Evaluating f(1) gives exception p=q=3, f(p)<0 and parity restrict p=3 to a=1 and p=5 to a∈{1,3} with 3|4q-5, q≥11. Independent direct digit-sum search agreed with formula for 190 ordered prime pairs p≤q below 70; this finite check is not used for the universal proof.

## originality

PASS

The Dunckley set is the natural prior all-base invariant. OEIS A060209 and original 2001 Vella–Vella citation give this definition but accessible records do not give the symbolic upper-base semiprime spectrum. The exact 2001 article and 2010 exposition remain inaccessible and are explicitly material originality risks. Later accessible Witno papers treat decimal Smith constructions, while OEIS A098837 tabulates fixed base-10 Smith semiprimes. The necessary congruence (B-1)|K does not imply the full digit bound or iff spectrum. Best-of-knowledge O passes without pretending that inaccessible work was read or that absence of an indexed hit proves novelty.

## value

PASS

The base spectrum is a natural exact invariant already studied as Dunckley base multiplicity. Determining all admissible bases in the geometrically/arithmetically distinguished one-digit-factor and two-digit-product stratum is a complete parametric classification, with nontrivial canonical-base law, parity obstruction, p=3 uniqueness and p=5 multiplicity layer. This is a self-contained result of direct future use for studying Dunckley sets, even though its derivation is elementary and does not classify bases ≤q.

The dated certificate retains the supplied scientific assessment, sources and limitations.
