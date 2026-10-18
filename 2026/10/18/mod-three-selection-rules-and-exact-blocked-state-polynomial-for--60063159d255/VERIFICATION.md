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

The accompanying standalone `verify.py` implements the original Hamiltonian directly, flips each individual spin to test strict blocking, and compares the resulting defect-energy coefficients with explicit integer matrix traces. It also checks the unrestricted energy polynomial and low-excitation coefficients. For sizes \(3\le N\le15\), **65,528** spin configurations were examined exhaustively. For \(16\le N\le24\), the script independently enumerates cyclically separated defect subsets and applies the periodic image-parity condition. A total of **201** polynomial evaluations passed, along with exact first-band multiplicity assertions.

Run with `python3 verify.py` in the directory containing this file and the script. No additional Python packages are required. The implementation uses only Python's standard library.

These finite-volume checks do not prove the result for arbitrary length; the analytic proof is in `RESULT.md`. No independent audit was performed, and no experimental or external mathematical certification is asserted.
