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

For the loopless digraph in the stated assumptions, Lemma 8 supplies Borel independent sections with the exact uniform vertex marginal p=2^{−d−1}; the raw fair-bit construction can be thinned to this marginal without affecting independence. At x the list minus current out-neighbor colors has at least d+1 entries. Joint Borelness of each step follows from countable-section projection on histories times vertices and ordering a finite set of natural numbers. A selected sad vertex clears its conflict since all its neighbors are unselected. Otherwise next-stage sadness is bounded by old sadness with nonselection and by new conflicts from previously sad out-neighbors. Conditional on the past, a specific out-neighbor recolors into the old color of x with probability at most p/(d+1): the independent fresh index can hit it at most once. The resulting recurrence contracts the uniform bound by 1−p/(d+1), and summability gives pointwise eventual constancy and eventual non-sadness. The Borel eventual-value rule with list-valued fallback gives properness with probability one on each fixed edge, not a single almost-sure event over all edges. Cyclically orienting K_{2d+1} as a regular tournament verifies sharpness for common lists of size 2d: the finitely many edge events would yield an impossible proper coloring. No local pointwise optimum is asserted. This is a proof check, not a finite experiment.

## originality

PASS

The proof method and sharp uniform palette size are known. The supported distinct claim is the jointly Borel edgewise-a.s. theorem for arbitrarily prescribed finite input lists with the local threshold d+d⁺(x)+1. The strongest inspected fixed-palette and residual-list results do not furnish this assertion.

## value

PASS

Prescribed allowable colors are a natural strengthening that a fixed palette does not handle. The local bound treats vertices of smaller out-degree with genuinely smaller lists while allowing unbounded in-degree, and preserves the nontrivial edgewise jointly Borel guarantee. The finite regular tournament demonstrates a meaningful uniform boundary. The contribution is the broader usable list theorem, not a new recoloring technique or pointwise sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
