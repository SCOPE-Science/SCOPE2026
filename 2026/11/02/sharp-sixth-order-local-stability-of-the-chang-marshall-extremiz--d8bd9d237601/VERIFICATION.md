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

Run `python3 verify.py` from the folder containing the extracted files. The program uses only Python's standard library and computes the constant Fourier coefficient in the exponential expansion through order six with exact rational arithmetic. It checks eight integer square orders and three symbolic-specialization tests at each order (twenty-four checks overall).

Analytical verification is supplied in `RESULT.md`: the uniform invertibility of the stable Hilbert Hessian, local real analyticity from exponential moment bounds, rotationally constrained implicit-function branch, exact fourth/sixth order normal form, and coercive comparison with Hilbert distance. The checker does not prove the Hilbert implicit-function theorem, exhaust all integer orders, establish historical priority, or provide an independent audit.
