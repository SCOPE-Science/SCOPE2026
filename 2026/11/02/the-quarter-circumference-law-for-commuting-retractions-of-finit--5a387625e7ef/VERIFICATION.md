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

# Reproducibility and logical checks

The unit-edge graph metric makes it sufficient to inspect each edge \(i\sim i+1\) when calculating Lipschitz norms. The proof in `RESULT.md` establishes (1) integer norm values; (2) winding-degree invariance at any removal step when \(4K<n\); and (3) an explicit commuting parent filtration with edge images at distance at most \(\lceil n/4ceil\).

`check_cycle.py` uses only Python 3 standard library features. Run `python3 check_cycle.py` from the directory containing the files. It reconstructs the parent maps for every \(3\le n\le128\), verifies prefix ranges and fixed-point identities, all cycle-edge Lipschitz bounds, and pairwise commutation. Actual execution result:

`PASS: 126 cycle sizes (n=3,...,128), every prefix, all cycle edges, and commutation`

A separate finite-depth exhaustive state search for \(5\le n\le12\) found no filtration below \(\lceil n/4ceil\). Such enumeration is only corroborative and is not an exhaustive proof for arbitrary n; the signed-degree argument proves the lower bound for all n. Independent audit or certification has not been performed.
