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

# Reproducibility and scientific boundaries

The welfare payoff table was reconstructed from Section 5.1 of the cited June 2026 article, which contains the four pure action profiles with domestic deadweight losses and partner-induced export losses. The theorem assumes \(D_A,D_B>0\), fixed additive losses and no subsidy. Recompute the tariff-versus-no-tariff gap in each country at both opponent actions; it is always exactly the negative domestic deadweight loss. Affinity in the partner's tariff probability then has zero slope. Verify the binary replicator differential equations by substitution and the displayed logistic solutions by exact differentiation.

`verify.py` checks these symbolic identities using SymPy, together with a separate exact rational sample. Running `python verify.py` in the actual package returned `VERIFY_OK`. No approximate eigenvalues, finite sampling, or unproved numerical continuation are used to establish the theorem.

The dynamic convergence statement is restricted to strictly interior policy frequencies. Boundary pure strategies remain fixed under replicator dynamics even when they are not Nash equilibria. The algebra does not decide which of the original article's two inconsistent representations was intended and makes no claim about implementation or real-world optimal tariffs. The claimed source-specific originality has not undergone independent audit.
