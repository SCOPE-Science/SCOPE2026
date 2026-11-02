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

# Reproducibility and scope

Run `python checker.py` with Python 3.9 or later using the standard library only. The program enumerates all increasing-labelled rooted trees of orders \(1\) through \(6\) (representing every rooted unlabelled tree of these sizes) and all uniform vertex-priority permutations. It calculates the complete subtree-argmin signature distribution and its exact \(k\)-fold collision probability using `fractions.Fraction` for \(k=2,3,4\). It compares each with the formula derived independently from child-subtree sizes. In total, \(462\) exact comparisons are made; separate brute-force tests with three valuations for \(n\le3\) verify the semantic minimum-of-sums equivalence. Successful output ends in `ALL_CHECKS_OK 462 exact collision probabilities and direct semantics n<=3`.

The verification is finite. The proof of the theorem for arbitrary finite tree size and all integer \(k\ge2\) is the uniform block-interleaving argument in `RESULT.md`. Exact tests cannot establish historical originality, independence, or generalization beyond the proved topology and distribution assumptions. Independent audit has not been performed.
