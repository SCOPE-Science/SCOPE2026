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

The scientific reduction is Wang and Zenger's finite-basis lemma: \(\mathbf G(\alpha)\) holds exactly when \(R_\alpha\subseteq R\). Their word-relation lemma fixes the convention \(R_{\beta\gamma}=R_\gamma\circ R_\beta\). With these two facts, the theorem reduces to six finite relation calculations plus the identity \(R_x=R\).

The packaged checker evaluates the seven words \(\epsilon,x,\overline{x},xx,x\overline{x},\overline{x}x,\overline{x}\overline{x}\) on the six displayed witness frames. It asserts that each chosen nontrivial condition is true and the other five are false. A successful replay prints `VERIFY_OK`.

The checker was replayed from the packaged path after construction. Its finite computation verifies only the displayed witness table. The general non-implication conclusion follows because a single finite frame is a valid countermodel to a proposed semantic implication. No finite enumeration is used to infer that an implication holds on all frames.

The claim does not cover longer words, conjunctions of GPCs, proof-search termination, or finite-model properties.
