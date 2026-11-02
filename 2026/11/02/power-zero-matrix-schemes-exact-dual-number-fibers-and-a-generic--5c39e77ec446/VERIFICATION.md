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

Run `python3 check_power_lifts.py`. The script uses standard-library arithmetic, including genuine characteristic-two degree-two extension-field multiplication, and does not require external data. Expected output is embedded in `check_output.txt`.

The program independently computes powers in dual-number matrix rings, enumerates all matrix pairs in the stated cases, evaluates the combinatorial formula from partition-orbit sizes, and compares the results. It checks the matrix-power differential rank by direct modular Gaussian elimination in 612 rectangular cases (characteristics two, three and five), and verifies 72 dense-partition dimension calculations. Its last line must read `ALL_NILPOTENT_MATRIX_POWER_LIFT_CHECKS_OK`.

This does not exhaust arbitrary matrix sizes or prove generic reducedness; these are established by the written mathematical argument. The checker does not attempt to certify historical priority or perform independent mathematical review.
