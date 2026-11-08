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

Verified the full scope n>=3, every permutation of n once-only Rule 150 updates repeated on a binary cycle. Each update swaps edge differences y_{i-1},y_i; the even-parity edge vector has two vertex anchors. Source/sink conjugations reduce any schedule with k cyclic ascents to two edge rotations of lengths k and m=n-k. Requiring their t-power return and zero anchor cocycle imposes two parity constraints on gcd(k,t)+gcd(m,t) periodic edge-pattern bits. The constraint determinant is n*t/(g*h) mod 2, giving rank 1+epsilon, hence exactly 2^(g+h-epsilon) complete fixed states including both anchor choices. Faithful permutation action on even-parity edge words and the terminal anchor parity prove the stated lcm/twice-lcm order; Eulerian cyclic-ascent counting gives n*A(n-1,k-1). I separately implemented direct vertex scan, bitmatrix nullities, predicted orders, and brute orbit checks for all 870 scan permutations n=3..6 (50,352 state evaluations); all matched. The finite checks corroborate, do not prove the arbitrary-n result. Evidence: Source text in assigned RESULT.md §§Finding, Assumptions and scope, Proof, Verification, Relationship to prior work; repository Git tree 9bac983eb5a27b5c32560e887fb524e1b91331dd

## originality

PASS

Best-of-knowledge novelty of the exact final quantitative claim, with classical proof mechanisms and expressly credited subcases excluded. Genuine broad/theorem and full-text comparison risks retained; inaccessible full texts alone do not dictate failure.

## value

PASS

The question asks for the entire primitive-period census and exact global order of a natural reversible asynchronous binary automaton under *all* one-pass schedules; it reveals genuine k-dependent orbit phases while the one-scan fixed-point count ignores the schedule. Explicit gcd/parity and Eulerian law provide a useful structural classification, not an arbitrary small-instance enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
