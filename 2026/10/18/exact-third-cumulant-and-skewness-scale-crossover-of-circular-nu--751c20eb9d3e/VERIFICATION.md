---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For n>=2 independent uniform points on a circle and 0<s<=1/3, overlap of circular arcs has Y_ij=(s-D_ij)_+. Deterministic expansion gives V_n=ns-n²s²+2 sum_{i<j}Y_ij. Center h_ij=Y_ij-s² is conditionally mean zero in either endpoint. In E(sum h)^3, any three-edge multigraph having a vertex of degree1 vanishes, leaving a triply repeated edge (binomial(n,2) choices) and a triangle (6 binomial(n,3) ordered choices). E[h^3]=s⁴/2-2s⁵+2s⁶; for triangle, integrate quadrant products at s<=1/3: equal-sign contribution 11/30*s⁵ and opposite-sign 11/60*s⁵, totaling 11/20*s⁵; centered triangle E=11/20*s⁵-s⁶. Independent SymPy exact double integrals reproduced 11/30,11/60,11/20; direct algebra with multiplicities gives κ3=2n(n-1)s⁴[(1-2s)²+(n-2)(11s/5-4s²)]. Pair orthogonality gives κ2=(4/3)n(n-1)s³(1-3s/2). The bracket is positive on 0<s<=1/3, and asymptotic substitution yields stated ns->0,τ,∞ constants without asserting a CLT. The s<=1/3 condition excludes positive-measure triple winding, and n=2 removes triangle terms.

## originality

PASS

Aistleitner–Hörmann–Manskova analyze the exact same torus number variance and give expectation/variance plus leading microscopic results, but not third cumulant or full finite-n skewness crossover. Degenerate U-statistic combinatorics is standard, but exact circle triangle integral and resulting all-n third moment are not established by that general framework alone.

## value

PASS

The exact non-Gaussian third cumulant and all-n sign, together with the sharp transition at window width n^-1 between repeated-edge and triangle mechanisms, are natural higher-moment refinements for an actively studied number-variance statistic. This is neither a trivial moment derived from variance nor an arbitrary discrete slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
