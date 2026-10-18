---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For the half graph H_n with a_i b_j iff i<=j, k>=2, n>=3, the defining inequality for every f(v)<k is f(N[v])>=k+|AN(v)|. Its endpoint leaf-support pairs have disjoint weight L,R>=k; equality L=k forces (a_1,b_1)=(0,k), and R=k forces (a_n,b_n)=(k,0). The submitted nested-neighborhood analysis excludes weight 2k+2 when either pair equals k. Otherwise L=R=k+1 and all interior labels vanish; a_2 and b_(n-1) force precisely f(a_1)=f(b_n)=k+1. This exhibits an admissible function of weight 2(k+1) and proves uniqueness. Independent direct constrained-composition enumeration tested every labeling of weight <=2(k+1) for n=3,4,5 and k=2,3: exactly 65,694 candidate labelings checked, all six instances had one endpoint optimum, no smaller valid label. This finite test is corroboration, not the universal proof.

## originality

PASS

The scalar k=2 value gamma_dR(H_n)=6 is already a consequence of Padamutham and Reddy 2020 (non-complete-bipartite connected chain graphs). The reviewed added fact is rigidity of every k=2 minimum function and the exact bound plus uniqueness for every k>=3. A published 2023 [k]-Roman general bound and 2024/2026 graph-family papers concern broad bounds/other families; from materials actually inspected they do not imply this complete specific optimizer classification. Search is not proof of novelty.

## value

PASS

The half graph is a canonical connected chain graph with two nested leaf-support extremes; exact optimizer rigidity on the whole infinite k,n domain is a motivated structural classification beyond its previously known scalar invariant. The unique optimal defensive configuration can be used as an exact benchmark for studying all minimum [k]-RDFs in ordered bipartite graph families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
