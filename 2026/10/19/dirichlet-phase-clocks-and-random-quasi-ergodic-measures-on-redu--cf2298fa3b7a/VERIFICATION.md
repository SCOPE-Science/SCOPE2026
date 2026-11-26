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

Restricting to reachable states makes the block maximum lambda relevant, with at least one critical block reachable and no cycles between components. For a fixed full route of h blocks, the h−1 interblock transitions leave n−h+1 intra-block transitions, so after removing lambda^n the factor is lambda^(−h+1) times the product of normalized kernels and interblock matrices. Each critical kernel equals its positive rank-one projector plus an exponentially small matrix in the residence count. Each subcritical kernel is summable with exponential norm bound, and its sum is precisely (I−A_i/lambda)^(-1). For fixed subcritical counts the number of critical weak compositions has leading factor n^(q−1)/(q−1)!, with q critical blocks. The bounded product error summed over critical counts is O(n^(q−2)) for q>=2; at q=1 it tends to zero for fixed subcritical counts, then by geometric domination over those counts. A route with no critical block has only a polynomial number of terms times exponential decay relative to lambda^n. Each route constant is strictly positive since the L_i have strictly positive entries and the interblock matrices and initial restriction are nonzero. Thus the d-critical routes determine the total survival and route weights. Summable subcritical tails and the O(L/n) fraction of compositions with a critical hold less than fixed L justify using uniform-composition Riemann sums against every bounded continuous test on the simplex; the single-critical case is deterministic. Residence counts of indices differ by one per block from transitions, which does not change the normalized limit. Critical entry times are partial sums of the limiting spacings. Within a critical block, conditional on its endpoints the segment is exactly a bridge of the Perron–Doob kernel: the factor lambda^m r(start)/r(end) telescopes. Its endpoint transition probability is uniformly bounded below at large m by primitivity, so the finite-state ergodic law still holds for bridges, uniformly in endpoints. This proves convergence to the stated nu on each long segment and hence the mixture with an independent Dirichlet vector. At d>=2 the block supports are disjoint and the conditional Dirichlet variances are positive, ruling out convergence to the deterministic mean.

## originality

PASS

The supported addition is the joint distribution of all critical holding fractions and state occupations for the full finite primitive-block model, with exact matrix-resolvent route weights. The scalar-subcritical path asymptotic, polynomial survival factor and occupation means are substantially covered by Colonius–Rasmussen, and the simplex limit there is a natural distributional strengthening using their weak-composition argument. The inspected earlier statements do not give the arbitrary nonscalar subcritical law plus the joint occupation and phase clocks. Terminal conditional convergence and two-phase analogues do not give this multitime statement.

## value

PASS

Even when quasi-ergodic expectations converge, surviving trajectories may randomly allocate a macroscopic fraction of time to each class. The result resolves that ambiguity by giving an explicit route-and-spacings law, including fluctuations and entry times for all routes at once. Matrix-valued detours affect route probabilities even though their time fractions vanish; treating those effects is important beyond scalar examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
