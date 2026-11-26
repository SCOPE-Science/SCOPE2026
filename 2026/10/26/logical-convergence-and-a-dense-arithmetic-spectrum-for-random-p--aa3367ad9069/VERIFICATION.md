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

On a specified j-label set the path and cycle weights after division by j! are 1 and 1/j, with isolated vertices and loops separate. Distinguishing ordered components gives the exact mixed falling-factorial moments by deleting the distinguished labels and multiplying by the appropriate cycle weights. The requisite coefficient-ratio limit also follows directly: a_n=Σ_k binom(n,k)/k! by counting domain sizes (k is the number of missing domain points). Under these normalized weights E[k²]=n−E[k] by the adjacent-weight identity, and a_(n−1)/a_n=1−E[k]/n tends to one. Fixed shifts follow by telescoping. Mixed factorial moments then converge to those of the independent finite Poisson vector. For any cutoff and any fixed K, the total count of paths dominates the count on K distinct fixed lengths beyond the cutoff, which tends to Poisson(K); taking K arbitrarily large proves cap saturation. For radius r in the directed relational language, every ball in a component longer than 2r+1 is an induced directed path, and every such type occurs in a directed path of size 2r+2. Therefore a representative with the capped short-component counts and t copies of that long path has the correct truncated Hanf summary on the high-probability saturation event. This also supplies an explicit effective algorithm: evaluate the sentence on the representative for each capped Poisson vector, and sum the accepted probabilities. With D=lcm(1,…,2r+1), each mean is a nonnegative integer multiple of 1/D, so these finite sums/products belong to the stated ring. The bounded-length cycle family has exactly the proposed limit by independent Poisson counts; tails of harmonic sums with arbitrarily small successive increments approximate any positive exponent, giving density and nonzero–one behavior. Independent exact checks corroborate the weight identities and the small-radius induced-ball cutoff.

## originality

PASS

The supported distinct claim is the effective arithmetic containment and dense first-order limiting probabilities for the uniform labelled, arbitrary-domain partial-injection relation. Its assembly counts, concentration and effective locality are prior, and conditional small-component laws have substantial prior coverage. The inspected stronger-looking comparisons either concern these inputs without the logical conclusion, or have non-equivalent probability laws/signatures. No direct containment of the arithmetic-and-density result was established in the strongest inspected sources. Bare convergence alone is not credited as distinct.

## value

PASS

This is a natural size-uniform labelled relational ensemble, and the argument connects its component structure to exact effective probabilities for all fixed first-order sentences. The sharp qualitative combination is useful: the attainable values are arithmetically restricted but dense, with an explicit elementary witnessing family. It is not just the numerical failure of a zero–one law for one sentence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
