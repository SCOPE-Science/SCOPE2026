---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the printed 4D system, independently expanded L[(u^2-e w^2)/2]=-a u^2+a uv+b e w^2 and Lw=-bw+uv using exact symbols. Stationarity eliminates E[uv]=bE[w] and gives E[(w+a/(2e))^2]=(a/(2e))^2+(a/(be))E[u^2]. When the defect E[u^2]=0, compact invariant support lies at u=0; L(w^2), L(uv), and L(vp) respectively force w=0, v=0, p=0 using b>0,a>0,m>0. Slab |w+a/(2e)|<=a/(2e) gives the strict support excursion for all non-origin measures. Fractions a=15,b=43,e=5 yield center 3/2, squared-radius 9/4, activity 3/43. Did not infer existence of non-equilibrium recurrent dynamics from simulation.

## originality

PASS

The primary Cui–Li 4D article and antecedent three-dimensional Qi energy work concern equilibria/bifurcations and a different Casimir-energy balance. The same-model published Resultary correction concerns local equilibrium coordinates and spectrum. None supplies the exact signed w-shell or compact-invariant-measure slab rigidity. Best-of-knowledge priority, with scope-limited bibliographic risk.

## value

PASS

The 4D hyperchaotic controller was introduced to study bounded recurrent behavior; an exact signed stationary shell and strict excluded recurrence slab provide natural nonlocal constraints on all compact recurrent states and a baseline-specific numeric test unavailable from local equilibria alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
