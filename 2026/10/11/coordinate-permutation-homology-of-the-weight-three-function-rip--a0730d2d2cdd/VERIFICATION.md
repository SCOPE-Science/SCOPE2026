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

# Reproducibility and scope

Run `python3 verify.py` with Python 3. The standalone script uses only the standard library and exhaustively enumerates the simplicial faces of the weight-three sublevel in dimensions three through six. It verifies all coordinate-permutation Lefschetz characters (respectively 6, 24, 120 and 720 permutations), as well as the local graph-dominance and line-graph reduction for every triple in dimensions three through seven. The expected terminal message is `VERIFY_OK`.

The dimension-four exhaustive character comparison is a **finite** step of the mathematical argument: it identifies the one-dimensional quotient as the sign representation. The general decomposition for every dimension additionally requires the uniform link reduction, the nullhomotopic-link attachment and the coordinate-retraction independence proof in RESULT.md. These infinite-family steps cannot be certified solely by finite enumeration. The checks do not assess other function levels, integral representation decompositions or persistence death times.
