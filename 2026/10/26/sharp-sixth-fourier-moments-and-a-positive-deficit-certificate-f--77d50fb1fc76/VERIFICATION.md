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

# Reproduction and scientific scope

The theorem is proved symbolically in `RESULT.md`. Its core identity can be verified without floating-point arithmetic using `python3 check_sixth.py` (Python standard library only). `check_output.txt` gives the original observed output: 2923 exact integer or rational checks passed. The checker directly expands cubic Laurent powers for random Gaussian-integer inputs, independently recomputes the algebraic sixth-moment formula and the nonnegative deficit, and verifies boundary examples in cyclic groups of orders six and seven. Random test arrays are seeded deterministically.

An exhaustive check of arbitrary complex coefficients or all dimensions cannot be obtained from finite computation; instead, the proof uses Fourier coefficient classification and an exact nonnegative identity valid for arbitrary coefficients and dimensions. No separate independent scientific audit has been carried out.
