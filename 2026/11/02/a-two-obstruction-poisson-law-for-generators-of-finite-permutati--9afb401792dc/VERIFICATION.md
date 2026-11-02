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

# Reproducibility and evidential limits

Running `python3 checker.py` reconstructs each tested tense algebra as a powerset of a finite permutation, closes every tested candidate generator tuple directly under Boolean meet, join, complement and the forward/backward operators, and checks the count against the necklace formula. It tests 339 permutation/rank cases and 10,999 tuples across permutations of size one through five; the output includes `FINITE_GENERATION_OK ...` and terminates with `ALL_CHECKS_OK` if all assertions hold. It additionally checks tense-algebra identities and prints sample finite probabilities against their asymptotic targets.

The Poisson limit, asymptotic independence and logarithmic threshold are established by the analytic proof in `RESULT.md`, not by simulation. The original first-public date of the motivating paper is independently stated on the arXiv record (2026-10-01). Scientific novelty is assessed against inspected sources and remains subject to possible broader prior coverage. No external independent validation has been performed.
