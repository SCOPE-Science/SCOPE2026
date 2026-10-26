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
# Reproducibility and limits

Run `python3 verify_fractional_torus.py` from the extracted package directory. It uses only the Python standard library and prints `VERIFY_OK` on success. The execution was completed against this packaged script.

For the sample parameters \(\beta\in\{1/4,1/2,3/4\}\) and sample horizons \(n\in\{512,1024,2048\}\), it checks bounded Birkhoff sums and normalized displacement for five sample coordinates; monotonic Birkhoff-phase differences on a lower-bound visit-time strip; existence of circular separation of nearby initial fractional coordinates; and positive base-coordinate separation between two visit-time strips. The checks use ordinary floating-point arithmetic and do not claim exhaustive verification over continua or unbounded times.

The proof depends instead on the analytic estimates for the tail amplitude and derivative, an explicit Bowen spanning cover and the first-crossing separation argument. The numerical tests cannot establish mathematical novelty or substitute for these estimates. No independent audit is asserted.
