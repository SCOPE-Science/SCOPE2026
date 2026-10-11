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

# Verification and scope of checks

The analytic argument in `RESULT.md` proves the result for **all** integers \(n\ge2\), odd polynomial degrees \(m\ge n\), and all eligible initial points in the invariant wedge. It establishes wedge invariance, finite original-time maximal existence, two terms in velocity versus oriented position, and two terms in remaining physical time.

The reproducible code `verification/check_coefficients.py` uses the Python standard library `fractions.Fraction` to inspect representative degrees, including \(m=n\) and \(m>n\), and verifies exact identities for the coefficients \(A,Q,L\), integration, and inversion. Run `python verification/check_coefficients.py`. It prints `CHECK_OK` if its finite calculations pass. It does **not** certify the wedge geometry, asymptotics for all degrees, or literature originality; those require reading the proof and comparing published results.

The scientific overlap check compared the primary published family, established center classifications, general near-infinity and blow-up theories, and the exact time-dependent claim. Full text of Dumortier–Herssens (1999) was not obtained, and absolute priority remains unproved.
