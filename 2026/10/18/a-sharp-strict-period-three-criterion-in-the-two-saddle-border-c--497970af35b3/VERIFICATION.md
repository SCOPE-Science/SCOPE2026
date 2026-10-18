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

# Verification record

The self-contained `verify.py` program uses Python standard-library `fractions.Fraction`. It checks the strict two-saddle hypothesis at the rational example; exact itinerary coordinates and return of all three points; strict Jury inequalities; and formula consistency at admissible finite rational test parameters. It prints `EXACT_PERIOD3_CYCLE_AND_SCHUR_CHECKS_OK` when successful. Run `python verify.py` from the folder containing the extracted script.

Analytically established: the universal strict admissibility and Schur-stability criterion for \(LLR\); the algebraic impossibility of a Schur-stable strict \(LRR\) orbit in the two-saddle parameter region; exclusion of homogeneous Schur-attracting primitive period-three words; and persistence of the rational witness on an open set. These are proved in `RESULT.md`, not inferred from the finite checks.

Not established: behavior at switching or eigenvalue-modulus-one boundaries; global attractor classification; existence of chaos at the rational example; publication uniqueness across all possible sources. Independent mathematical audit has not been performed.
