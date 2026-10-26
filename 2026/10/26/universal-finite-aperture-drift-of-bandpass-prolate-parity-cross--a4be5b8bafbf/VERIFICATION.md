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

The complete analytic proof and ranges are in `RESULT.md`. Execute `python verify.py` in an environment with dependencies listed in `requirements.txt`; `CHECKER_OUTPUT.txt` contains the actual output. At the parameter choices \(a=1\), \(n=1,2,3\) and \(arepsilon=0.2,0.1,0.05,0.025\), the program computes even/odd sector spectra using independent 72- and 48-point Gauss–Legendre Nyström discretizations. It locates the crossings, tests double-leading spectral isolation, exact operator trace, gap sign change, numerical transversality and the \(O(arepsilon^4)\) asymptotic remainder. Twelve cases passed, with the output printed in full.

Numerical quadrature does not prove an infinite family of crossings or a rigorous analytic remainder. The theorem's universal claims are instead derived from rank-one analytic perturbation theory, uniform local spectral separation and the analytic implicit function theorem. The paper-level novelty comparison is provisional because one highly relevant 1963 primary article could not be examined in full. No independent audit or independent mathematical validation was performed.
