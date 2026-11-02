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
# Verification instructions

Run `python3 verify.py` in the directory containing this file. The program uses only the Python standard library and prints `VERIFY_OK` after completing all checks. It does not rely on external data files.

Its exact checks reconstruct the 4-by-4 Boolean edge matrices from the stated local rule, the reachable 75-element relation monoid, and 61 accepting relation states. It then proves a vector identity with **75 zero components**, namely \(T^2p(T)v=0\), using arbitrary-precision integers. This is a finite mathematical certificate for an all-length recurrence; the proof of its implication is in `RESULT.md`. The program also checks the first coefficients, rational denominator, numerator and independent Newton-power-sum identity.

An independent direct implementation applies Rule 110 to every binary ring input at each length from 1 to 16 and counts distinct output words, including rings with coinciding neighbor indices. These exhaustive finite checks do not alone establish the all-length statement; the finite transition-algebra identity does. The dominant-root argument is given analytically in `RESULT.md`.

The package does not certify multi-step reachability, fixed-density counts or priority over every historical publication. The scientific review is not an independent audit.
