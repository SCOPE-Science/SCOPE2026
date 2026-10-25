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

# Reproducibility

Run `python3 verify_colored_equivalence.py` in the directory containing the script. This creates `CLASSIFICATION.csv` and prints a deterministic transcript (a captured execution is supplied as `verification_output.txt`). The assertions check all \(6560\) nonempty canonical profiles, the \(207\) distinct rank-two signatures, the representative-size distribution, and the two size-\(13\) extremizers. The proof that every finite structure has one of these canonical signatures uses a two-round Ehrenfeucht–Fraïssé game argument in `RESULT.md`; executable enumeration verifies only the resulting finite exact instance.

Two implementations of the one-step character partition are compared on all canonical profiles: a five-bit formula using per-class colour counts, and direct enumeration of atomic two-point extensions for every individual element. They induce identical partitions, as asserted by the program. Neither is external or independent scientific validation. The classification table is regenerated without external packages or network access.

# Limits

The exhaustive census is complete only because the block truncation lemma reduces the unbounded finite class to a finite set. No amount of finite enumeration alone establishes that lemma. No checks were performed for counting-quantifier languages, additional predicates, or larger quantifier rank.
