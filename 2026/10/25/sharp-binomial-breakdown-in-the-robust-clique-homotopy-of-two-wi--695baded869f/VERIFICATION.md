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
# Reproducible finite verification

Run `python3 verify.py` with only the Python standard library. The program constructs both labeled grids, checks independence numbers by two distinct complete-mask algorithms, constructs a deterministic element-toggle matching separately for each relevant integer parameter, verifies the complete incidence-oriented Hasse digraph is acyclic using a topological sort, and verifies critical-cell counts and reduced Euler characteristics. `CHECK_RESULTS.txt` contains the actual observed output. The end marker is `VERIFY_OK`.

This checks all \(32768\) vertex masks of the \(3\times5\) grid and all \(262144\) vertex masks of the \(3\times6\) grid. It proves only the explicitly tested finite cases. The homotopy conclusion then uses the standard discrete-Morse CW theorem and the fact that no critical cells occur in intermediate dimensions. This is self-review and not external validation.
