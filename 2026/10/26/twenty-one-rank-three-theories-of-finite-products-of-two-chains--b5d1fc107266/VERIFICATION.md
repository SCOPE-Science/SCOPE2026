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

# Verification evidence

Execute `python3 verify.py` with Python 3 and no external packages. The program enumerates all 28 canonical unordered grids with coordinate lengths at most seven and constructs the complete rank-three extension-type recurrence. Two independently encoded atomic diagrams induce the same equality partition on those 28 models. The code confirms the 21 class labels, 21 least representatives, the sharp 30-point maximum and the class-21 equivalences. A separate direct back-and-forth recursion tests all 64 ordered pairs of eight tiny grids; ten supplementary larger instances test the coordinate cutoff empirically. Replayed output is preserved in `verification_output.txt`.

The code does **not** establish the universal, all-size claim by sampling. The infinite statement uses the mathematically proved three-round chain interval invariant and coordinatewise product game strategy in `RESULT.md`. Its correctness depends on that argument and the exact finite enumeration, not on a finite-test extrapolation.

The published-source comparison does not guarantee that all historical equivalents have been found. No independent scientific audit has yet been performed.
