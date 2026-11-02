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

# Reproduction

Run `python verify.py` using Python 3.10 or newer; only Python's standard library is needed. The program checks exact rational Green-kernel moments and normalizations for seven integer mobility exponents, six interior reset positions, and five noninteger exponents through independent numerical quadrature. The successful run reports 158 checks.

The numerical quadrature is not an infinite proof and is deliberately separated from the Dirichlet and regenerative arguments in RESULT.md. The nonsticky time change, moment finiteness, and Brownian invariance are derived analytically. No independent audit has been performed.
