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

The standalone `verify.py` is executable with `python3 verify.py` and uses only the Python standard library. It separately constructs coordinate-fiber covers and checks rational-tensor pairing matrices for inclusion-minimal noncoverable teams.

Observed output:

`CONSTANCY_COHERENCE_VERIFY_OK exhaustive_teams=788 failures=337 minimal=54 random_minimal=268 tensor_pairings=30790 cube_levels=1..6`

Exhaustive universes: dimension 1, alphabet 2; dimension 2, alphabet 2; dimension 3, alphabet 2; dimension 2, alphabet 3. All 788 subteams were considered. For larger alphabets, a fixed-seed sample of 140 random teams in each of dimensions 3 and 4, alphabet 3, was reduced to inclusion-minimal obstructions when possible. Binary cubes were checked in dimensions 1 through 6. Every tested minimal obstruction had a valid diagonal dual pairing, hence tested size at most the tensor dimension; every checked cube was minimally noncoverable.

The computational result is not an exhaustive classification of arbitrary dimensions, alphabets, or infinite teams. Infinite finite character and the exact universal upper bound require the inductive and linear-algebraic arguments in `RESULT.md`. The distinguishing constructions cover both the \(n+1\) and \(2^n\) endpoints. Source priority has not been independently audited.
