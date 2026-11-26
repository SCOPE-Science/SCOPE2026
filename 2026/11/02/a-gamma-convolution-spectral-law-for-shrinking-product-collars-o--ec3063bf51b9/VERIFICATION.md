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

At lift degree, multiplying by the symmetric-map Jacobian sends Schur functions to strict alternants with sum of exponents bounded by N+d(d−1)/2. Coordinate angular integration kills every unmatched exponent vector; permutation symmetry gives identical copies in the surviving integrals. The squared radial law is Beta(m+1,p), and the indicator is the stated upper tail of the sum of negative log radii squared. For m/N→u>0 the scaled beta densities converge to the gamma density (pointwise with equal limiting mass), and tightness controls the difference between N(−log R) and N(1−R). Interior convergence is uniform on compact subsets by the sequential criterion and continuity of the gamma profile; lattice boundary strips and the fixed shift of the sum cutoff have negligible normalized count. The ordered simplex is 1/d! of a simplex of volume 1/d!; the strictly decreasing profile along rays removes threshold atoms. The off-critical limits follow by tightness and absence of mass at zero in the interior limit. At small a, uniform control of the exponential gives the two Dirichlet integrals. At large a let v=a u_d and dominate by the Gamma(dp,1) tail; the remaining chamber volume is 1/((d−1)!)². The limiting v integral is E(G−H)_+, which by the Beta(p,p) fraction and Gamma(2p,1) sum is 2·4^(−p)/B(p,p), the stated duplication constant. The bidisc examples give 1/96 and 1/2. The frozen checker and verification notes are supplementary; no supplied scripts were executed.

## originality

PASS

The finite beta-product reduction is a direct use of known quotient and polydisc methods, not an independently novel diagonalization principle. The supported distinct claim is its critical empirical gamma-convolution law, the sharp scale and both evaluated trace-defect endpoints. No equivalent result for these was found in the inspected sources.

## value

PASS

At the natural reciprocal-degree scale the limit is a genuine distribution rather than just a trace bound: it gives threshold counts and quantifies the loss of projection behavior. The two sharp endpoint constants detect different mechanisms, bulk gamma convolution and concentration by the smallest exponent, in a natural quotient finite section.

The dated certificate retains the supplied scientific assessment, sources and limitations.
