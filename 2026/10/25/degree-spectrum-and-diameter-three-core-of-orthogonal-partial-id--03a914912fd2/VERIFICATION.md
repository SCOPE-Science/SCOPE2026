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

Run `python verify.py` with Python 3.10 or later and no third-party packages. The script generates partial maps independently and checks the explicit semigroup products for sizes one through five, using independent image/domain bitmasks at size six. It verifies all \((r,d,s)\) neighbor-rank counts, all vertex multiplicities, and every mutual-annihilation rank-pair count through size six; independently recomputes the graph adjacency and breadth-first distances through size four; and checks aggregated integer identities through size nineteen. Actual replay from the standalone file printed `VERIFY_OK_ORTHOGONAL_PARTIAL_IDEMPOTENT_RANK_DEGREES` and `VERIFY_OK_ORTHOGONAL_IDEMPOTENT_GRAPH_METRIC`. Exhaustive finite checks do not prove the statement for arbitrary size; the uniform bijections and path arguments in RESULT.md do that. Historical priority is not independently established.
