---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For the canonical unit-weight graph associahedron of K_{p,q} (p≤q, p→∞, n=p+q), support width additivity and the dichromatic connected-subset criterion give exactly 2^{-n}width(z)=H_n(z)-2^{-p}H_q(z_B)-2^{-q}H_p(z_A), H_m(z)=Σ2^{-r}(z_(r)-z_(m+1-r)). Projected Gaussian directions normalized by χ_{n-1} give sphere widths; radial error b_n²/√n→0. Gaussian maxima/minima have independent Poisson extremes and the geometric weights admit a true L1-uniform tail via beta order-statistics, not just fixed K convergence. The two class subtractions reduce to 2^{1-p}b_n at scale 1/b_n; hence b_n(√(n-1)W/2^n-2(1-2^{-p})b_n) converges to Xi_++Xi_-, each Xi=-Σ2^{-r}logΓ_r. The alternate 2b_n centering shifts by -4(log n)/2^p. Gamma-log covariance summation proves the stated mean/variance; a one-sided exponential lower tail shows non-Gaussianity.

## originality

PASS

Best-of-knowledge PASS for the geometric log-log part-size crossover and full non-Gaussian fluctuation law of this canonical K_{p,q} graph associahedron. Gaussian extremal Poisson laws are known methodological ingredients, but known generalized-permutahedron Minkowski structure and graph-associahedron diameter bounds do not imply the exact 2^{-p} subtraction and shift T-4λ. Related stellohedron p=1 formulas lie outside the p→∞ assumption.

## value

PASS

The formula isolates a geometrically meaningful double-scaling phase transition in canonical complete-bipartite graph associahedra: when the smaller part has log₂log n size, the Gaussian directional-width law shifts by a nontrivial deterministic amount. The precise non-Gaussian limiting law and explicit moments resolve information invisible to combinatorial diameters or a leading mean-width estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
