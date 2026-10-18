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

Run `python3 check.py` from the directory containing this file. The program uses only the Python standard library. It computes exact rational longest-cycle cumulative probabilities using the recurrence in RESULT.md, checks the marked-cycle covariance formula and sharp sign assertions for every \(n\) from \(2\) to \(35\), and separately enumerates every permutation through \(n=8\) to compute covariances without using the marked-cycle identity. It was run successfully with the output `PASS: exact recurrence n<=35; exhaustive permutation enumeration n<=8.`.

These computations verify a finite portion of an infinite family. The all-parameter correctness argument is the separate combinatorial proof in RESULT.md: cycle marking, uniform insertion growth, fixed-label cycle distribution, and an elementary truncation inequality. The Golomb–Dickman limit is taken from the cited classical literature, not inferred from finite data. Independent audit and external validation have not been performed.
