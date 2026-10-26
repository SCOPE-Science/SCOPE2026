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

Run `python verify_cutoff.py` after installing `requirements.txt` in a Python environment. The script evaluates concrete density matrices for one through four qubits, multiple shift probabilities and cycle counts; it independently composes the channel and compares to the finite binomial expansion. It also confirms that the homogeneous rotation commutes with shift/reinjection and that the shift is fully depolarizing after exactly the chain length. For two through ten qubits it checks the finite probability bounds against exact computational-basis distributions. At larger dimensions it compares the binomial tails with Gaussian values without allocating exponentially sized matrices.

The script completed successfully in the present evaluation, reporting **2732 numerical assertions**. Tolerances apply only to floating-point matrix calculations. The full diamond-norm inequalities are analytic, using the maximal channel distance and a physical measurement witness; the infinite-size cutoff follows from the standard binomial central limit theorem. Neither the experiments nor the numerical central-limit illustrations constitute independent proof of the analytic theorem. No independent audit has been performed.
