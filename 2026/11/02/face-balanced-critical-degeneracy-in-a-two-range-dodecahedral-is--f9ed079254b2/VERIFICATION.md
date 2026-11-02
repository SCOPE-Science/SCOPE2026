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

# Verification record

The exhaustive checker `verify_dodecahedron.py` is included. Run `python3 verify_dodecahedron.py`: it builds the twenty-vertex graph, verifies the twelve-face and distance-two incidence identities, enumerates the entire \(2^{20}\)-configuration spin space, and compares direct energy minima against a separate face-equality census. All operations determining the claimed multiplicities use exact integers.

The analytical bounds in RESULT.md cover all positive coupling ratios and identify the exact equality conditions. The finite checker establishes the counts for those equality sets; the thermal-response limit follows from standard finite-state Gibbs convergence and the explicitly listed magnetization counts.

No independent audit, experimental verification, or certification of exhaustive historical priority has been performed. The result does not extend automatically to larger graphs, nonuniform couplings, or finite magnetic fields.
