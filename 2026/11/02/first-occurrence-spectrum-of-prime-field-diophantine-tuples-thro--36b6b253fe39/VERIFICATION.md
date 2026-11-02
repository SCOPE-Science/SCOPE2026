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

Run `python3 verify.py` (Python 3 standard library only) alongside the included `SPECTRUM.csv`. The algorithm constructs each full undirected graph from exact quadratic-residue arithmetic modulo every odd prime through 353. Its greedy independent-set coloring is a rigorous upper bound for maximum-clique search; the proof of exhaustive branching and pruning is in `RESULT.md`.

Observed checks: all seventy primes; eleven exact first-occurrence thresholds; direct pairwise verification of a twelve-element witness modulo 353; no clique of thirteen in that field. The program's canonical table hash is `16c12abf37901cb41a7515e6c6408f210092250527e0de9e89429139224e4bec`. Additional comparisons via a distinct general-purpose maximal-clique enumerator agreed on primes 3, 7, 11, 23, 37, 59, 83, 131, 181, and 251; they are supplementary and do not enter the proof certificate.

The result is finite and reproducible, not an infinite generalization, and does not constitute independent scientific validation.
