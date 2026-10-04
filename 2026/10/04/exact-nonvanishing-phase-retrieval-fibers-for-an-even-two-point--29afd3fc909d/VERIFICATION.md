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

The proof in `RESULT.md` is the primary verification. It is symbolic and valid for every admissible \(N\) and \(a\); the finite computation below is only an independent consistency check of the algebraic mechanism.

`verify_two_point_phase_fibers.py` uses exact Python `Fraction` arithmetic and Gaussian-rational pairs. It does not evaluate roots of unity numerically. Instead, it represents each squared two-term STFT slice by its exact character coefficients. For every \(4\le N\le120\) and every nonzero step whose order is even and at least \(4\), it checks that the three characters \(0\), \(a\), and \(-a\) are distinct; verifies exact coefficient preservation under every constructed two-level parity swap; derives the admissible alternating modulus ratio from the recovered sum equations; and verifies that perturbing one same-parity magnitude destroys the nontrivial solution.

A package replay prints:

```text
N_MAX=120 checks=400616 swap_cycles=5856 perturbed_cycles=5856
VERIFY_OK
```

The computation does not establish the infinite theorem by enumeration. The infinite necessity and sufficiency are the quotient recurrence and factored edge equation written explicitly in `RESULT.md`. The order-two step case and signals with zeros are intentionally outside the verified claim.
