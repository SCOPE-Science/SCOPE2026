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

# Reproducibility checks

Run `python3 verify_biclique.py` using Python 3. The script has no nonstandard dependencies and uses exact rational arithmetic. It independently solves pinned random-walk systems on explicitly labeled vertices rather than reusing the two-population formula. It then compares its feasibility decisions and all coefficients to the derived binomial polynomial. Separately it tests the universal lower and upper integer bounds over a larger rational parameter grid.

The checked finite range is \(1\le a\le b\le4\) for the direct solver, with fidelity values \(1/4,1/2,3/4\) and six stated floor thresholds. Broader direct-profile bound tests cover \(1\le a\le12\), \(a\le b\le14\), five fidelity values and nine floor thresholds. The output is in `verification_output.txt`.

The exact strict-gap witness at \(K_{3,4}\), \(\lambda=1/3\), \(\tau=1/8\) has no qualifying two-source set and exactly 31 qualifying three-source sets. Only the written concavity argument proves the infinite family statement; finite checks cannot rule out errors in other parameters or establish novelty. Independent external validation has not been performed.
