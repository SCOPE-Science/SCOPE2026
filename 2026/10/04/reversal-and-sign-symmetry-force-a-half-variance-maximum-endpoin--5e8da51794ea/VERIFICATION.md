---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reversal sends the path maximum to \(S-m\) while preserving \(S\), so reversal invariance gives \(\mathbb E[Mg(S)]=\mathbb E[(S-m)g(S)]\). Global sign change sends \((M,S)\) to \((-m,-S)\), and oddness of \(g\) gives \(\mathbb E[Mg(S)]=\mathbb E[mg(S)]\). Combining yields the exact half identity. The covariance, drawdown and range formulas follow algebraically. For iid symmetric increments, \(\operatorname{Var}(S)=n\sigma^2\); Donsker plus maximal-moment uniform integrability gives \(\operatorname{Var}(M)/(n\sigma^2)\to1-2/\pi\), hence the displayed correlation. The inspected checker verifies the exact identities on deliberately nonexchangeable reversal/sign-orbit mixtures and on iid finite walks, while the proof itself is the two-symmetry argument.

## originality

PASS

Classical Spitzer theory covers the iid specialization through a much stronger joint-transform identity, but not the weak dependence class. Heinrich's author-uploaded full paper initially claims an extension to cyclic exchangeability, and the posted correction explicitly says that proof only works for iid variables because independence is required. Anis--Gharib concern marginal maximum moments under exchangeability, not this maximum--endpoint mixed moment. Resultary searches under covariance, reversal, sign symmetry and odd transforms found no prior statement matching the two-symmetry identity.

## value

PASS

The result isolates an exact component of classical maximum theory that survives under very weak dependence: only reversal and global sign symmetry are needed, not independence or exchangeability. The odd-transform family, drawdown/range companions, and explicit nonexchangeable examples make the identity a reusable structural symmetry principle rather than a single iid covariance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
