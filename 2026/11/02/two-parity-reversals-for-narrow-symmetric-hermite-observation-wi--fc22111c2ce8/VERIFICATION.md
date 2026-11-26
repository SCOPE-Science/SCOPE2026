---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Parity eliminates all even–odd matrix entries. Independently, divide both blocks by the common positive Gaussian mass factor and write m=I2/I0 and s=I4/I0 on the positive window. The odd eigenvalue becomes 2m; the determinant of the normalized even block minus 2m times the identity is (1-2m)(2s-3m), with first diagonal 1-2m. If m<1/2 the even top is larger by its first diagonal. For m>1/2, the determinant and first diagonal show that the even top is below, equal to, or above the odd eigenvalue as s/m is below, equal to, or above 3/2. The two ratios are averages of x^2 under the positive fixed weights exp(-x^2) and x^2 exp(-x^2): each increases strictly as both endpoints translate right (an overlapping window loses strictly lower x and gains strictly higher x). For small width both thresholds are above the ratios at a=epsilon, both are below the ratios at sufficiently large a, and at a=1 the ratios straddle the two thresholds in the required order. At m=1/2 the off-diagonal vanishes and the other even eigenvalue is strictly below the odd one because s/m<3/2. At the upper crossing the first diagonal of the shifted even block is negative and its determinant vanishes, again ruling out a third top mode. The centered-window expansion of the weighted average of x^2 for a weight w is a^2+epsilon^2(2+4a w'(a)/w(a))/6+O(epsilon^4). Both coefficient functions evaluate to -1/3 at their respective squared-center thresholds, where the derivative in squared center at zero width is 1. Analytic implicit functions therefore give both claimed positive shifts and their analytic dependence on epsilon^2. This verifies the global quantifier independently of the numerical samples. VERIFICATION.md records 565 symbolic/numeric assertions; the supplied checker was inspected, not rerun.

## originality

PASS

The distinct result is the uniform exactly-two leading parity switches, their squared-center drifts, and the top multiplicity in the three-mode two-window problem. Parity decomposition and rank-one limiting arguments are standard. The closest records share a motif or observable but not this operator and parameter variation; no stronger claim implying the classification was found in the bounded source comparison.

## value

PASS

The three-mode oscillator is the first Hermite band in which a two-dimensional even sector competes with an independent odd mode. The theorem gives the full moving-center classification of the optimum for symmetric narrow detectors, including the absence of further switches in the far tails. Both leading boundary corrections and the exact dimension at each degeneracy are useful additions to the zero-width limiting comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
