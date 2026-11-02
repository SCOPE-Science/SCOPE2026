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

Run `python3 verify_odd5.py` with the Python standard library. The program reconstructs all \(126\) four-subset vertices and disjointness edges, independently evaluates all \(15{,}876\) ordered shortest-path distances by BFS, and compares all \(79{,}380\) distance-regular recurrence entries. It checks five exact adjacency eigenvalues and multiplicities via integer traces, and independently checks powered-distance spectral sums at exponents \(1,2,3\). It calculates a high-precision diagnostic approximation to the unique critical root.

The script's expected final line is `ALL_ODD_GRAPH_KG94_CHECKS_OK`. This script has been executed successfully. The proof of the interval-wide sign inequalities, uniqueness of the two transitions, and minimum embedding ranks is analytic and written in `RESULT.md`; those claims must not be inferred from the finite checks alone.

Scientific status: self-review passed; independent audit not performed.
