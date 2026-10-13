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

The proof is analytic. Let \(G_V\) be bipartite and choose \(s_a\in\{-1,+1\}\) with \(s_as_b=-1\) on each edge. The unitary \(U\) defined by \((U\psi)_a=s_a\psi_a\) satisfies
\[
UK_TU^*=K_T,\qquad UV^{\mathrm d}U^*=V^{\mathrm d},\qquad UV^{\mathrm{od}}U^*=-V^{\mathrm{od}}.
\]
Hence \(UH_T(\lambda,\kappa)U^*=H_T(\lambda,-\kappa)\). Equality of spectra and of the positivity sets used to define \(T_c\) follows immediately.

For the converse gauge statement, a diagonal phase gauge requires \(e^{i(\theta_a-\theta_b)}=-1\) on every nonzero inter-band block. Such phases exist exactly when every cycle has even length, i.e. exactly when \(G_V\) is bipartite.

No finite computation is used. The result does not claim that non-bipartite graphs necessarily produce sign-dependent \(T_c\); they only obstruct this global bandwise sign gauge.
