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

Run `python3 verify.py` in a directory containing the supplied standalone source. It uses only the Python standard library. On the provided source, the run printed `PASS exact assertions: 14234` after enumerating every insertion word through \(n=12\).

For each enumeration case it reconstructs a permutation using the two inversion-tree insertions, separately builds the inversion graph from all inversion pairs, computes all vertex degrees and a breadth-first-search diameter, and compares the outcomes with the run composition. It then checks all exact conditional means, total mean, variance and covariance using rational arithmetic. Through \(n=10\) it checks every adjacent-cut split, equal degree sums, each sorted-degree partial-sum inequality, and strict squared-degree improvement.

The all-size theorem follows from the mathematical proof, not finite verification. No computational experiment establishes historical originality, and no external or independent audit has been conducted. The Gaussian limit is proved by the renewal-reward argument using four explicit geometric moments, not by a finite Gaussian fit.
