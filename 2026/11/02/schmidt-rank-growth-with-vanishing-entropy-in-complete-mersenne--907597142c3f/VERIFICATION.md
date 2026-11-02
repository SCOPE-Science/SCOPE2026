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

# Reproducibility

Run `python -m pip install -r requirements.txt` in a Python 3 environment, then `python verify_mersenne.py`. The checker constructs the residue probability vectors by an independent cyclic Bernoulli convolution, forms the normalized cross-cut amplitude matrix, compares small cases with the direct computational-basis state matrix, and checks the limiting spectrum and purity for three values of the modulus. It prints a final `PASS` line only after all assertions hold.

The analytic rank proof is the factorization of the cyclic sign matrix and the root-of-unity convergence in `RESULT.md`. Numerical tests do not prove the theorem for unbounded parameters; their purpose is to independently check normalization, small examples, and the finite-to-limit calculation. The model, coupling convention, and sequential-limit restriction are explicit in the result. No independent audit has been performed.
