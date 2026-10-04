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

The analytic verification has four steps.

1. Under the stated primitive assumptions, the motivating stability theorem gives \(\Gamma_n\Rightarrow\Gamma\), while uniform integrability gives convergence of \(m_n=\mathbb E A_n\) and \(\mathbb E|B_n|\).
2. Perspective cancellation gives the exact absolute first moments of \(\Gamma_n\) and \(\Gamma\). Their difference converges to \(m^{-1}\int_{\{a=0\}}|b|\,dQ\).
3. A standalone clipping argument proves that for weakly convergent laws on \(\mathbb R\) with convergent absolute first moments, the limiting \(W_1\) distance equals the excess limiting first moment. This is a proof, not a numerical extrapolation.
4. Applying the call and put perspective identities and a linear-growth uniform-integrability envelope yields the one-sided boundary offsets. Equi-Lipschitzness in strike gives uniformity on compact strike sets.

`verify.py` checks a three-atom family with both positive and negative boundary payoff mass. For decreasing \(\varepsilon\), it constructs the weighted law exactly, compares its \(W_1\) distance to the predicted defect, and checks call/put offset convergence on a bounded strike grid. The script is a reproducibility sanity check only; it is not used to justify the infinite theorem.

Limits: the verification does not provide a rate theorem, does not address \(W_s\) for \(s>1\), and does not substitute finite computation for the analytic proof.
