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

Re-multiplied L=[[aI,-B],[-B^T,bI]] to obtain cross-class T_UV=h F(h)B+(h³/6)(1-(a+b)h/2)BB^T B and same-part blocks with strictly positive quadratic coefficient discriminant −16(5a²+2ab+2b²) plus nonnegative higher walks. For h<=2/(a+b), both cross-block coefficient terms are nonnegative and all diagonals positive because 24R4(-x)=(x²-2x+2)²+4((x-2)²+1)>0. In any incomplete connected bipartite graph some cross-part nonedge has distance exactly 3, so its B entry is 0 while (BB^TB)>0, forcing a strictly negative entry for every h>2/(a+b). For complete bicliques BB^TB=abB, giving cross entries h Q((a+b)h)/24 with Q strictly decreasing and unique root rho. λmax(L)=a+b (opposite-sign vector) and R4(-x)<=1 exactly up to x=rho. Independent sympy exact C6 nonedge T[0,3]=−h³(2h−1)/3 and K_2,3 edge factor hQ(5h)/24 agree. This covers every graph through a structural proof, not enumeration.

## originality

PASS

Best-of-knowledge graph-specific exact universal classification, beyond general RK absolute-monotonicity theory or earlier narrow bipartite graph subfamilies.

## value

PASS

Natural sharp positivity timestep criterion for every connected biregular bipartite network. It unifies prior restricted graph calculations, distinguishes graph completeness as sole structural exception, and proves the surprising invariant ratio rho/2 for all incomplete cases with a universal distance-three witness. This is not a routine Taylor expansion because a necessity/sufficiency dichotomy and global non-return of positivity are proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
