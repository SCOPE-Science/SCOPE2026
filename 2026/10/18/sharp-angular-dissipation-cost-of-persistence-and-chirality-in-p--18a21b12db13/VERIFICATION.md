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

# Verification of the angular dissipation tradeoff

`verify.py` is a standalone Python-standard-library script. Execute it with `python verify.py` in this directory. The verified output was:

```
PASS random reflected turning kernels: 240 comparisons
PASS exact two-angle optimizers: 6 comparisons
PASS constrained narrow bump approximation: 5 comparisons
PASS finite cyclic orientation Markov chains: 64 comparisons
PASS quadratic weak-chirality asymptotic: 3 comparisons
TOTAL 318 checks passed
```

The random tests represent independent finite reflected-pair kernels and check their stationary entropy-production costs against the proposed universal minimum. Six exact optimizer instances check first-moment constraints and equality. The narrow-bump tests check that both prescribed first moments are retained exactly while reflection entropy approaches the minimum. On finite cyclic orientation spaces, the entropy is computed independently from stationary directed-edge fluxes; this checks the factor of the jump rate and reflection normalization. The small-chirality comparisons test the predicted quadratic coefficient. All 318 are numerical/algebraic tests on finite examples; they do not establish the infinite family of turning laws. That universal statement is proved using measure symmetrization, Cauchy–Schwarz, Jensen's inequality, and explicit equality conditions in `RESULT.md`.

The boundary convention is that positive probability for turns whose reverse has zero probability gives infinite jump relative entropy. The theorem covers such singular laws as an extended-value inequality, but the finite numerical checks do not attempt to certify singular-law behavior in every measure class. The orientational rate is not the complete energetic dissipation of a self-propelled particle. Independent validation has not been performed.
