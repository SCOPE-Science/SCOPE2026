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

# Reproducibility of the density-optimizer classification

Install `requirements.txt` in Python 3 and execute `python verify.py`. Actual execution passed the following checks: equality between direct differentiation and the quartic sign polynomial; exact whole-interval and three subinterval transforms; resultant factorization; exact turning-point and edge substitutions; seven 65-digit bisection and prefactor-normalization cases for squared activities 0.01, 1, 1.4862468561950113, 4, 9, 15, and 15.99.

The proof of all-parameter positivity, negativity, and uniqueness is the sign analysis in `RESULT.md` together with Descartes' rule and the implicit-function theorem. Checking finite parameters does not certify a continuum. The starting macroscopic current-variance formula and spinodal come from primary sources; verification here does not rederive their microscopic hydrodynamic limit. No third-party paper, unavailable dependency, or external proof system is embedded.

Scientific limitations: the optimizing density is for the leading long-time coefficient at fixed subcritical activity, and the calculation does not establish uniform finite-system convergence as activity approaches the spinodal. Independent audit has not been performed.
