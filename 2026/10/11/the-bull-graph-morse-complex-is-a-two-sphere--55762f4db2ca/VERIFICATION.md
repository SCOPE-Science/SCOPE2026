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

Run `python3 verify_bull_morse.py`. The script uses only the Python standard library and reconstructs the graph, primitive gradient fields, all simplices, the full Hasse diagram, the discrete-Morse matching, and finite-field chain complexes from definitions.

The expected exact data are: ten primitive fields; face vector \((10,33,40,15)\); \(98\) nonempty faces; \(246\) Hasse covers; \(48\) matched pairs; critical vector \((1,0,1,0)\). The Morse-oriented Hasse diagram must be acyclic. The signed boundary ranks must be \((9,24,15)\) over each of \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), giving Betti vector \((1,0,1,0)\).

A successful replay ends with `VERIFY_OK`. The homotopy conclusion rests on the complete acyclic matching; the finite-field computations are independent consistency checks. No statement beyond the specified five-vertex graph is verified.
