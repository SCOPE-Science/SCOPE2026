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

# Reproducibility
Run `python3 CHECKER.py` from the directory containing the delivered files. This program uses only the Python 3 standard library and performs 198 direct and Fourier-sum checks, including exact rational arithmetic in a four-point critical configuration and both modulation signs for several harmonic orders. The expected final line begins `PASS:`.

# Verification limits
The program checks finite cases and floating-point approximations, not the universal statement. The universal statement follows from the Poisson expansion, the direct-sum defect-bond operator norm argument, and uniqueness of finite measures from all Fourier coefficients, as fully written in RESULT.md. The exact four-site Gram example is an additional rational check. Independent audit has not been performed.
