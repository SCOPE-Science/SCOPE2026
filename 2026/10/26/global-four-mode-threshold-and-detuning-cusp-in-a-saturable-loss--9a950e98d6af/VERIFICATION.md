---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

In the fixed-norm lossy dimer with 0<Gamma<J and equal g/(1+|psi_j|²) nonlinearities, writing imbalance s=|psi1|²-|psi2|² and relative phase gives sin(phi)=Gamma sqrt(1-s²)/J, so precisely two phase branches exist. Their exact detuning functions are delta_±(s)=2g s/(9-s²)±F(s), F(s)=s sqrt[J²/(1-s²)-Gamma²]. The plus branch is a bijective strictly increasing map R to R. The negative branch derivative =2(9+s²)/(9-s²)² [g-R(s²)], and exact log derivative inequalities make R strictly increasing from g_c=(9/2)sqrt(J²-Gamma²) to infinity. Thus for g<=gc there is one negative branch crossing everywhere (total 2); for g>gc one pair of folds and negative branch has 3,2,1 intersections by detuning, giving total 4,3,2. Cubic Taylor of negative branch at s=0 proves a nondegenerate cusp width proportional to (g-gc)^(3/2), with coefficient [8/(27 sqrt3)]sqrt(sqrt(J²-Gamma²)/(7J²+2Gamma²)); as g->infinity s*->1 and delta*/g->1/4. No claims about dynamics or linear exceptional points.

## originality

PASS

Gu, Qu and Zhang (2024) introduced the exact Hamiltonian and its eighth-degree population polynomial and found multiple nonlinear eigenvalues numerically around exceptional-point geometries. The new global non-EP threshold for all real detunings and exact fold cusp coefficient is not given by those numerical root counts. Similar PT-symmetric saturable dimers and general nonlinear catastrophe arguments do not automatically imply the exact J>Gamma global classification. A potentially relevant 2026 balanced-gain/loss paper was accessible only at abstract level, so its detailed implications remain a priority risk.

## value

PASS

A parameter-sharp distinction between nonlinear four-mode folds and linear exceptional points is structurally informative. The exact non-EP threshold, all-detuning 2/3/4 mode partition, cusp coefficient, and large-g fold slope give natural, reproducible bifurcation invariants for this physically motivated dimer, not a routine application of an unspecified catastrophe normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
