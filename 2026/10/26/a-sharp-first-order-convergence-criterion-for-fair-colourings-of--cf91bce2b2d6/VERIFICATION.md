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

The standard-library script `colour_block_verifier.py` was executed with `python3 colour_block_verifier.py` and returned `COLOURED_EQ_EXACT_OK 123856 1346 24`.

The three numerical fields count binary colourings in exhaustive small-block multinomial checks, depth-one/two finite Ehrenfeucht–Fraïssé matched-profile comparisons, and finite critical-intensity checks. The verifier recomputes these checks from its own enumerations, rather than reading pre-existing logs. Its conclusions concern only finite cases. The necessity argument, universal finite-rank back-and-forth lemma, infinite Poisson convergence, and complete first-order probability spectrum rely on the written proof, not on extrapolation from finite data.
