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

# Mathematical verification

The sharp norm, equality conditions, and deficit identity are established in `RESULT.md` by exact pair-sum geometry and completed squares. No continuous complex parameter has been exhaustively enumerated; that is unnecessary for the proof.

The standalone checker `artifacts/verify.py` runs under Python 3 standard library, using exact integer arithmetic for pair-sum and Fourier convolution identities and floating-point evaluation only when directly checking complex characters and square roots. Run:

`python artifacts/verify.py`

Observed output:

`VERIFY_OK finite_fields=5 quadratic_extension=F25 exact_integer_convolution_cases=40 direct_fourier_cases=20 deficit_checks=PASS`

The checker inspects every ordered pair in each tested field, verifies the unique nonzero-sum fibers and the exceptional antipodal fiber, compares exact Gaussian-integer convolution energies with a separate closed formula in forty cases, tests random nonnegative deficits, and checks twenty direct Fourier sums including constructed extremizers. Its quadratic extension implementation represents \(\mathbb F_{25}=\mathbb F_5[\omega]/(\omega^2-2)\), and uses the trace to define its additive character. Its finite scope is \(q\in\{5,7,11,13,25\}\).

The analytic argument covers all finite fields of characteristic greater than \(3\), not only those tested. No independent audit or external correctness certificate has been performed. The source comparison is limited to the specifically identified published literature and search results and does not certify global priority.
