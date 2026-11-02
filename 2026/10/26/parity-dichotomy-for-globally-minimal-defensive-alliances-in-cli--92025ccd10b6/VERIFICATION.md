---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Let a_i=floor(r_i/2), T=sum a_i and o=count odd r_i. The defensive inequality on a chosen peripheral vertex is 2(k_i-1+z0)+1>=r_i. If the apex is absent, global minimality forces a single nonempty blade with k_i=a_i+1. With apex present, any blade with k_i>a_i contains its own defensive suballiance, while the center requires sum k_i>=T+floor(o/2), giving k_i=a_i for all blades and o<=1. Conversely every nonempty proper subset of either proposed type fails a peripheral or apex inequality. New independent exhaustive all-subset tests exactly matched all families for seven heterogeneous bouquets; B(2,4,4) has 81 minimal sets.

## originality

PASS

General algorithmic enumeration of minimal defensive alliances by Feng–Fernau–Mann and recent parameterized classification do not give the specific all-orders heterogeneous clique-bouquet polynomial nor the odd-blade parity obstruction; those graph family aliases were explicitly searched. No asserted stronger published formula was found.

## value

PASS

The parity threshold for whether apex-containing globally minimal defensive alliances exist, and their all-size census across an infinite natural block graph family, are motivated and not just a textbook minimum-size exercise. The family has unbounded minimal-size gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
