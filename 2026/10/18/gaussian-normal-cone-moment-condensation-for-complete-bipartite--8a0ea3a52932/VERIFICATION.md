---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Reconstructed Gaussian edge-sign fan: positive generators do not alter hyperplane comparisons; iid Gaussian ranks induce uniform permutations. Acyclic orientations of K_{p,q} correspond bijectively to alternating maximal monochrome labeled blocks; each orientation has linear extensions equal to product of block factorials. Summing t-th powers after allocating labeled elements gives the formal generating function. For one large-side B-block, the complete weighted contribution is p!(q!)^t sum_{r=0}^p[r!(p-r)!]^{t-1}. For any b>=2 B blocks, the reciprocal binomial bound sum_{s=1}^{m-1} C(m,s)^-1<=4/m proves R_b(q)<=4^{b-1}(q-b+1)!; since b<=p+1 at fixed p, their total moment mass is a relative O(q^{-(t-1)}). It follows that collision-conditional condensation tends to one, and r-bias, entropy and vanishing unconditional condensation follow by exact normalization. Endpoints r=0,p and integer t>=2 handled; the finite checks are corroborative only.

## originality

PASS

Best-of-knowledge comparison: Iriarte identifies a single orientation’s cone probability with its number of linear extensions over (p+q)!, and graphical-zonotope orientation correspondence is established. Neither his extremal-linear-extension results nor the inspected complete-bipartite ellipsoid/circumsphere results supply the all-order weighted alternating-composition moment identity or the fixed-p condensation and Renyi entropy law. Formal factorial generating functions and higher moments must not be inferred from vertex counts alone; priority in differently indexed combinatorial identities remains a risk.

## value

PASS

Same-vertex exposure collisions are a canonical Euclidean normal-cone statistic of a complete-bipartite graphical zonotope. The exact joint p,q,t identity and the structurally unexpected concentration of high-order mass on 2^p rare orientations explain a genuine entropy–vertex-count separation, not a routine corollary of orientation counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
