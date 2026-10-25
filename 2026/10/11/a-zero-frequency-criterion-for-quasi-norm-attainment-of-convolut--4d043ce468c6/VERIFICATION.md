---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification of the zero-frequency criterion

The proof concerns infinitely many coordinates. A scalar-norming sequence converges coordinatewise to a single phase because the positive-weight deficit is a sum of nonnegative terms. For each fixed output coordinate, convolution uses a finite coefficient sum, so the corresponding image-limit coordinate is the partial sum of the kernel coefficients multiplied by that phase. The limiting target is \(c_0\); hence the coefficient sum must vanish.

For the converse, the norm-convergent estimate for the finite ramps is

\[
\|W_c u^{(k)}-b\|_\infty\le
\sup_{n>k}|b_n|+\sum_{j\ge0}|c_j|\min\{1,j/k\}\longrightarrow0.
\]

The first term vanishes because \(b\in c_0\). The second vanishes by dominated convergence with the absolutely summable majorant \((|c_j|)\). This proves norm convergence, not merely pointwise convergence. The scalar functional converges to its norm by dominated convergence with weights \((a_n)\).

Every convolution row has coefficient norm \(\sum_{j<n}|c_j|\). If the kernel is infinitely supported, each row norm is strictly less than \(\|c\|_1\), excluding a maximal-norm vector in the norm closure of the convolution ball because a nonzero \(c_0\) vector attains its supremum at a coordinate. For finite support, one late row can be aligned by a finitely supported unit vector.

The exact distance formula is achieved by phase-aligned removal of positive projections of the coefficients. This correction preserves the strict bound \(\|d\|_1<A\), annihilates the total sum, and has \(\ell_1\) norm exactly \(|\sum_jc_j|\). Complex coefficients are treated with a fixed unimodular phase.

Supplemental checks compute exact rational coefficient corrections, floating-point complex corrections, and finite-ramp convolution errors. They do not prove the infinite-dimensional assertions. The results concern the structured fixed-weight family, not all bounded operators.
