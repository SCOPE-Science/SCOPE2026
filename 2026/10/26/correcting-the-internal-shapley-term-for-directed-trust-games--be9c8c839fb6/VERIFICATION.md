---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

For the general identity, fix the target of the external terms in (8)–(9). Its weight increment at rank \(t\) is divided by \(t\) and appears once for the target and \(t-1\) times for its predecessors. The terminal subtraction appears \(m_j+1\) times and cancels the telescoping increment sum. Summing the first term of (8) counts each reciprocal pair's two arc weights once in aggregate. Subtracting from the grand coalition worth leaves the sum of the one-way arc weights. This is a symbolic check over the full directed trust-game class.

The original exact-rational checker `verify_trust_game.py` remains unchanged and checks the unit 3-cycle only. The recorded execution enumerated all eight coalitions (values \(0,1,2,3\) by size) and all six player orders (internal Shapley value \(1\) per player, external value \(0\), reciprocal-only internal term \(0\)). Direct substitution into the paper equations gives one external term of \(+1/2\) and one of \(-1/2\) per player, confirming the printed zero vector. The original checker does not verify the all-graph identity or parse the printed formula.
