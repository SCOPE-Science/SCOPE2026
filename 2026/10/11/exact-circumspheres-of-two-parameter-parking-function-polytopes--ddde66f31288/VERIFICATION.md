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

Hanada–Lentfer–Vindas-Meléndez Prop 3.4 gives vertex layers with k entries 1 and shifted tail lambda_j=a-1+jb. After translation by -1 and symmetry, unique minimax center equals s 1_n with layer distances Q_k(s)=ns^2-2S_k s+T_k; adjacent differences lambda_k(lambda_k-2s) ensure one active layer or two neighbors. D_k=2S_k-n lambda_(k-1) is strictly decreasing with difference -2(a-1)-b(2k+n); first K satisfying D_K<=nb and boundary cases yield claimed center/radius and contacts, accounting for coincident layers k=0,1 at a=1. Independent rational arithmetic tested 576 triples 2<=n<=10,1<=a,b<=8, checking the minmax against ALL breakpoints and stationary candidates and verifying contact adjacency after collapsing equal layers. Classical K_n formula and golden-ratio limit follow exact quadratic inequality; not a numerical asymptotic extrapolation.

## originality

PASS

Compared the exact claim/implications against independently searched Resultary and relevant published mathematical literature. Accepted on best-of-knowledge evidence with explicitly bounded overlap and residual risks; no claim of exhaustive bibliographic novelty.

## value

PASS

The entire natural (a,b,...,b)-parking-function-polytope family gains a closed Euclidean minimum enclosing sphere, support-layer transitions, and a concrete golden-ratio classical limit. Known face/volume formulas do not themselves yield this metric optimization; the general a,b metric classification has use despite overlap with partial permutohedra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
