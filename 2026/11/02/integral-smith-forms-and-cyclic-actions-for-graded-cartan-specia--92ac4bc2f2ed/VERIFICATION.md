---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n≥1,L≥3,a≥1 set g=gcd(n,L),h=lcm(n,L),D=a^h−1,B=Σ_(j=0)^(L/g−1) a^(nj). The cyclic group-ring cokernel Z[z]/(z^n−1,Σ_(j<L)(az)^j), substituting w=az after showing D=0, is S[w]/(w^g−a^(nu),B(1+...+w^(g−1))) where u(n/g)+v(L/g)=1. The relation B(c−1)=0 makes BN_g(w) a fixed primitive coefficient vector, leaving S^(g−1)⊕S/(B), i.e. SNF 1^(n−g), B,D^(g−1); handles a=1 with D=0 and n=1,g=1. Exact independent Smith tests on representative matrices, including 6,4,2, agreed. Finite test grid is not general proof. The stated P_n action is z=a^(−1)w in S.

## originality

PASS

Earlier weighted Cartan, circulant polynomial and q-Cartan determinant literature directly overlaps determinants and some normal forms. Zhao–Zhang 2020 abstract expressly says diagonalizable and gives same determinant: it could contain an integral SNF derivation. Its full six-page primary text could not be read (authorized institutional attempt returned vpn_disconnected), so the residual priority risk is substantial. Best current scientific comparison distinguishes all-integer specialization and explicit cyclic action, absent from available abstract and other inspected work. This is a qualified PASS, not assertion of total noncoverage.

## value

PASS

The integral torsion invariants and module structure under cyclic permutation are natural invariants for graded Cartan specializations of a standard self-injective representation-theory family, finer than determinant or rational similarity. A closed all-n,L,a formula including singular a=1 and mod-p ranks is useful in exact representation computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
