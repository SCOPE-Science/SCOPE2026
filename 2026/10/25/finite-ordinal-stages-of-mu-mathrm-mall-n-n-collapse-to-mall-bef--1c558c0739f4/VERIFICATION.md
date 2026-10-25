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

The following proof checks support the stated finite-stage claim:

1. For every finite \(\beta\), the family \(\{\gamma:\gamma<\beta\}\) is finite, so the translated additive connectives have finite arity and can be encoded by binary MALL connectives.
2. The \(\mu^\beta\) inference chooses one lower approximant, matching an additive-disjunction introduction; the \(\nu^\beta\) inference requires all lower approximants, matching additive conjunction.
3. The zero stages translate to \(0\) and \(\top\). Induction on annotations and syntax terminates because every same-binder recursive call decreases \(\beta\), and nested subformulas are handled recursively.
4. Translation is uniform when the finite numeral \(n\) is input. The target MALL sequent has finite cut-free proof search.
5. The \(\Sigma^0_{\omega^{\omega^\omega}}\)-completeness statement at \(\alpha=\omega\) is cited from Theorem 2.8 of arXiv:2602.10280; it is not presented as a new proof here.

Limits: no time/space complexity bound for the finite translation is established; no independent audit or external certification has been performed. The trusted importer initializes absent external channels as unperformed; research does not assess or author them.
