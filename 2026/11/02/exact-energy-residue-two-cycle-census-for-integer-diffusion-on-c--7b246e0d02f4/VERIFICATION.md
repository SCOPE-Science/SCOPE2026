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

The exact mathematical claim and its universal proof are in `RESULT.md`. Run the included `verify.py` with Python 3 to reproduce the finite checks without external packages. The embedded `verification_output.txt` records the successful execution.

The checker independently enumerates normalized nondecreasing integer-height profiles for clique sizes 2 through 9, computes the original vertexwise update twice, counts periodic states by conserved total modulo the clique size with multinomial label factors, and compares these counts with a separate composition-and-gap implementation. It examines 379,706 profiles and also stress-tests 324,504 further profiles exceeding the proposed periodic spread bound through size 7, finding none periodic. It verifies 26 explicit extremal witnesses through size 29. It also checks the claimed extreme-spread multiplicity for sizes 4 through 9.

These are finite checks only. The all-size result follows from the sign-reversal, potential, integer-height congruence, and sharp-spread arguments in `RESULT.md`. No independent scientific audit has been performed.
