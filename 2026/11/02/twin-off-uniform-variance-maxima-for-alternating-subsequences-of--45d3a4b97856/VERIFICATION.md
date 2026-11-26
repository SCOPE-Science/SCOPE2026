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

The down-first convention is essential: each consecutive comparison of a subsequence must use a step with the matching sign in its disjoint index interval. At most one such step can be used in each maximal sign run, and the initial run must be skipped if it ascends. Turning points and the final point, with the initial point added exactly when the first step descends, attain this bound. Under the Mallows law fixing the value sets of disjoint consecutive blocks makes cross-block inversions fixed while the within-block weights factor; the unchanged conditional laws prove independence without conditioning as well. Thus only turning-window lags one and two and the two overlaps with the first descent contribute. Exact descent-word counts on lengths two through five reproduce all six probabilities, the covariance multiplicities n-3 and n-4, and the separately verified V and K rational functions; n=4 is valid and has no lag-two turning pair. For complementary positive q the leading coefficient is reciprocal. Its positive numerator equals (1-q)(1-q^5)+2q^3 up to the positive prefactor, and its limits are zero at the extremes. Differentiation gives the displayed reciprocal degree-ten polynomial; exactly two coefficient sign changes, P(0)=1, P(1)=-25 and positive leading coefficient yield exactly one simple positive root on each side of one. The derivative signs +,-,+,- establish the outlying maxima and the strict local minimum at one. The derivative of 2q/T has the sign of 1-q^2. Independent replay python3 -B /workspace/reproduce_frozen.py 1 checks the symbolic identities and rational root bracket, and exhausts all subsequences of permutations of lengths 4–7, checking exact moments at q=2/5,1,5/2. This does not claim to optimize the full variance at any fixed n.

## originality

PASS

Credit the deterministic representation, the one-window mean ingredients, the uniform moments, and the known Mallows local-dependence machinery. A distinct later catalogue record already implies the exact coefficient V(q) through its peak/valley covariance identities; an isolated discovery of V is not the point of the pass. The retained contribution is the exact finite-size down-first variance including the first-descent boundary correction and the explicit reciprocal off-uniform maximizer classification of the leading coefficient. No located statement covers those conclusions together or reports the extremal classification.

## value

PASS

A natural parameter governing inverse biases controls two different optimizations: the uniform law maximizes the density of the alternating length but is an interior local minimum for its fluctuation coefficient. The exact pair of reciprocal optima gives a structural answer on the full positive half-line, not a comparison of selected q values. The boundary correction also determines exact finite moments for the specified asymmetric orientation. The known uniform values or isolated slope identity are not the reason for a value pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
