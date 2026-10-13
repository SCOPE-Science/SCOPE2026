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

The proof was replayed directly from the published definitions.

1. Start with an arbitrary rule with premises \\(\\Gamma_i\\Rightarrow\\Delta_i\\) and conclusion \\(\\Gamma\\Rightarrow\\Delta\\).
2. Apply \\(f=(\\ell,\\rho)\\), then \\(g=(p,q)\\). The resulting premises are \\(p(\\ell(\\Gamma_i))\\Rightarrow q(\\rho(\\Delta_i))\\), and the conclusion is \\(p(\\ell(\\Gamma))\\Rightarrow q(\\rho(\\Delta))\\).
3. Compare with one translation by \\(g\\circ f=(p\\circ\\ell,q\\circ\\rho)\\). The rule schemata are identical, proving strict equality of iterated and composite rule translation.
4. Apply the equality elementwise to obtain the translated-calculus and union identities.
5. Chain the defining implication for soundness through the intermediate calculus. Reverse the implication chain for faithfulness.
6. Check identity and associativity componentwise from ordinary function composition.

No experimental enumeration, finite approximation, or external formal certificate is used. The proof covers arbitrary premise index sets allowed by the source rule convention, arbitrary multi-succedent sequents, distinct underlying languages, and calculi without cut or reflexivity.

The verification establishes only the structural composition theorem. It does not establish soundness or faithfulness for any particular concrete logical translation, and it does not eliminate the residual literature risk that an equivalent categorical observation exists under another terminology.
