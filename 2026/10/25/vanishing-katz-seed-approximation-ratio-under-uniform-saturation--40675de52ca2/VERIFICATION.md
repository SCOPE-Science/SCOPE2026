---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

All vertices communicate along the two-cycle, broadcast and return arcs. Write alpha=w/2 and e=epsilon/2. The positive right Perron vector of W/2 has equal leaf coordinates; eliminating three coordinates gives lambda(lambda^2-alpha^2)=k e^2/2, so lambda>alpha. The left side is strictly increasing above alpha, and its value at 1 exceeds k e^2/2 because 1-alpha^2-k e^2/2=1/(4k)-1/(64k^2)-1/(80000k^5)>1/(8k) for k>=4. Thus the outgoing Katz series converges. Solving c=(W/2)(1+c) gives the displayed c_a0 with numerator alpha+alpha^2+e(1+k/2)+k e^2/2<3, hence c_a0<24k. Thus c_leaf=e(1+c_a0)<1 and c_b=k(1+c_leaf)/2<k. Each cycle vertex has score at least the alternating-walk sum alpha/(1-alpha)=8k-1. Every maximizer is therefore a cycle vertex. From either such seed, nonpersistent clipping bounds the cycle mass by 2 at each positive time, b by epsilon and each leaf by epsilon (also at the first step, when the leaves are zero). The discount weights at positive times sum to one. Seed b contributes k/2 at step one alone. Dividing the uniform cycle-seed bound 2+(k+1)epsilon by k/2 gives exactly the claimed upper bound, independent of ties, which tends to zero.

## originality

PASS

The primary source establishes exact Katz optimization at the linear endpoint and explores nonlinear initialization numerically; these results do not establish a worst-case vanishing ratio in the unit-clipped feedback process. The indexed comparators and wider approximation references concern different targets, heuristics or dynamics. No equivalent earlier family was established in the bounded comparison.

## value

PASS

This is a worst-case impossibility for a named linear seed heuristic on a natural nonlinear specialization. Strong connectivity and zero lower threshold remove common degeneracies; convergence rules out failure just from using an undefined resolvent. The construction isolates recurrent reinforcement versus one-step broadcast and proves the effect for every score maximizer, not just a bad tie break or one finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
