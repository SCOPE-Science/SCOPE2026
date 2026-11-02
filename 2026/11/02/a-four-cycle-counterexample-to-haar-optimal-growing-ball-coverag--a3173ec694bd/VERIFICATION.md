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

# Reproducible verification

Run `python3 check_counterexample.py` with Python 3 and its standard library. The checker enumerates all 15 nonempty site subsets and builds each Poisson void integral as a rational linear combination of \(e^{-z}\), with \(z\in\{0,1/4,1/2,3/4,1\}\). It verifies the exact Haar and antipodal coefficient dictionaries, the resulting difference, and a strict rational interval from degree-12/13 alternating Taylor bounds. It also evaluates the exact formulas to aid independent inspection. No random seed or network access is needed.

An independent pathwise proof for the antipodal measure comes from first arrivals at supported sites, giving \(C=M+\max(1,\min(G,2))\), \(M\sim\operatorname{Exp}(1)\), \(G\sim\operatorname{Exp}(1/2)\), independent. This route does not use inclusion-exclusion and provides a second verification of that formula.

The exact certificate establishes a finite four-site counterexample only. The calculation does not establish a global seed-law minimizer, a connected-group counterexample, a general theorem, or independent historical priority.
