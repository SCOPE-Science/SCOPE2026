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

# Verification and reproducibility

Run `python check.py` using Python 3 and SymPy. The checker evaluates normalized sphere monomial moments with exact rational arithmetic, reconstructs the real degree-one/degree-two moment identity for 125 trace-free symmetric matrices and vectors, and checks the two-term deficit. It also integrates normalized Legendre functions directly and verifies the optimizer fraction and sharp constant.

Recorded output from a completed run is in `check_output.txt`: `PASS: 1008 exact moment and optimization assertions`.

The universal inequality and equality cases follow analytically from the formula for normalized spherical even moments, the traceless eigenvalue bound, the two-square deficit, and the real/imaginary reduction. The finite suite checks formulas but cannot establish these all-parameter arguments on its own. No independent mathematical audit has occurred.
