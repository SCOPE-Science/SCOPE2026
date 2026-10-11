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

The proof was replayed symbolically from the final statement.

For a fixed nonzero sampling time \(t\) and target \(d<h_{\mathrm{top}}(\phi_t)\), set \(c=d/|t|\). Standard flow entropy scaling puts both the restricted topological entropy and the flow-invariant realizing measure at entropy \(d\) for \(\phi_t\). The realizing measure is therefore maximal on its compact sampled subsystem.

The proof does not assume that this measure is \(\phi_t\)-ergodic. In its \(\phi_t\)-ergodic decomposition every component has entropy at most \(d\), while the entropy average is exactly \(d\); hence almost every component has entropy \(d\). For one such component \(\nu_d\), the compact support \(K_d\) satisfies
\[
d=h_{\nu_d}(\phi_t)\le h_{\mathrm{top}}(\phi_t|_{K_d})\le d,
\]
which forces equality.

The motivating arXiv source was inspected at the entropy-flexibility definition, the strict flow-realizer theorem/discussion, and the time-one definition of flow entropy. published-finding corpus comparisons and the current/prior own ledgers were checked for equivalent real-time sampling claims. The closest prior result handles positive integer iterates only. No numerical computation, finite enumeration, or external certification is used.

Limit: the transfer hypothesis is whole-flow invariance of the entropy realizers. The argument does not derive that hypothesis from time-one entropy flexibility alone and does not preserve strict ergodicity or uniqueness for resonant sampled maps.
