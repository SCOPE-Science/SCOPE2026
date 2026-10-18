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

At every finite state of the printed DAE the algebraic equation is e(t)(p x(t)-c)=m>0. From e(0)>0 it follows p x(0)-c>0; continuity of finite x and e and nonzero product prevent either factor crossing zero. Therefore throughout any finite continuous classical solution x(t)>c/p and e(t)>0. If it reached x=c/p, the exact algebraic equation would give 0=m, contradiction; the conclusion is independent of the delay dynamics. With source p=2500,c=.02,m=604.33, independently reduced exact rationals give c/p=1/125000, required effort at x=.2 =60433/49998 and at x=.8 =223/738; if caption initial triple is model order (x,y,e), the printed e=1.2 gives algebraic residuals -2177/500 and 897823/500 respectively. The primary published Figure 6 caption explicitly describes prey dying out from (.2,.5,1.2) and wildly fluctuating effort; those reported curves cannot be finite classical trajectories of this DAE if crossing the barrier or taking negative finite effort. An approximation may jump over the pole, and the initial-order interpretation is conditional; neither caveat alters the hard branch result.

## originality

PASS

Singular barrier/positive-feasibility analysis of DAEs and bioeconomic predator models is a known general methodology. No generic non-crossing theorem is claimed novel. The specific source paper's Figure 6 presents a finite trajectory interpreted as prey extinction under precisely the printed m>0 effort relation, in conflict with the noncrossing proof and numerical consistency checks. Comparison with other published singular predator–prey models shows different closures, not an earlier diagnosis of this particular Figure 6. The mathematical contribution is a motivated falsification of an interpretation of an original simulation, not the elementary algebraic sign observation by itself; earlier figure critiques may be unindexed.

## value

PASS

A sharp viability restriction that invalidates a published model's claimed extinction simulation has scientific value: it distinguishes genuine biological extinction from numerical singularity crossing and exposes inconsistent initial data. The pole at c/p sets an explicit hard domain for admissible classical numerical integration and invalidates negative harvest effort from a positive branch; this is a substantive model-interpretation boundary rather than an arbitrary type/units check. No broad theory of DAE singularity is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
