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

Execute `python3 CHECKER.py` (Python 3.8+). It must print `BOUNDARY_CHECK_OK 71` and the three nonpositive signatures \((2,1)\), \((2,2)\), and \((4,1)\). The algorithm enumerates exactly all \(n\ge2,nk<17,n\ne3\) and \(n=3,3k<128\). All integer powers are compared exactly. The analytic infinite part rests on the published Rosser--Schoenfeld lower bound and two elementary monotonic logarithmic quotients; verify those steps from RESULT.md independently. This is a finite-boundary reproducibility check, not independent validation of the theorem or a proof by experimentation.
