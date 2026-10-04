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

The proof was checked symbolically. No finite experiment or numerical approximation is used.

1. For an ergodic time-\(t\) MME \(\nu\), commutation gives \(T_t\)-invariance and equal entropy for every translate \((\varphi^s)_*\nu\). Averaging over one time-\(t\) interval is flow-invariant.
2. Entropy affinity and the identities \(h_{\mathrm{top}}(\varphi^t)=|t|h_{\mathrm{top}}(\varphi)\) and \(h_\mu(\varphi^t)=|t|h_\mu(\varphi)\) for flow-invariant \(\mu\) show that the average is a flow MME.
3. A flow-invariant measurable set is \(T_t\)-invariant, so ergodicity of \(\nu\) forces the average to be flow-ergodic.
4. Uniqueness of ergodic decomposition then identifies every time-\(t\) MME with a component of one of the finitely many flow MMEs.
5. In the Bernoulli-times-rotation model, irrational \(t/c\) gives an ergodic rotation, while rational \(t/c=p/q\) gives uniform \(q\)-cycle components. A Bernoulli time map is weakly mixing, so its product with each ergodic rotation component is ergodic. The rotational factor contributes zero entropy, hence every component is maximal.

Limits: the check does not compute any period \(c_i\), does not cover singular flows or finite smoothness, and does not establish independent validation. The closest textbook section was compared through its indexed text excerpt rather than an exhaustive read of the full large PDF.
