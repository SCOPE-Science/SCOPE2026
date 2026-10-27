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

Execute `python3 verify.py` with an unmodified Python 3 standard-library installation. The checker reconstructs the fourteen prime-power moduli \(p^{\nu_p(45!)}\), evaluates \(P_{45}(t_p)\) modulo each, and verifies the supplied \(R\) satisfies their Chinese-remainder congruences. It independently evaluates \(h_{45}^{(r)}\) as an exact reduced rational at \(r=R\), \(R+45!\), and \(R+2\cdot45!\), checking denominator one, and recomputes the derivative identity in exact integers.

Expected successful output:

`VERIFY_OK: 14 exact prime-power derivative zeros; CRT modulus=45!; three independent direct hyperharmonic integers; every nonsquarefree n<45 is even or an odd prime power.`

The explicit local checks are a finite exact certificate for the fixed index \(45\). The assertion for infinitely many orders is a polynomial congruence theorem, not an extrapolation from the three sampled orders. The lower-index exclusion is a mathematical consequence of the published nonintegrality theorem for even and prime-power indices. No exhaustive search for all admissible orders, no full access to the 2025 density paper, and no independent mathematical audit is asserted.
