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

# Reproducing the finite mathematical certificate

Run `python3 -m pip install -r requirements.txt` in an isolated environment and then `python3 verify.py`. Python 3.10 or later is required. The verifier uses only Python's standard library and SymPy for integer Smith normal form; there are no external data files or precomputed matrix dependencies.

Expected final messages include `FACES_OK`, `MOD2_OK ranks [19, 161, 523, 532] betti3=11 betti4=30`, `MATCHING_OK 8047 critical {-1: 1, 0: 1, 3: 13, 4: 32}`, `ACYCLIC_OK 16140 87800`, `SMITH_OK [1, 1] matrix_shape (13, 32) nonzero_entries 14`, `HOMOTOPY_OK wedge_11_S3_plus_30_S4`, and `ALL_VERIFY_OK`. Each check is asserted in code rather than represented by a stored log.

The original complex has 20 distinct facets, each a ten-vertex closed ball. The first 6814 matched pairs are valid elementary simplicial collapses; the remaining 1233 pairs are coordinate-toggle discrete-Morse pairs. All gradient incidences are checked on the complete original poset. The exact signed 13-by-32 Morse boundary has two unit Smith factors, sufficient with the explicit critical-cell dimensions for the integral homotopy conclusion. Mod-two ranks supply a separate numerical check but cannot by themselves prove the homotopy type or torsion freedom.

This verifies one finite graph, not an infinite family; an independent audit is not performed.
