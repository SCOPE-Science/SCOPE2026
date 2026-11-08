---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each fixed complex dimension d≥1, the radial Toeplitz operator is scalar on degree-n holomorphic polynomials with multiplicity binomial(n+d−1,d−1), eigenvalue E[e^{iG_k^alpha}] for G_k~Gamma(k,1), k=n+d. For 0<alpha<1/2, Gamma concentration controls phase drift O(k^{alpha−1/2}); alpha=1/2 follows delta-method normal fluctuation with damping exp(−1/8). For alpha>1/2, truncate at |G_k−k|≤k^{1/2+epsilon}, use Chernoff outside and repeated nonstationary integration by parts inside, with each derivative gaining k^{−(alpha−1/2−epsilon)}, yielding O(k^−M) for every M. Polynomial degree multiplicity gives all Schatten S_p; alpha≤1/2 is noncompact. For alpha≤1/2, Weyl phase equidistribution of k^alpha mod 2pi (alpha<1) and Abel summation for multiplicities give Haar limit and circle essential spectrum; decay yields {0} above boundary. The alpha=1 exact gamma characteristic function and gamma quadratures at k=20,50,100 separately corroborated the threshold behavior, not the infinite proof.

## originality

PASS

Classical radial Fock diagonalization, alpha=1 exponential phase and critical real-cosine damping are explicitly credited. Esmeral–Maximenko 2015 Example 4.5 produces e^-1/8 cos(sqrt(n)) already; the claimed new conjunction is the full complex unimodular power family and three-way asymptotic/ideal/circular distribution classification in all d. Known general criteria might imply selected compactness consequences but do not explicitly calculate the complete law in inspected statements.

## value

PASS

The exact half-power oscillatory-smoothing transition of a unit-modulus symbol, including all-Schatten compactification in arbitrary fixed complex dimension and the limiting eigenvalue measures, is an independently useful natural phase diagram linking Gaussian concentration to spectral/operator-ideal behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
