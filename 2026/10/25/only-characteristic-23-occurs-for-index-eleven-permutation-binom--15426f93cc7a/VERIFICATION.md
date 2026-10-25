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

# Exact computational certificate

Run `python3 verify.py` with standard Python 3. No third-party packages or input data are required.

The script reconstructs the complete integer Wendt determinant at index \(11\) using a \(22\)-row Sylvester matrix and fraction-free Bareiss elimination. It verifies the factorization
\[
101832157445630503=23^5\cdot67^2\cdot89\cdot199^2.
\]
It checks the four prime factors are prime by exact trial division, enumerates all allowed \(11\)-th roots with the required product identity, all first-sum roots modulo the three excluded primes, and both permitted second-sum arguments. For the \(24\) required nonzero second-sum values, the code evaluates the polynomial two different ways: by the formal generating-coefficient identity and directly from its polynomial-derivative recurrence. Finally it verifies that the explicit witness polynomial permutes all \(23\) elements in the prime field.

Expected terminal conclusions:

`CERTIFICATE_OK 24 nonzero second-sum residues`

`WITNESS_OK x^12+2x permutes F_23`

The enumerations are exhaustive **only because** the proof reduces an arbitrary extension to these three finite prime fields and two inverse-power-sum identities. No exhaustive examination of all polynomials or all extension degrees is asserted or required. The independent-audit channel has not been performed.
