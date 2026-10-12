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
# Exact verification

Execute `python3 verify.py` in the directory with the proof. No optional packages, network requests, random seeds, or numerical tolerances are required. The script multiplies two rational phase-space maps exactly, tests both trace factorizations on a rational parameter grid, checks the determinant identity, samples rational parameter pairs from both stable and unstable regimes, and verifies exact rational witnesses. The proof in `RESULT.md` establishes the universal classification by the matrix identities and the full Jordan-boundary analysis; finite checks cannot replace it.
