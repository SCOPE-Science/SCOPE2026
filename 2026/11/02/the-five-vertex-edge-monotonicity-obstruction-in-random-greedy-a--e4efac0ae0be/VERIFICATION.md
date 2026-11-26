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

The only positive-change order has the marked clique vertex first globally and the centre first among its star. Its probability is 1/[(k+m+1)(k+1)]. The leaves replace the centre, contributing k−1 extra accepts; if the centre instead blocks the clique vertex, a different clique vertex replaces it for m≥2. Moving this mass from 2 to k+1 gives the law. For m=1 the mean difference of the larger star versus the smaller star plus an isolate is −2/[(k+1)(k+2)]. Independent exhaustive set-based permutation counting of 1, 2, 8, 64 and 1024 graphs tested 0, 1, 12, 192 and 5120 nonedges; positive counts were 0, 0, 0, 0, 240, all gains 8/120. The full relabelling orbits of the displayed representatives are disjoint, of sizes 60, 120, 60, and exhaust the positives; their respective old/new numerators over 120 are (320,328), (296,304), (304,312). The empty graph trivially contributes no augmentation.

## originality

PASS

Credit only the exact star–clique comparison and the complete lowest-order marked census. Edge-addition improvement itself was already known via a bridge between two stars. The bounded literature and catalogue comparison did not establish earlier equivalent coverage of the credited claims.

## value

PASS

The exact first failure of monotone response under one added exclusion edge has an intrinsic finite cutoff. The complete marked list distinguishes connected and disconnected mechanisms, and the signed coupled family gives a structural explanation (substitution within the clique) rather than just a small numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
