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

# Reproducibility and limits

The accompanying `verify.py` uses Python 3 standard-library `fractions`, `itertools`, `collections` and `math`, and requires no external files or services. Run `python verify.py` from the extracted package directory. It directly enumerates all finite partial injections, checks distance preservation on all pairs in their domains, rejects directed cycles, determines the nilpotency index by following every orbit, and counts the rank/index cells.

Separately, the verifier expands the two labeled component generating functions using rational arithmetic and factorial normalization; it does not reuse the graph-metric predicate when producing the predicted coefficients. Both methods agree for all ordered part sizes \(1\leq a,b\leq4\) with \(a+b\leq7\) (15 configurations), including balanced and unequal-part graphs. The sharp maximum-index and extremizer formulas are checked against the direct counts in the same configurations. The previously established star case is included in tests as a boundary check, not as a new research claim.

Expected stdout: `VERIFY_OK 15 complete bipartite graph sizes; every rank/index cell and maximal-chain count`.

Exhaustive finite checks support the formulas but do not prove the unrestricted theorem; the proof uses the two-orientation decomposition, cycle-free path assemblies, and direct extremal counting. No independent audit has been performed.
