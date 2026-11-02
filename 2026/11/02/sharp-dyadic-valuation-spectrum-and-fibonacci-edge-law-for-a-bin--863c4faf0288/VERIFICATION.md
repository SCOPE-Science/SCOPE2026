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
# Verification and limits

Run `python3 verify.py` after extracting all supplied files. Its direct binomial parity computations use the Lucas bit-subset condition; its run-based calculations use a separately implemented valuation; and its distribution recursion independently appends binary bits. The expected output is:

`VERIFY_OK: 4096 independent binomial-sum values, 2000 run-deficit inequalities, 121 full distribution recurrences, 262143 brute binary values and extremizer counts through r=17`

The exact proof uses the published run-length identity and symbolic token/deficit arguments. Computations are finite supporting checks, not infinite certification. The full source identity and the two inspected mathematical papers are cited in RESULT.md. No external independent audit or certification has been performed.
