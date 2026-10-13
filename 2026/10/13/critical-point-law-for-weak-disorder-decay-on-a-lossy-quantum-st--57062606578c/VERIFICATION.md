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

# Reproduction and verification

The proof is given in `RESULT.md` and reduces the characteristic polynomial to a scalar critical-point equation. Run `python verify.py` after installing the dependencies from `requirements.txt`. The verifier directly constructs the complex star Hamiltonian, computes its eigenspectrum and full matrix exponentials, and independently compares results against the rates extracted from real zeros of the derivative of the detuning polynomial.

A local execution returned `VERIFY_OK models=8 survival_comparisons=64 rate_checks=30`. Tests covered four distinct detuning configurations (three, four, five and seven leaves), two small positive disorder strengths, randomly generated complex normalized pure initial states, and scaled times \(\tau=0.4\) and \(\tau=1\). The comparisons used an absolute tolerance of \(0.01\) for survival probabilities, and checked orthogonality of the predicted critical-point modes as well as nonpositive imaginary eigenspectra. The count of rate checks is the sum of dimensions of the dark groups across all eight models. This is finite numerical corroboration; the infinite small-disorder limit is established by the analytical eigenvalue and spectral-projector arguments in `RESULT.md`.

Limitations: no certified interval arithmetic was used; the numerical tests do not certify the general statement or publication priority. The exact limit holds for each fixed positive rescaled time and fixed distinct detunings. No independent audit has been performed.
