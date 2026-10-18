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

# Reproduction

Execute `python3 verify_chvatal.py` and `python3 verify_modular.py` after installing the exact SymPy version listed in `requirements.txt`. The first script reconstructs the full graph, face poset, acyclic discrete-Morse vector field, integral Morse boundary, 423 induced octahedral cycles, and integer Smith spanning certificates. The second independently regenerates all faces and computes modular simplicial boundary ranks.

Observed exact output from the first executable:

```text
VERIFY_OK GRAPH_12_24 F_VECTOR_24_204_752_1175_628_52
MORSE_ACYCLIC_1399_PAIRS CRITICAL_1_32_4
INTEGRAL_MORSE_SNF_1_1_1_3 H3_Z28_PLUS_Z3
MINIMAL_OCTAHEDRA_423 EXACTLY_ONE_ORDER3_422_INFINITE
ORDER3_BLOCKS [(2, 3), (4, 6), (10, 14), (15, 16)]
INTEGRAL_GENERATION_SNF_32_UNITS VERIFY_OK
```

The second script reports boundary ranks (degrees three to five) 571,576,52 in characteristics 2,5,7 and 571,575,52 in characteristic 3. These machine checks are exhaustive for this explicit finite graph but are not a substitute for independent scientific scrutiny.
