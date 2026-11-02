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
Run `python3 verify_groetzsch_four_cut.py` in an environment with the Python 3 standard library. No network, external package, copied data table or external certificate is required.

The program exhaustively builds \(\mu(C_5)\), enumerates disconnected four-sets, reconstructs all simplices, checks the exact deterministic matching, checks global acyclicity on all Hasse incidences, computes the signed integral Morse differential and independently reduces the original simplicial boundary matrices over \(\mathbb F_2\).

Expected verified values: \(180\) facets; face vector \((11,55,165,330,462,431,180)\); \(812\) nonempty matched pairs; critical counts one in degree zero, four in degree five, five in degree six; \(8,081\) nonempty Hasse incidences; zero integer four-by-five Morse boundary; binary boundary ranks \((10,45,120,210,252,175)\).

The calculation proves finite combinatorial conditions exactly. The topological conclusion then invokes the established discrete Morse equivalence and the degree-five Hurewicz isomorphism. It does not assert that other Mycielski graphs have the same behavior. Independent audit has not been performed.
