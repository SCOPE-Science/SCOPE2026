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

# Reproduction and limits

Run `python3 checker.py` with Python's standard library. The script independently enumerates all labeled attachment histories through size eight, checks the corresponding killed seed-pair chain state by state, proves sample star boundary identities by exact fractions, tests all finite harmonic lower inequalities through size 35, and verifies the proposed product supersolution at 576 pairs of positive integer counts. It additionally probes three large sizes using floating point. Its deterministic output is `PASS: 720 exact comparisons, rational inequalities, and asymptotic probes`.

The checker is a finite verification aid, not a proof of an all-size statement. The all-size proof is the analytic transition decomposition, the summable first-entry flux, and the explicit harmonic positive supersolution given in `RESULT.md`. Neither an independent audit nor an external formal proof has been performed.
