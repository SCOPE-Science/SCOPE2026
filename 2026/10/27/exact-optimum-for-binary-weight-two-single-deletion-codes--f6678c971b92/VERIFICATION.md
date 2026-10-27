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

The theorem is established by the resource-capacity proof and construction in `RESULT.md`. To reproduce finite checks, place the embedded `check.py` in the same folder and run `python3 check.py` using Python 3.8 or newer; the script requires only the Python standard library.

The script independently constructs each candidate binary word and every exact single-deletion descendant by deleting one literal character. It compares the resulting one-marker descendants with the required position rule for every pair of marked positions at lengths \(2\) through \(40\), performs a separate branch-and-bound maximum-independent-set census at lengths \(2\) through \(8\), and verifies deletion-ball disjointness of the explicit code at each of those lengths and selected lengths through \(200\). Passing such finite tests does not prove the universal optimum; the proof establishes every \(n\ge2\).

Boundary checks: length \(2\) has only the word `11`, and the upper-bound argument includes the case of no adjacent-start neighbors. The construction uses only in-range positions, so all integer residue classes are valid. The historical-priority conclusion remains provisional pending independent literature audit.
