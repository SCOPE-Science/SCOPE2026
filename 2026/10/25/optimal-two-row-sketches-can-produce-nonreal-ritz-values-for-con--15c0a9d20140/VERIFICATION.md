---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For p in (0,1), h,t>0 and d>sqrt(h^2+t^2), orthogonal Q rotates e1,e3; H=[d,h,0;h,d,t;0,t,d] has eigenvalues d,d±w, A=QHQ^T is SPD. V=[Qe1,Qe2] is genuinely K2(A,Qe1) since h>0. Exhausting three two-coordinate rows gives uniquely optimal {1,2}: singular minima c, pc and 0; DEIM and Q-DEIM choose it. The sampled projection is M=[d,h-pt;h,d], with real/defective/conjugate spectral transition at h=pt. At d=3w full condition number equals 2. Completing square in k=h/t verifies exact maximum imaginary/w=sqrt((sqrt(1+p^2)-1)/2), attained k=p/(1+sqrt(1+p^2)); it scales as sqrt(delta)/2 for delta=p^2/(1+p^2). Independently constructed rational witness p=3/4,h=5/13,t=12/13,d=3: A spectrum {2,3,4}, M eigenvalues 3±2sqrt5 i/13; separate exact symbolic envelope gap identity checked.

## originality

PASS

Best-of-knowledge PASS limited to the simultaneous exact E-optimality, DEIM and Q-DEIM selection, genuine Krylov basis, condition-two SPD family, complete degeneracy frontier and attained envelope. Qualitative complex sketched Ritz values for Hermitian/SPD inputs are expressly previously known and not part of originality; similarity-restored methods are different algorithms.

## value

PASS

A sharply quantified counterexample to a natural numerical assumption (excellent basis embedding assures real SPD Ritz output), with fully optimal sketch and arbitrarily small squared embedding error and an attained sharp pollution envelope. This is more informative than renaming the known qualitative phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
