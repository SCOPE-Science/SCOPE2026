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

Run `python3 verify.py` with Python 3. No third-party packages or internet access are required. This executed certificate independently checks the exact closed-form first moment for all integers from 2 through 40; verifies 14 additional direct group-permutation calculations for parameters 2 through 15; exhausts every subset at parameters 2, 3, and 4; and checks the exact integer bound at parameter 41.

The program prints `VERIFICATION_OK` and the boundary moment values. Its computations establish the finite base range only. The displayed universal theorem also uses the proof that Lucas numbers satisfy \(L_m\le7^{m/4}\) for \(m\ge3\), the complete group-specific cycle decomposition, and the strictly increasing normalized lower bound for every integer \(n\ge41\). These arguments are supplied in `RESULT.md`.

This record reports successful self-review of the supplied mathematical proof and certificate, not an independent audit or machine-certified formal theorem.
