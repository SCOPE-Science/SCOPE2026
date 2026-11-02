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

# Verification and reproducibility

The finding is proved by an exact all-parameter classification of ordered-pair extension possibilities and the corresponding three-round game-type recurrence. Finite computations are corroboration only; no finite sample is used as a proof of stabilization.

Run `python3 verify_profiles.py` to enumerate every ordered-pair third-vertex adjacency pattern for all \(66\) unordered path-length pairs \(2\le m\le n\le12\). The script independently compares the resulting sets of rank-two pointed profiles with the five-class table. Its expected output is included in `verify_profiles.out`.

Run `python3 verify_recursive.py` to calculate full first-order rank-three types by recursively extending atomic equality/adjacency diagrams, without using the geometric pair-code classification. This independently checks \(27\) grids, including the five representative graphs, all unordered dimensions up to seven and selected larger boundaries through \(8\)-by-\(8\). Its expected output is in `verify_recursive.out`.

Both checks were executed directly from these source files and passed. The standalone programs require only Python 3 standard library modules. They do not prove any claim for larger parameter values beyond the cases enumerated. The infinite-dimensional conclusions depend on the complete case analysis in the proof.

Independent mathematical auditing and exhaustive historical-priority verification have not been performed.
