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

# Reproducible checks

Run `python3 verify.py` with Python 3; no third-party packages or downloads are required. The script builds the exact count and founder generators from the stated event rules, normalizes their solutions, applies finite rational Taylor recursions through order five, and checks the coefficients \((0,0,0,0,0,89/56010528)\). It also independently reconstructs the full nonperturbative source instance with killing vector \((1,2,4)\), checking \(421413160/139117744582101\). The actual program output is in `CHECKER_OUTPUT.txt`.

The verified operations are finite exact-rational eliminations, not stochastic simulations. The extension to all sufficiently small real perturbations uses the analytical invertibility of the normalized finite-state systems and reflection symmetry. Positivity is only asserted locally; a quantitative choice of the unspecified positive neighbourhood radius is not established. Independent mathematical audit remains unperformed.
