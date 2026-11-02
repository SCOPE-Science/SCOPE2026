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

# Verification summary

The program `verify_jump_bipartite_cutoff.py` is standalone and uses only the Python 3 standard library. Execute `python3 verify_jump_bipartite_cutoff.py` in the same directory.

Its exact rational sweep examines all \(K_{s,t}\) with \(s,t\ge1\), \(3\le s+t\le6\), all positive two-color population sizes and at least one vacancy, and all preference-comparison cells of \(0<\Lambda<1\). Every transition is recomputed after moving the selected agent. A DFS detects any directed cycles. The observed total is **3,079** graph/composition/peak instances, **140,610** configuration/parameter pairs and **216,828** strictly improving transitions, with the complete classification asserted. The witness's four edge moves and all eight exact fraction values are separately asserted.

The infinite set of real peak choices is reduced by a mathematical argument: all local fractions have denominator at most six; two candidate fractions can change their utility ordering only at their analytically calculated rational crossing. Tests cover all crossings and one interior point from each gap. No Monte Carlo computation, numerical tolerance, sampling of unbounded graph sizes or unproven extrapolation is used.

The code's enumeration of finitely many states certifies only the finite-order range. It does not replace a proof for larger graphs or verify related utility models without the source's reflected-branch property. Independent audit has not been performed.
