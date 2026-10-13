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

Execute `python3 verify.py` using Python 3. The verifier exhaustively evaluates all \(2^4\) binary and \(2^9\) ternary subsets of the complete two-letter word spaces. For both edit directions it counts distinct compatible codewords for every possible received word and reports exact maxima. It checks the explicit ternary six-word witness independently. For each integer \(2\le q\le24\), it constructs all diagonal words plus a matching (deletion) and the bidirected balanced bipartite family (insertion) and checks every received word. Its observed concluding line is `VERIFY_OK`.

The general-\(q\) proof is symbolic: each deletion output contributes at most two incidences, the bipartite insertion construction has at most two cross-part position pairs, and the ternary equality case follows from a six-permutation count and the digon/loop obstruction. No unrestricted insertion optimum beyond \(q=3\) is claimed. Independent audit evidence is not available.
