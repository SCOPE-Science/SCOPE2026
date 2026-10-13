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

Execute `python3 verify.py`. The program has no third-party dependencies. It reconstructs the projective matrix groups, computes rational-function trace numerators by polynomial division over \(\mathbb F_{11}\), and evaluates the resulting morphism on the entire \(\mathbb P^1(\mathbb F_{121})\). It uses the exact field model \(\mathbb F_{121}=\mathbb F_{11}[u]/(u^2-2)\), verifies that all tangents at multiple image fibers are distinct, and checks that the ordinary-point contributions saturate the arithmetic genus \(55\).

Observed successful output:

`VERIFY_OK: 122 source points; 25 nodes, 6 triples, 2 quadruples; all transverse; delta 55; 5 F11-rational nodes`

The finite-field enumeration alone would not prove absence of geometric singularities over larger fields. Exhaustiveness follows from the birationality proof and the arithmetic-genus delta identity, which leaves no remaining delta contribution. No proof is claimed for other trace-coordinate embeddings or other characteristics. Independent auditing has not occurred.
