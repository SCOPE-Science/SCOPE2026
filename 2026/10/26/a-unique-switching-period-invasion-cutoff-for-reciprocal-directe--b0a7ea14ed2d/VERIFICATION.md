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

# Verification record

The standalone `verify.py` (Python standard library only) was executed successfully from the supplied package source. It tested 300 random independent Floquet-exponent reconstructions via direct multiplication of both layer exponentials; 250 derivative comparisons to the exact concavity identity; the sign bracket and unique root of the \(a=9\), \(b=1\), \(\beta=1\), \(\mu=4\) example; three near-critical square-root comparisons; and the exact-symmetry limiting case. These checks are finite numerical corroboration, **not** substitutes for the determinant/trace proof, strict concavity argument or endpoint asymptotics.

Observed bracket \(0.9472132<T_c<0.9472133\); numerical approximation \(T_c\approx0.9472132582826853\). Comparisons use floating-point tolerances (up to \(5\times10^{-7}\) for cancellation-prone determinants). Analytic theorems cover every positive parameter in the stated domain, including finite periods arbitrarily close to the critical value.

Known limitations: no independent mathematical audit; no general claim for unequal residence weights or finite-state stochastic survival.
