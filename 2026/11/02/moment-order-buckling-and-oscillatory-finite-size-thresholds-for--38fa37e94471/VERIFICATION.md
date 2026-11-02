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

# Reproduction and verification scope

Run `python3 verify.py` from this directory using Python 3.10 or later. The checker uses the standard library only. Its deterministic tests verify the defining minimizer equations, the sign change when tension amplitude crosses its calculated threshold, the moment-order cubic boundary, the exact finite-time telegraph formula against an independently integrated pair of coupled equations, the sharp small-overdrive scaling, the finite-domain geometric threshold and the leading finite-size quantization error. The expected final line is `PASS 2979 deterministic assertions`.

The analytical proof in `RESULT.md` establishes the universal statement, including all positive real moments and all positive continuous squared wave numbers. Finite deterministic tests cannot prove universal assertions, publication priority, stochastic-model realism, or the correctness of an untested nonlinear extension.

The theorem assumes an initially stationary symmetric two-state Markov chain, a single globally modulated tension common to every Fourier mode, strictly positive mean tension, bending modulus and flip rate, and linearized surface mechanics. Almost-sure and ensemble-moment results refer to distinct notions of growth and must not be interchanged. Independent audit and independent validation have not been performed.
