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

The energy−(−1) gap is four times the combined probability of 000 and 111, so equality requires support on the other six basis states. For any product constituent both probabilities must vanish individually: one site is certainly 0 and a different site certainly 1, leaving at most one unit of total transverse expectation. Convexity forces 3c≤1. Cyclic averaging the product of opposite Z eigenstates and (I+3cX)/2 and averaging under the global bit flip yields exactly the three target marginals and no support outside the ground space. For unrestricted states, the compressed transverse sum is the adjacency of a connected 2-regular six-cycle. Its norm bound follows from 2Re(conjugate(a)b)≤|a|²+|b|² on each edge, with equality at the uniform vector. There are two edges per site flip, while complement symmetry and real amplitudes annul Z and Y. Mixture with the diagonal ground ensemble covers every c through 2/3; none above it is possible. The packaged verification/verify.py was inspected rather than executed and supplements the proof with finite combinatorial and rational checks. Editorial caution: the Finding correctly makes no entanglement-depth claim across the witness interval; do not read the caveat in the Limitations as saying a nongenuine state is possible at c=2/3 itself. Equality there forces the unique uniform ground vector, whose one-site marginals all have rank two, so the pure endpoint is genuinely tripartite.

## originality

PASS

The supported contribution is the paired exact fixed-marginal feasibility boundary, especially the full-separability cutoff on a frustrated complete graph. The angular-momentum matrix element underlying the unrestricted endpoint is standard; the Hamiltonian in SM7 of the motivating paper is the same interaction after rotation and a constant shift at zero field, not an unrelated interaction. Its optimized class is different, however. No inspected statement gives or implies the paired boundary. This is not a priority claim for the collective-spin spectrum, fixed-marginal method or energy witnesses.

## value

PASS

The triangle is the smallest frustrated odd cycle, where a natural bondwise benchmark loses sharpness. The result identifies exactly when routine one-site coherence and the total ground energy cannot coexist in a fully separable state, yet can coexist quantum mechanically. Both endpoints and the full intermediate witness interval are attainable or excluded precisely as appropriate. This is meaningful without a broader lattice theorem or a robustness claim away from exact ground energy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
