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

# Verification record

The stated multi-species alternating reduction was reconstructed from the source equation and independently checked by rational-arithmetic tests in `verification.py`. The Jacobi profile was tested through its exact defining differential polynomial; the displayed positive linearized eigenvalue was checked through an independent polynomial factorization. The source's sinusoidal initialization and normalization were compared directly with its posted full text. Numerical Fourier-periodic integrations were supplementary to, not substitutes for, the comparison-principle, energy, elliptic-period and eigenfunction proofs in `RESULT.md`.

## Run instructions

Use Python 3.10 or newer. From the extracted directory run `python verification.py`. No external libraries, papers, or network access are required to execute the embedded checks. The program reports individual assertion totals or fails immediately.

## Limits

The checker cannot exhaust infinite spatial dimensions, all parameters, or all possible published literature. The complete mathematical proof and its assumptions remain in `RESULT.md`. The public preprint was read in HTML form, including the relevant nonlinear PDE, frozen-wave conjecture and appendix. The later journal article's full text has not been compared line by line, which is a residual priority risk. This is same-model verification only; no independent audit or independent validation has occurred.
