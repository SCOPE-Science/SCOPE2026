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

# Reproducibility and mathematical boundaries

Run `python3 verify.py` in a directory containing this file and the standalone verifier. The program requires Python 3 only and uses no external data.

It enumerates all reduced-row-echelon subspaces of each tested ambient vector space, retaining those closed under the specified exterior-square bracket, then tests adjacency by taking the linear span of both bases together with all cross-brackets. This latter check does not assume the proved quotient-spanning equivalence. It compares the full degree histogram with the closed formula.

Observed exact exhaustive cases: \((n,q)=(2,2)\): \(10\) vertices, degree histogram \((0:1,6:9)\); \((2,3)\): \(17\) vertices, \((0:1,12:16)\); \((3,2)\): \(575\) vertices, \((0:15,116:357,378:203)\). Formula-only evaluations (not exhaustive subspace checks) include \((n,q)=(3,3)\): \((0:27,1062:2392,3072:1534)\), and several parameter checks for degree-stratum strictness. On success the script prints `VERIFY_OK`.

These finite-field tests are not a proof for arbitrary \(q\) or \(n\); the combinatorial proof in RESULT.md establishes the theorem. The conclusion concerns only the free class-two family and is not an unconditional graph-to-algebra classification.
