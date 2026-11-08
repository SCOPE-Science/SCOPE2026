---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For the counting-measure symmetric Laplacian and unit metric edges, gradients g_x=f(x)−f(o), z=−k⁻¹Σ_jg_j satisfy T=[[-2a,kb],[a,−(k+1)b]] and fast gradient deviations decay at b. The eigenvalues −α,−β give X(t)=[(β+d)e^(−αt)−(α+d)e^(−βt)]/Δ with d=kb−2a>0. Strict slow-edge domination follows from the exact fast-row absolute sum and the three-exponential comparison J(t)>0 (positivity/Jensen cases), not merely from numeric tests. An all-nonzero slow gradient row forces unique ± three-level ramps; the derivative X′ has one positive zero and the singular limit yields sup=2−1/(k+1), unattained when a>0. Independently exponentiated the full (k+2)×(k+2) Laplacian for four heterogeneous examples; the slow-edge norm matched the formula and strictly exceeded each fast edge.

## originality

PASS

Best-of-knowledge independent search and theorem-level comparison. Kantorovich duality equates a Lipschitz operator norm with a maximal W1 contraction factor; this changes formulation but does not produce the specific two-rate star all-time closed profile, equality cases, or contrast envelope. A general gradient-curvature equivalence/bound is not an equality formula for this particular multi-leaf induced infinity norm. The claimed exact spectral reduction is additional; standard two-point/equal-rate star cases do not imply it for a<b. Under direct specialization of earlier works one can derive general inequalities, but not the strict slow-edge dominance and 2−1/(k+1) envelope without evaluating new matrix row sums and sign regimes. An unsuccessful search alone is not evidence of priority. Actual primary material read and remaining limits below.

## value

PASS

Precisely quantifies a natural and counterintuitive transient gradient amplification from inhomogeneous diffusion on the simplest branched network, identifies the unique spatial bottleneck and every optimizer, and gives a sharp fixed-size contrast limit. This is not routine Markov contraction: weighted-heat maps need not contract the UNWEIGHTED graph-Lipschitz seminorm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
