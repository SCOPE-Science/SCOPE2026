---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

At the Kirchhoff central vertex, the edgewise solution of Du''=su with absorbing leaves gives F(s)=[csch(z)+q csch(qz)]/[coth(z)+q coth(qz)], z=ell sqrt(s/D). The series at zero yields T0=ell^2(1+q^2)/(4D) and T'0=ell^4 q^2/(24D^2)>0. The renewal identity (1-F)/(rF) is standard. At z=log4, the exact q=4 ratio before dividing by (log4)^2 is 299421/37000; the strict rational logarithm bound proves benefit, while 19q^2-75q-26>0 covers every q>=5. As q grows, csch(qz) decays exponentially and the gain ratio is asymptotic to 15/[2(log4)^2 q]. The large-rate asymptotic shows eventual divergence, giving a positive global minimizer, not uniqueness. The independent rational q4 calculation and q=5,6,10,50,100 samples agree; samples are not the infinite proof.

## originality

PASS

PASS best-of-knowledge for the specific complete metric-star family with a strictly adverse weak-reset slope but a finite-rate all-q benefit and asymptotic unbounded advantage. Renewal Laplace formulas, resetting transitions and graph Brownian constructions are established prior machinery, not novel.

## value

PASS

The theorem gives an explicit infinite topological family in which the local coefficient-of-variation restart test cannot decide global utility, with exact quantitative design at a fixed rate; this is a motivated phenomenon, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
