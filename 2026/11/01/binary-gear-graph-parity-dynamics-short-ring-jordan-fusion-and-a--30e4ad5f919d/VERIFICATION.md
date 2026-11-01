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

# Reproducible checks

Run `python3 gear_verify.py` from the folder containing `gear_verify.py`. The program uses only Python 3's standard library. Its stdout must match `gear_verify_output.txt` and begin with `VERIFY_OK`.

The program constructs independent binary adjacency matrices for each simple gear graph, computes exact matrix ranks for successive powers, compares exact return-time kernel ranks against direct polynomial-gcd arithmetic, and exhaustively classifies states on six small graphs by direct trajectory iteration. All parameter ranges and results are recorded in the output file: 2,326 zero-primary rank checks, 1,984 fixed-point checks, and 174,720 exhaustively visited states. The exact infinite-family argument appears in `RESULT.md`, including the primary-factor decomposition and the required nonstandard rank calculation. No finite computation is used as an infinite proof.

An independent audit has not been performed; the metadata above describes an unperformed channel, not evidence of validation.
