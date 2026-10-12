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
The proof is symbolic and infinite; finite computation is used only as a cross-check.

`verify_fan_zero_forcing.py` constructs \(F_m=K_1\vee P_m\), simulates ordinary zero forcing from every subset for \(3\le m\le10\), compares the outcome with the two-case structural criterion, evaluates the claimed polynomial using the path nonforcing coefficients and the four-state transfer recurrence, and checks the minimum value and the four minimum sets.

Packaged replay output:

`VERIFY_OK m_range=3..10 subset_checks=4080 criterion_checks=4080 coefficient_checks=68 minimum_checks=16 max_order=11`

The computation checks only the displayed finite range. It does not establish the theorem for arbitrarily large \(m\); that is supplied by the proof in `RESULT.md`.
