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

# Verification and reproducibility

Run `python3 verify.py` in this folder. The script uses only the Python standard library: it computes all binary-source profiles for lengths two through seventeen and independently counts feasible de Bruijn edge-frequency vectors by graph-flow enumeration for totals zero through thirteen. Each matches the corresponding rational-function coefficient. It concludes with `VERIFY_OK`.

For the symbolic derivation run `python3 derive.py` with SymPy installed. This implements exactly the finite geometric-series formulas given in the proof, simplifies the full symbolic rational function, prints its first twenty-two coefficients, and compares source-word enumeration through length seventeen. The `derive.py` printout is evidence of *algebraic replay*, not a substitute for inspection of the degree/connectedness lemmas. Both scripts are provided as independent standalone files with no external data dependencies.

The infinite theorem is established by the Euler-trail criterion, connectivity argument and rational series identities in the proof; finite enumeration alone cannot establish it. The eight-coordinate profile deliberately omits source endpoints and all shorter read counts. The known initial eighteen terms are acknowledged as prior work, not asserted original. No independent external audit has been performed.
