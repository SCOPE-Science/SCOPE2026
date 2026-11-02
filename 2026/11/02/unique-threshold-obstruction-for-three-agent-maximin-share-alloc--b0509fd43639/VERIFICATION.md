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
# Verification

The package contains `verify.py`, an independent finite checker using only Python's standard library. Run `python3 verify.py` from the directory containing the extracted files. It enumerates unordered set partitions and direct disjoint-part transversals, tests all \(25^3=15625\) labeled partition triples on five goods, confirms the exceptional \(30\), and determines their single good/agent relabeling orbit. It checks the \(216\) four-good profiles, direct binary-valued threshold realizations for all \(30\) patterns across \(243\) assignments, and feasibility after each of \(720\) single-extra-bundle acceptance changes.

Expected output: `VERIFY_OK partitions_5=25 profiles_5=15625 obstructions=30 unlabelled_orbits=1 profiles_3=1 profiles_4=216 valuations_and_allocations_checked=30x243 proper_acceptable_extensions_checked=720`.

The implementation checks finite combinatorial objects, not the theorem over the infinite space of monotone real-valued utility functions. That extension follows from the threshold-acceptability equivalence and its explicit proof in `RESULT.md`. Unindexed prior work may affect publication priority. Independent audit has not been performed.
