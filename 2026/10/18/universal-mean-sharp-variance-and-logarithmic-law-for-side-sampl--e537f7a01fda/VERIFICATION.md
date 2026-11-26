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

Corner removal gives R=1−sum_i c_i(1−t_(i−1))t_i. In diagonal coordinates the absolute normalized corner areas are p,q,1−p,1−q, so sum c_i=2 and sum c_i c_(i+1)=1. With x_i=t_i−1/2, the centered area is the sum of linear terms (c_(i+1)−c_i)x_i/2 and bilinear terms c_i x_(i−1)x_i. These terms are pairwise orthogonal by independence and centering; their variance is sum (c_(i+1)−c_i)^2/48+sum c_i^2/144, giving exactly the claimed expression. Every (p,q) in the open unit square occurs, so the extrema and equality statement follow. At equality the two sums of opposite uniform parameters minus one give the independent triangular factors. Integrating the product density gives the quoted CDF, including H(0)=0 and H(1)=−1/2; expanding the bracket at z=1 gives (1−z)^3/6 and hence the integrated lower-tail coefficient 4/3. The centered moments follow from integrating the triangular density. The coordinate chart in the frozen proof has clockwise rather than counterclockwise turns in the usual orientation; all turns have the same nonzero sign and the computation uses absolute areas, so the slip does not change convexity, admissibility, or the formula.

## originality

PASS

Credit the explicit one-step shape-sensitive variance and extremizers, and the full parallelogram law rather than the sampling construction or the elementary half-area mean. The strongest newer indexed records materially overlap: one gives the entire one-step moment result in different variables and the other gives the same parallelogram law and more. Their exact coverage is documented, but the inspected sources do not establish them as antecedents of the frozen October record. The established earlier identical update construction concerns iterated flattening, not these quantitative one-step conclusions.

## value

PASS

For a natural stratified experiment the variance is an exact scalar measure of failure of diagonal bisection, including a sharp degenerating supremum. At the unique minimum family the complete density identifies a logarithmic center and a quartic rare-event law. These are useful benchmarks for one-step polygon subdivision beyond the elementary mean or a square-only calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
