---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The rho_2 maximum is attained on a nonempty compact domain. The norm bound 3 and equality of BOTH distances imply ||x||=1, ||y_i||=2 and dual norm-one functionals simultaneously supporting x and z_i=-y_i/2; separation gives ||z_1-z_2||>=1. Conversely two star points with norm separation >=1 generate y_i=-2z_i and both distances exactly 3. Compactness of the supporting-functional incidence relation ensures the maximum diameter is attained, including nonsmooth vertices. In K_a the only non-singleton exposed faces are vertical segments of norm diameter 2sqrt(1-a^2); equality is a<=sqrt3/2. In P_N, vertex stars are pairs of incident edges; their endpoints have norm distance D_N=2sin(2pi/N) if 4|N and D_N=4sin(pi/N) otherwise. Edge distances are <=2tan(pi/N)<=D_N; checking trigonometric monotonicity gives N=4,6,8,10,12 exactly. The modulus statement follows from the single-face diameter threshold 1/2 at a=sqrt15/4. No exact subcritical rho_2 is proved.

## originality

PASS

The originating full-text article defines the exact constant and the universal upper bound, with a sufficient bound via the modulus delta_K(1/2), but does not give a necessary-and-sufficient geometry-of-equality test or either sharp phase cutoff. The face-star criterion detects strict subcriticality in a specific interval where the published modulus bound cannot. This is a best-of-knowledge originality finding, not a claim to have ruled out all older norm equality criteria.

## value

PASS

The two-ball factor is motivated by a canonical geometric covering problem. A dimension-uniform iff saturation characterization and two exact sharp families determine when the universal bound is qualitatively improvable. The clipped-disk interval where the older modulus bound is blind makes the exact new boundary independently useful; it is not a mere normalization or finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
