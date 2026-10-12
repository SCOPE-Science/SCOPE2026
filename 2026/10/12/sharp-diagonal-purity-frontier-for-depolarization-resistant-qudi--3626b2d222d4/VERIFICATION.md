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

# Verification of the sharp diagonal-purity NPT threshold

The package includes `verify.py`, requiring only Python 3 standard library. Execute `python3 verify.py`. The recorded check `VERIFY_OK 8016` comprises explicit optimizer construction for dimensions 3 through 18 at 101 collision-purity grid points each (1,616 checks), plus randomized inequality checks for 400 points per dimension (6,400 checks). The analytic proof separately establishes the continuum of purities and all dimensions; grid checks are not an infinite proof. All mathematical facts needed for reproduction appear directly in RESULT.md and the standalone script; no external data or paper binaries are required.

The input's *diagonal* purity is not the full pure-state density matrix purity. The threshold is for negative partial transpose; the script does not attempt to test separability beyond this condition. Independently performed external review is not represented here.
