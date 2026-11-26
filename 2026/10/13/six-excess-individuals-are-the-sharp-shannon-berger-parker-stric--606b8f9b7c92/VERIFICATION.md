---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At common k,N, both scores decrease in exact integer keys: Shannon in ∏n_i^{n_i}, order ∞ in max n_i. I independently generated all length-k sorted excess vectors with entries in 0,…,r, filtered on sum r, restored the ones, and compared all pairs for k=3,4,5,6 and r=0,…,6. There are no discrepancies through r=3. At r=4 the unique tie split has max 3 and products 729 vs 432, with the second profile preferred by Shannon. No strict reversal occurs through r=5. At r=6 the two excess-partition reversals are (3,3) vs (4,1,1), with abundance maxima 4<5 and products 65536>50000, and (2,2,2) vs (3,1,1,1), with maxima 3<4 and products 19683>16384. The latter requires k≥4. There are no other strict reversals at r=6. Beyond k=6 every possible excess partition in the audited range was already admitted; added ones affect neither key. Thus the finite comparison and stabilization prove the claim for all k≥3.

## originality

PASS

The supported contribution is the first weak and strict Shannon–order-∞ disagreement boundary and its all-richness classification, not the indices, exact comparison keys, or the first witness in isolation. The exact witness overlap with the same-day HHI–entropy record supplies the Shannon comparison on that pair (so a maximum check immediately gives one reversal), but does not establish no earlier strict reversals, the first weak layer, or the complete first strict layer. Related maximum–quadratic comparisons do not supply the missing Shannon comparisons.

## value

PASS

With richness controlled, the resolution question for two widely used diversity orders is naturally discrete: when can redistribution underneath the largest abundance first change a tie, and when can it outweigh the maximum's ordering? The exact onset separates these phenomena and identifies all first strict witnesses across richnesses. This supplies benchmark profiles and a protection window against opposite rankings, beyond producing another example of disagreement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
