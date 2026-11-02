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

# Reproducibility and verification

Execute `python verify.py` in a Python environment with NumPy as specified in `requirements.txt`. A successful replay of the program supplied with this package passed 326 finite assertions. The checker constructs the complete Ising phase sector sets for one through four environmental qubits and tests all pairwise channel multipliers. It also reconstructs branch Choi matrices, full three- and seven-logical-qubit process density matrices, and independent Gram spectra. The mixed-weight tests verify the sharp frame-potential equality at the Fourier clock and the lower bound for random clocks, including strictly unequal weights.

The code's finite precision does not establish uniqueness for all possible phases, infinitely many memory dimensions, or the asymptotic binomial entropy theorem. Those statements are proved analytically in `RESULT.md`, respectively by square-frame orthogonality, finite geometric sums, Dicke-basis expansion, and Stirling's formula with Chernoff tails. The large-size coherence asymptotic is an analytic assertion, not a numerical fit. The relevant physics source was inspected directly in HTML form; the related published phase-ensemble record was accessible only by its indexed title/summary, and independent priority assessment has not been performed.
