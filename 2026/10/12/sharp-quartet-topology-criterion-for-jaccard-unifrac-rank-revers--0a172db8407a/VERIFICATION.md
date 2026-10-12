---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the rooted-quartet rank criterion

Execute the standalone file `check_unifrac.py` with standard-library Python 3:

```sh
python3 check_unifrac.py
```

The executed check returned exactly:

```text
VERIFY_OK profiles=2262 classifies_reversal=630 direct_pair_scores=33930
```

The program recomputes presence-on-descendant-edge indicators independently of the theorem's closed-form expressions using exact `fractions.Fraction`. It enumerates all two-species communities and unordered distinct comparisons on both rooted four-tip shapes, checks the complete overlapping/disjoint UniFrac score multisets and extremal signed margin, and tests the strict criterion for 2,262 rational branch profiles of denominator 40. It also verifies that other common richness levels have no strict reversals, and checks the concrete symmetric balanced example at branch fraction \(3/4\). Every evaluated fraction is exact; no floating-point tolerance is used.

The infinite family of branch fractions is covered by the direct symbolic formulas and inequalities in RESULT.md, not by the finite grid. The verification does not address alternate root conventions, weighted UniFrac, more than four tips, unequal richness, or the uniqueness of the result in unindexed literature.
