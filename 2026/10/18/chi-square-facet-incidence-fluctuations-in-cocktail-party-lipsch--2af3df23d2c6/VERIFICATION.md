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

The exact checker `verify.py` is self-contained and uses only Python's standard library. Execute with `python3 verify.py`. For each of \(m=3,4,5,6\), it enumerates all normalized integer potential vectors with coordinates in \(\{0,1,2\}\), tests edge Lipschitz constraints, determines a tight-edge subgraph, and verifies its connectivity. It independently enumerates facet orbits under pair swaps, pair permutations and sign inversion. It compares the results with the symbolic incidence polynomial, exact first and second moments, symmetry-orbit count, and extremal-incidence multiplicities. These are complete finite-domain tests for those four parameters.

Expected counts are 56, 246, 1012, 4082 facets; 5, 8, 11, 15 orbits, with respective maximal incidences 8, 16, 24, 36 attained by 24, 6, 80, 20 facets. The exact incidence histograms are reproduced in RESULT.md. The checker was executed successfully on the packaged program source, and the log is included separately for comparison.

The derivation for every integer \(m\ge3\), and especially the central-limit statement, relies on the mathematical proof, not enumeration. There is no independent scientific audit or external certification.
