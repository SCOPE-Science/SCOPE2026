---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: In C² take T=[[1,1],[0,0]], K=I−T=[[0,−1],[0,1]], C=I, ψ=(−1,1). Exact multiplication gives T²=T, TK=KT=0, R(T)=span{e1} closed, R(TK)={0} complemented. For all x, |<x,ψ>|²=||K*x||²; ψ is Parseval K-frame. Yet Tψ=0 while K*e1=(0,−1) !=0 for e1∈R(T). Therefore transformed family has no positive lower K-frame bound. Published proof uses TT†=P_R(T) as identity on K*C^(1/2)f without membership; K*(R(T))⊂R(T) repairs that step. Independent exact matrix proof.

## originality

PASS

PASS best-of-knowledge: source Thm 3.5 retains erroneous closed-range claim and invalid projection. Related general K-g-fusion transport and an isometry-theorem counterexample concern different hypothesis packages; not an implication of the closed-range oblique-idempotent construction.

## value

PASS

PASS: Genuine sharp logical obstruction to a published structural invariance theorem; exhibits why commuting oblique idempotents do not make their adjoint range invariant. The 2D exact zero-image counterexample is directly useful and identifies a precise natural sufficient repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
