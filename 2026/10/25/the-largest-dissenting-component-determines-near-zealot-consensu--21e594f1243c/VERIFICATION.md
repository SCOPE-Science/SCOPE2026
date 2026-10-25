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

The companion `verify.py` constructs state-transition generators from adjacency lists, computes the recursion coefficient independently, and compares it with symbolic exact-rational mean absorption times. Checked examples include a three-leaf star, three-free-agent clique, a path, a two-plus-one disconnected induced free-agent graph, and a two-zealot clique. Run from this directory with `python verify.py` (requires SymPy). Expected final line: `All exact symbolic assertions passed.`

For the three-leaf star, the exact mean is \(11/(3\delta)\). For the three-free-agent clique, the exact mean is \((25\delta^2+8\delta+16)/(6\delta^3)\). The analytical finite-state perturbation and renewal argument, not finite experimentation, establishes the general theorem. No formal infinite-graph or independent proof verification was performed.
