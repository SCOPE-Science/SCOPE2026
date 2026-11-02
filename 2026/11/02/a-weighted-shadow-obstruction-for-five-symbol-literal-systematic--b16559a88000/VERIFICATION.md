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

# Reproducibility of the weighted-subsequence converse

Run `python3 verify_shadow.py` with Python 3. It requires no third-party packages. The recorded output appears in `verify_shadow_output.txt` and was produced by executing this exact source file.

The checker exhaustively enumerates all 52 canonical equality patterns of length five; checks the minimum weight according to equality of the first two symbols; independently enumerates actual words for every alphabet size from two through seven; calculates the total ambient output weight by direct enumeration and by the symbolic polynomial; and evaluates the packing gap for each alphabet. These are exact computations. The mathematical reduction from shadow disjointness to the weighted upper bound is written in `RESULT.md`.

The certificate proves impossibility for alphabets of sizes two through six. It does not attempt to determine feasibility for seven or more symbols. No independent audit has been performed.
