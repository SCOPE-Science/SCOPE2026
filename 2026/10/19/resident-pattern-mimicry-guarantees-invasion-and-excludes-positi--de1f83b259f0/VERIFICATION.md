---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For each scalar equation the ordered barriers epsilon R and M R yield an equilibrium by cooperative comparison; uniqueness follows by comparing the maximum scaled ratio at a contact index (swap the equilibria if necessary). At a positive scalar equilibrium Z, its Metzler Jacobian maps Z to -Z squared componentwise, so that block is Hurwitz. At (Q,0), put a=d(Q1/P1-Q2/P2); the stationarity residuals are (a/Q1,-a/Q2), and the invader block has determinant -a^2/(Q1 Q2) for every e>0. At (0,V), orient the patches to make a>0 and put ti=Vi/Qi, D=t1-t2. If D<=0, the equilibrium signs would force t1>=m1/Q1>1>m2/Q2>=t2, a contradiction. Equality of the two formulas for eD gives aD=sum Qi^2 ti(ti-1), hence t1>1. The resident transverse determinant factors as (eD/(Q1 Q2 t1 t2))*(Q1^2 t1(t1-1)+d Q2 D/P2)>0; its lower-right diagonal is negative and the positive off-diagonal product makes the upper-left entry negative too. Both blocks are Hurwitz. At a putative coexistence equilibrium, nonzero residual growth g forces u and v to be collinear by conservation and the two-dimensional orthogonal complement. Then their sum would be Q by scalar uniqueness, but the invader target Q forces g=0. For g=0, separate flux balance instead gives m=alpha P+beta Q with alpha=-d(Q2/Q1+Q1/Q2)/(P1 P2)<0. A species cannot vanish in exactly one patch at equilibrium. Checked the exact example by rational substitution: a=1/4, D=9/52, eD=135/1352 equals V1(m1-V1) and -V2(m2-V2); the transverse determinants are -1/32 and 61/5408 and the latter trace is -59/104. Inspected RESULT.md lines 30–110 and frozen verify.py/VERIFICATION.md. The source checks one witness, not the universal theorem, and was not executed. Local stability and equilibrium exclusion do not prove global attraction.

## originality

PASS

Best-of-knowledge PASS for the joint two-patch classification with shared growth and invader target equal to the nonbalanced resident equilibrium, not for invasion eigenvalue methods or generic two-patch phase diagrams. The identified continuum mimicry theorem assumes a strict advantage; the inspected common-kernel patch theorem cannot cover the distinct kernels. Three named nearby publications could not be compared at full theorem level, and remain access risks, not negative evidence.

## value

PASS

The exact two-patch model tests the equal-resource resident-profile mechanism without assuming a favorable intrinsic growth difference between competitors. The sign remains strict for every positive mimic movement intensity, and the converse local resistance and absence of coexistence equilibria add meaningful information beyond linear invasion. The two-dimensional conservation argument also identifies why the result does not automatically extend to more patches. It is a useful finite-dimensional classification rather than a claim of global exclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
