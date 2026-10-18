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

# Verification of the folded-Poisson range dispersion transition

The standalone program `check_dispersion.py` uses only Python's standard library and constructs lower and upper exact rational bounds for \(e^t\), \(I_0(t)\), and \(I_1(t)\). It verifies strict opposite signs of \(H(t)-1\) at \(17389/5000\) and \(1739/500\). It also checks the modified-Bessel mean against independently summed Poisson probabilities at \(\lambda=1/2,1,2,3\) to high arithmetic precision.

The global uniqueness statement rests on the written proof's strict Turán-based estimate and negative derivative at every crossing, combined with endpoint asymptotics. A finite checker cannot independently prove these analytic steps. Review is not independent: no third-party validation or separate certification has been performed.
