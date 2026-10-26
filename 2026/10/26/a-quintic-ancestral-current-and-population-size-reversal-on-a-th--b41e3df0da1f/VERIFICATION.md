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

# Algebraic verification

The attached `verify_fleming_viot.py` is self-contained apart from the SymPy dependency. It constructs all ten count states and eighteen distinguished-founder states from the displayed stochastic generators and exactly solves stationary and harmonic equations over \(\mathbb Q(\varepsilon)\). It checks that each row equation and the normalization is satisfied and cancels the difference between the resulting rational current and the claimed formula to zero. This is an all-parameter symbolic check, not a finite grid of interpolating samples.

An independently constructed, absorbing two-colour chain on six site-colour types and thirty-six transient states solves fixation probabilities from a separate Dirichlet problem. Two exact-rational contrast values and the published vector \((1,2,4)\) agree with the symbolic formula and literature result. The script checks strict sign bounds on the natural domain and the exact fifth-order coefficient. The supplied `verification_output.txt` records the output of running the actual included script.

The mathematical interpretation uses well-posed finite continuous-time Markov chains, unique stationary probabilities for the irreducible count chain, and eventual fixation of one ancestral label. The external four-or-more-particle cubic expansion is cited rather than recomputed; no assertion of independent audit, global priority certification, arbitrary-killing classification, or uniform-in-population sign threshold is made.
