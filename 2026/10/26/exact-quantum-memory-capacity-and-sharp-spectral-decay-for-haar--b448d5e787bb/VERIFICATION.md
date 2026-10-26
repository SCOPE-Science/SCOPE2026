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

Run `python3 verify.py` using Python 3 and only its standard library. Expected final line: `CHECKS_PASSED_FINAL 7417`.

The program compares independent convolution and Walsh-Fourier constructions of random-walk distributions for hypercubes, checks normalization and parity support, checks the entropy-capacity expression and monotonicity, and tests asymptotic coefficients at selected finite depths. It also constructs full complex matrices for two small coin-position Hilbert spaces and verifies that repeated averaged-coin evolution equals the final-coin conditional-shift expression. Finally, it independently checks odd and even cyclic Cayley examples and the four-cycle's finite-time saturation. The checks use floating-point tolerance and do not certify general infinite-depth or operational channel-capacity theorems.

The proof is in `RESULT.md`, including all hypotheses, the dephasing degrading map, the coherent-information maximization, the parity-coset Parseval identity and the entropy expansion. The cited general degradable-channel coding theorem is a mathematical premise documented in [2]; no independent review has been performed.
