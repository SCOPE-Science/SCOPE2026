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
The symbolic proof reduces every source set on \(K_{m,n}\) to its part-count profile \((a,b)\) by automorphism symmetry, solves the exact two-variable equilibrium, and derives the ceiling thresholds by cross-multiplying positive denominators.

`verify_complete_bipartite.py` was executed from the packaged path using Python's exact `Fraction` arithmetic. It checked \(1280\) profile-level parameter cases with \(1\le m,n\le8\) and then independently enumerated every source subset in \(28\) small graph/parameter cases, solving the full equilibrium linear system exactly rather than invoking the two-variable formulas. It also verified the unique optimum profile \((3,3)\) for \(K_{10,10}\) at \((\lambda,\tau)=(3/5,3/10)\).

Stored replay output:
`ALL CHECKS PASSED; profile_cases=1280; subset_cases=28; split_example=K10,10:(3,3)`

Finite checks do not establish the infinite theorem by themselves; they test the algebra and boundary cases of the symbolic proof. No external certification has been performed.
