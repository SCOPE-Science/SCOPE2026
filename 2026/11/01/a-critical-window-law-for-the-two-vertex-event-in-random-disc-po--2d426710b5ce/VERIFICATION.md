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

# Reproducibility and proof boundary

Run `python verify.py` in a Python 3 environment with `sympy` and `mpmath`. The verifier, distributed as a complete standalone file alongside this document, performs two independent forms of checking: exact symbolic series inversion in the critical regime and high-precision evaluation of the original two-point distance integral. It checks the known exact probabilities for two, three, and four sample points at radius one, and compares normalized integral values against each fixed-radius and crossover asymptotic across a range of parameters.

Observed output for the packaged verifier:

`VERIFY_OK: 32 symbolic identities / integral checks; fixed-radial and critical-window comparisons`

The symbolic inversion confirms \(h(u)=\pi^4u^4/96+11\pi^6u^6/11520+O(u^8)\). The large-sample tests check convergence in selected cases \(R=1,1.1,1.5,2,4\) and \(R_n=1+\kappa/n^2\) for \(\kappa=0,1,10\). The finite tests do not establish the claimed asymptotic error bounds uniformly over infinite parameter domains. Full mathematical justification is in RESULT.md, which includes exact definitions, endpoint expansions, a beta-integral remainder estimate, and the domination argument for the critical window.

The exact all-sample-size Efron–Buchta moment identity, two-point distance density, and spindle area formula are **known inputs** and are attributed to the original literature. No separate formal proof assistant, independent reviewer, or outside certification was used.
