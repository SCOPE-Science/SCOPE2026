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

# Verification and reproducibility

The proof uses the exact Brownian hitting-time Laplace transform and the first-reset renewal identity. Differentiating the exact mean in \(u=\sqrt r\) gives \(uF'(u)/F(u)=h(u)-2+u\mu(u)\). The uniform dominance inequality \(|\mu(c/a_j)/a_j-1|<0.01\), at \(c=1/2\) and \(c=2\), follows from two convergent geometric/superexponential tail bounds independent of \(j\) and finite \(N\). It implies strict alternating derivative signs and thereby the claimed local extrema for **every** finite \(N\).

Run `python3 check.py` with Python 3 standard library. In the completed check it printed `PASS: 1287 assertions across k=1,...,20; exact proof handles every k.` Checks include uniform bounds, signs, disjoint intervals, bisection brackets, and independent finite-difference comparisons. The script is not an infinite-\(N\) certificate and its finite tests are not treated as an infinite proof.

Scientific limits: no equality or coexistence of global minimizing rates is proved; no upper bound on the total number of local extrema is derived; non-Poisson, state-dependent or continuous-location resetting distributions are not covered. Independent audit has not been performed.
