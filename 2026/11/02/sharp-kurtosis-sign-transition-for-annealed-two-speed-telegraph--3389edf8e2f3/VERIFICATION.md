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

# Reproduction and boundaries

Execute `python checker.py` with Python 3 and installed `numpy`, `scipy`, and `sympy`. The executable derives a characteristic polynomial of the finite tilted generator symbolically; it then solves separate forward moment equations through order four and compares the asymptotic cumulant slopes against their closed forms for six independent parameter sets. It performs numerical comparisons at three large times, using the difference between two times to eliminate bounded boundary terms.

The mathematical proof itself uses finite-dimensional analytic eigenvalue perturbation at a simple eigenvalue, an explicitly derived scalar eigenvalue equation, a fourth-order series coefficient, polynomial factorization under \(u=q+q^{-1}\), and a derivative sign analysis. The code checks finite cases only and cannot certify global quantifiers or historical priority. The result concerns fixed parameters as observation time tends to infinity. Independent mathematical validation has not been performed.
