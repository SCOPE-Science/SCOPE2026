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

On the cone over K_{m,m} minus a perfect matching, average over simultaneous index permutations and side swaps. A hub edge weight a has 2ma<=1, and the periphery has diagonal 1-a-(m-1)b. The hub contrast has eigenvalue 1-(2m+1)a. On the side contrast and the two zero-sum standard spaces, use the cross block b(11^T-I) to get v=1-a-2(m-1)b, u=1-a-(m-2)b for antisymmetric vectors, and 1-a-mb for symmetric vectors. The identity 2(m-1)u-(m-2)v=m(1-a) bounds SLEM below by t=(2m-1)/(2(3m-4)). Equality forces a=1/(2m), u=t, v=-t. The resulting b=2t/m gives positive peripheral holding, zero hub holding, and remaining nontrivial eigenvalues -1/(2m) and (m-4)t/m of modulus at most t for m>=4. For any optimizer, the averaged kernel is this invariant matrix. The PSD constraints tI-P_g and tI+P_g on 1-perp force every conjugated kernel to agree on the active +t and -t eigenspaces: a PSD quadratic form that vanishes on a vector annihilates it. Time reversal here is matrix symmetry, not an invariance assumption on the optimizer. The +t antisymmetric zero-sum space forces each row and each column of the allowed cross weights to be constant, since the corresponding coefficient vector is orthogonal to the zero-sum space. Distinct rows have a common allowed column, making every cross weight equal; both sides then have a common hub weight. The -t side contrast gives the second equality a+2(m-1)b=1+t and fixes those weights, and row sums fix all diagonals. This certifies uniqueness without assuming graph invariance of P and gives the limit 1/3 directly.

## originality

PASS

The distinct claim is the exact crown-cone result, especially uniqueness over all supported symmetric kernels, not just invariant ones. Later exact catalogue results together recover the value and exhibit the same kernel; those parts are not independent of the broader theorem and base value when these results are available. Their catalogue dates are later, and their statements do not settle the unrestricted optimizer assertion. The literature search is bounded.

## value

PASS

Crown cones naturally combine a hub and a sparsified bipartite core. Their exact optimum makes the two active eigenvalue constraints explicit. The rigidity proof answers a question symmetry reduction leaves open: whether a nonsymmetric assignment of edge weights under graph automorphisms can match the optimal SLEM. This is a structural result for an infinite family, rather than just evaluating a solver or repeating a transfer formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
