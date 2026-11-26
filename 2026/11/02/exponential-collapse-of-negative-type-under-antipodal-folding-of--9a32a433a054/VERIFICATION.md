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

On the zero-sum subspace the discrete distance kernel is −I, and the error of powering it is bounded in quadratic form by N_d(M_d^p−1)||c||², giving the claimed lower bound. The quotient characters have even weight, and summing over all cube vectors counts each quotient class twice. For weight four, orthogonality and the two removed endpoint terms give F_d(0)=−2, including at d=4. The coefficient duality follows by counting choices of overlaps, and the degree-four polynomial follows from the fourth elementary symmetric polynomial in d signs with sum d−2k (Newton's identities). After multiplication by d² the normalized polynomial converges to Z⁴−6Z²+3. The centered log term times √d converges on compact Z-sets to −|Z| and is bounded by 2|Z| for |Z_d|≤√d/2. The binomial subgaussian tails give uniform integrability of the degree-five product there; outside that event the product grows at most polynomially times log d, including the endpoints, against an exponentially small probability. The moments give −(8−12+3)√(2/π)=√(2/π). The absolute coefficient sum is at most 2^d, so at p=(√(2π)+η)d^(5/2)2^(−d) the Taylor remainder is o(1), and the nontrivial eigenvalue is positive for fixed η>0. Downward nesting in p and the all-d lower bound then give the log-rate. The folded exponent is only bounded above with this particular constant, not asymptotically evaluated with that constant. For the unfolded cube, Hamming distance is a sum of cut metrics, and a two-face with alternating coefficients rules out any p>1. Schoenberg gives the Hilbert-snowflake statement. The supplied finite checker was inspected, not run; mpmath is used unconditionally, and the label on the exact checks includes a tolerance-based comparison, so the proof rather than that label establishes the result.

## originality

PASS

The distinct contributions are the weight-four derivative limit and the resulting obstruction for every sufficiently large dimension, including the all-dimension logarithmic collapse. The quotient geometry, finite negative-type machinery, unfolded baseline and generic lower bound are known. A distinct indexed claim obtains the same collapse rate on d divisible by four and a better constant there by a different character; it is credited as a substantive partial overlap. Neither it nor the p=1 and small-dimensional formulas gives the all-dimension weight-four derivative.

## value

PASS

This gives a quantitative example of how taking a natural metric quotient destroys the cube's negative type. It resolves the exponential scale across all dimensions rather than just an infinite subsequence and identifies a particular harmonic obstruction with its constant. It also delineates where a stronger analysis of the globally critical mode is still needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
