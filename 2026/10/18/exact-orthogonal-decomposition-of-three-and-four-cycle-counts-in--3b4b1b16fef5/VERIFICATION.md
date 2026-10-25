---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

On each 4-vertex tournament the complete local (number of cyclic triples A, number of 4-cycles B) table has frequencies (0,0):24,(1,0):16,(2,1):24 of 64 orientations. For Z_S=B_S-A_S/2+1/8, conditioning on any specified triple U gives E[A_S|T[U]]=I_U+3/4 and E[B_S|T[U]]=1/4+I_U/2, hence E[Z_S|T[U]]=0, also for smaller intersections. Distinct 4-sets overlap in <=3 vertices, so conditional independence of their nonshared edge variables gives pairwise E[Z_SZ_T]=0, and likewise orthogonality to every triangle indicator. Sum over 4-sets: R_n=Y_n-(n-3)X_n/2+C(n,4)/8; each triangle appears n-3 times. Independent triple cyclic indicators are pairwise uncorrelated even when sharing one edge, giving VarX=3C(n,3)/16. Then Cov(X,Y)=3C(n,4)/8, VarR=3C(n,4)/64, VarY=3(4n-11)C(n,4)/64 and Corr=sqrt[4(n-3)/(4n-11)], for all n>=4. Our independent exact enumeration checked all 64 local tournaments, triple-conditioned zero residual and n=4,5 whole-tournament moments. Pairwise orthogonality is NOT independence.

## originality

PASS

Best-of-knowledge originality: explicit cross-statistic theorem not established by the inspected primary statements; compare four mathematical implications below. No guarantee of absolute historical priority.

## value

PASS

The exact finite-n joint relation between directed triangle and directed four-cycle statistics, together with a per-fourset degenerate residual orthogonal to EACH triangle event, is a structural statistic of uniform random tournament fluctuations. It cleanly explains the asymptotic perfect correlation while quantifying its finite defect and provides an explicit projection/regression primitive beyond known separate means or generic extremal cycle-density inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
