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

# Reproducibility and scientific limits

Execute `python verify_broom.py` under Python 3 with installed SymPy and NumPy. The source verifies the quotient characteristic polynomial and its sign evaluations by symbolic cancellation, exact Rayleigh energy identities, the positivity inequality for all integers at least three, 98 full transition matrices of increasing size, and a strict five-vertex boundary witness using exact positive-definite principal minors. The algebraic proof in `RESULT.md` supplies universal quantifiers; the finite matrix tests are supplemental independent reconstructions of those identities. The SLEM result concerns real symmetric nonnegative stochastic kernels with holding probabilities; no claims are made for nonuniform stationary distributions, other bistar branch counts or continuous-time chains.

The recorded scientific assessment is a self-review only. Independent audit has not been performed.
