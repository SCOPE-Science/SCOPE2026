---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The two complementary projectors reduce the recurrence exactly to the unit constant mode and a scalar mode u_k; the entry criterion is −1/(m−1)≤u_k≤1 and both sets of sums are identically one. For 0<s<1/2 the larger real characteristic root lies below e^(−s), because the characteristic polynomial at e^(−s) is positive and e^(−s) exceeds the smaller root. The resulting positive difference of powers decreases from one; the repeated-root formula at s=1/2 is also positive and decreasing. With D=3+2s>4 the oscillatory formula gives |u_k|≤2^(−k)(1+k/4) for s≤1, using |sin(kθ)|≤k sin θ, and |u_k|<√5·5^(−k/2) for s≥1. These are <1/11 from k=5 and k=4 respectively and give the upper barrier for all k≥2. For k=2 the minimum of s+22e^(−s)−4 is log(22)−3>0. The k=3 interval bounds compare D²−44+11(16−D)e^(−s) to positive quantities (at D=√44 the exponential term is positive); the k=4 numerator intervals give bounds uniformly above −1/11. The source's strict intermediate estimate u₄>−1/64 on [8,32] in D should be non-strict at D=8, where u₄=−1/64; the preceding interval includes that endpoint and the desired barrier is strict even there. Thus this local strictness slip does not affect the proof or claim. At s=3 the positive Taylor sum 131/8<e³ gives u₂(3)<−1/12, so the diagonal is negative for every m≥13. No finite sweep is used to establish the universal barrier.

## originality

PASS

Credit the unconditional all-index entrywise classification on the uniform complete graph with exact start. General BDF2 monotonicity and boundedness theory and the elementary projection argument are prior background. There is material overlapping second-step coverage in the wider weighted-graph catalogue result, which includes a sharp diagonal threshold and the same 13-state witness value; it cannot establish positivity of all entries at later indices. The pass does not credit the k=2 obstruction as a distinct discovery in that comparison.

## value

PASS

An exact semigroup start removes startup discretization error as the explanation for negative probabilities. On the simplest nontrivial complete-graph generator, the sharp finite size boundary specifies when the numerical transition remains genuinely stochastic, even though its row and column sums alone are always one. The positive all-index half is essential: checking the second computed step cannot exclude a later failure. The conclusion is useful as a precise benchmark, not a universal statement about Markov generators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
