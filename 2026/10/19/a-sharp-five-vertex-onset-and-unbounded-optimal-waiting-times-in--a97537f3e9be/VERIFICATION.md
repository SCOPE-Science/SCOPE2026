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

Reconstructed the neutral-copying proof in RESULT.md:38–81 and reviewed the evidence in VERIFICATION.md and verify_exact.py without executing the uploaded script. In the final graph the degree-weighted count is a bounded martingale because both edge orientations cancel, and connectivity gives a uniform positive chance of spreading an opinion along a spanning tree in a bounded block, so absorption is almost sure. Uniform single-cooperator initialization makes all first-stage expectations equal, unchanged by any number of copying updates. Adding vertex 2 gives (1/2,1/2,0). Multiplying the path expectation matrix on the constant, antisymmetric end, and symmetric nonconstant vectors gives eigenvalues 1, 2/3 and 1/3, with coefficients 3/8, 1/4 and 1/8 for the record's eigenvectors; contraction against the final degrees and subtracting adjacent g gives the two formulas, including g=0. The five-vertex witness has degrees (3,2,2), total 10 and sign(ΔF)=sign(3−2^g). Independent rational absorption and exact distribution propagation through the edge and path gave F_0=1/4, F_1=4/15, F_2=97/360 and F_3=29/108, and checked the terminal payoff on all 32 configurations. Replay: reproduce_absorbing_chain.py in the private branch evidence for this check. The limit 21/80 and unique g=2 optimum follow from the all-g formula. For at most four vertices two snapshots give a constant and three force sizes 2,3,4; the triangle has one decaying mode. For the path the increment numerator is e0+e2−e1−(e0−e2)2^g, with attachment flags e_i∈{0,1}. Equal end flags make this constant; (1,0) makes it nonpositive including a possible zero at g=0, and (0,1) strictly positive. This excludes a strict interior optimum; constant schedules trivially have weak maximizers everywhere and are not the onset claim. In the pendant-tree family V=4t+6, degrees (t+2,2,t+1), and the sign numerator is 2t+1−2^g. For integer t≥1 the odd threshold is not a power of two, so the first g after the sign switch, ceil(log₂(2t+1)), uniquely maximizes fixation, equal to log₂(N)+O(1).

## originality

PASS

The rule, initial condition, finite-duration setting and basic fixation tools are established. The supported distinct contribution is the strict finite-duration reversal, the sharp five-vertex minimum and the unbounded exact tree optimizer for this growth rule. The most relevant supplement was not available after reasonable lawful attempts; this is a remaining comparison risk, not verified non-coverage or an operational blocker.

## value

PASS

This resolves a natural question raised by monotonic examples: even without a cost of waiting, neutral growth can favor a finite duration over both immediate growth and arbitrarily long waits. Minimality identifies the onset rather than merely exhibiting a reversal, and logarithmically growing exact optima rule out a universal small waiting cutoff even within trees. No claim about selection or unequal stage durations is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
