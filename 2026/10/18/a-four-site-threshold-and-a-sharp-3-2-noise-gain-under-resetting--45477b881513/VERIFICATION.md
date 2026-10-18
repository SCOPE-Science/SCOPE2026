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

# Reproduction and limits

Run `python verify.py` with Python 3.10 or newer; it needs no external dependencies. The script independently forms the full generator of the reset cycle, computes exact stationary weights and the occupation Poisson corrector, forms an independent exact resolvent of the no-reset cycle, and verifies the resulting asymptotic variance identity. It also numerically compares independent Fourier and hyperbolic representations and checks the trigonometric finite sums and a large-cycle witness. Expected output starts with `PASS: 30 independent exact finite-chain generator/resolvent comparisons`.

The finite enumeration covers only cycles of sizes 3 through 12 and the three listed rational reset rates. The arbitrary-size claim, the sharp initial-response transition, and the global upper envelope are established by explicit analytical arguments in `RESULT.md`. Finite checks are not an exhaustive validation of unbounded size. Independent scientific audit has not been performed.
