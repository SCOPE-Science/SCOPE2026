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

# Reproducibility and verification

Run `python3 verify_direct.py` and `python3 verify_structure.py` using standard Python 3 (no external packages). The stored outputs are `direct_output.txt` and `structure_output.txt`; both scripts use assertions and end with explicit success markers. The first independently enumerates relative permutation conjugacy classes and Hamming intersections at lengths \(3\) through \(8\). The second independently checks derangement-restriction identities at lengths \(5\) through \(8\), the strict positivity bound for \(5\le n\le100\), and two published diagonal numerical examples. The all-length conclusion follows from the detailed proof, not from any finite verifier. The authoritative source for the motivating conjecture and the published numeric benchmarks is arXiv:2601.02844v1.
