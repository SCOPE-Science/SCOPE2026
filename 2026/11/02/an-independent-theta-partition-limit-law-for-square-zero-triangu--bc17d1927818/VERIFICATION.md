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

# Reproducibility
Run `python3 verify.py` in a directory containing this file and the script. The verifier uses Python's standard library, independently enumerates every binary strictly upper-triangular matrix in dimensions 1 through 6, checks the absence of length-two directed paths, reconstructs the source/sink Ferrers partition when no vertices are isolated, and checks the total against the independent q-Stirling recurrence. Expected terminal output ends with `VERIFY_OK`; the expected total counts are `1, 2, 6, 26, 158, 1330`.

These exhaustive checks cover precisely dimensions 1–6 and nothing larger; they do not establish the infinite-dimensional limit. The limit follows from the proof's canonical support partition, fixed-diagram nonempty-row bound, exact isolate convolution, and dominated convergence. The proof does not use numerical fitting or statistical inference.
