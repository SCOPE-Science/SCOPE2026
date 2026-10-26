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
# Verification
Run `python3 verify.py` with standard Python 3. The script computes every binary starting configuration of the explicitly constructed graph (2048 cases). It independently checks forcing by parallel steps and by sequential single-step updates, verifies triangle-freeness and 4-chromaticity by backtracking, checks every of the 175 minimum sets and their 19 symmetry orbits, and constructs the optimum token-jump graph in two ways. Breadth-first search from each optimum computes every asserted pair distance. The program raises an assertion failure if any claim fails, and prints `VERIFY_OK` only at completion. `orbit_types.csv` lists zero-based representative masks in human-readable index form, and is regenerated from the program output.

No external proof assistant, experimental extrapolation, inaccessible network resource or precomputed database is used. This checks a finite graph only; no claim of validation by independent parties or of global absence of prior coverage is made.
