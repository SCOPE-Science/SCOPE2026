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

# Reproducibility and checks

The exact checker `check_engel_laws.py` uses only Python's standard library (`fractions`, `itertools`, `collections`). From the directory containing the artifact files, run `python3 check_engel_laws.py` and compare its output with `checker_output.txt`. The output concludes with `VERIFY_OK`.

The code enumerates all pairs in each tested semidirect product, directly multiplies group elements, computes each of the first six Engel words, and compares exact rational probabilities at **every** group element with the proposed distribution. It tests twelve parameter/action families, including actions by inversion, swaps, negative swaps and the identity. Some sample groups have identical expected scalar signatures despite different odd-primary structure; the test is only a finite sample of the theorem.

The proof itself is symbolic. Its critical nonstandard steps are the explicit four-case first-commutator formula, the identity \((\theta-1)^2=-2(\theta-1)\), and the reconstruction of finite abelian \(2\)-primary elementary divisors from successive image cardinalities. Neither the checker nor its log constitutes an infinite proof or an independent audit.

Self-review: passed. Independent audit: not yet performed.
