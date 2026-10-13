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

The construction was checked symbolically by distinguishing the root, the two parity classes of nonroot vertices, root chords, other internal chords and inter-cycle red edges. Each red matching edge is scheduled once and each scheduled gap lies strictly between the required incident two-colour edges. This gives an infinite proof independent of experiments.

Run `python3 verify_sequential_chords.py`. The supplied `verify_sequential_chords_output.txt` contains the captured output ending in `VERIFICATION_OK`. The script enumerates all admissible one-cycle chord matchings for five even cycle lengths, verifies randomly chosen multi-cycle chord/matching configurations, and directly checks the antipodal-matching family for the first 25 parameters. The pseudorandom generator is seeded. These finite checks do not establish originality or independently validate the universal theorem. The result assumes a fixed proper three-colour edge colouring and a chord on every alternating factor cycle.
