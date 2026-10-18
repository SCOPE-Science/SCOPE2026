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

# Reproducible verification

With `verify.py`, `cycle_cocycle.json`, and `verify_output.txt` in the same directory, run `python3 verify.py`. No nonstandard dependencies are required. A successful execution terminates with `VERIFY_OK`, and its standard output must exactly equal `verify_output.txt`.

The verifier regenerates all 65,535 nonempty subsets and uses two independent cycle tests. The six stagewise acyclic discrete Morse matchings were verified against the complete face posets (full Hasse incidence totals: 1200, 9280, 36160, 68560, 77520, 77616). Acyclicity is checked by topological sorting, not sample testing. It computes the exact signed Morse boundary at degree bound two and a unit 2-by-2 minor. The separate integral cycle and cocycle certificate is checked term by term, including all 4,360 five-simplices needed for the cocycle condition and an integral pairing of \(-1\). This latter calculation certifies the inclusion map, which cannot be inferred from homotopy types alone.

The computation proves the specified finite statements using standard discrete Morse and homotopy theorems. General-graph extrapolation, full automorphism representations, external certification, and independent mathematical auditing are outside its scope.
