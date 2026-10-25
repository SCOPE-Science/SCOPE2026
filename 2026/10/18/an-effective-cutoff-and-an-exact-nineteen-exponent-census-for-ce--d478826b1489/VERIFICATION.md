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

For k,m>=2 and u,v>=0 with (2m+1)^k=u m^k+v(m+1)^k, positivity implies 0<=v<2^k. Reduction mod m yields v=1+jm, j>=0; reduction mod m² (k>=2) yields j=k mod m. If m>k, j>=k, so 1+km<=2^k-1 and m<=(2^k-2)/k. Otherwise m<=k. The cutoff M_k=max(k,floor((2^k-2)/k)) therefore covers ALL k. For each m,k, coprime m^k,(m+1)^k give unique admissible v as least residue of (2m+1)^k [(m+1)^k]^{-1} modulo m^k since v<2^k<=m^k. A nonnegative quotient gives solution; otherwise none. Independently enumerated all 111,114 pairs (k,m) for k=2..20 within proved cutoff using exact Python integers, obtaining exactly (2,2,4,1),(4,2,34,1),(4,3,17,4),(11,2,1093,263),(13,2,51118,503). Inspected companion CHECKER.py contains independent residue and constrained-j methods. This is finite but exhaustive because the cutoff is proved; no conclusion for k>20.

## originality

PASS

Fel 2016 studied numerical semigroups from powers of three consecutive integers, including earlier k=2,3,4 classifications and the individual k=11,13 examples in a bounded search m<=50. The present identities are NOT individually novel. The surviving mathematics is a uniform analytic all-m cutoff for arbitrary k and a complete proof-level classification for k=2..20, rather than a truncated computational table.

## value

PASS

The natural semigroup center-generator membership question previously had searches bounded ad hoc in m. The modular obstruction makes it decidable over a proved finite domain for each exponent; the nineteen-exponent census is a natural complete classification with exact, reproducible arithmetic, not an arbitrary slice. No claim is made to solve all k or all symmetric semigroups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
