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

## Reproduction

From the package directory, run `python3 verify.py` with a standard Python 3 interpreter; no third-party modules are required. The program applies the original neighbor-equality utilities rather than using the proposed potential in its direct cycle checks. It reports 6600 graph/type/action combinations, 4812 cross-type cyclic instances, and 203904 exact potential-identity comparisons in CR-free configurations, and checks the three-vertex coexistence witness and action-cardinality boundary.

## Mathematical proof boundary

This finite search does not establish the theorem for arbitrarily large networks. The proof in RESULT.md does: absence of CR edges gives a bounded exact potential on every finite graph, and a single CR edge embeds a length-four strictly improving cycle using two actions absent among stubborn agents, while all other flexible agents use a third action. The latter constructs one permissible infinite improvement trajectory; it does not assert nonconvergence for a specified random scheduling rule. Neither programmatic checks nor self-review constitutes independent mathematical audit.
