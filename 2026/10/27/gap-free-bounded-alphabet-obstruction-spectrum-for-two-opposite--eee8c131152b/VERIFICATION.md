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

The mathematical proof in `RESULT.md` establishes the claim for every pair of positive finite alphabet sizes; it is not extrapolated from finite enumeration. Executing `python3 checker.py` enumerates all labelled subteams of eight small complete bipartite graphs, tests edge-minimal failures, compares the first several cases against direct split semantics, and checks explicit theta witnesses of both parities through forty occupied vertices on the smaller shore. The expected terminal message is `ALL_CHECKS_OK`, following a count of 71,636 tracked diagnostic checks.

The exact source of the logical graph equivalence is Fröhlich--Kolaitis--Meier, *Disjunctions of Two Dependence Atoms*, Lemma 15 (DOI:10.4230/LIPIcs.CSL.2026.10). Exact minimal-failure sizes for all alphabet dimensions are established by the upper-bound argument and explicit constructions in `RESULT.md`; no separate universal computer certificate is required. The existing literature's exact-size notion of coherence is not conflated with this at-most-size finite certificate property. Independent audit or external validation has not been performed.
