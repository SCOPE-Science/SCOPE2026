---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Pinned RESULT.md uses the exact rank-n orthogonal kernel K(x,y)=Σ(x_i-p_i)(y_i-p_i)/(p_i(1-p_i)); on finite C(Ω), norm is max_x E|K(x,Y)|, attained by choosing input sign of that row. At x_i rare, the individual centered summand U has endpoints -1 and (1-r)/r; at common x_i, V has endpoints -1 and r/(1-r) contained in [minU,maxU]; both have zero mean. Chord convexity proves V≤cx U, and independence lets one replace each common coordinate for convex |S+t|, yielding global rare-corner optimum for arbitrary heterogeneous p_i. At homogeneous p the row is ±(Bin(n,p)-np)/min(p,1-p); binomial telescoping yields 2n max(p,q) C(n-1,floor(np)) p^{floor(np)} q^{n-1-floor(np)}. Local CLT and Poisson convergence prove fixed-bias sqrt n and sparse p=c/n linear boundary; integer c handled by equal adjacent Poisson masses. Independently exact-rational enumerated 308 row assertions including four heterogeneous profiles and homogeneous n≤5. Boundaries n=1, p=1/2 included.

## originality

PASS

Best-of-knowledge published-result and primary-literature implication comparison; concrete matching/overlap and residual risks stated, not a novelty certification.

## value

PASS

Computes a natural, nonminimum L∞ amplification factor of the canonical first Hoeffding/Walsh chaos projector for *unequal* product biases, reducing a 2^n row optimization to one explicit rare corner. The sparse-to-dense scaling transition matters for stability of biased Boolean decompositions. Uniform cube results were known and are not claimed as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
