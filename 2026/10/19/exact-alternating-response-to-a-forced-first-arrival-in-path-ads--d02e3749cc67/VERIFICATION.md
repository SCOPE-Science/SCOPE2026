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
# Reproduction and evidentiary limits

Run `python3 rsa_path_first_arrival_verify.py` with Python 3 standard libraries only. The verifier checks all vertex permutations for paths of sizes \(1\) through \(8\), comparing the direct exact mean both unconditioned and conditional on the first proposal against separate recurrence computations. It then evaluates all sites on every path of length at most \(100\) with exact rational arithmetic, checking the predicted strict signs, exact zero exceptions, and the interior factorial upper bound. The expected output is `PASS: 44 direct-arrival rational checks; 5050 sign and bound checks; n<=100.`

No finite check certifies the infinite family. The all-size result depends on the analytic remainder identity, monotonicity of its positive integral and the complete parity case split in RESULT.md. The accessible prior literature already establishes the unperturbed mean and its conditional-first decomposition; the contribution is the new comparison theorem. Source coverage is limited by inaccessible full texts and may miss an unindexed equivalent claim. No external independent audit has been performed.
